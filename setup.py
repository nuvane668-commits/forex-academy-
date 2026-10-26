from pathlib import Path

files = {}

files["index.html"] = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Forex Academy - Learn forex trading from beginner to advanced with practical chart analysis, strategies, risk management and psychology.">
<title>Forex Academy | Learn Forex Trading</title>
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;background:#f4f6f8;color:#17202a;line-height:1.6}
header{background:#101820;color:#fff;position:sticky;top:0;z-index:20}
.nav{max-width:1150px;margin:auto;padding:15px 18px;display:flex;align-items:center;justify-content:space-between;gap:15px}
.logo{font-weight:800;font-size:21px}
nav{display:flex;gap:15px;flex-wrap:wrap}
nav a{color:#fff;text-decoration:none;font-size:14px}
.hero{background:#172a3a;color:#fff;padding:75px 20px;text-align:center}
.hero h1{font-size:42px;line-height:1.15;margin:0 0 15px}
.hero p{max-width:700px;margin:auto;color:#dce5eb;font-size:18px}
.btn{display:inline-block;background:#00a86b;color:#fff;padding:13px 20px;border-radius:8px;text-decoration:none;font-weight:bold;margin-top:22px}
.container{max-width:1150px;margin:auto;padding:45px 18px}
.center{text-align:center}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}
.card{background:#fff;padding:24px;border-radius:12px;box-shadow:0 3px 15px rgba(0,0,0,.07)}
.card h3{margin-top:0}
.card a{color:#087f5b;font-weight:bold;text-decoration:none}
.number{font-size:13px;color:#087f5b;font-weight:bold}
.ad{min-height:90px;background:#eef1f4;border:1px dashed #adb5bd;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#777;margin:25px 0}
.warning{background:#fff3cd;padding:20px;border-radius:10px}
footer{background:#101820;color:#ccc;text-align:center;padding:35px 18px}
@media(max-width:650px){.hero h1{font-size:31px}nav{gap:8px}.container{padding:30px 14px}}
</style>
</head>
<body>
<header>
<div class="nav">
<div class="logo">Forex Academy</div>
<nav>
<a href="index.html">Home</a>
<a href="#lessons">Lessons</a>
<a href="training.html">Training</a>
<a href="practice.html">Practice</a>
<a href="strategy.html">Strategies</a>
<a href="journal.html">Journal</a>
</nav>
</div>
</header>

<section class="hero">
<h1>Learn Forex Trading From Zero</h1>
<p>Understand currencies, charts, market structure, technical analysis, strategies, risk management and trading psychology through practical lessons.</p>
<a class="btn" href="#lessons">Start Learning</a>
</section>

<main>
<div class="container">

<div class="ad">Advertisement</div>

<h2 id="lessons" class="center">Forex Learning Path</h2>

<div class="grid">

<div class="card">
<span class="number">01 • BEGINNER</span>
<h3>What Is Forex?</h3>
<p>Understand the foreign exchange market, currency pairs and why prices move.</p>
<a href="forex.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">02 • BEGINNER</span>
<h3>Currency Pairs</h3>
<p>Learn base currency, quote currency, majors, minors, exotics and pips.</p>
<a href="lesson-pairs.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">03 • CHARTS</span>
<h3>Candlesticks</h3>
<p>Learn what candles show and how to interpret price action without guessing.</p>
<a href="lesson-candles.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">04 • ANALYSIS</span>
<h3>Market Structure</h3>
<p>Learn higher highs, higher lows, lower highs, lower lows and ranges.</p>
<a href="lesson-structure.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">05 • TECHNICAL</span>
<h3>Support & Resistance</h3>
<p>Learn how to identify and mark important price zones.</p>
<a href="lesson-levels.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">06 • ENTRIES</span>
<h3>Finding Setups</h3>
<p>Learn how traders build a reasoned entry instead of entering randomly.</p>
<a href="lesson-entries.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">07 • RISK</span>
<h3>Risk Management</h3>
<p>Learn stop-losses, position sizing, risk/reward and capital protection.</p>
<a href="lesson-risk.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">08 • MINDSET</span>
<h3>Trading Psychology</h3>
<p>Understand fear, greed, FOMO, revenge trading, patience and discipline.</p>
<a href="lesson-psychology.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">09 • FUNDAMENTALS</span>
<h3>Economic News</h3>
<p>Learn how interest rates, inflation, employment and central banks can affect currencies.</p>
<a href="lesson-fundamentals.html">Start lesson →</a>
</div>

<div class="card">
<span class="number">10 • STRATEGY</span>
<h3>Build Your Strategy</h3>
<p>Turn your ideas into objective entry, exit and risk rules.</p>
<a href="strategy.html">Build strategy →</a>
</div>

</div>

<div class="ad">Advertisement</div>

<h2 class="center">Practice What You Learn</h2>

<div class="grid">

<div class="card">
<h3>📊 Training Zone</h3>
<p>Study a market chart and learn the analysis process step by step.</p>
<a href="training.html">Open Training Zone →</a>
</div>

<div class="card">
<h3>🎯 Practice Lab</h3>
<p>Practice identifying trend, support, resistance, entry, stop and target.</p>
<a href="practice.html">Open Practice Lab →</a>
</div>

<div class="card">
<h3>🧩 Strategy Builder</h3>
<p>Create your own written trading rules and test whether they are objective.</p>
<a href="strategy.html">Build a strategy →</a>
</div>

<div class="card">
<h3>📒 Trading Journal</h3>
<p>Record practice trades, reasons, results and lessons learned.</p>
<a href="journal.html">Open Journal →</a>
</div>

</div>

<div class="ad">Advertisement</div>

<div class="warning">
<strong>⚠️ Risk warning</strong>
<p>Forex trading involves substantial risk. Educational examples on this website are not guaranteed trading signals or personalized financial advice. Never risk money needed for essential expenses.</p>
</div>

</div>
</main>

<footer>
<p>© 2026 Forex Academy</p>
<p>Learn • Analyze • Practice • Manage Risk</p>
</footer>
</body>
</html>
'''

files["forex.html"] = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>What Is Forex? | Forex Academy</title>
<style>
body{margin:0;font-family:Arial;background:#f4f6f8;color:#17202a;line-height:1.7}
header{background:#101820;color:white;padding:18px}
.nav,main{max-width:900px;margin:auto}
.nav{display:flex;justify-content:space-between}.nav a{color:white}
main{padding:30px 18px}.lesson{background:white;padding:30px;border-radius:12px}
.example{background:#eef2f5;padding:18px;border-radius:8px}.warning{background:#fff3cd;padding:18px;border-radius:8px}
.back{display:inline-block;background:#172a3a;color:white;padding:11px 16px;border-radius:7px;text-decoration:none;margin-top:20px}
</style>
</head>
<body>
<header><div class="nav"><strong>Forex Academy</strong><a href="index.html">Home</a></div></header>
<main><article class="lesson">
<h1>What Is Forex?</h1>
<p>Forex, short for foreign exchange, is the global market where one currency is exchanged for another.</p>
<h2>How does forex work?</h2>
<p>Forex is traded in currency pairs. A pair compares the value of one currency against another.</p>
<h2>Example: EUR/USD</h2>
<div class="example"><p>EUR/USD compares the euro with the US dollar.</p><p>If EUR/USD is 1.1000, the quoted exchange rate means 1 euro corresponds to 1.1000 US dollars.</p></div>
<h2>Why do currencies move?</h2>
<p>Currency prices can change because of interest rates, economic data, inflation, political developments, market expectations and supply and demand.</p>
<h2>Currency pairs</h2>
<p>The first currency is the <strong>base currency</strong>; the second is the <strong>quote currency</strong>.</p>
<div class="example"><strong>GBP/USD</strong><br>GBP = base currency<br>USD = quote currency</div>
<h2>Important beginner lesson</h2>
<p>Forex is not a guaranteed way to make money. A trader can lose some or all of the money placed at risk. Risk management is therefore just as important as chart analysis.</p>
<div class="warning"><strong>Risk warning:</strong> This website is educational information only and does not provide personalized financial advice.</div>
<a class="back" href="index.html">← Back to Lessons</a>
</article></main>
</body>
</html>
'''

lesson_template = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE} | Forex Academy</title>
<style>
body{{margin:0;font-family:Arial;background:#f4f6f8;color:#17202a;line-height:1.7}}
header{{background:#101820;color:white;padding:18px}}.nav,main{{max-width:900px;margin:auto}}
.nav{{display:flex;justify-content:space-between}}.nav a{{color:white}}
main{{padding:30px 18px}}article{{background:white;padding:30px;border-radius:12px}}
.box{{background:#eef2f5;padding:18px;border-radius:8px;margin:15px 0}}
.warning{{background:#fff3cd;padding:18px;border-radius:8px}}
.back{{display:inline-block;background:#172a3a;color:white;padding:11px 16px;border-radius:7px;text-decoration:none;margin-top:20px}}
</style></head>
<body><header><div class="nav"><strong>Forex Academy</strong><a href="index.html">Home</a></div></header>
<main><article>
<h1>{TITLE}</h1>
{CONTENT}
<div class="warning"><strong>Educational note:</strong> Examples are for learning. A setup can fail, and no indicator or strategy guarantees profit.</div>
<a class="back" href="index.html">← Back to Lessons</a>
</article></main></body></html>
'''

files["lesson-pairs.html"] = lesson_template.format(
TITLE="Currency Pairs",
CONTENT="""
<p>A currency pair shows the value of one currency relative to another.</p>
<h2>Major pairs</h2><p>Major pairs commonly include the US dollar and are among the most actively traded forex pairs.</p>
<h2>Base and quote currency</h2><div class="box"><strong>EUR/USD = 1.1000</strong><br>EUR is the base currency and USD is the quote currency.</div>
<h2>Pips</h2><p>A pip is a commonly used unit for describing small changes in a forex quote. The exact convention depends on the pair and broker.</p>
<h2>Spread</h2><p>The spread is the difference between the bid and ask price. Trading costs matter when evaluating a strategy.</p>
""")

files["lesson-candles.html"] = lesson_template.format(
TITLE="Candlesticks",
CONTENT="""
<p>A candlestick summarizes price movement during a chosen timeframe.</p>
<div class="box"><strong>Open</strong> — price at the beginning of the period.<br><strong>High</strong> — highest price reached.<br><strong>Low</strong> — lowest price reached.<br><strong>Close</strong> — price at the end.</div>
<h2>Body and wicks</h2><p>The candle body shows the relationship between open and close. Wicks show prices reached beyond the body.</p>
<h2>Don't trade a candle alone</h2><p>A candle pattern has more meaning when considered with market structure, location, timeframe and risk.</p>
""")

files["lesson-structure.html"] = lesson_template.format(
TITLE="Market Structure",
CONTENT="""
<p>Market structure is the organization of price highs and lows.</p>
<div class="box"><strong>Uptrend:</strong> higher highs and higher lows.<br><strong>Downtrend:</strong> lower highs and lower lows.<br><strong>Range:</strong> price repeatedly moves between areas without a sustained directional trend.</div>
<h2>Multi-timeframe analysis</h2><p>A trader may use a higher timeframe for broader context and a lower timeframe for detailed analysis. The exact combination should be part of the strategy rules.</p>
<h2>Structure breaks</h2><p>A break of a previous high or low can provide information about changing market conditions, but a break is not automatically a valid entry.</p>
""")

files["lesson-levels.html"] = lesson_template.format(
TITLE="Support & Resistance",
CONTENT="""
<p>Support and resistance describe areas where price has previously reacted.</p>
<h2>Finding support</h2><p>Look for previous areas where selling pressure was followed by upward movement or repeated buying interest.</p>
<h2>Finding resistance</h2><p>Look for previous areas where buying pressure was followed by downward movement or repeated selling interest.</p>
<div class="box"><strong>Important:</strong> Treat levels as zones rather than assuming price must reverse at one exact number.</div>
<h2>Retests</h2><p>After a level breaks, traders sometimes watch whether price returns to test the area. A retest can fail, so confirmation and risk control remain important.</p>
""")

files["lesson-entries.html"] = lesson_template.format(
TITLE="Finding Potential Entries",
CONTENT="""
<p>A disciplined entry begins with a reasoned market hypothesis, not a random button press.</p>
<h2>A basic process</h2>
<ol><li>Identify higher-timeframe context.</li><li>Identify structure.</li><li>Mark support and resistance.</li><li>Wait for price to reach an area of interest.</li><li>Define confirmation rules.</li><li>Define invalidation and stop-loss.</li><li>Calculate position size.</li><li>Only then consider the entry.</li></ol>
<div class="box"><strong>Example:</strong> A trader might study a bullish market, wait for a pullback toward support, require a predefined confirmation condition, then place a stop at a logical invalidation point. This is an example framework—not a guaranteed signal.</div>
""")

files["lesson-risk.html"] = lesson_template.format(
TITLE="Risk Management",
CONTENT="""
<p>Risk management is one of the most important parts of trading.</p>
<h2>Risk per trade</h2><p>Many traders choose a small, predefined fraction of account equity as their maximum planned loss. The appropriate amount depends on the individual and strategy.</p>
<div class="box"><strong>Basic calculation:</strong><br>Risk amount = Account balance × Risk percentage.</div>
<h2>Stop-loss</h2><p>A stop-loss can define where a trade idea is considered invalid. It does not guarantee the exact exit price in every market condition.</p>
<h2>Risk/reward</h2><p>Compare planned potential reward with planned risk before entering. A high reward-to-risk ratio does not make a losing strategy profitable by itself.</p>
<h2>Never risk essential money</h2><p>Money needed for school fees, rent, food, bills or emergencies should not be treated as trading capital.</p>
""")

files["lesson-psychology.html"] = lesson_template.format(
TITLE="Trading Psychology",
CONTENT="""
<p>Trading involves uncertainty, and emotions can strongly influence decisions.</p>
<h2>FOMO</h2><p>Fear of missing out can cause traders to enter after a move has already happened.</p>
<h2>Revenge trading</h2><p>Trying to immediately recover a loss can lead to excessive risk and impulsive decisions.</p>
<h2>Overtrading</h2><p>More trades do not automatically mean more opportunity. A written strategy can define when not to trade.</p>
<h2>Discipline</h2><p>The goal is to follow your process consistently rather than trying to predict every market move.</p>
""")

files["lesson-fundamentals.html"] = lesson_template.format(
TITLE="Fundamental Analysis",
CONTENT="""
<p>Fundamental analysis studies economic and financial factors that can influence currencies.</p>
<h2>Important factors</h2>
<ul><li>Central-bank interest-rate decisions</li><li>Inflation</li><li>Employment data</li><li>Economic growth</li><li>Government and geopolitical developments</li><li>Market expectations</li></ul>
<h2>News risk</h2><p>Major economic releases can cause rapid price movements and wider trading costs. A strategy should define how it handles important news.</p>
<div class="box"><strong>Beginner rule:</strong> Know what major events are scheduled before trading a currency pair.</div>
""")

files["training.html"] = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Training Zone | Forex Academy</title>
<style>
body{margin:0;font-family:Arial;background:#f4f6f8;color:#17202a}
header{background:#101820;color:white;padding:18px}.nav{max-width:1100px;margin:auto;display:flex;justify-content:space-between}.nav a{color:white}
main{max-width:1100px;margin:auto;padding:25px 15px}.hero,.panel{background:white;padding:25px;border-radius:12px;margin-bottom:22px;box-shadow:0 3px 15px rgba(0,0,0,.07)}
.hero{background:#172a3a;color:white}.hero p{color:#dce5eb}
.chart{background:white;border-radius:12px;overflow:hidden;box-shadow:0 3px 15px rgba(0,0,0,.1)}
iframe{width:100%;height:600px;border:0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:15px}.box{padding:18px;background:#f1f4f6;border-radius:8px}
.ad{min-height:90px;background:#eef1f4;border:1px dashed #adb5bd;display:flex;align-items:center;justify-content:center;color:#777;margin:22px 0;border-radius:8px}
.warning{background:#fff3cd;padding:18px;border-radius:8px}
</style></head>
<body>
<header><div class="nav"><strong>Forex Academy</strong><a href="index.html">← Home</a></div></header>
<main>
<section class="hero"><h1>📊 Training Zone</h1><p>Study a live market chart and apply the analysis process you learned in the lessons.</p></section>
<div class="chart"><iframe src="https://www.tradingview.com/widgetembed/?frameElementId=tradingview_chart&symbol=FX%3AEURUSD&interval=60&hidesidetoolbar=0&hidetoptoolbar=0&symboledit=1&saveimage=0&toolbarbg=f1f3f6&studies=%5B%5D&theme=light&style=1&timezone=Etc%2FUTC" allowtransparency="true" scrolling="no"></iframe></div>
<div class="ad">Advertisement</div>
<section class="panel"><h2>🔎 Analysis Process</h2><div class="grid">
<div class="box"><h3>1. Context</h3><p>Start with the broader timeframe and determine whether the market is trending or ranging.</p></div>
<div class="box"><h3>2. Structure</h3><p>Mark important highs and lows. Look for higher highs/lows or lower highs/lows.</p></div>
<div class="box"><h3>3. Levels</h3><p>Identify important support and resistance zones.</p></div>
<div class="box"><h3>4. Setup</h3><p>Wait for your predefined conditions rather than entering because price simply moved.</p></div>
<div class="box"><h3>5. Risk</h3><p>Determine invalidation, stop-loss, position size and potential reward before entry.</p></div>
<div class="box"><h3>6. Execute</h3><p>Only act when every condition in your strategy is satisfied.</p></div>
</div></section>
<section class="panel"><h2>🎯 Example BUY Framework</h2><ol><li>Market context is bullish.</li><li>Price approaches a previously identified support zone.</li><li>Your confirmation condition occurs.</li><li>Entry is defined.</li><li>Stop-loss is placed at a logical invalidation point.</li><li>Target is defined before entry.</li><li>Risk is within the strategy's limit.</li></ol></section>
<section class="panel"><h2>🎯 Example SELL Framework</h2><ol><li>Market context is bearish.</li><li>Price approaches resistance.</li><li>Your confirmation condition occurs.</li><li>Entry is defined.</li><li>Stop-loss is placed at logical invalidation.</li><li>Target is defined.</li><li>Risk remains within the strategy limit.</li></ol></section>
<section class="panel"><h2>🧠 What Not To Do</h2><div class="grid"><div class="box">❌ Don't chase a move.</div><div class="box">❌ Don't increase risk to recover losses.</div><div class="box">❌ Don't trade without a stop/invalidation plan.</div><div class="box">❌ Don't treat indicators as guaranteed predictions.</div></div></section>
<div class="warning"><strong>Educational only:</strong> The examples are frameworks for learning, not guaranteed trading signals or personalized financial advice.</div>
</main>
</body></html>
'''

files["practice.html"] = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Practice Lab | Forex Academy</title>
<style>
body{margin:0;font-family:Arial;background:#f4f6f8;color:#17202a}
header{background:#101820;color:white;padding:18px}.nav{max-width:1100px;margin:auto;display:flex;justify-content:space-between}.nav a{color:white}
main{max-width:1100px;margin:auto;padding:25px 15px}.hero,.panel{background:white;padding:25px;border-radius:12px;margin-bottom:20px}
.hero{background:#172a3a;color:white}
canvas{width:100%;height:520px;background:#111820;border-radius:10px;cursor:crosshair}
button{padding:11px 14px;margin:5px;border:0;border-radius:7px;background:#172a3a;color:white;font-weight:bold}
button.active{outline:3px solid #ffd43b}.clear{background:#c92a2a}
.result{padding:15px;background:#eef2f5;border-radius:8px;margin-top:15px}
</style></head>
<body>
<header><div class="nav"><strong>Forex Academy</strong><a href="index.html">← Home</a></div></header>
<main>
<section class="hero"><h1>🎯 Practice Lab</h1><p>Practice marking important areas on a simulated market chart.</p></section>
<section class="panel">
<canvas id="chart"></canvas>
<div>
<button onclick="tool='support';active(this)">🟦 Support</button>
<button onclick="tool='resistance';active(this)">🟥 Resistance</button>
<button onclick="tool='entry';active(this)">🟢 Entry</button>
<button onclick="tool='stop';active(this)">🛑 Stop Loss</button>
<button onclick="tool='target';active(this)">🎯 Take Profit</button>
<button class="clear" onclick="reset()">Clear</button>
</div>
<div id="result" class="result">Choose a tool and click the chart.</div>
</section>
<section class="panel">
<h2>How to practice</h2>
<ol><li>Identify the general direction.</li><li>Find important reaction zones.</li><li>Mark support and resistance.</li><li>Choose a hypothetical entry only after your conditions are met.</li><li>Mark invalidation/stop and target.</li><li>Explain your reasoning in your journal.</li></ol>
</section>
</main>
<script>
const c=document.getElementById("chart"),x=c.getContext("2d");let tool=null,marks=[];
function size(){c.width=c.clientWidth*devicePixelRatio;c.height=c.clientHeight*devicePixelRatio;x.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);draw()}
let p=[],v=100;for(let i=0;i<100;i++){v+=(Math.random()-.47)*2.2;p.push(v)}
function draw(){
let w=c.clientWidth,h=c.clientHeight;x.clearRect(0,0,w,h);
let min=Math.min(...p)-2,max=Math.max(...p)+2;
x.strokeStyle="#2c3942";x.lineWidth=1;
for(let i=1;i<6;i++){let y=h*i/6;x.beginPath();x.moveTo(0,y);x.lineTo(w,y);x.stroke()}
let cw=w/p.length;
for(let i=0;i<p.length;i++){
let open=i?p[i-1]:p[i],close=p[i],high=Math.max(open,close)+Math.random(),low=Math.min(open,close)-Math.random();
let yo=h-(open-min)/(max-min)*h,yc=h-(close-min)/(max-min)*h,yh=h-(high-min)/(max-min)*h,yl=h-(low-min)/(max-min)*h;
x.strokeStyle=close>=open?"#4dabf7":"#ff8787";x.fillStyle=x.strokeStyle;
x.beginPath();x.moveTo(i*cw+cw/2,yh);x.lineTo(i*cw+cw/2,yl);x.stroke();
let top=Math.min(yo,yc),bh=Math.max(2,Math.abs(yc-yo));x.fillRect(i*cw+2,top,cw-4,bh)
}
marks.forEach(m=>{x.strokeStyle=m.color;x.lineWidth=3;x.beginPath();x.moveTo(0,m.y);x.lineTo(w,m.y);x.stroke();x.fillStyle=m.color;x.font="bold 13px Arial";x.fillText(m.label,10,m.y-8)})
}
function active(b){document.querySelectorAll("button").forEach(q=>q.classList.remove("active"));b.classList.add("active");document.getElementById("result").textContent="Click the chart to place "+tool+"."}
c.onclick=e=>{if(!tool)return;let r=c.getBoundingClientRect(),y=e.clientY-r.top,info={support:["SUPPORT","#4dabf7"],resistance:["RESISTANCE","#ff8787"],entry:["ENTRY","#51cf66"],stop:["STOP LOSS","#ff6b6b"],target:["TAKE PROFIT","#ffd43b"]}[tool];marks.push({y,label:info[0],color:info[1]});draw();document.getElementById("result").textContent=info[0]+" marked. Now consider why this location matters."}
function reset(){marks=[];tool=null;document.querySelectorAll("button").forEach(q=>q.classList.remove("active"));document.getElementById("result").textContent="Choose a tool and click the chart.";draw()}
addEventListener("resize",size);size();
</script>
</body></html>
'''

files["strategy.html"] = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Strategy Builder | Forex Academy</title>
<style>
body{margin:0;font-family:Arial;background:#f4f6f8;color:#17202a}header{background:#101820;color:white;padding:18px}.nav,main{max-width:900px;margin:auto}.nav{display:flex;justify-content:space-between}.nav a{color:white}main{padding:30px 18px}.panel{background:white;padding:25px;border-radius:12px;margin-bottom:20px}label{display:block;font-weight:bold;margin-top:15px}input,textarea,select{width:100%;padding:12px;margin-top:7px;border:1px solid #ccc;border-radius:7px}button{margin-top:20px;padding:13px 18px;background:#087f5b;color:white;border:0;border-radius:7px;font-weight:bold}.output{margin-top:20px;background:#eef2f5;padding:20px;border-radius:8px;white-space:pre-wrap}
</style></head>
<body>
<header><div class="nav"><strong>Forex Academy</strong><a href="index.html">Home</a></div></header>
<main>
<div class="panel">
<h1>🧩 Strategy Builder</h1>
<p>A strategy should contain objective rules that can be tested. Avoid rules such as “buy when the chart looks good.”</p>
<label>Strategy name</label><input id="name" placeholder="Example: London Pullback">
<label>Market/pairs</label><input id="market" placeholder="Example: EUR/USD">
<label>Timeframe</label><select id="tf"><option>15 minutes</option><option>1 hour</option><option>4 hours</option><option>Daily</option></select>
<label>Trend condition</label><textarea id="trend" placeholder="What must the market structure look like?"></textarea>
<label>Entry condition</label><textarea id="entry" placeholder="What exact conditions must happen before entry?"></textarea>
<label>Stop-loss rule</label><textarea id="stop" placeholder="Where is the trade invalidated?"></textarea>
<label>Take-profit rule</label><textarea id="tp" placeholder="How is the target determined?"></textarea>
<label>Risk rule</label><textarea id="risk" placeholder="Maximum planned risk per trade?"></textarea>
<label>No-trade conditions</label><textarea id="avoid" placeholder="When will you refuse to trade?"></textarea>
<button onclick="build()">Create Strategy</button>
<div id="output" class="output" style="display:none"></div>
</div>
<div class="panel"><h2>Test before trusting it</h2><p>A strategy should be tested on historical data or in a demo environment before risking real money. Track enough trades to understand its behavior rather than judging it from a handful of wins or losses.</p></div>
</main>
<script>
function build(){
let g=id=>document.getElementById(id).value.trim();
let out=`STRATEGY: ${g("name")||"Untitled"}\n\nMARKET: ${g("market")}\nTIMEFRAME: ${g("tf")}\n\nTREND:\n${g("trend")}\n\nENTRY:\n${g("entry")}\n\nSTOP LOSS:\n${g("stop")}\n\nTAKE PROFIT:\n${g("tp")}\n\nRISK:\n${g("risk")}\n\nNO-TRADE CONDITIONS:\n${g("avoid")}`;
let o=document.getElementById("output");o.style.display="block";o.textContent=out;
localStorage.setItem("forexStrategy",out)
}
</script>
</body></html>
'''

files["journal.html"] = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trading Journal | Forex Academy</title>
<style>
body{margin:0;font-family:Arial;background:#f4f6f8;color:#17202a}header{background:#101820;color:white;padding:18px}.nav,main{max-width:900px;margin:auto}.nav{display:flex;justify-content:space-between}.nav a{color:white}main{padding:30px 18px}.panel{background:white;padding:25px;border-radius:12px}label{display:block;font-weight:bold;margin-top:14px}input,textarea,select{width:100%;padding:12px;margin-top:7px;border:1px solid #ccc;border-radius:7px}button{margin-top:18px;padding:12px 18px;background:#172a3a;color:white;border:0;border-radius:7px;font-weight:bold}.trade{background:#eef2f5;padding:15px;border-radius:8px;margin-top:12px}.danger{background:#c92a2a}
</style></head>
<body>
<header><div class="nav"><strong>Forex Academy</strong><a href="index.html">Home</a></div></header>
<main>
<div class="panel">
<h1>📒 Trading Journal</h1>
<p>Record practice trades and, most importantly, record why you made the decision.</p>
<label>Pair</label><input id="pair" placeholder="EUR/USD">
<label>Direction</label><select id="direction"><option>BUY</option><option>SELL</option></select>
<label>Entry</label><input id="entry" placeholder="Entry price">
<label>Stop Loss</label><input id="stop" placeholder="Stop price">
<label>Target</label><input id="target" placeholder="Target price">
<label>Reason for trade</label><textarea id="reason" placeholder="What conditions did you identify?"></textarea>
<label>Lesson learned</label><textarea id="lesson" placeholder="What did you learn?"></textarea>
<button onclick="save()">Save Practice Trade</button>
<button class="danger" onclick="clearAll()">Clear Journal</button>
<div id="list"></div>
</div>
</main>
<script>
let trades=JSON.parse(localStorage.getItem("forexJournal")||"[]");
function save(){let g=id=>document.getElementById(id).value.trim();trades.unshift({pair:g("pair"),direction:g("direction"),entry:g("entry"),stop:g("stop"),target:g("target"),reason:g("reason"),lesson:g("lesson"),date:new Date().toLocaleString()});localStorage.setItem("forexJournal",JSON.stringify(trades));render()}
function render(){document.getElementById("list").innerHTML=trades.length?trades.map((t,i)=>`<div class="trade"><strong>${t.direction} ${t.pair}</strong><br>Entry: ${t.entry} | SL: ${t.stop} | TP: ${t.target}<br><small>${t.date}</small><p><strong>Reason:</strong> ${t.reason}</p><p><strong>Lesson:</strong> ${t.lesson}</p></div>`).join(""):"<p>No journal entries yet.</p>"}
function clearAll(){if(confirm("Clear the practice journal?")){trades=[];localStorage.removeItem("forexJournal");render()}}
render()
</script>
</body></html>
'''

# Create files
for name, content in files.items():
    Path(name).write_text(content, encoding="utf-8")

print("Forex Academy Pro created successfully.")
print("Files created:")
for name in files:
    print(" -", name)
print("\nOpen the site with:")
print("termux-open index.html")
