let imgs = document.getElementById("img");
let mols; let label;
let name = document.getElementById("answer");
let prev = document.getElementById("previous");

fetch("json.json")
    .then(response => response.json())
    .then(data => {
        mols = data;
        console.log(mols);

        change()
    });

function change() {
    if (!mols) return;

    prev.textContent = "Previous: " + name.textContent;

    imgs.classList.remove("show");
    name.classList.remove("show");

    let ind = Math.floor(Math.random() * mols.length);
    let imgpath = mols[ind];

    label = imgpath.replace(".png", "");

    imgs.src = "Images/" + imgpath;

    name.textContent = ""; // ✅ keep empty

    setTimeout(() => {
        imgs.classList.add("show");
    }, 100);
}

function answer() {
    name.classList.remove("show");

    // force reset so animation can replay
    void name.offsetWidth;

    name.textContent = label;

    name.classList.add("show");
}

let musicPlaying = false;
let stopAfterCycle = false;

const musicBtn = document.querySelector('.music-btn');
const audio = document.getElementById('music'); // make sure your audio has id="music"

// Set low volume once
audio.volume = 0.25;

function music() {
    if (!musicPlaying) {
        audio.play();
        musicBtn.classList.add('playing');
        stopAfterCycle = false;
        musicPlaying = true;
    } else {
        audio.pause();
        stopAfterCycle = true; // finish current bounce cycle
        musicPlaying = false;
    }
}

// Finish bounce cycle before stopping
musicBtn.addEventListener('animationiteration', () => {
    if (stopAfterCycle) {
        musicBtn.classList.remove('playing');
        stopAfterCycle = false;
    }
});