"""
🇬🇲 THE GAMBIA COMPLETE KNOWLEDGE BASE
Expert-level conversational Q&A system for travelers
Every answer is written like a helpful local guide talking to you
"""

# =============================================================================
# SMART ANSWER DATABASE - Conversational, Expert, Helpful
# =============================================================================

QUICK_ANSWERS = {
    # ==================== VISA & ENTRY ====================
    "do i need a visa": """**Quick Answer: Probably NOT!**

Most tourists don't need to apply for a visa beforehand. Here's the deal:

🟢 **NO VISA NEEDED:**
- ECOWAS countries (Nigeria, Ghana, Senegal, etc.) - Just show your passport
- UK, EU, USA, Canada, Australia, NZ - Visa on arrival (FREE, 28 days)

⚠️ **But heads up:** You'll pay a **€20 Tourism Levy on entry AND exit** (€40 total). Have cash ready!

What's your nationality? I can give you specifics.""",

    "visa": """**Visa for The Gambia - The Simple Version:**

✅ **You probably don't need one beforehand!**

| Your Country | What You Need |
|--------------|---------------|
| ECOWAS (Nigeria, Ghana, Senegal...) | Just passport - no visa! |
| UK, USA, Canada, Australia, EU | Visa on arrival (FREE) |
| Most others | Visa on arrival (FREE) |

📋 **What to bring:**
- Passport valid 6+ months
- Return ticket
- €20 cash for entry levy (€40 total with exit)

**Stay:** 28 days, extendable at Immigration in Banjul.""",

    "ecowas visa": """**ECOWAS Citizens - You're Golden! 🎉**

If you're from Nigeria, Ghana, Senegal, Sierra Leone, Liberia, Guinea, Mali, Niger, Burkina Faso, Togo, Benin, Côte d'Ivoire, Guinea-Bissau, or Cape Verde:

✅ **NO VISA needed - ever!**
✅ Just bring your valid passport
✅ Free movement under ECOWAS protocol

⚠️ **Still pay:** €20 Tourism Levy at entry + €20 at exit

That's it. Welcome home, neighbor! 🤝""",

    "uk visa": """**UK Citizens - Super Easy Entry! 🇬🇧**

✅ **Visa on arrival - FREE**
✅ **28 days** automatically
✅ Just need valid passport (6+ months)

💰 **Costs:**
- Visa: FREE
- Tourism Levy: €20 in + €20 out = **€40 total**

Many direct flights from London Gatwick (TUI, seasonal). About 6 hours flight time.

Need to stay longer? Extend at Immigration Banjul for ~$15.""",

    "us visa": """**US Citizens - Easy Entry! 🇺🇸**

✅ **Visa on arrival - FREE**
✅ **28 days** automatically
✅ Valid US passport required (6+ months validity)

💰 **Only cost:** €40 Tourism Levy (€20 in, €20 out)

**Getting there:** No direct flights from US. Best routes:
- Via Brussels (Brussels Airlines)
- Via Istanbul (Turkish Airlines)
- Via Casablanca (Royal Air Maroc)

Total travel time: 10-14 hours with connection.""",

    "tourism levy": """**Tourism Development Levy (TDL) - Don't Get Caught Off Guard!**

💰 **€20 per person ENTERING**
💰 **€20 per person LEAVING**
= **€40 total per person**

**Payment:**
- Cash: EUR, USD, or GBP accepted
- Card: Sometimes works, don't rely on it
- **Have cash ready!**

**Who's exempt:**
- Children under 2
- Diplomats
- Returning residents

This catches many tourists by surprise. Budget for it!""",

    # ==================== SAFETY ====================
    "is gambia safe": """**Yes, The Gambia is safe for tourists! 🛡️**

It's called "The Smiling Coast" for good reason. Here's the real talk:

✅ **Safe:**
- Tourist areas (Kololi, Kotu, Bakau) well-policed
- Violent crime against tourists very rare
- People genuinely friendly and helpful
- One of West Africa's safest countries

⚠️ **Normal precautions:**
- Don't flash expensive items
- Agree taxi prices before getting in
- "Bumsters" (unofficial guides) can be persistent - firm "no thanks" works
- Use hotel safe for valuables

**Solo women:** Generally safe. Dress modestly, avoid walking alone at night.

**Emergency:** Police 117, Ambulance 116""",

    "safe for women": """**Solo Female Travel in The Gambia:**

✅ **Generally safe!** Many women travel here solo.

**Tips:**
- Dress modestly (cover shoulders/knees outside beach)
- Avoid walking alone after dark
- "Bumsters" may try to chat you up - be firm but polite
- Stick to tourist areas at night
- Tell hotel if anyone bothers you

**Good areas:** Kololi, Kotu, Bakau beach areas

Gambian people are protective of guests. If uncomfortable, locals will often help. The Tourist Police in Kololi are very responsive.""",

    "bumsters": """**Bumsters - What You Need to Know:**

"Bumsters" are unofficial guides/beach boys who approach tourists offering:
- Tours, taxis, friendship
- "Just want to practice English"
- Companionship

**How to handle:**
- Firm, polite "No thank you"
- Don't engage in long conversations if not interested
- They're usually harmless, just persistent
- If someone won't leave you alone, walk toward a hotel/restaurant

**Want a guide?** Ask your hotel to recommend a licensed one instead. Costs $20-40/day and worth it!""",

    # ==================== WEATHER & TIMING ====================
    "best time to visit": """**Best Time to Visit The Gambia:**

🏆 **November to February** = PERFECT
- Dry, sunny, 24-30°C
- Peak birdwatching season
- Christmas/New Year popular
- Book hotels early!

👍 **March to May** = Good
- Hotter (30-35°C) but dry
- Fewer crowds, good deals
- Still great for beach

🌧️ **June to October** = Rainy Season
- Heavy rains, especially July-Sept
- Lush green landscapes
- Cheapest prices, few tourists
- Some roads difficult

**My recommendation:** Come in November or early December - perfect weather, not too crowded yet.""",

    "weather": """**Gambia Weather - Simple Breakdown:**

☀️ **Dry Season (Nov-May):** Hot, sunny, no rain
- Nov-Feb: 24-30°C (75-86°F) - Most comfortable
- Mar-May: 30-40°C (86-104°F) - Very hot!

🌧️ **Rainy Season (Jun-Oct):** Hot, humid, daily storms
- Short intense rains, usually afternoon
- July-Sept wettest
- 26-33°C (79-91°F)

**Right now?** Always sunny and warm! Pack light clothes, sunscreen, hat.""",

    "rainy season": """**Rainy Season (June-October):**

**What to expect:**
- Short, heavy downpours (usually 1-2 hours)
- Often in afternoon/evening
- Mornings usually clear
- Very humid

**Pros:**
- Cheapest hotel rates (50% off!)
- Few tourists - locals love this
- Landscape is lush green
- Great for photography

**Cons:**
- Some beach erosion
- Upcountry roads can be difficult
- More mosquitoes

**Verdict:** Still enjoyable if you don't mind occasional rain. Bring umbrella!""",

    # ==================== MONEY ====================
    "money": """**Money in The Gambia - What You Need:**

💵 **Currency:** Gambian Dalasi (GMD)
- $1 USD ≈ 65-70 GMD
- €1 EUR ≈ 70-75 GMD  
- £1 GBP ≈ 80-85 GMD

**Best approach:**
1. Bring some EUR/USD/GBP cash
2. Exchange at forex bureaus (better than banks/hotels)
3. Use ATMs for Dalasi (Kololi, Bakau, Banjul)

**Cards:** Major hotels accept them. Most places = **cash only**

**Budget guide:**
- Local meal: 100-300 GMD ($2-5)
- Restaurant meal: 500-1500 GMD ($8-25)
- Beer: 75-150 GMD ($1-2.50)
- Taxi (short): 150-250 GMD ($2-4)""",

    "atm": """**ATMs in The Gambia:**

✅ **Where to find them:**
- Kololi/Senegambia area
- Bakau
- Banjul
- Serekunda

**Banks with ATMs:** Trust Bank, Standard Chartered, Ecobank, GT Bank

⚠️ **Important:**
- Visa/Mastercard work
- Daily limit usually 5,000-10,000 GMD (~$80-150)
- ATMs sometimes run out of cash!
- **Always carry backup cash**

**Tip:** Withdraw larger amounts less frequently to avoid multiple fees.""",

    "how much does it cost": """**Daily Budget in The Gambia:**

💰 **Budget Traveler:** $30-50/day
- Guesthouse: $15-25
- Local food: $5-10
- Transport: $5-10
- Activities: $5-10

💰 **Mid-Range:** $80-150/day
- 3-star hotel: $50-80
- Restaurant meals: $15-30
- Taxi/driver: $15-25
- Tours: $20-40

💰 **Luxury:** $200+/day
- 5-star resort: $120-200
- Fine dining: $40-60
- Private driver: $50+

**The Gambia is very affordable!** Your money goes far here.""",

    # ==================== TRANSPORT ====================
    "taxi": """**Taxis in The Gambia - Know Before You Go:**

🚕 **Green Tourist Taxis:**
- More comfortable, air-con
- Higher prices (negotiate!)
- Found at hotels, airport

🚕 **Yellow Taxis:**
- Local rates, can be shared
- Basic but cheap

**GOLDEN RULE: Agree price BEFORE getting in!**

**Typical prices:**
| Route | Cost |
|-------|------|
| Airport → Kololi | 1000-1500 GMD ($15-25) |
| Kololi → Banjul | 500-800 GMD ($8-12) |
| Short trip | 150-250 GMD ($2-4) |

**No Uber/Bolt** - doesn't exist here yet.""",

    "getting around": """**Getting Around The Gambia:**

🚕 **Taxis** (Best for tourists)
- Negotiate price first!
- Green = tourist, Yellow = local

🚐 **Gele-Gele** (Minibuses)
- Super cheap: 25-50 GMD
- Crowded but authentic experience
- Set routes, no schedule

🚗 **Hire a Driver** (Recommended!)
- $50-80/day including fuel
- Ask your hotel to arrange
- Best for day trips

⛴️ **Barra Ferry**
- Banjul ↔ Barra crossing
- ~50 GMD, scenic ride
- Can be crowded

**My tip:** Hire a driver for your whole stay. It's affordable and makes everything easier!""",

    "airport transfer": """**Airport to Hotel - Your Options:**

✈️ **Banjul International Airport (BJL)** is 24km from tourist areas.

**Option 1: Pre-arranged** (Best)
- Book through hotel ($20-30)
- Driver waiting with your name
- No hassle!

**Option 2: Airport Taxi**
- Fixed price booth inside airport
- Kololi/Senegambia: 1000-1500 GMD ($15-25)
- No negotiating needed

**Option 3: Walk outside & negotiate**
- Can get cheaper if you bargain
- But hassle after a long flight

**Time:** 40-60 minutes to Kololi depending on traffic

**Tip:** If arriving late, pre-book your transfer!""",

    # ==================== DISTANCES & TIMES ====================
    "how far": """**Distances from Kololi (Tourist Area):**

| Destination | Distance | Time | Taxi Cost |
|-------------|----------|------|-----------|
| Banjul | 15 km | 30-45 min | 500-800 GMD |
| Airport (BJL) | 24 km | 40-60 min | 1000-1500 GMD |
| Serekunda | 5 km | 10-15 min | 150-250 GMD |
| Bakau | 3 km | 5-10 min | 100-150 GMD |
| Tanji | 25 km | 45 min | 600-900 GMD |
| Sanyang | 35 km | 1 hour | 800-1200 GMD |
| Brikama | 30 km | 45-60 min | 700-1000 GMD |

**Upcountry:**
| Route | Distance | Time |
|-------|----------|------|
| Banjul → Basse | 400 km | 6-8 hours |
| Kololi → Janjanbureh | 300 km | 5-6 hours |""",

    "banjul to basse": """**Banjul to Basse - The Long Trip:**

📍 **Distance:** ~400 km
⏱️ **Time:** 6-8 hours by road

**Options:**

🚗 **Private car/driver:** 
- Most comfortable
- $80-120 for the trip
- Can stop at attractions

🚐 **Public transport (Gele-gele):**
- Very cheap (~500 GMD)
- Crowded, slow, multiple stops
- Adventure experience!

**Route:** Banjul → Soma → Farafenni → Janjanbureh → Basse

**What you'll see:** River views, rural villages, rice fields, wildlife

**Tip:** Stay overnight in Janjanbureh to break the journey and see Kunta Kinteh Island!""",

    "kololi to banjul": """**Kololi to Banjul:**

📍 **Distance:** 15 km
⏱️ **Time:** 30-45 minutes (depends on traffic)
💰 **Taxi:** 500-800 GMD ($8-12)

**Route:** Through Bakau and along the coast

**Traffic tip:** Serekunda junction can be slow. Mornings and evenings busiest.

**In Banjul:** Visit Arch 22, Albert Market, National Museum

**Return:** Same route or catch a shared taxi from Banjul ferry terminal area.""",

    "from senegal": """**Coming from Senegal to The Gambia:**

**From Dakar:**
- 5-6 hours total
- Cross at Karang border
- Or take Barra ferry from near border

**From Cap Skirring:**
- 3-4 hours
- Enter at southern border (Seleti/Kartong)
- Quick and scenic route

**From Ziguinchor:**
- 4-5 hours
- Trans-Gambia highway
- Cross at Farafenni

**Border crossing:**
- Passport required
- €20 Tourism Levy at entry
- Usually straightforward
- Some "helpers" may approach - you don't need them

**Tip:** Start early morning for same-day arrival with time to explore!""",

    # ==================== DAY TRIPS & ITINERARIES ====================
    "day trip": """**One Day in The Gambia - Make It Count!**

**🏖️ COASTAL DAY (Best for short visits):**
```
9:00 AM  → Kachikally Crocodile Pool (Bakau)
10:30 AM → Bijilo Monkey Park
12:30 PM → Lunch at Senegambia Strip
2:30 PM  → Albert Market, Banjul
4:30 PM  → Tanji Fishing Village (boats return!)
6:30 PM  → Sunset dinner at Sanyang Beach
```

**🏛️ HISTORY DAY (Roots experience):**
```
7:00 AM  → Depart for Jufureh
10:00 AM → Jufureh village & museum
11:30 AM → Boat to Kunta Kinteh Island
2:00 PM  → Return & lunch
5:00 PM  → Back to hotel
```

**💰 Budget:** Hire a driver for $50-80. Worth every dalasi!""",

    "one day": """**Only One Day? Here's What I'd Do:**

If you're coming from Senegal and just passing through:

**Morning (9 AM - 12 PM):**
- Start at Kachikally Crocodile Pool - touch a croc for luck!
- Quick walk at Bijilo Monkey Park

**Lunch (12 - 2 PM):**
- Senegambia Strip - pick any restaurant
- Try local fish or domoda (peanut stew)

**Afternoon (2 - 5 PM):**
- Banjul: Arch 22 views + Albert Market
- OR stay coastal: Beach time

**Evening (5 - 7 PM):**
- Tanji Fishing Village (boats come in around 5)
- Sunset at Sanyang Paradise Beach

**Total cost:** ~$60-80 including driver, food, entry fees

You'll get the best of The Gambia in a day!""",

    "3 days": """**3 Days in The Gambia - Perfect Intro!**

**DAY 1 - Coastal Vibes:**
- Morning: Bijilo Monkey Park
- Lunch: Beach bar at Kololi
- Afternoon: Kachikally Crocodiles + Bakau fish market
- Evening: Senegambia Strip nightlife

**DAY 2 - Culture & History:**
- Full day trip to Jufureh & Kunta Kinteh Island
- UNESCO World Heritage site
- Book through hotel ($45-65 per person)

**DAY 3 - Nature & Local Life:**
- Morning: Abuko Nature Reserve (monkeys, birds, crocs)
- Lunch: Local chop shop experience
- Afternoon: Brikama craft market (best wood carvings!)
- Evening: Tanji fishing village at sunset

**Budget:** ~$150-200 total (mid-range)""",

    "one week": """**7 Days in The Gambia - The Complete Experience:**

**Day 1:** Arrive, settle in, beach sunset
**Day 2:** Kololi/Kotu area - Bijilo monkeys, Kachikally crocs, nightlife
**Day 3:** Jufureh & Kunta Kinteh Island (full day)
**Day 4:** Abuko Nature Reserve + Brikama craft market
**Day 5:** River cruise OR Makasutu Culture Forest
**Day 6:** Beach day + Tanji fishing village sunset
**Day 7:** Shopping, relax, departure

**Add-ons if you have more time:**
- Upcountry trip to Janjanbureh (2 days)
- Bird watching at Kartong
- Day trip to Senegal

**Budget:** $400-700 mid-range for the week""",

    # ==================== BEACHES ====================
    "best beach": """**Best Beaches in The Gambia:**

🥇 **Sanyang Beach** - My Top Pick!
- Less touristy, beautiful
- Fresh grilled fish from fishermen
- Paradise Beach bar for sunset
- 45 min from Kololi

🥈 **Kololi Beach**
- Most popular, lively
- Beach bars, water sports
- Walking distance to hotels

🥉 **Kotu Beach**
- Calmer, good for swimming
- Family-friendly
- Great for birding nearby

**Also worth visiting:**
- **Cape Point** - Scenic, local vibe
- **Kartong** - Remote, eco-lodges
- **Tanji** - Not for swimming but amazing fishing scene

**Swimming safety:** Generally safe but watch for currents. No lifeguards.""",

    "kololi beach": """**Kololi Beach - The Tourist Hub:**

📍 **Location:** Heart of the tourist strip

**The vibe:**
- Most popular beach
- Beach bars and restaurants
- Sunbeds for rent
- Water sports available
- Vendors will approach you

**Good for:**
- Social atmosphere
- Nightlife nearby
- Walking distance to hotels
- Meeting other travelers

**Not so good:**
- Can be crowded
- Persistent vendors
- Not the prettiest beach

**Tip:** Walk south toward Cape Point for quieter stretches.""",

    "sanyang beach": """**Sanyang Beach - Local Secret! 🏆**

📍 **Location:** 35 km south of Kololi (~1 hour)

**Why I love it:**
- Beautiful, less touristy
- Watch fishing boats come in
- Fresh fish grilled on the spot!
- Paradise Beach bar = best sunset spot

**Facilities:**
- Rainbow Beach bar
- Paradise Beach bar
- Basic but charming

**Getting there:**
- Taxi: 800-1200 GMD from Kololi
- Or hire driver for half day

**Best time:** Arrive by 4 PM for fishing boats + sunset

**Tip:** Combine with Tanji fishing village (10 min away).""",

    # ==================== FOOD ====================
    "food": """**Gambian Food - What to Try:**

🍛 **Must-eat dishes:**

**Benachin** (Jollof Rice)
- THE national dish
- One-pot rice with fish/meat
- Find it everywhere

**Domoda**
- Groundnut (peanut) stew
- Rich, creamy, delicious
- Usually with rice

**Yassa**
- Chicken/fish with onions & lemon
- Tangy and flavorful

**Afra**
- Grilled meat street food
- Best late night snack!

**Where to eat:**
- Local "chop shops": $2-5 per meal
- Hotel restaurants: $15-30
- Beach bars: $8-15 for fish

**Vegetarian?** Try domoda without meat, or vegetable benachin.""",

    "where to eat": """**Where to Eat in The Gambia:**

**🍽️ Tourist Area (Kololi/Senegambia):**
- Many restaurants: African, European, Lebanese, Indian
- Prices: $8-30 per meal
- Try: Sea shells, Butcher's Shop, Solomon's

**🏠 Local Experience:**
- "Chop shops" - look for busy places with locals
- $2-5 for huge portions
- Authentic and delicious!

**🏖️ Beach Bars:**
- Fresh grilled fish
- Kololi Beach bars
- Sanyang Paradise Beach (worth the trip!)

**🌙 Night food:**
- Afra spots (grilled meat) appear after dark
- Best in Serekunda

**Tip:** Ask locals "Where do YOU eat?" - they'll point you right!""",

    "best restaurant": """**Top Restaurant Picks:**

**Senegambia Area:**
- **Butcher's Shop** - Great steaks, expat favorite
- **Solomon's Beach Bar** - Seafood, ocean views
- **Sea Shells** - Mixed menu, reliable

**For Local Food:**
- **Ali Baba's** - Lebanese/local mix
- **Mama's** - Authentic Gambian
- Any busy local chop shop!

**Special Occasion:**
- **Coco Ocean** - Fine dining, sunset views
- **Ngala Lodge** - Boutique restaurant

**Fresh Fish:**
- Sanyang Paradise Beach (worth the drive!)
- Tanji - straight from the boat

**Budget tip:** Lunch specials are often half the dinner price.""",

    # ==================== ATTRACTIONS ====================
    "kunta kinteh": """**Kunta Kinteh Island - A Must-Visit! 🏛️**

📍 **Location:** Up the Gambia River, near Jufureh

**What it is:**
- UNESCO World Heritage Site
- Historic slave trade fort (James Island)
- Where Alex Haley traced "Roots"
- Powerful, emotional experience

**The trip includes:**
- Boat ride up the river
- Jufureh village & museum
- Walking on the island ruins
- Local guide explains history

**Practical info:**
- Full day trip from Kololi
- Cost: $45-75 per person (tour)
- Book through hotel or tour operator
- Bring: sun protection, water, camera

**Best time:** Dry season. Tours leave early morning.

**Note:** Emotional experience - prepare yourself for the history.""",

    "things to do": """**Top Things to Do in The Gambia:**

**🏆 Must-Do:**
1. Kunta Kinteh Island (UNESCO site)
2. Kachikally Crocodile Pool (touch a croc!)
3. Bijilo Monkey Park
4. Tanji Fishing Village at sunset
5. River Gambia boat trip

**🦜 Nature:**
- Abuko Nature Reserve
- Makasutu Culture Forest
- Birdwatching (560+ species!)

**🛍️ Shopping:**
- Albert Market (Banjul)
- Brikama Craft Market (best carvings)

**🏖️ Beaches:**
- Kololi, Kotu, Sanyang, Kartong

**🌙 Nightlife:**
- Senegambia Strip bars
- Jokor Night Club

**Culture:**
- Wrestling matches (weekends)
- Kora music performances""",

    "abuko": """**Abuko Nature Reserve - Mini Safari! 🐒**

📍 **Location:** 30 min from Kololi

**What you'll see:**
- Monkeys (very close!)
- Crocodiles in pools
- 270+ bird species
- Monitor lizards
- Sometimes hyenas

**Practical:**
- Entry: ~150-200 GMD ($3)
- Open: 8 AM - 6 PM
- Duration: 1.5-2 hours
- Hire a guide at entrance (~200 GMD)

**What to bring:**
- Binoculars
- Camera
- Mosquito repellent
- Water

**Best time:** Early morning for birds, midday for basking crocs

**Tip:** Combine with Brikama craft market (nearby)!""",

    "crocodile pool": """**Kachikally Crocodile Pool - Touch a Croc! 🐊**

📍 **Location:** Bakau (10 min from Kololi)

**What it is:**
- Sacred pool with 80+ crocs
- Local fertility shrine
- You can TOUCH them!
- Very docile Nile crocodiles

**The experience:**
- Local guide tells history
- Walk among crocodiles
- Photo with a croc (they're calm!)
- Learn about local beliefs

**Practical:**
- Entry: ~100-150 GMD ($2)
- Open: Daily 8 AM - 6 PM
- Duration: 30-45 minutes

**Is it safe?** Yes! These crocs are well-fed and used to people. Guides know which ones to approach.

**Tip:** Morning is best - crocs more active, fewer tourists.""",

    # ==================== ACCOMMODATION ====================
    "where to stay": """**Where to Stay - Area Guide:**

**🌟 Kololi/Senegambia (Most Popular)**
- Pros: Restaurants, nightlife, beach
- Cons: Can be busy, vendors
- Best for: First-timers, social travelers

**🌊 Kotu**
- Pros: Quieter, good beach, birding
- Cons: Less nightlife
- Best for: Families, relaxation

**🏡 Cape Point/Bakau**
- Pros: Local vibe, near attractions
- Cons: Fewer restaurants
- Best for: Cultural experience

**🌴 Bijilo/Kerr Serign**
- Pros: Upscale, near nature reserve
- Cons: Pricier
- Best for: Luxury seekers

**My advice:** Stay in Kololi for first visit - everything's walkable!""",

    "budget hotel": """**Budget Accommodation ($20-50/night):**

**Guesthouses:**
- Luigi's (Kololi) - $25-35, popular with backpackers
- Lemon Creek B&B (Bijilo) - $30-45
- African Village Hotel - $20-35

**What you get:**
- Clean room with AC or fan
- Usually breakfast included
- Friendly owners
- Good local tips!

**Tips:**
- Book on WhatsApp/email for best rates
- Low season (Jun-Oct) = 30-50% off
- Ask to see room first

**Also consider:**
- Airbnb options exist
- Shared apartments cheaper for groups""",

    "best hotel": """**Top Hotels by Category:**

**🏆 Luxury (5-star):**
- **Coco Ocean Resort** (Bijilo) - $150-250
  Best pool, spa, beach
- **Mandina Lodges** (Makasutu) - $180-300
  Eco-luxury in the forest

**⭐ Mid-Range (4-star):**
- **Senegambia Beach Hotel** - $80-140
  Classic, great pool
- **Ngala Lodge** (Fajara) - $90-150
  Boutique, beautiful gardens
- **Ocean Bay Hotel** (Cape Point) - $80-130

**💰 Good Value (3-star):**
- **Sunset Beach Hotel** (Kotu) - $60-100
- **Kombo Beach Hotel** (Kotu) - $50-90
- **Bakotu Hotel** (Kotu) - $45-80

**Book on:** Booking.com or contact hotels directly (often cheaper)""",

    # ==================== HEALTH ====================
    "malaria": """**Malaria in The Gambia - Take It Seriously!**

⚠️ **Yes, malaria exists here.** Take precautions:

**Prevention:**
1. **Take antimalarials** (ask your doctor):
   - Malarone (most popular)
   - Doxycycline (cheaper)
   - Start before arrival!

2. **Avoid bites:**
   - DEET repellent (30%+)
   - Long sleeves at dusk
   - Sleep under mosquito net
   - Air-con rooms help

**Symptoms:** Fever, chills, headache, body aches (can appear up to 4 weeks after)

**If you feel sick:** Get tested immediately. Malaria is treatable if caught early!

**Honest truth:** Many tourists take precautions and are fine. Don't skip the antimalarials.""",

    "vaccines": """**Vaccinations for The Gambia:**

**Required:**
- **Yellow Fever** - Only if coming from endemic country (certificate checked)

**Recommended:**
- Hepatitis A & B ✓
- Typhoid ✓
- Tetanus-Diphtheria ✓
- Meningitis (dry season) ✓

**Consult your doctor** 6-8 weeks before travel.

**Malaria:** Not a vaccine but take prophylaxis (Malarone or Doxycycline)

**Other health tips:**
- Drink bottled water only
- Use sunscreen (sun is strong!)
- Bring basic meds from home
- Travel insurance recommended

**Medical care:** MRC Medical Centre (Fajara) is reliable. Pharmacies available.""",

    # ==================== CULTURE ====================
    "culture": """**Gambian Culture - Quick Guide:**

**🤝 Greetings are EVERYTHING!**
- Always say hello first
- Take time for greetings (How are you? How's the family?)
- Rush = rude

**🗣️ Useful phrases:**
- "Salaamaleekum" - Hello (universal)
- "Abaraka" - Thank you (Mandinka)
- "Jërëjëf" - Thank you (Wolof)

**👔 Dress code:**
- Tourist areas: Casual fine
- Villages/markets: Cover shoulders & knees
- Beach only: Swimwear OK

**🕌 Religion:**
- 95% Muslim (very relaxed)
- Respect prayer times
- Ramadan: Eating in public is fine for tourists

**🍽️ Food etiquette:**
- Right hand for eating/giving
- Accept tea if offered (Attaya ceremony)
- Refusing food can seem rude

**📷 Photos:** Always ASK before photographing people.""",

    "mandinka greeting": """**Mandinka Greetings & Phrases:**

**Basics:**
| English | Mandinka | Say it |
|---------|----------|--------|
| Hello | Salaamaleekum | sa-lam-a-LAY-kum |
| Response | Maalekum salaam | ma-LAY-kum sa-lam |
| How are you? | Here be di? | HAY-ray bay DEE |
| I'm fine | Here dorong | HAY-ray DOH-rong |
| Thank you | Abaraka | ah-ba-RA-ka |
| Goodbye | Fo waati kutoo | foh WAH-tee koo-TOH |

**Handy words:**
- Yes = Haa
- No = Hani
- How much? = Jelu?
- Water = Ji
- Food = Domoroo
- Good = Beteyata

**People LOVE when you try!** Even just "Abaraka" gets big smiles.""",

    # ==================== PRACTICAL QUESTIONS ====================
    "sim card": """**Getting a SIM Card in The Gambia:**

📱 **Options:**
- **Africell** - Most popular, good coverage
- **QCell** - Also good
- **Comium** - Less common

**Where to buy:**
- Airport (convenient!)
- Phone shops everywhere
- Small kiosks

**Cost:**
- SIM: 100-200 GMD ($2-3)
- Data: 500 GMD (~$8) for 5-10GB

**What you need:**
- Passport (for registration)
- 5 minutes

**Coverage:** Good in tourist areas and towns. Patchy upcountry.

**Tip:** Africell works well. Top up with scratch cards from any small shop.""",

    "wifi": """**Internet & WiFi in The Gambia:**

📶 **Hotel WiFi:**
- Most hotels have it
- Speed varies (don't expect fast)
- Often lobby/restaurant only

📱 **Best option: Local SIM with data**
- Africell or QCell
- 5-10GB for ~$8
- 4G in tourist areas

💻 **If you need to work:**
- Coco Ocean has decent WiFi
- Some cafes in Kololi
- Don't rely on it for video calls

**Reality check:** Internet is slower than you're used to. Perfect excuse to disconnect! 🌴""",

    "what to pack": """**Packing List for The Gambia:**

**👕 Clothes:**
- Light, breathable fabrics
- Modest clothes for villages (cover shoulders/knees)
- Swimwear
- Light sweater (evenings can be cool Nov-Feb)
- Comfortable walking shoes

**🧴 Essentials:**
- Sunscreen SPF 30+
- Mosquito repellent (DEET)
- Sunglasses & hat
- Basic first aid kit

**💊 Health:**
- Antimalarials
- Diarrhea medicine
- Hand sanitizer
- Any personal medications

**📱 Tech:**
- UK-style power adapter (Type G)
- Portable charger
- Camera

**💡 Don't forget:**
- €40 cash for Tourism Levy!
- Copies of passport
- Travel insurance docs""",

    "electricity": """**Electricity in The Gambia:**

⚡ **Voltage:** 230V (same as UK/Europe)
🔌 **Plug type:** UK 3-pin (Type G)

**What to bring:**
- UK adapter if you have EU/US plugs
- Universal adapter works

**Power cuts:** Happen occasionally. Most hotels have generators.

**Tip:** Bring a portable charger for your phone - useful for day trips!""",

    "tipping": """**Tipping in The Gambia:**

**General guide:**
- Not mandatory but appreciated
- Service isn't usually included

**Suggested tips:**
| Who | How Much |
|-----|----------|
| Restaurant | 10% if good service |
| Hotel porter | 50-100 GMD ($1) |
| Tour guide | 200-500 GMD ($3-8) |
| Driver (day) | 200-400 GMD ($3-6) |
| Spa/massage | 10-15% |

**Note:** In local chop shops, no tip expected.

**Bumsters/unofficial guides:** You don't owe them anything if you didn't ask for help.""",

    # ==================== QUICK ANSWERS ====================
    "hello": """**Hello! 👋 Welcome to The Gambia Travel Assistant!**

I'm here to help you plan your trip to The Smiling Coast of Africa.

**Popular questions:**
- "Do I need a visa?"
- "Is it safe?"
- "Best time to visit?"
- "What should I see?"
- "How do I get around?"

Just ask me anything about The Gambia!""",

    "thanks": """**You're welcome! 🙏**

Anything else you'd like to know about The Gambia?

Safe travels to the Smiling Coast! 🇬🇲""",

    "emergency": """**Emergency Numbers in The Gambia:**

🚔 **Police:** 117
🚑 **Ambulance:** 116
🚒 **Fire:** 118

**Tourist Police:** Located in Kololi/Senegambia area - very helpful!

**Embassies in Banjul:**
- UK: +220 449 5133
- US: +220 439 2856

**Medical:**
- MRC Medical Centre (Fajara): Best facility
- EFSTH Hospital (Banjul)

**Lost passport?** Contact your embassy immediately.

**Stay calm - Gambians are very helpful in emergencies!**""",
}

# =============================================================================
# KEYWORD MATCHING SYSTEM
# =============================================================================

# Maps various ways of asking to the correct answer key
KEYWORD_MAP = {
    # Visa
    "visa": "visa",
    "need visa": "do i need a visa",
    "do i need visa": "do i need a visa",
    "entry requirements": "visa",
    "passport": "visa",
    "ecowas": "ecowas visa",
    "nigerian visa": "ecowas visa",
    "uk visa": "uk visa",
    "british visa": "uk visa",
    "american visa": "us visa",
    "us visa": "us visa",
    "usa visa": "us visa",
    "tourism levy": "tourism levy",
    "tdl": "tourism levy",
    "entry fee": "tourism levy",
    
    # Safety
    "safe": "is gambia safe",
    "safety": "is gambia safe",
    "is it safe": "is gambia safe",
    "dangerous": "is gambia safe",
    "crime": "is gambia safe",
    "solo female": "safe for women",
    "solo woman": "safe for women",
    "women travel": "safe for women",
    "female travel": "safe for women",
    "bumster": "bumsters",
    "beach boy": "bumsters",
    
    # Weather
    "weather": "weather",
    "best time": "best time to visit",
    "when to visit": "best time to visit",
    "when to go": "best time to visit",
    "climate": "weather",
    "rainy season": "rainy season",
    "dry season": "best time to visit",
    
    # Money
    "money": "money",
    "currency": "money",
    "dalasi": "money",
    "exchange": "money",
    "atm": "atm",
    "cash": "money",
    "how much cost": "how much does it cost",
    "budget": "how much does it cost",
    "expensive": "how much does it cost",
    
    # Transport
    "taxi": "taxi",
    "transport": "getting around",
    "getting around": "getting around",
    "uber": "taxi",
    "airport transfer": "airport transfer",
    "airport taxi": "airport transfer",
    
    # Distances
    "how far": "how far",
    "distance": "how far",
    "how long": "how far",
    "banjul to basse": "banjul to basse",
    "basse": "banjul to basse",
    "kololi to banjul": "kololi to banjul",
    "from senegal": "from senegal",
    "cap skirring": "from senegal",
    "dakar": "from senegal",
    
    # Day trips
    "day trip": "day trip",
    "one day": "one day",
    "1 day": "one day",
    "passing through": "one day",
    "3 day": "3 days",
    "three day": "3 days",
    "week": "one week",
    "7 day": "one week",
    "itinerary": "3 days",
    
    # Beaches
    "beach": "best beach",
    "beaches": "best beach",
    "best beach": "best beach",
    "kololi beach": "kololi beach",
    "sanyang": "sanyang beach",
    "swimming": "best beach",
    
    # Food
    "food": "food",
    "eat": "where to eat",
    "restaurant": "where to eat",
    "where to eat": "where to eat",
    "best restaurant": "best restaurant",
    
    # Attractions
    "kunta kinteh": "kunta kinteh",
    "james island": "kunta kinteh",
    "roots": "kunta kinteh",
    "jufureh": "kunta kinteh",
    "things to do": "things to do",
    "what to do": "things to do",
    "attractions": "things to do",
    "abuko": "abuko",
    "nature reserve": "abuko",
    "crocodile": "crocodile pool",
    "kachikally": "crocodile pool",
    
    # Accommodation
    "hotel": "best hotel",
    "where to stay": "where to stay",
    "accommodation": "where to stay",
    "budget hotel": "budget hotel",
    "cheap hotel": "budget hotel",
    "best hotel": "best hotel",
    "luxury hotel": "best hotel",
    
    # Health
    "malaria": "malaria",
    "vaccine": "vaccines",
    "vaccination": "vaccines",
    "health": "vaccines",
    "yellow fever": "vaccines",
    
    # Culture
    "culture": "culture",
    "greeting": "mandinka greeting",
    "mandinka": "mandinka greeting",
    "phrases": "mandinka greeting",
    "hello in": "mandinka greeting",
    
    # Practical
    "sim card": "sim card",
    "phone": "sim card",
    "wifi": "wifi",
    "internet": "wifi",
    "pack": "what to pack",
    "packing": "what to pack",
    "bring": "what to pack",
    "electricity": "electricity",
    "plug": "electricity",
    "adapter": "electricity",
    "tip": "tipping",
    "tipping": "tipping",
    
    # Misc
    "hello": "hello",
    "hi": "hello",
    "thanks": "thanks",
    "thank you": "thanks",
    "emergency": "emergency",
    "police": "emergency",
    "help": "emergency",
}


def get_smart_answer(query: str) -> dict:
    """
    Find the best conversational answer for a query.
    Returns dict with answer, confidence, and suggestions.
    """
    query_lower = query.lower().strip()
    
    # Remove common question words
    query_clean = query_lower
    for word in ["what", "where", "when", "how", "why", "is", "are", "do", "does", "can", "the", "a", "an", "i", "my", "in", "to", "for", "about"]:
        query_clean = query_clean.replace(word + " ", " ")
    query_clean = " ".join(query_clean.split())  # Clean up spaces
    
    # 1. Try exact match in KEYWORD_MAP
    for keyword, answer_key in KEYWORD_MAP.items():
        if keyword in query_lower:
            if answer_key in QUICK_ANSWERS:
                return {
                    "answer": QUICK_ANSWERS[answer_key],
                    "confidence": 0.95,
                    "matched": answer_key,
                }
    
    # 2. Try direct key match
    for key in QUICK_ANSWERS.keys():
        if key in query_lower or query_lower in key:
            return {
                "answer": QUICK_ANSWERS[key],
                "confidence": 0.9,
                "matched": key,
            }
    
    # 3. Fuzzy word matching
    query_words = set(query_clean.split())
    best_match = None
    best_score = 0
    
    for key, answer in QUICK_ANSWERS.items():
        key_words = set(key.replace("_", " ").split())
        overlap = len(query_words & key_words)
        if overlap > best_score:
            best_score = overlap
            best_match = key
    
    if best_match and best_score > 0:
        return {
            "answer": QUICK_ANSWERS[best_match],
            "confidence": min(0.5 + (best_score * 0.2), 0.85),
            "matched": best_match,
        }
    
    # 4. No match - return None
    return {
        "answer": None,
        "confidence": 0,
        "matched": None,
    }


def get_suggestions(query: str) -> list:
    """Get related topic suggestions for unclear queries."""
    suggestions = []
    query_lower = query.lower()
    
    topic_suggestions = {
        "travel": ["visa", "best time to visit", "how much does it cost"],
        "visit": ["things to do", "best time to visit", "where to stay"],
        "gambia": ["is gambia safe", "best time to visit", "things to do"],
        "trip": ["day trip", "3 days", "one week"],
        "stay": ["where to stay", "best hotel", "budget hotel"],
        "go": ["things to do", "getting around", "day trip"],
        "see": ["things to do", "kunta kinteh", "best beach"],
    }
    
    for word, suggs in topic_suggestions.items():
        if word in query_lower:
            suggestions.extend(suggs)
    
    return list(set(suggestions))[:3]


# Test
if __name__ == "__main__":
    test_queries = [
        "do i need a visa",
        "is gambia safe for women",
        "best time to visit",
        "how far is basse",
        "i have one day",
        "where should i eat",
        "taxi prices",
    ]
    
    for q in test_queries:
        result = get_smart_answer(q)
        print(f"\n📝 '{q}'")
        print(f"   Matched: {result['matched']} (confidence: {result['confidence']:.0%})")
        if result['answer']:
            print(f"   Answer: {result['answer'][:80]}...")
