"""
🇬🇲 The Gambia Tourism FAQ Database
Pre-written, high-quality answers for common tourist questions.
This provides instant, ChatGPT-like responses without needing AI.

Features:
- Exact keyword matching for instant responses
- Fuzzy matching for misspellings and near-matches
- "Did you mean...?" suggestions
- Conversational memory support
"""

# Common misspellings and variations mapping
SPELLING_CORRECTIONS = {
    # Visa variations
    "viza": "visa", "visas": "visa", "visum": "visa", "viz": "visa",
    "enrty": "entry", "entrey": "entry", "entrry": "entry",
    "pasport": "passport", "passort": "passport", "passprt": "passport",
    "imigration": "immigration", "imigration": "immigration",
    "requirment": "requirement", "requiremnt": "requirement", "requirments": "requirement",
    
    # Hotels/Accommodation
    "hotell": "hotel", "hotles": "hotel", "hotl": "hotel", "hotels": "hotel",
    "accomodation": "accommodation", "acommodation": "accommodation", "acomodation": "accommodation",
    "reosrt": "resort", "resrt": "resort",
    "loddge": "lodge", "lodg": "lodge",
    
    # Beach
    "beech": "beach", "bech": "beach", "beachs": "beach", "beaches": "beach",
    "swimm": "swimming", "swiming": "swimming",
    
    # Weather/Climate
    "wheather": "weather", "wether": "weather", "waether": "weather",
    "climat": "climate", "climte": "climate",
    "temprature": "temperature", "temperture": "temperature",
    "rainy": "rain", "raining": "rain",
    
    # Money
    "curency": "currency", "curreny": "currency", "currancy": "currency",
    "excange": "exchange", "exchang": "exchange", "xchange": "exchange",
    "dolasi": "dalasi", "dalassi": "dalasi",
    "atms": "atm",
    
    # Safety
    "saftey": "safety", "safty": "safety", "saef": "safe",
    "dangrous": "dangerous", "dangerus": "dangerous",
    
    # Transport
    "transprt": "transport", "transportaion": "transport", "transportation": "transport",
    "taxy": "taxi", "taxii": "taxi", "taxis": "taxi",
    "airprot": "airport", "ariport": "airport",
    
    # Food
    "resturant": "restaurant", "restraunt": "restaurant", "restarant": "restaurant",
    "cusine": "cuisine", "cuisne": "cuisine",
    "traditonal": "traditional", "tradtional": "traditional",
    
    # Health
    "vacine": "vaccine", "vacination": "vaccination", "vacinnation": "vaccination",
    "maleria": "malaria", "malariaa": "malaria",
    "hosptal": "hospital", "hospitl": "hospital",
    
    # Culture
    "tradtion": "tradition", "traditon": "tradition", "traditions": "tradition",
    "custm": "custom", "customes": "customs",
    "religon": "religion", "religous": "religious",
    
    # Places
    "gamiba": "gambia", "gmabia": "gambia", "gambai": "gambia",
    "banjull": "banjul", "banjuul": "banjul",
    "kolol": "kololi", "kololii": "kololi", "kolla": "kololi",
    "sengambia": "senegambia", "senegmbia": "senegambia",
    
    # Common words
    "informaton": "information", "informtion": "information",
    "recomend": "recommend", "reccommend": "recommend",
    "availble": "available", "availabel": "available",
}

# Topic aliases - different ways to ask about the same thing
TOPIC_ALIASES = {
    "visa": ["visa", "entry", "passport", "immigration", "border", "documents", "papers", "permit", "stay duration", "how long can i stay", "enter gambia", "entering", "arrival"],
    "flights": ["flight", "fly", "airline", "airport", "plane", "travel to", "get to gambia", "arrive", "bjl", "banjul airport", "connections"],
    "hotels": ["hotel", "stay", "accommodation", "resort", "lodge", "sleep", "room", "book", "booking", "where to stay", "place to stay", "guest house", "airbnb"],
    "beaches": ["beach", "beaches", "swimming", "sand", "ocean", "sea", "coast", "coastline", "waterfront", "sunbathe"],
    "weather": ["weather", "climate", "temperature", "rain", "hot", "cold", "season", "when to visit", "best time", "dry season", "rainy season", "humid"],
    "money": ["money", "currency", "dalasi", "exchange", "atm", "cash", "credit card", "pay", "cost", "expensive", "price", "afford", "how much"],
    "safety": ["safe", "safety", "dangerous", "crime", "security", "risk", "worry", "scared", "solo travel", "woman", "women"],
    "transport": ["transport", "taxi", "car", "bus", "rent", "driver", "getting around", "travel around", "move", "uber", "gele"],
    "attractions": ["attraction", "see", "do", "visit", "tourist", "sightseeing", "must see", "things to do", "activities", "tour", "excursion", "day trip"],
    "food": ["food", "eat", "restaurant", "cuisine", "dish", "meal", "breakfast", "lunch", "dinner", "local food", "try", "taste", "hungry"],
    "language": ["language", "speak", "english", "mandinka", "wolof", "french", "communicate", "understand", "talk", "greeting", "hello"],
    "health": ["health", "vaccine", "vaccination", "malaria", "hospital", "doctor", "medicine", "sick", "medical", "yellow fever", "ill", "pharmacy"],
    "culture": ["culture", "custom", "tradition", "religion", "dress", "etiquette", "respect", "muslim", "islam", "behavior", "polite", "rude"],
    "festivals": ["festival", "event", "celebration", "holiday", "party", "music", "roots", "dance", "carnival"],
    "shopping": ["shopping", "buy", "market", "souvenir", "craft", "bargain", "gift", "present", "take home"],
    "internet": ["internet", "wifi", "phone", "sim", "data", "mobile", "call", "network", "online", "connected"],
    "nightlife": ["nightlife", "bar", "club", "party", "night", "drink", "beer", "entertainment", "dancing", "evening"],
    "tipping": ["tipping", "tip", "gratuity", "how much tip", "should i tip", "service charge"],
    "packing": ["packing", "pack", "bring", "luggage", "what to bring", "clothes", "essentials", "suitcase", "checklist"],
    "about_gambia": ["about gambia", "tell me about", "what is gambia", "gambia like", "overview", "information", "introduce", "basics", "general"],
    "itinerary_3day": ["3 day", "3-day", "three day", "weekend trip", "short trip"],
    "itinerary_7day": ["7 day", "7-day", "one week", "week trip", "week itinerary"],
    "itinerary_budget": ["budget trip", "cheap trip", "affordable", "backpacker", "low cost", "save money", "budget ideas"],
    "plan_trip": ["plan trip", "plan my trip", "help me plan", "planning", "trip planner", "how to plan", "book trip", "booking"],
    "emergency": ["emergency", "help", "police", "ambulance", "hospital", "embassy", "lost", "stolen", "accident", "urgent", "contact"],
    "day_trip": ["day trip", "one day", "1 day", "passing through", "few hours", "quick visit", "spend the day", "day in gambia", "have a day", "only one day", "just one day", "day to spare", "single day"],
    "distances": ["distance", "how far", "how long", "travel time", "hours to", "banjul to", "serekunda to", "kololi to", "from senegal", "senegal to gambia", "cap skirring", "dakar to banjul", "drive time", "km to"],
}

# Follow-up question patterns (for conversational memory)
FOLLOWUP_PATTERNS = [
    "what about", "how about", "and", "also", "more", "else", "other",
    "tell me more", "more info", "more information", "explain",
    "what else", "anything else", "something else",
    "can you", "could you", "please",
    "it", "that", "this", "there", "they", "them",
    "the same", "similar", "like that",
    "why", "how", "when", "where", "which", "who",
]

GAMBIA_FAQS = {
    # ============== VISA & ENTRY ==============
    "visa": {
        "keywords": ["visa", "entry", "passport", "immigration", "enter", "requirement", "need visa", "travel document"],
        "answer": """**Who Needs a Visa for The Gambia?**

**✅ NO VISA NEEDED (Visa-Free Entry):**
- **ECOWAS Countries:** Nigeria, Ghana, Senegal, Sierra Leone, Liberia, Guinea, Mali, Niger, Burkina Faso, Togo, Benin, Côte d'Ivoire, Guinea-Bissau, Cape Verde - **No visa, just valid passport!**
- **Commonwealth Citizens:** UK, Canada, Australia, New Zealand, Jamaica, Trinidad etc. - **Visa on arrival (FREE)**
- **EU Citizens:** Germany, France, Italy, Spain, Netherlands, Belgium etc. - **Visa on arrival (FREE)**
- **USA & North America:** Americans get **visa on arrival (FREE)**
- **Scandinavian Countries:** Sweden, Norway, Denmark, Finland - **Visa on arrival (FREE)**

**📍 Bottom Line:**
- Most tourists just show up and get stamped in!
- You get **28 days** automatically
- Just bring: passport (6+ months valid) + return ticket

**⚠️ Tourism Levy (This catches people off guard!):**
- **€20 on entry + €20 on exit = €40 total**
- Pay in cash (EUR/USD/GBP) or card
- Have cash ready for smooth entry!

**🚌 Coming from Senegal by land?**
- Same rules apply at the border
- Keep your passport handy
- Border crossings: Karang, Farafenni, Basse

**Need to stay longer?** Extend at Immigration in Banjul (500-1000 GMD fee).

💡 **Tip:** Have your €20 ready in cash for a smooth entry. Keep receipt for exit!"""
    },
    # ============== PLAN MY TRIP ==============
    "plan_trip": {
        "keywords": ["plan trip", "plan my trip", "help me plan", "planning", "trip planner", "how to plan", "book trip", "booking", "itinerary", "travel plan", "organize trip", "trip ideas"],
        "answer": """**How to Plan Your Trip to The Gambia**\n\nHere's a step-by-step guide to planning a great trip to The Gambia:\n\n1. **Choose Your Dates**\n   - Best time: November to May (dry season, pleasant weather)\n   - Rainy season: June to October (fewer tourists, lush scenery)\n\n2. **Book Your Flights**\n   - Main airport: Banjul International (BJL)\n   - Direct flights from Europe (Brussels, UK, Turkey)\n\n3. **Arrange Accommodation**\n   - Popular areas: Kololi/Senegambia (lively), Kotu (family-friendly), Cape Point (local vibe)\n   - Book hotels, guesthouses, or eco-lodges in advance during peak season\n\n4. **Check Visa & Entry Requirements**\n   - Most visitors get visa on arrival (see 'Visa' FAQ)\n   - €20 Tourism Levy on entry & exit\n\n5. **Plan Activities**\n   - Beaches: Kololi, Kotu, Cape Point\n   - Nature: Abuko Nature Reserve, Makasutu Forest, birdwatching\n   - Culture: Kunta Kinteh Island, local markets, music & dance\n   - River cruises, fishing, day trips to Senegal\n\n6. **Health & Safety**\n   - Vaccinations: Yellow fever, Hepatitis A/B, Typhoid (check with your doctor)\n   - Malaria prevention: Bring mosquito repellent, consider prophylaxis\n   - Travel insurance recommended\n\n7. **Money**\n   - Currency: Gambian Dalasi (GMD)\n   - Bring some cash (Euros, USD, GBP)\n   - ATMs available in main towns\n\n8. **Packing Tips**\n   - Light, breathable clothing\n   - Sun protection (hat, sunscreen, sunglasses)\n   - Modest dress for rural/village visits\n   - Power adapter: UK-style (Type G)\n\n💡 **Tip:** Book tours and excursions with licensed guides for the best experience!\n"""
    },
    # ============== DAY TRIP ITINERARY ==============
    "day_trip": {
        "keywords": ["day trip", "one day", "1 day", "passing through", "short visit", "few hours", "day in gambia", "quick visit"],
        "answer": """**One Day in The Gambia - How to Spend It**

**Coming by land from Senegal (Cap Skirring/Dakar)?**
You'll arrive in 3-4 hours. Here's the best plan:

**🌅 COASTAL DAY (Recommended for Land Arrivals):**
```
9:00 AM  → Start at Kachikally Crocodile Pool (Bakau) - touch a croc!
10:30 AM → Head to Bijilo Monkey Park - quick walk with monkeys
12:00 PM → Lunch at Senegambia Strip (many restaurants)
2:00 PM  → Explore Albert Market in Banjul (crafts, spices)
4:00 PM  → Drive to Tanji Fishing Village - watch boats return
6:00 PM  → Sunset dinner at Sanyang Paradise Beach
```

**🚢 COMING VIA BARRA FERRY?**
Start in Banjul, then head coastal:
```
9:00 AM  → Arch 22 & Banjul National Museum
11:00 AM → Albert Market for shopping
1:00 PM  → Taxi to Bakau for Kachikally
3:00 PM  → Bijilo Forest Park
5:00 PM  → Beach bar for sunset
```

**🏛️ WANT HISTORY? (Full Day Trip)**
Go upcountry to see Kunta Kinteh Island:
```
Depart Barra Terminal early morning
→ Boat to Jufureh village (Roots history)
→ Visit Kunta Kinteh Island (UNESCO site)
→ Return late afternoon
```

💡 **Tips:**
- Hire a driver for the day ($50-80) - makes everything easier
- Agree on taxi prices BEFORE getting in
- Bring cash (Dalasi or Euros)"""
    },
    
    # ============== DISTANCES & TRAVEL TIMES ==============
    "distances": {
        "keywords": ["distance", "how far", "how long", "travel time", "hours", "banjul to", "serekunda to", "kololi to", "senegal to gambia", "from senegal"],
        "answer": """**Travel Times & Distances in The Gambia**

**🚗 From Tourist Area (Kololi/Senegambia):**
| Destination | Distance | Time | Taxi Cost |
|-------------|----------|------|-------|
| Banjul | 15 km | 30-45 min | 500-800 GMD |
| Serekunda | 5 km | 10-15 min | 150-250 GMD |
| Airport (BJL) | 24 km | 40-60 min | 1000-1500 GMD |
| Tanji Beach | 25 km | 45 min | 600-900 GMD |
| Brikama | 30 km | 45-60 min | 700-1000 GMD |
| Sanyang | 35 km | 1 hour | 800-1200 GMD |

**🚌 Long Distance (Upcountry):**
| Route | Distance | Time |
|-------|----------|------|
| Banjul → Basse | 400 km | 6-8 hours |
| Serekunda → Janjanbureh | 300 km | 5-6 hours |
| Kololi → Jufureh (by road+boat) | - | 3-4 hours |

**🇸🇳 From Senegal:**
| From | To | Time |
|------|-----|------|
| Dakar → Banjul | - | 5-6 hours (by road+ferry) |
| Cap Skirring → Kololi | - | 3-4 hours |
| Ziguinchor → Banjul | - | 4-5 hours |

**💡 Tips:**
- Gele-gele (minibus) is cheapest: ~25-50 GMD short trips
- Roads are decent on main routes, rough upcountry
- Hire a driver for day trips - very affordable!"""
    },
    
    # ============== BUDGET TRIP ==============
    "budget": {
        "keywords": ["budget trip", "cheap trip", "affordable", "backpacker", "low cost", "save money", "budget ideas", "travel cheap", "inexpensive", "cost saving", "budget travel"],
        "answer": """**How to Travel The Gambia on a Budget**\n\n- **Flights:** Book in advance, compare prices (Brussels Airlines, TUI, Turkish Airlines)\n- **Accommodation:** Choose guesthouses, hostels, or local lodges (from $20/night)\n- **Transport:** Use shared taxis, minibuses (gele-gele), or walk for short distances\n- **Food:** Eat at local restaurants (bantabas), street food, or markets for cheap, tasty meals\n- **Activities:** Enjoy free/low-cost attractions: beaches, markets, local festivals, birdwatching\n- **Money:** Bring some cash, but use ATMs in main towns to avoid high exchange fees\n- **Travel in groups:** Share costs for taxis, tours, and accommodation\n- **Visit in off-season:** Cheaper prices June–October (rainy season)\n\n💡 **Tip:** Bargain politely in markets and with taxi drivers. Local guides can help you find the best deals!\n"""
    },
    
    "visa_cost": {
        "keywords": ["visa cost", "visa fee", "how much visa", "visa price", "entry fee", "exit fee", "tourism levy", "tdl"],
        "answer": """**Entry Costs for The Gambia**

**Tourism Development Levy (TDL):**
- **€20 per person on ENTRY**
- **€20 per person on EXIT**
- **Total: €40 per person** for your trip
- Children under 2: Free
- Payment: Cash (EUR/USD/GBP) or card at airport

**Visa fees:**
- **Visa on arrival (tourism):** FREE for most nationalities (28 days)
- **Visa extension:** Around 500-1000 GMD (~$10-20 USD)
- **Business visa:** Varies by nationality

💡 **Tip:** The €20 levy is mandatory - budget €40 total per person for entry+exit fees."""
    },

    # ============== FLIGHTS & GETTING THERE ==============
    "flights": {
        "keywords": ["flight", "fly", "airline", "airport", "get there", "travel to gambia", "banjul airport"],
        "answer": """**Flights to The Gambia**

**Airport:** Banjul International Airport (BJL) - about 24km from the city center

**Airlines flying to The Gambia:**
- 🇧🇪 **Brussels Airlines** - Via Brussels (popular from Europe)
- 🇹🇷 **Turkish Airlines** - Via Istanbul
- 🇬🇧 **TUI Airways** - Direct from UK (seasonal)
- 🇳🇬 **Air Peace** - From Nigeria
- 🇸🇳 **Air Senegal** - From Dakar (quick 30-min hop)
- 🇲🇦 **Royal Air Maroc** - Via Casablanca
- 🇪🇸 **Vueling/Iberia** - Via Spain

**Flight times:**
- London → Banjul: ~6 hours direct
- Brussels → Banjul: ~6 hours
- New York → Banjul: ~10-12 hours (with connection)

**Best prices:** Book 2-3 months in advance. November-February is peak season (higher prices).

💡 **Tip:** Brussels Airlines often has the best connections from Europe."""
    },

    # ============== ACCOMMODATION ==============
    "hotels": {
        "keywords": ["hotel", "stay", "accommodation", "resort", "lodge", "where to stay", "beach hotel", "book hotel"],
        "answer": """**Where to Stay in The Gambia**

**Popular Areas:**

🏖️ **Kololi/Senegambia Strip** (Most Popular)
- Heart of tourism, restaurants, nightlife
- Hotels: Senegambia Beach Hotel, Kairaba Beach Hotel, Sunset Beach Hotel
- Price range: $50-150/night

🌊 **Kotu Beach**
- Quieter, good for families
- Hotels: Kombo Beach Hotel, Bungalow Beach Hotel
- Price range: $40-100/night

🐊 **Cape Point/Bakau**
- Near Kachikally Crocodile Pool
- More local feel
- Price range: $30-80/night

🏝️ **Bijilo/Kerr Serign**
- Upscale area near nature reserve
- Hotels: Coco Ocean Resort, Ocean Bay Hotel
- Price range: $80-200/night

**Budget Options:**
- Guesthouses and B&Bs: $20-40/night
- Airbnb options available

💡 **Tip:** Book on Booking.com or contact hotels directly for better rates in low season (June-October)."""
    },

    # ============== BEACHES ==============
    "beaches": {
        "keywords": ["beach", "beaches", "swimming", "sand", "ocean", "coast", "best beach"],
        "answer": """**Best Beaches in The Gambia**

🏆 **Top Beaches:**

1. **Kololi Beach** ⭐
   - Most popular tourist beach
   - Beach bars, restaurants, water sports
   - Good for: Social atmosphere, nightlife nearby

2. **Kotu Beach**
   - Calmer waters, good for swimming
   - Less crowded than Kololi
   - Good for: Families, relaxation

3. **Cape Point Beach**
   - Beautiful scenery, local vibe
   - Great for sunset walks
   - Good for: Photography, quiet time

4. **Sanyang Beach**
   - Pristine, less touristy
   - Fishing village atmosphere
   - Good for: Adventure seekers, authentic experience

5. **Kartong Beach**
   - Southernmost beach, near Senegal border
   - Eco-lodges nearby
   - Good for: Nature lovers, bird watching

**Beach Safety:**
- Swimming is generally safe but watch for currents
- Avoid swimming alone or at night
- Some beaches have lifeguards in tourist season

💡 **Tip:** Visit beaches early morning or late afternoon - midday sun is intense!"""
    },

    # ============== WEATHER ==============
    "weather": {
        "keywords": ["weather", "climate", "temperature", "rain", "hot", "cold", "season", "when to visit", "best time"],
        "answer": """**Weather & Best Time to Visit The Gambia**

**Climate:** Tropical with two seasons

☀️ **Dry Season (November - May)** - BEST TIME TO VISIT
- Little to no rain
- Temperatures: 24-32°C (75-90°F)
- Peak tourist season
- Perfect beach weather

🌧️ **Rainy Season (June - October)**
- Heavy rainfall, especially July-September
- Temperatures: 26-33°C (79-91°F)
- Fewer tourists, lower prices
- Lush green landscapes
- Some roads may be difficult

**Month-by-Month:**
| Month | Weather | Tourism |
|-------|---------|---------|
| Nov-Feb | Perfect, cooler | Peak season |
| Mar-May | Hot and dry | Good, less crowded |
| Jun-Oct | Rainy, humid | Low season, budget deals |

💡 **Tip:** December-February offers the best combination of weather and atmosphere. Book early!"""
    },

    # ============== MONEY & CURRENCY ==============
    "money": {
        "keywords": ["money", "currency", "dalasi", "exchange", "atm", "cash", "credit card", "pay", "cost", "expensive", "how much cost"],
        "answer": """**Money & Currency in The Gambia**\n\n**Currency:** Gambian Dalasi (GMD)\n- Current rate: ~$1 USD = 65-70 GMD (check current rates)\n- £1 GBP = ~80-85 GMD\n- €1 EUR = ~75-80 GMD\n\n**Where to Exchange:**\n- Banks (Standard Chartered, Ecobank, Trust Bank)\n- Licensed forex bureaus (often better rates)\n- Hotels (convenient but worse rates)\n- Avoid street money changers\n\n**ATMs:**\n- Available in tourist areas (Kololi, Bakau, Banjul)\n- Withdraw Dalasi with Visa/Mastercard\n- Daily limits typically 5,000-10,000 GMD\n- Carry backup cash - ATMs sometimes run out\n\n**Credit Cards:**\n- Accepted at major hotels and some restaurants\n- Many places are **cash only**\n- Always carry Dalasi for markets, taxis, small shops\n\n**Budget Guide:**\n| Item | Cost |\n|------|------|\n| Local meal | 100-300 GMD ($2-5) |\n| Restaurant meal | 500-1500 GMD ($8-25) |\n| Beer | 75-150 GMD ($1-2.50) |\n| Taxi (short) | 100-200 GMD ($1.50-3) |\n| Taxi (airport) | 1000-1500 GMD ($15-25) |\n\n**Affordability:**\n- The Gambia is the world's 2nd most price competitive destination for travel & tourism (World Economic Forum)\n- Up to 81% more cost effective than some other destinations\n\n*Sources: Community, Culture and Heritage Activities, Invest in Tourism in The Gambia*\n"""
    },

    # ============== SAFETY ==============
    "safety": {
        "keywords": ["safe", "safety", "dangerous", "crime", "security", "tourist safe", "safe for women"],
        "answer": """**Safety in The Gambia**

**Overall:** The Gambia is considered **one of the safest countries in West Africa** for tourists. It's nicknamed "The Smiling Coast" for a reason!

✅ **Generally Safe:**
- Tourist areas (Kololi, Kotu, Bakau) are well-policed
- Violent crime against tourists is rare
- People are genuinely friendly and welcoming

⚠️ **Be Aware Of:**
- **Petty theft** - Watch belongings at beaches/markets
- **"Bumsters"** - Unofficial guides may approach you; a firm "no thanks" works
- **Taxi scams** - Agree on price before getting in
- **Beach vendors** - Can be persistent; be polite but firm

**Tips for Staying Safe:**
- Don't flash expensive jewelry/electronics
- Use hotel safes for valuables
- Stick to well-lit areas at night
- Use registered taxis
- Carry a copy of your passport, not the original

**For Solo Women:**
- Generally safe, but dress modestly (cover shoulders/knees)
- Avoid walking alone at night
- Be cautious of overly friendly strangers

**Emergency Numbers:**
- Police: 117
- Fire: 118  
- Ambulance: 116

💡 **Tip:** The Gambian Tourist Police in Kololi are very helpful - don't hesitate to ask them for assistance!"""
    },

    # ============== TRANSPORT ==============
    "transport": {
        "keywords": ["transport", "taxi", "car", "rent", "bus", "getting around", "uber", "driver"],
        "answer": """**Getting Around The Gambia**

🚕 **Taxis** (Most Common for Tourists)
- Green "tourist taxis" - more expensive but comfortable
- Yellow taxis - local rates, can be shared
- **Always agree on price BEFORE getting in**
- No meters - negotiate!

Typical taxi costs:
- Airport to Kololi: 1000-1500 GMD ($15-25)
- Kololi to Banjul: 500-800 GMD ($8-12)
- Short trips: 100-200 GMD ($1.50-3)

🚐 **Gele-Gele (Shared Minibuses)**
- Very cheap (~25-50 GMD)
- Crowded but authentic experience
- Set routes, no timetable

🚗 **Car Rental**
- Available but roads can be challenging
- 4x4 recommended for upcountry
- International license required
- Cost: $40-80/day

👨‍✈️ **Hire a Driver**
- Best option for day trips
- Around $50-80/day including fuel
- Many hotels can arrange

🛥️ **Pirogue (River Boats)**
- For river crossings and excursions
- Banjul-Barra ferry: ~50 GMD

**No Uber/Bolt** - These apps don't operate in The Gambia yet.

💡 **Tip:** Hire a driver for your whole trip - it's affordable and makes everything easier!"""
    },

    # ============== ATTRACTIONS ==============
    "attractions": {
        "keywords": ["attraction", "see", "do", "visit", "tourist", "sightseeing", "must see", "things to do", "activities"],
        "answer": """**Top Things to See & Do in The Gambia**

🏆 **Must-Visit Attractions:**

1. **Kachikally Crocodile Pool** (Bakau)
   - Sacred pool with friendly crocodiles
   - Touch them for good luck!
   - Entry: ~100 GMD

2. **Abuko Nature Reserve**
   - First national park, easy to access
   - Monkeys, birds, wildlife
   - Entry: ~150 GMD

3. **Kunta Kinteh Island** (UNESCO Site)
   - Historic slave trade site
   - Featured in "Roots"
   - Full day trip from Banjul

4. **Makasutu Culture Forest**
   - Beautiful forest walks
   - Cultural performances
   - Great birdwatching

5. **Bijilo Forest Park** (Monkey Park)
   - Walk among monkeys
   - Just outside Kololi
   - Entry: ~100 GMD

6. **River Gambia Cruise**
   - See hippos, birds, mangroves
   - Full or half-day trips

**Day Trips:**
- Jufureh & James Island (Roots tour)
- Brikama Wood Carvers Market
- Tanji Fishing Village
- Kartong (beach & border town)

**Activities:**
- Birdwatching (560+ species!)
- Fishing trips
- Quad biking
- Cultural village visits
- Cooking classes

💡 **Tip:** Don't miss a boat trip on the River Gambia - the birdlife is incredible!"""
    },

    # ============== FOOD ==============
    "food": {
        "keywords": ["food", "eat", "restaurant", "cuisine", "dish", "meal", "breakfast", "dinner", "local food"],
        "answer": """**Food & Dining in The Gambia**

🍛 **Traditional Gambian Dishes:**

1. **Benachin** (Jollof Rice)
   - One-pot rice with fish/meat & vegetables
   - The national dish!

2. **Domoda**
   - Groundnut (peanut) stew
   - Rich, creamy, delicious

3. **Yassa**
   - Marinated chicken/fish with onions & lemon
   - Tangy and flavorful

4. **Supakanja**
   - Okra soup with palm oil
   - Served with rice or fufu

5. **Afra**
   - Grilled meat (beef/chicken)
   - Street food favorite

**Where to Eat:**

🍽️ **Tourist Area Restaurants (Kololi/Senegambia):**
- Wide variety: African, European, Lebanese, Indian
- Prices: 500-2000 GMD ($8-30) per meal

🏠 **Local "Chop Shops":**
- Authentic Gambian food
- Very affordable: 100-300 GMD ($2-5)
- Look for busy places with locals

🌴 **Beach Bars:**
- Fresh grilled fish
- Casual atmosphere
- Great for sunset

**Food Safety Tips:**
- Drink bottled water (sealed)
- Eat freshly cooked hot food
- Peel fruits yourself
- Avoid ice in drinks outside hotels

**Vegetarian?** Options exist but can be limited - domoda without meat, rice & vegetables are always available.

💡 **Tip:** Try the fresh grilled fish at Sanyang Beach - straight from the fishermen!"""
    },

    # ============== LANGUAGE ==============
    "language": {
        "keywords": ["language", "speak", "english", "mandinka", "wolof", "french", "communicate"],
        "answer": """**Languages in The Gambia**

**Official Language:** English 🇬🇧
- Used in government, education, business
- Most people in tourist areas speak English
- You'll get by fine with just English!

**Local Languages:**
- **Mandinka** - Most widely spoken (40%+)
- **Wolof** - Common, especially in urban areas
- **Fula** - Spoken in rural areas
- **Jola, Serahule** - Regional languages

**Useful Phrases:**

| English | Mandinka | Wolof |
|---------|----------|-------|
| Hello | Salaamaleekum | Na nga def |
| How are you? | I be di? | Na nga def? |
| Fine, thank you | Tanaante | Mangi fi rekk |
| Thank you | Abaraka | Jërëjëf |
| Goodbye | Fo waati kutoo | Ba beneen |
| Yes | Haa | Waaw |
| No | Hani | Déedéet |

**Communication Tips:**
- Greetings are VERY important - always say hello first
- A few local words go a long way - people appreciate the effort
- "Toubab" means foreigner (not offensive)
- French is understood by some due to Senegal proximity

💡 **Tip:** Learn "Salaamaleekum" (peace be upon you) - the universal greeting that opens all doors!"""
    },

    # ============== HEALTH ==============
    "health": {
        "keywords": ["health", "vaccine", "vaccination", "malaria", "hospital", "doctor", "medicine", "sick", "medical", "yellow fever"],
        "answer": """**Health & Vaccinations for The Gambia**
\n💉 **Required Vaccinations:**\n- **Yellow Fever** - Required if coming from an endemic country (certificate checked at airport)\n\n💉 **Recommended Vaccinations:**\n- Hepatitis A & B\n- Typhoid\n- Tetanus-Diphtheria\n- Meningitis (especially dry season)\n- Rabies (if planning bush travel)\n\n🦟 **Malaria Prevention:**\n- **Malaria IS present** in The Gambia\n- Take antimalarials (consult your doctor - Malarone, Doxycycline, or Lariam)\n- Use mosquito repellent (DEET 30%+)\n- Sleep under a mosquito net\n- Wear long sleeves/pants at dusk\n\n**Other Health Tips:**\n- Drink only bottled/purified water\n- Use high SPF sunscreen (sun is strong!)\n- Bring basic medications from home\n- Travel insurance with medical evacuation is recommended\n\n**Medical Facilities:**\n- **MRC Medical Centre** (Fajara) - Good standard\n- **Edward Francis Small Teaching Hospital** (Banjul)\n- Private clinics available in tourist areas\n- Serious cases may require evacuation to Dakar or Europe\n\n**Pharmacies:**\n- Available in main towns\n- Many common medications available without prescription\n- Bring specific medications from home\n\n**Health System & Policy:**\n- The Gambia's health system is supported by national development plans and international organizations\n- Emergency and development plans are in place for health and tourism\n\n*Sources: Recovery-Focused National Development Plan, Official Country Guide*\n"""
    },

    # ============== CULTURE & CUSTOMS ==============
    "culture": {
        "keywords": ["culture", "custom", "tradition", "religion", "dress", "etiquette", "respect", "muslim", "islam", "mandinka", "greeting", "phrase", "hello", "language"],
        "answer": """**Culture & Customs in The Gambia**

🗣️ **Basic Mandinka Greetings:**
Learning a few Mandinka phrases will delight locals!

| English | Mandinka | Pronunciation |
|---------|----------|---------------|
| Hello | *I be di* | ee-bay-dee |
| Good morning | *I suma kori* | ee-soo-ma-kor-ee |
| How are you? | *Here be di?* | hay-ray-bay-dee |
| I'm fine | *Here dorong* | hay-ray-doh-rong |
| Thank you | *Abaraka* | ah-ba-ra-ka |
| Please | *Dukare* | doo-ka-ray |
| Goodbye | *Fo tuma doo* | foh-too-ma-doh |
| Yes | *Haa* | hah |
| No | *Hani* | ha-nee |
| How much? | *Jelu?* | jay-loo |
| Too expensive | *A songo jata* | ah-song-oh-ja-ta |
| Water | *Ji* | jee |
| Food | *Domoroo* | doh-moh-roo |

💡 **Tip:** Even attempting "Abaraka" (thank you) will earn you big smiles!

🕌 **Religion:**
- ~95% Muslim, but very tolerant and relaxed
- Christian minority (~4%)
- Traditional beliefs coexist peacefully

👔 **Dress Code:**
- Generally conservative outside tourist areas
- Cover shoulders and knees when visiting villages/markets
- Swimwear only at beach/pool
- Men can wear shorts in tourist areas

🤝 **Greetings & Etiquette:**
- **Greetings are essential** - take time to say hello properly
- Use right hand for giving/receiving (left hand is considered unclean)
- Handshakes are common; slight bow shows respect
- Ask permission before photographing people
- Respect is shown to elders

🍽️ **Social Customs:**
- Tea ceremony (Attaya) is important - accepting tea is polite
- Removing shoes when entering homes
- Eating from communal bowls with right hand (in traditional settings)
- Bargaining is expected at markets

❌ **Things to Avoid:**
- Public displays of affection
- Criticizing religion or government
- Pointing with index finger (use whole hand)
- Showing bottom of feet to people
- Walking in front of someone praying

**During Ramadan:**
- Be respectful - don't eat/drink publicly during daylight hours
- Restaurants still serve tourists
- Evenings are festive after iftar (breaking fast)

💡 **Tip:** Gambians are incredibly friendly - a smile and greeting will be warmly received!"""
    },

    # ============== FESTIVALS ==============
    "festivals": {
        "keywords": ["festival", "event", "celebration", "holiday", "party", "music", "roots"],
        "answer": """**Festivals & Events in The Gambia**
\n🎭 **Major Festivals:**\n- **International Roots Festival** (May/June): Celebrates African heritage & diaspora connections, music, dance, cultural events, and the history of the slave trade\n- **Kartong Festival** (February): Cultural display of music & dance, border communities of Gambia & Senegal, traditional Djembe drumming workshops\n- **Janjanbureh Kankurang Festival** (January): Ancient Mandinka tradition, masked figure (Kankurang) ceremonies, UNESCO Intangible Heritage\n\n🎵 **Music Events:**\n- Live music at hotels year-round\n- Traditional drumming performances\n- Modern Afro-beats scene\n\n📅 **Public Holidays:**\n- New Year's Day (Jan 1)\n- Independence Day (Feb 18) - Big celebration!\n- Good Friday & Easter Monday\n- Eid al-Fitr (end of Ramadan)\n- Eid al-Adha (Feast of Sacrifice)\n- Christmas Day (Dec 25)\n\n**Weekly Events:**\n- Wrestling matches (traditional sport) - weekends\n- Sunday markets at various villages\n\n**National Calendar of Events:**\n- The Gambia maintains a national calendar of cultural, sports, and tourism events\n\n*Sources: Official Country Guide, Tourism Project Reports*\n"""
    },

    # ============== SHOPPING ==============
    "shopping": {
        "keywords": ["shopping", "buy", "market", "souvenir", "craft", "bargain", "gift"],
        "answer": """**Shopping in The Gambia**

🛍️ **What to Buy:**

**Traditional Crafts:**
- Wood carvings (masks, statues)
- Batik fabric & clothing
- Leather goods (bags, sandals)
- Woven baskets
- Djembe drums
- Traditional jewelry

**Local Products:**
- Cashew nuts (locally grown)
- Baobab products
- Shea butter
- Local honey
- Spices

🏪 **Where to Shop:**

**Albert Market (Banjul)**
- Largest market in the country
- Everything from food to crafts
- Authentic local experience
- Bargaining essential!

**Brikama Wood Carvers Market**
- Best for wood carvings
- Watch artisans at work
- Good prices

**Senegambia Craft Market**
- Touristy but convenient
- Fixed prices at some stalls
- Good for quick shopping

**Banjul Craft Market**
- Near the ferry terminal
- Variety of souvenirs

💰 **Bargaining Tips:**
- Start at 40-50% of asking price
- Be friendly and patient
- Walk away if price too high (they often call you back)
- Don't show too much interest
- Compare prices at different stalls first

💡 **Tip:** Buy a few things from Brikama market - the quality is better and prices lower than tourist areas!"""
    },

    # ============== GENERAL / ABOUT ==============
    "about_gambia": {
        "keywords": ["about gambia", "tell me about", "what is gambia", "gambia like", "overview", "information", "introduce", "basics", "general"],
        "answer": """**🇬🇲 About The Gambia**\n\nThe Gambia is known as the **'Smiling Coast of Africa'** for its friendly people and vibrant culture.\n\n- **Location:** West Africa, surrounded by Senegal except for its Atlantic coast\n- **Area:** 11,295 km² (4,361 sq. miles)\n- **Capital:** Banjul\n- **Population:** ~2.76 million (2024)\n- **Languages:** English (official), Mandinka, Wolof, Peul, and others\n- **Currency:** Dalasi (GMD)\n- **Timezone:** GMT\n- **Climate:** Sub-tropical; dry season (Nov-Jun), wet season (Jul-Oct), avg. 27°C\n\n**Highlights:**\n- Diverse coastline, rich culture, and history\n- National parks, wildlife, and UNESCO sites (e.g., Kunta Kinteh Island)\n- Renowned for hospitality, tolerance, and stability\n- 80km of coastline and a navigable river\n- 7 ethnic groups living peacefully together\n- One of Africa's most stable democracies\n\n**Tourism Reputation:**\n- Competitive, affordable, and safe destination\n- Strong demand: 14% annual increase in arrivals (2001-2019)\n- Vibrant culture and young talent\n\n**Did You Know?**\n- The Ninki Nanka legend is central to local culture\n- The River Gambia runs through the entire country\n\n*Sources: Gambia Official Country Guide (2022), Gambia Travel Guide, Gambia-brochure, GMB in italiano*\n"""
    },

    # ============== COMMUNICATION ==============
    "internet": {
        "keywords": ["internet", "wifi", "phone", "sim", "data", "mobile", "call"],
        "answer": """**Internet & Phone in The Gambia**

📱 **Mobile Networks:**
- **Africell** - Best coverage, recommended
- **Qcell** - Good alternative
- **Comium** - Smaller network

**Getting a SIM Card:**
- Buy at airport or any phone shop
- Cost: 50-100 GMD (~$1-2)
- Data packages: 1GB for ~150-300 GMD (~$3-5)
- Bring passport for registration

📶 **Internet Quality:**
- 4G available in tourist areas
- Can be slow during peak times
- Mobile data is often more reliable than WiFi

**Hotel WiFi:**
- Most tourist hotels have WiFi
- Quality varies - often slow
- Sometimes limited to lobby

**Tips:**
- WhatsApp works great for calls/messages
- Download offline maps before arriving
- Mobile data is affordable - buy a local SIM

💡 **Tip:** Get an Africell SIM at the airport - makes everything easier for maps, rides, and staying in touch!"""
    },

    # ============== NIGHTLIFE ==============
    "nightlife": {
        "keywords": ["nightlife", "bar", "club", "party", "night", "drink", "beer", "entertainment"],
        "answer": """**Nightlife in The Gambia**

🌙 **Main Nightlife Area:** Senegambia Strip (Kololi)

🍺 **Popular Spots:**

**Bars & Lounges:**
- Churchill's (British-style pub)
- Poco Loco (beach bar)
- Senegambia Beach Hotel bars
- Various beach bars along Kololi

**Clubs:**
- Duplex (popular nightclub)
- Jokor (dancing)
- Club 7 (local scene)

**Live Music:**
- Many hotels have live bands
- Traditional drumming shows
- Reggae and Afro-beats nights

**Tips:**
- Most action starts after 10pm
- Dress code is casual but smart
- Drinks are affordable ($2-5)
- Always negotiate taxi fare home

💡 **Tip:** Senegambia Strip on weekends has the best atmosphere!"""
    },

    # ============== TIPPING ==============
    "tipping": {
        "keywords": ["tipping", "tip", "gratuity", "how much tip", "should i tip", "service charge"],
        "answer": """**Tipping Guide for The Gambia**

💵 **General Guidelines:**

**Restaurants:**
- 10% is appreciated but not mandatory
- Check if service charge is included

**Hotels:**
- Porters: 20-50 GMD per bag
- Housekeeping: 50-100 GMD per day
- Concierge: Based on service

**Guides & Drivers:**
- Day tour guide: 200-500 GMD
- Multi-day: 500+ GMD per day

🏖️ **Beach Services:**
- Sun lounger attendants: 25-50 GMD
- Beach vendors (if buying): Round up

**Tips for Tipping:**
- Carry small notes (5, 10, 20, 50 GMD)
- Tip in Dalasi, not foreign currency
- Tip directly to the person who served you
- A smile and "Abaraka" (thank you) goes far!

💡 **Tip:** Keep a separate pocket with small notes for easy tipping throughout the day!"""
    },

    # ============== PACKING LIST ==============
    "packing": {
        "keywords": ["packing", "pack", "bring", "luggage", "what to bring", "packing list", "clothes", "essentials"],
        "answer": """**Packing List for The Gambia** 🧳

**☀️ Clothing (Light & Modest):**
- Lightweight, breathable clothes
- Long pants/skirts for cultural sites
- Swimwear (for beach/pool)
- Cover-up for leaving beach areas
- Light cardigan/jacket (evenings can be cool)
- Comfortable walking sandals
- Flip-flops for beach
- Hat or cap for sun protection

**🧴 Health & Sun:**
- Sunscreen SPF 30+
- Insect repellent (DEET)
- Malaria tablets
- Personal medications
- First aid basics
- Hand sanitizer

**🔌 Electronics:**
- UK-style adapter (Type G)
- Power bank
- Camera
- Phone with offline maps

**📄 Documents:**
- Passport (6+ months validity)
- Travel insurance docs
- Hotel confirmations
- Copies of documents (digital + paper)

**💰 Money:**
- Some EUR/USD/GBP cash
- Credit/debit card for ATMs

💡 **Tip:** Pack light - you can buy clothes cheaply at local markets!"""
    },

    # ============== ECOTOURISM ==============
    "ecotourism": {
        "keywords": ["ecotourism", "eco-tourism", "nature travel", "responsible travel", "sustainable tourism", "green travel"],
        "answer": """**🌱 Ecotourism in The Gambia**

Tourism is a major industry in The Gambia, and ecotourism is growing!

**What is Ecotourism?**
Environmentally and socially responsible travel to natural areas that promotes conservation and benefits local people.

**Eco-Friendly Activities:**
- Bird watching (560+ species!)
- River cruises through mangroves
- Nature reserve visits
- Eco-lodge stays
- Community-based tourism

**Top Eco Destinations:**
- Makasutu Culture Forest
- Abuko Nature Reserve
- River Gambia National Park
- Tanji Bird Reserve
- Kartong eco-lodges

**Tips for Eco-Travelers:**
- Choose community-based tours
- Respect wildlife and habitats
- Support local businesses
- Minimize plastic use
- Stay at eco-certified lodges

💡 **Tip:** Community-based tourism supports local livelihoods while preserving culture!"""
    },

    # ============== ITINERARIES ==============
    "itinerary_3day": {
        "keywords": ["3 day", "3-day", "three day", "weekend", "short trip", "quick visit", "itinerary"],
        "answer": """**3-Day Gambia Itinerary** 🗓️

**Day 1 - Arrival & Beach**
- ✈️ Arrive at Banjul Airport
- 🚕 Transfer to hotel (Kololi/Senegambia area)
- 🏖️ Relax at the beach
- 🌅 Sunset drinks at a beach bar
- 🍽️ Dinner at a local restaurant

**Day 2 - Culture & Nature**
- 🐒 Morning: Visit Bijilo Forest Park (monkeys!)
- 🏛️ Afternoon: Banjul city tour (Albert Market, Arch 22)
- 🐊 Optional: Kachikally Crocodile Pool
- 🎭 Evening: Traditional music/drumming show

**Day 3 - River & Departure**
- 🚤 Morning: River boat trip or fishing village visit
- 🛍️ Shopping for souvenirs at craft market
- ✈️ Transfer to airport

💡 **Tips:**
- Stay in Kololi for easy beach access
- Book airport transfer in advance
- Don't miss the sunset on Day 1!"""
    },

    "itinerary_7day": {
        "keywords": ["7 day", "7-day", "one week", "week trip", "week itinerary", "full week"],
        "answer": """**7-Day Gambia Itinerary** 🗓️

**Day 1 - Arrival**
- ✈️ Arrive, transfer to hotel
- 🏖️ Beach time & relax
- 🌅 Welcome sunset drinks

**Day 2 - Beaches & Wildlife**
- 🏖️ Morning: Beach relaxation
- 🐒 Afternoon: Bijilo Forest Park
- 🍛 Try local Gambian food

**Day 3 - Banjul & Culture**
- 🏛️ Banjul city tour
- 🛒 Albert Market shopping
- 🏰 Arch 22 viewpoint
- 🐊 Kachikally Crocodile Pool

**Day 4 - River Adventure**
- 🚤 Full day river cruise
- 🐦 Bird watching
- 🌿 Mangrove exploration
- 🎣 Fishing village visit

**Day 5 - Roots & History**
- 🚗 Day trip to Jufureh (Roots)
- ⛓️ James Island (UNESCO site)
- 📖 Learn about slave trade history

**Day 6 - Relax & Explore**
- 🏖️ Beach day (try water sports)
- 💆 Spa treatment
- 🛍️ Craft market shopping
- 🌙 Nightlife in Senegambia

**Day 7 - Departure**
- ☀️ Final morning swim
- 🛍️ Last-minute shopping
- ✈️ Airport transfer

💡 **Pro Tips:**
- Book Roots trip in advance
- Wednesdays are best for Brikama market
- Save energy for nightlife on Day 6!"""
    },

    "itinerary_budget": {
        "keywords": ["budget trip", "budget ideas", "cheap trip", "affordable trip", "backpacker", "low cost", "save money", "budget gambia", "cheap gambia"],
        "answer": """**Budget Gambia Trip Guide** 💰

**Accommodation (~$15-30/night):**
- Guesthouses in Kololi
- Airbnb rooms
- Budget hotels inland

**Food (~$5-10/day):**
- Local "chop shops" - 50-100 GMD/meal
- Street food (safe and delicious)
- Cook at guesthouse (market shopping)
- Avoid tourist restaurant markups

**Transport:**
- Shared taxis (gele-gele) - 7-25 GMD
- Green taxis (negotiate!) - 50-200 GMD
- Walk in tourist areas

**Free/Cheap Activities:**
- Beach (free!)
- Walking tours
- People watching at markets
- Sunset at beach bars (buy one drink)
- River bank walks

**Budget Breakdown (per day):**
- Accommodation: $20
- Food: $10
- Transport: $5
- Activities: $5-10
- **Total: ~$40-45/day**

**Money-Saving Tips:**
- Exchange at forex bureaus (better rates)
- Bargain at markets (start at 50%)
- Buy water in large bottles
- Eat where locals eat
- Share taxis with others

💡 **Tip:** The Gambia is already affordable - you can travel well on a budget here!"""
    },

    # ============== EMERGENCY CONTACTS ==============
    "emergency": {
        "keywords": ["emergency", "help", "police", "ambulance", "hospital", "embassy", "lost passport", "crime", "accident"],
        "answer": """**Emergency Contacts in The Gambia** 🆘\n\n**Emergency Numbers:**\n- 📞 **Police:** 117\n- 🚑 **Ambulance:** 116\n- 🔥 **Fire:** 118\n\n**Hospitals:**\n- **EFSTH (Banjul):** +220 422 8223\n- **MRC Hospital:** +220 449 5442\n- **Afrimed Clinic (Kololi):** +220 446 0946\n\n**Embassies/Consulates:**\n- 🇬🇧 **British High Commission**: +220 449 5133/4\n- 🇺🇸 **US Embassy**: +220 439 2856\n- 🇪🇺 **EU Delegation**: +220 449 5146\n- 🇮🇹 **Italian Consular Services:** No embassy in Gambia; consular services via Dakar, Senegal\n\n**Lost Passport:**\n1. Report to police (get report)\n2. Contact your embassy\n3. Get emergency travel document\n\n**Tourist Police:**\n- Based at major tourist areas\n- Helpful and English-speaking\n- Report any issues to them\n\n**Useful Tips:**\n- Save embassy number in phone\n- Keep photo of passport on phone\n- Know your hotel address\n- Travel insurance is essential\n\n*Sources: GMB in italiano, Official Country Guide*\n"""
    },

    # ============== TRIP PLANNER ==============
    "plan_trip": {
        "keywords": ["plan trip", "plan my trip", "help me plan", "planning trip", "trip planner", "plan a trip", "how to plan"],
        "answer": """**Plan Your Gambia Trip** 🗓️\n\n**Step 1: Choose Your Dates**\n- **Best Season:** November - May (dry season)\n- **Peak:** December - February (book early!)\n- **Budget:** June - October (rainy but cheaper)\n\n**Step 2: Book Flights ✈️**\n- [Skyscanner](https://www.skyscanner.com) - Compare all airlines\n- [Google Flights](https://www.google.com/flights) - Track prices\n- [Brussels Airlines](https://www.brusselsairlines.com) - Main EU carrier\n- [TUI](https://www.tui.co.uk) - UK direct flights\n\n**Step 3: Book Accommodation 🏨**\n- [Booking.com](https://www.booking.com) - Best selection\n- [Airbnb](https://www.airbnb.com) - Local stays\n- [Expedia](https://www.expedia.com) - Flight + hotel deals\n- [Hotels.com](https://www.hotels.com) - Rewards program\n\n**Step 4: Plan Activities 🎯**\n- Ask me about: \"3-day itinerary\" or \"7-day itinerary\"\n- Popular: Beaches, River trips, Roots tour, Bird watching\n\n**Step 5: Essentials Checklist ✅**\n- [ ] Passport (6+ months validity)\n- [ ] €40 cash for entry/exit levy\n- [ ] Travel insurance\n- [ ] Yellow fever vaccine (if required)\n- [ ] Malaria tablets\n\n**Quick Trip Ideas:**\n- 🏖️ **Beach Holiday:** 5-7 days in Kololi\n- 🌍 **Cultural Tour:** 7-10 days with Roots visit\n- 💰 **Budget Trip:** 3-5 days backpacking\n\n**Tourism Industry Associations:**\n- Gambia Hotel Association\n- Licensed Tour Guide Associations\n- Community-based tourism organizations\n\n*Sources: Official Country Guide, Discover Gambia Travel Assistant, Gambia-brochure*\n"""
    },
}

# ============== HELPER FUNCTIONS ==============

def correct_spelling(query: str) -> str:
    """Correct common misspellings in the query."""
    words = query.lower().split()
    corrected = []
    for word in words:
        # Remove punctuation for matching
        clean_word = word.strip('?.,!')
        if clean_word in SPELLING_CORRECTIONS:
            corrected.append(SPELLING_CORRECTIONS[clean_word])
        else:
            corrected.append(clean_word)
    return ' '.join(corrected)


def calculate_similarity(word1: str, word2: str) -> float:
    """Calculate similarity between two words (0 to 1)."""
    if word1 == word2:
        return 1.0
    
    # Check if one contains the other
    if word1 in word2 or word2 in word1:
        return 0.8
    
    # Simple character overlap ratio
    set1 = set(word1)
    set2 = set(word2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    
    if union == 0:
        return 0.0
    
    jaccard = intersection / union
    
    # Bonus for same starting characters
    prefix_bonus = 0
    for i in range(min(len(word1), len(word2), 3)):
        if word1[i] == word2[i]:
            prefix_bonus += 0.1
        else:
            break
    
    return min(jaccard + prefix_bonus, 1.0)


def find_topic_from_aliases(query: str) -> tuple[str | None, float]:
    """Find topic using aliases with fuzzy matching. Returns (topic, confidence)."""
    query_lower = query.lower()
    query_words = [w.strip('?.,!') for w in query_lower.split()]
    
    best_topic = None
    best_score = 0.0
    
    for topic, aliases in TOPIC_ALIASES.items():
        topic_score = 0.0
        
        for alias in aliases:
            alias_words = alias.split()
            
            # Check for exact phrase match
            if alias in query_lower:
                topic_score = max(topic_score, 1.0)
                continue
            
            # Check for word-level matches
            for query_word in query_words:
                for alias_word in alias_words:
                    if query_word == alias_word:
                        topic_score = max(topic_score, 0.9)
                    elif len(query_word) > 3 and len(alias_word) > 3:
                        sim = calculate_similarity(query_word, alias_word)
                        if sim > 0.7:
                            topic_score = max(topic_score, sim * 0.8)
        
        if topic_score > best_score:
            best_score = topic_score
            best_topic = topic
    
    return best_topic, best_score


def is_followup_question(query: str) -> bool:
    """Detect if a query is a follow-up question."""
    query_lower = query.lower().strip()
    
    # Very short queries are often follow-ups
    if len(query_lower.split()) <= 3:
        return True
    
    # Check for follow-up patterns
    for pattern in FOLLOWUP_PATTERNS:
        if query_lower.startswith(pattern) or f" {pattern} " in f" {query_lower} ":
            return True
    
    # Starts with pronoun without context
    if query_lower.split()[0] in ['it', 'that', 'this', 'they', 'there', 'the']:
        return True
    
    return False


def enhance_query_with_context(query: str, previous_topic: str | None, previous_query: str | None) -> str:
    """Enhance a follow-up query with context from previous conversation."""
    if not previous_topic:
        return query
    
    query_lower = query.lower()
    
    # Map topic to context keywords
    topic_context = {
        "visa": "visa entry requirements",
        "flights": "flights airlines airport",
        "hotels": "hotels accommodation stay",
        "beaches": "beaches coast swimming",
        "weather": "weather climate season",
        "money": "money currency dalasi exchange",
        "safety": "safety security crime",
        "transport": "transport taxi getting around",
        "attractions": "attractions things to do sightseeing",
        "food": "food restaurants cuisine eating",
        "language": "language speaking communication",
        "health": "health medical vaccines malaria",
        "culture": "culture customs traditions religion",
        "festivals": "festivals events celebrations",
        "shopping": "shopping markets souvenirs",
        "internet": "internet phone wifi sim",
        "nightlife": "nightlife bars clubs drinks",
    }
    
    context = topic_context.get(previous_topic, previous_topic)
    
    # Add context to query
    enhanced = f"{context} {query}"
    return enhanced


def get_suggestions_for_query(query: str) -> list[tuple[str, str]]:
    """Get "Did you mean...?" suggestions for an unclear query."""
    suggestions = []
    query_lower = query.lower()
    query_words = [w.strip('?.,!') for w in query_lower.split() if len(w) > 2]
    
    # Check each topic for partial matches
    for topic, aliases in TOPIC_ALIASES.items():
        for alias in aliases[:5]:  # Check first 5 aliases
            for query_word in query_words:
                if len(query_word) > 3:
                    sim = calculate_similarity(query_word, alias)
                    if 0.5 < sim < 0.9:  # Partial match, not exact
                        # Get display name for topic
                        display_names = {
                            "visa": "🛂 Visa & Entry Requirements",
                            "flights": "✈️ Flights & Airlines",
                            "hotels": "🏨 Hotels & Accommodation",
                            "beaches": "🏖️ Beaches",
                            "weather": "🌤️ Weather & Best Time to Visit",
                            "money": "💰 Money & Currency",
                            "safety": "🛡️ Safety",
                            "transport": "🚕 Transport & Getting Around",
                            "attractions": "🎭 Attractions & Things to Do",
                            "food": "🍛 Food & Restaurants",
                            "language": "🗣️ Language",
                            "health": "💉 Health & Vaccinations",
                            "culture": "🕌 Culture & Customs",
                            "festivals": "🎪 Festivals & Events",
                            "shopping": "🛍️ Shopping",
                            "internet": "📱 Internet & Phone",
                            "nightlife": "🌙 Nightlife",
                        }
                        display = display_names.get(topic, topic.title())
                        if (topic, display) not in suggestions:
                            suggestions.append((topic, display))
                        break
    
    return suggestions[:3]  # Return top 3 suggestions


def find_best_faq(query: str, previous_topic: str = None, previous_query: str = None) -> dict | None:
    """
    Find the FAQ that best matches the user's query.
    
    Returns dict with:
    - answer: The FAQ answer
    - topic: The matched topic
    - confidence: Match confidence (0-1)
    - suggestions: List of "did you mean" suggestions if low confidence
    - is_followup: Whether this was detected as a follow-up
    """
    original_query = query
    query_lower = query.lower().strip()
    
    # Step 1: Correct spelling
    corrected_query = correct_spelling(query_lower)
    was_corrected = corrected_query != query_lower
    
    # Step 2: Check if this is a follow-up question
    is_followup = is_followup_question(query_lower)
    
    # Step 3: If follow-up, enhance with previous context
    if is_followup and previous_topic:
        corrected_query = enhance_query_with_context(corrected_query, previous_topic, previous_query)
    
    # Step 4: Find topic using aliases (fuzzy matching)
    topic, confidence = find_topic_from_aliases(corrected_query)
    
    # Step 5: Get the FAQ answer
    result = {
        "answer": None,
        "topic": topic,
        "confidence": confidence,
        "suggestions": [],
        "is_followup": is_followup,
        "was_corrected": was_corrected,
        "corrected_query": corrected_query if was_corrected else None,
    }
    
    if topic and confidence >= 0.7:
        # Good match - return answer
        if topic in GAMBIA_FAQS:
            result["answer"] = GAMBIA_FAQS[topic]["answer"]
        return result
    
    elif topic and confidence >= 0.5:
        # Medium confidence - return answer but with note
        if topic in GAMBIA_FAQS:
            result["answer"] = GAMBIA_FAQS[topic]["answer"]
        result["suggestions"] = get_suggestions_for_query(original_query)
        return result
    
    else:
        # Low/no confidence - provide suggestions
        result["suggestions"] = get_suggestions_for_query(original_query)
        
        # If we have suggestions, still try to give a partial answer
        if result["suggestions"]:
            top_suggestion = result["suggestions"][0][0]
            if top_suggestion in GAMBIA_FAQS:
                result["topic"] = top_suggestion
                result["answer"] = None  # Don't auto-answer, just suggest
        
        return result


def get_faq_topics() -> list:
    """Get list of available FAQ topics for UI."""
    return [
        ("🛂 Visa & Entry", "visa"),
        ("✈️ Flights", "flights"),
        ("🏨 Hotels", "hotels"),
        ("🏖️ Beaches", "beaches"),
        ("🌤️ Weather", "weather"),
        ("💰 Money", "money"),
        ("🛡️ Safety", "safety"),
        ("🚕 Transport", "transport"),
        ("🎭 Attractions", "attractions"),
        ("🍛 Food", "food"),
        ("🗣️ Language", "language"),
        ("💉 Health", "health"),
        ("🕌 Culture", "culture"),
        ("🎪 Festivals", "festivals"),
        ("🛍️ Shopping", "shopping"),
        ("📱 Internet", "internet"),
        ("🌙 Nightlife", "nightlife"),
    ]


def get_faq_by_topic(topic: str) -> str | None:
    """Get FAQ answer by topic key."""
    if topic in GAMBIA_FAQS:
        return GAMBIA_FAQS[topic]["answer"]
    return None


# Quick test
if __name__ == "__main__":
    print("=" * 60)
    print("Testing FAQ System with Fuzzy Matching")
    print("=" * 60)
    
    # Test queries including misspellings
    test_queries = [
        ("What are the viza requirements?", None),  # Misspelling
        ("Best beachs in Gambia", None),  # Misspelling
        ("Is it safe?", None),  # Short query
        ("Where can I eat local food?", None),
        ("hotles near the airport", None),  # Misspelling
        ("tell me more", "beaches"),  # Follow-up
        ("what about safety?", "visa"),  # Follow-up with context
        ("how much does it cost", "hotels"),  # Follow-up
        ("asdfgh", None),  # Nonsense
    ]
    
    for query, prev_topic in test_queries:
        result = find_best_faq(query, previous_topic=prev_topic)
        print(f"\n📝 Query: '{query}'" + (f" (prev: {prev_topic})" if prev_topic else ""))
        if result:
            print(f"   Topic: {result['topic']}")
            print(f"   Confidence: {result['confidence']:.2f}")
            print(f"   Is follow-up: {result['is_followup']}")
            if result['was_corrected']:
                print(f"   Corrected to: {result['corrected_query']}")
            if result['answer']:
                print(f"   ✅ Answer: {result['answer'][:80]}...")
            if result['suggestions']:
                print(f"   💡 Suggestions: {[s[1] for s in result['suggestions']]}")
