const arrayContainer = document.getElementById("array-container");
const generateArrayButton = document.getElementById("generate-array");
const bubbleSortButton = document.getElementById("bubble-sort");

let array = [];

// Generate a random array
function generateArray() {
  array = [];
  arrayContainer.innerHTML = "";
  for (let i = 0; i < 50; i++) {
    const value = Math.floor(Math.random() * 300) + 10;
    array.push(value);
    const bar = document.createElement("div");
    bar.classList.add("bar");
    bar.style.height = `${value}px`;
    bar.style.width = "15px";
    arrayContainer.appendChild(bar);
  }
}

// Bubble Sort Algorithm
async function bubbleSort() {
  const bars = document.getElementsByClassName("bar");
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = 0; j < array.length - i - 1; j++) {
      bars[j].style.backgroundColor = "red";
      bars[j + 1].style.backgroundColor = "red";
      
      if (array[j] > array[j + 1]) {
        // Swap values
        [array[j], array[j + 1]] = [array[j + 1], array[j]];
        // Swap heights
        bars[j].style.height = `${array[j]}px`;
        bars[j + 1].style.height = `${array[j + 1]}px`;
      }
      
      await new Promise(resolve => setTimeout(resolve, 50)); // Delay
      bars[j].style.backgroundColor = "#4caf50";
      bars[j + 1].style.backgroundColor = "#4caf50";
    }
  }
}

// Event Listeners
generateArrayButton.addEventListener("click", generateArray);
bubbleSortButton.addEventListener("click", bubbleSort);

// Generate initial array
generateArray();
