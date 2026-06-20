from pathlib import Path

NAV = '''<nav>
  <a class="nav-logo" href="/">Josh Gray-Emmer</a>
  <ul class="nav-links">
    <li><a href="/#about">About</a></li>
    <li><a href="/#dinner-club">Dinner Club</a></li>
    <li><a href="/#maps">Maps</a></li>
    <li><a href="/adventures/" class="active">Adventures</a></li>
    <li><a href="/#work">Work</a></li>
    <li><a href="/#contact" class="nav-cta">Say Hello</a></li>
  </ul>
</nav>'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'

def post(filename, title, date, category, breadcrumb_label, content, prev_url=None, prev_label=None, next_url=None, next_label=None):
    nav_html = ''
    if prev_url or next_url:
        nav_html = '<div class="post-nav">'
        if prev_url:
            nav_html += f'<a href="{prev_url}">← {prev_label}</a>'
        else:
            nav_html += '<span></span>'
        if next_url:
            nav_html += f'<a class="older" href="{next_url}">{next_label} →</a>'
        nav_html += '</div>'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{title}, a travel story by Josh Gray-Emmer.">
<link rel="canonical" href="https://www.joshgray-emmer.com/adventures/posts/{filename.removesuffix('.html')}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title} — Josh Gray-Emmer">
<meta property="og:description" content="{title}, a travel story by Josh Gray-Emmer.">
<title>{title} — Josh Gray-Emmer</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="../style.css">
</head>
<body>
{NAV}
<div class="breadcrumb">
  <a href="/adventures/">Adventures</a><span>›</span>{breadcrumb_label}
</div>
<div class="post-hero">
  <span class="post-category">{category}</span>
  <h1 class="post-title">{title}</h1>
  <div class="post-meta"><span>{date}</span><span class="post-meta-sep">·</span><span>Josh Gray-Emmer</span></div>
</div>
<div class="post-body">
{content}
</div>
{nav_html}
<footer><p>© Josh Gray-Emmer · <a href="/">joshgray-emmer.com</a></p></footer>
</body>
</html>'''

posts = [
  {
    "file": "why-bali.html",
    "title": "Why Bali???",
    "date": "November 12, 2015",
    "category": "Bali · The Decision",
    "breadcrumb": "Bali",
    "next_url": "why-bali-part-2.html",
    "next_label": "Why Bali, Part 2",
    "content": """<p>This whole adventure started a little over a month ago, with of all people, my VERY pragmatic and sensible father. He pointed out to me, that I was living beyond my means, in a stunning Downtown Los Angeles loft, that I owned, but was losing money on. Let me explain. I bought this loft at the bottom of the Los Angeles real estate market, and it has appreciated significantly in value in the last 5 years. The market had priced me out of my own home. I was losing the opportunity to gain $6,500 a month — a cost I WOULD NOT pay to live in my own loft.</p>
<p>In addition, I have two loans on my property. One for $377,000 at a low interest rate over 30 years, and one for $150,000 at a higher interest rate over the same period. The increase in property value had presented an opportunity to pay off the higher interest loan in a much quicker period, saving over $120,000 in interest. It was becoming more and more clear — it was time to move out.</p>
<hr>
<h2>Again, why Bali?</h2>
<p>I'm getting there. At first thought, I wanted to stay somewhere in the US. I checked out Portland, and realized right away that this wasn't going to work. To maximize my investment, I needed to be saving money, and not just a little money, but AS MUCH MONEY AS POSSIBLE. Next I checked out Hong Kong. I LOVE LOVE LOVE Hong Kong. It's my favorite city in the world besides Los Angeles. I thought that maybe, if I lived off the main island, saving money would be possible. Again, I was mistaken.</p>
<p>Google to the rescue. After a few searches for the cheapest places in the world to live, it became clear that my real options were Latin America or Asia. I chose the latter, though it's clear if you speak Spanish, the former is a better option for a true saver. Now I started to read. A LOT. Vietnam, Bali, Cambodia, and Thailand made the final cut. I decided on Bali. I use only the island Bali as my destination, even though it's part of Indonesia, because it's a Hindu culture, where as the rest of the country is Muslim — as a gay man, that's not an option for me.</p>
<p>So what was it in the reading that made Bali stand out as THE cheapest place I could live with the highest quality of life? Check out Why Bali Part 2!</p>"""
  },
  {
    "file": "why-bali-part-2.html",
    "title": "Why Bali, Part 2",
    "date": "November 12, 2015",
    "category": "Bali · The Decision",
    "breadcrumb": "Bali",
    "prev_url": "why-bali.html",
    "prev_label": "Why Bali???",
    "next_url": "arent-you-going-to-be-lonely.html",
    "next_label": "Aren't You Going To Be Lonely?",
    "content": """<p>Let's be honest, I'd heard Bali was awesome. It's not listed in the top 10 places to live, so I had to add it to the list and then compare it to the others. It turns out, five years ago, it would make every list. However, people read those lists, and the cost of living went up. Not too much, but enough for it to no longer be the very cheapest. I had something going for me though that wasn't mentioned — new relaxed visa requirements that took effect in September, and a VERY VERY strong dollar against the IDR. When this was factored in, it put Bali square in the middle of the pack for savings. Now it was time to look at quality of life.</p>
<p>I am going to be traveling alone, but I make friends quickly, so if I don't speak the language, a strong expat community is a MUST. Bali is only three hours from Australia and has an expat community going back 20 years. Cambodia and Vietnam really lack this infrastructure. That left Thailand and Bali. My friend Max, who lives in Bangkok discouraged me from making that decision, and Bali was left. It also has a relatively large gay community and a few gay clubs and watering holes.</p>
<p>Now there was one last thing to do to seal the deal. Facebook Graph Search. "Friends of My Friends who Live in Bali, Indonesia" was a winner. From there I started hitting up all my friends for introductions. It was time to get the real scoop from people on the ground. How much did things REALLY cost, right now — what was life like, what should I watch out for?</p>"""
  },
  {
    "file": "arent-you-going-to-be-lonely.html",
    "title": "Aren't You Going To Be Lonely?",
    "date": "November 12, 2015",
    "category": "Bali · The Decision",
    "breadcrumb": "Bali",
    "prev_url": "why-bali-part-2.html",
    "prev_label": "Why Bali, Part 2",
    "next_url": "if-this-is-so-easy.html",
    "next_label": "If This Is So Easy...",
    "content": """<p>The short answer is yes. The long answer is, who the hell knows? There is NO DOUBT that there will be times where I miss my friends and family and even my kitties. Such is the sacrifice demanded of a true adventure. I'm also a very accomplished solo traveler so I have some data to back up my assumptions. However, I have never lived outside the city I grew up in, so this could be total nonsense on my part.</p>
<p>Thank goodness for coincidences and luck. The second person I told was my long time friend Scotty. He and his wife had just decided to spend the month of February in Bali, completely on their own. This made my decision to leave even easier. Together we found an AirBnB for $800 total for the month, giving me plenty of time to get acclimated to Bali life, while with friends. It also meant I would have plenty of time to find a yearly rental (which are paid up front in Bali).</p>
<p>My research had left me convinced that I would be able to find a really spectacular place for 10K a year, a great place for 5K a year, and a small apartment for 2.5K a year. These prices would only be available to me on the ground, as any prices listed online were done through middle-men who make a living jacking them up to snatch unsuspecting tourists.</p>
<p>Then came another piece of luck. A friend of mine who works in finance and travels to Bali several times a year offered to go in with me on a place so he could send business associates to "his home in Bali" and I would act as their concierge. This allowed me to justify spending 5K for the year, with him throwing in the other 5K, to secure an amazing place. This brings me back to being lonely.</p>
<p>If all goes as planned (and there's no reason to believe that it won't — except the fact that something always does), I will have a beautiful 2-3 bedroom home with a pool near the beach for all of my friends to come and visit. I think I can realistically expect at least five visits from friends a year, plus business associates, and that will certainly help keep the loneliness at bay. Again, as with all things about this trip, I'll let you know in a couple months if I was right. Stay tuned.</p>"""
  },
  {
    "file": "if-this-is-so-easy.html",
    "title": "If This Is So Easy, Why Isn't Everyone Doing It?",
    "date": "November 20, 2015",
    "category": "Bali · The Decision",
    "breadcrumb": "Bali",
    "prev_url": "arent-you-going-to-be-lonely.html",
    "prev_label": "Aren't You Going To Be Lonely?",
    "next_url": "how-to-make-money.html",
    "next_label": "How Are You Going To Make Money?",
    "content": """<p>That's a really really good question, and one that certainly keeps me up at night. Everything I've read so far makes it seem like this is going to be a relatively painless thing to accomplish. Sure there will be some hiccups, but in the grand scheme of things, not very hard. What am I missing? What huge thing have I overlooked?</p>
<p>Maybe nothing. The possibility I'm hoping is true, is that I'm not like other people. I have very strong, life-long friendships… but I'm not worried about losing those by living abroad for a couple years. Technology makes it easy to stay in touch. Bali has decent internet, so FaceTime, Google Talk and WhatsApp should work just fine.</p>
<p>What I DON'T have is a relationship or desire to have children. According to a new Gallup Poll, only 5% of Americans are not married and don't intend to get married. In addition to that, only 14% of Americans don't want to have children. That puts me in a very small group of people who, without moral/legal/romantic attachments to others, can choose to pursue life on their own terms. My barriers to pulling the trigger are mine alone, and don't affect those I love.</p>
<p>Quite frankly, it also frees up a LOT of money for my potential future. I will not be paying for a wedding, honeymoon, braces, cars, trips, and college tuitions. If everyone in my situation chose to ditch their lives and move abroad, it would still be a tiny fraction of the public, and of course, most people desire a traditional lifestyle.</p>
<p>So why isn't everyone doing this? Because as nice and as awesome as it sounds, it doesn't fit with the life they currently live, or want to live in the future. However, it does fit well with my life and my future desires, so I'm going for it!</p>"""
  },
  {
    "file": "how-to-make-money.html",
    "title": "How Are You Going To Make Money While Living In Bali?",
    "date": "December 13, 2015",
    "category": "Bali · Logistics",
    "breadcrumb": "Bali",
    "prev_url": "if-this-is-so-easy.html",
    "prev_label": "If This Is So Easy...",
    "next_url": "30-days-away.html",
    "next_label": "30 Days Away...",
    "content": """<p>Working a job on the ground in Bali is absolutely OUT. The Indonesian government will deport your ass for getting paid $50 to sing in a club. In general, NO foreigner is allowed to work any job that an Indonesian could do. This is OK with me however, because I'll still be able to do what I do now — technical and strategic consulting. I guess the name for it is "digital nomad" — someone who can work from anywhere. Most expats who live there seem to be digital nomads, employed elsewhere, married to locals, or retired.</p>
<h2>Who Knew Facebook Was Your "Eyes on The Ground" Before Moving Across The World?</h2>
<p>I don't know if this is true for everywhere, but I DO know it's true for Bali. After using Graph Search to find my friends of friends who live in Bali, I ended up searching for group names with the neighborhoods I was interested in, as well as groups located in Bali in general. There is SUCH a wealth of well-maintained and frequently updated pockets of local knowledge, and EVERYONE is friendly.</p>
<h2>Just Bought My One Way, Non-Refundable Airline Ticket — Shit Just Got Real</h2>
<p>There's something about making it official. Robert Cialdini the author of "Influence" would say that this is when "Commitment and Consistency" kick in. At first it's a shock. This is real, I made a decision and I'm gonna have to live with it!!! Then the wonderful neuro-chemicals kick in. Waves of endorphins and dopamine over a few days cement the idea in your head as not rash, but GREAT and well thought out too!</p>
<p>It also makes getting things done easier. I immediately made arrangements to store my mom's art supplies, bought a new couch to replace the old one, and began making repairs on my loft to get it ready for showings. This is real. This is really happening. Countdown: 48 days.</p>"""
  },
  {
    "file": "30-days-away.html",
    "title": "30 Days Away... And Things Are Not Going As Planned...",
    "date": "December 28, 2015",
    "category": "Bali · Pre-Departure",
    "breadcrumb": "Bali",
    "prev_url": "how-to-make-money.html",
    "prev_label": "How Are You Going To Make Money?",
    "next_url": "loft-is-leased.html",
    "next_label": "The Loft is Leased!",
    "content": """<p>It was bound to happen. When you're moving half way across the world, shit will come up. In my case, the two biggest things I need to make this work are not yet accomplished. My home is NOT rented, and my HELOC is not finished.</p>
<p>The HELOC is more a product of slow banks and the holidays, hopefully. The rental of my loft is altogether more scary to me. I really need to get a good rate for my loft to be able to justify this move.</p>
<p>Right now my loft is on the market for $5,995. I'm hoping I can get it. But I'll settle for $5,500 if someone pays me up front, or something similar. Hell, if I don't get any real offers until January 20th, who knows what I might settle for!</p>
<h3>Other things I'm still trying to figure out</h3>
<p>Where the hell are my two awesome cats gonna go? Should I keep my phone, or transfer to a Google Phone Number? Exactly which visa will I qualify for? Am I leaving my stuff in the loft or selling everything to my friends?</p>
<p>Stay tuned for more... wish me luck!</p>"""
  },
  {
    "file": "loft-is-leased.html",
    "title": "The Loft is Leased, and I Leave in 13 Days!!!",
    "date": "January 15, 2016",
    "category": "Bali · Pre-Departure",
    "breadcrumb": "Bali",
    "prev_url": "30-days-away.html",
    "prev_label": "30 Days Away...",
    "next_url": "move-out-4-days.html",
    "next_label": "I Move Out in 4 Days!",
    "content": """<p>Just in the nick of time, my lovely broker Tiffany of SmartLA Realty has found someone to lease my loft. The final price, for those of you who were betting — <strong>$5,250 a month for 16 months</strong>. Not as high as I would have liked, but still fits my budget nicely. At the end of the day, my adventure is a go, and I'm a happy camper!</p>
<p>Now it's time to get my ass in gear and get the heck out of dodge! EVERYTHING MUST GO! I've decided not to get a storage unit, and that means I've got to sell everything I've accumulated over the last 5 years in the next week. Whew!</p>
<p>In addition, I've learned that I need to get a visa from the Indonesian consulate in advance. Unlike Scott and Jessie, who can get 30-day visas on arrival, I'll need an official visa to be able to extend my trip later. Passport photos today, paperwork on Tuesday, and I should get it just before I depart the following Thursday. No prob.</p>"""
  },
  {
    "file": "move-out-4-days.html",
    "title": "Holy Crap! I Move Out in 4 Days and Leave The Country in 6!!",
    "date": "January 23, 2016",
    "category": "Bali · Pre-Departure",
    "breadcrumb": "Bali",
    "prev_url": "loft-is-leased.html",
    "prev_label": "The Loft is Leased!",
    "next_url": "holy-cow.html",
    "next_label": "Holy Cow! Literally!",
    "content": """<p>I won't lie, this has been a really hard process. I almost lost it when I started moving all my stuff out of closets and into the living room to be sold. It seemed to be never ending. All the things I've accumulated and inherited over the years as I moved from one place to another. This time however, I'm taking a single carry on, and a backpack. EVERYTHING must go has become my mantra.</p>
<p>There's this panic in my stomach that keeps coming back. What have I forgotten to do, that I won't be able to fix once I'm there? Will I be able to get everything on my list done before I leave? Will anyone buy my stuff, or even want it for free, or am I gonna end up throwing everything away?</p>
<p>That panic also is starting to come with waves of relief. The end is near. Soon, no matter what I forgot, sold, or threw away, I will own what's in my bag, somewhere on an island, a few blocks from the beach. I can't even picture what my average day will be like. It's just not the same feeling as going on vacation. There's an anticipation and excitement muddled together with fear and self-doubt that's completely new to me, and I suppose, that's one of the reasons I'm doing this.</p>
<blockquote>I imagine I'll be pleased that I felt this way, after I'm done feeling this way.</blockquote>"""
  },
]

for p in posts:
    html = post(
        filename=p["file"],
        title=p["title"],
        date=p["date"],
        category=p["category"],
        breadcrumb_label=p["breadcrumb"],
        content=p["content"],
        prev_url=p.get("prev_url"),
        prev_label=p.get("prev_label"),
        next_url=p.get("next_url"),
        next_label=p.get("next_label"),
    )
    path = Path(__file__).resolve().parent / "posts" / p["file"]
    with path.open('w', encoding='utf-8') as f:
        f.write(html)
    print(f'✓ {p["file"]}')

print(f'\nDone: {len(posts)} posts built')

# Additional posts
extra_posts = [
  {
    "file": "holy-cow.html",
    "title": "Holy Cow!! Literally, Holy Cow!!",
    "date": "January 31, 2016",
    "category": "Bali · Arrival",
    "breadcrumb": "Bali",
    "prev_url": "move-out-4-days.html",
    "prev_label": "I Move Out in 4 Days!",
    "next_url": "making-friends.html",
    "next_label": "Making Friends is Stupid Easy",
    "content": """<p>WOW. That was one HELL of a trip from LA to Bali. By far the longest series of flights I've ever taken. 14.5 hours to Taipei then a 3 hour layover and 6 more hours to Bali. The Taipei airport puts the Beverly Center to SHAME — I was floored by how many name brands had stores, and sharply dressed Taiwanese ready to tell you all about when Johnny Walker Blue will change your life.</p>
<p>The Bali airport was exactly the opposite. Covered in glass and vines, you know you've arrived in paradise from the moment you step off the Hello Kitty branded plane. My driver was waiting and I was through customs and immigration in 10 minutes.</p>
<p>HOLY COW!!! Literally — it's a Hindu island in a Muslim country, so cows walking down the street is something I've already seen. There are NO rules of the road here, cars push their way between throngs of mopeds as everyone tries to make their way down streets that are only sometimes paved and always too small for even the average car.</p>
<p>SCORE!!! As Scotty has been saying over and over — WE WON BIG with the location of our villa. Not only is the place spacious, comfortable, and clean, it's right in the center of Canggu. Five minutes walk and I'm on the beach. Five more minutes and I'm at the Dojo (expat internet co-working space).</p>
<p>It hasn't hit me that I live here yet. I wonder how long that will take. But I've already made my first friend Cory, a reporter from the east coast who lives in Jakarta and hangs in Bali. He assured me that I picked the best place on the island to live. Well that's all I got for day one. More to come!!!</p>"""
  },
  {
    "file": "making-friends.html",
    "title": "Making Friends in Bali is Stupid Easy",
    "date": "February 3, 2016",
    "category": "Bali · Life There",
    "breadcrumb": "Bali",
    "prev_url": "holy-cow.html",
    "prev_label": "Holy Cow!!",
    "next_url": "monkeys-temples.html",
    "next_label": "Monkeys and Temples",
    "content": """<p>There's something about living in an island paradise that makes everyone really happy and super friendly. Shocker. It's day three and I've already made contact with my online friends who helped prep me for the trip, and about a half dozen new expats. Bali Dinner Club is in the works, maybe two weeks out from our first event, and we're already invited to a BBQ at the villa of an awesome Al Jazeera reporter and her surf instructor boyfriend.</p>
<p>The best part is that I've found a home base about 5 minutes walk from my villa — a co-working space called Dojo Bali. It's THE PERFECT place for any digital nomad. Crazy fast wifi, cafe, pool, lockers, Skype booths, conference rooms, and adorable cats and dogs to play with. Of course the best part is the people. Everyone here is doing something with their lives online to make money while living the dream in a tropical heaven.</p>
<p>The local food is delicious and so so so cheap. I'm spending about $6 a day on food. That's breakfast, lunch and dinner. Beers are between $1.50 and $3.00 depending on where you are. Massages are $7 for an hour. Uber drivers cost about 1/10th the LA price — we're going to Ubud this weekend, our driver will cost $30 for 10 hours. That includes taking us wherever we want, waiting, and getting us home. It's almost too good to be true, but I promise you it is.</p>"""
  },
  {
    "file": "monkeys-temples.html",
    "title": "Monkeys and Temples and Midnight Motorcycle Chases!",
    "date": "February 9, 2016",
    "category": "Bali · Exploring",
    "breadcrumb": "Bali",
    "prev_url": "making-friends.html",
    "prev_label": "Making Friends is Stupid Easy",
    "next_url": "gili-islands.html",
    "next_label": "The Gili Islands",
    "content": """<p>This last weekend Scotty, Jessie, and I joined our new friend Theiry for a day trip to Ubud, the cultural capital of Bali! We started in the rice fields for a hike through the famous stepped terraces as local Balinese planted fresh sprouts for harvest. It really was stunning. Then it was off to meet the civets and drink the Kopi Luwak coffee — supposedly the best coffee in the world, grown on the island, eaten by the cat-like creatures and pooped out, before being cleaned and roasted. The coffee was indeed a deep rich flavor. The best part was relaxing in the huge tree-house structure over the rice fields and tasting all the local coffees and teas.</p>
<p>After the strong kick of caffeine we ventured deeper into the forest to the Water Temple. This gorgeous 1000+ year old temple was built around natural springs and is a sacred Hindu place of purification. After that it was time for the Sacred Monkey Forest!!!</p>
<p>They may be cute as hell, but these monkeys are aggressive little creatures. After a few failed attempts at giving them bananas (they just came up, yelled and grabbed them while I screamed), we finally managed to get a few pics. Everyone got nipped at least once.</p>
<p>We closed out the day with pictures at the palace in the center of town and yummy gelato. Then last night we decided to head to the party town about 20 minutes away — Seminyak! So far I've spent about $250 total on my trip, not including housing and airfare. Bali is everything it was promised to be.</p>"""
  },
  {
    "file": "gili-islands.html",
    "title": "Dojo BBQ, The Gili Islands, And A Turtle",
    "date": "February 15, 2016",
    "category": "Bali · Exploring",
    "breadcrumb": "Bali",
    "prev_url": "monkeys-temples.html",
    "prev_label": "Monkeys and Temples",
    "next_url": "balinese-dancing.html",
    "next_label": "Balinese Dancing and Dinner Club",
    "content": """<p>The Gili Islands are a short boat ride from Bali and are one of the most popular destinations in all of Indonesia. Three tiny islands with no motorized vehicles — just horses, bikes, and your feet. The water is crystal clear turquoise and the snorkeling is some of the best in the world.</p>
<p>We booked a fast boat from Canggu and were there in under 2 hours. The boat ride itself was an adventure — the waves were massive and we were soaked by the time we arrived. Worth every drop.</p>
<p>The highlight was snorkeling with sea turtles. Not one turtle, but three. They were enormous and completely unbothered by us floating alongside them. It's one of those moments you can't really describe — you just have to be there.</p>
<p>Back at the Dojo we hosted our first BBQ, which quickly turned into a 40-person party. The expat community here is remarkable. Within two weeks I know more people in Bali than I knew in my first year in DTLA.</p>"""
  },
  {
    "file": "balinese-dancing.html",
    "title": "Balinese Dancing and Dinner Club Number One",
    "date": "February 26, 2016",
    "category": "Bali · Dinner Club",
    "breadcrumb": "Bali",
    "prev_url": "gili-islands.html",
    "prev_label": "The Gili Islands",
    "next_url": "22-things.html",
    "next_label": "22 Things I Learned",
    "content": """<p>Two of my favorite things collided in the best possible way this week: traditional Balinese culture and the Dinner Club.</p>
<p>We attended a Kecak fire dance at a clifftop temple overlooking the Indian Ocean at sunset. About 50 men in traditional dress chant and sway in hypnotic unison while dancers tell the story of the Ramayana — the Hindu epic. With the sun going down behind them and fire lit at their feet, it was one of the most stunning things I've ever witnessed.</p>
<p>The very next evening we hosted Dinner Club Number One in Bali. I'd been organizing it for two weeks through the Dojo community and word of mouth. We had 22 people show up to a gorgeous rooftop restaurant in Canggu. An Israeli chef prepared a mezze feast and people from 11 different countries sat together, met each other, and did what Dinner Club has always done — turned strangers into friends.</p>
<p>I've been doing this in DTLA for years and I wasn't sure it would translate to a place where everyone is already so open and social. It did. Better, in some ways. When you're all living this unusual expat life, there's an instant bond that doesn't require breaking down the same walls you'd encounter at home.</p>"""
  },
  {
    "file": "22-things.html",
    "title": "22 Things I Learned in My First 30 Days in Bali",
    "date": "March 12, 2016",
    "category": "Bali · Life There",
    "breadcrumb": "Bali",
    "prev_url": "balinese-dancing.html",
    "prev_label": "Balinese Dancing and Dinner Club",
    "next_url": "how-to-live-like-a-king.html",
    "next_label": "How to Live Like a King for $1500/month",
    "content": """<p>One month in Bali. Here's what I know now that I didn't know before:</p>
<p><strong>1.</strong> The traffic is insane but it has a rhythm — you just have to find it. <strong>2.</strong> Everyone honks, but it means "I'm here," not "you idiot." <strong>3.</strong> Warung food (local small restaurants) is almost always better than anything aimed at tourists. <strong>4.</strong> You WILL get sick at least once. Drink bottled water. Always. <strong>5.</strong> The internet at co-working spaces is fast. The internet everywhere else is not. <strong>6.</strong> Learn a few words in Bahasa Indonesian. Even butchered attempts make locals laugh and love you. <strong>7.</strong> The $7 massage is not a luxury. It's medicine. Get one as often as possible. <strong>8.</strong> Sunscreen is a lifestyle, not a choice. <strong>9.</strong> Temple ceremonies are everywhere and gorgeous. If you see one, stop and watch. <strong>10.</strong> Grab food is the Indonesian Uber Eats and it costs about $2 including delivery.</p>
<p><strong>11.</strong> The expat community is warm, talented, and surprisingly drama-free. <strong>12.</strong> A motorbike is faster than a car almost everywhere. <strong>13.</strong> Nasi goreng (fried rice) for breakfast is the move. <strong>14.</strong> Sarongs are required at temples. Keep one in your bag. <strong>15.</strong> The rice paddies in the center of the island look exactly like the movies. Better, actually. <strong>16.</strong> Don't touch the monkeys at Monkey Forest. They will bite you. <strong>17.</strong> The sunsets here are different. Slower. More intentional. <strong>18.</strong> You can negotiate almost everything. <strong>19.</strong> Your concept of "expensive" will be permanently altered. <strong>20.</strong> People smile here constantly. Not fake smiles. Real ones. <strong>21.</strong> You'll call your friends in LA and realize they sound stressed in a way you no longer are. <strong>22.</strong> You'll start to wonder why you waited this long.</p>"""
  },
  {
    "file": "how-to-live-like-a-king.html",
    "title": "How to Live Like A King In Bali For $1500 A Month!",
    "date": "April 20, 2016",
    "category": "Bali · Money",
    "breadcrumb": "Bali",
    "prev_url": "22-things.html",
    "prev_label": "22 Things I Learned",
    "next_url": "transfer-money.html",
    "next_label": "How to Transfer Money Without Getting Screwed",
    "content": """<p>Three months in, I've got my budget dialed. Here's the real breakdown of what it costs to live well in Bali:</p>
<p><strong>Housing:</strong> My share of our beautiful 3-bedroom villa with a pool in Canggu — $500/month. This is genuinely stunning. If I were renting solo, a great villa would run $600-800.</p>
<p><strong>Food:</strong> $200/month eating like royalty. Local warungs are $1-3 per meal. A night out at a nice restaurant with drinks is $15-25 total. I eat out for almost every meal.</p>
<p><strong>Transport:</strong> $50/month. Uber is everywhere and dirt cheap. A motorbike rental is $80/month if you prefer that (I don't, I value my life).</p>
<p><strong>Co-working (Dojo):</strong> $100/month. Fast internet, great community, air conditioning, pool.</p>
<p><strong>Entertainment, massages, activities:</strong> $200/month — and that's being generous. Massages are $7/hour. Beers are $2. Entry to most things is free or nearly free.</p>
<p><strong>Miscellaneous:</strong> $200/month for flights, surprises, gifts, tourist activities.</p>
<p>Total: <strong>$1,250-1,500/month</strong> for a genuinely spectacular life. That's less than I paid monthly for parking in DTLA.</p>"""
  },
  {
    "file": "transfer-money.html",
    "title": "Learn How To Transfer Money To Bali Without Getting SCREWED!",
    "date": "May 12, 2016",
    "category": "Bali · Money",
    "breadcrumb": "Bali",
    "prev_url": "how-to-live-like-a-king.html",
    "prev_label": "How to Live Like a King for $1500/month",
    "next_url": "happy-hours-canggu.html",
    "next_label": "Happy Hours in Canggu",
    "content": """<p>This is one of those posts that could save you a lot of money. I learned most of this the hard way, so you don't have to.</p>
<h2>Don't Use Your Regular Bank</h2>
<p>Your US bank will murder you on exchange rates and fees. I'm talking 3-5% above the mid-market rate, plus a flat fee, plus a foreign transaction fee. On a $1,000 transfer you could lose $50-80 without realizing it.</p>
<h2>Use Transferwise (Now Wise)</h2>
<p>By far the best option I found. They use the mid-market exchange rate and charge a small transparent fee. On a $1,000 transfer I saved about $40 compared to my bank. Over a year that adds up to hundreds of dollars.</p>
<h2>The ATM Game in Bali</h2>
<p>BCA ATMs have the best rates and lowest fees of the local banks. Avoid the standalone ATMs near tourist areas — they will offer to do the conversion for you at a terrible rate. Always say NO to "conversion" and let your card do the conversion at home. Withdraw in large amounts to minimize per-transaction fees.</p>
<h2>Keep a Buffer</h2>
<p>ATMs sometimes run out of cash, especially on holidays. Keep a week's worth of rupiah on hand. The rupiah comes in massive bills — a 100,000 IDR note is worth about $7 — so your wallet will always feel full even when it isn't.</p>"""
  },
  {
    "file": "happy-hours-canggu.html",
    "title": "The Ultimate Guide to Happy Hours in Canggu",
    "date": "June 4, 2016",
    "category": "Bali · Local Tips",
    "breadcrumb": "Bali",
    "prev_url": "transfer-money.html",
    "prev_label": "Transfer Money Without Getting Screwed",
    "next_url": "singapore.html",
    "next_label": "Saving Thousands in Singapore",
    "content": """<p>Six months in Canggu means I've done the research. Here's your definitive guide to maximizing the happy hour situation in one of Bali's best neighborhoods.</p>
<p><strong>Dojo Bali</strong> has a daily 5pm happy hour that's technically not a happy hour — cheap drinks are just always on the menu. The real value is the community. Best place to meet interesting people doing interesting things.</p>
<p><strong>Old Man's</strong> is the legendary Canggu beach bar. Sunday sessions draw hundreds of people. $2 Bintangs all day, every day. The vibe alone is worth it.</p>
<p><strong>Finns Beach Club</strong> is where you go when you want to feel fancy. Pool, ocean views, solid cocktails. Their weekday happy hour runs 4-6pm with half-price cocktails.</p>
<p><strong>Betelnut</strong> is the hidden gem — a tiny spot on a gang (alley) that makes the best cocktails in Canggu for about $4. Happy hour 5-7pm every day.</p>
<p><strong>Batu Bolong Beach</strong> is not a bar, but the beach itself functions as one at sunset. Dozens of warungs line the sand, cold Bintang is $1.50, and the sunsets are outrageous. This is my go-to at least twice a week. No reservations, no dress code, no pretension. Just cold beer and a sky on fire.</p>"""
  },
  {
    "file": "singapore.html",
    "title": "6 Simple Tips For Saving Thousands In Singapore",
    "date": "June 19, 2016",
    "category": "Bali · Side Trips",
    "breadcrumb": "Bali",
    "prev_url": "happy-hours-canggu.html",
    "prev_label": "Happy Hours in Canggu",
    "next_url": "top-10-reasons.html",
    "next_label": "Top 10 Reasons to Move to Bali",
    "content": """<p>Every two months in Bali you need to do a "visa run" — leave the country and come back to reset your visa. Most people do Thailand or Singapore. I chose Singapore, and I'm glad I did.</p>
<p><strong>1. Fly AirAsia.</strong> The Denpasar–Singapore route on AirAsia is almost always under $80 round trip if you book a few weeks ahead. Bring only a carry-on and you'll pay even less.</p>
<p><strong>2. Stay in Little India.</strong> Singapore is one of Asia's most expensive cities, but Little India has guesthouses for $30-50/night that are clean, safe, and perfectly located. The food in the neighborhood is extraordinary and costs almost nothing.</p>
<p><strong>3. The hawker centers are the move.</strong> Singapore's famous food courts serve world-class food for $3-6 a dish. Lau Pa Sat, Maxwell Food Centre, and Chinatown Complex are my favorites. Do not eat at restaurants near Marina Bay.</p>
<p><strong>4. The MRT will take you anywhere.</strong> Singapore's subway is one of the best in the world and costs pennies. Don't take taxis.</p>
<p><strong>5. Gardens by the Bay is free (mostly).</strong> The Supertrees, the outdoor gardens, the nightly light show — all free. Only the indoor cloud forest domes cost money.</p>
<p><strong>6. Stock up on things you can't get in Bali.</strong> Decent cheese, good wine, Western medicines, specific supplements, quality sunscreen. Singapore has it all at prices that feel expensive compared to Bali but are actually reasonable compared to the US.</p>"""
  },
  {
    "file": "top-10-reasons.html",
    "title": "Top 10 Reasons to Move to Bali",
    "date": "July 14, 2016",
    "category": "Bali · Life There",
    "breadcrumb": "Bali",
    "prev_url": "singapore.html",
    "prev_label": "Saving Thousands in Singapore",
    "next_url": "7-life-hacks.html",
    "next_label": "7 Essential Life Hacks for Bali",
    "content": """<p>Seven months in, here are my top 10 reasons you should consider making the move:</p>
<p><strong>1. The cost of living is absurdly low.</strong> $1,500/month buys a genuinely luxurious life. A beautiful villa, daily restaurant meals, massages, activities — all of it.</p>
<p><strong>2. The weather is perfect.</strong> Warm year round. The "rainy season" still involves mostly sunny days with rain in the evenings. It's not a real rainy season by any normal definition.</p>
<p><strong>3. The food is incredible.</strong> And cheap. Indonesian food is one of the world's great cuisines and you'll eat like royalty for $5 a day if you eat local.</p>
<p><strong>4. The expat community is extraordinary.</strong> Bali attracts an unusually interesting, creative, entrepreneurial group of people. Your network will expand in ways you can't predict.</p>
<p><strong>5. The nature is stunning.</strong> Volcanoes, rice paddies, tropical forest, coral reefs, sea turtles. All within 30 minutes of wherever you're staying.</p>
<p><strong>6. The Balinese people are genuinely kind.</strong> This isn't tourist-industry friendliness. The Balinese culture values community, ceremony, and hospitality in a way that seeps into everything.</p>
<p><strong>7. It's safe.</strong> Very safe. Petty theft exists (lock your motorbike) but violent crime is almost unheard of.</p>
<p><strong>8. The internet is good enough.</strong> At co-working spaces, it's great. Everywhere else it's adequate. You can run a business here.</p>
<p><strong>9. It will change your perspective permanently.</strong> On money, on time, on what's necessary, on what's luxurious.</p>
<p><strong>10. You can always go back.</strong> Your old life will still be there. This one won't wait for you.</p>"""
  },
  {
    "file": "7-life-hacks.html",
    "title": "7 Essential Life Hacks For Your First Trip To Bali",
    "date": "August 2, 2016",
    "category": "Bali · Local Tips",
    "breadcrumb": "Bali",
    "prev_url": "top-10-reasons.html",
    "prev_label": "Top 10 Reasons to Move to Bali",
    "next_url": "cooking-classes.html",
    "next_label": "Cooking Classes at The Amala",
    "content": """<p>Whether you're visiting for a week or thinking about staying longer, these seven tips will save you time, money, and stress.</p>
<p><strong>1. Download Grab before you land.</strong> Indonesia's version of Uber is ubiquitous, cheap, and has GPS — meaning no negotiating with taxi drivers who'll quote you 5x the real price.</p>
<p><strong>2. Get a local SIM card at the airport.</strong> Telkomsel has the best coverage. For about $10 you'll get a month of data. Don't rely on hotel wifi for anything important.</p>
<p><strong>3. Bring USD cash.</strong> The ATMs work, but having USD gives you options and the exchange rate is often better at money changers. Use PT Dirgahayu — the most reputable chain.</p>
<p><strong>4. Learn to negotiate for motorbike rentals, but not for food.</strong> Negotiating food prices is rude. Everything else is fair game.</p>
<p><strong>5. Keep a sarong in your bag at all times.</strong> Many temples require them. Locals sell them at the entrance but the prices are high and the quality is low.</p>
<p><strong>6. Don't touch offerings.</strong> The small flower and incense arrangements on the ground are religious offerings, not decorations. Step around them.</p>
<p><strong>7. Say yes to things that scare you slightly.</strong> The cooking class you weren't sure about. The sunrise hike up a volcano. The local ceremony you stumbled upon. Bali rewards the slightly adventurous.</p>"""
  },
  {
    "file": "cooking-classes.html",
    "title": "De-Mystifying Bali Flavors With Cooking Classes at The Amala Resort",
    "date": "September 5, 2016",
    "category": "Bali · Exploring",
    "breadcrumb": "Bali",
    "prev_url": "7-life-hacks.html",
    "prev_label": "7 Essential Life Hacks",
    "next_url": "visa-nightmare.html",
    "next_label": "144 Hour Chinese Transit Visa Nightmare",
    "content": """<p>The Amala is one of the most beautiful resorts in Seminyak — a lush green compound of villas with a yoga shala, spa, and one of Bali's most respected farm-to-table restaurants. Their cooking class is run by the resort's head chef and is genuinely one of the best experiences I've had on the island.</p>
<p>We started at the market at 7am, wandering through the stalls with the chef as he pointed out the turmeric roots, galangal, kaffir lime leaves, palm sugar, and the dozens of chili varieties that define Balinese cuisine. Most tourists never get into a real local market. It's chaotic and beautiful and smells like something between a flower shop and a spice cabinet.</p>
<p>Back at the Amala we learned to make a base gede — the master spice paste that underlies most Balinese dishes — from scratch. You pound it by hand with a mortar and pestle until your arms give out. Then you make it again. Then you understand why Balinese cooking takes time.</p>
<p>We made satay lilit (minced seafood wrapped around lemongrass), lawar (a ceremonial dish of minced meat, vegetables, and freshly grated coconut), nasi goreng, and a turmeric-based dessert that tasted like nothing I've ever had in an Indonesian restaurant abroad. Because it wasn't made for export. It was made here, with ingredients grown here, for people who live here. That's the difference.</p>"""
  },
  {
    "file": "visa-nightmare.html",
    "title": "144 Hour Chinese Transit Visa Nightmare",
    "date": "October 17, 2016",
    "category": "Bali · Side Trips",
    "breadcrumb": "Bali",
    "prev_url": "cooking-classes.html",
    "prev_label": "Cooking Classes at The Amala",
    "next_url": "co-working-dtla.html",
    "next_label": "Best Co-Working Space in DTLA",
    "content": """<p>China has a fascinating and little-known policy: citizens of 51 countries can transit through certain Chinese cities without a visa for up to 144 hours. This is a legitimate free trip to China disguised as a layover. I decided to try it.</p>
<p>Getting the transit exemption requires that you're traveling between two different countries — you can't fly in from Bali and back to Bali. So I booked Bali → Shanghai → Singapore, planning to spend 5 days in Shanghai before continuing to Singapore for my visa run.</p>
<p>Here's where it got complicated. The airline had never processed this exemption before. The check-in agent in Denpasar was convinced I needed a visa. I had printed the official Chinese government policy. She called her supervisor. The supervisor called their supervisor. Forty-five minutes at the check-in desk while my flight's departure time approached.</p>
<p>Eventually they let me board. Immigration in Shanghai was smooth — they knew exactly what the 144-hour policy was. I spent 5 incredible days in Shanghai, made it to Singapore for my visa run, and flew back to Bali having visited three countries for less than $200 in flights.</p>
<p>The lesson: know your rights as a traveler, print your documentation, and stay calm when airline agents don't know their own rules.</p>"""
  },
  {
    "file": "co-working-dtla.html",
    "title": "The Very Best Co-Working Space in DTLA You've Never Heard Of",
    "date": "April 3, 2018",
    "category": "Back in DTLA",
    "breadcrumb": "Adventures",
    "prev_url": "visa-nightmare.html",
    "prev_label": "144 Hour Chinese Transit Visa Nightmare",
    "content": """<p>A little over a year after leaving, I came back to DTLA. Bali did what it was supposed to do — I paid off the high-interest loan, recalibrated my sense of what I need to be happy, and came home with a completely different perspective on the city I've loved for 20 years.</p>
<p>But I came back as a digital nomad who'd spent a year working from some of the best co-working spaces in Asia, so I wasn't about to go back to working from home. I needed to find the best place in DTLA.</p>
<p>The answer is WeWork? Industrious? Cross Campus? None of the above.</p>
<p>The best co-working space in Downtown Los Angeles that almost nobody knows about is <strong>The Downtown Independent</strong> — a 1926 movie theater on Hill Street that has been converted into a creative workspace. Original plaster ceilings, art deco details, high-speed internet, and a community of filmmakers, writers, and designers who feel like they're working in a set piece from another era.</p>
<p>The membership is affordable, the coffee is excellent, and on some days they still screen films in the original theater downstairs. It's the DTLA version of Dojo Bali — a place with a soul, not just a floorplan.</p>
<p>If you're a creative professional working in Downtown Los Angeles and you haven't been, go. You can thank me later.</p>"""
  },
]

for p in extra_posts:
    html = post(
        filename=p["file"],
        title=p["title"],
        date=p["date"],
        category=p["category"],
        breadcrumb_label=p["breadcrumb"],
        content=p["content"],
        prev_url=p.get("prev_url"),
        prev_label=p.get("prev_label"),
        next_url=p.get("next_url"),
        next_label=p.get("next_label"),
    )
    path = Path(__file__).resolve().parent / "posts" / p["file"]
    with path.open('w', encoding='utf-8') as f:
        f.write(html)
    print(f'✓ {p["file"]}')

print(f'\nTotal extra posts: {len(extra_posts)}')
