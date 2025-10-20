import streamlit as st

def show_home():
    st.markdown('<h1 class="main-header">✨ AI-Powered Content Generation</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Generate high-quality content for your e-commerce business with AI</p>', unsafe_allow_html=True)

    # Overview section
    st.header("🚀 What is this app?")
    st.write("""
    This AI-powered platform helps e-commerce businesses create compelling content automatically using advanced AI technology.
    Generate product descriptions, blog posts, and promotional copy with just a few clicks!
    """)

    # Features section
    st.header("🎯 Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <h4>📝 Product Descriptions</h4>
        <p>Generate professional product descriptions by providing basic details like name, category, and key features.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <h4>📖 Blog Posts</h4>
        <p>Create comprehensive blog posts on any topic related to your products or industry.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <h4>📢 Promotional Copy</h4>
        <p>Craft engaging promotional content for social media, emails, and advertising campaigns.</p>
        </div>
        """, unsafe_allow_html=True)

    # Additional features
    st.header("🔧 Advanced Features")

    features = [
        "🎨 **Content Personalization**: Choose from different tones (Casual, Formal, Persuasive)",
        "📊 **Content Analytics**: Get SEO insights, readability scores, and sentiment analysis",
        "⭐ **User Feedback**: Rate generated content and provide feedback for improvements",
        "💾 **Save & Reuse**: Store your favorite content for future use",
        "🎯 **Target Audience**: Customize content for specific demographics"
    ]

    for feature in features:
        st.markdown(f"- {feature}")

    # How to use section
    st.header("📋 How to Use")
    st.write("""
    1. **Navigate**: Use the sidebar to select the type of content you want to generate
    2. **Input Details**: Fill in the required fields for your content type
    3. **Customize**: Choose your preferred tone and target audience
    4. **Generate**: Click the generate button to create your content
    5. **Analyze**: Review the analytics and make adjustments if needed
    6. **Save**: Store your content for future reference
    """)

    # Getting started button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Get Started", type="primary", use_container_width=True):
            st.session_state.selected = "Product Description"
            st.rerun()
