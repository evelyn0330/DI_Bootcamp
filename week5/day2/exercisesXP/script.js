//Exercise 1
// let h1 = document.querySelector("h1");
// console.log(h1);
// let remove = document.querySelector("p:last-child");
// remove.remove();

// let h2 = document.querySelector("h2");
// h2.addEventListener("click", function () {
//   h2.style.backgroundColor = "red";
// });

// let h3 = document.querySelector("h3");
// h3.addEventListener("click", function () {
//   h3.style.display = "none";
// });

// let btn = document.getElementById("toggleBold");
// let bold = document.querySelectorAll("p");
// console.log(bold);

// btn.addEventListener("click", function () {
//   for (i = 0; i < bold.length; i++) {
//     bold[i].style.fontWeight = "bold";
//   }
// });
//-----------------------------------------------------------------------------------------------------------------------------------
//Exercise 2
let form = document.getElementsByTagName("form")[0];
console.log(form);
let input1 = document.getElementById("fname");
let input2 = document.getElementById("lname");
let input3 = document.getElementById("submit");
console.log(input1, input2, input3);

console.log(form);
let firstIndex = form.elements.fname;
for (let a = 0; a < form.elements.length; a++) {
  let c = form.elements[a];
  console.log(c);
}
for (let a = 0; a < form.length; a++) {
  let f = form.elements[a].name;
  console.log(f);
}
form.addEventListener("submit", function101);
function function101(e) {
  e.preventDefault();
  let inputValue1 = form.elements[0].value;
  let inputValue2 = form.elements[1].value;
  if (inputValue1 && inputValue2) {
    // let li = document.createElement("li")
    // let textNode = document.createTextNode(`${inputValue1} ${inputValue2}`)
    // li.append(textNode)
    // let ul = document.querySelector("ul")
    // ul.append(li)
    for (let a = 0; a < e.target.elements.length - 1; a++) {
      let currentInput = e.target.elements[a];
      let li = document.createElement("li");
      let textNode = document.createTextNode(currentInput.value);
      li.append(textNode);
      let ul = document.querySelector("ul");
      ul.append(li);
    }
  }
}
//-----------------------------------------------------------------------------------------------------------------------------------
// // //Exercise 3
// let allBoldItems = document.getElementsByTagName("strong");
// // window.onload = getBold_items;

// // function getBold_items() {
// //   allBoldItems = document.getElementsByTagName("strong");
// // }
// function highlight() {
//   for (let i = 0; i < allBoldItems.length; i++) {
//     allBoldItems[i].style.color = "blue";
//   }
// }

// function return_normal() {
//   for (let i = 0; i < allBoldItems.length; i++) {
//     allBoldItems[i].style.color = "black";
//   }
// }
//-----------------------------------------------------------------------------------------------------------------------------------
//Exercise 4
// function volume_sphere() {
//   let volume;
//   let radius = document.getElementById("radius").value;
//   radius = Math.abs(radius);
//   volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
//   volume = volume.toFixed(4);
//   document.getElementById("volume").value = volume;
//   return false;
// }
// window.onload = document.getElementById("MyForm").onsubmit = volume_sphere;
