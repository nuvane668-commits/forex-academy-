from pathlib import Path

pages = {
"lesson-pairs.html": (
"Currency Pairs",
"""
<p>A currency pair shows the value of one currency compared with another.</p>

<h2>Base and quote currency</h2>
<p>In EUR/USD, EUR is the base currency and USD is the quote currency.</p>

<div class="box">
<strong>Example:</strong><br>
EUR/USD = 1.1000<br><br>
This means one euro corresponds to 1.1000 US dollars at that quoted rate.
</div>

<h2>Major pairs</h2>
<p>Major currency pairs generally involve the US dollar and are among the most actively traded pairs.</p>

<h2>Minor pairs</h2>
<p>Minor pairs generally involve major currencies but exclude the US dollar.</p>

<h2>Exotic pairs</h2>
<p>Exotic pairs generally combine a major currency with a currency from a smaller or emerging economy. They can have different liquidity and trading costs.</p>

<h2>Pips</h2>
<p>A pip is a commonly used unit for describing small price changes in forex. The exact convention depends on the currency pair and broker.</p>

<h2>Spread</h2>
<p>The spread is the difference between the bid and ask price. It is one of the costs a trader should consider before entering a position.</p>
"""
),

"lesson-candles.html": (
"Candlesticks",
"""
<p>Candlesticks are one of the most common ways traders visualize price movement.</p>

<div class="box">
<strong>Every candle can show:</strong><br>
Open — where the period began.<br>
High — highest price reached.<br>
Low — lowest price reached.<br>
Close — where the period ended.
</div>

<h2>Candle body</h2>
<p>The body shows the relationship between the opening and closing price.</p>

<h2>Wicks</h2>
<p>The upper and lower wicks show prices that were reached outside the candle body.</p>

<h2>Bullish and bearish candles</h2>
<p>A bullish candle closes above its open. A bearish candle closes below its open.</p>

<h2>Do not trade candles alone</h2>
<p>A candle pattern should be considered together with market structure, location, timeframe and risk management.</p>

<h2>Practice</h2>
<p>Open the Practice Lab and try identifying areas where price rejected a level or continued through a level.</p>
"""
),

"lesson-structure.html": (
"Market Structure",
"""
<p>Market structure describes how price forms highs and lows.</p>

<div class="box">
<strong>Uptrend:</strong> higher highs and higher lows.<br><br>
<strong>Downtrend:</strong> lower highs and lower lows.<br><br>
<strong>Range:</strong> price moves between relatively defined areas without a sustained directional trend.
</div>

<h2>Why structure matters</h2>
<p>Understanding structure helps a trader describe what price is doing instead of simply guessing whether it will rise or fall.</p>

<h2>Break of structure</h2>
<p>When price moves beyond an important previous high or low, it may provide information about changing market conditions. However, a break does not automatically mean a trade should be entered.</p>

<h2>Multiple timeframes</h2>
<p>A trader may use a higher timeframe to understand broader context and a lower timeframe to study a possible setup.</p>

<h2>Beginner exercise</h2>
<p>Look at a chart and mark the most recent significant highs and lows. Ask: Is price making higher highs, lower lows, or moving sideways?</p>
"""
),

"lesson-levels.html": (
"Support & Resistance",
"""
<p>Support and resistance are areas where price has previously reacted.</p>

<h2>Support</h2>
<p>Support is an area where buying interest has previously helped prevent or slow a downward move.</p>

<h2>Resistance</h2>
<p>Resistance is an area where selling interest has previously helped prevent or slow an upward move.</p>

<div class="box">
<strong>Important:</strong> Think of support and resistance as zones rather than perfectly precise lines.
</div>

<h2>How to mark a zone</h2>
<ol>
<li>Look for repeated price reactions.</li>
<li>Identify the area containing important highs or lows.</li>
<li>Mark a reasonable zone around the reaction area.</li>
<li>Wait to see how price behaves when it returns.</li>
</ol>

<h2>Break and retest</h2>
<p>Sometimes price breaks through an important zone and later returns to test it. This can become part of a strategy, but it is not guaranteed to work every time.</p>

<h2>Practice</h2>
<p>Use the Practice Lab to mark possible support and resistance zones.</p>
"""
),

"lesson-entries.html": (
"Finding Potential Entries",
"""
<p>A good trading process starts with a plan. The goal is not to predict every market movement but to define situations where your strategy gives you a reason to participate.</p>

<h2>Before considering an entry</h2>

<ol>
<li>Check the broader market context.</li>
<li>Identify the current market structure.</li>
<li>Mark important support and resistance zones.</li>
<li>Wait for price to reach an area relevant to your strategy.</li>
<li>Look for your predefined confirmation condition.</li>
<li>Define the invalidation point.</li>
<li>Calculate the position size.</li>
<li>Determine the potential target.</li>
</ol>

<h2>Example framework</h2>

<div class="box">
The market is showing a bullish structure.<br>
Price pulls back toward a previously identified support zone.<br>
Your predefined confirmation condition appears.<br>
You calculate the risk before considering the entry.
</div>

<h2>What not to do</h2>

<p>Do not enter simply because a candle looks exciting, because price has already moved a lot, or because you are afraid of missing the move.</p>
"""
),

"lesson-risk.html": (
"Risk Management",
"""
<p>Risk management is one of the most important skills a trader can develop.</p>

<h2>Risk amount</h2>

<p>A simple planning formula is:</p>

<div class="box">
<strong>Risk amount = Account balance × Risk percentage</strong>
</div>

<p>For example, if someone chooses to risk 1% of a hypothetical $1,000 account, the planned risk would be $10. This is an educational example, not a recommendation of what percentage you should use.</p>

<h2>Stop loss</h2>
<p>A stop loss can define where the original trade idea is considered invalid. It does not guarantee the exact exit price in every market condition.</p>

<h2>Risk/reward</h2>
<p>Before entering, compare the amount you could lose with the potential amount you are targeting.</p>

<h2>Position sizing</h2>
<p>Position size should be calculated from the amount you are willing to risk and the distance to your invalidation point—not simply from how much money is available in the account.</p>

<h2>Protect essential money</h2>

<div class="box">
Never use money needed for school fees, rent, food, bills or emergencies as trading capital.
</div>
"""
),

"lesson-psychology.html": (
"Trading Psychology",
"""
<p>Trading decisions can be affected by emotions because outcomes are uncertain.</p>

<h2>Fear</h2>
<p>Fear can cause someone to exit too early, avoid valid setups or change their plan during a trade.</p>

<h2>Greed</h2>
<p>Greed can encourage excessive position sizes or unrealistic profit expectations.</p>

<h2>FOMO</h2>
<p>Fear of missing out can cause traders to enter after a large move has already happened.</p>

<h2>Revenge trading</h2>
<p>Trying to immediately recover a loss can lead to emotional decisions and excessive risk.</p>

<h2>Discipline</h2>
<p>A written trading plan can help reduce impulsive decisions. The objective is to follow a repeatable process rather than trying to win every trade.</p>

<h2>Trading journal</h2>
<p>Record why you entered, what your plan was, whether you followed it and what you learned.</p>
"""
),

"lesson-fundamentals.html": (
"Fundamental Analysis",
"""
<p>Fundamental analysis studies economic and financial factors that can influence currencies.</p>

<h2>Important economic factors</h2>

<ul>
<li>Central-bank interest rates</li>
<li>Inflation</li>
<li>Employment data</li>
<li>Economic growth</li>
<li>Government policy</li>
<li>Geopolitical developments</li>
<li>Market expectations</li>
</ul>

<h2>Interest rates</h2>
<p>Changes in interest-rate expectations can influence demand for currencies because they can affect the attractiveness of assets denominated in that currency.</p>

<h2>Economic news</h2>
<p>Major announcements can produce rapid price movements and changing trading conditions.</p>

<div class="box">
<strong>Beginner habit:</strong> Before trading, know whether major economic events are scheduled for the currencies you are analyzing.
</div>
"""
)
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Forex Academy</title>

<style>
*{{box-sizing:border-box}}

body{{
margin:0;
font-family:Arial,sans-serif;
background:#f4f6f8;
color:#17202a;
line-height:1.7
}}

header{{
background:#101820;
color:white;
padding:18px
}}

.nav{{
max-width:900px;
margin:auto;
display:flex;
justify-content:space-between;
align-items:center
}}

.nav a{{
color:white;
text-decoration:none
}}

main{{
max-width:900px;
margin:auto;
padding:30px 18px
}}

article{{
background:white;
padding:30px;
border-radius:12px;
box-shadow:0 3px 15px rgba(0,0,0,.07)
}}

h1{{margin-top:0}}

h2{{
margin-top:30px
}}

.box{{
background:#eef2f5;
padding:18px;
border-radius:8px;
margin:18px 0
}}

.warning{{
background:#fff3cd;
padding:18px;
border-radius:8px;
margin-top:25px
}}

.back{{
display:inline-block;
margin-top:25px;
background:#172a3a;
color:white;
padding:12px 18px;
border-radius:7px;
text-decoration:none
}}

footer{{
text-align:center;
padding:30px;
color:#666
}}
</style>
</head>

<body>

<header>
<div class="nav">
<strong>Forex Academy</strong>
<a href="index.html">Home</a>
</div>
</header>

<main>

<article>

<h1>{title}</h1>

{content}

<div class="warning">
<strong>⚠️ Educational warning</strong>
<p>
Forex trading involves substantial risk. The examples on this website are for educational purposes and are not guaranteed trading signals or personalized financial advice.
</p>
</div>

<a class="back" href="index.html">
← Back to Lessons
</a>

</article>

</main>

<footer>
© 2026 Forex Academy
</footer>

</body>
</html>
"""

for filename, (title, content) in pages.items():
    Path(filename).write_text(
        template.format(title=title, content=content),
        encoding="utf-8"
    )

print("All lesson pages created successfully.")
