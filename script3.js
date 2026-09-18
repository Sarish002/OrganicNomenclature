// List of available chapters and their JSON files
const chapters = [
  { id: "ch1", name: "1. Units and Measurements", file: "Physics Problems/ch1.json" },
  { id: "ch2", name: "2. Motion in a Straight Line", file: "Physics Problems/ch2.json" },
  { id: "ch3", name: "3. Motion in a Plane", file: "Physics Problems/ch3.json" },
  { id: "ch4", name: "4. Laws of Motion", file: "Physics Problems/ch4.json" },
  { id: "ch5", name: "5. Work, Energy and Power", file: "Physics Problems/ch5.json" },
  { id: "ch6", name: "6. System of Particles & Rotational Motion", file: "Physics Problems/ch6.json" },
  { id: "ch7", name: "7. Gravitation", file: "Physics Problems/ch7.json" },
  { id: "ch8", name: "8. Mechanical Properties of Solids", file: "Physics Problems/ch8.json" },
  { id: "ch9", name: "9. Mechanical Properties of Fluids", file: "Physics Problems/ch9.json" },
  { id: "ch10", name: "10. Thermal Properties of Matter", file: "Physics Problems/ch10.json" },
];

let selectedProblems = [];
let currentProblem = null;

// Create checkboxes
const chapterList = document.getElementById("chapterList");

chapters.forEach(ch => {
  const div = document.createElement("div");
  div.className = "chapter-item";
  div.innerHTML = `
    <input type="checkbox" id="${ch.id}" checked>
    <label for="${ch.id}">${ch.name}</label>
  `;
  chapterList.appendChild(div);
});

// Start Quiz
async function startQuiz() {
  selectedProblems = [];

  const checkedChapters = chapters.filter(ch => 
    document.getElementById(ch.id).checked
  );

  if (checkedChapters.length === 0) {
    alert("Please select at least one chapter!");
    return;
  }

  // Load all selected JSON files
  for (const ch of checkedChapters) {
    try {
      const res = await fetch(ch.file);
      const data = await res.json();
      selectedProblems = selectedProblems.concat(data);
    } catch (err) {
      console.error("Failed to load", ch.file);
    }
  }

  if (selectedProblems.length === 0) {
    alert("No problems found in selected chapters.");
    return;
  }

  // Show quiz card
  document.getElementById("quizCard").style.display = "flex";
  nextProblem();
}

// Next random problem
function nextProblem() {
  const randomIndex = Math.floor(Math.random() * selectedProblems.length);
  currentProblem = selectedProblems[randomIndex];

  document.getElementById("chapter").textContent = currentProblem.chapter;
  document.getElementById("problem").textContent = currentProblem.problem;

  document.getElementById("answer").classList.remove("show");

}


function showAnswer() {
  document.getElementById("answer").textContent = "Answer: " + currentProblem.answer;
  document.getElementById("answer").classList.add("show");
}

function toggleMusic() {
  const music = document.getElementById("music");
  const btn = document.getElementById("musicBtn");

  if (music.paused) {
    music.play();
    btn.classList.add("playing");
  } else {
    music.pause();
    btn.classList.remove("playing");
  }
}