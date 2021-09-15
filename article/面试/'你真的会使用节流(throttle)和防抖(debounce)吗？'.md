标题:你真的会使用节流(throttle)和防抖(debounce)吗？
描述:背景之前我做了一个关于throttle和debounce这两个函数理解程度的小调查，调查结果令我感到意外：有的人在项目开发中没使用过 throttle 或者 debounce，有的用过 throttl

## 背景

之前我做了一个关于`throttle`和`debounce`这两个函数理解程度的小调查，调查结果令我感到意外：有的人在项目开发中没使用过 throttle 或者 debounce，有的用过 throttle 或者 debounce 中的一个，有的用过但是不能准确的说出它们的区别，还有就是应用场景错误。因此，我决定整理一下这两个方法的知识，厘清它们的区别，希望能帮助大家在实际项目中正确应用。

## 实际场景

在开始之前我们先看一下两个开发中的场景。

1. 有一个搜索按钮，每次点击发送一次AJAX请求到后台请求数据。如果我们在前端不加以限制，用户就可能连续点击，必然会发送大量重复的请求，浪费服务器资源。更极端的情况是，如果下一次请求依赖于上一次请求的结果，在这样的情况下，必然造成数据的混乱。

2. 页面上有大量Echart图表，每个图标都监听了resize事件，window resize 的时候频繁的触发resize事件导致页面性能下降。

## 案例分析

下面我们来看一下实际的项目案例。

![案例.gif](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78aaa3cf3dde4854a1a6989ccb8b2b8d~tplv-k3u1fbpfcp-watermark.image)

通过上面的示例，我们发现滚动事件频繁的被触发，而这么密集的事件触发是完全没有必要的，无意义的，浪费资源的。

因此，我们编写了一个debounce函数，它的作用是延迟400ms执行scroll事件的回调函数，先看一下这段代码。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80160816ece04ca1a64d23af175e4025~tplv-k3u1fbpfcp-watermark.image)

我们可以看到这段代码的核心原理是使用一个`setTimeout`，异步执行回调。这个`debounce`至少有两个问题：

+ 延迟时间我们没法控制，400ms是写死的，因此复用就变得困难；

+ 给method添加了tId属性修改了我们的原始方法，产生了副作用。当然最主要的问题还是它不能适应需求的变化。

那么有没有更好的办法呢？这里我提供了一种更优雅的解决方案。直接从 lodash-es 中引入 debounce，将原来的回调函数 print 作为 debounce 的第一个参数，在原本的回调函数替换为 debounce，仅此而已，我们就实现了上一步中同样的效果，并且更具扩展性。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29f9979da7834210849a2e1e5da52d4f~tplv-k3u1fbpfcp-watermark.image)

**lodash里提供的throttle和debounce**

lodash 提供了`debounce`和`throttle`两个方法。先来看看文档上是如何描述这两个方法的：
+ throttle **创建一个节流函数**，在 `wait` 毫秒内最多执行 `func` 一次；
+ debounce **创建一个防抖函数**，该函数会从上一次被调用后，延迟 `wait` 毫秒后调用 `func` 。
可能大家觉得文档很枯燥，那我们就来看看它们是怎么使用的。

**使用debounce**

首先，定义一个doAjax的方法，这个方法的作用是执行一个ajax请求，从服务器请求我们需要的数据；第二步，我们给button绑定一个点击（click）事件，我们在callback里调用debounced函数。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e9d8e6af46645ef99bfed8cd1e06c7d~tplv-k3u1fbpfcp-watermark.image)

预期本是第一次点击以后延迟 300ms 在控制台打印出 you clicked，我们可以发现，结果并没有按照预期执行。原因是什么呢？再次回到文档，文档里说的是 **创建一个防抖函数**，也就是说debounce返回的是一个函数，因此，正确的使用方法是这样的。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00ac94b9135a4d8b859a0115c47f0343~tplv-k3u1fbpfcp-watermark.image)

修改以后，执行的结果就符合预期了。接下来我们通过一个动画，来看一下debounce的执行细节。

![ezgif-3-0801903fb33d.gif](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cf8ede8cb8f49ccbaea7885f914a3ad~tplv-k3u1fbpfcp-watermark.image)


这个动画由3部分组成，分别是 “触发区域”、”原生事件” 和 “防抖处理后的事件”，竖线分割的小格子代表100ms，每一个色块代表在该时间段内触发了事件，当我们连续不断的触发事件的时候，“原生事件”一直在触发，而“防抖处理后的事件”在我们停止触发后400ms才执行。反复执行该动画，直到我们了解了细节。接下来我们再看一下debounce的细节。

debounce接受3个参数，第一个callback是必填的，wait和option是可选的，但是，可选参数都是有默认值的。我们依次来看一下这些参数的含义：

- func需要防抖的函数，也就是我们原本直接放在callback位置的函数；
- wait需要延迟的毫秒数，默认值是0，如果我们用debounce包装了func，但是没有指定wait，就相当于我们把func变成了一个异步函数；
- option.leading指定延迟开始的时候是否调用，通过我们刚才的测试，它的默认值是false；
- option.trailing指定延迟结束的时候是否调用，默认值是true；
- option.maxWait允许被延迟的最大值，如果我们指定这个值以后，当到达maxWait以后我们的func会被调用；

这些参数里我们注意一下option.maxWait，本质上来说，当我们设置了option.maxWait的时候，debounce就和throttle一样了。接下来我们从throttle的源码的角度来验证这个说法。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9b242d4294b4c46849c2b0885c6f315~tplv-k3u1fbpfcp-watermark.image)

throttle的核心代码就20几行，我们看到第一行就是引入了debounce函数，再看到16行，把throttle函数的wait参数赋值给了debounce的maxWait，这个操作是不是很熟悉，给debounce设置maxWait参数。至少从源代码层面来说这两个函数的关系非同一般。

既然，throttle是debounce的套壳，那么接下来我们先别管他们的区别，继续看看它们的使用，接下来都用debounce来解释。

**给debounce传参**

如果我们的func需要传递参数，通过debounce包装以后怎么传递参数呢？很简单，只需要把需要的参数传递给`debounce()`调用后返回的函数就可以了。如果是多个参数，还是同样的，使用剩余参数`func(...arg)`的方式接收，就可以把所有的参数都接收下来了。

说一点儿题外话，如果你使用别人提供函数，比如一些第三方库，没办法修改源代码，这时候又想传递参数，一个最简单的方法就是使用闭包。提醒一下，按需使用闭包。

**一张图总结**

这两个函数的使用都介绍的差不多了，我们用一张图来总结一下。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb772bd4e8c545e78508d246e7195bbb~tplv-k3u1fbpfcp-watermark.image)

第一行是原生事件，只要触发回调函数就会不停的执行，祸乱之源！

第二行throttle的默认行为，我们可以看到最开始，和结束都有函数调用，中间过程是间隔开的。函数调用减少了75%。

第三行和第二行的区别是结束的时候少了一次函数调用，只是因为我们设置了option.trailing = false这种情况我倒是没有想到应用场景。

第四行和第二行的区别是开始的时候少了一次函数调用，原因也是设置了option.leading = false

当然我们要是把trailing = leading = false必然是既没有头也没有尾了。

第五行是debounce的默认行为，在连续的事件触发停止200ms后执行回调函数；

第六行我们把leading设置为了true，trailing设置位false，一开始就执行了一次回调函数，没有任何延迟，结尾的时候没有执行回调函数。

第七行我们把leading设置为了true，trailing设置位true，也是一开始就执行了一次回调函数，没有任何延迟，结尾的时候也执行了回调函数。

最后一行，是不是和第四行的行为很类似，如果我们把 maxWait 改为 200ms 他们就是一摸一样的了，这也和我们刚才分析的源码的预期结果一致。

**辨析区别**

用一个更形象的方式来总结一下这两个方法的区别：

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c66ce218b4a4e2a9be6d3566bc46ad7~tplv-k3u1fbpfcp-watermark.image)

throttle的行为就像地铁，不管上了多少人，什么时候上的，时间一到就按时发车。

debounce就像电梯，第一个人进去以后，如果在10s（假设值）内有人进来，电梯又要等10s才关门，以次类推。直到电梯装满，人们都主动等下一趟了，电梯才会关门。通过以上的介绍我们已经掌握了这两个函数的使用和区别，现在我们再来区分一下他们的应用场景。

## 应用场景

这里我只是按照我个人的经验做的总结和区分，实际情况千变万化，大家根据项目需求合理的取用。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28818d0dd3f442e1a229c89fc0b8d61d~tplv-k3u1fbpfcp-watermark.image)

click事件我们最常见的就是异步请求一个后台接口，通常我们都只需要执行一次，频繁的执行，响应都是相同的数据没有意义，同时也增加了服务器的压力。这种情况最适合的就是debounce函数;

scroll事件如果是触发UI的变化呢，我建议使用throttle。如果是，通过scroll事件加载数据呢则可以使用debounce函数。总之按需取用。

resize事件就推荐debounce了，一般情况下只需要在resize结束的时候执行一次回调函数就满足需求了，但是也不是绝对的情况。如果要保持UI的连续性也可以使用throttle函数。

mousemove事件一般都是配合UI的改变，因此推荐使用throttle。

现在看一下细分的情况；

滚动加载我们也是在滚动到底部的时候才去加载一次数据，多余的加载都是没有意义的，而且有可能出错，因此使用debounce。

搜索框那就推荐使用throttle了，在合适的间隔去请求搜索结果，既提高了用户体验，又减少了服务器的压力。

以上这些都是我总结的常用的场景，大家也可以根据实际的使用场景合理的选用。

## 实际应用案例展示

接下来我们看一个实际的应用案例。“自定义vue指令实现防止按钮连续点击”在我们不使用任何辅助函数的情况下，设想一下代码应该是这样的：设置了一个isDisabled = false来控制按钮的状态，点击按钮后修改isDisabled = true禁用按钮，等ajax resolve以后恢复设置isDisabled = false恢复按钮的状态。

这样确实能满足我们的需求。但是我们有没有更好的办法呢？答案是有的！我开发了一个Vue插件 **[v-pfc](https://www.npmjs.com/package/vuepfc)**，就是使用了debounce来阻止了多余的请求，再也不怕用户连续点击了。当我们使用v-pfc以后我们的代码变成了这样。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7484b9ef28b94ad7a4475848b21ea8ee~tplv-k3u1fbpfcp-watermark.image)

最明显的变化是少了一个flag。用的同学可能会觉得，费了那么多劲就少了一个flag完全没必要了，我用flag也很香啊。请大家想象一下这种情况：页面里有10个按钮，你是不是要定义10个flag呢？有没有要抓狂的感觉。

至此，我关于throttle和debounce的分享就结束了，不过还有一个one more thing再说一下。

如果我们把throttle的wait设置为16ms是不是和requestAnimationFrame很像了。在这篇文章中就不展开讲了，更多的介绍大家可以去搜索一下。

**总结一下rAF**
1. 用于优化事件处理
2. 相似但是又不完全相同
3. requestAnimationFrame提供比throttle更流畅的动画体验

## 总结
throttle和debounce相似但又不尽相同，它们在不同的使用场景发光发热。

## 参考资料
+ Debouncing and Throttling Explained Through Examples ：https://css-tricks.com/debouncing-throttling-explained-examples/
+ The Difference Between Throttling and Debouncing ：https://css-tricks.com/the-difference-between-throttling-and-debouncing/
+ debounce文档：https://lodash.com/docs/4.17.15#debounce
+ throttle文档：https://lodash.com/docs/4.17.15#throttle
+ JavaScript 函数节流和函数去抖应用场景辨析 ：https://github.com/lessfish/underscore-analysis/issues/20
+ underscore 函数去抖的实现 ：https://github.com/lessfish/underscore-analysis/issues/21


感兴趣的小伙伴，欢迎前往联通ANOV沃云门户，了解开发手册以及培训视频等更多内容 https://anov.woyun.cn

![800.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aae85029e5a04bd2a2dee5cc56a41f86~tplv-k3u1fbpfcp-watermark.image)