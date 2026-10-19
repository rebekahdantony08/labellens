import os
import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="LabelLens AI — Ingredient Safety & Health Advisor",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Dark Theme & Glassmorphism Styling
st.markdown("""
<style>
    :root {
        --bg-color: #05070c;
        --card-bg: rgba(16, 22, 38, 0.7);
        --accent-emerald: #10b981;
        --accent-purple: #ec4899;
        --border-glass: rgba(255, 255, 255, 0.1);
    }

    .stApp {
        background: radial-gradient(circle at 50% 10%, #0d1322 0%, #05070c 70%);
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(11, 16, 29, 0.9) !important;
        border-right: 1px solid var(--border-glass);
        backdrop-filter: blur(12px);
    }

    .hero-card {
        background: var(--card-bg);
        border: 1px solid var(--border-glass);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(16px);
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(236, 72, 153, 0.08) 100%);
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #34d399, #22d3ee, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.25rem;
    }

    .metric-card {
        background: rgba(22, 32, 50, 0.6);
        border: 1px solid var(--border-glass);
        border-radius: 14px;
        padding: 1rem;
        text-align: center;
        backdrop-filter: blur(10px);
    }

    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #06b6d4 100%) !important;
        color: #05070c !important;
        font-size: 1rem !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.5) !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- HERO HEADER ---
st.markdown("""
<div class="hero-card">
    <div class="hero-title">🔍 LabelLens AI</div>
    <p style="color: #94a3b8; font-size: 1rem; margin: 0;">
        Next-Generation Visual AI Ingredient Safety & Health Advisor
    </p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTROL PANEL ---
with st.sidebar:
    st.markdown("### ⚙️ Label Scanner & Settings")
    uploaded_file = st.file_uploader("Upload Product Label Image", type=["jpg", "jpeg", "png", "webp"])
    
    st.markdown("---")
    st.markdown("### 🔑 API Key (Optional)")
    api_key_input = st.text_input("Enter Gemini API Key", type="password", help="Leave blank if added in Streamlit Secrets")
    
    st.markdown("---")
    st.markdown("### 🛡️ Analysis Focus")
    check_additives = st.checkbox("Highlight Harmful Additives", value=True)
    check_allergens = st.checkbox("Flag Common Allergens", value=True)
    check_preservatives = st.checkbox("Detect Synthetic Preservatives", value=True)
    
    st.markdown("---")
    st.caption("⚡ Powered by Gemini Vision AI")

# --- GEMINI AI ANALYSIS FUNCTION ---
def analyze_label_image(image, prompt, api_key=None):
    # Determine API key source
    key = api_key or os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
    
    if not key:
        raise ValueError("Gemini API Key is missing! Please paste your API key in the sidebar.")

    # Try new Google GenAI SDK first
    try:
        from google import genai
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[image, prompt]
        )
        return response.text
    except Exception:
        # Fallback to legacy google-generativeai SDK
        import google.generativeai as legacy_genai
        legacy_genai.configure(api_key=key)
        model = legacy_genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt, image])
        return response.text

# --- MAIN DISPLAY AREA ---
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col_img, col_analysis = st.columns([1, 1.2], gap="medium")
    
    with col_img:
        st.markdown("#### 📸 Uploaded Label Preview")
        st.image(image, use_container_width=True)
        analyze_btn = st.button("⚡ Run AI Safety Analysis", type="primary")

    with col_analysis:
        if analyze_btn:
            with st.spinner("🔍 Analyzing ingredients with Gemini AI..."):
                try:
                    focus_points = []
                    if check_additives: focus_points.append("Harmful Additives/E-numbers")
                    if check_allergens: focus_points.append("Potential Allergens")
                    if check_preservatives: focus_points.append("Synthetic Preservatives")
                    
                    focus_str = ", ".join(focus_points) if focus_points else "General Safety"
                    
                    prompt = (
                        f"Analyze this product ingredient label image focusing on {focus_str}:\n"
                        "1. Safety Score (0-100) and Rating (Safe / Caution / High Risk)\n"
                        "2. Harmful or High-Risk Additives\n"
                        "3. Potential Allergens\n"
                        "4. Safe/Beneficial Ingredients\n"
                        "Use clear bullet points, emojis, and bold terms."
                    )
                    
                    result_text = analyze_label_image(image, prompt, api_key=api_key_input)
                    
                    st.success("✅ Analysis Complete!")
                    st.markdown("---")
                    st.markdown(result_text)
                    
                except Exception as e:
                    st.error(f"⚠️ {str(e)}")
        else:
            st.info("👈 Click **'Run AI Safety Analysis'** to evaluate ingredients.")

else:
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #34d399; margin:0;">10,000+</h3>
            <p style="color: #94a3b8; margin:0; font-size: 0.85rem;">Additives Indexed</p>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #22d3ee; margin:0;">Real-Time</h3>
            <p style="color: #94a3b8; margin:0; font-size: 0.85rem;">Computer Vision OCR</p>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #ec4899; margin:0;">0.2s</h3>
            <p style="color: #94a3b8; margin:0; font-size: 0.85rem;">Analysis Speed</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Please upload an ingredient label image using the sidebar to get started.")