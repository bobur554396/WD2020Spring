// var a;
// console.log(a);
// console.log("2" == 2);

// // 1.
// function sum(a, b){
//   // console.log(a + b);
//   return a + b;
// }
// res = sum(2, 4);
// console.log(res);


// 2.
// let mult = function (a, b){
//   return a * b;
// }
// // res = mult(2, 4);
// // console.log(res);

// function hello(a) {
//   console.log(a);  
// }

// hello(mult(3, 4))




function plus(){
  let a = 2; // local variable
  if(plus.inc == undefined)
    plus.inc = 0;
  plus.inc += 1;
}

plus()
plus()
plus()
plus()
plus()
console.log(plus.inc);
