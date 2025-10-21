import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI/UX with glass effects and animations
st.markdown("""
<style>
    /* CSS Custom Properties (Variables) for consistent theming */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff6b6b;
        --accent-color: #4ecdc4;
        --background-primary: rgba(255, 255, 255, 0.95);
        --background-secondary: rgba(248, 249, 250, 0.8);
        --background-glass: rgba(255, 255, 255, 0.1);
        --text-primary: #2c3e50;
        --text-secondary: #7f8c8d;
        --border-radius: 15px;
        --shadow-light: 0 4px 6px rgba(0, 0, 0, 0.1);
        --shadow-medium: 0 8px 25px rgba(0, 0, 0, 0.15);
        --shadow-heavy: 0 12px 40px rgba(0, 0, 0, 0.2);
        --transition-fast: all 0.3s ease;
        --transition-medium: all 0.5s ease;
        --transition-slow: all 0.8s ease;
    }

    /* Global styles */
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Glass effect containers */
    .glass-container {
        background: var(--background-glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: var(--border-radius);
        box-shadow: var(--shadow-medium);
        transition: var(--transition-fast);
    }

    .glass-container:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-heavy);
    }

    /* Animated headers */
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out;
        background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .sub-header {
        font-size: 1.5rem;
        color: var(--text-secondary);
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInUp 1.2s ease-out;
    }

    /* Enhanced feature cards with glass effects */
    .feature-card {
        background: var(--background-glass);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        padding: 1.5rem;
        border-radius: var(--border-radius);
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: var(--shadow-light);
        transition: var(--transition-medium);
        animation: slideInLeft 0.8s ease-out;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
        animation: shimmer 2s infinite;
    }

    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-heavy);
    }

    .feature-card h4 {
        color: var(--text-primary);
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .feature-card p {
        color: var(--text-secondary);
        line-height: 1.6;
    }

    /* Form styling with glass effects */
    .stForm {
        background: var(--background-glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: var(--border-radius);
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-medium);
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, var(--primary-color), var(--accent-color));
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: var(--transition-fast);
        box-shadow: var(--shadow-light);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-medium);
        background: linear-gradient(45deg, var(--accent-color), var(--secondary-color));
    }

    /* Sidebar styling */
    .css-1d391kg {  /* Sidebar container */
        background: var(--background-glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Content containers */
    .content-container {
        background: var(--background-glass);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: var(--border-radius);
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-light);
        animation: fadeInScale 0.6s ease-out;
    }

    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes fadeInScale {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    @keyframes shimmer {
        0% {
            transform: translateX(-100%);
        }
        100% {
            transform: translateX(100%);
        }
    }

    /* Metric cards */
    .metric-card {
        background: var(--background-glass);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: var(--border-radius);
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: var(--transition-fast);
    }

    .metric-card:hover {
        transform: scale(1.05);
        box-shadow: var(--shadow-medium);
    }

    /* Success and info messages */
    .stSuccess, .stInfo {
        background: var(--background-glass);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: var(--border-radius);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--background-glass);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: var(--border-radius);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Footer styling */
    footer {
        background: var(--background-glass);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: var(--border-radius);
        padding: 1rem;
        text-align: center;
        margin-top: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
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
