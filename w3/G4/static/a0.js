let time = document.querySelector('.time');


function showCurTime(){
  time.innerHTML = new Date();
}


setInterval(showCurTime, 1000)


// i = 0
// setInterval(function (){
//   console.log(`item: ${i++}`);
// }, 1000)




// function show(){
//   console.log('show method');
// }
// setTimeout(show, 3000)
