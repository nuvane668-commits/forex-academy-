const lessons = [
  { id: "forex", name: "What Is Forex?" },
  { id: "pairs", name: "Currency Pairs" },
  { id: "candles", name: "Candlesticks" },
  { id: "structure", name: "Market Structure" },
  { id: "levels", name: "Support & Resistance" },
  { id: "entries", name: "Finding Setups" },
  { id: "risk", name: "Risk Management" },
  { id: "psychology", name: "Trading Psychology" },
  { id: "fundamentals", name: "Economic News" },
  { id: "strategy", name: "Build Your Strategy" }
];

function getCompletedLessons() {
  return JSON.parse(localStorage.getItem("forexAcademyProgress") || "[]");
}

function completeLesson(id) {
  const completed = getCompletedLessons();

  if (!completed.includes(id)) {
    completed.push(id);
    localStorage.setItem(
      "forexAcademyProgress",
      JSON.stringify(completed)
    );
  }

  updateProgress();
}

function updateProgress() {
  const completed = getCompletedLessons();
  const percentage = Math.round(
    (completed.length / lessons.length) * 100
  );

  const percentageElement = document.getElementById("progressPercentage");
  const bar = document.getElementById("progressBar");

  if (percentageElement) {
    percentageElement.textContent = percentage + "%";
  }

  if (bar) {
    bar.style.width = percentage + "%";
  }
}

document.addEventListener("DOMContentLoaded", updateProgress);
