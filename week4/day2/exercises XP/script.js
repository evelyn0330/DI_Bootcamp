// // Exercise 1 : Information
// // Part I
// function infoAboutMe() {
//   console.log("My name is Evelyn, I'm 28 years old and my hobbie is reading.");
// }
// infoAboutMe();

// // Part II
// function infoAboutPerson(personName, personAge, PersonFavoriteColor) {
//   console.log(
//     "Your name is " +
//       personName +
//       " your age is " +
//       personAge +
//       " your favorite color is " +
//       PersonFavoriteColor
//   );
// }
// infoAboutPerson("David", 45, "blue");
// infoAboutPerson("Josh", 12, "yellow");

// Part III
// function infoAboutPerson(
//   personName,
//   personAge,
//   PersonFavoriteColor,
//   personHobbies
// ) {
//   console.log(
//     "Your name is " +
//       personName +
//       " your age is " +
//       personAge +
//       " your favorite color is " +
//       PersonFavoriteColor +
//       " your hobbies are"
//   );
//   for (let i = 0; i < personHobbies.length; i++) {
//     console.log(personHobbies[i]);
//   }
// }
// infoAboutPerson("David", 45, "blue", ["tennis", "painting"]);
// infoAboutPerson("Josh", 12, "yellow", [
//   "video games",
//   "hanging out with friends",
//   "playing cards",
// ]);
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 2: Keyless Car

// function checkDriverAge(age) {
//   if (age < 18) {
//     console.log("Sorry, you are too young to drive. Powering off.");
//   } else if (age == 18) {
//     console.log(
//       "Congratulations on your first year of driving! Enjoy the ride!"
//     );
//   } else if (age > 18) {
//     console.log("Enjoy the ride. Powering on.");
//   }
// }
// checkDriverAge(16); //Sorry, you are too young to drive. Powering off.
// checkDriverAge(18); //Congratulations on your first year of driving! Enjoy the ride!
// checkDriverAge(21); //Enjoy the ride. Powering on.
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 3: Odd or Even
// function checkNumber() {
//   for (let i = 0; i <= 100; i++)
//     if (i % 2 === 0) {
//       console.log("Your number " + i + " is even.");
//     } else {
//       console.log("Your number " + i + " is odd.");
//     }
// }
// checkNumber();
//-----------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 4: Tips
// let bill = parseInt(prompt("Hi John, please give your bill amount!"));

// function calcTips(num) {
//   if (num < 50) {
//     return num * 0.2;
//   } else if (num >= 50 && num <= 200) {
//     return num * 0.15;
//   } else if (num > 200) {
//     return num * 0.1;
//   }
// }

// prompt(
//   `Your tip is ${calcTips(bill)} and your total amount is ${
//     bill + calcTips(bill)
//   }`
// );
//------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 5: Find the Numbers Divisible by 23
// function isDivisible() {
//   let sum = 0;
//   for (let i = 0; i <= 500; i++)
//     if (i % 23 === 0) {
//       console.log(i);
//       sum += i;
//     } else {
//     }
//   console.log(sum);
// }
// isDivisible();
// Bonus;
// function isDivisible(divisor) {
//   let sum = 0;
//   for (let i = 0; i <= 500; i++)
//     if (i % divisor === 0) {
//       console.log(i);
//       sum += i;
//     } else {
//     }
//   console.log(sum);
// }
// isDivisible(45);
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 6: Amazon Shopping
// let amazonBasket = {
//   glasses: 1,
//   books: 2,
//   floss: 100,
// };

// function checkBasket(obj) {
//   let key = prompt("Give me the name of an item!");

//   if (key in obj) {
//     console.log(`Your item ${key} is in the basket`);
//   } else {
//     console.log(`Nope! your item ${key} is not in the basket!`);
//   }
// }

// checkBasket(amazonBasket);

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 7: Shopping List

// let stock = {
//   banana: 6,
//   apple: 0,
//   pear: 12,
//   orange: 32,
//   blueberry: 1,
// };

// let prices = {
//   banana: 4,
//   apple: 2,
//   pear: 1,
//   orange: 1.5,
//   blueberry: 10,
// };

// let shoppingList = ["banana", "orange", "apple"];
// let receipt = 0;

// function myBill() {
//   for (i = 0; i <= shoppingList.length; i++) {
//     produce = shoppingList[i];
//     if (produce in stock == true && stock[produce] > 0) {
//       receipt += prices[produce];
//       stock[produce] -= 1;
//     } else {
//       continue;
//     }
//   }
//   alert(`"Your receipt amount is ${receipt}`);
// }

// myBill();

//------------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 8: What's in my Wallet?

// function changeEnough(price, array) {
//   let quarter = array[0] * 0.25;
//   let dime = array[1] * 0.1;
//   let nickel = array[2] * 0.05;
//   let penny = array[3] * 0.01;
//   if (price <= quarter + dime + nickel + penny) {
//     return true;
//   } else return false;
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0])); //true
// console.log(changeEnough(14.11, [2, 100, 0, 0])); //false
// console.log(changeEnough(0.75, [0, 0, 20, 5])); //true
//----------------------------------------------------------------------------------------------------------------------------------------------------------------------
//Exercise 9: Vacation Costs
// function hotelCost(numberNights){
// numberNights = parseInt(numberNights);
// let hotelCost = 140;
// if (isNaN(numberNights)) {
//   return hotelCost();
// } else {
//   return (hotelCost *= numberNights);
// }
// function planeRideCost(dest) {
//   dest = dest.toLowerCase();
//   switch (dest) {
//     case "london":
//       planeCost = 183;
//       break;
//     case "paris":
//       planeCost = 220;
//       break;
//     case "":
//       planeCost = false;
//       break;

//     default:
//       planeCost = 300;
//       break;
//   }
//   return planeCost;
// }
