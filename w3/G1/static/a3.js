// alert('')

function hello(name) {
  console.log(`hi ${name}`);
}

function plus1() {
  if (plus1.inc == undefined) {
    plus1.inc = 0;
  }
  plus1.inc += 1;
}
plus1()
plus1()
plus1()
plus1()
console.log(plus1.inc);