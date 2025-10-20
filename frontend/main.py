import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
        color: #000000;
    }
    .feature-card h4 {
        color: #000000;
    }
    .feature-card p {
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("🧠 AI Content Generator")
    st.markdown("---")

    if 'selected' not in st.session_state:
        st.session_state.selected = "Home"

    options = ["Home", "Product Description", "Blog Post", "Promotional Copy"]
    selected = option_menu(
        menu_title=None,
        options=options,
        icons=["house", "box", "book", "megaphone"],
        default_index=options.index(st.session_state.selected),
    )
    st.session_state.selected = selected

# Main content based on selection
if selected == "Home":
    from home import show_home
    show_home()
elif selected == "Product Description":
    from product_description import show_product_description
    show_product_description()
elif selected == "Blog Post":
    from blog_post import show_blog_post
    show_blog_post()
elif selected == "Promotional Copy":
    from promotional_copy import show_promotional_copy
    show_promotional_copy()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Groq AI")
