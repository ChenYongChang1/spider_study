标题:如何实现一个 LazyMan？
描述:网上看到一道 JavaScript 笔试题，感觉还挺有意思的，在此记录一番。 下面是 ES6 的实现方式，如果用 ES5 来写要在维护 this 方面多写一些代码。 吐槽一下，最近想换工作，一直在准备面试，复习的时候感觉前端能考到的知识点真是多啊。

<p>网上看到一道 JavaScript 笔试题，感觉还挺有意思的，在此记录一番。</p>
<p>考察知识点：<strong>闭包</strong>，<strong>事件轮询机制</strong>，<strong>链式调用</strong>，<strong>队列</strong></p>
<pre><code class="hljs bash" lang="bash">实现一个LazyMan，可以按照以下方式调用:
LazyMan(“Hank”)输出:
Hi! This is Hank!

LazyMan(“Hank”).sleep(10).eat(“dinner”)输出
Hi! This is Hank!
//等待10秒..
Wake up after 10
Eat dinner~

LazyMan(“Hank”).eat(“dinner”).eat(“supper”)输出
Hi This is Hank!
Eat dinner~
Eat supper~

LazyMan(“Hank”).sleepFirst(5).eat(“supper”)输出
//等待5秒
Wake up after 5
Hi This is Hank!
Eat supper
以此类推。
</code></pre><p>下面是 ES6 的实现方式，如果用 ES5 来写要在维护 <code>this</code> 方面多写一些代码。</p>
<pre><code class="hljs bash" lang="bash">class _LazyMan {
  constructor(name) {
    this.tasks = [];
    const task = () =&gt; {
      console.log(`Hi! This is <span class="hljs-variable">${name}</span>`);
      this.next();
    }
    this.tasks.push(task);
    <span class="hljs-built_in">set</span>Timeout(() =&gt; {               // 把 this.next() 放到调用栈清空之后执行
      this.next();
    }, 0);
  }

  <span class="hljs-function"><span class="hljs-title">next</span></span>() {
    const task = this.tasks.shift(); // 取第一个任务执行
    task &amp;&amp; task();
  }

  sleep(time) {
    this._sleepWrapper(time, <span class="hljs-literal">false</span>);
    <span class="hljs-built_in">return</span> this;                     // 链式调用
  }

  sleepFirst(time) {
    this._sleepWrapper(time, <span class="hljs-literal">true</span>);
    <span class="hljs-built_in">return</span> this;
  }

  _sleepWrapper(time, first) {
    const task = () =&gt; {
      <span class="hljs-built_in">set</span>Timeout(() =&gt; {
        console.log(`Wake up after <span class="hljs-variable">${time}</span>`);
        this.next();
      }, time * 1000)
    }
    <span class="hljs-keyword">if</span> (first) {
      this.tasks.unshift(task);     // 放到任务队列顶部
    } <span class="hljs-keyword">else</span> {
      this.tasks.push(task);        // 放到任务队列尾部
    }
  }

  eat(name) {
    const task = () =&gt; {
      console.log(`Eat <span class="hljs-variable">${name}</span>`);
      this.next();
    }
    this.tasks.push(task);
    <span class="hljs-built_in">return</span> this;
  }
}

<span class="hljs-keyword">function</span> LazyMan(name) {
  <span class="hljs-built_in">return</span> new _LazyMan(name);
}
</code></pre><p>吐槽一下，最近想换工作，一直在准备面试，复习的时候感觉前端能考到的知识点真是多啊。</p>
<p>参考：
https://zhuanlan.zhihu.com/p/22387417</p>
