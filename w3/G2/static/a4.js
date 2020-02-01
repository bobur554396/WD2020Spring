let text = document.getElementById("text");
text.innerHTML = "TO DO";
// console.log(text);

let box = document.querySelector('.box');
let input = document.querySelector('.todo_input');
let btn = document.querySelector('.btn');


console.log(btn.offsetTop, btn.offsetLeft);


// btn.addEventListener('onclick', addElement);

function addElement(){
  let new_el = document.createElement("li");
  new_el.innerHTML = input.value;
  box.appendChild(new_el);

  input.value = "";
}


