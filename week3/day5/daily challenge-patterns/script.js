//First loop
let s = 6;
let string = "";
for (let i = 0; i < s; i++) {
  {
    string += "* ";
  }
  string += "<br>";
}
document.write(string);

//Second loop - Nested
let s = 6;
let string = "";
for (let i = 0; i < s; i++) {
  for (let j = 0; j <= i; j++) {
    string += "* ";
  }
  string += "<br>";
}
document.write(string);
