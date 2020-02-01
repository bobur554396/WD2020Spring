// res = confirm('asd')
// let name = prompt("Enter your name: ")


let el = document.getElementById("test");
// el.innerHTML = 'name';


// let el = document.querySelector('.box')

// let text = document.createElement("h1");
// text.innerHTML = "added text attr";
// el.appendChild(text)
// text.addEventListener('onclick', function(){})

let time = document.querySelector('.time');
let btn = document.querySelector('.btn');



function show(){
  time.innerHTML = new Date();
}


setInterval(show, 1000)


// i = 1
// setInterval(function(){
//   console.log(`hello: ${i++}`);
// }, 1000)

// setInterval()
// setTimeout()


