标题:前端面试官： React我就问这些问题！能不能刷到我就看你的造化了
描述:1. React 中 keys 的作用是什么？ Keys 是 React 用于追踪哪些列表中元素被修改、被添加或者被移除的辅助标识。 有了key属性后，就可以与组件建立了一种对应关系，react根据key来决定是销毁重新创建组件还是更新组件。 key相同，若组件属性有所变化，则…

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3a435d39f5a4d87804caabef263e9f8~tplv-k3u1fbpfcp-zoom-1.image)

## 1.基础篇

### 1. React 中 keys 的作用是什么？

*   Keys 是 React 用于追踪哪些列表中元素被修改、被添加或者被移除的辅助标识。

```
render () {
  return (
    <ul>
      {this.state.todoItems.map(({item, key}) => {
        return <li key={key}>{item}</li>
      })}
    </ul>
  )
}

```

*   react利用key来识别组件，它是一种身份标识标识，相同的key react认为是同一个组件，这样后续相同的key对应组件都不会被创建
*   有了key属性后，就可以与组件建立了一种对应关系，react根据key来决定是销毁重新创建组件还是更新组件。
*   key相同，若组件属性有所变化，则react只更新组件对应的属性；没有变化则不更新。
*   key值不同，则react先销毁该组件(有状态组件的componentWillUnmount会执行)，然后重新创建该组件（有状态组件的constructor和componentWillUnmount都会执行）

### 2.调用 setState 之后发生了什么？

*   在代码中调用 setState 函数之后，React **会将传入的参数对象与组件当前的状态合并**，然后触发所谓的调和过程。
*   经过调和过程，React会以相对高效的方式根据新的状态构建React元素树并且着手重新渲染整个 UI 界面。
*   在 React 得到元素树之后，React **会自动计算出新的树与老树的节点差异**，然后根据差异对界面**进行最小化重渲染**。
*   在差异计算算法中，React 能够相对精确地知道哪些位置发生了改变以及应该如何改变，这就保证了**按需更新**，而不是全部重新渲染。

### 3.触发多次setstate，那么render会执行几次？

*   多次setState会**合并**为一次render，因为setState并不会立即改变state的值，而是将其放到一个**任务队列**里，最终将多个setState合并，一次性更新页面。
*   所以我们可以在代码里多次调用setState，每次只需要关注当前修改的字段即可。

### [补充] react中如何对state中的数据进行修改？setState为什么是一个异步的？

*   修改数据通过this.setState(参数1,参数2)
*   this.setState是一个异步函数
    *   参数1 : 是需要修改的数据是一个对象
    *   参数2 : 是一个回调函数，可以用来验证数据是否修改成功，同时可以获取到数据更新后的DOM结构等同于componentDidMount
*   this.setState中的第一个参数除了可以写成一个对象以外，还可以写成一个函数 **！**，函数中第一个值为prevState 第二个值为prePprops this.setState((prevState,prop)=>({}))

#### 为什么建议传递给 setState的参数是一个callback而不是一个对象？

*   因为this.props 和this.state的更新可能是异步的，不能依赖它们的值去计算下一个state

#### 为什么setState是一个异步的？（请看3）

*   当批量执行state的时候可以让DOM渲染的更快,也就是说多个setstate在执行的过程中还需要被合并

### 4.this.setState之后react做了哪些操作？

*   shouldComponentUpdate
*   componentWillUpdate
*   render
*   componentDidUpdate

### 5.简述一下virtual DOM （虚拟dom）如何工作？（4 & 5 取一回答）

*   当数据发生变化，比如setState时，会引起组件重新渲染，整个UI都会以virtual dom的形式重新渲染
*   然后收集差异也就是diff新的virtual dom和老的virtual dom的差异
*   最后把差异队列里的差异，比如增加节点、删除节点、移动节点更新到真实的DOM上

### 5.为什么虚拟 dom 会提高性能?

*   虚拟 dom 相当于在 js 和真实 dom 中间加了一个缓存，利用 dom diff 算法避免了没有必要的 dom 操作，从而提高性能。
*   用 JavaScript 对象结构表示 DOM 树的结构
*   然后用这个树构建一个真正的 DOM 树，插到文档当中当状态变更的时候，重新构造一棵新的对象树。
*   然后用新的树和旧的树进行比较，记录两棵树差异把 2 所记录的差异应用到步骤 1 所构建的真正的 DOM 树上，视图就更新了。

### 6.react diff 原理

*   把树形结构按照层级分解，只比较同级元素。
*   给列表结构的每个单元添加唯一的 key 属性，方便比较。
*   React 只会匹配相同class的component（这里面的class指的是组件的名字）
*   合并操作，调用 component 的 setState 方法的时候, React 将其标记为 dirty.到每一个事件循环结束, React检查所有标记 dirty 的 component 重新绘制.
*   选择性子树渲染。开发人员可以重写 shouldComponentUpdate 提高 diff 的性能。

### 7.React 中 refs 的作用是什么？（详细版本）

*   Refs 是 React 提供给我们的安全访问DOM元素或者某个组件实例的句柄。
*   是父组件用来获取子组件的dom元素的
*   我们可以为元素添加 ref 属性然后在回调函数中接受该元素在 DOM 树中的句柄，该值会作为回调函数的第一个参数返回

```
class CustomForm extends Component {
  handleSubmit = () => {
    console.log("Input Value: ", this.input.value)
  }
  render () {
    return (
      <form onSubmit={this.handleSubmit}>
        <input
          type='text'
          ref={(input) => this.input = input} />
        <button type='submit'>Submit</button>
      </form>
    )
  }
}
```

*   上述代码中的 input 域包含了一个 ref 属性，该属性声明的回调函数会接收 input 对应的 DOM 元素，我们将其绑定到 this 指针以便在其他的类函数中使用。
*   另外值得一提的是，refs 并不是类组件的专属，函数式组件同样能够利用闭包暂存其值

```
 function CustomForm ({handleSubmit}) {
  let inputElement
  return (
    <form onSubmit={() => handleSubmit(inputElement.value)}>
      <input
        type='text'
        ref={(input) => inputElement = input} />
      <button type='submit'>Submit</button>
    </form>
  )
}
```

### [详细易懂版本(推荐)]

**1. ref设置为普通字符串**

```
<button ref="myBtn"></button>
```

*   给**元素**定义ref属性，后续可以通过 this.refs.myBtn 来获取这个真实DOM对象
*   给**组件**定义ref属性，后续可以通过 this.refs.myBtn 来获取这个组件的实例对象

**2. ref设置为箭头函数**

```
<button ref="{ (sl) => { this.myBtn = sl } }"></button>

```

*   给**元素**定义ref属性，后续可以通过 this.myBtn 来获取这个真实DOM对象
*   给**组件**定义ref属性，后续可以通过 this.myBtn 来获取这个组件的实例对象

### 8.React 中有哪些构建组件的方式？

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/833bcb7f133841e4a96df8f6fc8f612d~tplv-k3u1fbpfcp-zoom-1.image)

**有什么区别？**

*   函数组件看似只是一个返回值是DOM结构的函数，其实它的背后是无状态组件的思想。
*   函数组件中，你无法使用State，也无法使用组件的生命周期方法，这就决定了函数组件都是展示性组件，接收Props，渲染DOM，而不关注其他逻辑
*   函数组件中没有this
*   函数组件更容易理解。当你看到一个函数组件时，你就知道它的功能只是接收属性，渲染页面，它不执行与UI无关的逻辑处理，它只是一个**纯函数**。而不用在意它返回的DOM结构有多复杂。

### 9.事件处理函数的this指向问题

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dc3b86b3c464af8b82827797117fa51~tplv-k3u1fbpfcp-zoom-1.image)

### [补充] 事件处理函数如何传递参数？

*   可以使用 bind 传递参数
*   将事件处理函数交给箭头函数，然后在箭头函数里面调用我自己开始想要调用的那个方法，这时我已经是个普通函数了。

### [注意！！！]

*   如果一个事件处理函数传递了额外的参数，那么事件对象会摸摸的放置在最后一个里面


## 2.十万个为什么篇

### 1.为什么列表循环渲染的key最好不要用index？

*   举例说明

> 变化前数组的值是[1,2,3,4]，key就是对应的下标：0，1，2，3 变化后数组的值是[4,3,2,1]，key对应的下标也是：0，1，2，3

*   那么diff算法在变化前的数组找到key =0的值是1，在变化后数组里找到的key=0的值是4
*   因为子元素不一样就重新删除并更新
*   但是如果加了唯一的key,如下:

> 变化前数组的值是[1,2,3,4]，key就是对应的下标：id0，id1，id2，id3

> 变化后数组的值是[4,3,2,1]，key对应的下标也是：id3，id2，id1，id0

*   那么diff算法在变化前的数组找到key =id0的值是1，在变化后数组里找到的key=id0的值也是1
*   因为子元素相同，就不删除并更新，只做移动操作，这就提升了性能

### 2.什么是状态提升？

### 3.什么是高阶组件？

### 4.什么是受控组件和非受控组件？

### 5.什么是纯函数？

### 6.什么是上下文Context?

### 7.react中的Portal是什么？

### 8.react16的错误边界（Error Boundaries）是什么?


**除了React之外，我整理的这份《前端校招面试真题解析大全》还包括html，css，JavaScript，ES6，计算机网络，浏览器，工程化，模块化，Node.js，框架，数据结构，性能优化，项目等等。**

文章中所列主要为大纲部分，详细内容可以在文末自行获取哈！

## HTML

* HTML5新特性，语义化
* 浏览器的标准模式和怪异模式
* xhtml和html的区别
* 使用data-的好处
* meta标签
* canvas
* HTML废弃的标签
* IE6 bug，和一些定位写法
* css js放置位置和原因
* 什么是渐进式渲染
* html模板语言
* meta viewport原理

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a86f022e2e94c029055443e278a7ac2~tplv-k3u1fbpfcp-zoom-1.image)


## CSS

* 盒模型，box-sizing
* CSS3新特性，伪类，伪元素，锚伪类
* CSS实现隐藏页面的方式
* 如何实现水平居中和垂直居中。
* 说说position，display
* 请解释*{box-sizing:border-box;}的作用，并说明使用它的好处
* 浮动元素引起的问题和解决办法？绝对定位和相对定位，元素浮动后的display值
* link和@import引入css的区别
* 解释一下css3的flexbox，以及适用场景
* inline和inline-block的区别
* 哪些是块级元素那些是行级元素，各有什么特点
* grid布局
* table布局的作用
* 实现两栏布局有哪些方法？
* css dpi
* 你知道attribute和property的区别么
* css布局问题？css实现三列布局怎么做？如果中间是自适应又怎么做？
* 流式布局如何实现，响应式布局如何实现
* 移动端布局方案
* 实现三栏布局（圣杯布局，双飞翼布局，flex布局）
* 清除浮动的原理
* overflow:hidden有什么缺点？
* padding百分比是相对于父级宽度还是自身的宽度
* css3动画，transition和animation的区别，animation的属性，加速度，重力的模拟实现
* CSS 3 如何实现旋转图片（transform: rotate）
* sass less
* 对移动端开发了解多少？（响应式设计、Zepto；@media、viewport、JavaScript 正则表达式判断平台。）
* 什么是bfc，如何创建bfc？解决什么问题？
* CSS中的长度单位（px,pt,rem,em,ex,vw,vh,vh,vmin,vmax）
* CSS 选择器的优先级是怎样的？
* 雪碧图
* svg
* 媒体查询的原理是什么？
* CSS 的加载是异步的吗？表现在什么地方？
* 常遇到的浏览器兼容性问题有哪些？常用的hack的技巧
* 外边距合并
* 解释一下“::before”和“:after”中的双冒号和单冒号的区别

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21464e53e4464d5da90651b7e62e4776~tplv-k3u1fbpfcp-zoom-1.image)

## JS

* js的基本类型有哪些？引用类型有哪些？null和undefined的区别。
* 如何判断一个变量是Array类型？如何判断一个变量是Number类型？（都不止一种）
* Object是引用类型嘛？引用类型和基本类型有什么区别？哪个是存在堆哪一个是存在栈上面的？
* JS常见的dom操作api
* 解释一下事件冒泡和事件捕获
* 事件委托（手写例子），事件冒泡和捕获，如何阻止冒泡？如何组织默认事件？
* 对闭包的理解？什么时候构成闭包？闭包的实现方法？闭包的优缺点？
* this有哪些使用场景？跟C,Java中的this有什么区别？如何改变this的值？
* call，apply，bind
* 显示原型和隐式原型，手绘原型链，原型链是什么？为什么要有原型链
* 创建对象的多种方式
* 实现继承的多种方式和优缺点
* new 一个对象具体做了什么
* 手写Ajax，XMLHttpRequest
* 变量提升
* 举例说明一个匿名函数的典型用例
* 指出JS的宿主对象和原生对象的区别，为什么扩展JS内置对象不是好的做法？有哪些内置对象和内置函数？
* attribute和property的区别
* document load和document DOMContentLoaded两个事件的区别
* === 和 == , [] === [], undefined === undefined,[] == [], undefined == undefined
* typeof能够得到哪些值
* 什么是“use strict”,好处和坏处
* 函数的作用域是什么？js 的作用域有几种？ 
* JS如何实现重载和多态
* 常用的数组api，字符串api
* 原生事件绑定（跨浏览器），dom0和dom2的区别？
* 给定一个元素获取它相对于视图窗口的坐标
* 如何实现图片滚动懒加载
* js 的字符串类型有哪些方法？ 正则表达式的函数怎么使用？
* 深拷贝
* 编写一个通用的事件监听函数
* web端cookie的设置和获取
* setTimeout和promise的执行顺序
* JavaScript 的事件流模型都有什么？
* navigator对象，location和history
* js的垃圾回收机制
* 内存泄漏的原因和场景
* DOM事件的绑定的几种方式
* DOM事件中target和currentTarget的区别
* typeof 和 instanceof 区别，instanceof原理
* js动画和css3动画比较
* JavaScript 倒计时（setTimeout）
* js处理异常
* js的设计模式知道那些
* 轮播图的实现，以及轮播图组件开发，轮播10000张图片过程
* websocket的工作原理和机制。
* 手指点击可以触控的屏幕时，是什么事件？
* 什么是函数柯里化？以及说一下JS的API有哪些应用到了函数柯里化的实现？(函数柯里化一些了解，以及在* 函数式编程的应用，最后说了一下JS中bind函数和数组的reduce方法用到了函数柯里化。)
* JS代码调试
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c831d7eafdf4446384267ed88903e3f4~tplv-k3u1fbpfcp-zoom-1.image)

## 框架

* 使用过哪些框架？
* zepto 和 jquery 是什么关系，有什么联系么？
* jquery源码如何实现选择器的，为什么$取得的对象要设计成数组的形式，这样设计的目的是什么
* jquery如何绑定事件，有几种类型和区别
* 什么是MVVM，MVC，MVP
* Vue和Angular的双向数据绑定原理
* Vue，Angular组件间通信以及路由原理
* react和vue的生命周期
* react和vue的虚拟dom以及diff算法
* vue的observer，watcher，compile
* react和angular分别用在什么样的业务吗？性能方面和MVC层面上的区别
* jQuery对象和JS的Element有什么区别
* jQuery对象是怎么实现的
* jQuery除了它封装了一些方法外，还有什么值得我们去学习和使用的？
* jQuery的$(‘xxx’)做了什么事情
* 介绍一下bootstrap的栅格系统是如何实现的

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dcd11096f5b441181781e9e8b31c970~tplv-k3u1fbpfcp-zoom-1.image)

## 浏览器相关

* 跨域，为什么JS会对跨域做出限制
* 前端安全：xss，csrf...
* 浏览器怎么加载页面的？script脚本阻塞有什么解决方法？defer和async的区别？
* 浏览器强缓存和协商缓存
* 浏览器的全局变量有哪些
* 浏览器同一时间能够从一个域名下载多少资源
* 按需加载，不同页面的元素判断标准
* web存储、cookies、localstroge等的使用和区别
* 浏览器的内核
* 如何实现缓存机制？（从200缓存，到cache到etag再到）
* 说一下200和304的理解和区别
* 什么是预加载、懒加载
* 一个 XMLHttpRequest 实例有多少种状态？ 
* dns解析原理，输入网址后如何查找服务器
* 服务器如何知道你？
* 浏览器渲染过程
* ie的某些兼容性问题
* session
* 拖拽实现
* 拆解url的各部分

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f67b1ad450ca488cbd71363362741e6c~tplv-k3u1fbpfcp-zoom-1.image)

##面试题完整文档划到文末直接免费领取。

## ES6

* 谈一谈 promise
* 所有的 ES6 特性你都知道吗？如果遇到一个东西不知道是 ES6 还是 ES5, 你该怎么区分它
* es6的继承和es5的继承有什么区别
* promise封装ajax
* let const的优点
* es6 generator 是什么，async/await 实现原理
* ES6和node的commonjs模块化规范区别
* 箭头函数，以及它的this

## 计算机网络

* HTTP协议头含有哪些重要的部分，HTTP状态码
* 网络url输入到输出怎么做？
* 性能优化为什么要减少 HTTP 访问次数？
* Http请求的过程与原理
* https（对是https）有几次握手和挥手？https的原理。
* http有几次挥手和握手？TLS的中文名？TLS在哪一网络层？
* TCP连接的特点，TCP连接如何保证安全可靠的？
* 为什么TCP连接需要三次握手，两次不可以吗，为什么
* 为什么tcp要三次握手四次挥手？
* tcp的三次握手和四次挥手画图（当场画写ack 和 seq的值）？
* tcp与udp的区别
* get和post的区别？什么情况下用到？
* http2 与http1 的区别？
* websocket
* 什么是tcp流，什么是http流
* babel是如何将es6代码编译成es5的
* http2的持久连接和管线化
* 域名解析时是tcp还是udp
* 域名发散和域名收敛
* Post一个file的时候file放在哪的？
* HTTP Response的Header里面都有些啥？


## 工程化

* 对webpack,gulp，grunt等有没有了解?对比。
* webpack的入口文件怎么配置，多个入口怎么分割。
* webpack的loader和plugins的区别
* gulp的具体使用。
* 前端工程化的理解、如何自己实现一个文件打包，比如一个JS文件里同时又ES5 和ES6写的代码，如何编译兼容他们

## 模块化

* 对AMD,CMD,CommonJS有没有了解?
* 为什么要模块化？不用的时候和用RequireJs的时候代码大概怎么写？
* 说说有哪些模块化的库，有了解过模块化的发展的历史吗？
* 分别说说同步和异步模块化的应用场景，说下AMD异步模块化实现的原理？
* 如何将项目里面的所有的require的模块语法换成import的ES6的语法？
* 使用模块化加载时，模块加载的顺序是怎样的，如果不知道，根据已有的知识，你觉得顺序应该是怎么样的？

## Nodejs

* 对nodejs有没有了解
* Express 和 koa 有什么关系，有什么区别？
* nodejs适合做什么样的业务？
* nodejs与php，java有什么区别
* Nodejs中的Stream和Buffer有什么区别？
* node的异步问题是如何解决的？
* node是如何实现高并发的？
* 说一下 Nodejs 的 event loop 的原理

## 数据结构

* 基本数据结构：（数组、队列、链表、堆、二叉树、哈希表等等）
* 8种排序算法，原理，以及适用场景和复杂度
* 说出越多越好的费波拉切数列的实现方法？

## 性能优化

* cdn的用法是什么？什么时候用到？
* 浏览器的页面优化？
* 如何优化 DOM 操作的性能
* 单页面应用有什么SEO方案？
* 单页面应用首屏显示比较慢，原因是什么？有什么解决方案？

## 其他

* 正则表达式
* 前端渲染和后端渲染的优缺点
* 数据库的四大特性，什么是原子性，表的关系
* 你觉得前端体系应该是怎样的？
* 一个静态资源要上线，里面有各种资源依赖，你如何平稳上线
* 如果要你去实现一个前端模板引擎，你会怎么做
* 知道流媒体查询吗？
* SEO
* mysql 和 mongoDB 有什么区别？
* restful的method解释
* 数据库知识、操作系统知识
* click在ios上有300ms延迟，原因及如何解决
* 移动端的适配，rem+媒体查询/meta头设置
* 移动端的手势和事件；
* unicode，utf8，gbk编码的了解，乱码的解决

## 三面、四面常问的开放性问题

* 你都看过什么书？最近在看什么书？
* 用过什么框架？有没有看过什么框架的代码？
* 有没有学过设计模式？
* 说一说观察者模式吧！能不能写出来？
* 你最大的优点是什么？那你最大的缺点呢？
* 你大学期间做过最疯狂的事情是什么？
* 你除了写博客还有什么输出？
* 现在你的领导给你了一份工作，要求你一个星期完成，但你看了需求以后估计需要3周才能完成，你该怎么办？
* 平时关注的前端技术
* 如何规划自己的职业生涯
* 项目过程中，有遇到什么问题吗？怎么解决的？
* 最近在研究哪方面的东西？
* 请介绍一项你最热爱、最擅长的专业领域，并且介绍的学习规划。
* 请介绍你参与的印象最深刻的一个项目，为什么？并且介绍你在项目中的角色和发挥的作用。

## HR面

* 你为什么要学习前端？
* 你平时的是怎么学习前端的？有什么输出？
* 你觉得自己最好的项目是什么？
* 身边比较佩服的人有什么值得你学习的？你为什么没有跟他们一样？
* 同事的什么问题会让你接受不了
* 压力最大的事情是什么？
* 和同学做过的最好的项目？
* 身边的朋友通常对你的评价是什么
* 喜欢什么样的工作氛围
* 如何看待加班
* 有没有对象
* 意向城市
* 其他的offer
* 为什么要录取你？
* 大学里花费时间最多的三件事情
* 周末都会干什么？
* 未来职业规划

## 建议

* 面试的时候不要表现出自己想创业。敲黑板。

* 从来没有看过源码的话，建议从jQuery，zepto这之类的源码入手，后期可以了解Vue，React常见的功能的源码思路和实现。

* 项目经验描述的时候不用太太太详细，拣重点的讲。

#### **由于篇幅有限，只能分享部分面试题，完整版面试题及答案可以[【点击我】](https://jq.qq.com/?_wv=1027&k=SBb7oFqq)阅读下载哦~无偿分享给大家**


