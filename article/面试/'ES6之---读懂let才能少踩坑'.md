标题:ES6之---读懂let才能少踩坑
描述:在刚接触ES6的时候，我就「以为」我理解了let。然后漫长的自学道路上，let一次又一次的让我认识到了自己的无知。 希望写了这篇文章之后能用我的无知，让在这条道路上的人能少踩些坑。 和很多人一样，在听说了ES6很好用之后，就马不停蹄的去学习这门充满着语法糖的东西。开始抱着emm…

<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/4/20/162e2df2264b297c~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h1 class="heading">开聊吧！(前面一小部分大佬们可以自动忽略)</h1>
<p><strong>首先，打脸我的无知！</strong></p>
<p>在刚接触ES6的时候，我就「以为」我理解了let。然后漫长的自学道路上，<strong>let</strong>一次又一次的让我认识到了自己的无知。</p>
<h3 class="heading">希望写了这篇文章之后能用我的无知，让在这条道路上的人能少踩些坑。</h3>
<hr>
<h2 class="heading">初识let</h2>
<p>和很多人一样，在听说了ES6很好用之后，就马不停蹄的去学习这门充满着语法糖的东西。开始抱着emmmm快速把es6过一遍的念头去了菜鸟教程（因为觉得这里的教程很简洁，但是希望大家以后慎重选择初学教程！！！）</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/4/20/162e2f19a4731084~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
如图所示，这就是我对他的初始理解---一个解决javascript没有块级作用域的东西。嗯....就是这样也仅此而已。<p></p>
<h2 class="heading">let浅解</h2>
<h3 class="heading">《1》let 声明的变量的作用域是块级的；</h3>
<pre><code class="hljs bash" lang="bash">{
  <span class="hljs-built_in">let</span> a = 10;
  var b = 1;
}

a // ReferenceError: a is not defined.
b // 1
</code></pre><p>用法类似于var，但是所声明的变量，只在let命令所在的代码块内有效.</p>
<h3 class="heading">说说这个「块级作用域」里面的坑吧！！！</h3>
<p>首先，用阮大神的一个示例来说说过第一个坑</p>
<pre><code class="hljs bash" lang="bash">var a = [];
<span class="hljs-keyword">for</span> (var i = 0; i &lt; 10; i++) {
  a[i] = <span class="hljs-function"><span class="hljs-title">function</span></span> () {
    console.log(i);
  };
}
a[6](); 
</code></pre><p>输出几呢？是6吗？ <strong>答案是</strong>10</p>
<p>为什么呢？因为上面代码中，变量i是var命令声明的，在全局范围内都有效，所以全局只有一个变量i。每一次循环，变量i的值都会发生改变，而循环内被赋给数组a的函数内部的console.log(i)，里面的i指向的就是全局的i。也就是说，所有数组a的成员里面的i，指向的都是同一个i，导致运行时输出的是最后一轮的i的值，也就是 10。</p>
<p>那么怎么解决呢？
ES6之前的解决方式--构造闭包形成不销毁的作用域保存变量</p>
<pre><code class="hljs bash" lang="bash">var a = [];
<span class="hljs-keyword">for</span> (var i = 0; i &lt; 10; i++) {
  (<span class="hljs-keyword">function</span> (arg) {a[i] = <span class="hljs-function"><span class="hljs-title">function</span></span> () {
    console.log(arg);
  }})(i);
}
a[6](); //6
</code></pre><p>ES6的解决方式</p>
<pre><code class="hljs bash" lang="bash">var a = [];
<span class="hljs-keyword">for</span> (<span class="hljs-built_in">let</span> i = 0; i &lt; 10; i++) {
  a[i] = <span class="hljs-function"><span class="hljs-title">function</span></span> () {
    console.log(i);
  };
}
a[6](); // 6
</code></pre><p>代码中，变量i是let声明的，当前的i只在本轮循环有效，所以每一次循环的i其实都是一个新的变量，所以最后输出的是6。
<strong>用ES5的代码描述就是这样的！</strong></p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-string">"use strict"</span>;

var a = [];

var _loop = <span class="hljs-keyword">function</span> _loop(i) {
  a[i] = <span class="hljs-function"><span class="hljs-title">function</span></span> () {
    console.log(i);
  };
};

<span class="hljs-keyword">for</span> (var i = 0; i &lt; 10; i++) {
  _loop(i);
}
a[6](); // 6
</code></pre><h3 class="heading">再来一个平常码代码经常会遇到的，面试也会经常遇到。</h3>
<pre><code class="hljs bash" lang="bash">var liList = document.querySelectorAll(<span class="hljs-string">'li'</span>) // 共5个li
<span class="hljs-keyword">for</span>( var i=0; i&lt;liList.length; i++){
  liList[i].onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>(){
    console.log(i)
  }
}
</code></pre><p>打印多少呢？0，1，2，3，4 还是 5，5，5，5，5？
相信大家大家应该都知道依次点击 li 会打印出 5 个 5。</p>
<p>如果把 var i 改成 let i，就会分别打印出 0、1、2、3、4：</p>
<pre><code class="hljs bash" lang="bash">var liList = document.querySelectorAll(<span class="hljs-string">'li'</span>) // 共5个li
<span class="hljs-keyword">for</span>( <span class="hljs-built_in">let</span> i=0; i&lt;liList.length; i++){
  liList[i].onclick = <span class="hljs-function"><span class="hljs-title">function</span></span>(){
    console.log(i)
  }
}
</code></pre><p>阐述一下我的理解吧！</p>
<ul>
<li>for( let i = 0; i&lt; 5; i++) 这句话的圆括号之间，有一个隐藏的作用域。</li>
<li>for( let i = 0; i&lt; 5; i++) { 循环体 } 在每次执行循环体之前，JS 引擎会把 i 在循环体的上下文中重新声明及初始化一次。</li>
<li><strong>用ES5的代码描述就是这样的！</strong></li>
</ul>
<pre><code class="hljs bash" lang="bash"><span class="hljs-string">'use strict'</span>;

var liList = document.querySelectorAll(<span class="hljs-string">'li'</span>); // 共5个li

var _loop = <span class="hljs-keyword">function</span> _loop(i) {
  liList[i].onclick = <span class="hljs-function"><span class="hljs-title">function</span></span> () {
    console.log(i);
  };
};

<span class="hljs-keyword">for</span> (var i = 0; i &lt; liList.length; i++) {
  _loop(i);
}
</code></pre><p><strong>总结：希望大家在已有遇到跟循环  异步事件之类的问题的时候多注意下，不要掉坑里了☺</strong></p>
<h3 class="heading">《2》let 声明的变量不存在变量提升，有暂时性死区；</h3>
<p>先来解释解释这两个吧</p>
<p>变量提升</p>
<pre><code class="hljs bash" lang="bash">console.log(foo); // 输出undefined
console.log(bar); // 报错ReferenceError

var foo = 2;
<span class="hljs-built_in">let</span> bar = 2;
</code></pre><p>let不像var那样会发生“变量提升”现象。所以，变量一定要在声明后使用，否则报错。</p>
<p>暂时性死区</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-built_in">let</span> x = <span class="hljs-string">'global'</span>
{
  console.log(x) // Uncaught ReferenceError: x is not defined
  <span class="hljs-built_in">let</span> x = 1
}
</code></pre><p>存在全局变量x，但是块级作用域内let又声明了一个局部变量x，导致后者绑定这个块级作用域，所以在let声明变量前，对tmp赋值会报错。</p>
<p>在详细的解释这个问题之前，我们先来弄懂ES6之前，我们的作用域里的变量预解释。</p>
<pre><code class="hljs bash" lang="bash">var a = 1;
<span class="hljs-keyword">function</span> b(params) {
    var c = 2; 
    console.log(params);
}

console.log(a);
b(3);
</code></pre><p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/4/20/162e34e89ccde81a~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
红色框框中的部分是在b函数被调用的时候才会按照预解释规则一步步产生，现在写出来是为了方便你们理解。正因为b函数被预先声明且赋值了，所以在b函数之前调用他就能得到结果，代码如下,相信你又学到不少吧！<p></p>
<pre><code class="hljs bash" lang="bash">b(3);
<span class="hljs-keyword">function</span> b(params) {
    var c = 2; 
    console.log(params);
}

</code></pre><p>然后就是函数执行的第二步了</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/4/20/162e356ebafd35a7~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
够清楚！！！！够明了吧！！！<p></p>
<p>这个我们弄清楚了 就再把let的说一遍 那么上面的问题你自然就豁然开朗了。</p>
<blockquote>
<p>关于let的是这样的</p>
</blockquote>
<blockquote>
<p>&lt;1&gt;找到所有用 let 声明的变量，在环境中「创建」这些变量</p>
</blockquote>
<blockquote>
<p>&lt;2&gt;开始执行代码（注意现在还没有初始化也没有假装赋值为undefined）</p>
</blockquote>
<blockquote>
<p>&lt;3&gt;执行 let声明的变量时，将 该变量 「初始化直接赋值」</p>
</blockquote>
<p><strong>现在关于上面的不存在变量提升，有暂时性死区你应该都懂了吧。关于暂时性死区是因为let声明的变量有块级作用域而且没有变量提升所以就产生了</strong></p>
<p>也来看看暂时性死区在es6之前的环境里是怎样的吧。</p>
<pre><code class="hljs bash" lang="bash">//es6中
<span class="hljs-built_in">let</span> x = <span class="hljs-string">'global'</span>
{
  console.log(x) // Uncaught ReferenceError: x is not defined
  <span class="hljs-built_in">let</span> x = 1
}

//之前版本的环境中
<span class="hljs-string">'use strict'</span>;

var x = <span class="hljs-string">'global'</span>;
{
  console.log(_x); // Uncaught ReferenceError: x is not defined
  var _x = 1;
}

</code></pre><h3 class="heading">《3》let 不能重复声明已存在的变量</h3>
<p>这个知识点就基本没啥坑了  自己注意点儿就好</p>
<pre><code class="hljs bash" lang="bash">// 报错
<span class="hljs-function"><span class="hljs-title">function</span></span> () {
  <span class="hljs-built_in">let</span> a = 10;
  var a = 1;
}

// 报错
<span class="hljs-function"><span class="hljs-title">function</span></span> () {
  <span class="hljs-built_in">let</span> a = 10;
  <span class="hljs-built_in">let</span> a = 1;
}
</code></pre><h2 class="heading">总结</h2>
<blockquote>
<p>总共也就三个知识点：完全掌握还是要多用！！！</p>
</blockquote>
<blockquote>
<p>1、let的块级作用域！</p>
</blockquote>
<blockquote>
<p>2、let声明的变量不存在变量提升，有暂时性死区！</p>
</blockquote>
<blockquote>
<p>3、let声明的变量不允许重复声明，无论重复用var或者其他声明都不行！</p>
</blockquote>
<blockquote>
<p>let的故事就这样暂时说完啦(疯狂求有位大佬来带带我啊)  不知不觉又晚上10点多了 该回寝室了 哈哈  如果学到了就给我个小心心吧 哈哈哈</p>
</blockquote>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/4/20/162e369d5d40ff99~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
