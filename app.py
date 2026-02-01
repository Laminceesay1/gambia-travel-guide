"""
✈️ The Gambia Travel Assistant
Your AI-Powered Guide to the Smiling Coast of Africa
Mobile-First • Fast • Simple
"""

import streamlit as st
import requests
from datetime import datetime
from urllib.parse import quote

# Page config - MUST be first Streamlit command
st.set_page_config(
    page_title="Gambia Travel Guide",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Site info
SITE_URL = "https://gambia-travel-guide.streamlit.app"
SITE_TITLE = "The Gambia Travel Guide"
CONTACT_EMAIL = "info@gambia-travel-guide.com"

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

/* Share buttons */
.share-container {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
    margin: 0.5rem 0;
}
.share-btn {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 8px 14px;
    border-radius: 20px;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    transition: transform 0.2s;
}
.share-btn:hover { transform: scale(1.05); }
.share-whatsapp { background: #25D366; color: white !important; }
.share-facebook { background: #1877F2; color: white !important; }
.share-twitter { background: #1DA1F2; color: white !important; }
.share-linkedin { background: #0077B5; color: white !important; }
.share-reddit { background: #FF4500; color: white !important; }
.share-email { background: #EA4335; color: white !important; }

/* Quick help links */
.help-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    margin: 1rem 0;
}
.help-link {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 16px;
    background: #f8f9fa;
    border-radius: 12px;
    text-decoration: none;
    color: #333 !important;
    font-weight: 500;
    transition: all 0.2s;
    cursor: pointer;
    border: 1px solid #e9ecef;
}
.help-link:hover {
    background: #0C1C8C;
    color: white !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(12, 28, 140, 0.2);
}

/* Booking links bar */
.booking-bar {
    background: linear-gradient(135deg, #0C1C8C 0%, #1a3d9e 100%);
    border-radius: 12px;
    padding: 1rem;
    margin: 0.5rem 0 1rem 0;
    text-align: center;
}
.booking-bar a {
    color: white !important;
    text-decoration: none;
    padding: 8px 16px;
    margin: 4px;
    display: inline-block;
    background: rgba(255,255,255,0.15);
    border-radius: 8px;
    font-weight: 500;
}
.booking-bar a:hover { background: rgba(255,255,255,0.25); }
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

FLIGHTS = [
    {"airline": "Brussels Airlines", "route": "Brussels ↔ Banjul", "freq": "3-4x weekly", "icon": "🇧🇪"},
    {"airline": "Vueling", "route": "Barcelona ↔ Banjul", "freq": "2x weekly (seasonal)", "icon": "🇪🇸"},
    {"airline": "TUI Airways", "route": "London Gatwick ↔ Banjul", "freq": "Weekly (Nov-Apr)", "icon": "🇬🇧"},
    {"airline": "Royal Air Maroc", "route": "Casablanca ↔ Banjul", "freq": "Daily", "icon": "🇲🇦"},
    {"airline": "Turkish Airlines", "route": "Istanbul ↔ Banjul", "freq": "3x weekly", "icon": "🇹🇷"},
    {"airline": "Binter Canarias", "route": "Las Palmas ↔ Banjul", "freq": "2x weekly", "icon": "🇪🇸"},
    {"airline": "ASKY Airlines", "route": "Lomé ↔ Banjul", "freq": "2x weekly", "icon": "🌍"},
    {"airline": "Air Senegal", "route": "Dakar ↔ Banjul", "freq": "Daily", "icon": "🇸🇳"},
]

# Social Media Links
SOCIAL_LINKS = {
    "facebook": "https://facebook.com/GambiaTravelGuide",
    "twitter": "https://twitter.com/GambiaTravelGM",
    "linkedin": "https://linkedin.com/company/gambia-travel-guide",
    "reddit": "https://reddit.com/r/GambiaTravel",
}

# ============== SHARE FUNCTION ==============
def render_share_buttons():
    """Render social share buttons"""
    msg = quote("Check out The Gambia Travel Guide - Your AI guide to the Smiling Coast! 🇬🇲✈️")
    url = quote(SITE_URL)
    st.markdown(f"""
    <div class="share-container">
        <a class="share-btn share-whatsapp" href="https://wa.me/?text={msg}%20{url}" target="_blank">📱 WhatsApp</a>
        <a class="share-btn share-facebook" href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank">📘 Facebook</a>
        <a class="share-btn share-twitter" href="https://twitter.com/intent/tweet?text={msg}&url={url}" target="_blank">🐦 Twitter</a>
        <a class="share-btn share-linkedin" href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank">💼 LinkedIn</a>
        <a class="share-btn share-reddit" href="https://reddit.com/submit?url={url}&title=The%20Gambia%20Travel%20Guide" target="_blank">🔶 Reddit</a>
        <a class="share-btn share-email" href="mailto:?subject=The%20Gambia%20Travel%20Guide&body={msg}%20{url}" target="_blank">📧 Email</a>
    </div>
    """, unsafe_allow_html=True)

# ============== HEADER ==============
st.markdown('<div class="flag-bar"></div>', unsafe_allow_html=True)

# Title row with logo, title, weather
col_logo, col_title, col_weather = st.columns([1, 3, 2])
with col_logo:
    try:
        st.image("assets/logo.png", width=60)
    except:
        st.markdown("✈️")
with col_title:
    st.markdown("## Gambia Travel Guide")
    st.caption("Your AI Guide to the Smiling Coast 🇬🇲")
with col_weather:
    w = get_weather()
    rate = get_exchange_rate()
    st.markdown(f"**{weather_icon(w['code'])} {w['temp']}°C**")
    st.markdown(f"**💵 {rate} GMD/$1**")

# ============== NAVIGATION TABS ==============
tab_home, tab_flights, tab_guides, tab_plan, tab_hotels, tab_see, tab_tours = st.tabs([
    "🏠 Ask", "✈️ Flights", "📖 Guides", "📅 Plan", "🏨 Stay", "⭐ See", "🎫 Tours"
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
        # Welcome message when no search - with clickable links
        st.markdown("---")
        st.markdown("**🌴 Welcome to The Gambia!**")
        st.markdown("I can help you with:")
        
        # Clickable help topics in 2 columns
        help_col1, help_col2 = st.columns(2)
        help_topics = [
            ("🛂 Visa Requirements", "visa"),
            ("🛡️ Safety Info", "is gambia safe"),
            ("🏖️ Best Beaches", "best beach"),
            ("🏨 Where to Stay", "where to stay"),
            ("💰 Money & Currency", "money"),
            ("🚕 Getting Around", "getting around"),
            ("🧳 Packing List", "what to pack"),
            ("📅 Day Trip Ideas", "day trip"),
        ]
        
        for i, (label, key) in enumerate(help_topics):
            col = help_col1 if i % 2 == 0 else help_col2
            with col:
                if st.button(label, key=f"help_{key}", use_container_width=True):
                    st.session_state.help_query = key
                    st.rerun()
        
        # Check if a help topic was clicked
        if "help_query" in st.session_state:
            help_key = st.session_state.help_query
            del st.session_state.help_query
            if KB_LOADED and help_key in QUICK_ANSWERS:
                st.markdown("---")
                st.markdown(f'<div class="answer-box">{QUICK_ANSWERS[help_key]}</div>', unsafe_allow_html=True)

# ============== FLIGHTS TAB ==============
with tab_flights:
    st.markdown("### ✈️ Getting to The Gambia")
    
    st.info("**Banjul International Airport (BJL)** — 24km from tourist areas")
    
    st.markdown("#### Direct Flight Routes")
    
    for f in FLIGHTS:
        st.markdown(f"""
        <div class="info-card">
            <strong>{f['icon']} {f['airline']}</strong><br>
            ✈️ {f['route']}<br>
            📅 {f['freq']}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 🔍 Search & Book Flights")
    st.markdown("""
    <div class="booking-bar">
        <a href="https://www.skyscanner.com/routes/uk/bjl/united-kingdom-to-banjul.html" target="_blank">🛫 Skyscanner</a>
        <a href="https://www.google.com/travel/flights?q=flights%20to%20Banjul" target="_blank">🔍 Google Flights</a>
        <a href="https://www.kayak.com/flights/to-BJL" target="_blank">🎯 Kayak</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 💡 Tips")
    st.markdown("""
    - **Peak season:** November to April (book early!)
    - **Off-peak:** May to October (rainy, but cheaper)
    - **Flight time:** 5-6 hours from Europe, 10-14 hours from US
    - **Best value:** Brussels Airlines offers most frequent connections
    - **From US/Canada:** Connect via Brussels, Istanbul, or Casablanca
    """)

# ============== GUIDES TAB ==============
with tab_guides:
    st.markdown("### 📖 Essential Travel Guides")
    
    guide_tabs = st.tabs(["🛂 Visa", "💰 Money", "🛡️ Safety", "☀️ Weather", "🚕 Transport", "🏖️ Beaches", "🍛 Food", "💉 Health"])
    guide_keys = ["visa", "money", "is gambia safe", "weather", "getting around", "best beach", "food", "vaccines"]
    
    for i, gtab in enumerate(guide_tabs):
        with gtab:
            if KB_LOADED and guide_keys[i] in QUICK_ANSWERS:
                st.markdown(QUICK_ANSWERS[guide_keys[i]])
            else:
                st.info("Guide loading...")

# ============== PLAN TAB ==============
with tab_plan:
    st.markdown("### 📅 Plan Your Trip")
    
    plan_tabs = st.tabs(["📅 Day Trips", "🧳 Packing", "🗺️ Maps", "📍 Distances"])
    
    with plan_tabs[0]:
        st.markdown("#### One Day Itineraries")
        if KB_LOADED and "day trip" in QUICK_ANSWERS:
            st.markdown(QUICK_ANSWERS["day trip"])
        
        st.markdown("---")
        st.markdown("#### Multi-Day Plans")
        day_options = ["3 days", "one week"]
        for opt in day_options:
            if KB_LOADED and opt in QUICK_ANSWERS:
                with st.expander(f"📅 {opt.title()} in The Gambia"):
                    st.markdown(QUICK_ANSWERS[opt])
    
    with plan_tabs[1]:
        st.markdown("#### What to Pack")
        if KB_LOADED and "what to pack" in QUICK_ANSWERS:
            st.markdown(QUICK_ANSWERS["what to pack"])
        else:
            st.markdown("""
**👕 Clothes:**
- Light, breathable fabrics
- Modest clothes for villages
- Swimwear for beaches
- Light sweater (evenings Nov-Feb)

**🧴 Essentials:**
- Sunscreen SPF 30+
- Mosquito repellent (DEET)
- Sunglasses & hat

**💊 Health:**
- Antimalarials (ask doctor)
- Basic first aid kit
- Hand sanitizer

**🔌 Tech:**
- UK-style adapter (Type G)
- Portable charger

**💡 Don't forget:**
- €40 cash for Tourism Levy!
- Passport copies
- Travel insurance
            """)
    
    with plan_tabs[2]:
        st.markdown("#### Interactive Maps")
        
        st.markdown("""
        <div class="booking-bar">
            <a href="https://www.google.com/maps/place/The+Gambia" target="_blank">🗺️ Google Maps</a>
            <a href="https://www.openstreetmap.org/relation/192774" target="_blank">🌍 OpenStreetMap</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Key locations
        st.markdown("#### 📍 Key Locations")
        locations = [
            ("Banjul International Airport", "13.338,-16.652", "Main airport"),
            ("Kololi / Senegambia", "13.441,-16.718", "Tourist hub"),
            ("Kunta Kinteh Island", "13.326,-16.364", "UNESCO Heritage"),
            ("Abuko Nature Reserve", "13.398,-16.640", "Wildlife park"),
            ("Banjul City Center", "13.454,-16.579", "Capital city"),
        ]
        for name, coords, desc in locations:
            st.markdown(f"""
            <div class="info-card">
                <strong>📍 {name}</strong><br>
                {desc}<br>
                <a href="https://www.google.com/maps?q={coords}" target="_blank">🗺️ View on Map</a>
            </div>
            """, unsafe_allow_html=True)
    
    with plan_tabs[3]:
        st.markdown("#### Distances & Travel Times")
        if KB_LOADED and "how far" in QUICK_ANSWERS:
            st.markdown(QUICK_ANSWERS["how far"])
        else:
            st.markdown("""
| From Kololi → | Distance | Time | Taxi Cost |
|--------------|----------|------|-----------|
| Banjul | 15 km | 30-45 min | $8-12 |
| Airport (BJL) | 24 km | 40-60 min | $15-25 |
| Serekunda | 5 km | 10-15 min | $3-4 |
| Tanji | 25 km | 45 min | $10-15 |
| Brikama | 30 km | 45-60 min | $12-16 |
            """)

# ============== HOTELS TAB ==============
with tab_hotels:
    st.markdown("### 🏨 Where to Stay")
    
    # Booking platforms at top
    st.markdown("""
    <div class="booking-bar">
        <strong style="color: white;">🔍 Find Accommodation:</strong><br>
        <a href="https://airbnb.com/s/Gambia" target="_blank">🏠 Airbnb</a>
        <a href="https://booking.com/country/gm.html" target="_blank">🏨 Booking.com</a>
        <a href="https://hotels.com/de10348/hotels-the-gambia" target="_blank">🌟 Hotels.com</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Popular Hotels")
    
    for h in HOTELS:
        stars = "⭐" * h["stars"]
        st.markdown(f"""
        <div class="info-card">
            <strong>{h['name']}</strong> {stars}<br>
            📍 {h['area']} &nbsp;|&nbsp; 💵 {h['price']}/night<br>
            <a href="{h['url']}" target="_blank">📅 Book on Booking.com</a>
        </div>
        """, unsafe_allow_html=True)

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

# Share section
st.markdown("#### 📤 Share with Friends")
render_share_buttons()

# Follow us section
st.markdown("#### 🔗 Follow Us")
st.markdown(f"""
<div class="share-container">
    <a class="share-btn share-facebook" href="{SOCIAL_LINKS['facebook']}" target="_blank">📘 Facebook</a>
    <a class="share-btn share-twitter" href="{SOCIAL_LINKS['twitter']}" target="_blank">🐦 Twitter</a>
    <a class="share-btn share-linkedin" href="{SOCIAL_LINKS['linkedin']}" target="_blank">💼 LinkedIn</a>
    <a class="share-btn share-reddit" href="{SOCIAL_LINKS['reddit']}" target="_blank">🔶 Reddit</a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="flag-bar"></div>', unsafe_allow_html=True)

# Contact & Credits
st.markdown(f"""
<p style="text-align:center; color:#888; font-size:0.85rem;">
    ✈️ <strong>Gambia Travel Guide</strong><br>
    📧 <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a><br>
    <a href="https://visitthegambia.gm">🌐 Official Tourism</a> &nbsp;|&nbsp;
    🚔 Police: 117 &nbsp;|&nbsp; 🚑 Ambulance: 116
</p>
""", unsafe_allow_html=True)
