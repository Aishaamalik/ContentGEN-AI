import streamlit as st
import sys
import os

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.groq_api import generate_promotional_copy
from backend.content_analytics import analyze_content

def show_promotional_copy():
    st.title("📢 Promotional Copy Generator")
    st.markdown("Create engaging promotional content for your marketing campaigns")

    # Input form with glass effect
    st.markdown("""
    <div class="content-container">
    <h3 style="color: var(--primary-color); margin-bottom: 1rem;">📝 Enter Promotion Details</h3>
    </div>
    """, unsafe_allow_html=True)

    with st.form("promo_form"):
        col1, col2 = st.columns(2)

        with col1:
            promotion_details = st.text_input("Promotion Details",
                                            placeholder="e.g., 20% off on all jackets")
            tone = st.selectbox("Tone", ["Persuasive", "Casual", "Urgent", "Friendly"])

        with col2:
            platform = st.selectbox("Platform",
                                  ["Social Media", "Email", "Website Banner", "SMS", "Print Ad"])
            target_audience = st.selectbox("Target Audience",
                                         ["General", "Young Adults", "Families", "Professionals", "Seniors"])

        submitted = st.form_submit_button("✨ Generate Promotional Copy", type="primary")

    if submitted and promotion_details:
        with st.spinner("Generating your promotional copy..."):
            try:
                # Generate content
                promo_copy = generate_promotional_copy(promotion_details, tone.lower())

                # Store in session state
                st.session_state.generated_promo = promo_copy
                st.session_state.promotion_details = promotion_details
                st.session_state.promo_tone = tone
                st.session_state.platform = platform

            except Exception as e:
                st.error(f"Error generating promotional copy: {str(e)}")
                return

    # Display generated content
    if 'generated_promo' in st.session_state:
        st.success("Promotional copy generated successfully!")

        # Display the promotional copy in a more presentable format
        st.subheader("📢 Generated Promotional Copy")

        # Promo info header
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"**Promotion:** {st.session_state.promotion_details}")
        with col2:
            st.markdown(f"**Tone:** {st.session_state.promo_tone}")
        with col3:
            st.markdown(f"**Platform:** {st.session_state.platform}")


        # Formatted promotional copy in a glass effect container
        st.markdown("""
        <div class="content-container" style="animation: fadeInScale 0.8s ease-out;">
        <div style="
            background: var(--background-glass);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-left: 4px solid var(--secondary-color);
            padding: 20px;
            border-radius: var(--border-radius);
            font-size: 18px;
            line-height: 1.6;
            color: var(--text-primary);
            text-align: center;
            font-weight: bold;
            box-shadow: var(--shadow-light);
        ">
        """, unsafe_allow_html=True)
        # Clean and format the promotional copy
        promo_content = st.session_state.generated_promo.strip()

        # Replace markdown-style formatting with HTML
        promo_content = promo_content.replace('**', '<strong>', 1)
        while '**' in promo_content:
            promo_content = promo_content.replace('**', '</strong>', 1)

        # Handle different formats - could be single line or multi-line
        if '\n' in promo_content:
            # Multi-line format
            lines = promo_content.split('\n')
            for line in lines:
                line = line.strip()
                if line:
                    st.markdown(f"<div style='margin-bottom: 10px;'>{line}</div>", unsafe_allow_html=True)
        else:
            # Single line format
            st.markdown(f"<div>{promo_content}</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Copy to clipboard button
        if st.button("📋 Copy Promotional Copy"):
            st.code(st.session_state.generated_promo, language=None)
            st.success("Promotional copy copied to clipboard!")

        # Platform-specific suggestions
        if st.session_state.platform == "Social Media":
            st.info("💡 **Social Media Tip**: Keep it under 125 characters for better engagement")
        elif st.session_state.platform == "SMS":
            st.info("💡 **SMS Tip**: Keep it under 160 characters to avoid splitting")
        elif st.session_state.platform == "Email":
            st.info("💡 **Email Tip**: Include a clear call-to-action")

        # Analytics section with enhanced styling
        with st.expander("📊 Content Analytics"):
            analytics = analyze_content(st.session_state.generated_promo, st.session_state.promotion_details.split()[0])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("""
                <div class="metric-card">
                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 0.5rem;">Readability Score</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--primary-color);">{}/100</div>
                <div style="font-size: 0.8rem; color: var(--text-secondary);">Level: {}</div>
                </div>
                """.format(analytics['readability']['score'], analytics['readability']['level']), unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div class="metric-card">
                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 0.5rem;">Sentiment</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--accent-color);">{}</div>
                <div style="font-size: 0.8rem; color: var(--text-secondary);">Score: {:.3f}</div>
                </div>
                """.format(analytics['sentiment']['sentiment'], analytics['sentiment']['compound_score']), unsafe_allow_html=True)

            with col3:
                char_count = len(st.session_state.generated_promo)
                st.markdown("""
                <div class="metric-card">
                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 0.5rem;">Character Count</div>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--secondary-color);">{:,}</div>
                <div style="font-size: 0.8rem; color: var(--text-secondary);">Total characters</div>
                </div>
                """.format(char_count), unsafe_allow_html=True)



        # Save content
        if st.button("💾 Save Content", type="secondary"):
            st.success("Content saved successfully!")
            # Here you could save to database

        # Regenerate option
        if st.button("🔄 Regenerate", type="secondary"):
            # Clear previous generation
            for key in ['generated_promo', 'promotion_details', 'promo_tone', 'platform']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    elif submitted:
        st.warning("Please enter promotion details")
