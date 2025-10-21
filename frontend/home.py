import streamlit as st

def show_home():
    st.markdown('<h1 class="main-header">✨ AI-Powered Content Generation</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Generate high-quality content for your e-commerce business with AI</p>', unsafe_allow_html=True)

    # Overview section with glass effect
    st.markdown("""
    <div class="content-container">
    <h2 style="color: var(--primary-color); margin-bottom: 1rem;">🚀 What is this app?</h2>
    <p style="color: var(--text-primary); line-height: 1.6; font-size: 1.1rem;">
    This AI-powered platform helps e-commerce businesses create compelling content automatically using advanced AI technology.
    Generate product descriptions, blog posts, and promotional copy with just a few clicks!
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Features section
    st.markdown('<h2 style="color: var(--primary-color); text-align: center; margin: 2rem 0 1rem 0; animation: fadeInUp 1.4s ease-out;">🎯 Key Features</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card" style="height: 200px;">
        <h4>📝 Product Descriptions</h4>
        <p>Generate professional product descriptions by providing basic details like name, category, and key features.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card" style="height: 200px;">
        <h4>📖 Blog Posts</h4>
        <p>Create comprehensive blog posts on any topic related to your products or industry.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card" style="height: 200px;">
        <h4>📢 Promotional Copy</h4>
        <p>Craft engaging promotional content for social media, emails, and advertising campaigns.</p>
        </div>
        """, unsafe_allow_html=True)

    # Additional features with glass container
    st.markdown("""
    <div class="content-container">
    <h2 style="color: var(--primary-color); margin-bottom: 1.5rem;">🔧 Advanced Features</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
    """, unsafe_allow_html=True)

    features = [
        ("🎨 Content Personalization", "Choose from different tones (Casual, Formal, Persuasive)"),
        ("📊 Content Analytics", "Get SEO insights, readability scores, and sentiment analysis"),
        ("💾 Save & Reuse", "Store your favorite content for future use"),
        ("🎯 Target Audience", "Customize content for specific demographics")
    ]

    for icon_text, description in features:
        st.markdown(f"""
        <div class="glass-container" style="padding: 1rem; margin-bottom: 0.5rem;">
        <div style="color: var(--text-primary); font-weight: 600; margin-bottom: 0.5rem;">{icon_text}</div>
        <div style="color: var(--text-secondary);">{description}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # How to use section with glass effect
    st.markdown("""
    <div class="content-container">
    <h2 style="color: var(--primary-color); margin-bottom: 1.5rem;">📋 How to Use</h2>
    <div style="background: var(--background-glass); backdrop-filter: blur(10px); border-radius: var(--border-radius); padding: 1.5rem; border: 1px solid rgba(255, 255, 255, 0.2);">
    """, unsafe_allow_html=True)

    steps = [
        ("1. Navigate", "Use the sidebar to select the type of content you want to generate"),
        ("2. Input Details", "Fill in the required fields for your content type"),
        ("3. Customize", "Choose your preferred tone and target audience"),
        ("4. Generate", "Click the generate button to create your content"),
        ("5. Analyze", "Review the analytics and make adjustments if needed"),
        ("6. Save", "Store your content for future reference")
    ]

    for step_title, step_desc in steps:
        st.markdown(f"""
        <div style="display: flex; align-items: flex-start; margin-bottom: 1rem; animation: slideInLeft 0.8s ease-out;">
        <div style="background: linear-gradient(45deg, var(--primary-color), var(--accent-color)); color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem; flex-shrink: 0;">{step_title.split('.')[0]}</div>
        <div>
        <div style="color: var(--text-primary); font-weight: 600; margin-bottom: 0.25rem;">{step_title}</div>
        <div style="color: var(--text-secondary);">{step_desc}</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # Getting started button with enhanced styling
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Get Started", type="primary", use_container_width=True):
            st.session_state.selected = "Product Description"
            st.rerun()
