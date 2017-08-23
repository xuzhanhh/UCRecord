let rp = require("request-promise")
let co = require("co")
let rf = require('fs-readfile-promise')

let queue = [];

function sleep(ms) {
  return function (cb) {
    setTimeout(cb, ms);
  };
}

co(function* () {
  let index = 0;
  while (true) {
    queue.push(index);
    console.log("produceing",index)
    console.log("current queue is",queue)
    yield sleep(5000);
    index++;

  }
});

co(function* () {
  yield sleep(20000)
  while (true) {
    if (queue.length !== 0) {
      let comsumedata = queue.shift()
      console.log("comsumeing:" + comsumedata)
      yield sleep(2500)
    }
    else{
      console.log("no data in .waiting")
      yield sleep(2500)
    }
  }
})
// co(function *() {
//   let url = yield rf('123')
//   let jsondata = yield rp(url.toString())
//   console.log(jsondata)
// })