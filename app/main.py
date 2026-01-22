"""
Production-Grade Cold Email Generator
A sophisticated AI-powered application for generating personalized cold emails from job postings.
Author: Ishank Mishra
"""

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from typing import List, Dict, Optional
import logging
from datetime import datetime
import time
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ColdEmailApp:
    """
    Enterprise-grade Cold Email Generator Application.
    
    Features:
    - Intelligent job extraction from career pages
    - AI-powered personalized email generation
    - Portfolio matching based on required skills
    - Caching for improved performance
    - Comprehensive error handling and logging
    """
    
    def __init__(self):
        """Initialize the application with required components."""
        self.setup_page_config()
        self.initialize_components()
        
    @staticmethod
    def setup_page_config():
        """Configure Streamlit page settings."""
        st.set_page_config(
            layout="wide",
            page_title="AI Cold Email Generator",
            page_icon="📧",
            initial_sidebar_state="expanded"
        )
        
    @st.cache_resource
    def initialize_components(_self):
        """Initialize and cache LLM chain and portfolio components."""
        try:
            chain = Chain()
            portfolio = Portfolio()
            portfolio.load_portfolio()
            logger.info("Successfully initialized application components")
            return chain, portfolio
        except Exception as e:
            logger.error(f"Failed to initialize components: {str(e)}")
            raise
    
    @staticmethod
    @st.cache_data(ttl=3600, show_spinner=False)
    def load_and_process_url(url: str) -> Optional[str]:
        """
        Load and process content from URL with caching.
        
        Args:
            url: The URL to scrape and process
            
        Returns:
            Cleaned text content or None if failed
        """
        try:
            logger.info(f"Loading URL: {url}")
            loader = WebBaseLoader([url])
            page_data = loader.load()
            
            if not page_data:
                logger.warning(f"No data loaded from URL: {url}")
                return None
                
            raw_content = page_data[0].page_content
            cleaned_content = clean_text(raw_content)
            logger.info(f"Successfully processed URL: {url}")
            return cleaned_content
            
        except Exception as e:
            logger.error(f"Error loading URL {url}: {str(e)}")
            return None
    
    def render_sidebar(self):
        """Render application sidebar with information and controls."""
        with st.sidebar:
            st.header("ℹ️ About")
            st.markdown("""
            **AI Cold Email Generator** uses advanced LLMs to:
            
            - 🔍 Extract job requirements from career pages
            - 🤖 Generate personalized cold emails
            - 🎯 Match relevant portfolio projects
            - ⚡ Deliver results in seconds
            
            ---
            
            **Tech Stack:**
            - LangChain + Ollama/Groq
            - Streamlit
            - Vector Embeddings
            - Web Scraping
            """)
            
            st.header("📊 Statistics")
            if 'generated_count' not in st.session_state:
                st.session_state.generated_count = 0
            
            st.metric("Emails Generated", st.session_state.generated_count)
            
            st.header("⚙️ Settings")
            st.session_state.show_raw_data = st.checkbox("Show Raw Data", value=False)
            st.session_state.show_extraction = st.checkbox("Show Job Extraction", value=False)
            
            st.markdown("---")
            st.markdown("**Developed by:** Ishank Mishra")
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/yourusername)")
    
    def render_main_interface(self, chain: Chain, portfolio: Portfolio):
        """
        Render the main application interface.
        
        Args:
            chain: Initialized Chain object for LLM operations
            portfolio: Initialized Portfolio object for skill matching
        """
        # Header
        st.title("📧 AI-Powered Cold Email Generator")
        st.markdown("""
        Generate compelling, personalized cold emails from job postings using AI.
        Perfect for business development, sales outreach, and recruitment.
        """)
        
        # Input section
        col1, col2 = st.columns([3, 1])
        
        with col1:
            url_input = st.text_input(
                "🔗 Enter Job Posting URL",
                value="https://jobs.nike.com/job/R-33460",
                placeholder="https://company.com/careers/job-posting",
                help="Paste the URL of any job posting or career page"
            )
        
        with col2:
            st.write("")  # Spacing
            st.write("")  # Spacing
            submit_button = st.button("🚀 Generate Email", type="primary", use_container_width=True)
        
        # Example URLs
        with st.expander("📌 Example URLs"):
            example_urls = [
                "https://jobs.nike.com/job/R-33460",
                "https://www.google.com/about/careers/applications/",
                "https://careers.microsoft.com/",
            ]
            for url in example_urls:
                st.code(url, language=None)
        
        # Processing section
        if submit_button:
            if not url_input or not url_input.startswith(('http://', 'https://')):
                st.error("⚠️ Please enter a valid URL starting with http:// or https://")
                return
            
            self.process_url(url_input, chain, portfolio)
    
    def process_url(self, url: str, chain: Chain, portfolio: Portfolio):
        """
        Process URL and generate cold emails.
        
        Args:
            url: Job posting URL to process
            chain: Chain object for LLM operations
            portfolio: Portfolio object for skill matching
        """
        try:
            # Step 1: Load and process URL
            with st.spinner("🔄 Loading and analyzing job posting..."):
                progress_bar = st.progress(0)
                
                cleaned_data = self.load_and_process_url(url)
                progress_bar.progress(33)
                
                if not cleaned_data:
                    st.error("❌ Failed to load content from URL. Please check the URL and try again.")
                    return
                
                # Show raw data if enabled
                if st.session_state.get('show_raw_data', False):
                    with st.expander("📄 Raw Scraped Data"):
                        st.text_area("Content", cleaned_data, height=200)
                
                # Step 2: Extract jobs
                st.info("🔍 Extracting job information...")
                progress_bar.progress(66)
                
                jobs = chain.extract_jobs(cleaned_data)
                
                if not jobs:
                    st.warning("⚠️ No job postings found on this page. Try a different URL.")
                    return
                
                progress_bar.progress(100)
                time.sleep(0.3)
                progress_bar.empty()
            
            # Step 3: Display results
            st.success(f"✅ Found {len(jobs)} job posting(s)!")
            
            # Show extraction details if enabled
            if st.session_state.get('show_extraction', False):
                with st.expander("🔍 Extracted Job Details"):
                    for idx, job in enumerate(jobs, 1):
                        st.json(job)
            
            # Step 4: Generate emails
            st.divider()
            st.subheader("📨 Generated Cold Emails")
            
            for idx, job in enumerate(jobs, 1):
                with st.container():
                    # Job header
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"### Email {idx}: {job.get('role', 'Position')}")
                    with col2:
                        exp = job.get('experience', 'N/A')
                        st.metric("Experience", exp)
                    
                    # Skills tags
                    skills = job.get('skills', [])
                    if skills:
                        st.markdown("**Required Skills:**")
                        skill_cols = st.columns(min(len(skills), 5))
                        for i, skill in enumerate(skills[:5]):
                            with skill_cols[i]:
                                st.markdown(f"`{skill}`")
                    
                    # Generate email with loading
                    with st.spinner(f"✍️ Generating personalized email {idx}..."):
                        links = portfolio.query_links(skills)
                        email = chain.write_mail(job, links)
                    
                    # Display email
                    st.markdown("**Generated Email:**")
                    st.code(email, language='markdown')
                    
                    # Action buttons
                    col1, col2, col3 = st.columns([1, 1, 4])
                    with col1:
                        st.download_button(
                            label="📥 Download",
                            data=email,
                            file_name=f"cold_email_{idx}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain"
                        )
                    with col2:
                        if st.button(f"📋 Copy", key=f"copy_{idx}"):
                            st.toast("Email copied to clipboard!", icon="✅")
                    
                    st.divider()
            
            # Update statistics
            st.session_state.generated_count += len(jobs)
            
            # Success message
            st.balloons()
            st.success(f"🎉 Successfully generated {len(jobs)} personalized email(s)!")
            
        except Exception as e:
            logger.error(f"Error processing URL: {str(e)}", exc_info=True)
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("💡 Try a different URL or check your internet connection.")
    
    def run(self):
        """Main application entry point."""
        try:
            # Initialize components
            chain, portfolio = self.initialize_components()
            
            # Render UI
            self.render_sidebar()
            self.render_main_interface(chain, portfolio)
            
            # Footer
            st.markdown("---")
            st.markdown("""
            <div style='text-align: center'>
                <p>Built with ❤️ using LangChain, Ollama, and Streamlit | 
                <a href='https://github.com/ishank-2301' target='_blank'>GitHub</a> | 
                <a href='https://linkedin.com/in/ishank-mishra-5689842a1' target='_blank'>LinkedIn</a>
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            logger.critical(f"Critical error in application: {str(e)}", exc_info=True)
            st.error("💥 Application failed to initialize. Please check logs and restart.")


def main():
    """Application entry point."""
    app = ColdEmailApp()
    app.run()


if __name__ == "__main__":
    main()