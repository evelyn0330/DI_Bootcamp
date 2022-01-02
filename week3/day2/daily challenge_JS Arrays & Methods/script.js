//EXERCISE 1!

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(fruits); // ['Banana', 'Apples', 'Oranges', 'Blueberries']
fruits.shift();
console.log(fruits); // ['Apples', 'Oranges', 'Blueberries']
fruits.sort();
console.log(fruits); // ['Apples', 'Blueberries', 'Oranges']
fruits.push("Kiwi");
console.log(fruits); // ['Apples', 'Blueberries', 'Oranges', 'Kiwi']
fruits.splice(0, 1);
console.log(fruits); // ['Blueberries', 'Oranges', 'Kiwi']
fruits.reverse();
console.log(fruits); // ['Kiwi', 'Oranges', 'Blueberries']

//EXERCISE 2!

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits);
console.log(moreFruits[1][1][0]); // Oranges
