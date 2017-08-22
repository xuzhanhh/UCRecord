//hello world
//async表示这是一个async函数，await只能用在这个函数里面
//await表示在这里等待promise返回结果了，再继续执行
//await 后面跟着的应该是一个promise对象（当然，其他返回值也没关系，只是会立即执行，不过那样就没有意义了…）

// let sleep = function (time) {
//     return new Promise(function (resolve, reject) {
//         setTimeout(()=>{resolve()}, time);
//     })
// };
//
// let start = async function () {
//     // 在这里使用起来就像同步代码那样直观
//     console.log('start');
//     await sleep(3000).then(function () {
//         console.log('in promise')
//     });
//     console.log('end');
// };
//
// start();


//获得返回值
// await等待的虽然是promise对象，但是不用写then直接可以得到返回值
// let sleep = function (time) {
//     return new Promise(function (resolve, reject) {
//         setTimeout(function () {
//             // 返回 ‘ok’
//             resolve('ok');
//         }, time);
//     })
// };
//
// let start = async function () {
//     let result = await sleep(3000);
//     console.log(result); // 收到 ‘ok’
// };
// start()

//捕捉错误
//既然.then不用写了，那么.catch也不用写了，可以使用标准的try catch语法捕捉错误
// var sleep = function (time) {
//     return new Promise(function (resolve, reject) {
//         setTimeout(function () {
//             // 模拟出错了，返回 ‘error’
//             reject('this is an error');
//         }, time);
//     })
// };
//
// var start = async function () {
//     try {
//         console.log('start');
//         await sleep(3000); // 这里得到了一个返回错误
//
//         // 所以以下代码不会被执行了
//         console.log('end');
//     } catch (err) {
//         console.log(err); // 这里捕捉到错误 `error`
//     }
// };
// start()

console.log(__dirname)