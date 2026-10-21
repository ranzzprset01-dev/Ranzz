import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🏘️",
    layout="wide",
    
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-image: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.82), rgba(21, 128, 61, 0.78)), url("pages/OIP.webp");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        border-right: 10px solid #22c55e; /* Aksen hijau neon sesuai tema config Anda */
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc; /* Warna teks putih */
    }

    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        background-color: #22c55e;
        color: black !important;
        border-radius: 8px;
        font-weight: bold; 
    }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] + div[role="radiogroup"] label[data-checked="true"] {
        background-color: #22c55e;
        color: black !important;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1 {
        color: #f8fafc;
        font-size: clamp(2.5rem, 5vw, 4rem) !important;
        font-weight: 800 !important;
        letter-spacing: 0.08em;
        text-shadow: 0 4px 24px rgba(34, 197, 94, 0.3);
    }

    [data-testid="stSidebar"] {
        border-right: 3px solid #22c55e;
        box-shadow: 8px 0 30px rgba(0, 0, 0, 0.25);
    }

    [data-testid="stImage"] img,
    [data-testid="stVideo"] {
        border: 1px solid rgba(134, 239, 172, 0.35);
        border-radius: 18px;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.3);
    }

    [data-testid="stPageLink-NavLink"] {
        display: block;
        padding: 0.7rem 1rem;
        margin: 0.6rem 0;
        text-align: center;
        box-shadow: 0 6px 18px rgba(34, 197, 94, 0.18);
    }

    [data-testid="stPageLink-NavLink"]:hover {
        box-shadow: 0 10px 24px rgba(34, 197, 94, 0.3);
    }

    @media (max-width: 768px) {
        .block-container { padding-top: 1.5rem; }
        h1 { letter-spacing: 0.04em; }
    }
    
    </style>
    """,
    unsafe_allow_html=True
    )
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #15803d 100%);
    }
    /* Style tambahan untuk mempercantik tabel */
    .biodata-table {
        width: 100%;
        border-collapse: collapse;
        color: #f8fafc;
        font-family: sans-serif;
    }
    .biodata-table td {
        padding: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .label-kolom {
        font-weight: bold;
        color: #22c55e; /* Aksen hijau neon sesuai tema config Anda */
        width: 30%;
    }
    [data-testid="stPageLink-NavLink"] {
        background: linear-gradient(135deg, #22c55e 0%, #86efac 50%, #16a34a 100%);
        color: #0f172a !important;
        border: 1px solid #86efac;
        border-radius: 8px;
        font-weight: bold;
        transition: background 0.2s ease, transform 0.2s ease;
    }
    [data-testid="stPageLink-NavLink"]:hover {
        background: linear-gradient(135deg, #16a34a 0%, #22c55e 50%, #15803d 100%);
        color: #f8fafc !important;
        transform: translateY(-2px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>HALAMAN BERANDA</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#cbd5e1; font-size:1.1rem; margin-top:-0.8rem;'>"
    "Selamat datang di portofolio saya — jelajahi karya, profil, dan aktivitas saya.</p>",
    unsafe_allow_html=True,
)



col1, col2, col3, col4, col5 = st.columns([2, 1, 2, 1, 2])

with col1:
    st.image("PORTOFOLIO/pages/OIP.webp", width=200)
    st.page_link("pages/kemampuan.py", label="lihat kemampuan", use_container_width=True)
    st.page_link("pages/profil.py", label="lihat profil", use_container_width=True)
    st.page_link("pages/sosmed.py", label="lihat sosmed", use_container_width=True)
with col3:
    st.video("PORTOFOLIO/pages/my video.mp4", width=640, autoplay=True, muted=False, loop=True)
with col5:
    st.image("PORTOFOLIO/pages/unduhan.jpeg", width=200)
    st.image("PORTOFOLIO/pages/unduhan.webp", width=200)
