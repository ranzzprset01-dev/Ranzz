import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 15% 5%, rgba(34, 197, 94, .16), transparent 35%),
            linear-gradient(145deg, #07111f 0%, #101d2b 55%, #0c241d 100%);
        color: #f8fafc;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #101d2b, #0c241d);
        border-right: 1px solid rgba(34, 197, 94, .35);
    }
    [data-testid="stSidebar"] * { color: #f8fafc; }
    .block-container { max-width: 1050px; padding-top: 2.5rem; }
    .social-eyebrow {
        color: #4ade80; font-size: .78rem; font-weight: 700;
        letter-spacing: .2em; text-transform: uppercase; margin-bottom: .45rem;
    }
    .social-title {
        color: #f8fafc; font-size: clamp(2.3rem, 6vw, 3.8rem);
        font-weight: 800; letter-spacing: -.055em; line-height: 1.05;
        margin: 0;
    }
    .social-subtitle {
        color: #a7b6c8; font-size: 1.05rem; margin-top: .9rem;
        margin-bottom: 2rem;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, .045);
        border: 1px solid rgba(255, 255, 255, .1);
        border-radius: 22px;
        box-shadow: 0 18px 45px rgba(0, 0, 0, .18);
        transition: transform .2s ease, border-color .2s ease;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(74, 222, 128, .45);
        transform: translateY(-4px);
    }
    [data-testid="stVerticalBlockBorderWrapper"] img {
        border-radius: 16px;
    }
    [data-testid="stLinkButton"] a {
        background: linear-gradient(100deg, #22c55e, #86efac);
        border: 0;
        border-radius: 12px;
        color: #07111f !important;
        font-weight: 700;
        transition: filter .2s ease, transform .2s ease;
    }
    [data-testid="stLinkButton"] a:hover {
        filter: brightness(1.08);
        transform: translateY(-1px);
    }
    [data-testid="stPageLink"] a {
        border: 1px solid rgba(255, 255, 255, .16);
        border-radius: 10px;
    }
    @media (max-width: 640px) {
        .block-container { padding-top: 1.5rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="social-eyebrow">Temukan saya di</div>', unsafe_allow_html=True)
st.markdown('<h1 class="social-title">Media Sosial</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="social-subtitle">Ikuti aktivitas dan karya terbaru saya di platform berikut.</p>',
    unsafe_allow_html=True,
)

st.page_link("home.py", label="← Kembali ke beranda", use_container_width=True)
st.write("")

col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.image("PORTOFOLIO/pages/TIKTOK.webp", use_container_width=True)
        st.markdown("### TikTok")
        st.caption("Video, cerita, dan konten terbaru")
        st.link_button(
            "Kunjungi @bgranzzprset ↗",
            url="https://www.tiktok.com/@bgranzzprset",
            use_container_width=True,
        )

with col2:
    with st.container(border=True):
        st.image("PORTOFOLIO/pages/INSTAGRAM.webp", use_container_width=True)
        st.markdown("### Instagram")
        st.caption("Foto dan momen keseharian")
        st.link_button(
            "Kunjungi @bgranzzprset ↗",
            url="https://www.instagram.com/bgranzzprset/",
            use_container_width=True,
        )
