let title = document.getElementById('title');
title.innerHTML = 'To Do';


let box = document.querySelector('.box');
let todo_input = document.querySelector('.todo_input');


// btn.addEventListener('click', addItem)

console.log(todo_input.offsetTop, todo_input.offsetLeft);


let i = 0; 
function addItem(){  
  let item = document.createElement('li');
  if (todo_input.value != ''){
    item.innerHTML = todo_input.value;
    box.appendChild(item);
    todo_input.value = '';
  } else {
    alert('error');
  }
}


