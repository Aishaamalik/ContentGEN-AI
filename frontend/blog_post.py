import streamlit as st
import sys
import os

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from backend.groq_api import generate_blog_post
from backend.content_analytics import analyze_content

def show_blog_post():
    st.title("📖 Blog Post Generator")
    st.markdown("Create comprehensive blog posts for your e-commerce website")

    # Input form
    with st.form("blog_form"):
        col1, col2 = st.columns(2)

        with col1:
            blog_topic = st.text_input("Blog Topic", placeholder="e.g., Sustainable Fashion Trends 2024")
            tone = st.selectbox("Tone", ["Informative", "Casual", "Professional", "Engaging"])

        with col2:
            target_audience = st.selectbox("Target Audience",
                                         ["General", "Young Adults", "Families", "Professionals", "Seniors"])
            word_count = st.selectbox("Approximate Word Count", ["500", "750", "1000", "1500"])

        submitted = st.form_submit_button("Generate Blog Post", type="primary")

    if submitted and blog_topic:
        with st.spinner("Generating your blog post..."):
            try:
                # Generate content
                blog_post = generate_blog_post(blog_topic, tone.lower())

                # Store in session state
                st.session_state.generated_blog = blog_post
                st.session_state.blog_topic = blog_topic
                st.session_state.blog_tone = tone

            except Exception as e:
                st.error(f"Error generating blog post: {str(e)}")
                return

    # Display generated content
    if 'generated_blog' in st.session_state:
        st.success("Blog post generated successfully!")

        # Display the blog post in a more presentable format
        st.subheader("📝 Generated Blog Post")

        # Blog info header
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"**Topic:** {st.session_state.blog_topic}")
        with col2:
            st.markdown(f"**Tone:** {st.session_state.blog_tone}")
        with col3:
            word_count = len(st.session_state.generated_blog.split())
            st.markdown(f"**Words:** {word_count}")

        # Formatted blog post in a card-like container
        st.markdown("""
        <div style="
            background-color: #f8f9fa;
            border-left: 4px solid #28a745;
            padding: 20px;
            border-radius: 8px;
            margin: 10px 0;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
        ">
        """, unsafe_allow_html=True)

        # Clean and format the blog post
        blog_content = st.session_state.generated_blog.strip()

        # Split into sections and format
        lines = blog_content.split('\n')
        current_paragraph = []

        for line in lines:
            line = line.strip()
            if not line:
                # Empty line - end current paragraph
                if current_paragraph:
                    paragraph_text = ' '.join(current_paragraph)
                    if paragraph_text:
                        st.markdown(f"<p style='margin-bottom: 15px; text-align: justify;'>{paragraph_text}</p>", unsafe_allow_html=True)
                    current_paragraph = []
                continue

            # Check for titles and section headers in **text**
            if line.startswith('**') and line.endswith('**') and not '**:' in line:
                # End previous paragraph
                if current_paragraph:
                    paragraph_text = ' '.join(current_paragraph)
                    if paragraph_text:
                        st.markdown(f"<p style='margin-bottom: 15px; text-align: justify;'>{paragraph_text}</p>", unsafe_allow_html=True)
                    current_paragraph = []

                # Format header - check if it's a title (usually the first one)
                header_text = line.strip('**')
                if not hasattr(st.session_state, 'title_displayed'):
                    # This is likely the title
                    st.markdown(f"<h2 style='color: #28a745; margin-top: 20px; margin-bottom: 10px; font-weight: bold; text-align: center;'>{header_text}</h2>", unsafe_allow_html=True)
                    st.session_state.title_displayed = True
                else:
                    # Section header
                    st.markdown(f"<h3 style='color: #28a745; margin-top: 20px; margin-bottom: 10px; border-bottom: 2px solid #28a745; padding-bottom: 5px;'>{header_text}</h3>", unsafe_allow_html=True)

            # Check for numbered items like "1. **Item**: description"
            elif line[0].isdigit() and '. **' in line and '**: ' in line:
                # End previous paragraph
                if current_paragraph:
                    paragraph_text = ' '.join(current_paragraph)
                    if paragraph_text:
                        st.markdown(f"<p style='margin-bottom: 15px; text-align: justify;'>{paragraph_text}</p>", unsafe_allow_html=True)
                    current_paragraph = []

                # Extract number, bold part and description
                number_part = line.split('.')[0] + '.'
                remaining = line.split('.', 1)[1].strip()
                if remaining.startswith('**') and '**: ' in remaining:
                    parts = remaining.split('**: ', 1)
                    bold_text = parts[0].strip('**')
                    description = parts[1]
                    st.markdown(f"<div style='margin-bottom: 8px; margin-left: 20px;'><strong>{number_part} {bold_text}:</strong> {description}</div>", unsafe_allow_html=True)

            elif line.startswith('- ') or line.startswith('• '):
                # Handle regular bullet points
                if current_paragraph:
                    paragraph_text = ' '.join(current_paragraph)
                    if paragraph_text:
                        st.markdown(f"<p style='margin-bottom: 15px; text-align: justify;'>{paragraph_text}</p>", unsafe_allow_html=True)
                    current_paragraph = []

                bullet_text = line[2:] if line.startswith('- ') else line[2:]
                st.markdown(f"<div style='margin-bottom: 8px; margin-left: 20px;'>• {bullet_text}</div>", unsafe_allow_html=True)

            elif line.startswith('* '):
                # Handle asterisk bullet points
                if current_paragraph:
                    paragraph_text = ' '.join(current_paragraph)
                    if paragraph_text:
                        st.markdown(f"<p style='margin-bottom: 15px; text-align: justify;'>{paragraph_text}</p>", unsafe_allow_html=True)
                    current_paragraph = []

                bullet_text = line[2:]
                st.markdown(f"<div style='margin-bottom: 8px; margin-left: 20px;'>• {bullet_text}</div>", unsafe_allow_html=True)

            else:
                # Regular paragraph text
                current_paragraph.append(line)

        # Handle any remaining paragraph
        if current_paragraph:
            paragraph_text = ' '.join(current_paragraph)
            if paragraph_text:
                st.markdown(f"<p style='margin-bottom: 15px; text-align: justify;'>{paragraph_text}</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Copy to clipboard button
        if st.button("📋 Copy Blog Post"):
            st.code(st.session_state.generated_blog, language=None)
            st.success("Blog post copied to clipboard!")

        # Analytics section
        with st.expander("📊 Content Analytics"):
            analytics = analyze_content(st.session_state.generated_blog, st.session_state.blog_topic)

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
                             help="Density of topic keywords in content")

            # Word count
            word_count_actual = len(st.session_state.generated_blog.split())
            st.metric("Word Count", word_count_actual)



        # Save content
        if st.button("💾 Save Content", type="secondary"):
            st.success("Content saved successfully!")
            # Here you could save to database

        # Regenerate option
        if st.button("🔄 Regenerate", type="secondary"):
            # Clear previous generation
            for key in ['generated_blog', 'blog_topic', 'blog_tone']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    elif submitted:
        st.warning("Please enter a blog topic")
