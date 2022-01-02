let words = prompt("Pleave write several words divided by commas.");

let arrayWords = words.split(",");

function frameStars(array) {
  let longestLength = array[0].length;

  for (i = 0; i < array.length; i++) {
    if (longestLength < array[i].length) {
      longestLength = array[i].length;
    }
  }

  let arrayRes = [];

  arrayRes[0] = "";
  arrayRes[array.length + 1] = "";
  longestLength += 4;

  for (i = 0; i <= longestLength; i++) {
    arrayRes[0] += "*";
    arrayRes[array.length + 1] += "*";
  }

  for (i = 1; i <= array.length; i++) {
    arrayRes[i] = "* " + array[i - 1];

    for (j = arrayRes[i].length; j < longestLength; j++) {
      arrayRes[i] += " ";
    }

    arrayRes[i] += "*";
  }

  return arrayRes;
}

let arrayResult = frameStars(arrayWords);

for (i = 0; i < arrayResult.length; i++) {
  console.log(arrayResult[i]);
}
