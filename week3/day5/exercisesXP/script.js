// Exercise 1 : Your Favorite Colors

let colors = ["blue", "black", "purple", "white", "pink"];

for (let i = 0; i < colors.length; i++) {
  console.log("My #" + (i + 1) + " choice is " + colors[i]);
}

// Exercise 2 : List Of People

// let people = ["Greg", "Mary", "Devon", "James"];
// people.shift();
// console.log(people); //['Mary', 'Devon', 'James']
// people.splice(2, 1, "Jason");
// console.log(people); // ['Mary', 'Devon', 'Jason']
// people.push("Evelyn");
// console.log(people); // ['Mary', 'Devon', 'Jason', 'Evelyn']

// for (let i of people) {
//   console.log(i);
// }

// for (let i = 0; i < people.length; i++) {
//   console.log(people[i]);
//   if (i == 2) break;
// }

// console.log(people.slice(1, 3)); // ['Devon', 'Jason']
// console.log(people.indexOf("Mary")); //0
// console.log(people.indexOf("Foo")); // It returns -1 because "Foo" doesn't exits in the array.
// let last = people[people.length - 1];
// console.log(last);

// Exercise 3 : Repeat The Question

// let num;

// do {
//   num = parseInt(prompt("Give me a number!"));
// } while (num < 10);

// Exercise 4 : Building Management

// let building = {
//   numberOfFloors: 4,
//   numberOfAptByFloor: {
//     firstFloor: 3,
//     secondFloor: 4,
//     thirdFloor: 9,
//     fourthFloor: 2,
//   },
//   nameOfTenants: ["Sarah", "Dan", "David"],
//   numberOfRoomsAndRent: {
//     sarah: [3, 990],
//     dan: [4, 1000],
//     david: [1, 500],
//   },
// };

// console.log(building.numberOfFloors); //4
// console.log(
//   building.numberOfAptByFloor.firstFloor +
//     ", " +
//     building.numberOfAptByFloor.thirdFloor
// ); //3, 9
// console.log(
//   building.nameOfTenants[1] + ", " + building.numberOfRoomsAndRent.dan[0]
// ); // Dan 4
// if (
//   building.numberOfRoomsAndRent.sarah[1] +
//     building.numberOfRoomsAndRent.david[1] >
//   building.numberOfRoomsAndRent.dan[1]
// ) {
//   building.numberOfRoomsAndRent.dan[1] = 1200;
// }
// console.log(building.numberOfRoomsAndRent.dan[1]); //1200

// Exercise 5 : Family

// let family = {
//   name: "Ana",
//   age: 32,
//   children: 3,
// };

// for (let key in family) {
//   console.log(key);
// }

// for (let [key, value] of Object.entries(family)) {
//   console.log(`${value}`);
// }

//Exercise 6

// let details = {
//   my: "name",
//   is: "Rudolf",
//   the: "raindeer",
// };
// for (let [key, value] of Object.entries(details)) {
//   console.log(key, value);
// }

// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// names.sort();

// for (let index = 0; index < names.length; index++) {
//   let element = names[index];
//   if ((element = element.slice(0, 1))) {
//   }
//   console.log(element);
// }
