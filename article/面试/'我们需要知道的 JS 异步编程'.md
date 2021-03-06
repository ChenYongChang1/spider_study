标题:我们需要知道的 JS 异步编程
描述:思维导图一、定时器1. 设定定时器setTimeout([function], [interval])setInterval([function], [interval])2. 清除定时器如何清除定时

> __大家好，我是林一一，异步编程在 JS 中是无法避免的，也是面试必问的。本文使用通俗易懂的语言解析异步编程中的原理，开始阅读吧😁__
## 思维导图


![bd34e30b2bef4dafaef7d3236af9be69_tplv-k3u1fbpfcp-watermark.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a13e906aa34bf7aef8f1e38bfe3827~tplv-k3u1fbpfcp-watermark.image)

## 一、定时器
> 定时器：设定一个定时器，到了设定时间，浏览器会把对应的方法执行。每一个定时器执行后都会有一个编号返回，每个定时器编号不一样。
### 1. 设定定时器
* setTimeout([function], [interval])
> function 都是在到达设定时间后才执行。且执行一次
``` js
let count = 1
let timer = setTimeout(function(){
    count++
    console.log(count)  // 2
}, 1000)
console.log(timer)  // 1
```
* setInterval([function], [interval])
> 在设定时间内执行，不主动停止的情况下一直执行。
``` js
let count = 1
let timer = setInterval(function(){
    count++
    console.log(count)  // 2
}, 1000)
console.log(timer)  // 1
/*
*   2
*   3
*   4
*   ...
*/
```
### 2. 清除定时器
> `clearTimeout/clearInterval` 两者都可以清除上面的两种定时器。
* 如何清除定时器？
> 只需要定时器的返回值编号清除即可。
```js
let count = 1
let timer = setInterval(function(){
    count++
    console.log(count)
    // count == 3 ? clearTimeout(timer) : null
    count == 3 ? clearInterval(timer) : null
}, 1000)
```

## 二、异步编程的原理
__先来看一个小例子__
``` js
let a = 0
setTimeout(() =>{
    console.log('a', ++a)
}, 0)
console.log(a)
/* 输出
*   0
*   1
*/
```
> 上面的例子中，`setTimeout` 是异步的，浏览器会将异步的代码加入到任务队列中，等到同步的代码执行完成后才执行异步的代码
### 1. 同步
> JS 是单线程的，代码至上而下执行时遇到同步的代码需要先执行完才可以进行下一步任务。比如循环等

### 2. 异步
> 所有需要等待的任务都是异步的。遇到异步代码时，不需要等待而是直接异步任务放入任务队列，等到后面的任务完成后，才会返回来执行没有完成异步的代码。比如事件绑定，所有定时器，ajax 的异步处理，部分回调函数，浏览器的渲染过程等等。
``` js
let a = 0
setTimeout(() =>{
    console.log('a', ++a)
}, 0)
console.log(a)
while(true){
}
```
> 上面的代码死循环了，即使定时器的时间到了也不会执行。因为同步的代码没有执行完一步就不会执行。

## 三、promise
### 1.基本概念
> `Promise` 只是一个管理异步编程的类，本身是同步。`Promise` 有三个状态 `pending/fulfilled/rejected`，三个状态只有两个状态出现要么成功要么失败。`new Promise()`时必须要传入回调函数 `executor`，否则报错。其中回调函数中有两个参数 `resolve, reject`，这两个参数可不写。
* `pending` ：初始化状态，开始执行异步的任务，只要执行 new，`new Promise(()=>{})`，promise 的状态就会变成 `pending`
* `fulfilled`：成功状态，执行 `resolve()`。
* `rejected`：失败状态, 执行 `rejected()`。
__先看一个小栗子。__
``` js
new Promise(()=> {
    setTimeout(()=> {
        console.log(1)
    }, 0)
    console.log(2)
}).then()
console.log(3)
/* 输出
*   2
*   3
*   1
*/
```
> 创建一个新的 `Promise` 的实例也就是 `new` 这个过程中会把 `Promise 中` 的函数先执行(不清楚 `new` 创建实例的过程中发生了什么可以看看这篇 [面试 | 你不得不懂得 JS 原型和原型链](https://juejin.cn/post/6938590449674223624#heading-6))。函数体内有异步操作的仍会加入任务队列，等到同步执行完成后才执行异步任务，比如函数体内的 `setTimeout 函数`。所以输出的结果就是 `2，3，1`。

__再来看一个小栗子__
``` js
const promise = new Promise((resolve, reject) => {
  resolve('success1')
  reject('error')
  resolve('success2')
})

promise.then((res) => {
    console.log('then: ', res)
}).catch((err) => {
    console.log('catch: ', err)
}
// then: success1
```
> promise 的状态只能改变一次，最后的状态不是 `fulfilled` 就是 `rejected`。也就是说同一个 `promise` 中的`resolve()/ reject()`只能执行一个且一次。

### 2. promise 是怎么管理异步的
> `promise` 参数的回调函数体内接收两个参数 `resolve/ reject`，这两个参数可以作为两个回调函数。
> 1. `resolve()`：是异步操作执行成功后执行，promise 的状态变成了 `fulfilled`，可以提供返回值，在 `.then()`中第一个参数接收
> 2. `reject()`：异步操作执行失败后执行，promise 的状态变成了 `rejected`，可以提供返回值，在 `.then()` 中第二个参数接收
> `resolve()` 和 `reject()` 中只能传递一个参数。promise 的状态发生改变后不会再变化。
> `resolve() 和 reject() 是异步操作`，执行这两个方法时，会先执行 `resolve/reject` 下面的同步代码，等到主任务为空时，再去调用 `resolve/reject` 把存放的方法执行。
> `Promise` 对象上有私有属性`Promise.resolve()/ Promise.reject()`等。
__举一个没什么意义的小栗子__
``` js
new Promise((resolve, reject)=> {
    setTimeout(()=> {
        console.log('林')
        resolve('ok')
        // reject('fail')
        console.log('一一')
    }, 0)
}).then( res => {
    console.log('status:', res)
}, res => {
    console.log('status:', res)
})
// 林 
// 一一 
// ok
```
> 上面的栗子直接看出 `resolve/reject` 是异步的。

### 3. promise.then(onfulfilled, onrejected) / promise.catch() 
* `promise.then(onfulfilled, onrejected)`
> 1. `promise.then()` 方法中有两个参数，分别对应着 promise 的两种不同的状态，`fulfilled, rejected`。对应的状态执行对应的方法。
> 2. `promise.then()` 中的参数是函数，如果传递的不是函数就会造成`值穿透`，也就是`resolve()/reject()` 的返回值会`.then()`中接收。
> 3. `promise.then()` 能够链式的调用，能够链式调用的原因不是`.then()` 方法中有`return this`，而是每一个 `.then()` 方法中都会返回一个新的`Promise` 实例。

* `promise.catch()`
> 1. `promise.catch()` 是 `promise.then()` 第二个参数的简便写法，也就是用来捕获 `reject()` 执行后的 `rejected`状态。
> 2. `.catch()`也可以实现链式调用，原因和`.then()` 方法一样都是返回了一个新的 `promise`。

__`.then()/.catch()` 中的返回值都不能是 `promise`自己本身的实例，因为会造成死循环__
#### 热身题
#### 1.举一个小栗子
``` js
Promise.resolve(1)
    .then((res) => {
        console.log(res)
        return 2
    }).catch(err => {
        console.log(err)
    }).then( res => {
        console.log(res)
    })
// 1 2
```
> 最终输出 `1 2`,

#### 2. 举一个值穿透的小栗子
``` js
Promise.resolve(1)
  .then(2)
  .then(Promise.resolve(3))
  .then(console.log)

// 等价于
// Promise.resolve(1)
//   .then(console.log)
```
#### 3. then()/.catch() 内不能返回自己本身的promise 实例，举一个栗子
``` js
let pro = Promise.resolve()
  .then(() => {
    console.log('promise', pro)
    return pro
  })
// Uncaught (in promise) TypeError: Chaining cycle detected for promise #<Promise>
```
> 创建的`promise` 实例是`pro`,返回值就不能是`pro`, 否则会造成死循环。

### 4. 关于 Promise.catch()
先看一道面试题
``` js
new Promise((resolve, reject) => {
    reject(1)
}).catch(() => {
    console.log(2)
//    throw 'err'
}).then(() => console.log(3), (v) => console.log(v))

// 输出： 2 3
```
> 不知你答对了没
* catch 确实是 .then 第二个参数的语法糖。值得一提的是在 `.catch` 内部如果没有抛出错误或一个错误的 promise 的`reject()`，那么都认为 .catch 返回的结果值是 `resolve()`的都将显示为成功。输出第二个输出是 3。


### 5.并行 Promise.all([promise1, promise2...])
> `Promise.all()` 中需要等待参数中所有 `promise` 的状态都成功才执行回调的`.then()`，如果有一个是失败的那么就执行 `.catch()`。接收的参数是一个包含 `promise` 实例的数组，`.all()` 这个方法的返回值也是一个新的`promise` 实例。
* 全部执行成功回调 `.then()` 接收到的就是一个数组
* 如果有执行失败的 `promise` 状态，回调 `.catch` 中就会捕获到执行失败的 `promise`。
* 执行失败的 promise 会让 promise.all 方法立即停止执行。
``` js
var p1 = Promise.resolve(1)
var p2 = Promise.resolve(2)
var p3 = Promise.resolve(3)
let pro =  Promise.all([p1, p2, p3])
  .then(res => {
      console.log(res)  //  [1, 2, 3]
  })
  .catch( err => {
      console.log(err)
  })
console.log(pro)    // Promise {<pending>}
```
> 全部执行成功，那么`.then()` 获取到的值就是`resolve()` 的返回值数组。
### 6. Promise.race()
> `.race()` 的作用也是接收一组异步任务，然后并行执行异步任务，只保留取一个最快执行完成的异步操作的结果，其他的方法仍在执行，不过执行结果会被抛弃。
*  接收的是一组数组，只获取一个最快执行完成 `resolve()/rejected()` 的返回值，返回值不是一个数组
``` js
var p1 = new Promise(function(resolve, reject) {
    setTimeout(reject, 500, "one");
});
var p2 = new Promise(function(resolve, reject) {
    setTimeout(resolve, 100, "two");
});

Promise.race([p1, p2]).then(function(value) {
  console.log(value); // "two"
});
```
> 两个都完成，但 p2 更快

### 7. Promise.finally()
> `.finally` 方法也是返回一个 `Promise`，他在 `Promise` 结束的时候，无论结果为 `resolved` 还是 `rejected`，都会执行里面的回调函数。
``` js
let promise = new Promise((resolve, reject) => {
    reject('error')
}).then( res => {
    console.log('then', res)
    return res
}).catch( err => {
    console.log('catch', err)   // `catch error`
     return err
}).finally( () => {
    console.log('finally')  //'finally'
})
```

### 热身题
#### 热身题1
``` js
const promise = new Promise((resolve, reject) => {
  console.log(1)
  resolve()
  console.log(2)
})
promise.then(() => {
  console.log(3)
})
console.log(4)
// 1, 2, 4, 3
```
> 因为 `resolve()` 是异步的，`promise.then`也是异步的，在没有获取到 `resolve()` 的`fulfilled` 状态时`.then()` 不会执行。

#### 热身题2
``` js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('once')
    resolve('success')
  }, 1000)
})

const start = Date.now()
promise.then((res) => {
  console.log(res, Date.now() - start)
})
promise.then((res) => {
  console.log(res, Date.now() - start)
})
/* 输出
* once
* success 1002
* success 1002
*/
```
> `promise.then()` 即使有多个，但是`resolve()/reject()`后的调用时同时执行的。所以同时输出了 `success 1002`
#### 热身题3
```js
const p = function(){
    return new Promise((resolve, reject) =>{
        const p1 = new Promise((resolve, reject) => {
            setTimeout(()=>{
                resolve(1)
            },0)
            resolve(2)
        })
        p1.then((res) =>{
            console.log(res)
        })
        console.log(3)
        resolve(4)
    })
}
p().then(res => {
    console.log(res)
})
console.log('end')
// 3, end, 2, 4
```
> 这里只需要注意是`resolve(2)`夏安进入队列，`resolve(4)·才进入的异步队列。同时 `resolve(1)` 抛出的结果不会在被执行，因为 Promise 状态已经改变。

## 三、async 和 await 
__先来看一个栗子__
``` js
function fn(){
    return new Promise((resolve, reject) => {
        setTimeout( () => {
            Math.random() < 0.5 ? resolve('resolve 001') : reject('reject 002')
        }, 0)
    })
}

async function get() {
    let res = await fn()
    console.log(res)
    console.log(1212)
}
get()
```
### 1. async
>1. `async` 和 `await` 是 ES7 中增加来对 `promise` 操作的方法，是 ES7 系列提供的语法糖，`await` 不能单独使用一定要结合 `async` 来使用。
>2. `async` 会返回一个 `promise`  对象，`async` 函数调用不会造成代码的阻塞
### 2. await
>1. `await` 是用来 `等待获取` 一个 `promise` 的 `resolve/reject` 的执行结果，像上面的 `let res = await fn()` 是先把 `fn()`执行后，来获取 `resolve/reject` 返回的结果，不过 `await` 后面也可以不跟着一个 `promise`，但是这样写就没有意义了。
>2. `await 或 await fn()` 这个操作不是同步的，而是异步的。`await` 下面的代码不会执行，而是移入到任务队列等待区，等到主栈中的其他任务完成且 `fn()` 中的 `promise` 将结果返回，`await` 下面的代码才可以重新回到主栈中执行。`await` 可以使 `promise` 的操作更加像同步的代码。
>3. __如果 `await` 等待的 `Promise` 返回值如果是 `rejected/peding`，`await` 下面的代码都不会执行, `reject()` 返回的代表已经报错了。记住 await 10 等价于 await Promise.resolve(10)__
__举一个小栗子,说明 async/await 是语法糖__
``` js
async function async1() {
	console.log('async1 start');
	await async2();
	console.log('async1 end');
}
// 上面的代码等价于 ==>
async function async1() {
    console.log('async1 start');
    Promise.resolve(async2()).then(() => {
        console.log('async1 end')
    })
}
```

### 思考
#### 热身1，await 是同步吗？，求输出的结果
``` js
console.log(1)
function fn(){
    return new Promise((resolve, reject) => {
        console.log(5)
        resolve('resolve 001')
        console.log(6)
    })
}

async function get() {
    console.log(2)
    let res = await fn()
    console.log(res)
    console.log(3)
}
get()
console.log(4)
//1, 2, 5, 6, 4, resolve 001, 3
```
>`await` 是异步的同时会让出线程，`fn()` 执行后线程开始让出，那么 `await` 的下面的代码不会立即执行会先到主栈的等待区，主栈中 `console.log(4)` 执行后，再回来执行 `await` 处的代码。

### 2. 热身2，求输出结果
```js
console.log(1)
async function get() {
    console.log(2)
    let res = await 200
    console.log(res)
    console.log(3)
}
get()
console.log(4)
// 1, 2, 4, 200, 3
```
> 根据上面一题  `await` 异步代码的原因，可以容易的分析出答案。同时说明 `await` 后面也可以跟着一个非 `promise` 的实例。

### 3. 热身，求输出结果
``` js
async function fn(){
    await fo() // Promise.resolve(fo()) ==> undefined
    console.log(1)
}

async function fo(){
}
fn()
// 1
```
> 输出结果是 1 因为 `fo()` 有返回值，且返回值不是 `reject()`

### 4. 热身，求输出结果
``` js
async function async1() {
  console.log('async1 start')
  await new Promise(resolve => {
    console.log('promise1')
  })
  console.log('async1 success')
  return 'async1 end'
}
console.log('srcipt start')
async1().then(res => console.log(res))
console.log('srcipt end')  
// srcipt start, async1 start, promise1, srcipt end,
``` 
> 上面没有输出 `async1 success` 是因为 await 返回的Promise实例还处于 pending 状态，没有结果返回所以下面的代码不会执行。`async1` 的返回值是一个 Promise，也不会打印`async1 end`



## 四、经典面试题
### 1. promise 的优缺点/为什么使用 promise？
* 优点：promise 可以解决回调地狱，promise 大大增强了嵌套函数的可读性和可维护性，
* 缺点：无法取消 Promise，错误需要通过回调函数来捕获；如果不设置回调函数，Promise 内部抛出的错误，不会反映到外部；当处于 pending（等待）状态时，无法得知目前进展到哪一个阶段，是刚刚开始还是即将完成

### 2. setTimeout、Promise、Async/Await 的区别
* setTimeout: setTimeout 的回调函数放到宏任务队列里，等到执行栈清空以后执行
* Promise: Promise 本身是同步的立即执行函数，当在 executor 中执行 resolve或者 reject 的时候，此时是异步操作，会先执行 then/catch 等，当主栈完成时，才会去调用 resolve/reject 方法中存放的方法。
* async: async 函数返回一个 Promise 对象，当函数执行的时候，一旦遇到 await 就会先返回，等到触发的异步操作完成，再执行函数体内后面的语句。可以理解为，是让出了线程，跳出了 async 函数体。

### 3. 实现一个 sleep 函数，比如 sleep(1000) 意味着等待 1000 毫秒。
``` js
function sleep1(time) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve();
        }, time);
    })
}
sleep1(1000).then(() => console.log("sleep1"));
```

### 4. Promise 构造函数是同步执行还是异步执行，那么 then 方法呢
> `Promise` 是同步的，执行 `new promise(callback)` 时回调函数`callback` 就会被立即执行，`then()` 方法是异步的。
``` js
const promise = new Promise((resolve, reject) => {
    console.log(1)
    resolve()
    console.log(2)
})
promise.then(() => {
    console.log(3)
})
console.log(4)
```
> 1243，promise 构造函数是同步执行的，then 方法是异步执行的

### 5. 介绍下 Promise.all 使用、原理实现及错误处理
``` js
const p = Promise.all([p1, p2, p3]);
```
> Promise.all 方法接受一个数组作为参数，p1、p2、p3 都是 Promise 实例，如果不是，就会先调用下面讲到的 Promise resolve 方法，将参数转为 Promise 实例，再进一步处理。（Promise.all 方法的参数可以不是数组，但必须具有 Iterator 接口，且返回的每个成员都是 Promise 实例。）

### 5. 介绍下 Promise.all, Promise.race() 的区别
> 看上面的介绍

## Promise 的各种 api 实现会在下一篇文章中实现。给个期待吧😂

## 五、参考
[Promise 必知必会（十道题）](https://juejin.cn/post/6844903509934997511)

[BAT前端经典面试问题：史上最最最详细的手写Promise教程](https://juejin.cn/post/6844903625769091079#heading-0)

[MDN async/await](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Async_await)

## 六、结束
> __感谢阅读到这里，如果着篇文章能对你有一点启发或帮助的话欢迎  [github star](https://github.com/lurenacm/againJS/issues), 我是林一一,下次见。__






