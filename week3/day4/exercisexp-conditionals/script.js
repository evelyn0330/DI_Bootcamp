//Exercise 1
let x = 20;
let y = 8;
if (x > y) {
  console.log("X is the biggest number!");
} else {
  console.log("Y is the biggest number!");
}

//Exercise 2
var newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog === "Chihuahua") {
  console.log("I love Chihuahas, it's my favorite dog breed!");
} else {
  console.log("I don't care, I prefer cats.");
}

//Exercise 3
var num = prompt("Give me a number! Any number!");
if (num % 2 == 0) {
  console.log(num + " is an even number");
} else {
  console.log(num + " is an odd number.");
}

//Exercise 4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
var len = users.length; // making a new variable helps return the elements in the array.

if (len == 0) {
  console.log("no one is online.");
} else if (len == 1) {
  console.log(users[0] + " is online");
} else if (len == 2) {
  console.log(users[0] + " and " + users[1] + " are online");
} else {
  console.log(users[0] + " , " + users[1] + " and two more are online.");
}
