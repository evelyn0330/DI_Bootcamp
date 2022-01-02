let libButton = document.getElementById("lib-button");
let libIt = function () {
  let storyDiv = document.getElementById("story");
  let noun = document.getElementById("noun").value;
  let adjective = document.getElementById("adjective").value;
  let name = document.getElementById("person").value;
  let verb = document.getElementById("verb").value;
  let place = document.getElementById("place").value;
  storyDiv.innerHTML = `A ${noun} was found acting ${adjective}. ${name} was not happy about it, so they decided to ${verb} and take it to a ${place}`;
};
libButton.addEventListener("click", libIt);
