function addTask() {
  let item = document.getElementById("todoInput").value;
  let text = document.createTextNode(item);
  let checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.name = "name";
  checkbox.value = "value";
  let newItem = document.createElement("div");

  newItem.appendChild(checkbox);
  newItem.appendChild(text);
  document.getElementsByClassName("listTasks")[0].appendChild(newItem);
}
