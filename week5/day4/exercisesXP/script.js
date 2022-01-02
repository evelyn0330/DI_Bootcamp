let incrementPosition = 0;
const redSquare = document.querySelector("#animate");
let incrementInterval = () => {
  let currentInterval = setInterval(() => {
    redSquare.style.top = `${incrementPosition}px`;
    redSquare.style.left = `${incrementPosition}px`;
    incrementPosition += 50;
    if (incrementPosition == 400) {
      clearInterval(currentInterval);
      incrementPosition = 0;
    }
  }, 400);
};

function myMove() {
  let clickMe = document.querySelector("button");
  clickMe.addEventListener("click", incrementInterval);
}
