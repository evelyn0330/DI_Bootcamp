let gameRound = 0;
function playTheGame() {
  if (confirm("Would you like to play a game?")) {
    let num = parseInt(prompt("Give me a number between 0 and 10"));
    if (isNaN(num)) {
      alert("Sorry Not a number, Goodbye.");
    } else if (num > 10) {
      alert("Sorry, it's not a good number, Goodbye.");
    } else {
      computerNumber = Math.floor(Math.random() * 11);
      test(num, computerNumber);
    }
  } else {
    alert("No problem. Goodbye.");
  }
}

function test(num, computerNumber) {
  gameRound++;
  if (gameRound > 3) {
    return alert("Sorry, you're out of Chances!");
  }

  if (num === computerNumber) {
    return alert("Winner!!");
  }

  if (num > computerNumber) {
    alert("Your number is bigger than the computer's, guess again.");
    return test(parseInt(prompt("Give me a new number.")), computerNumber);
  } else if (num < computerNumber) {
    alert("Your number is smaller than the computer's, guess again.");
    return test(parseInt(prompt("New Guess!")), computerNumber);
  }
}
