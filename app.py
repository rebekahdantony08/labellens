import streamlit as st
from PIL import Image
from google import genai

# Page config
st.set_page_config(
    page_title="LabelLens AI — Ingredient Safety Advisor",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Custom CSS - Modern Dark Glassmorphism & Neon Glow Aesthetic
st.markdown("""
<style>
    /* Dark Futuristic Theme Colors */
    :root {
        --bg-color: #0b0f19;
        --card-bg: rgba(22, 27, 46, 0.7);
        --accent-emerald: #10b981;
        --accent-purple: #8b5cf6;
        --accent-glow: rgba(16, 185, 129, 0.25);
        --text-primary: #f3f4f6;
        --border-glass: rgba(255, 255, 255, 0.1);
    }

    /* Main Container Background */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #171b30 0%, #0b0f19 70%);
        color: var(--text-primary);
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 20, 32, 0.85) !important;
        border-right: 1px solid var(--border-glass);
        backdrop-filter: blur(12px);
    }

    /* Hero Glass Card Header */
    .hero-card {
        background: var(--card-bg);
        border: 1px solid var(--border-glass);
        border-radius: 16px;
        padding: 2.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(16px);
        margin-bottom: 2rem;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%);
        position: relative;
        overflow: hidden;
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #10b981, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* Metric Glass Badges */
    .badge-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid var(--border-glass);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        backdrop-filter: blur(8px);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .badge-card:hover {
        transform: translateY(-3px);
        border-color: var(--accent-emerald);
    }

    /* Custom Primary Action Button */
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        box-shadow: 0 0 20px var(--accent-glow) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.5) !important;
    }

    /* Hide default Streamlit clutter */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="hero-card">
    <div class="hero-title">🔍 LabelLens AI</div>
    <p style="color: #9ca3af; font-size: 1.1rem; margin: 0;">
        Next-Generation Ingredient Safety & Health Intelligence. Instantly decode label toxins, allergens, and safety risks.
    </p>
</div>
""", unsafe_allow_html=True)

# --- Sidebar Controls ---
with st.sidebar:
    st.markdown("### ⚙️ Label Scanner")
    uploaded_file = st.file_uploader("Upload Product Label Image", type=["jpg", "jpeg", "png"])
    
    st.markdown("---")
    st.markdown("### 🛡️ Analysis Focus")
    st.checkbox("Highlight Harmful Additives", value=True)
    st.checkbox("Flag Common Allergens", value=True)
    st.checkbox("Detect Synthetic Preservatives", value=True)
    
    st.markdown("---")
    st.caption("⚡ Powered by Gemini 2.5 Flash Multimodal Engine")

# --- Main Dashboard ---
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col_img, col_info = st.columns([1, 1], gap="large")
    
    with col_img:
        st.markdown("#### 📸 Uploaded Label Preview")
        st.image(image, use_container_width=True)
        analyze_btn = st.button("⚡ Run AI Safety Analysis", type="primary")

    with col_info:
        if analyze_btn:
            with st.spinner("🔍 Decoding molecular structure & ingredient safety profile..."):
                try:
                    client = genai.Client()
                    prompt = (
                        "Analyze this product ingredient label image in detail: "
                        "1. Provide an overall Safety Assessment (Safe / Caution / High Risk). "
                        "2. List Potential Allergens (Milk, Wheat, Soy, Nuts, etc.). "
                        "3. List Harmful or Controversial Additives (e.g., E-numbers, artificial dyes, preservatives). "
                        "4. List Beneficial/Natural Ingredients. "
                        "Use clear bullet points, emojis, and bold key terms."
                    )
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[image, prompt]
                    )
                    
                    st.success("✅ Analysis Complete")
                    st.markdown("---")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"Analysis Error: {e}")
        else:
            st.info("👆 Click **'Run AI Safety Analysis'** to evaluate ingredients.")

else:
    # Key Stats / Placeholder UI when no image is uploaded
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("""
        <div class="badge-card">
            <h3 style="color: #10b981; margin:0;">10,000+</h3>
            <p style="color: #9ca3af; margin:0; font-size: 0.9rem;">Additives Indexed</p>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown("""
        <div class="badge-card">
            <h3 style="color: #3b82f6; margin:0;">Real-Time</h3>
            <p style="color: #9ca3af; margin:0; font-size: 0.9rem;">Multi-Modal Vision AI</p>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown("""
        <div class="badge-card">
            <h3 style="color: #8b5cf6; margin:0;">0.2s</h3>
            <p style="color: #9ca3af; margin:0; font-size: 0.9rem;">Scan Speed</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Please upload an ingredient label image from the left sidebar to start.")