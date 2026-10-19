import streamlit as st
from PIL import Image
from google import genai

# Page configuration
st.set_page_config(
    page_title="LabelLens - Ingredient Safety Advisor",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS styling for a modern look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        background-color: #7c3aed;
        color: white;
    }
    .stButton>button:hover {
        background-color: #6d28d9;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🔍 LabelLens")
st.subheader("AI-Powered Ingredient Safety & Health Advisor")
st.write("Instantly analyze product ingredient labels for health risks, toxins, and allergens.")

# Sidebar for controls & uploads
with st.sidebar:
    st.header("⚙️ Controls")
    uploaded_file = st.file_uploader("Upload product label", type=["jpg", "jpeg", "png"])
    
    st.markdown("---")
    st.info("💡 **Tip:** Take a clear photo of the ingredients list on the back of the package for best results.")

# Main Display Area
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(image, caption="Uploaded Label", use_container_width=True)
    
    if st.button("🚀 Analyze Ingredients", type="primary"):
        with st.spinner("Analyzing ingredients with Gemini AI..."):
            try:
                # Initialize Gemini Client
                client = genai.Client()
                
                prompt = (
                    "Analyze this product ingredient label image. "
                    "1. List Potential Allergens Detected (Milk, Wheat, Soy, Nuts, Corn, etc.). "
                    "2. List Safe or Natural Ingredients. "
                    "3. Identify any harmful additives or toxins. "
                    "Keep the formatting clean with bullet points and bold titles."
                )
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[image, prompt]
                )
                
                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.warning("👈 Please upload a label image using the sidebar to begin analysis.")