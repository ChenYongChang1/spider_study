标题:《前端面试总结点线面》之点-CS篇
描述:本文不成文，谨慎阅读。 《前端面试总结点线面》系列是为了收拢杂而乱的前端领域知识，由点及线，再涉及面，目的是为帮助广大前端同学复习巩固或查漏补缺或增删改查，为了更好的建立前端领域知识体系，为了更好的为前端面试做好准备，从而做一个合格、进步的前端开发工程师。 并发 - 同时进行多…

<p><strong>特别提示：</strong>
本文不成文，谨慎阅读。</p>
<p>《前端面试总结点线面》系列是为了收拢杂而乱的前端领域知识，由点及线，再涉及面，目的是为帮助广大前端同学复习巩固或查漏补缺或增删改查，为了更好的建立前端领域知识体系，为了更好的为前端面试做好准备，从而做一个合格、进步的前端开发工程师。</p>
<ul>
<li><a href="#cs">CS</a>
<ul>
<li><a href="#%E8%BF%9B%E7%A8%8B--%E7%BA%BF%E7%A8%8B">进程 🆚 线程</a>
<ul>
<li><a href="#%E8%BF%9B%E7%A8%8B%E9%97%B4%E9%80%9A%E4%BF%A1">进程间通信</a></li>
<li><a href="#%E7%BA%BF%E7%A8%8B%E9%97%B4%E9%80%9A%E4%BF%A1">线程间通信</a></li>
<li><a href="#%E5%8D%8F%E7%A8%8B">协程</a></li>
</ul>
</li>
<li><a href="#%E4%BA%8B%E5%8A%A1">事务</a></li>
<li><a href="#%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F">设计模式</a>
<ul>
<li><a href="#%E8%A7%82%E5%AF%9F%E8%80%85%E6%A8%A1%E5%BC%8F--%E5%8F%91%E5%B8%83-%E8%AE%A2%E9%98%85%E8%80%85%E6%A8%A1%E5%BC%8F">观察者模式 🆚 发布-订阅者模式</a></li>
</ul>
</li>
<li><a href="#%E7%AE%97%E6%B3%95">算法</a>
<ul>
<li><a href="#dfs--bfs">DFS 🆚 BFS</a>
<ul>
<li><a href="#%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2-depth-first-search">深度优先搜索 Depth-First-Search</a></li>
<li><a href="#%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2-breadth-first-search">广度优先搜索 Breadth-First-Search</a></li>
</ul>
</li>
<li><a href="#%E6%8E%92%E5%BA%8F">排序</a></li>
<li><a href="#%E5%9F%BA%E6%9C%AC%E7%AE%97%E6%B3%95">基本算法</a></li>
<li><a href="#%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">正则表达式</a></li>
<li><a href="#%E9%97%AE%E9%A2%98">问题</a></li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 class="heading">CS</h1>
<h2 class="heading">进程 🆚 线程</h2>
<ul>
<li>进程是一个动态的过程，是一个活动的实体</li>
<li>进程是操作系统进行资源分配和调度的最小单元</li>
<li>线程是程序执行流的最小单元</li>
<li>一个进程由一个或多个线程组成，线程是一个进程中代码的不同执行路线</li>
<li>进程之间相互独立，线程之间共享内存空间</li>
<li>调度和切换：线程上下文切换比进程切换快得多</li>
</ul>
<p>单线程 - 顾名思义只有一条线程在执行任务</p>
<p>多线程 - 创建多条线程同时执行任务</p>
<p>并发 - 同时进行多种时间，这几种时间并不是同时进行的，而是交替进行的。</p>
<p>并行 - 同时进行多种事情</p>
<p><strong>线程间共享</strong> 堆地址空间，全局变量
<strong>线程独享</strong> 栈，寄存器，程序计数器</p>
<p><strong>线程状态：</strong></p>
<ol>
<li>新创建 New</li>
<li>就绪状态 Runnable</li>
<li>运行状态 Running</li>
<li>阻塞状态 Blocked</li>
<li>死亡状态 Dead</li>
</ol>
<p><strong>进程调度</strong></p>
<p></p><figure><img alt="进程调度" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/21/16deecc24dfd080c~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<ol>
<li>先到先得 FCFS</li>
<li>轮转</li>
<li>最短进程优先</li>
<li>最短剩余时间</li>
<li>最高响应比优先</li>
<li>反馈法</li>
</ol>
<h4 class="heading">进程间通信</h4>
<ol>
<li>无名管道：半双工通信方式，数据只能单向流动，且只能在具有亲缘关系的进程间（父子通信）。</li>
<li>命名管道： 半双工通信方式，允许没有亲缘关系的进程通信</li>
<li>消息队列：消息队列是有消息的链表，存放在内核中，并由消息队列标识符标识，消息队列克服了信号传递信息少，管道只能承载无格式字节流以及缓冲区大小受限的缺点</li>
<li>共享内存（shared memory）：共享内存就是映射一段能被其他进程所访问的内存，这段共享内存由一个进程创建，但多个进程都可以访问。共享内存是最快的 ipc 通信方式，它是针对其他进程间通信方式运行效率低而专门设计的。它往往和其他通信方式如信号量，配合使用来实现进程间的同步和通信。</li>
<li>信号（sinal）：信号是一种比较复杂的通信方式，用于通知接受进程某个事件已经发生。</li>
<li>信号量（semophonre）：信号量是一个计数器，可以用来控制多个进程队共享资源的访问。它常作为一个锁机制，防止某进程在访问共享资源时，其他进程也访问此资源。因此，主要作为进程间以及同一进程内不同线程之间的同步手段。</li>
<li>套接字（socket）：套接字也是一种进程间通信机制，与其他通信机制不同的是，它可用于不同设备间的进程通信。</li>
<li>全双工管道：共享内存、信号量、消息队列、管道和命名管道只适用于本地进程间通信，套接字和全双工管道可用于远程通信，因此可用于网络编程。</li>
</ol>
<h4 class="heading">线程间通信</h4>
<ul>
<li>锁机制：包括互斥锁、条件变量、读写锁
<ul>
<li>互斥锁：提供以排他方式防止数据结构被并发修改的方法</li>
<li>读写锁：允许多个线程同时共享数据，而对写操作互斥。</li>
<li>条件变量：可以以原子的方式阻塞进程，直到某个特定条件为真为止。对条件的测试是在互斥锁的保护下进行的。条件变量始终与互斥锁一起使用。</li>
</ul>
</li>
<li>信号量机制（Semaphore）：包括无名进程信号量和命名线程信号量</li>
<li>信号机制（Signal）：类似进程间的信号处理</li>
</ul>
<h3 class="heading">协程</h3>
<blockquote>
<p>协程是管理子程序的暂停（悬挂）和恢复来实现非抢占式多任务处理的计算机程序</p>
</blockquote>
<p>协程就是主程序管理子程序调用（call）和让出（yield）来决定当前的运行时来处理哪些部分：资源让出的时候，当前子程序挂起，等到资源被释放回来的时候，又恢复执行，从而通过合理使用资源实现了多任务处理</p>
<h2 class="heading">事务</h2>
<blockquote>
<p>事务是逻辑上的一组操作，要么都执行，要么都不执行。</p>
</blockquote>
<p><strong>事务的特性：</strong></p>
<ol>
<li>原子性</li>
<li>一致性</li>
<li>隔离性</li>
<li>持久性</li>
</ol>
<h2 class="heading">设计模式</h2>
<ol>
<li>外观模式
<blockquote>
<p>它为子系统的一组接口提供一个统一的高层接口，使子系统更容易使用，也就是把多个子系统中复杂逻辑进行抽象，从而提供一个更统一、更简洁、更易用的 API</p>
</blockquote>
</li>
</ol>
<pre><code class="hljs bash" lang="bash">// 绑定事件
<span class="hljs-keyword">function</span> addEvent(element, event, handler) {
  <span class="hljs-keyword">if</span> (element.addEventListener) {
    element.addEventListener(event, handler, <span class="hljs-literal">false</span>);
  } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (element.attachEvent) {
    element.attachEvent(<span class="hljs-string">'on'</span> + event, handler);
  } <span class="hljs-keyword">else</span> {
    element[<span class="hljs-string">'on'</span> + event] = fn;
  }
}

// 取消绑定
<span class="hljs-keyword">function</span> removeEvent(element, event, handler) {
  <span class="hljs-keyword">if</span> (element.removeEventListener) {
    element.removeEventListener(event, handler, <span class="hljs-literal">false</span>);
  } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (element.detachEvent) {
    element.detachEvent(<span class="hljs-string">'on'</span> + event, handler);
  } <span class="hljs-keyword">else</span> {
    element[<span class="hljs-string">'on'</span> + event] = null;
  }
}
</code></pre><ol start="2">
<li>
<p>代理模式</p>
<ul>
<li>增加对一个对象的访问控制</li>
<li>当访问一个对象的过程中需要添加额外的控制</li>
</ul>
</li>
<li>
<p>工厂模式（Factory Pattern）</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> BMWCar(color) {
  this.color = color
  this.brand = <span class="hljs-string">'BMW'</span>
}
</code></pre></li>
<li>
<p>策略模式</p>
<blockquote>
<p>策略模式的定义：定义一系列的算法，把他们一个个封装起来，并且使他们可以相互替换。</p>
</blockquote>
<p>策略模式的目的就是将算法的使用算法的实现分离开来。
一个基于策略模式的程序至少由两部分组成。第一个部分是一组策略类（可变），策略类封装了具体的算法，并负责具体的计算过程。第二个部分是环境类 Context（不变），Context 接受客户的请求，随后将请求委托给某一个策略类。要做到这一点，说明 Context 中要维持对某个策略对象的引用。</p>
<pre><code class="hljs bash" lang="bash">/*策略类*/
 const levelOBJ = {
     <span class="hljs-string">"A"</span>: <span class="hljs-keyword">function</span>(money) {
         <span class="hljs-built_in">return</span> money * 4;
     },
     <span class="hljs-string">"B"</span> : <span class="hljs-keyword">function</span>(money) {
         <span class="hljs-built_in">return</span> money * 3;
     },
     <span class="hljs-string">"C"</span> : <span class="hljs-keyword">function</span>(money) {
         <span class="hljs-built_in">return</span> money * 2;
     }
 };
 /*环境类*/
 const calculateBouns =<span class="hljs-keyword">function</span>(level,money) {
     <span class="hljs-built_in">return</span> levelOBJ[level](money);
 };
 console.log(calculateBouns(<span class="hljs-string">'A'</span>,10000)); // 40000
</code></pre></li>
</ol>
<ol start="5">
<li>单例模式（Singleton Pattern）
<blockquote>
<p>单例模式的定义：保证一个类仅有一个实例，并提供一个访问它的全局访问点。实现的方法为先判断实例存在与否，如果存在则直接返回，如果不存在就创建了再返回，这就确保了一个类只有一个实例对象。
适用场景：一个单一对象。比如：弹窗，无论点击多少次，弹窗只应该被创建一次。</p>
</blockquote>
<pre><code class="hljs bash" lang="bash">class CreateUser{
  constructor(name) {
    this.name=name
    this.getName()
  }
  <span class="hljs-function"><span class="hljs-title">getName</span></span>() {
    <span class="hljs-built_in">return</span> this.name
  }
}
const SingleService = (<span class="hljs-function"><span class="hljs-title">function</span></span>(){
  <span class="hljs-built_in">let</span> instance = null
  <span class="hljs-built_in">return</span> <span class="hljs-keyword">function</span>(name) {
    <span class="hljs-keyword">if</span>(!instance) {
      instance = new CreateUser(name)
    }
    <span class="hljs-built_in">return</span> instance
  }
})()
</code></pre></li>
</ol>
<h3 class="heading">观察者模式 🆚 发布-订阅者模式</h3>
<p></p><figure><img alt="观察者模式 🆚 发布-订阅者模式" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2017/11/22/15fe1b1f174cd376~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>观察者模式：
</p><figure><img alt="观察者模式" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2017/11/22/15fe1b1f1797e09a~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>发布-订阅者：
</p><figure><img alt="发布-订阅者" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2017/11/22/15fe1b1f07c13719~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<ol>
<li>观察者模式中，观察者是知道 Subject，Subject 一直保持着对观察者进行记录。</li>
<li>发布-订阅者模式，发布者（Publisher）和订阅者（Subscriber）不知道对方的存在，只能通过消息代理通信。</li>
<li>发布-订阅者中，组件是松散耦合的，与观察者模式相反</li>
<li>观察者模式大多数是同步的，比如当时间触发，Subject 就会去调用观察者方法。发布订阅者通常通过消息队列异步处理。</li>
<li>观察者模式需要在单个应用程序地址空间中出现，而发布订阅者更像是交叉模式。</li>
</ol>
<pre><code class="hljs bash" lang="bash">// 发布订阅模式简单版
class Events {
  <span class="hljs-function"><span class="hljs-title">constructor</span></span>() {
    this.handlers = {};
    <span class="hljs-built_in">return</span> this;
  }
  on(eventName, callback) {
    <span class="hljs-keyword">if</span> (!this.handlers[eventName]) {
      this.handlers[eventName] = [];
    }
    this.handlers[eventName].push(callback);
  }
  off(eventName, callback) {
    <span class="hljs-keyword">if</span> (!this.handlers[eventName]) <span class="hljs-built_in">return</span>;
    this.handlers[eventName] = this.handlers[eventName].filter(
      (item) =&gt; item !== callback
    );
  }
  emit(eventName, ...rest) {
    <span class="hljs-keyword">if</span> (this.handlers[eventName]) {
      this.handlers[eventName].forEach((cb) =&gt; cb.apply(this. rest));
    }
  }
  once(eventName, callback) {
    <span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">fn</span></span>() {
      callback()
      this.off(eventName, callback)
    }
    this.on(eventName, fn)
  }
}
</code></pre><h2 class="heading">算法</h2>
<h3 class="heading">DFS 🆚 BFS</h3>
<h4 class="heading">深度优先搜索 Depth-First-Search</h4>
<blockquote>
<p>DFS 沿着树的深度遍历树的节点，尽可能深的搜索树的分之。当节点 v 的所有边都已被探寻过，将回溯到发现节点 v 的那条边的起始节点。这一过程一直进行到已探寻源节点到其他所有节点为止，，如果还有未被发现的节点，则选择其中一个未被发现的节点为源节点并重复以上操作，直到所有节点都被探寻完成。</p>
</blockquote>
<blockquote>
<p>简单的说，DFS 从图中的一个节点开始追溯，直到最后一个节点，然后回溯，继续追溯下一条路径，直到到达所有的节点，如此往复，直到没有路径为止。</p>
</blockquote>
<pre><code class="hljs bash" lang="bash">const deepTraversal = node =&gt; {
  <span class="hljs-built_in">let</span> nodes = []
  <span class="hljs-keyword">if</span>(node) {
    nodes.push(node)
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0, ilen = nodes.children; i &lt; ilen; i++) {
      nodes = [...nodes, deepTraversal(nodes.children[i])]
    }
  }
  <span class="hljs-built_in">return</span> nodes
}
</code></pre><h4 class="heading">广度优先搜索 Breadth-First-Search</h4>
<blockquote>
<p>从根节点开始，沿着图的宽度遍历节点，如果所有节点均被访问，则算法结束，BFS 同样属于盲目搜索，一般用队列结构实现。</p>
</blockquote>
<pre><code class="hljs bash" lang="bash">
const widthTraversal = node =&gt; {
  <span class="hljs-built_in">let</span> nodes = []
  <span class="hljs-built_in">let</span> queue = []
  <span class="hljs-keyword">if</span>(node) {
    queue.push(node)
    <span class="hljs-keyword">while</span>(queue.length) {
      <span class="hljs-built_in">let</span> head = queue.shift()
      nodes.push(head)
      const children = head.children
      <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0,ilen=children.length;i&lt;ilen;i++) {
        queue.push(children[i])
      }
    }
  }
  <span class="hljs-built_in">return</span> nodes
}
</code></pre><h3 class="heading">排序</h3>
<p></p><figure><img alt="时间复杂度" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/7/6/173246d0ac803214~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<pre><code class="hljs bash" lang="bash">const swap = (arr, i, j) =&gt; {
  [arr[i], arr[j]] = [arr[j], arr[i]]
}
</code></pre><ol>
<li>冒泡排序</li>
</ol>
<blockquote>
<p>通过相邻元素的比较和交换
平均 O(n2)
</p><figure><img alt="bubble sort" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/7/6/173246d0abf8cd5e~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
</blockquote>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> bubbleSort(arr) {
  const len = arr.length
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0; i &lt; len; i++) {
    <span class="hljs-built_in">let</span> mark = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> j = 0; j &lt; len - i - 1; j++) {
      <span class="hljs-keyword">if</span>(arr[i] &gt; arr[j+1]) {
        // [arr[i], arr[j+1]] = [arr[j+1], arr[i]]
        swap(arr, i, j+1)
        mark = <span class="hljs-literal">false</span>
      }
    }
    <span class="hljs-keyword">if</span>(mark) <span class="hljs-built_in">return</span>
  }
  <span class="hljs-built_in">return</span> arr
}
</code></pre><ol start="2">
<li>选择排序</li>
</ol>
<blockquote>
<p>每一个元素和他后面所有的元素进行比较和交换
平均 O(n2)
</p><figure><img alt="selection Sort" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/7/6/173246d0b1349f5a~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
</blockquote>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> selectionSort(arr) {
  <span class="hljs-built_in">let</span> len = arr.length
  <span class="hljs-built_in">let</span> minIndex = 0
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i &lt; len - 1;i++) {
    minIndex = i
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> j = i + 1; j &lt; len; j++) {
      <span class="hljs-keyword">if</span>(arr[minIndex] &gt; arr[j]) {
        minIndex = j
      }
    }
    // [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]]
    swap(arr, i, minIndex)
  }
  <span class="hljs-built_in">return</span> arr
}
</code></pre><ol start="3">
<li>插入排序</li>
</ol>
<blockquote>
<p>以第一个元素为有序数组，其后的元素通过在已有序的数组中找到合适的位置并插入
平均 O(n2)
</p><figure><img alt="insertSort" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/7/6/173246d0b0d7ce85~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
</blockquote>
<p>方法 1:</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> insertSort(arr) {
  <span class="hljs-built_in">let</span> len = arr.length
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 1; i &lt; len;i++) {
    <span class="hljs-built_in">let</span> temp = arr[i]
    <span class="hljs-built_in">let</span> j = i
    <span class="hljs-keyword">for</span>(;j&gt;0;j--) {
      <span class="hljs-keyword">if</span>(temp &gt; arr[j-1]) {
        <span class="hljs-built_in">break</span>;// 当前数大于前一个数，证明有序，退出循环
      }
      arr[j] = arr[j-1] // 将前一个数复制到后一个数上
    }
    arr[j]=temp // 找到考察的数应在的位置
  }
  <span class="hljs-built_in">return</span> arr
}
</code></pre><p>方法 2：</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> insertSort(arr){
  const len = arr.length
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 1; i &lt; len; i++) {
    <span class="hljs-built_in">let</span> j = i - 1
    <span class="hljs-built_in">let</span> temp = arr[i]
    <span class="hljs-keyword">while</span>(j&gt;=0&amp;&amp;temp&lt;arr[j]){
      arr[j+1]=arr[j]
      j--
    }
    arr[j+1]=temp
  }
  <span class="hljs-built_in">return</span> arr
}
</code></pre><ol start="4">
<li>希尔排序
<blockquote>
<p>希尔排序是插入排序的一种更高效率的实现。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。
O(nlogn)</p>
</blockquote>
</li>
</ol>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> shellSort(nums) {
  <span class="hljs-built_in">let</span> len = nums.length;
  // 初始步数
  <span class="hljs-built_in">let</span> gap = parseInt(len / 2);
  // 逐渐缩小步数
  <span class="hljs-keyword">while</span>(gap) {
    // 从第gap个元素开始遍历
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i=gap; i&lt;len; i++) {
      // 逐步其和前面其他的组成员进行比较和交换
      <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> j=i-gap; j&gt;=0; j-=gap) {
        <span class="hljs-keyword">if</span>(nums[j] &gt; nums[j+gap]) {
          [nums[j], nums[j+gap]] = [nums[j+gap], nums[j]];
        }
        <span class="hljs-keyword">else</span> {
          <span class="hljs-built_in">break</span>;
        }
      }
    }
    gap = parseInt(gap / 2);
  }
}
</code></pre><ol start="5">
<li>归并排序</li>
</ol>
<blockquote>
<p>采用自下而上的分而治之的迭代思想
O(nlogn)
</p><figure><img alt="Merge Sort" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/7/6/173246d0b172446f~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
</blockquote>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> mergeSort(arr) {
  const len = arr.length
  <span class="hljs-keyword">if</span>(len &lt; 2) <span class="hljs-built_in">return</span> arr;
  const middle = Math.floor(len / 2)
  const left = arr.slice(0, middle)
  const right = arr.slice(middle)
  <span class="hljs-built_in">return</span> merge(mergeSort(left), mergeSort(right))
}
<span class="hljs-keyword">function</span> merge(left, right) {
  <span class="hljs-built_in">let</span> result = []
  <span class="hljs-keyword">while</span>(left.length &amp;&amp; right.length) {
    <span class="hljs-keyword">if</span>(left[0] &lt; right[0]) {
      result.push(left.shift())
    } <span class="hljs-keyword">else</span> {
      result.push(right.shift())
    }
  }
  result = result.concat(lest, right)
  /**
  <span class="hljs-keyword">while</span>(left.length) {
    result.push(left.shift())
  }
  <span class="hljs-keyword">while</span>(right.length) {
    result.push(right.length)
  }
  */
  <span class="hljs-built_in">return</span> result
}
</code></pre><ol start="6">
<li>快速排序</li>
</ol>
<blockquote>
<p>选择一个元素作为基数，把比基数小的放左边，比基数大的放右边，再不断递归基数左右两边的序列，分而治之。
O(nlogn)
</p><figure><img alt="quick sort" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/7/6/173246d0b9b527c9~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
</blockquote>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> quickSort(arr) {
  const len = arr.length
  <span class="hljs-keyword">if</span>(len &lt; 2) <span class="hljs-built_in">return</span> arr
  const pivot = arr[len-1]
  const left = []
  const right = []
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i &lt; len - 1; i++) {
    <span class="hljs-keyword">if</span>(arr[i] &lt; pivot) {
      left.push(arr[i])
    } <span class="hljs-keyword">else</span> {
      right.push(arr[i])
    }
  }
  <span class="hljs-built_in">return</span> [...quickSort(left), pivot, ...quickSort(right)]
}
</code></pre><ol start="7">
<li>桶排序
<blockquote>
<p>取 n 个桶，根据数组的最大值和最小值确认每个桶存放的数的区间，将数组元素插入到相应的桶里，最后再合并各个桶。
O(n+k) k 表示桶的个数</p>
</blockquote>
</li>
</ol>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> bucketSort(nums) {
  // 桶的个数，只要是正数即可
  <span class="hljs-built_in">let</span> num = 5;
  <span class="hljs-built_in">let</span> max = Math.max(...nums);
  <span class="hljs-built_in">let</span> min = Math.min(...nums);
  // 计算每个桶存放的数值范围，至少为1，
  <span class="hljs-built_in">let</span> range = Math.ceil((max - min) / num) || 1;
  // 创建二维数组，第一维表示第几个桶，第二维表示该桶里存放的数
  <span class="hljs-built_in">let</span> arr = Array.from(Array(num)).map(() =&gt; Array().fill(0));
  nums.forEach(val =&gt; {
    // 计算元素应该分布在哪个桶
    <span class="hljs-built_in">let</span> index = parseInt((val - min) / range);
    // 防止index越界，例如当[5,1,1,2,0,0]时index会出现5
    index = index &gt;= num ? num - 1 : index;
    <span class="hljs-built_in">let</span> temp = arr[index];
    // 插入排序，将元素有序插入到桶中
    <span class="hljs-built_in">let</span> j = temp.length - 1;
    <span class="hljs-keyword">while</span>(j &gt;= 0 &amp;&amp; val &lt; temp[j]) {
      temp[j+1] = temp[j];
      j--;
    }
    temp[j+1] = val;
  })
  // 修改回原数组
  <span class="hljs-built_in">let</span> res = [].concat.apply([], arr);
  nums.forEach((val, i) =&gt; {
    nums[i] = res[i];
  })
}
</code></pre><ol start="8">
<li>堆排序</li>
</ol>
<blockquote>
<p>根据数组建立一个堆（类似完全二叉树），每个结点的值都大于左右结点（最大堆，通常用于升序），或小于左右结点（最小堆，通常用于降序）。对于升序排序，先构建最大堆后，交换堆顶元素（表示最大值）和堆底元素，每一次交换都能得到未有序序列的最大值。重新调整最大堆，再交换堆顶元素和堆底元素，重复 n-1 次后就能得到一个升序的数组。
</p><figure><img alt="heap sort" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/7/6/173246d108c21651~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
</blockquote>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> heapSort(nums) {
  // 调整最大堆，使index的值大于左右节点
  <span class="hljs-keyword">function</span> adjustHeap(nums, index, size) {
    // 交换后可能会破坏堆结构，需要循环使得每一个父节点都大于左右结点
    <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>) {
      <span class="hljs-built_in">let</span> max = index;
      <span class="hljs-built_in">let</span> left = index * 2 + 1;   // 左节点
      <span class="hljs-built_in">let</span> right = index * 2 + 2;  // 右节点
      <span class="hljs-keyword">if</span>(left &lt; size &amp;&amp; nums[max] &lt; nums[left])  max = left;
      <span class="hljs-keyword">if</span>(right &lt; size &amp;&amp; nums[max] &lt; nums[right])  max = right;
      // 如果左右结点大于当前的结点则交换，并再循环一遍判断交换后的左右结点位置是否破坏了堆结构（比左右结点小了）
      <span class="hljs-keyword">if</span>(index !== max) {
        [nums[index], nums[max]] = [nums[max], nums[index]];
        index = max;
      }
      <span class="hljs-keyword">else</span> {
        <span class="hljs-built_in">break</span>;
      }
    }
  }
  // 建立最大堆
  <span class="hljs-keyword">function</span> buildHeap(nums) {
    // 注意这里的头节点是从0开始的，所以最后一个非叶子结点是 parseInt(nums.length/2)-1
    <span class="hljs-built_in">let</span> start = parseInt(nums.length / 2) - 1;
    <span class="hljs-built_in">let</span> size = nums.length;
    // 从最后一个非叶子结点开始调整，直至堆顶。
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i=start; i&gt;=0; i--) {
      adjustHeap(nums, i, size);
    }
  }

  buildHeap(nums);
  // 循环n-1次，每次循环后交换堆顶元素和堆底元素并重新调整堆结构
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i=nums.length-1; i&gt;0; i--) {
    [nums[i], nums[0]] = [nums[0], nums[i]];
    adjustHeap(nums, 0, i);
  }
}
</code></pre><h3 class="heading">基本算法</h3>
<p><a target="_blank" href="https://blog.csdn.net/weixin_42235173/article/details/90897252">剑指 OFFER</a></p>
<ol>
<li>
<p>数组交集</p>
<blockquote>
<p>给定 nums1 = [1, 2, 2, 1]，nums2 = [2, 2]，返回 [2, 2]。</p>
</blockquote>
<pre><code class="hljs bash" lang="bash">const intersection = (arr1, arr2) =&gt; arr1.filter(some =&gt; arr2.includes(some))
</code></pre><p>多个数组之间</p>
<pre><code class="hljs bash" lang="bash">const intersection = (...args) =&gt; args.reduce(
  (acr, cur) =&gt; acr.filter(item =&gt; cur.includes(item))
)
</code></pre><p>双指针+归并排序</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> intersect(nums1, nums2) {
   nums1 = nums1.sort((a, b) =&gt; a - b);
   nums2 = nums2.sort((a, b) =&gt; a - b);
   const len1 = nums1.length;
   const len2 = nums2.length;
   <span class="hljs-built_in">let</span> i = 0;
   <span class="hljs-built_in">let</span> j = 0;
   <span class="hljs-built_in">let</span> k = 0;
   <span class="hljs-keyword">while</span> (i &lt; len1 &amp;&amp; j &lt; len2) {
     <span class="hljs-keyword">if</span> (nums1[i] &lt; nums2[j]) {
       i++;
     } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (nums1[i] &gt; nums2[j]) {
       j++;
     } <span class="hljs-keyword">else</span> {
       nums1[k++] = nums1[i];
       i++;
       j++;
     }
   }
   <span class="hljs-built_in">return</span> nums1.slice(0, k);
 }
</code></pre></li>
<li>
<p>字符串的大小写取反</p>
<pre><code class="hljs bash" lang="bash">const processStr = str =&gt; str.split(<span class="hljs-string">''</span>).map(item =&gt; item === item.toUpperCase() ? item.toLowerCase() : item.toUpperCase()).join(<span class="hljs-string">''</span>)
</code></pre></li>
<li>
<p>字符串 S 中查找字符串 T 的位置</p>
<pre><code class="hljs bash" lang="bash">const findSonStrIndex = (S, T) =&gt; {
  <span class="hljs-keyword">if</span>(S.length &lt; T.length) <span class="hljs-built_in">return</span> -1
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0; i&lt;S.length;i++) {
    <span class="hljs-keyword">if</span>(S.slice(i, i+T.length) === T) <span class="hljs-built_in">return</span> i
  }
  <span class="hljs-built_in">return</span> -1
}
</code></pre></li>
<li>
<p>旋转数组</p>
<pre><code class="hljs bash" lang="bash">const rotate(arr, key) =&gt; {
  const len = arr.length
  const step = key % len
  <span class="hljs-built_in">return</span> arr.slice(-step).concat(arr.slice(0, len - step))
}
</code></pre></li>
<li>
<p>对称数</p>
<pre><code class="hljs bash" lang="bash">const reverseFind = max =&gt; {
  const result = []
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0, i &lt; max; i++) {
    const origin = <span class="hljs-string">''</span> + i
    const reverse = origin.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>)
    <span class="hljs-keyword">if</span>(origin === reverse) {
      result.push(i)
    }
  }
  <span class="hljs-built_in">return</span> result
}
</code></pre></li>
<li>
<p>数组 0 移至末尾（愿数组上操作）</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> zeroMove(array){
  const len = array.length
  <span class="hljs-built_in">let</span> j = 0;
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i &lt; len - j; i++) {
    <span class="hljs-keyword">if</span>(array[i] === 0) {
      array.push(0)
      array.splice(i, 1)
      i--
      j++
    }
  }
  <span class="hljs-built_in">return</span> array
}
</code></pre></li>
<li>
<p>currying add</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> curryingAdd(...outer) {
  <span class="hljs-built_in">let</span> result = 0
  result = outer.reduce((acr, cur) =&gt; acr + cur, result)

  const ret = <span class="hljs-keyword">function</span>(...inner) {
    result = inner.reduce((acr, cur) =&gt; acr+cur, result)
    <span class="hljs-built_in">return</span> ret
  }
  ret.toString = <span class="hljs-function"><span class="hljs-title">function</span></span>() { <span class="hljs-built_in">return</span> result}
  ret.valueOf = <span class="hljs-function"><span class="hljs-title">function</span></span>() { <span class="hljs-built_in">return</span> result}

  <span class="hljs-built_in">return</span> ret
}
</code></pre></li>
<li>
<p>两数之和</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> findTwoSum(arr, target) {
  <span class="hljs-built_in">let</span> result = []
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0, ilen = arr.length; i &lt; ilen;i++) {
    <span class="hljs-built_in">let</span> another = target - arr[i]
    <span class="hljs-built_in">let</span> index = arr.indexOf(another, i)
    <span class="hljs-keyword">if</span>(index &gt; 0) {
      result.push(i, index)
      // <span class="hljs-built_in">break</span>
    }
  }
  <span class="hljs-built_in">return</span> result
}
</code></pre></li>
<li>
<p>中位数</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> mid(arr1, arr2) {
  <span class="hljs-built_in">let</span> arr = []
  <span class="hljs-keyword">while</span>(arr1.length &amp;&amp; arr2.length) {
    <span class="hljs-keyword">if</span>(arr1[0] &lt; arr2[0]) {
      arr.push(arr1.shift())
    } <span class="hljs-keyword">else</span> {
      arr.push(arr2.shift())
    }
  }
  arr = arr.concat(arr1, arr2)
  const len = arr.length
  <span class="hljs-keyword">if</span>(len % 2) {
    <span class="hljs-built_in">return</span> arr[Math.floor(len/2)]
  } <span class="hljs-keyword">else</span> {
    <span class="hljs-built_in">return</span> (arr[len/2 -1] + arr[len/2]) / 2
  }
}
</code></pre></li>
<li>
<p>数字变反序字符串</p>
<pre><code class="hljs bash" lang="bash">const numReStr = num =&gt;
    num != 0 ? `<span class="hljs-variable">${num%10}</span><span class="hljs-variable">${numReStr(num/10&gt;&gt;0)}</span>` : <span class="hljs-string">''</span>
const numReStr = num =&gt; num.toString().split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>)
</code></pre></li>
<li>
<p>数组中抽取不重复的数</p>
<pre><code class="hljs bash" lang="bash">const sliceArray = (arr, size) =&gt; {
  <span class="hljs-built_in">let</span> result = [];
  const len = arr.length;
  const arr_ = [...arr];

  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i &lt; size; i++) {
    <span class="hljs-built_in">let</span> key = Math.floor(Math.random() * arr_.length);
    result.push(arr_[key]);
    arr_.splice(key, 1);
  }
  console.log(result);
  <span class="hljs-built_in">return</span> result;
};
</code></pre></li>
<li>
<p>flat 对象</p>
<pre><code class="hljs bash" lang="bash">const flatObj = (obj, parentKey=<span class="hljs-string">''</span>, result={}) {
  <span class="hljs-keyword">for</span>(const key <span class="hljs-keyword">in</span> obj) {
    <span class="hljs-keyword">if</span>(obj.hasOwnProperty(key)) {
      const keyName = `<span class="hljs-variable">${parentkey}</span><span class="hljs-variable">${key}</span>`
      <span class="hljs-keyword">if</span>(typeof obj[key] === <span class="hljs-string">'object'</span>) {
        flatObj(obj[key], `<span class="hljs-variable">${keyName}</span>.`, result)
      }<span class="hljs-keyword">else</span> {
        result[keyName]=obj[key]
      }
    }
  }
  <span class="hljs-built_in">return</span> result
}
// { <span class="hljs-string">'a.b.c.dd'</span>: <span class="hljs-string">'abcdd'</span>, <span class="hljs-string">'a.d.xx'</span>: <span class="hljs-string">'adxx'</span>, <span class="hljs-string">'a.e'</span>: <span class="hljs-string">'ae'</span> }
</code></pre></li>
<li>
<p>计算 1-n 中出现的 1 的次数</p>
<pre><code class="hljs bash" lang="bash">const findOne = n =&gt; {
  <span class="hljs-built_in">let</span> str = <span class="hljs-string">''</span>
  <span class="hljs-keyword">while</span>(n&gt;0) {
    str+=n
    n--
  }
  <span class="hljs-built_in">return</span> str.split(<span class="hljs-string">''</span>).filter(n =&gt; n===<span class="hljs-string">'1'</span>).length
}
</code></pre></li>
<li>
<p>牌顶牌底</p>
<pre><code class="hljs bash" lang="bash">const sort = arr =&gt; {
  <span class="hljs-built_in">let</span> pre = []
  <span class="hljs-keyword">while</span>(arr.length&gt;1){
    pre.push(arr.pop())
    pre.push(arr.shift())
  }
  pre.push(arr.pop())
  console.log(pre)
  <span class="hljs-built_in">return</span> pre
}
</code></pre></li>
<li>
<p>二进制转 base64</p>
<pre><code class="hljs bash" lang="bash">String.fromCharCode(...new Unit8Array(response.data))
</code></pre></li>
<li>
<p>normalize 函数</p>
<blockquote>
<p><code>'[abc[bcd[def]]]' --&gt; {value: 'abc', children: {value: 'bcd', children: {value: 'def'}}}</code></p>
</blockquote>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> normalize(str) {
  <span class="hljs-built_in">let</span> result = {}
  str
    .split(/[\[\]]/)
    .filter(item=&gt;item)
    .reduce((acr, cur, index, arr) =&gt; {
      acr.value = cur
      <span class="hljs-keyword">if</span>(index !== arr.length - 1) {
        <span class="hljs-built_in">return</span> acr.children = {}
      }
    }, result)
  <span class="hljs-built_in">return</span> result
}
</code></pre></li>
<li>
<p>十进制转二进制</p>
<pre><code class="hljs bash" lang="bash">const toBit = num =&gt; {
  const res = []
  <span class="hljs-keyword">while</span>(num&gt;0){
    res.unshift(num%2)
    num=Math.floor(num/2)
  }
  <span class="hljs-built_in">return</span> res.join(<span class="hljs-string">''</span>)
}
</code></pre></li>
<li>
<p>判断成对符号</p>
<pre><code class="hljs bash" lang="bash">const validParentheses = str =&gt; {
  <span class="hljs-keyword">if</span>(!str) <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
  const len = str.length
  <span class="hljs-keyword">if</span>(len % 2 !== 0) <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
  const maps = {
    <span class="hljs-string">'('</span>: 1,
    <span class="hljs-string">'['</span>: 2,
    <span class="hljs-string">'{'</span>: 3,
    <span class="hljs-string">')'</span>: -1,
    <span class="hljs-string">']'</span>: -2,
    <span class="hljs-string">'}'</span>: -3
  }
  const stack = []
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0;i &lt; len;i++) {
    const cur = maps[str[i]]
    <span class="hljs-keyword">if</span>(cur &gt; 0) {
      stack.push(cur)
    }<span class="hljs-keyword">else</span> {
      <span class="hljs-keyword">if</span>(cur + stack.pop() !== 0) <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
    }
  }
  <span class="hljs-keyword">if</span>(stack.length === 0) <span class="hljs-built_in">return</span> <span class="hljs-literal">true</span>
  <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
}
</code></pre></li>
<li>
<p>三数之和</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> threeSumZero(arr) {
  const len = arr.length;
  <span class="hljs-keyword">if</span> (len &lt; 3) <span class="hljs-built_in">return</span> [];
  const nums = arr.sort((a, b) =&gt; a - b);
  const result = [];
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i &lt; len; i++) {
    <span class="hljs-keyword">if</span> (nums[i] &gt; 0) <span class="hljs-built_in">break</span>;
    <span class="hljs-keyword">if</span> (nums[i] === nums[i - 1]) <span class="hljs-built_in">continue</span>;
    <span class="hljs-built_in">let</span> l = i + 1;
    <span class="hljs-built_in">let</span> r = len - 1;
    <span class="hljs-keyword">while</span> (l &lt; r) {
      <span class="hljs-built_in">let</span> sum = nums[i] + nums[l] + nums[r];
      <span class="hljs-keyword">if</span> (sum === 0) {
        result.push([nums[i], nums[l], nums[r]]);
        <span class="hljs-keyword">while</span> (l &lt; r &amp;&amp; nums[l] === nums[l + 1]) {
          l++;
        }
        <span class="hljs-keyword">while</span> (l &lt; r &amp;&amp; nums[r] === nums[r - 1]) {
          r--;
        }
        l++;
        r--;
      } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sum &lt; 0) {
        l++;
      } <span class="hljs-keyword">else</span> {
        r--;
      }
    }
  }
  console.log(result);
  <span class="hljs-built_in">return</span> result;
}
</code></pre></li>
<li>
<p>红绿灯</p>
<pre><code class="hljs bash" lang="bash">async <span class="hljs-keyword">function</span> step(color, duration) {
  console.log(color)
  await new Promise((resolve, reject) =&gt; <span class="hljs-built_in">set</span>Timeout(resolve, duration))
}
async <span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">showLight</span></span>() {
  <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>) {
    await step(<span class="hljs-string">'red'</span>, 3000)
    await step(<span class="hljs-string">'green'</span>, 1000)
    await step(<span class="hljs-string">'yellow'</span>, 2000)
  }
}
</code></pre></li>
<li>
<p>最大无重复子串长度</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> loneSubStr(s) {
  const arr = s.split(<span class="hljs-string">''</span>)
  const len = arr.length
  <span class="hljs-keyword">if</span>(len === 1) <span class="hljs-built_in">return</span> 1
  const maxLen = 0
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0; i &lt; len-1; i++){
    <span class="hljs-built_in">let</span> str = arr[i]
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> j= i+1; j &lt; len; j++){
      <span class="hljs-keyword">if</span>(str.indexOf(arr[j]) !== -1) {
        maxLen = str.length &gt; maxLen ? str.length : maxLen
        <span class="hljs-built_in">break</span>;
      }
      str += arr[j]
      maxLen = str.length &gt; maxLen ? str.length : maxLen
      <span class="hljs-built_in">break</span>;
    }
  }
  <span class="hljs-built_in">return</span> maxLen
}
</code></pre></li>
<li>
<p>最大子串和</p>
<pre><code class="hljs bash" lang="bash">const maxSum = arr =&gt; {
  <span class="hljs-built_in">let</span> current = 0
  <span class="hljs-built_in">let</span> sum = 0
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0,ilen=arr.length;i&lt;ilen;i++) {
    <span class="hljs-keyword">if</span>(current &gt; 0) {
      current+=arr[i]
    } <span class="hljs-keyword">else</span> {
      current = arr[i]
    }

    <span class="hljs-keyword">if</span>(current&gt;sum) {
      sum = current
    }
  }
  <span class="hljs-built_in">return</span> sum
}
</code></pre></li>
<li>
<p>最大公共子串</p>
<pre><code class="hljs bash" lang="bash">const findSubstr = (str1, str2) =&gt; {
  <span class="hljs-keyword">if</span>(str1.length &gt; str2.length) {
    [str1, str2] = [str2, str1]
  }
  const len1 = str1.length
  const len2 = str2.length
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> j = len1;j&gt;0;j--) {
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0;i&lt;len1-j;i++) {
      const current = str1.substr(i,j)
      <span class="hljs-keyword">if</span>(str2.indexOf(current) &gt;=0) {
        <span class="hljs-built_in">return</span> current
      }
    }
  }
  <span class="hljs-built_in">return</span> <span class="hljs-string">''</span>
}
</code></pre></li>
<li>
<p>最大子序列长度</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> lcs(str1, str2) {
  const len1 = str1.length
  const len2 = str2.length
  const dp = [new Array(len2+1).fill(0)]
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 1; i&lt;= len1;i++) {
    dp[i] = [0]
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> j = 1;j&lt;=len2;j++) {
      <span class="hljs-keyword">if</span>(str1[i-1]===str2[j-1]) {
        dp[i][j]=dp[i-1][j-1]+1
      } <span class="hljs-keyword">else</span> {
        dp[i][j]=Math.max(dp[i-1][j], dp[i][j-1])
      }
    }
  }
  <span class="hljs-built_in">return</span> dp[len1][len2]
}
</code></pre></li>
<li>
<p>最长公共前缀</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> longFirstStr(strs) {
  <span class="hljs-keyword">if</span> (strs === null || strs.length === 0) <span class="hljs-built_in">return</span> <span class="hljs-string">""</span>;
  <span class="hljs-built_in">let</span> prevs = strs[0];
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0, ilen = strs.length; i &lt; ilen; i++) {
    <span class="hljs-built_in">let</span> j = 0;
    <span class="hljs-keyword">for</span> (; j &lt; prevs.length &amp;&amp; j &lt; strs[i].length; j++) {
      <span class="hljs-keyword">if</span> (prevs.charAt(j) !== strs[i].charAt(j)) <span class="hljs-built_in">break</span>;
    }
    prevs = prevs.substr(0, j);
    <span class="hljs-keyword">if</span> (prevs === <span class="hljs-string">""</span>) <span class="hljs-built_in">return</span> <span class="hljs-string">""</span>;
  }
  <span class="hljs-built_in">return</span> prevs;
}
</code></pre></li>
<li>
<p>斐波那契</p>
<pre><code class="hljs bash" lang="bash">const cache = []
<span class="hljs-keyword">function</span> fib(n) {
  <span class="hljs-keyword">if</span>(cache[n]) <span class="hljs-built_in">return</span> cache[n]
  <span class="hljs-keyword">if</span>(n&lt;=2) {
    cache[n]=1
    <span class="hljs-built_in">return</span> 1
  }
  cache.push(fib(n-1) + fib(n-2))
  <span class="hljs-built_in">return</span> cache[n]
}
</code></pre><p>青蛙每次跳一阶或两阶台阶，n 阶台阶多少种方式</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> climbStairs(n) {
  <span class="hljs-keyword">if</span>(n ===1 ) <span class="hljs-built_in">return</span> 1
  <span class="hljs-built_in">let</span> first = 1
  <span class="hljs-built_in">let</span> second = 2
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 3; i &lt;= n; i++) {
    <span class="hljs-built_in">let</span> third = first + second
    first = second
    second = third
  }
  <span class="hljs-built_in">return</span> second
}
</code></pre></li>
<li>
<p>链式调用</p>
<pre><code class="hljs bash" lang="bash">class LazyManClass {
  constructor(name) {
    this.name = name
    console.log(`My name is <span class="hljs-variable">${name}</span>`)
    this.queue = []
    <span class="hljs-built_in">set</span>Timeout(() =&gt; this.next(), 0)
  }
  eat(food) {
    const fn = () =&gt; {
      console.log(`I am eating <span class="hljs-variable">${food}</span>`)
      this.next()
    }
    this.queue.push(fn)
    <span class="hljs-built_in">return</span> this
  }
  sleepFirst(time) {
    const fn = () =&gt; {
      <span class="hljs-built_in">set</span>Timeout(() =&gt; {
        console.log(`Wait first <span class="hljs-keyword">for</span> <span class="hljs-variable">${time}</span>ms`)
        this.next()
      }, time)
    }
    this.queue.unshift(fn)
    <span class="hljs-built_in">return</span> this
  }
  sleep(time) {
    const fn = () =&gt; {
      <span class="hljs-built_in">set</span>Timeout(() =&gt; {
        console.log(`<span class="hljs-built_in">wait</span> <span class="hljs-keyword">for</span> <span class="hljs-variable">${time}</span>ms`)
        this.next()
      }, time)
    }
    this.queue.push(fn)
    <span class="hljs-built_in">return</span> this
  }
  <span class="hljs-function"><span class="hljs-title">next</span></span>() {
    const fn = this.queue.shift()
    fn &amp;&amp; fn()
  }
}
<span class="hljs-keyword">function</span> lazyMan(name) {
  <span class="hljs-built_in">return</span> new LazyManClass(name)
}
lazyMan(<span class="hljs-string">'Tom'</span>).eat(<span class="hljs-string">'eggs'</span>).sleepFirst(1000).eat(<span class="hljs-string">'apple'</span>).sleep(2000).eat(<span class="hljs-string">'junk food'</span>)
</code></pre></li>
<li>
<p>setTimeout 实现 setInterval</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">mySetInterval</span></span>() {
  mySetInterval.timer = <span class="hljs-built_in">set</span>Timeout(() =&gt; {
    arguments[0]()
    mySetInterval(...arguments)
  }, arguments[1])
  mySetInterval.clear = <span class="hljs-function"><span class="hljs-title">function</span></span> () {
    clearTimeout(mySetInterval.timer)
  }
}
</code></pre></li>
<li>
<p>实现 multiRequest</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> multiRequest(urls, maxNum, callback) {
  <span class="hljs-built_in">let</span> urlCount = urls.length;
  <span class="hljs-built_in">let</span> requestQueue = [];
  <span class="hljs-built_in">let</span> result = [];
  <span class="hljs-built_in">let</span> currentIndex = 0;
  const handleRequest = (url) =&gt; {
    const req = fetch(url).then(res =&gt; {
      const len = result.push(res)
      <span class="hljs-keyword">if</span> (len &lt; urlCount &amp;&amp; currentIndex + 1 &lt; urlCount) {
        requestQueue.shift()
        handleRequest(urls[++i])
      } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (len === urlCount) {
        typeof callback === <span class="hljs-string">'function'</span> &amp;&amp; callback(result)
      }
    }).catch(e =&gt; result.push(e))
    <span class="hljs-keyword">if</span> (requestQueue.push(req) &lt; maxNum) {
      handleRequest(urls[++i])
    }
  };
  handleRequest(urls[i])
}
</code></pre></li>
<li>
<p>实现 once 函数</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> once(func) {
  <span class="hljs-built_in">let</span> flag = <span class="hljs-literal">true</span>
  <span class="hljs-built_in">return</span> <span class="hljs-function"><span class="hljs-title">function</span></span>() {
    <span class="hljs-keyword">if</span>(flag) {
      func.apply(this, arguments)
      flag = <span class="hljs-literal">false</span>
    }
    <span class="hljs-built_in">return</span> undefined
  }
}
</code></pre></li>
<li>
<p>连续数字格式化</p>
<pre><code class="hljs bash" lang="bash">// 1,3,4,5,7,8
//=&gt; 1, 3-5, 7-8
<span class="hljs-keyword">function</span> formatNum(...nums) {
  const arr = nums.sort((a, b) =&gt; a - b);
  const len = arr.length;
  <span class="hljs-built_in">let</span> idx = 0;
  <span class="hljs-built_in">let</span> temp = [[arr[0]]];
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 1; i &lt; len; i++) {
    <span class="hljs-keyword">if</span> (arr[i] - 1 === arr[i - 1]) {
      temp[idx].push(arr[i]);
    } <span class="hljs-keyword">else</span> {
      temp[++idx] = [arr[i]];
    }
  }
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> j = 0, jlen = temp.length; j &lt; jlen; j++) {
    const len = temp[j].length;
    <span class="hljs-keyword">if</span> (len &gt; 1) {
      temp[j] = `<span class="hljs-variable">${temp[j][0]}</span>-&gt;<span class="hljs-variable">${temp[j][len - 1]}</span>`;
    } <span class="hljs-keyword">else</span> {
      temp[j] = `<span class="hljs-variable">${temp[j][0]}</span>`;
    }
  }
  <span class="hljs-built_in">return</span> temp.join(<span class="hljs-string">", "</span>);
}
</code></pre></li>
<li>
<p>字符串转换</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> trans(str) {
  <span class="hljs-keyword">if</span> (typeof str !== <span class="hljs-string">"string"</span>) <span class="hljs-built_in">return</span> <span class="hljs-string">""</span>;
  <span class="hljs-built_in">let</span> len = str.length;
  <span class="hljs-keyword">if</span> (len &lt; 2) <span class="hljs-built_in">return</span> str;
  <span class="hljs-built_in">let</span> idx = 1;
  <span class="hljs-built_in">let</span> nums = 1;
  <span class="hljs-built_in">let</span> res = str[0];
  <span class="hljs-built_in">let</span> last = res;
  <span class="hljs-keyword">while</span> (idx &lt; len) {
    <span class="hljs-keyword">if</span> (str[idx] === last) {
      nums++;
      <span class="hljs-keyword">if</span> (idx === len - 1) {
        res = res + nums;
        <span class="hljs-built_in">break</span>;
      }
    } <span class="hljs-keyword">else</span> {
      res = res + (nums &gt; 1 ? nums : <span class="hljs-string">""</span>) + str[idx];
      last = str[idx];
      nums = 1;
    }
    idx++;
  }
  <span class="hljs-built_in">return</span> res;
}
console.log(trans(<span class="hljs-string">"aaabcccaa"</span>));
// a3bc3a2
</code></pre></li>
<li>
<p>全排列</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> permute(...nums) {
  const res = [];
  nums.sort((a, b) =&gt; a - b);
  find(nums, []);
  <span class="hljs-built_in">return</span> res;
  <span class="hljs-keyword">function</span> find(nums, temp) {
    const len = nums.length;
    <span class="hljs-keyword">if</span> (nums.length === 0) {
      res.push(temp.slice());
    }
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i &lt; len; i++) {
      temp.push(nums[i]);
      const copy = nums.slice();
      copy.splice(i, 1);
      find(copy, temp);
      temp.pop();
    }
  }
}
</code></pre></li>
<li>
<p>二叉树</p>
<pre><code class="hljs bash" lang="bash">/** binary tree
      1
  2          3
4    5    6    7
*/
const root = {
  val: 1,
  left: {
    val: 2,
    left: {
      val: 4,
    },
    right: {
      val: 5,
    },
  },
  right: {
    val: 3,
    left: {
      val: 6,
    },
    right: {
      val: 7,
    },
  },
};

// 递归
// 先序
<span class="hljs-keyword">function</span> rlr(root) {
  <span class="hljs-keyword">if</span> (!root) <span class="hljs-built_in">return</span> <span class="hljs-string">""</span>;
  console.log(root.val);
  rlr(root.left);
  rlr(root.right);
}

// 中序
<span class="hljs-keyword">function</span> lrr(root) {
  <span class="hljs-keyword">if</span> (!root) <span class="hljs-built_in">return</span> <span class="hljs-string">""</span>;
  lrr(root.left);
  console.log(root.val);
  lrr(root.right);
}

// 后序
<span class="hljs-keyword">function</span> lr(root) {
  <span class="hljs-keyword">if</span> (!root) <span class="hljs-built_in">return</span> <span class="hljs-string">""</span>;
  lr(root.left);
  lr(root.right);
  console.log(root.val);
}

// 非递归前序遍历
<span class="hljs-keyword">function</span> RLR(root) {
  const arr = [];
  const res = [];
  <span class="hljs-keyword">if</span>(!root) <span class="hljs-built_in">return</span> []
  arr.push(root)
  <span class="hljs-keyword">while</span> (arr.length) {
    const temp = arr.pop();
    res.push(temp.val);
    temp.right &amp;&amp; arr.push(temp.right);
    temp.left &amp;&amp; arr.push(temp.left);
  }
  <span class="hljs-built_in">return</span> res;
}

// 非递归中序遍历
<span class="hljs-keyword">function</span> LRR(root) {
  const arr = [];
  const res = [];
  <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) {
    <span class="hljs-keyword">while</span> (root) {
      arr.push(root);
      root = root.left;
    }
    <span class="hljs-keyword">if</span> (arr.length === 0) <span class="hljs-built_in">break</span>;
    const temp = arr.pop();
    res.push(temp.val);
    root = temp.right;
  }
  <span class="hljs-built_in">return</span> res;
}

// 非递归后序遍历
<span class="hljs-keyword">function</span> LR(root) {
  const arr = [];
  const res = [];
  <span class="hljs-keyword">if</span>(!root) <span class="hljs-built_in">return</span> []
  arr.push(root);
  <span class="hljs-keyword">while</span>(arr.length) {
    const temp = arr.pop()
    res.unshift(temp.val)
    temp.left &amp;&amp; arr.push(temp.left)
    temp.right &amp;&amp; arr.push(temp.right)
  }
}

// 层序遍历
<span class="hljs-keyword">function</span> levelDfs(root){
  const arr = []
  const res = []
  <span class="hljs-keyword">if</span>(!root) <span class="hljs-built_in">return</span> []
  arr.push(root)
  <span class="hljs-built_in">let</span> level = 0
  <span class="hljs-keyword">while</span>(arr.length) {
    <span class="hljs-built_in">let</span> len = arr.length
    res[level] = []
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0; i &lt; len; i++) {
      const temp = arr.shift()
      res[level].push(temp.val)
      temp.left &amp;&amp; arr.push(temp.left)
      temp.right &amp;&amp; arr.push(temp.right)
    }
    level++
  }
  <span class="hljs-built_in">return</span> res
}

// 路径遍历
// [ <span class="hljs-string">'1-&gt;2-&gt;4'</span>, <span class="hljs-string">'1-&gt;2-&gt;5'</span>, <span class="hljs-string">'1-&gt;3-&gt;6'</span>, <span class="hljs-string">'1-&gt;3-&gt;7'</span> ]
<span class="hljs-keyword">function</span> treeDfs(root) {
  <span class="hljs-keyword">if</span>(!root) <span class="hljs-built_in">return</span> []
  const res = []
  const arr = []
  const path = []
  arr.push(root)
  path.push(root.val.toString())
  <span class="hljs-keyword">while</span>(arr.length){
    const temp = arr.pop()
    const cur = path.pop()
    <span class="hljs-keyword">if</span>(!temp.left &amp;&amp; !temp.right) {
      res.unshift(cur)
    }
    <span class="hljs-keyword">if</span>(temp.left) {
      arr.push(temp.left)
      path.push(cur + <span class="hljs-string">'-&gt;'</span> + temp.left.val)
    }
    <span class="hljs-keyword">if</span>(temp.right) {
      arr.push(temp.right)
      path.push(cur + <span class="hljs-string">'-&gt;'</span> + temp.right.val)
    }
  }
  <span class="hljs-built_in">return</span> res
}
</code></pre></li>
<li>
<p>多叉树的深度</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> getMaxFloor(tree) {
  <span class="hljs-built_in">let</span> max = 0;
  <span class="hljs-keyword">function</span> each(data, floor) {
    data.forEach((e) =&gt; {
      e.floor = floor;
      <span class="hljs-keyword">if</span> (floor &gt; max) {
        max = floor;
      }
      <span class="hljs-keyword">if</span> (e.children.length) {
        each(e.children, floor + 1);
      }
    });
  }
  each(tree, 1);
  <span class="hljs-built_in">return</span> max;
}
</code></pre><pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> getTreeDeep(tree) {
  <span class="hljs-built_in">let</span> deep = 0
  tree.children &amp;&amp; tree.children.forEach(item =&gt; {
    <span class="hljs-keyword">if</span>(item.children) {
      deep = Math.max(deep, getTreeDeep(item.children) + 1)
    } <span class="hljs-keyword">else</span> {
      deep = Math.max(deep, 1)
    }
  })
  <span class="hljs-built_in">return</span> deep
}
</code></pre></li>
<li>
<p>多叉树的广度</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> getTreeExtend(tree) {
  <span class="hljs-built_in">let</span> extend = 0
  tree.forEach(item =&gt; {
    <span class="hljs-keyword">if</span>(item.children) {
      extend += getTreeExtend(item.children)
    } <span class="hljs-keyword">else</span> {
      extend += 1
    }
  })
  <span class="hljs-built_in">return</span> extend
}
</code></pre></li>
<li>
<p>有效三角形的个数</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> triangleNumer(...nums) {
  const len = nums.length;
  <span class="hljs-keyword">if</span> (len &lt; 3) <span class="hljs-built_in">return</span> 0;
  <span class="hljs-built_in">let</span> res = 0;
  nums.sort((a, b) =&gt; a - b);
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = len - 1; i &gt; 1; i--) {
    <span class="hljs-built_in">let</span> l = 0;
    <span class="hljs-built_in">let</span> r = i - 1;
    <span class="hljs-keyword">while</span> (l &lt; r) {
      <span class="hljs-keyword">if</span> (nums[l] + nums[r] &gt; nums[i]) {
        res += r - l;
        r--;
      } <span class="hljs-keyword">else</span> {
        l++;
      }
    }
  }
  <span class="hljs-built_in">return</span> res;
}
</code></pre></li>
<li>
<p>判断是扑克连子</p>
<pre><code class="hljs bash" lang="bash">// 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

const isStraight = <span class="hljs-keyword">function</span>(nums) {
    const repeat = new Set()
    <span class="hljs-built_in">let</span> min = 14
    <span class="hljs-built_in">let</span> max = 0
    const len = nums.length
    <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0; i &lt; len; i++){
        const num = nums[i]
        <span class="hljs-keyword">if</span>(num === 0) <span class="hljs-built_in">continue</span> // 判断是否大小王，跳过
        max = Math.max(max, num) // 最大牌
        min = Math.min(min, num) // 最小牌
        <span class="hljs-keyword">if</span>(repeat.has(num)) <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span> // 有重复，必定不是连子
        repeat.add(num) // 添加至Set
    }
    <span class="hljs-built_in">return</span> max - min &lt; 5 // 最大牌-最小牌&lt;5 构成连子
};
</code></pre></li>
<li>
<p>升序二维数组 二分查找</p>
<pre><code class="hljs bash" lang="bash">// O(mlogn)
<span class="hljs-keyword">function</span> find(target, arr){
  const len = arr.length
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 0; i &lt; len; i++) {
    <span class="hljs-built_in">let</span> l = 0
    <span class="hljs-built_in">let</span> r = arr[i].length
    <span class="hljs-keyword">while</span>(l&lt;r){
      const mid = Math.floor((l+r)/2)
      <span class="hljs-keyword">if</span>(target === arr[i][mid]) <span class="hljs-built_in">return</span> <span class="hljs-literal">true</span>
      <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(target &gt; arr[i][mid]) l=mid+1
      <span class="hljs-keyword">else</span> r=mid
    }
  }
  <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
}
</code></pre></li>
<li>
<p>质数</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> isPrime(n) {
  <span class="hljs-keyword">if</span>(n &lt;= 3) <span class="hljs-built_in">return</span> n&gt;1
  <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(n%2 === 0) <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
  const sq = Math.sqrt(n)
  <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i = 3; i &lt;= sq; i+=2){
    <span class="hljs-keyword">if</span>(n%i === 0) <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
  }
  <span class="hljs-built_in">return</span> <span class="hljs-literal">true</span>
}
</code></pre></li>
<li>
<p>字符串解码</p>
<pre><code class="hljs bash" lang="bash">// <span class="hljs-string">'HG[3|B[2|CA]]F'</span>
// ---&gt;
// <span class="hljs-string">'HGBCACABCACABCACAF'</span>
<span class="hljs-keyword">function</span> decodeStr(str) {
  <span class="hljs-built_in">let</span> i = 0;
  <span class="hljs-built_in">let</span> x = -1,
    y = -1,
    z = -1;
  const len = str.length;
  <span class="hljs-keyword">while</span> (i &lt; len) {
    <span class="hljs-keyword">if</span> (str[i] === <span class="hljs-string">"["</span>) {
      x = i;
    } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (str[i] === <span class="hljs-string">"|"</span>) {
      y = i;
    } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (str[i] === <span class="hljs-string">"]"</span>) {
      z = i;
      <span class="hljs-built_in">break</span>;
    }
    i++;
  }
  <span class="hljs-keyword">if</span> (x !== -1 &amp;&amp; y !== -1 &amp;&amp; z !== -1) {
    const <span class="hljs-built_in">times</span> = Number(str.slice(x + 1, y));
    const sub = str.slice(y + 1, z);
    const decode_str = str.slice(0, x) + sub.repeat(<span class="hljs-built_in">times</span>) + str.slice(z + 1);
    <span class="hljs-built_in">return</span> decodeStr(decode_str);
  }
  <span class="hljs-built_in">return</span> str;
}
</code></pre></li>
<li>
<p>矩阵最短路径和</p>
<pre><code class="hljs bash" lang="bash">/**
[
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1],
]
---&gt; 7
*/
<span class="hljs-keyword">function</span> findTwoArrayM<span class="hljs-keyword">in</span>Path(arr) {
  const m = arr.length - 1;
  <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = m; i &gt;= 0; i--) {
    const n = arr[0].length - 1;
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> j = n; j &gt;= 0; j--) {
      <span class="hljs-keyword">if</span> (i === m &amp;&amp; j !== n) {
        arr[i][j] = arr[i][j] + arr[i][j + 1];
      } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (i !== m &amp;&amp; j === n) {
        arr[i][j] = arr[i][j] + arr[i + 1][j];
      } <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (i !== m &amp;&amp; j !== n) {
        arr[i][j] = arr[i][j] + Math.min(arr[i + 1][j], arr[i][j + 1]);
      }
    }
  }
  <span class="hljs-built_in">return</span> arr[0][0];
}
</code></pre></li>
<li>
<p>最少优惠券数量</p>
<pre><code class="hljs bash" lang="bash">// minCoupon(65, [4, 30, 20, 10, 5])
// [30,30,5]
<span class="hljs-keyword">function</span> minCoupon(money, list) {
  list = list.sort((a, b) =&gt; b - a);
  <span class="hljs-keyword">function</span> _coupon(total, minus, tmp) {
    <span class="hljs-keyword">if</span> (total &lt; minus[minus.length - 1] || tmp.length &gt;= 5) <span class="hljs-built_in">return</span> tmp;
    <span class="hljs-keyword">if</span> (total - minus[0] &gt;= 0) {
      tmp.push(minus[0]);
      <span class="hljs-built_in">return</span> _coupon(total - minus[0], minus, tmp);
    } <span class="hljs-keyword">else</span> {
      <span class="hljs-built_in">return</span> _coupon(total, minus.slice(1), tmp);
    }
  }
  const result = [];
  <span class="hljs-built_in">return</span> _coupon(money, list, result);
}
</code></pre></li>
</ol>
<h3 class="heading">正则表达式</h3>
<ol>
<li>
<p>判断正确的网址</p>
<pre><code class="hljs bash" lang="bash">const reg = /^(?:(https?|ftp):\/\/)?((?:[\w-]+\.)+[a-z0-9]+)((?:\/[^?<span class="hljs-comment">#]*)+)?(\?[^#]+)?(#.+)?$/i</span>
</code></pre><pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> isURL(str) {
  try{
    const {
      href, origin,
      host, hostname,
      pathname
    } = new URL(str)
    <span class="hljs-built_in">return</span> <span class="hljs-literal">true</span>
  }catch(e) {
    <span class="hljs-built_in">return</span> <span class="hljs-literal">false</span>
  }
}
</code></pre></li>
<li>
<p>search params</p>
<pre><code class="hljs bash" lang="bash">// https://www.xx.cn/api?keyword=&amp;level1=&amp;local_batch_id=&amp;elective=800,700&amp;local_province_id=33
// elective [<span class="hljs-string">'800'</span>, <span class="hljs-string">'700'</span>]
<span class="hljs-keyword">function</span> getVal(url) {
  <span class="hljs-keyword">if</span>(!url) <span class="hljs-built_in">return</span>
  const res = url.match(/(?&lt;elective)(\d+(,\d+)*)/)
  res ? res[0].split(<span class="hljs-string">','</span>) : []
}
// or
url = new URLSearchParams(url).get(<span class="hljs-string">'elective)
</span></code></pre></li>
<li>
<p>匹配连续出现子串</p>
<pre><code class="hljs bash" lang="bash">str.match(/(.)\1+/g)
// <span class="hljs-string">'aassscvbaff'</span>
// [<span class="hljs-string">'aa'</span>, <span class="hljs-string">'sss'</span>, <span class="hljs-string">'ff'</span>]
</code></pre></li>
<li>
<p>数字每三位加逗号</p>
<pre><code class="hljs bash" lang="bash">const addComma = str =&gt;
 str.replace(/(\d)(?=(\d{3})+\b)/g, <span class="hljs-string">'$1,'</span>)
</code></pre><pre><code class="hljs bash" lang="bash">const addComma = str =&gt; str.replace(/(?!\b)(?=(\d{3})+\b)/g, <span class="hljs-string">','</span>)
</code></pre></li>
<li>
<p>十六进制颜色值</p>
<pre><code class="hljs bash" lang="bash">string.match(/<span class="hljs-comment">#[0-9A-Fa-f]{6}|#[0-9a-fA-F]{3}/)</span>
</code></pre></li>
<li>
<p>时间</p>
<pre><code class="hljs bash" lang="bash">const reg = /^(0?[1-9]|1[0-9]|2[0-3]):(0?[0-9]|[1-5]|[0-9])$/
</code></pre></li>
<li>
<p>日期</p>
<pre><code class="hljs bash" lang="bash">const reg = /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/
</code></pre></li>
<li>
<p>windows 文件路径</p>
<pre><code class="hljs bash" lang="bash">const reg = /^[a-zA-Z]:\\([^\\:*&lt;&gt;|<span class="hljs-string">"?\r\n/]+\\)*([^\\:*&lt;&gt;|"</span>?\r\n/]+)?$/;
</code></pre></li>
<li>
<p>匹配 id <code>&lt;div id="leo" class="good"&gt;</code></p>
<pre><code class="hljs bash" lang="bash">const reg = /id=<span class="hljs-string">".*?"</span>/
const reg2 = /id=<span class="hljs-string">"[^"</span>]*<span class="hljs-string">"/
</span></code></pre></li>
<li>
<p>trim</p>
<pre><code class="hljs bash" lang="bash">const trim = str =&gt; str.replace(/^\s+|\s+$/g, <span class="hljs-string">''</span>)
</code></pre></li>
<li>
<p>每个单词首字母大写</p>
<pre><code class="hljs bash" lang="bash">const toFirstUpper = str =&gt; str.toLowerCase().replace(/(?:^|\s)\w/g, c =&gt; c.toUpperCase())
</code></pre></li>
<li>
<p>驼峰下划线转换</p>
<pre><code class="hljs bash" lang="bash">const toUnderLine = str =&gt; str.replace(/(^\b[A-Z])|([A-Z])/g, (a, b, c) =&gt; {
  <span class="hljs-keyword">if</span>(a===b) <span class="hljs-built_in">return</span> a.toLowerCase()
  <span class="hljs-built_in">return</span> `_<span class="hljs-variable">${a.toLowerCase()}</span>`
})

const toHump = str =&gt; str.replace(/\_(\w)/g, (a,b,c) =&gt; b.toUpperCase())
</code></pre></li>
</ol>
<h3 class="heading">问题</h3>
<ol>
<li>
<p>将数组扁平化去并除其中重复部分数据，最终得到一个升序且不重复的数组</p>
<blockquote>
<p><code>const arr = [ [1, 2, 2], [3, 4, 5, 5], [6, 7, 8, 9, [11, 12, [12, 13, [14] ] ] ], 10];</code></p>
</blockquote>
<pre><code class="hljs bash" lang="bash">// ES6
[...new Set(arr.flat(Infinity))].sort((a,b) =&gt; a-b)

// flat 1
arr.toString().split(<span class="hljs-string">','</span>)
// flat 2
Array.prototype.flat = <span class="hljs-keyword">function</span> (arr) {
   <span class="hljs-built_in">return</span> [].concat(
     ...this.map((item) =&gt; (Array.isArray(item) ? item.flat() : [item]))
   );
 };
 // flat 3
 const flat = arr =&gt; {
   <span class="hljs-keyword">while</span>(arr.some(item =&gt; Array.isArray(item))) {
     arr = [].concat(...arr)
   }
   <span class="hljs-built_in">return</span> arr
 }
 // flat4
 const flat = arr =&gt; arr.reduce(
   (acc, cur) =&gt; Array.isArray ?
   [...acc, ...flat(cur)]
   : [...acc, cur],
   []
 )

 // unique
 [...new Set(arr)]
 const unique = arr =&gt; {
   const temp = []
   <span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0, ilen = arr.length; i&lt;ilen;i++) {
     // <span class="hljs-keyword">if</span>(arr.indexOf(arr[i]) === i) {
     //   temp.push(arr[i])
     // }
     <span class="hljs-keyword">if</span>(temp.indexOf(arr[i]) &lt; 0) {
       temp.push(arr[i])
     }
   }
 }

 // sort
 [].sort((a, b) =&gt; a-b)
</code></pre></li>
<li>
<p>sleep</p>
</li>
</ol>
<pre><code class="hljs bash" lang="bash">const sleep = time =&gt; new Promise(resolve =&gt; <span class="hljs-built_in">set</span>Timeout(resolve, time))
</code></pre><ol start="3">
<li>实现 (5).add(3).minus(2) 功能。<pre><code class="hljs bash" lang="bash">Number.prototype.add = <span class="hljs-keyword">function</span>(i=0) {
  <span class="hljs-built_in">return</span> this.valueOf() + i
}
Number.prototype.minus = <span class="hljs-keyword">function</span>(i=0) {
  <span class="hljs-built_in">return</span> this.valueOf() - i
}
</code></pre></li>
</ol>
<p>其他经典算法参考</p>
<pre><code class="hljs bash" lang="bash">合并 K 个有序链表
求数独
二叉树的层级遍历
二叉树的锯齿形层级遍历
字符串翻转
重排链表
二叉树插入节点
二叉搜索树节点删除
链表翻转
接雨水
旋转有序数组的峰值数字
有序矩阵的第 k 小数字
编辑距离
二分查找
找出小于并且最接近目标数字的数
寻找旋转排序数组中的最小值
不同路径
两两交换链表中的节点
山脉数组的峰顶索引
盛最多水的容器
</code></pre><p>本人才疏学浅，文中难免有不妥错误之处，还望同学们批评指正，感激不尽！</p>
<p><a target="_blank" href="https://github.com/chinadbo/Interview">GitHub Repo</a></p>
