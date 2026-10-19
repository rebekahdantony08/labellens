import streamlit as st
from google import genai
from PIL import Image

# Page Configuration
st.set_page_config(page_title="LabelLens", page_icon="🔍", layout="centered")

st.title("🔍 LabelLens — Ingredient Safety Advisor")
st.write("Instantly analyze product ingredient labels for health risks, toxins, and allergens.")

# Sidebar for API Key input
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("**How to use:**\n1. Enter your Gemini API Key.\n2. Upload a photo of an ingredient label.\n3. Click Analyze!")

# Main File Uploader
uploaded_file = st.file_uploader("Upload product label image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Label", use_column_width=True)
    
    if st.button("🚀 Analyze Ingredients"):
        if not api_key:
            st.error("⚠️ Please enter your Gemini API Key in the sidebar first!")
        else:
            with st.spinner("Analyzing product label with AI..."):
                try:
                    # Initialize Gemini Client
                    client = genai.Client(api_key=api_key)
                    
                    # Structured Prompt for the AI
                    prompt = """
                    Analyze this product ingredient label image. 
                    Provide your response in clear markdown with these exact sections:
                    ### 📊 Overall Safety Score
                    (Give a score out of 100 and a rating like Safe / Moderate Caution / High Risk)
                    
                    ### ⚠️ Flagged / Harmful Ingredients
                    (List any toxins, harsh chemicals, or questionable preservatives with a 1-sentence explanation each)
                    
                    ### 🌾 Potential Allergens Detected
                    (Check for gluten, dairy, nuts, soy, parabens, etc.)
                    
                    ### ✅ Safe Ingredients
                    (List the safe or natural components found)
                    """
                    
                    # Generate response using Gemini 2.5 Flash
                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=[image, prompt]
                    )
                    
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
