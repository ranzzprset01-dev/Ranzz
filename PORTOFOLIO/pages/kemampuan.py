from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Kemampuan | Randi Prasetyo", page_icon="✨", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
skill_image = BASE_DIR / "alightmotion.webp"

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 14% 4%, rgba(34, 197, 94, .13), transparent 34%),
            linear-gradient(145deg, #07111f 0%, #101d2b 58%, #0c241d 100%);
        color: #e2e8f0;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(160deg, #0b1727 0%, #102a2a 100%);
        border-right: 1px solid rgba(52, 211, 153, .25);
    }
    [data-testid="stSidebar"] * { color: #e2e8f0; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        color: #6ee7b7 !important;
        font-weight: 600;
    }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] + div[role="radiogroup"] label[data-checked="true"] {
        background: rgba(34, 197, 94, .18);
        border-radius: 8px;
    }
    .block-container { max-width: 1100px; padding-top: 2.5rem; padding-bottom: 3rem; }
    .skills-hero { text-align: center; margin: 1rem 0 1.7rem; }
    .skills-eyebrow {
        display: inline-block;
        padding: .4rem .85rem;
        border: 1px solid rgba(52, 211, 153, .35);
        border-radius: 999px;
        color: #6ee7b7;
        background: rgba(16, 185, 129, .08);
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .15em;
    }
    .skills-title {
        margin: .8rem 0 .35rem;
        color: #f8fafc;
        font-size: clamp(2.2rem, 5vw, 3.4rem);
        font-weight: 800;
        letter-spacing: -.045em;
        line-height: 1.08;
    }
    .skills-subtitle { margin: 0; color: #94a3b8; font-size: 1.05rem; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(145deg, rgba(15, 31, 49, .92), rgba(10, 25, 37, .92));
        border: 1px solid rgba(148, 163, 184, .18);
        border-radius: 22px;
        box-shadow: 0 24px 70px rgba(0, 0, 0, .2);
    }
    [data-testid="stVerticalBlockBorderWrapper"] img {
        border: 1px solid rgba(110, 231, 183, .2);
        border-radius: 15px;
    }
    .skills-section-label {
        margin: .2rem 0 .35rem;
        color: #6ee7b7;
        font-size: .74rem;
        font-weight: 700;
        letter-spacing: .16em;
    }
    .skills-card-title { margin: 0 0 .7rem; color: #f8fafc; font-size: 1.5rem; }
    .skills-table { width: 100%; border-collapse: separate; border-spacing: 0 9px; }
    .skills-table td { padding: 14px 15px; background: rgba(255, 255, 255, .045); }
    .skills-table td:first-child {
        width: 30%;
        color: #6ee7b7;
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .07em;
        border-radius: 10px 0 0 10px;
        vertical-align: top;
    }
    .skills-table td:last-child {
        color: #e2e8f0;
        font-weight: 500;
        line-height: 1.7;
        border-radius: 0 10px 10px 0;
    }
    [data-testid="stPageLink"] a {
        color: #a7f3d0;
        border: 1px solid rgba(52, 211, 153, .3);
        border-radius: 10px;
        background: rgba(16, 185, 129, .06);
    }
    [data-testid="stPageLink"] a:hover {
        border-color: rgba(110, 231, 183, .6);
        background: rgba(16, 185, 129, .12);
    }
    @media (max-width: 700px) {
        .block-container { padding-top: 1.5rem; }
        .skills-table td { padding: 11px; }
        .skills-table td:first-child { width: 34%; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="skills-hero">
        <span class="skills-eyebrow">KREATIVITAS &amp; MINAT</span>
        <h1 class="skills-title">Keterampilan Saya</h1>
        <p class="skills-subtitle">Ruang untuk berkreasi, bereksplorasi, dan terus berkembang.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.page_link("home.py", label="← Kembali ke beranda")
st.write("")

image_col, details_col = st.columns([0.9, 1.4], gap="large", vertical_alignment="center")

with image_col:
    with st.container(border=True):
        st.image(str(skill_image), use_container_width=True)
        st.caption("Eksplorasi kreatif melalui editing foto dan video.")

with details_col:
    with st.container(border=True):
        st.markdown(
            """
            <div class="skills-section-label">TENTANG SAYA</div>
            <h2 class="skills-card-title">Kemampuan &amp; Hobi</h2>
            <table class="skills-table">
                <tr>
                    <td>KEMAMPUAN</td>
                    <td>Editing foto dan video menggunakan Alight Motion, Keyflow, Wink, CapCut, JJ, dan Animation.</td>
                </tr>
                <tr>
                    <td>HOBI</td>
                    <td>Bermain gitar, badminton, coding, dan editing.</td>
                </tr>
            </table>
            """,
            unsafe_allow_html=True,
        )
