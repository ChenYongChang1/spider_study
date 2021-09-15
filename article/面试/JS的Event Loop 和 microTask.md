标题:JS的Event Loop 和 microTask
描述:上面问题的答案，都在文章《Tasks, microtasks, queues and schedules》讲的非常透彻。 建议英文可以的同学直接看这篇文章，就不要看我这个“笔记”了。( 之所以叫笔记，因为大部分内容出自文章，但是又不是按字翻译 ) 问题来了，为什么promise…

<blockquote>
<p>面试和笔试题目中，经常会出现'promise','setTimeout'等函数混合出现时候的运行顺序问题。 我们都知道这些异步的方法会在当前任务执行结束之后调用，但为什么'promise'会在'setTimeout'之前执行？ 具体的实现原理是什么？</p>
</blockquote>
<p>有和我一样正在为秋招offer奋斗的小伙伴，欢迎到github获取更多我的总结和踩过的坑，一起进步→→→→<a target="_blank" href="https://github.com/forrany/Web-Project">传送门</a></p>
<h2 class="heading">问题的提出</h2>
<p>上面问题的答案，都在文章<a target="_blank" href="https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/?utm_source=html5weekly">《Tasks, microtasks, queues and schedules》</a>讲的非常透彻。 建议英文可以的同学直接看这篇文章，就不要看我这个“笔记”了。( <em>之所以叫笔记，因为大部分内容出自文章，但是又不是按字翻译</em> )</p>
<p>以下的题目是我们刷题可以经常看到的一个常规题目：</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script start'</span>);

setTimeout(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>{
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>);
}, <span class="hljs-number">0</span>);

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>{
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise1'</span>);
}).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>{
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise2'</span>);
});

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'script end'</span>);
</code></pre><p>几乎每个前端er都可以毫不犹豫的给出答案:</p>
<pre><code class="hljs javascript" lang="javascript">script start
script end
promise1
promise2
setTimeout
</code></pre><p>问题来了，为什么<code>promise</code>的异步执行会在<code>setTimeout</code>之前，甚至<code>setTimeout</code>设置的延时是0都不行。 还有在Vue中，我们常用的nextTick()函数原理中，说的microtasks是什么东西？ 一切的解释都在开头给的文章中。</p>
<p>ps： 再次再次声明，这篇文章仍然是我记得笔记，原文比我写的好得多，英文可以的小伙伴强烈推荐看原文。</p>
<h2 class="heading">js异步实现原理</h2>
<p>我们多多少少都应该听说过event loop，js是单线程的，通过异步它变得非常强大，而实现异步主要就是通过将异步的内容压入tasks，当前任务执行结束之后，再执行tasks中的callback。</p>
<p><strong>Tasks</strong>，是一个任务队列，Js在执行同步任务的时候，只要遇到了异步执行和函数，都会把这个内容压入Tasks中，然后在当前同步任务完成后，再去Tasks中执行相应的回调。 举个例子，比如刚才代码中的<code>setTimeout</code>，当遇到这个函数，总会跟一个异步执行的任务(callback)，那么这个时候，Tasks队列里，除了当前正在执行的script之外，会在后面压入一个<code>setTimeout callback</code>， 而这个callback的调用时机，就是在当前同步任务完成之后，才会调用。这就是为什么,'setTimeout' 会出现在'script end'之后了。</p>
<p><strong>MicroTasks</strong>，说一些这个，这个和<code>setTimeout</code>不同，因为它是在当前Task完成后，就立即执行的，或者可以理解成，'microTasks总是在当前任务的最后执行'。  另外，还有一个非常重要的特性是： <strong>如果当前JS stack如果为空的时候(比如我们绑定了click事件后，等待和监听click时间的时候，JS stack就是空的),一会立即执行。</strong> 关于这一点，之后有个例子会具体说明，先往下看。</p>
<p>那么MicroTasks队列主要是promise和mutation observer 的回掉函数生成</p>
<h3 class="heading">用新的理论来解释下</h3>
<p>好了，刚才大概说了几个概念，那么一开始的例子，到底发生了什么？</p>
<p><code>talk is cheap, show me a animation!!</code>---我自己说的</p>
<p>下面的<a target="_blank" href="https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/?utm_source=html5weekly">动画</a>说明对整个过程进行了说明:</p>
<p></p><figure><img alt="原文中的动态演示" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/8/5/1650827c4eb4d2a5~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>1、 程序执行  <code>log: script start</code></p>
<ul>
<li>Tasks: Run script</li>
<li>JS stack: script</li>
</ul>
<p>2、 遇到setTimeout  <code>log: script start</code></p>
<ul>
<li>Tasks： Run script | setTimeout callback</li>
<li>JS stack: script</li>
</ul>
<p>3、 遇到Promise</p>
<ul>
<li>Tasks: Run script | setTimeout callback</li>
<li>Microtasks: promise then</li>
<li>JS stack: script</li>
</ul>
<p>4、 执行最后一行 <code>log: script start | script end</code></p>
<ul>
<li>Tasks: Run script | setTimeout callback</li>
<li>Microtasks: promise then</li>
<li>JS stack: script</li>
</ul>
<p>4、 同步任务执行完毕，弹出相应的stack <code>log: script start | script end</code></p>
<ul>
<li>Tasks: Run script | setTimeout callback</li>
<li>Microtasks: promise then</li>
<li>JS stack:</li>
</ul>
<p>5、 同步任务最后是microTasks，JS stack压入callback <code>log: script start | script end | promise1</code></p>
<ul>
<li>Tasks: Run script | setTimeout callback</li>
<li>Microtasks: promise then | promise then</li>
<li>JS stack: promise1 calback
6、 promise返回新的promise，压入microTasks，继续执行 <code>log: script start | script end | promise1 | promise2</code></li>
<li>Tasks: Run script | setTimeout callback</li>
<li>Microtasks:  promise then</li>
<li>JS stack: promise2 calback</li>
</ul>
<p>8、 第一个Tasks结束,弹出 <code>log: script start | script end | promise1 | promise2</code></p>
<ul>
<li>Tasks: setTimeout callback</li>
<li>Microtasks:</li>
<li>JS stack:</li>
</ul>
<p>9、 下一个Tasks <code>log: script start | script end | promise1 | promise2 | setTimeout</code></p>
<ul>
<li>Tasks: setTimeout callback</li>
<li>Microtasks:</li>
<li>JS stack: setTimeout callback</li>
</ul>
<p>好了，结束了，这就比之前的理解"promise比setTimeout快，异步先执行promise，再执行setTimeout"就深刻的多。 因为promise所建立的回掉函数是压入了<code>mircroTasks</code>队列中，它仍然属于当前的Task，而<code>setTimeout</code>则是相当于在Task序列中添加了新的任务</p>
<h2 class="heading">一个更复杂的例子</h2>
<p>好了，有了刚才的认识和铺垫，接下来通过一个更加复杂的例子来熟悉JS事件处理的一个过程。</p>
<p>现在有这样一个页面结构：</p>
<pre><code class="hljs html" lang="html"><span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"outer"</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"inner"</span>&gt;</span><span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-name">div</span>&gt;</span>

</code></pre><p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/8/5/1650914100613dfd~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
js代码如下,现在如果点击里面的方块，控制台会输出什么呢？<a target="_blank" href="https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/?utm_source=html5weekly">在线实例</a><p></p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// Let's get hold of those elements</span>
<span class="hljs-keyword">var</span> outer = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.outer'</span>);
<span class="hljs-keyword">var</span> inner = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.inner'</span>);

<span class="hljs-comment">// Let's listen for attribute changes on the</span>
<span class="hljs-comment">// outer element</span>
<span class="hljs-keyword">new</span> MutationObserver(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>{
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mutate'</span>);
}).observe(outer, {
  <span class="hljs-attr">attributes</span>: <span class="hljs-literal">true</span>
});

<span class="hljs-comment">// Here's a click listener…</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onClick</span>(<span class="hljs-params"></span>) </span>{
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'click'</span>);

  setTimeout(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>{
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timeout'</span>);
  }, <span class="hljs-number">0</span>);

  <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>{
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'promise'</span>);
  });

  outer.setAttribute(<span class="hljs-string">'data-random'</span>, <span class="hljs-built_in">Math</span>.random());
}

<span class="hljs-comment">// …which we'll attach to both elements</span>
inner.addEventListener(<span class="hljs-string">'click'</span>, onClick);
outer.addEventListener(<span class="hljs-string">'click'</span>, onClick);
</code></pre><p>这里先把正确答案公布，按照之前的理论，正确答案应该是：</p>
<pre><code class="hljs javascript" lang="javascript">click
promise
mutate
click
promise
mutate
timeout
timeout
</code></pre><p>当然，不同浏览器，对于event loop的实现会稍有不同，这个是chrome下打印出来的结果，具体的其他形式还是推荐大家看原文了。</p>
<p>下面分析下，为什么是上面的顺序呢？</p>
<h3 class="heading">代码分析</h3>
<p>按照刚才的结论：</p>
<p>click事件显然是一个Task，Mutation observer和Promise是在microTasks队列中的，而setTimeout会被安排在Tasks之中。 因此</p>
<p>1、点击事件触发</p>
<ul>
<li>Tasks: Dispatch click</li>
<li>Microtasks:</li>
<li>JS stack:</li>
</ul>
<p>2、触发点击事件的函数，函数执行，压入JS stack</p>
<ul>
<li>Tasks: Dispatch click</li>
<li>Microtasks:</li>
<li>JS stack: onClick</li>
<li>Log: 'click'</li>
</ul>
<p>3、遇到setTimeout，压入Tasks队列</p>
<ul>
<li>Tasks: Dispatch click | setTimeout callBack</li>
<li>Microtasks:</li>
<li>JS stack: onClick</li>
<li>Log: 'click'</li>
</ul>
<p>4、遇到promise，压入Microtasks</p>
<ul>
<li>Tasks: Dispatch click | setTimeout callBack</li>
<li>Microtasks: Promise.then</li>
<li>JS stack: onClick</li>
<li>Log: 'click'</li>
</ul>
<p>5、遇到 outer.setAttribute，触发mutation</p>
<ul>
<li>Tasks: Dispatch click | setTimeout callBack</li>
<li>Microtasks: Promise.then | Mutation observers</li>
<li>JS stack: onClick</li>
<li>Log: 'click'</li>
</ul>
<p>6、onclick函数执行完毕，出JS stack</p>
<ul>
<li>Tasks: Dispatch click | setTimeout callBack</li>
<li>Microtasks: Promise.then | Mutation observers</li>
<li>JS stack:</li>
<li>Log: 'click'</li>
</ul>
<p>7、这个时候，JS stack为空，执行Microtasks</p>
<ul>
<li>Tasks: Dispatch click | setTimeout callBack</li>
<li>Microtasks: Promise.then | Mutation observers</li>
<li>JS stack: PromiseCallback</li>
<li>Log: 'click' 'promise'</li>
</ul>
<p>8、microtasks顺序执行</p>
<ul>
<li>Tasks: Dispatch click | setTimeout callBack</li>
<li>Microtasks:  Mutation observers</li>
<li>JS stack: Mutation callback</li>
<li>Log: 'click' 'promise' 'mutate'</li>
</ul>
<p>接下来是重点，当microtasks为空，该执行下一个Tasks(setTimeout)了吗？并没有，因为js事件流中的冒泡被触发，也就是在外面的一层Div也会触发click函数，因此我们把刚才的步骤再走一遍。</p>
<p>过程省略，结果为
9、冒泡走一遍的结果为</p>
<ul>
<li>Tasks: Dispatch click | setTimeout callBack | setTmeout callback(outer)</li>
<li>Microtasks:  Mutation observers</li>
<li>JS stack: Mutation callback</li>
<li>Log: <code>click</code> <code>promise</code> <code>mutate</code> <code>click</code>  <code>promise</code> <code>mutate</code></li>
</ul>
<p>10、 第一个Tasks完成，出栈</p>
<ul>
<li>Tasks: setTimeout callBack | setTmeout callback(outer)</li>
<li>Microtasks:</li>
<li>JS stack: setTimeout callback</li>
<li>Log: <code>click</code> <code>promise</code> <code>mutate</code> <code>click</code>  <code>promise</code> <code>mutate</code> <code>timeout</code></li>
</ul>
<p>11、 第二个Tasks完成，出栈</p>
<ul>
<li>Tasks: setTmeout callback(outer)</li>
<li>Microtasks:</li>
<li>JS stack: setTimeout(outer) callback</li>
<li>Log: <code>click</code> <code>promise</code> <code>mutate</code> <code>click</code>  <code>promise</code> <code>mutate</code> <code>timeout</code> <code>timeout</code></li>
</ul>
<p>结束了</p>
<p>所以这里的重点是什么？ 是<strong>MicroTasks的执行时机： 见缝插针，它不一定就必须在Tasks的最后，只要JS stack为空，就可以执行</strong>  这条规则出处在</p>
<blockquote>
<p>If the stack of script settings objects is now empty, perform a microtask checkpoint<br>
— HTML: Cleaning up after a callback step 3</p>
</blockquote>
<p>另一方面，ECMA也对此有过说明</p>
<blockquote>
<p>Execution of a Job can be initiated only when there is no running execution context and the execution context stack is empty…<br>
— ECMAScript: Jobs and Job Queues</p>
</blockquote>
<p><strong>但是对于其他浏览器(firefox  safari ie)同样的代码，得出的结果是不同的哦。关键在于，对与 <code>job</code>和<code>microTasks</code>之间的一个联系是很模糊的。  但是我们就按照Chrome的实现来理解吧。</strong></p>
<h3 class="heading">最后一关</h3>
<p>还是刚才那道题，只不过，我不用鼠标点击了，而是直接执行函数</p>
<pre><code class="hljs javascirpt" lang="javascirpt">inner.click()
</code></pre><p>如果这样，结果会一样吗？</p>
<p>答案是:</p>
<pre><code class="hljs javascript" lang="javascript">click
click
promise
mutate
promise
timeout 
timeout
</code></pre><p>What！！？？我怎么感觉我白学了？ 不着急，看下这次的过程是这样的，首先最大的不同在于，我们在函数最底部加了一个执行<code>inner.click()</code>，这样子，这个函数执行的过程，都是同步序列里的，所以这次的task的起点就在Run scripts:</p>
<p>1、不同与鼠标点击，我们执行函数后，进入函数内部执行</p>
<ul>
<li>Tasks: Run scripts</li>
<li>Microtasks:</li>
<li>JS stack: script | onClick</li>
<li>Log: <code>click</code></li>
</ul>
<p>2、遇到setTimeout和promise&amp;mutation</p>
<ul>
<li>Tasks: Run scripts | setTimeout callback</li>
<li>Microtasks: Promise.then | Mutation Observers</li>
<li>JS stack: script | onClick</li>
<li>Log: <code>click</code></li>
</ul>
<p>3、接下来关键，冒泡的时候，因为我们并没有执行完当前的script,还在<code>inner.click()</code>这个函数执行之中，因此当<code>onclick</code>结束，开始冒泡时，script并没有结束</p>
<ul>
<li>Tasks: Run scripts | setTimeout callback</li>
<li>Microtasks: Promise.then | Mutation Observers</li>
<li>JS stack: script | onClick(这是冒泡的click，第一次click已经结束)</li>
<li>Log: <code>click</code> <code>click</code></li>
</ul>
<p>4、冒泡阶段重复之前内容</p>
<ul>
<li>Tasks: Run scripts | setTimeout callback |setTimeout callback(outer)</li>
<li>Microtasks: Promise.then | Mutation Observers |promise.then</li>
<li>JS stack: script | onClick(这是冒泡的click，第一次click已经结束)</li>
<li>Log: <code>click</code> <code>click</code></li>
</ul>
<p>注意第二次没有增加mutation，因为已经有一个在渲染的了</p>
<p>5、inner.click()执行完毕,执行Microtasks</p>
<ul>
<li>Tasks: Run scripts | setTimeout callback |setTimeout callback(outer)</li>
<li>Microtasks: Promise.then | Mutation Observers |promise.then</li>
<li>JS stack:</li>
<li>Log: <code>click</code> <code>click</code> <code>promise</code></li>
</ul>
<p>6、按理论执行</p>
<ul>
<li>Tasks: Run scripts | setTimeout callback |setTimeout callback(outer)</li>
<li>Microtasks: Mutation Observers |promise.then</li>
<li>JS stack:</li>
<li>Log: <code>click</code> <code>click</code> <code>promise</code> <code>mutate</code>....</li>
</ul>
<p>后面的就不解释了，Microtasks依次出栈，接着Tasks顺序执行。</p>
<h2 class="heading">总结</h2>
<p>Jake老师的文章，对这个的解析和深入实在令人佩服，我也在面试中因把event loop解释的较为详尽而被面试官肯定，所以如果对异步以及event loop有疑惑的，可以好好的消化下这个内容，一起进步!</p>
