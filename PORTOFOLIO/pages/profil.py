import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Profil | Randi Prasetyo", page_icon="👤", layout="wide")

BASE_DIR = Path(__file__).resolve().parent

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(160deg, #0b1727 0%, #102a2a 100%);
        border-right: 1px solid rgba(52, 211, 153, .25);
    }

    [data-testid="stSidebar"] * {
        color: #e2e8f0;
    }

    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        color: #6ee7b7 !important;
        font-weight: 600;
    }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] + div[role="radiogroup"] label[data-checked="true"] {
        background: rgba(34, 197, 94, .18);
        border-radius: 8px;
    }
    .stApp {
        background-color: #07111f;
        color: #e2e8f0;
        font-family: 'DM Sans', sans-serif;
    }
    .block-container { max-width: 1100px; padding-top: 2.5rem; }
    .hero { text-align: center; margin: 1rem 0 2rem; }
    .eyebrow {
        display: inline-block; padding: .4rem .85rem; border: 1px solid rgba(52,211,153,.35);
        border-radius: 999px; color: #6ee7b7; background: rgba(16,185,129,.08);
        font-size: .78rem; font-weight: 700; letter-spacing: .14em;
    }
    .hero h1 { margin: .8rem 0 .35rem; color: #f8fafc; font-size: clamp(2rem, 5vw, 3.2rem); }
    .hero p { margin: 0; color: #94a3b8; font-size: 1.05rem; }
    .profile-card {
        padding: 1.5rem; border: 1px solid rgba(148,163,184,.18); border-radius: 22px;
        background: linear-gradient(145deg, rgba(15,31,49,.94), rgba(10,25,37,.94));
        box-shadow: 0 24px 70px rgba(0,0,0,.28);
    }
    .profile-photo img { border-radius: 16px; border: 1px solid rgba(110,231,183,.25); }
    .section-kicker { color: #6ee7b7; font-size: .75rem; font-weight: 700; letter-spacing: .16em; }
    .profile-title { margin: .3rem 0 1rem; color: #f8fafc; font-size: 1.6rem; font-weight: 700; }
    .bio-table { width: 100%; border-collapse: separate; border-spacing: 0 9px; }
    .bio-table td { padding: 13px 15px; background: rgba(255,255,255,.045); }
    .bio-table td:first-child {
        width: 34%; color: #6ee7b7; font-size: .76rem; font-weight: 700;
        letter-spacing: .07em; border-radius: 10px 0 0 10px;
    }
    .bio-table td:last-child { color: #e2e8f0; font-weight: 500; border-radius: 0 10px 10px 0; }
    [data-testid="stPageLink"] a {
        color: #a7f3d0; border: 1px solid rgba(52,211,153,.3); border-radius: 10px;
        background: rgba(16,185,129,.08);
    }
    @media (max-width: 700px) { .profile-card { padding: 1rem; } .bio-table td { padding: 10px; } }
    </style>
    """,
    unsafe_allow_html=True
)

background_path = BASE_DIR / "cyberpunk.webp"
photo_path = BASE_DIR / "Proyek Baru 140.jpg"
if background_path.exists():
    data_url = base64.b64encode(background_path.read_bytes()).decode("utf-8")
    st.markdown(
        f"<style>.stApp {{ background-image: linear-gradient(120deg, rgba(7,17,31,.94), rgba(7,17,31,.78)), url('data:image/webp;base64,{data_url}'); background-size: cover; background-position: center; background-attachment: fixed; }}</style>",
        unsafe_allow_html=True,
    )

st.markdown(
    "<div class='hero'><span class='eyebrow'>PROFIL MAHASISWA</span><h1>Halo, saya Randi.</h1><p>Mahasiswa Sistem Informasi yang terus belajar dan berkembang.</p></div>",
    unsafe_allow_html=True,
)
st.page_link("home.py", label="← Kembali ke beranda")
st.write("")

photo_col, info_col = st.columns([0.85, 1.65], gap="large", vertical_alignment="center")
with photo_col:
    st.markdown("<div class='profile-card profile-photo'>", unsafe_allow_html=True)
    if photo_path.exists():
        st.image(str(photo_path), use_container_width=True)
    else:
        st.markdown("<div style='padding:5rem 1rem;text-align:center;color:#94a3b8'>Foto profil belum tersedia</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with info_col:
    st.markdown(
        """
        <div class="profile-card">
            <div class="section-kicker">TENTANG SAYA</div>
            <div class="profile-title">Biodata Mahasiswa</div>
            <table class="bio-table">
                <tr><td>NAMA</td><td>Randi Prasetyo</td></tr>
                <tr><td>NIM</td><td>25111068</td></tr>
                <tr><td>PROGRAM STUDI</td><td>Sistem Informasi</td></tr>
                <tr><td>MATA KULIAH</td><td>Pemrograman Berbasis Platform</td></tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
