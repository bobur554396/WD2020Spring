let time = document.querySelector('.time');


function showTime(){
  time.innerHTML = new Date();
}

// time.addEventListener('onclick', showTime);


setInterval(showTime, 1000);


// setInterval
// setTimeout

// setTimeout(function(){
//   console.log('hi');
// }, 3000);


// let i = 0;
// setInterval(function(){
//   console.log(i++);
// }, 1000);
