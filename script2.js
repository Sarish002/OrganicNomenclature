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

    // remove show to reset animation
    imgs.classList.remove("show");
    name.classList.remove("show");

    // placeholder image
    imgs.src = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==";

    // pick new molecule
    let ind = Math.floor(Math.random() * mols.length);
    let imgpath = mols[ind];

    name.textContent = imgpath.replace(".png", "");
    label = "Images/" + imgpath;

    // trigger text animation after small delay
    setTimeout(() => {
        name.classList.add("show");
    }, 100);
}

function answer() {
    // reset animations
    name.classList.remove("show");
    imgs.classList.remove("show");

    // force reflow
    void name.offsetWidth;
    void imgs.offsetWidth;

    // set real image
    imgs.src = label;

    // trigger animations
    name.classList.add("show");
    imgs.classList.add("show");
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