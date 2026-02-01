"""
✈️ The Gambia Travel Assistant
Your AI-Powered Guide to the Smiling Coast of Africa
Mobile-First • Fast • Simple
"""

import streamlit as st
import requests
from datetime import datetime

# Page config - MUST be first Streamlit command
st.set_page_config(
    page_title="Gambia Travel Guide",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Import knowledge base
try:
    from data.gambia_knowledge_base import QUICK_ANSWERS, get_smart_answer, get_suggestions
    KB_LOADED = True
except ImportError:
    KB_LOADED = False
    QUICK_ANSWERS = {}
    def get_smart_answer(q): return {"answer": None, "confidence": 0}
    def get_suggestions(q): return []

# ============== SIMPLE CSS - Mobile First ==============
st.markdown("""
<style>
/* Hide sidebar completely */
[data-testid="stSidebar"], 
[data-testid="stSidebarCollapsedControl"] { display: none !important; }

/* Hide Streamlit extras */
#MainMenu, footer, [data-testid="stDecoration"], 
.stDeployButton { display: none !important; }

/* Mobile-first base */
.main .block-container {
    padding: 1rem !important;
    max-width: 100% !important;
}

/* Prevent zoom on mobile inputs */
input, textarea, select { font-size: 16px !important; }

/* Mobile typography */
@media (max-width: 768px) {
    h1 { font-size: 1.5rem !important; }
    h2 { font-size: 1.25rem !important; }
    h3 { font-size: 1.1rem !important; }
}

/* Touch-friendly buttons */
.stButton > button {
    min-height: 48px !important;
    border-radius: 24px !important;
    font-weight: 500 !important;
}

/* Touch-friendly inputs */
.stTextInput > div > div > input {
    min-height: 48px !important;
    border-radius: 24px !important;
    padding: 0 1rem !important;
}

/* Tabs - scrollable on mobile */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    overflow-x: auto;
    flex-wrap: nowrap;
    -webkit-overflow-scrolling: touch;
}
.stTabs [data-baseweb="tab"] {
    min-height: 44px;
    padding: 8px 12px;
    font-size: 0.9rem;
    white-space: nowrap;
}

/* Gambian flag colors */
.flag-bar {
    height: 4px;
    background: linear-gradient(to right, 
        #CE1126 0%, #CE1126 20%, 
        #FFFFFF 20%, #FFFFFF 35%, 
        #0C1C8C 35%, #0C1C8C 65%, 
        #FFFFFF 65%, #FFFFFF 80%, 
        #3A7728 80%, #3A7728 100%);
    border-radius: 2px;
    margin: 0.5rem 0;
}

/* Info cards */
.info-card {
    background: #fff;
    border-radius: 12px;
    padding: 1rem;
    margin: 0.5rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border: 1px solid #eee;
}

/* Answer box */
.answer-box {
    background: linear-gradient(135deg, #f8f9fa 0%, #fff 100%);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
    border-left: 4px solid #0C1C8C;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# ============== HELPER FUNCTIONS ==============
@st.cache_data(ttl=1800)
def get_weather():
    """Get Banjul weather from Open-Meteo (free, no API key)"""
    try:
        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 13.45, "longitude": -16.58, "current_weather": True},
            timeout=5
        )
        if r.ok:
            data = r.json().get("current_weather", {})
            return {"temp": round(data.get("temperature", 28)), "code": data.get("weathercode", 0)}
    except:
        pass
    return {"temp": 28, "code": 0}

@st.cache_data(ttl=3600)
def get_exchange_rate():
    """Get USD to GMD rate from Frankfurter (free, no API key)"""
    try:
        r = requests.get("https://api.frankfurter.app/latest?from=USD&to=GMD", timeout=5)
        if r.ok:
            return round(r.json().get("rates", {}).get("GMD", 68))
    except:
        pass
    return 68

def weather_icon(code):
    icons = {0: "☀️", 1: "🌤️", 2: "⛅", 3: "☁️", 45: "🌫️", 51: "🌧️", 61: "🌧️", 80: "🌧️", 95: "⛈️"}
    return icons.get(code, "🌤️")

@st.cache_data(ttl=86400)
def search_wikipedia(query):
    """Search Wikipedia for Gambia content"""
    try:
        terms = [f"{query} Gambia", query, f"The Gambia {query}"]
        for term in terms:
            r = requests.get(
                f"https://en.wikipedia.org/api/rest_v1/page/summary/{term.replace(' ', '_')}",
                headers={"User-Agent": "GambiaTravelGuide/1.0"},
                timeout=5
            )
            if r.ok and r.json().get("extract"):
                data = r.json()
                return {
                    "found": True,
                    "title": data.get("title", query),
                    "summary": data.get("extract", ""),
                    "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
                    "image": data.get("thumbnail", {}).get("source")
                }
    except:
        pass
    return {"found": False}

# ============== DATA ==============
HOTELS = [
    {"name": "Coco Ocean Resort & Spa", "stars": 5, "area": "Bijilo", "price": "$150-250", "url": "https://booking.com/hotel/gm/coco-ocean.html"},
    {"name": "Coral Beach Hotel", "stars": 4, "area": "Brufut", "price": "$100-150", "url": "https://booking.com/hotel/gm/coral-beach.html"},
    {"name": "Senegambia Beach Hotel", "stars": 4, "area": "Kololi", "price": "$80-120", "url": "https://booking.com/hotel/gm/senegambia.html"},
    {"name": "Sunbeach Hotel", "stars": 3, "area": "Bakau", "price": "$60-90", "url": "https://booking.com/hotel/gm/sunbeach.html"},
    {"name": "Kombo Beach Hotel", "stars": 3, "area": "Kotu", "price": "$50-80", "url": "https://booking.com/hotel/gm/kombo-beach.html"},
]

ATTRACTIONS = [
    {"name": "Kunta Kinteh Island", "type": "UNESCO Site", "desc": "Historic slave trade memorial", "cost": "D150"},
    {"name": "Abuko Nature Reserve", "type": "Wildlife", "desc": "Monkeys, crocodiles, 270+ birds", "cost": "D150"},
    {"name": "Bijilo Forest Park", "type": "Nature", "desc": "Monkeys & trails near hotels", "cost": "D100"},
    {"name": "Crocodile Pool Kachikally", "type": "Culture", "desc": "Sacred crocodile pool", "cost": "D100"},
    {"name": "Arch 22", "type": "Monument", "desc": "Banjul landmark with views", "cost": "D50"},
    {"name": "Tanji Fish Market", "type": "Culture", "desc": "Colorful fishing village", "cost": "Free"},
]

TOURS = [
    {"name": "Kunta Kinteh Island Tour", "duration": "Full day", "price": "$60-80"},
    {"name": "River Cruise & Birds", "duration": "Half day", "price": "$40-60"},
    {"name": "Abuko Nature Walk", "duration": "3 hours", "price": "$25-40"},
    {"name": "Tanji Village Experience", "duration": "4 hours", "price": "$30-50"},
]

# ============== HEADER ==============
st.markdown('<div class="flag-bar"></div>', unsafe_allow_html=True)

# Title row with weather/exchange
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("## ✈️ Gambia Travel Guide")
with col2:
    w = get_weather()
    rate = get_exchange_rate()
    st.markdown(f"**{weather_icon(w['code'])} {w['temp']}°C** &nbsp;|&nbsp; **💵 {rate} GMD/$1**")

# ============== NAVIGATION TABS ==============
tab_home, tab_guides, tab_hotels, tab_see, tab_tours = st.tabs([
    "🏠 Ask", "📖 Guides", "🏨 Stay", "⭐ See", "🎫 Tours"
])

# ============== HOME/ASK TAB ==============
with tab_home:
    st.markdown("### What would you like to know?")
    
    # Search input
    query = st.text_input(
        "Ask anything about The Gambia",
        placeholder="visa, beaches, safety, weather, hotels...",
        label_visibility="collapsed"
    )
    
    search_clicked = st.button("🔍 Search", type="primary", use_container_width=True)
    
    # Quick buttons
    st.markdown("**Popular:**")
    quick_cols = st.columns(5)
    quick_qs = ["Is it safe?", "Visa?", "Best beach?", "Weather?", "Money?"]
    quick_keys = ["safety", "visa", "best beach", "weather", "money"]
    
    selected_quick = None
    for i, (label, key) in enumerate(zip(quick_qs, quick_keys)):
        with quick_cols[i]:
            if st.button(label, key=f"q_{i}", use_container_width=True):
                selected_quick = key
    
    # Process query
    search_term = query if search_clicked and query else selected_quick
    
    if search_term:
        st.markdown("---")
        
        # Try knowledge base first
        if KB_LOADED:
            result = get_smart_answer(search_term)
            if result and result.get("answer") and result.get("confidence", 0) >= 0.4:
                st.markdown(f'<div class="answer-box">{result["answer"]}</div>', unsafe_allow_html=True)
                
                # Related suggestions
                suggestions = get_suggestions(search_term)
                if suggestions:
                    st.markdown("**Related:**")
                    for s in suggestions[:3]:
                        if st.button(s.replace("_", " ").title(), key=f"s_{s}"):
                            st.session_state.search_query = s
                            st.rerun()
            else:
                # Fall back to Wikipedia
                wiki = search_wikipedia(search_term)
                if wiki["found"]:
                    st.markdown(f"### {wiki['title']}")
                    st.markdown(wiki["summary"])
                    if wiki.get("image"):
                        st.image(wiki["image"], width=300)
                    st.markdown(f"[Read more on Wikipedia →]({wiki['url']})")
                else:
                    st.info(f"No results for '{search_term}'. Try: visa, beaches, safety, hotels")
        else:
            st.warning("Knowledge base loading...")
    
    else:
        # Welcome message when no search
        st.markdown("---")
        st.markdown("""
        **🌴 Welcome to The Gambia!**
        
        I can help you with:
        - 🛂 **Visa** requirements
        - 🛡️ **Safety** information  
        - 🏖️ **Beaches** to visit
        - 🏨 **Hotels** to stay
        - 💰 **Money** & currency
        - 🚕 **Transport** tips
        
        Just type your question above or tap a quick button!
        """)

# ============== GUIDES TAB ==============
with tab_guides:
    st.markdown("### 📖 Essential Travel Guides")
    
    guide_tabs = st.tabs(["🛂 Visa", "💰 Money", "🛡️ Safety", "☀️ Weather", "🏖️ Beaches"])
    guide_keys = ["visa", "money", "safety", "weather", "best beach"]
    
    for i, gtab in enumerate(guide_tabs):
        with gtab:
            if KB_LOADED and guide_keys[i] in QUICK_ANSWERS:
                st.markdown(QUICK_ANSWERS[guide_keys[i]])
            else:
                st.info("Guide loading...")

# ============== HOTELS TAB ==============
with tab_hotels:
    st.markdown("### 🏨 Where to Stay")
    
    for h in HOTELS:
        stars = "⭐" * h["stars"]
        st.markdown(f"""
        <div class="info-card">
            <strong>{h['name']}</strong> {stars}<br>
            📍 {h['area']} &nbsp;|&nbsp; 💵 {h['price']}/night<br>
            <a href="{h['url']}" target="_blank">📅 Book on Booking.com</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("**More options:** [Booking.com](https://booking.com/country/gm.html) • [Airbnb](https://airbnb.com/s/Gambia)")

# ============== ATTRACTIONS TAB ==============
with tab_see:
    st.markdown("### ⭐ What to See")
    
    for a in ATTRACTIONS:
        with st.expander(f"**{a['name']}** — {a['type']}"):
            st.markdown(f"📝 {a['desc']}")
            st.markdown(f"💵 Entry: {a['cost']}")

# ============== TOURS TAB ==============
with tab_tours:
    st.markdown("### 🎫 Popular Tours")
    
    for t in TOURS:
        st.markdown(f"""
        <div class="info-card">
            <strong>🎫 {t['name']}</strong><br>
            ⏱️ {t['duration']} &nbsp;|&nbsp; 💵 {t['price']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("**Book tours:** [GetYourGuide](https://getyourguide.com/gambia-l97) • [Viator](https://viator.com/Gambia-tours)")

# ============== FOOTER ==============
st.markdown("---")
st.markdown('<div class="flag-bar"></div>', unsafe_allow_html=True)
st.markdown("""
<p style="text-align:center; color:#888; font-size:0.85rem;">
    ✈️ Gambia Travel Guide | 
    <a href="https://visitthegambia.gm">Official Tourism</a> |
    🚔 117 | 🚑 116
</p>
""", unsafe_allow_html=True)
