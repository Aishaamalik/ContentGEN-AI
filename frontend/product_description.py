import streamlit as st
import sys
import os

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.groq_api import generate_product_description
from backend.content_analytics import analyze_content

def show_product_description():
    st.title("📝 Product Description Generator")
    st.markdown("Generate compelling product descriptions for your e-commerce store")

    # Input form
    with st.form("product_form"):
        col1, col2 = st.columns(2)

        with col1:
            product_name = st.text_input("Product Name", placeholder="e.g., Wireless Bluetooth Headphones")
            category = st.selectbox("Product Category",
                                  ["Electronics", "Fashion", "Home & Garden", "Sports", "Books", "Beauty", "Other"])

        with col2:
            tone = st.selectbox("Tone", ["Professional", "Casual", "Persuasive", "Friendly"])
            target_audience = st.selectbox("Target Audience",
                                         ["General", "Young Adults", "Families", "Professionals", "Seniors"])

        features = st.text_area("Key Features (comma-separated)",
                               placeholder="e.g., noise cancellation, 30-hour battery, comfortable fit",
                               height=100)

        submitted = st.form_submit_button("Generate Description", type="primary")

    if submitted and product_name and features:
        with st.spinner("Generating your product description..."):
            try:
                # Generate content
                description = generate_product_description(product_name, category, features, tone.lower())

                # Store in session state
                st.session_state.generated_description = description
                st.session_state.product_name = product_name
                st.session_state.category = category
                st.session_state.features = features
                st.session_state.tone = tone

            except Exception as e:
                st.error(f"Error generating description: {str(e)}")
                return

    # Display generated content
    if 'generated_description' in st.session_state:
        st.success("Description generated successfully!")

        # Display the description in a more presentable format
        st.subheader("📦 Generated Product Description")

        # Product info header
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"**Product:** {st.session_state.product_name}")
        with col2:
            st.markdown(f"**Category:** {st.session_state.category}")
        with col3:
            st.markdown(f"**Tone:** {st.session_state.tone}")

        # Formatted description in a card-like container
        st.markdown("""
        <div style="
            background-color: #f8f9fa;
            border-left: 4px solid #007bff;
            padding: 20px;
            border-radius: 8px;
            margin: 10px 0;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        ">
        """, unsafe_allow_html=True)

        # Clean and format the description
        description = st.session_state.generated_description.strip()

        # Replace markdown-style formatting with HTML
        description = description.replace('**', '<strong>', 1)
        while '**' in description:
            description = description.replace('**', '</strong>', 1)

        # Handle bullet points
        description = description.replace('- **', '• <strong>')
        description = description.replace('**:', '</strong>:')

        # Split into lines and format
        lines = description.split('\n')
        for line in lines:
            line = line.strip()
            if line:
                if line.startswith('•'):
                    st.markdown(f"<p style='margin-bottom: 10px; margin-left: 20px;'>{line}</p>", unsafe_allow_html=True)
                elif line.startswith('**') and line.endswith('**'):
                    st.markdown(f"<h4 style='margin-bottom: 10px; color: #007bff;'>{line.strip('**')}</h4>", unsafe_allow_html=True)
                elif '**' in line:
                    # Handle mixed content
                    st.markdown(f"<p style='margin-bottom: 10px;'>{line}</p>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<p style='margin-bottom: 15px;'>{line}</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Copy to clipboard button
        if st.button("📋 Copy Description"):
            st.code(st.session_state.generated_description, language=None)
            st.success("Description copied to clipboard!")

        # Analytics section
        with st.expander("📊 Content Analytics"):
            analytics = analyze_content(st.session_state.generated_description, st.session_state.product_name)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Readability Score",
                         f"{analytics['readability']['score']}/100",
                         help=f"Level: {analytics['readability']['level']}")

            with col2:
                st.metric("Sentiment",
                         analytics['sentiment']['sentiment'],
                         help=f"Compound Score: {analytics['sentiment']['compound_score']}")

            with col3:
                if 'keyword_density' in analytics:
                    st.metric("Keyword Density",
                             f"{analytics['keyword_density']}%",
                             help="Density of product name in description")

            # Detailed analytics
            st.subheader("Detailed Analysis")
            st.json(analytics)

        # Feedback section
        st.subheader("⭐ Rate this Content")
        col1, col2 = st.columns([3, 1])

        with col1:
            rating = st.slider("Rating (1-5)", 1, 5, 3)
            feedback = st.text_area("Additional Feedback (optional)", height=80)

        with col2:
            if st.button("Submit Feedback", use_container_width=True):
                st.success("Thank you for your feedback!")
                # Here you could save feedback to database

        # Save content
        if st.button("💾 Save Content", type="secondary"):
            st.success("Content saved successfully!")
            # Here you could save to database

        # Regenerate option
        if st.button("🔄 Regenerate", type="secondary"):
            # Clear previous generation
            for key in ['generated_description', 'product_name', 'category', 'features', 'tone']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    elif submitted:
        st.warning("Please fill in all required fields (Product Name and Key Features)")
