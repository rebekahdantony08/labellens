import streamlit as st
from PIL import Image
from google import genai

# 1. Page Setup
st.set_page_config(
    page_title="LabelLens AI", 
    page_icon="🔍", 
    layout="wide"
)

st.title("🔍 LabelLens AI")
st.write("Next-Generation Visual AI Ingredient Safety & Health Advisor")

# 2. Sidebar File Uploader
st.sidebar.markdown("### ⚙️ Scanner & Settings")
uploaded_file = st.sidebar.file_uploader("Upload Product Label", type=["jpg", "jpeg", "png", "webp"])

# 3. Securely Load Gemini Client using Streamlit Secrets
@st.cache_resource
def init_gemini():
    # This automatically reads the key you saved in Streamlit Cloud Secrets!
    api_key = st.secrets["GEMINI_API_KEY"]
    return genai.Client(api_key=api_key)

# 4. Main App Logic
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("#### 📸 Label Preview")
        st.image(image, use_container_width=True)
        analyze_btn = st.button("⚡ Run AI Safety Analysis", type="primary")
        
    with col2:
        st.markdown("#### 📊 Analysis Results")
        if analyze_btn:
            with st.spinner("🔍 Reading ingredients with Gemini AI..."):
                try:
                    client = init_gemini()
                    
                    prompt = (
                        "Analyze this product ingredient label image:\n"
                        "1. Safety Score (0-100) and Rating (Safe / Caution / High Risk)\n"
                        "2. Harmful or High-Risk Additives / E-numbers\n"
                        "3. Potential Allergens\n"
                        "4. Safe/Beneficial Ingredients\n"
                        "Use clear bullet points, emojis, and bold terms."
                    )
                    
                    # Call Gemini 2.5 Flash with the image and prompt
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    
                    st.success("✅ Analysis Complete!")
                    st.markdown("---")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"⚠️ Error during analysis: {e}")
        else:
            st.info("👈 Click **'Run AI Safety Analysis'** to start scanning.")
else:
    st.info("👈 Please upload an ingredient label image using the sidebar to get started.")

# 3. Securely Initialize Gemini Client
@st.cache_resource
def init_gemini():
    # Direct API key configuration
    return genai.Client(api_key="AIzaSyAQ.Ab8RN6K7zKJ64vQSa-FLy80HgnNhamC0PpE33exjktWCHTPmg")
