from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Happy Valentine 💐</title>

<style>
* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html, body {
    margin: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
}

body {
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;

    background:
      linear-gradient(rgba(120,0,0,0.55), rgba(120,0,0,0.55)),
      url("https://images.unsplash.com/photo-1518895949257-7621c3c786d7");
    background-size: cover;
    background-position: center;
}

/* ---------- หน้าแรก ช่อดอกไม้ ---------- */
#bouquet-screen {
    color: white;
}

#bouquet {
    font-size: 6.5em;
    cursor: pointer;
    animation: shake 1.8s infinite;
}

@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(-3deg); }
    50% { transform: rotate(3deg); }
    75% { transform: rotate(-2deg); }
    100% { transform: rotate(0deg); }
}

#hint {
    margin-top: 14px;
    font-size: 1.2em;
    opacity: 0.9;
}

/* ---------- Loading ---------- */
#loading {
    font-size: 2em;
    color: white;
    animation: pulse 1.2s infinite;
}

@keyframes pulse {
    0% { opacity: 0.3; }
    50% { opacity: 1; }
    100% { opacity: 0.3; }
}

/* ---------- เนื้อหา ---------- */
.hidden { display: none; }

#content {
    color: #7a1025;
}

/* ---------- กรอบจดหมาย ---------- */
.letter-box {
    background:
      repeating-linear-gradient(
        45deg,
        #fff6f0,
        #fff6f0 12px,
        #fde2e4 12px,
        #fde2e4 24px
      );
    border: 4px solid #c9184a;
    border-radius: 22px;
    padding: 26px 22px;
    max-width: 92%;
    width: 600px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.35);
}

#text {
    font-size: 1.25em;
    line-height: 1.8;
    min-height: 220px;
}

/* ---------- ปุ่ม ---------- */
button {
    margin-top: 18px;
    padding: 14px 38px;
    font-size: 1.05em;
    border: none;
    border-radius: 40px;
    background: linear-gradient(135deg, #ff4d6d, #c9184a);
    color: white;
    cursor: pointer;
}

button:active { transform: scale(0.92); }

/* ---------- ป้ายวาเลนไทน์ ---------- */
#banner {
    position: fixed;
    top: 16px;
    background: rgba(255,245,245,0.95);
    color: #c9184a;
    padding: 10px 28px;
    border-radius: 30px;
    font-size: 1.05em;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    animation: slideDown 0.8s ease forwards;
}

@keyframes slideDown {
    from { transform: translateY(-40px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

/* ---------- หัวใจลอย ---------- */
.heart-soft {
    position: absolute;
    font-size: 1.6em;
    opacity: 0.45;
    animation: floatSoft 4s linear forwards;
    pointer-events: none;
}

@keyframes floatSoft {
    from { transform: translateY(0); opacity: 0.45; }
    to { transform: translateY(-180px); opacity: 0; }
}

.credit {
    position: fixed;
    bottom: 8px;
    width: 100%;
    font-size: 0.75em;
    color: rgba(255,255,255,0.7);
}
</style>
</head>

<body>

<!-- หน้าแรก -->
<div id="bouquet-screen">
    <div id="bouquet" onclick="openGift()">💐</div>
    <div id="hint">แตะที่ช่อดอกไม้สิ 🌹</div>
</div>

<!-- Loading -->
<div id="loading" class="hidden">กำลังเปิดของขวัญ… 💕</div>

<!-- เนื้อหา -->
<div id="content" class="hidden">
    <h1 style="color:white;">💘 Happy Valentine 💘</h1>

    <div class="letter-box">
        <div id="text"></div>
    </div>

    <button onclick="loveBack()">บอกรักกลับ 💖</button>
    <div class="credit">Created by Kitthiphan Janthilar</div>
</div>

<!-- เสียง -->
<audio id="typeSound" src="https://assets.mixkit.co/sfx/preview/mixkit-keyboard-typing-1386.mp3"></audio>
<audio id="squishSound" src="https://assets.mixkit.co/sfx/preview/mixkit-squeeze-toy-3034.mp3"></audio>

<script>
function openGift(){
    document.getElementById("bouquet-screen").classList.add("hidden");
    document.getElementById("loading").classList.remove("hidden");

    setTimeout(()=>{
        document.getElementById("loading").classList.add("hidden");
        document.getElementById("content").classList.remove("hidden");
        typeWriter();
    },2500);
}

/* ---------- ข้อความ ---------- */
const message = [
 "สุขสันต์วันวาเลนไทน์นะค้าบที่รัก 💕","",
 "วันนี้เค้าอยากมอบช่อดอกไม้",
 "พร้อมหัวใจดวงนี้ให้เธอ 🌹","",
 "ขอบคุณที่ทำให้ทุกวันของเค้า",
 "เต็มไปด้วยความรักนะ 💖"
];

let line=0,char=0;
const textDiv=document.getElementById("text");
const sound=document.getElementById("typeSound");
sound.volume=0.12;

function typeWriter(){
 if(line<message.length){
  if(char<message[line].length){
   textDiv.innerHTML+=message[line].charAt(char++);
   sound.currentTime=0; sound.play();
   setTimeout(typeWriter,50);
  } else {
   textDiv.innerHTML+="<br>";
   line++; char=0;
   setTimeout(typeWriter,400);
  }
 } else {
   showBanner();
 }
}

/* ---------- ป้าย + หัวใจ ---------- */
function showBanner(){
 if(document.getElementById("banner")) return;

 const b=document.createElement("div");
 b.id="banner";
 b.innerText="สุขสันต์วันวาเลนไทน์นะค้าบที่ร๊ากก 💘🌹";
 document.body.appendChild(b);

 setInterval(()=>{
  const h=document.createElement("div");
  h.className="heart-soft";
  h.innerHTML=["💘","💖","💝","🌹"][Math.floor(Math.random()*4)];
  h.style.left=(40+Math.random()*20)+"%";
  h.style.bottom="60px";
  document.body.appendChild(h);
  setTimeout(()=>h.remove(),4000);
 },900);
}

function loveBack(){
 const s=document.getElementById("squishSound");
 s.volume=0.15; s.currentTime=0; s.play();
 showBanner();
}
</script>

</body>
</html>
"""
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)