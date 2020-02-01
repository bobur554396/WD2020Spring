let title = document.getElementById('title');
title.innerHTML = "To Do";

let box = document.querySelector('.box');
let text_input = document.querySelector('.text_input');


console.log(box.offsetTop, box.offsetLeft);

function addItem(){
  let item = document.createElement("li");
  item.innerHTML = text_input.value;
  box.appendChild(item);

  text_input.value = "";
}