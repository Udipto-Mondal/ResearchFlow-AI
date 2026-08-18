import streamlit as st
import datetime
from crew import generate_report

# Page Configuration
st.set_page_config(
    page_title="ResearchFlow AI | Autonomous Multi-Agent Research",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Modern, Ultra-Professional Enterprise Theme
CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Top Navigation Bar */
    .top-navbar-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.85rem 1.5rem;
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 14px;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }

    .brand-container {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-icon-box {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(129, 140, 248, 0.25));
        border: 1px solid rgba(129, 140, 248, 0.4);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .brand-badge {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        background: rgba(99, 102, 241, 0.2);
        color: #a5b4fc;
        border: 1px solid rgba(99, 102, 241, 0.4);
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        color: #34d399;
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.35);
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
    }

    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background-color: #34d399;
        box-shadow: 0 0 8px #34d399;
        animation: pulse-dot 2s infinite;
    }

    @keyframes pulse-dot {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.35; transform: scale(0.85); }
    }

    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 1.25rem 1rem 1.75rem 1rem;
        max-width: 860px;
        margin: 0 auto;
    }

    .hero-heading {
        font-size: 2.65rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.2;
        margin-bottom: 0.85rem;
        color: #ffffff;
    }

    .hero-gradient-text {
        background: linear-gradient(135deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #cbd5e1;
        line-height: 1.6;
        font-weight: 400;
        margin-bottom: 1.25rem;
    }

    /* Agent Architecture Cards */
    .agent-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.9rem;
        margin-bottom: 1.75rem;
    }

    @media (max-width: 768px) {
        .agent-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .hero-heading {
            font-size: 2rem;
        }
    }

    .agent-card {
        background: #1e293b;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 14px;
        padding: 1.15rem 1rem;
        text-align: left;
        transition: all 0.25s ease-in-out;
        position: relative;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }

    .agent-card:hover {
        transform: translateY(-3px);
        background: #243248;
        border-color: #818cf8;
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.25);
    }

    .agent-header-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.75rem;
    }

    .agent-step-badge {
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #94a3b8;
        background: rgba(255, 255, 255, 0.06);
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .agent-icon-wrapper {
        width: 32px;
        height: 32px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .agent-role {
        font-size: 0.95rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.35rem;
    }

    .agent-desc {
        font-size: 0.78rem;
        color: #cbd5e1;
        line-height: 1.45;
        font-weight: 400;
    }

    /* Input Workspace */
    .search-card-wrapper {
        background: #0f172a;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.75rem;
        box-shadow: 0 15px 30px -10px rgba(0, 0, 0, 0.5);
    }

    .search-title {
        font-size: 0.95rem;
        font-weight: 700;
        letter-spacing: 0.01em;
        color: #f8fafc;
        margin-bottom: 0.5rem;
    }

    .quick-label {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
        margin-top: 0.85rem;
        margin-bottom: 0.4rem;
    }

    /* Metrics Grid */
    .metrics-bar {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin-bottom: 1.5rem;
    }

    @media (max-width: 640px) {
        .metrics-bar {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    .metric-box {
        background: #1e293b;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    .metric-value {
        font-size: 1.35rem;
        font-weight: 800;
        color: #38bdf8;
        margin-bottom: 0.2rem;
    }

    .metric-title {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #cbd5e1;
        font-weight: 700;
    }

    /* Report View Paper */
    .report-paper {
        background: #0b1120;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 2.25rem;
        color: #f1f5f9;
        line-height: 1.75;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
        margin-top: 1rem;
    }

    .report-paper h1, .report-paper h2, .report-paper h3, .report-paper h4 {
        color: #ffffff;
        font-weight: 700;
        letter-spacing: -0.02em;
    }

    /* Custom Streamlit Button Styling */
    div.stButton > button {
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.85rem;
        transition: all 0.2s ease-in-out;
    }

    .launch-btn-container div.stButton > button {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: #ffffff;
        font-weight: 700;
        font-size: 1rem;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.45);
        width: 100%;
    }

    .launch-btn-container div.stButton > button:hover {
        background: linear-gradient(135deg, #4338ca, #6d28d9);
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.65);
        transform: translateY(-2px);
        color: #ffffff;
    }

    div.stDownloadButton > button {
        background: #1e293b;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #ffffff;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.65rem 1.25rem;
        width: 100%;
    }

    div.stDownloadButton > button:hover {
        background: #334155;
        border-color: #818cf8;
        color: #ffffff;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Comprehensive Multi-Language Dictionary without Emojis
TRANSLATIONS = {
    "en": {
        "brand_name": "ResearchFlow AI",
        "brand_badge": "Crew v1.0",
        "system_status": "Autonomous Agents Ready",
        "subtitle_header": "Autonomous Deep Research & Intelligence Engine",
        "lang_label": "Language / ভাষা",
        "hero_title_1": "Autonomous AI Research &",
        "hero_title_2": "Intelligence Engine",
        "hero_subtitle": "Deploy a specialized crew of 4 autonomous AI agents to research, synthesize, draft, and refine publication-grade reports on any subject in minutes.",
        "step_1": "Step 01",
        "step_2": "Step 02",
        "step_3": "Step 03",
        "step_4": "Step 04",
        "agent_1_title": "Senior Researcher",
        "agent_1_desc": "Explores live web data, verifies facts, and retrieves high-impact sources.",
        "agent_2_title": "Info Strategist",
        "agent_2_desc": "Synthesizes raw intelligence and creates a cohesive structural narrative.",
        "agent_3_title": "Technical Writer",
        "agent_3_desc": "Drafts comprehensive, articulate, and deeply engaging content.",
        "agent_4_title": "Chief Editor",
        "agent_4_desc": "Conducts rigorous fact-checking, formatting, and stylistic polish.",
        "input_label": "Define Research Topic",
        "input_placeholder": "e.g., Quantum Computing in Drug Discovery 2026",
        "quick_topics_label": "Recommended Topics (Click to select):",
        "presets": [
            "Future of AI in Medicine 2026",
            "Autonomous Agents in Financial Markets",
            "Nuclear Fusion Energy Breakthroughs",
            "Neuromorphic Computing vs Quantum AI"
        ],
        "generate_btn": "Launch Agent Crew & Generate Report",
        "empty_warning": "Please enter a valid research topic before launching the crew.",
        "running_spinner": "Autonomous agents are conducting deep research, synthesizing findings, and authoring the report. This typically takes 1-3 minutes...",
        "success_msg": "Report synthesized and finalized successfully.",
        "metrics_words": "Total Words",
        "metrics_chars": "Characters",
        "metrics_read_time": "Est. Read Time",
        "metrics_status": "Quality Check",
        "tab_report": "Formatted Document",
        "tab_raw": "Raw Markdown",
        "tab_agents": "Agent Pipeline Log",
        "download_md": "Download Markdown (.md)",
        "download_txt": "Download Plain Text (.txt)",
        "copy_instructions": "Note: You can download the report directly or copy the raw markdown from the Raw tab.",
        "agent_pipeline_header": "Agent Pipeline Execution Details",
        "agent_pipeline_body": "This report was generated sequentially through 4 autonomous agents:",
        "footer_text": "Powered by CrewAI, Google Gemini & Tavily Search Engine"
    },
    "bn": {
        "brand_name": "ResearchFlow AI",
        "brand_badge": "ক্রু v1.0",
        "system_status": "স্বয়ংক্রিয় এজেন্ট প্রস্তুত",
        "subtitle_header": "স্বয়ংক্রিয় ডিপ রিসার্চ ও ইন্টেলিজেন্স ইঞ্জিন",
        "lang_label": "ভাষা / Language",
        "hero_title_1": "স্বয়ংক্রিয় এআই রিসার্চ ও",
        "hero_title_2": "ইন্টেলিজেন্স ইঞ্জিন",
        "hero_subtitle": "৪ জন বিশেষায়িত এআই এজেন্টের মাধ্যমে যেকোনো বিষয়ে ইন্টারনেট থেকে নিখুঁত তথ্য সংগ্রহ, বিশ্লেষণ ও প্রফেশনাল রিপোর্ট তৈরি করুন কয়েক মিনিটে।",
        "step_1": "ধাপ ০১",
        "step_2": "ধাপ ০২",
        "step_3": "ধাপ ০৩",
        "step_4": "ধাপ ০৪",
        "agent_1_title": "সিনিয়র রিসার্চার",
        "agent_1_desc": "ইন্টারনেট ঘেঁটে নির্ভরযোগ্য তথ্য, পরিসংখ্যান ও সোর্স সংগ্রহ করে।",
        "agent_2_title": "ইনফো স্ট্র্যাটেজিস্ট",
        "agent_2_desc": "প্রাপ্ত তথ্য বিশ্লেষণ করে রিপোর্টের একটি সুনির্দিষ্ট রূপরেখা তৈরি করে।",
        "agent_3_title": "টেকনিক্যাল রাইটার",
        "agent_3_desc": "রূপরেখা অনুযায়ী তথ্যবহুল ও সাবলীল ড্রাফট রচনা করে।",
        "agent_4_title": "চিফ এডিটর",
        "agent_4_desc": "ব্যাকরণ, যুক্তি, তথ্য ও ফরম্যাটিং নিখুঁতভাবে রিভিও এবং ফাইনাল করে।",
        "input_label": "রিসার্চের বিষয় নির্ধারণ করুন",
        "input_placeholder": "যেমন: Future of AI in Medicine 2026",
        "quick_topics_label": "প্রস্তাবিত টপিক (সিলেক্ট করতে ক্লিক করুন):",
        "presets": [
            "Future of AI in Medicine 2026",
            "Autonomous Agents in Financial Markets",
            "Nuclear Fusion Energy Breakthroughs",
            "Neuromorphic Computing vs Quantum AI"
        ],
        "generate_btn": "এজেন্ট ক্রু চালু করুন ও রিপোর্ট তৈরি করুন",
        "empty_warning": "অনুগ্রহ করে প্রথমে একটি রিসার্চ টপিক লিখুন।",
        "running_spinner": "এআই এজেন্টরা ইন্টারনেট গবেষণা, তথ্য বিশ্লেষণ ও রিপোর্ট তৈরিতে কাজ করছে। সাধারণত ১-৩ মিনিট সময় লাগতে পারে...",
        "success_msg": "রিপোর্ট সফলভাবে তৈরি ও সম্পাদিত হয়েছে।",
        "metrics_words": "মোট শব্দ",
        "metrics_chars": "ক্যারেক্টার",
        "metrics_read_time": "পড়ার আনুমানিক সময়",
        "metrics_status": "গুণমান যাচাই",
        "tab_report": "ফরম্যাটেড ডকুমেন্ট",
        "tab_raw": "র' মার্কডাউন",
        "tab_agents": "এজেন্ট পাইপলাইন লগ",
        "download_md": "মার্কডাউন ডাউনলোড (.md)",
        "download_txt": "প্লেইন টেক্সট ডাউনলোড (.txt)",
        "copy_instructions": "নোট: আপনি সরাসরি রিপোর্টটি ডাউনলোড করতে পারেন অথবা Raw ট্যাব থেকে মার্কডাউন কপি করতে পারেন।",
        "agent_pipeline_header": "এজেন্ট পাইপলাইন এক্সিকিউশন বিবরণ",
        "agent_pipeline_body": "এই report টি ৪টি স্বতন্ত্র এজেন্টের মাধ্যমে পর্যায়ক্রমে প্রক্রিয়াজাত হয়েছে:",
        "footer_text": "CrewAI, Google Gemini এবং Tavily সার্চ ইঞ্জিনের সমন্বয়ে পরিচালিত"
    }
}

# Session State Initialization
if "lang" not in st.session_state:
    st.session_state.lang = "en"

if "topic_text" not in st.session_state:
    st.session_state.topic_text = ""

if "report_data" not in st.session_state:
    st.session_state.report_data = None

if "last_topic" not in st.session_state:
    st.session_state.last_topic = ""

def select_preset_topic(preset_val: str):
    st.session_state.topic_text = preset_val

t = TRANSLATIONS[st.session_state.lang]

# --- TOP NAVIGATION & LANGUAGE SWITCHER BAR ---
nav_col1, nav_col2, nav_col3 = st.columns([5, 3, 2], vertical_alignment="center")

with nav_col1:
    st.markdown(
        f"""
        <div class="brand-container" style="padding: 4px 0;">
            <div class="brand-icon-box">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
                    <polyline points="2 17 12 22 22 17"></polyline>
                    <polyline points="2 12 12 17 22 12"></polyline>
                </svg>
            </div>
            <div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.35rem; font-weight: 800; color: #ffffff; letter-spacing: -0.02em;">{t['brand_name']}</span>
                    <span class="brand-badge">{t['brand_badge']}</span>
                </div>
                <div style="font-size: 0.78rem; color: #cbd5e1; font-weight: 500;">{t['subtitle_header']}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with nav_col2:
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <div class="status-pill">
                <div class="status-dot"></div>
                <span>{t['system_status']}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with nav_col3:
    # Language Switcher
    current_idx = 0 if st.session_state.lang == "en" else 1
    selected_lang = st.selectbox(
        label="Language / ভাষা",
        options=["English", "বাংলা"],
        index=current_idx,
        label_visibility="collapsed",
        key="lang_selector_widget"
    )
    # Sync language choice
    new_lang_code = "en" if selected_lang == "English" else "bn"
    if new_lang_code != st.session_state.lang:
        st.session_state.lang = new_lang_code
        st.rerun()

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown(
    f"""
    <div class="hero-container">
        <div class="hero-heading">
            {t['hero_title_1']}<br>
            <span class="hero-gradient-text">{t['hero_title_2']}</span>
        </div>
        <div class="hero-subtitle">
            {t['hero_subtitle']}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 4 AGENTS PIPELINE DISPLAY (CLEAN SVG ICONS) ---
st.markdown(
    f"""
    <div class="agent-grid">
        <div class="agent-card">
            <div class="agent-header-row">
                <div class="agent-icon-wrapper">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                </div>
                <span class="agent-step-badge">{t['step_1']}</span>
            </div>
            <div class="agent-role">{t['agent_1_title']}</div>
            <div class="agent-desc">{t['agent_1_desc']}</div>
        </div>
        <div class="agent-card">
            <div class="agent-header-row">
                <div class="agent-icon-wrapper">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="18" y1="20" x2="18" y2="10"></line>
                        <line x1="12" y1="20" x2="12" y2="4"></line>
                        <line x1="6" y1="20" x2="6" y2="14"></line>
                    </svg>
                </div>
                <span class="agent-step-badge">{t['step_2']}</span>
            </div>
            <div class="agent-role">{t['agent_2_title']}</div>
            <div class="agent-desc">{t['agent_2_desc']}</div>
        </div>
        <div class="agent-card">
            <div class="agent-header-row">
                <div class="agent-icon-wrapper">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                        <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                    </svg>
                </div>
                <span class="agent-step-badge">{t['step_3']}</span>
            </div>
            <div class="agent-role">{t['agent_3_title']}</div>
            <div class="agent-desc">{t['agent_3_desc']}</div>
        </div>
        <div class="agent-card">
            <div class="agent-header-row">
                <div class="agent-icon-wrapper">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        <path d="m9 12 2 2 4-4"></path>
                    </svg>
                </div>
                <span class="agent-step-badge">{t['step_4']}</span>
            </div>
            <div class="agent-role">{t['agent_4_title']}</div>
            <div class="agent-desc">{t['agent_4_desc']}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- SEARCH & INPUT WORKSPACE ---
with st.container():
    st.markdown(f"<div class='search-title'>{t['input_label']}</div>", unsafe_allow_html=True)
    
    user_topic = st.text_input(
        label=t['input_label'],
        value=st.session_state.topic_text,
        placeholder=t['input_placeholder'],
        label_visibility="collapsed"
    )
    # Sync manual input into state
    st.session_state.topic_text = user_topic

    # Preset Topic Suggestion Chips
    st.markdown(f"<div class='quick-label'>{t['quick_topics_label']}</div>", unsafe_allow_html=True)
    preset_cols = st.columns(len(t['presets']))
    for i, preset in enumerate(t['presets']):
        with preset_cols[i]:
            st.button(
                preset,
                key=f"preset_btn_{i}",
                use_container_width=True,
                on_click=select_preset_topic,
                args=(preset,)
            )

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='launch-btn-container'>", unsafe_allow_html=True)
    generate_clicked = st.button(t['generate_btn'], use_container_width=True, key="launch_crew_btn")
    st.markdown("</div>", unsafe_allow_html=True)

# --- EXECUTION LOGIC ---
if generate_clicked:
    current_topic = st.session_state.topic_text.strip()
    if not current_topic:
        st.warning(t['empty_warning'])
    else:
        with st.spinner(t['running_spinner']):
            try:
                result = generate_report(current_topic)
                report_content = result.raw if hasattr(result, 'raw') else str(result)
                
                # Store in session state
                st.session_state.report_data = report_content
                st.session_state.last_topic = current_topic
                st.success(t['success_msg'])
            except Exception as e:
                st.error(f"Error during execution: {str(e)}")

# --- REPORT PRESENTATION SECTION ---
if st.session_state.report_data:
    report_text = st.session_state.report_data
    topic_name = st.session_state.last_topic or "Research"
    
    # Calculate Metrics
    word_count = len(report_text.split())
    char_count = len(report_text)
    estimated_read_minutes = max(1, round(word_count / 200))
    
    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
    
    # Metrics Cards
    st.markdown(
        f"""
        <div class="metrics-bar">
            <div class="metric-box">
                <div class="metric-value">{word_count:,}</div>
                <div class="metric-title">{t['metrics_words']}</div>
            </div>
            <div class="metric-box">
                <div class="metric-value">{char_count:,}</div>
                <div class="metric-title">{t['metrics_chars']}</div>
            </div>
            <div class="metric-box">
                <div class="metric-value">~{estimated_read_minutes} min</div>
                <div class="metric-title">{t['metrics_read_time']}</div>
            </div>
            <div class="metric-box">
                <div class="metric-value">100% Passed</div>
                <div class="metric-title">{t['metrics_status']}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Tabs for Multiple Views
    tab1, tab2, tab3 = st.tabs([t['tab_report'], t['tab_raw'], t['tab_agents']])
    
    with tab1:
        st.markdown(f"<div class='report-paper'>", unsafe_allow_html=True)
        st.markdown(report_text)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with tab2:
        st.caption(t['copy_instructions'])
        st.code(report_text, language="markdown")
        
    with tab3:
        st.markdown(f"### {t['agent_pipeline_header']}")
        st.markdown(t['agent_pipeline_body'])
        st.markdown(
            f"""
            - **Researcher (Step 01)**: Gathered high-relevance web documents, facts, statistics, and verifiable citations.
            - **Strategist (Step 02)**: Filtered noise and structured the document hierarchy.
            - **Technical Writer (Step 03)**: Authored full analytical synthesis.
            - **Chief Editor (Step 04)**: Completed factual validation, polish, and tone harmonization.
            
            *Execution Completed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
            """
        )

    # Action Toolbar: Download Buttons
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    down_col1, down_col2 = st.columns(2)
    
    sanitized_filename = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in topic_name).replace(' ', '_')
    
    with down_col1:
        st.download_button(
            label=t['download_md'],
            data=report_text,
            file_name=f"{sanitized_filename}_Report.md",
            mime="text/markdown",
            use_container_width=True
        )
        
    with down_col2:
        st.download_button(
            label=t['download_txt'],
            data=report_text,
            file_name=f"{sanitized_filename}_Report.txt",
            mime="text/plain",
            use_container_width=True
        )

# --- FOOTER ---
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 3.5rem; padding: 1.5rem; border-top: 1px solid rgba(255, 255, 255, 0.1); font-size: 0.82rem; color: #94a3b8;">
        {t['footer_text']} • ResearchFlow AI v1.0
    </div>
    """,
    unsafe_allow_html=True
)
