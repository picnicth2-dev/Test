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

<title>Valentine Surprise 🌹</title>

<style>
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}

body {
    background: repeating-radial-gradient(
        circle at center,
        #7a0000 0px,
        #8b0000 40px,
        #a00000 80px
    );
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #fff;
}

/* หน้ากดเปิด */
#cover {
    cursor: pointer;
    font-size: 4rem;
    animation: shake 1.5s infinite;
}

@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(2deg); }
    50% { transform: rotate(-2deg); }
    75% { transform: rotate(2deg); }
    100% { transform: rotate(0deg); }
}

/* ดอกไม้แตก */
.rose {
    position: absolute;
    font-size: 2rem;
    animation: burst 1.5s ease-out forwards;
}

@keyframes burst {
    from {
        transform: translate(0,0) scale(1);
        opacity: 1;
    }
    to {
        transform: translate(var(--x), var(--y)) scale(0.5);
        opacity: 0;
    }
}

/* กล่องข้อความ */
#letter {
    display: none;
    border: 3px solid #ffd6e8;
    padding: 30px;
    max-width: 85%;
    color: #ffd6e8;
}

#text {
    font-size: 1.3rem;
    line-height: 1.7;
    white-space: pre-line;
}

/* เครดิต */
#credit {
    margin-top: 20px;
    font-size: 0.9rem;
    opacity: 0.7;
}
</style>
</head>

<body>

<div id="cover">🌹</div>

<div id="letter">
    <div id="text"></div>
    <div id="credit">Created by Kitthiphan Janthilar</div>
</div>

<script>
const message = [
    "สวัสดีตอนเช้านะค้าบที่รัก 💕",
    "",
    "วันนี้วันวาเลนไทน์นะ",
    "ไม่รู้ว่าของขวัญชิ้นนี้จะถูกใจไหม",
    "",
    "แต่อยากให้รู้ว่า",
    "เค้ารักเธอมากจริงๆ 🌹💖"
];

let line = 0;
let char = 0;
const speed = 50;
const textDiv = document.getElementById("text");

function typeWriter() {
    if (line < message.length) {
        if (char < message[line].length) {
            textDiv.innerHTML += message[line].charAt(char);
            char++;
            setTimeout(typeWriter, speed);
        } else {
            textDiv.innerHTML += "\\n";
            line++;
            char = 0;
            setTimeout(typeWriter, 400);
        }
    }
}

document.getElementById("cover").addEventListener("click", () => {
    // สร้างดอกไม้แตก
    for (let i = 0; i < 25; i++) {
        const rose = document.createElement("div");
        rose.className = "rose";
        rose.innerText = "🌹";
        rose.style.left = "50%";
        rose.style.top = "50%";
        rose.style.setProperty("--x", (Math.random()*400 - 200) + "px");
        rose.style.setProperty("--y", (Math.random()*400 - 200) + "px");
        document.body.appendChild(rose);

        setTimeout(() => rose.remove(), 1500);
    }

    document.getElementById("cover").style.display = "none";
    document.getElementById("letter").style.display = "block";
    typeWriter();
});
</script>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)