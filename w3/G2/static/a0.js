let time = document.querySelector('.time');

function showTime(){
  time.innerHTML = new Date();
}

setInterval(showTime, 1000)


// let i = 0;
// setInterval(function(){
//   console.log(`item: ${i++}`);
// }, 1000)

// setTimeout
// setInterval