var sentence = "The dinner is not that bad! You cook well.";

let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
console.log(wordNot); //14
console.log(wordBad); //23

if (wordNot < wordBad) {
  console.log("The dinner is good! You cook well.");
} else {
  console.log("The dinner is not that bad! You cook well.");
}
