function sum(a, b){
  return a + b;
}
// console.log(sum(2, 3));

let mult = function (a, b) {
  return a * b;
}

let a = 2;
function hello(a){
  console.log(a(2, 4));
}
// hello(mult)









function plus(){
  let aa = 2; // local variable
  aa += 10;
  if(plus.inc == undefined)
    plus.inc = 0;
  
  plus.inc += 1;
}
plus()
plus()
plus()
plus()
console.log(plus.inc);


