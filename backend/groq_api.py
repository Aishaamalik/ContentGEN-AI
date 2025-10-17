import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def get_llm(temperature=0.7, max_tokens=500):
    """Initialize and return the Groq LLM instance."""
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=temperature,
        max_tokens=max_tokens
    )

def generate_product_description(product_name, category, features, tone="professional"):
    """Generate a product description based on input details."""
    llm = get_llm()

    prompt = f"""
    Generate a compelling product description for the following product:

    Product Name: {product_name}
    Category: {category}
    Key Features: {features}

    Tone: {tone}

    The description should be engaging, highlight the key features, and be suitable for an e-commerce website. Keep it concise but informative.
    """

    response = llm.invoke(prompt)
    return response.content.strip()

def generate_blog_post(topic, tone="informative"):
    """Generate a full blog post based on the given topic."""
    llm = get_llm(max_tokens=1000)

    prompt = f"""
    Write a comprehensive blog post about: {topic}

    Tone: {tone}

    Structure the blog post with:
    1. An engaging introduction
    2. Main body with detailed information and insights
    3. A conclusion with key takeaways

    Make it well-structured, informative, and suitable for an e-commerce blog.
    """

    response = llm.invoke(prompt)
    return response.content.strip()

def generate_promotional_copy(promotion_details, tone="persuasive"):
    """Generate promotional copy for marketing campaigns."""
    llm = get_llm(max_tokens=300)

    prompt = f"""
    Create catchy promotional copy for: {promotion_details}

    Tone: {tone}

    The copy should be engaging, persuasive, and suitable for social media, email campaigns, or ads. Keep it concise and impactful.
    """

    response = llm.invoke(prompt)
    return response.content.strip()
