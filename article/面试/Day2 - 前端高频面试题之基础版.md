url:https://juejin.cn/post/6844903870678695949
标题:Day2 - 前端高频面试题之基础版
描述:深拷贝则是开辟新的栈，不仅将原对象的各个属性逐一复制出去，而且会将属性所包含的对象也依次采用浅拷贝的方式递归复制到新对象中，拷贝了所有层级。 由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，所以不能滥用闭包，否则会造成网页的性能问题，在IE中可能导致内存泄露。解决方法…

<h4 class="heading">传送门&gt;&gt;&gt;</h4>
<p><a target="_blank" href="https://juejin.cn/post/6844903870036983821">Day1 - 前端高频面试题之基础版</a></p>
<p><a target="_blank" href="https://juejin.cn/post/6844903872121536519">Day3 - 前端高频面试题之基础版</a></p>
<hr>
<h4 class="heading">1、你了解浅拷贝、深拷贝吗？</h4>
<ul>
<li>浅拷贝是只复制一层对象的属性，不会进行递归复制，而js存储对象都是存地址的，所以浅拷贝会导致对象中的子对象指向同一块内存地址；</li>
<li>深拷贝则是开辟新的栈，不仅将原对象的各个属性逐一复制出去，而且会将属性所包含的对象也依次采用浅拷贝的方式递归复制到新对象中，拷贝了所有层级。</li>
</ul>
<p>浅拷贝的实现</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-keyword">var</span> obj = {
  <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">c</span>: [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
}

<span class="hljs-comment">// 浅拷贝</span>
<span class="hljs-comment">// 1、通过for-in方式实现</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">simpleCopy</span> (<span class="hljs-params">obj</span>) </span>{
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj != <span class="hljs-string">'object'</span>) {
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  }
  <span class="hljs-keyword">let</span> copyObj = {}
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> obj) {
    copyObj[i] = obj[i]
  }
  <span class="hljs-keyword">return</span> copyObj
}
simpleCopy(obj)	<span class="hljs-comment">// {"a":1,"b":2,"c":[3,4,5]}</span>

<span class="hljs-comment">// 2、通过属性描述符</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">simpleCopy2</span>(<span class="hljs-params">obj</span>) </span>{
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj != <span class="hljs-string">'object'</span>) {
    <span class="hljs-keyword">return</span>
  }
  <span class="hljs-keyword">let</span> copyObj = {}
  <span class="hljs-built_in">Object</span>.entries(obj).forEach(<span class="hljs-function"><span class="hljs-params">item</span> =&gt;</span> {
    copyObj[item[<span class="hljs-number">0</span>]] = item[<span class="hljs-number">1</span>]
  })
  <span class="hljs-keyword">return</span> copyObj
}
simpleCopy2(obj)

</code></pre><p>深拷贝的简易版本</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 1、JSON</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy1</span> (<span class="hljs-params">obj</span>) </span>{
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(obj))
}

<span class="hljs-comment">// 2、复制属性时，进行判断，如果是数组或者对象，则再次调用拷贝函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepCopy2</span>(<span class="hljs-params">obj, copyObj</span>) </span>{
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj != <span class="hljs-string">'object'</span>) {
    <span class="hljs-keyword">return</span>
  }
  <span class="hljs-keyword">var</span> copyObj = copyObj || {}
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> obj) {
    <span class="hljs-comment">// 过滤null</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> obj[i] === <span class="hljs-string">'object'</span> &amp;&amp; <span class="hljs-built_in">Object</span>.prototype.toString.call(obj[i]) !== <span class="hljs-string">'[object Null]'</span>) {
      copyObj[i] = <span class="hljs-built_in">Array</span>.isArray(obj[i]) ? [] : {}
      deepCopy2(obj[i], copyObj[i])
    } <span class="hljs-keyword">else</span> {
      copyObj[i] = obj[i]
    }
  }
  <span class="hljs-keyword">return</span> copyObj;
}
deepCopy2(obj)
</code></pre><p>推荐查看 <a target="_blank" href="https://lodash.com/docs/4.17.11#cloneDeep">lodash 的深拷贝函数</a></p>
<h4 class="heading">2、对闭包的理解？什么时候构成闭包？闭包的实现方法？闭包的优缺点？</h4>
<ul>
<li>闭包：闭包就是能够读取其他函数内部变量的函数</li>
<li>闭包的作用及好处：
<ul>
<li>一个是前面提到的可以读取函数内部的变量</li>
<li>一个就是让这些变量的值始终保持在内存中，不会在外部函数调用后被自动清除</li>
</ul>
</li>
<li>使用闭包的注意点：
<ul>
<li>由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，所以不能滥用闭包，否则会造成网页的性能问题，在IE中可能导致内存泄露。解决方法是，在退出函数之前，将不使用的局部变量全部删除。</li>
<li>闭包会在父函数外部，改变父函数内部变量的值。所以，如果你把父函数当作对象（object）使用，把闭包当作它的公用方法（Public Method），把内部变量当作它的私有属性（private value），这时一定要小心，不要随便改变父函数内部变量的值。</li>
</ul>
</li>
</ul>
<p>常见笔试题：</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 声明一个函数表达式</span>
<span class="hljs-keyword">var</span> add = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>)</span>{
    <span class="hljs-keyword">var</span> sum = x;
    <span class="hljs-comment">// 在函数表达式内部有一个求和的内部函数</span>
    <span class="hljs-keyword">var</span> tmp = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">y</span>)</span>{
        sum += y;<span class="hljs-comment">// 求和</span>
        <span class="hljs-keyword">return</span> tmp;
    }
    <span class="hljs-comment">// 构建一个函数体的toString()函数</span>
    tmp.toString = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>{
        <span class="hljs-keyword">return</span> sum;
    }
    <span class="hljs-keyword">return</span> tmp; <span class="hljs-comment">// JavaScript中，打印和相加计算，会分别调用toString或valueOf函数，所以我们重写tmp的toString和valueOf方法，返回sum的值</span>
}

add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">4</span>)   <span class="hljs-comment">// function 10</span>
<span class="hljs-keyword">var</span> a = add(<span class="hljs-number">1</span>)(<span class="hljs-number">2</span>)(<span class="hljs-number">3</span>)(<span class="hljs-number">4</span>).toString();  <span class="hljs-comment">//10</span>

<span class="hljs-comment">// 1、函数add(1)第一次调用，其实是只声明了var sum 这个变量，然后返回了tmp函数体，用于后面调用tmp函数</span>

<span class="hljs-comment">//2、函数add(1)(2)第二次调用才真正的把参数传进来使用了，即第一次传的&amp;emsp;1&amp;emsp;是没地方用的，没意义，第二次传的&amp;emsp;2&amp;emsp;是给第一次返回的tmp函数体传的参、即用在 sum=sum+x上 ---- sum=1+2</span>

<span class="hljs-comment">// 3、函数add(1)(2)(3)第三次调用和第二次一样，由于tmp函数体内部&amp;emsp;return tmp  返回了本身，所以后面可以继续调用tmp函数，也就是除第一次调用传参无效外，后面可以调用无数次，sum值会不断累加</span>

<span class="hljs-comment">// 4、toString是tmp函数体附带的属性方法函数，会随着主体函数toString执行一次调用一次</span>
</code></pre><h4 class="heading">3、如何理解原型？如何理解原型链？</h4>
<ol>
<li>
<p>每个函数在定义时都会自动带一个prototype属性，该属性是一个指针，指向一个对象，该对象称之为原型对象（通过prototype实现js的继承）。</p>
</li>
<li>
<p>原型对象上默认有一个属性constructor，指向该原型对象对应的构造函数。</p>
</li>
<li>
<p>通过调用构造函数创建的实例对象，都有一个内部属性__proto__，指向该构造函数的原型对象。其实例对象可以访问该原型对象上的所有属性和方法。</p>
</li>
<li>
<p>总结:</p>
<p>每个构造函数都有一个原型对象，原型对象上包含一个指向构造函数的指针，而实例对象都包含一个指向原型对象的内部指针。</p>
<p>通俗的说，实例对象通过内部指针__proto__访问到原型对象，原型对象通过constructor找到构造函数。</p>
<p>Foo.prototype只是一个指针，指向Foo的原型对象，利用这个指针可以实现JS的继承。</p>
</li>
</ol>
<p>原型链的作用：</p>
<ol>
<li>肯定是为了继承！</li>
<li>prototype用来实现基于原型的继承与属性的共享。</li>
<li>__proto__就构成了我们常说的原型链访问构造方法中的显示原型，同样用于实现基于原型的继承。</li>
</ol>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 面试题1:</span>
<span class="hljs-keyword">var</span> F = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{}
<span class="hljs-built_in">Object</span>.prototype.a = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{}
<span class="hljs-built_in">Function</span>.prototype.b = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{}

<span class="hljs-keyword">var</span> f = <span class="hljs-keyword">new</span> F()
<span class="hljs-comment">// 请问f有方法a  方法b吗</span>
f.a()	<span class="hljs-comment">// success	</span>
<span class="hljs-comment">// because:	f.__proto__ === F.prototype  F.prototype.__proto__ === Object.prototype  </span>

f.b()	<span class="hljs-comment">// f.b is not a function</span>
<span class="hljs-comment">// 	而f的原型链上没经过Function.prototype</span>

</code></pre><pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 面试题2:</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Foo</span> (<span class="hljs-params"></span>) </span>{}	<span class="hljs-comment">// 构造函数</span>
<span class="hljs-keyword">let</span> foo1 = <span class="hljs-keyword">new</span> Foo()	<span class="hljs-comment">// 实例对象</span>
<span class="hljs-keyword">let</span> foo2 = <span class="hljs-keyword">new</span> Foo()	<span class="hljs-comment">// 实例对象</span>
<span class="hljs-keyword">let</span> obj = {}
<span class="hljs-comment">// 写出 foo1  foo2  Foo  Function   obj   Object的原型链 ???</span>

foo1.__proto__ === Foo.prototype
foo2.__proto__ === Foo.prototype

Foo.__proto__ === <span class="hljs-built_in">Object</span>.prototype
Foo.prototype === <span class="hljs-built_in">Object</span>.prototype

Foo.prototype.__proto__ === <span class="hljs-built_in">Object</span>.prototype
Foo.prototype.constructor === Foo

<span class="hljs-comment">//  Function.prototype是引擎创造出来的对象，一开始就有了，又因为其他的构造函数都可以通过原型链找到Function.prototype，Function本身也是一个构造函数，为了不产生混乱，就将这两个联系到一起了</span>
<span class="hljs-built_in">Function</span>.__proto__ === <span class="hljs-built_in">Function</span>.prototype
<span class="hljs-built_in">Function</span>.prototype === <span class="hljs-built_in">Function</span>.prototype

<span class="hljs-built_in">Function</span>.prototype.__proto__ === <span class="hljs-built_in">Object</span>.prototype
<span class="hljs-built_in">Function</span>.prototype.constructor === <span class="hljs-built_in">Function</span>

obj.__proto__ === <span class="hljs-built_in">Object</span>.prototype

<span class="hljs-comment">// Object是对象的构造函数，那么它也是一个函数，当然它的__proto__也是指向Function.prototype</span>
<span class="hljs-built_in">Object</span>.__proto__ === <span class="hljs-built_in">Function</span>.prototype	
<span class="hljs-built_in">Object</span>.prototype === <span class="hljs-built_in">Object</span>.prototype

<span class="hljs-built_in">Object</span>.prototype.__proto__ === <span class="hljs-literal">null</span>
<span class="hljs-built_in">Object</span>.prototype.constructor === <span class="hljs-built_in">Object</span>

<span class="hljs-comment">// 构造函数有一个prototype属性，指向实例对象的原型对象</span>
Foo.prototype === foo1.__proto__

<span class="hljs-comment">// 通过同一个构造函数实例化的多个对象具有相同的原型对象</span>
foo1.__proto__ === foo2.__proto__

<span class="hljs-comment">// 原型对象上默认有一个属性constructor，指向该原型对象对应的构造函数</span>
Foo.prototype.constructor === Foo

foo1.__proto__.constructor === Foo

<span class="hljs-comment">// 由于实例对象可以继承原型对象的属性，所以实例对象也拥有constructor属性，同样指向原型对象对应的构造函数</span>
foo1.constructor === Foo

<span class="hljs-comment">// isPrototypeOf用来判断实例对象与原型对象的关系</span>
Foo.prototype.isPrototypeOf(f1)	<span class="hljs-comment">// true </span>

<span class="hljs-comment">// Object.getPrototypeOf() 返回该实例对象对应的原型对象，和proto是一样的，都返回原型对象</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(foo1)	<span class="hljs-comment">// Foo.prototype</span>
<span class="hljs-built_in">Object</span>.getPrototypeOf(foo1) === foo1.__proto__

<span class="hljs-comment">// in操作符可以判断某个属性在不在对象上，但无法区分是自有属性还是继承属性</span>
<span class="hljs-comment">// hasOwnPrototype可以判断该属性是自有属性还是继承属性</span>

</code></pre><h4 class="heading">4、创建对象有哪些方式？</h4>
<p>1、对象字面量方式</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-keyword">var</span> person = {
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Jack'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
    <span class="hljs-attr">sayName</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
    	alert(<span class="hljs-keyword">this</span>.name); 
		}
 }
<span class="hljs-comment">// 大量重复代码</span>
</code></pre><p>2、工厂模式</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span> (<span class="hljs-params">name, age</span>) </span>{
  <span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
  obj.name = name
  obj.age = age
  obj.alert = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
    alert(<span class="hljs-keyword">this</span>.name)
  }
  <span class="hljs-keyword">return</span> obj
}
<span class="hljs-keyword">var</span> a1 = a(<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>)
<span class="hljs-comment">// 工厂模式就是批量化生产, 由于是工厂暗箱操作的，所以你不能识别这个对象到底是什么类型</span>
</code></pre><p>3、构造函数（用来初始化新创建的对象的函数就是构造函数）</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params">name, age</span>) </span>{
  <span class="hljs-keyword">this</span>.name = name
  <span class="hljs-keyword">this</span>.age = age
  <span class="hljs-keyword">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
    alert(<span class="hljs-keyword">this</span>.name + <span class="hljs-keyword">this</span>.age)
  }
}
<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'xxx'</span>, <span class="hljs-number">22</span>)
<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'yyy'</span>, <span class="hljs-number">18</span>)

<span class="hljs-comment">// 拥有相同的功能的两个实例，却分配了不同的内存，浪费了内存空间</span>
p1.say === p2.say	<span class="hljs-comment">// false</span>

----------

<span class="hljs-comment">// 构造函数拓展模式</span>
<span class="hljs-comment">// 把方法转移到构造函数外部，可以解决方法被重复创建的问题。</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params">name, age</span>) </span>{
  <span class="hljs-keyword">this</span>.name = name
  <span class="hljs-keyword">this</span>.age = age
  <span class="hljs-keyword">this</span>.say = say
}
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span> (<span class="hljs-params"></span>) </span>{
  alert(<span class="hljs-keyword">this</span>.name + <span class="hljs-keyword">this</span>.age)
}
<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'xxx'</span>, <span class="hljs-number">22</span>)
<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'yyy'</span>, <span class="hljs-number">18</span>)
p1.say === p2.say	<span class="hljs-comment">// true</span>

<span class="hljs-comment">// 但是这是在全局作用域中定义，而且只供一个对象调用，不符合全局作用域的定义规范；并且如果有多个方法时，就要多个全局函数，严重污染全局空间。</span>

-------------
<span class="hljs-comment">// 寄生构造函数模式(是工厂模式和构造函数模式的结合)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span> (<span class="hljs-params">name, age</span>) </span>{
  <span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
  obj.name = name
  obj.age = age
  obj.alert = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
    alert(<span class="hljs-keyword">this</span>.name)
  }
  <span class="hljs-keyword">return</span> obj
}
<span class="hljs-keyword">var</span> a1 = <span class="hljs-keyword">new</span> A(<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>)
<span class="hljs-keyword">var</span> a2 = <span class="hljs-keyword">new</span> A(<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>)

<span class="hljs-comment">// 寄生构造函数模式与构造函数模式有相同的问题，每个方法都要在每个实例上重新创建一遍，创建多个完成相同任务的方法完全没有必要，浪费内存空间</span>
a1.alert === a2.alert	<span class="hljs-comment">// false</span>

<span class="hljs-comment">// 使用该模式返回的对象与构造函数之间没有关系。因此，使用instanceof运算符和prototype属性都没有意义</span>
a1.__proto === A.prototype	<span class="hljs-comment">// false</span>
</code></pre><p>4、原型模式</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params"></span>) </span>{}
Person.prototype = {
  <span class="hljs-attr">constructor</span>: Person,	<span class="hljs-comment">// 显示设置原型对象的constructor属性</span>
  name: <span class="hljs-string">'xxx'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>,
  <span class="hljs-attr">favoraties</span>: [],
  <span class="hljs-attr">say</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
    alert(<span class="hljs-keyword">this</span>.name + <span class="hljs-keyword">this</span>.age)
  }
}

<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person()
<span class="hljs-keyword">var</span> p2 = <span class="hljs-keyword">new</span> Person()

p1.favoraties.push(<span class="hljs-string">'sing'</span>)
p2.favoraties.push(<span class="hljs-string">'song'</span>)
p1.favoraties	<span class="hljs-comment">// ["sing", "song"]</span>
p2.favoraties	<span class="hljs-comment">// ["sing", "song"]</span>

<span class="hljs-comment">// 引用类型的值在原型对象上会被共享，修改一个实例的值，也会改变其他实例的变化</span>

</code></pre><p>5、组合使用构造模式和原型模式</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params">name, age</span>) </span>{
  <span class="hljs-keyword">this</span>.name = name
  <span class="hljs-keyword">this</span>.age = age
  <span class="hljs-keyword">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
    alert(<span class="hljs-keyword">this</span>.age)
  }
}
Person.prototype = {
  <span class="hljs-attr">constructor</span>: Person,
  <span class="hljs-attr">totalHobby</span>: <span class="hljs-string">'running'</span>,
  <span class="hljs-attr">sing</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
    alert(<span class="hljs-keyword">this</span>.name)
  }
}

<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'xxx'</span>, <span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'yyy'</span>, <span class="hljs-number">18</span>)

<span class="hljs-comment">// 将独立的属性和方法放在构造函数中，需要共享的属性和方法放在原型对象中，还支持向构造函数传递参数，这样可以最大限度的节省内存而又保留实例对象的独立性</span>

----------
<span class="hljs-comment">// 动态原型模式</span>
<span class="hljs-comment">// 动态原型模式将组合模式中分开使用的构造函数和原型对象都封装到了构造函数中，然后通过检查方法是否被创建，来决定是否初始化原型对象，也减少了全局空间的污染</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span> (<span class="hljs-params">name, age</span>) </span>{
  <span class="hljs-keyword">this</span>.name = name
  <span class="hljs-keyword">this</span>.age = age
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-keyword">this</span>.say != <span class="hljs-string">'function'</span>) {
    <span class="hljs-keyword">this</span>.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
      alert(<span class="hljs-keyword">this</span>.age)
    }
  }
}
<span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'name'</span>, <span class="hljs-string">'age'</span>)
p1.say()	
</code></pre><h4 class="heading">5、实现继承的多种方式和优缺点</h4>
<p>1、原型继承</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 原型继承	(本质就是重写原型对象，代之以一个新类型的实例)</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Super</span> (<span class="hljs-params"></span>) </span>{
  <span class="hljs-keyword">this</span>.value = <span class="hljs-literal">true</span>
  <span class="hljs-keyword">this</span>.colors = [<span class="hljs-string">'red'</span>]
}
Super.prototype.getValue = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.value
}
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Sub</span> (<span class="hljs-params"></span>) </span>{}
Sub.prototype = <span class="hljs-keyword">new</span> Super()	<span class="hljs-comment">// here</span>
Sub.prototype.constructor = Sub

<span class="hljs-keyword">var</span> instance = <span class="hljs-keyword">new</span> Sub()
instance.getValue()	<span class="hljs-comment">// true</span>

<span class="hljs-keyword">var</span> instance2 = <span class="hljs-keyword">new</span> Sub()
instance.colors.push(<span class="hljs-string">'green'</span>)

instance.colors	<span class="hljs-comment">//&nbsp;["red", "green"]</span>
instance2.colors	<span class="hljs-comment">//&nbsp;["red", "green"]</span>


<span class="hljs-comment">// 第一个缺点是所有子类共享父类的实例，其中一个子类修改了父类中引用对象的值，其他子类的属性值也会被修改</span>
<span class="hljs-comment">// 第二个缺点是在构造子类实例的时候，不能给父类传递参数。实际上，是没有办法在不影响所有对象实例的情况下，给父类传递参数。</span>
</code></pre><p>2、构造函数实现继承</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 构造函数继承，也叫做 伪类继承 或 经典继承 （本质就是在子类构造函数内部借用call/apply方法调用父类的构造函数）</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Super</span> (<span class="hljs-params">name, colors</span>) </span>{
  <span class="hljs-keyword">this</span>.name = name
  <span class="hljs-keyword">this</span>.colors = colors
}
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Sub</span> (<span class="hljs-params"></span>) </span>{
  <span class="hljs-comment">// 继承了Super</span>
  Super.call(<span class="hljs-keyword">this</span>, <span class="hljs-string">'xyz'</span>, [<span class="hljs-string">'red'</span>])
}
<span class="hljs-keyword">var</span> instance1 = <span class="hljs-keyword">new</span> Sub()
instance1.name	<span class="hljs-comment">// xyz</span>

instance1.colors.push(<span class="hljs-string">'white'</span>)
instance1.colors	<span class="hljs-comment">// ['red', 'white']</span>

<span class="hljs-keyword">var</span> instance2 = <span class="hljs-keyword">new</span> Sub()
instance2.colors	<span class="hljs-comment">// ['red']</span>
<span class="hljs-comment">// 相对于原型继承来说，有一个很大的优势就是可以传递参数给父类，并且也可以解决引用类型实例属性共享的问题。</span>
<span class="hljs-comment">// 缺点是方法都定义在构造函数内部，无法复用</span>
</code></pre><p>3、组合式继承</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 组合继承（原型继承+构造函数继承）</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Super</span> (<span class="hljs-params">name</span>) </span>{
  <span class="hljs-keyword">this</span>.name = name
  <span class="hljs-keyword">this</span>.colors = [<span class="hljs-string">'red'</span>]
}
Super.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
	<span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.name
}

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Sub</span> (<span class="hljs-params">name, age</span>) </span>{
  <span class="hljs-comment">// 继承属性</span>
  <span class="hljs-comment">// 第二次调用父类构造函数，Sub.prototype得到了name和colors，并覆盖了第一次得到的属性</span>
  Super.call(<span class="hljs-keyword">this</span>, name)
  <span class="hljs-keyword">this</span>.age = age
}
<span class="hljs-comment">// 继承方法</span>
<span class="hljs-comment">// 第一次调用父类构造函数，Sub.prototype得到了内部属性name，colors</span>
Sub.prototype = <span class="hljs-keyword">new</span> Super(<span class="hljs-string">'xyz'</span>)
Sub.prototype.constructor = Sub
<span class="hljs-comment">// 子类自己的方法</span>
Sub.prototype.getAge = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.age
}

<span class="hljs-keyword">var</span> instance1 = <span class="hljs-keyword">new</span> Sub(<span class="hljs-string">'xyz'</span>, <span class="hljs-number">22</span>)
instance1.getName()	<span class="hljs-comment">// xyz</span>
instance1.getAge()	<span class="hljs-comment">// 22</span>
instance1.colors.push(<span class="hljs-string">'white'</span>)
instance1.colors	<span class="hljs-comment">// ['red', 'white']</span>

<span class="hljs-keyword">var</span> instance2 = <span class="hljs-keyword">new</span> Sub(<span class="hljs-string">'zzz'</span>, <span class="hljs-number">18</span>)
instance2.colors	<span class="hljs-comment">// ['red']</span>

<span class="hljs-comment">// 缺点是无论什么情况下，总会调用两次父类构造函数。第一次是在创建子类原型的时候，第二次是在子类构造函数内部</span>
<span class="hljs-comment">// 占用的空间更大了</span>
</code></pre><p>4、寄生组合式继承</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// 寄生组合式继承，解决了调用两次父类构造函数的问题</span>
<span class="hljs-comment">// 也是借用构造函数来继承不可共享的属性，通过原型链的混成形式来继承方法和可共享的属性。只不过把原型继承改成了寄生式继承。</span>
<span class="hljs-comment">// 使用寄生组合继承可以不必为了指定子类的原型而调用父类的构造函数，所以只继承了父类的原型属性，而父类的实例属性是借用构造函数的方式来得到的。</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Super</span> (<span class="hljs-params">name</span>) </span>{
  <span class="hljs-keyword">this</span>.name = name
  <span class="hljs-keyword">this</span>.colors = [<span class="hljs-string">'red'</span>]
}
Super.prototype.getName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>{
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.name
}

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Sub</span> (<span class="hljs-params">name, age</span>) </span>{
  Super.call(<span class="hljs-keyword">this</span>, name)
  <span class="hljs-keyword">this</span>.age = age
}

<span class="hljs-comment">// 本质上，是对传入的对象进行了一次浅复制</span>
<span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Object</span>.create){
  <span class="hljs-built_in">Object</span>.create = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">proto</span>) </span>{
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>) </span>{}	<span class="hljs-comment">// 临时的构造函数</span>
    F.prototype = proto	<span class="hljs-comment">// 将传进来的参数作为这个构造函数的原型</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F()	<span class="hljs-comment">// 返回这个构造函数的新实例</span>
  }
}

Sub.prototype = <span class="hljs-built_in">Object</span>.create(Super.prototype)
Sub.prototype.constructor = Sub

<span class="hljs-keyword">var</span> instance1 = <span class="hljs-keyword">new</span> Sub(<span class="hljs-string">'xyz'</span>, <span class="hljs-number">18</span>)
instance1.getName()	<span class="hljs-comment">// xyz</span>
instance1.colors.push(<span class="hljs-string">'white'</span>)
instance1.colors	<span class="hljs-comment">// ['red', 'white']</span>

<span class="hljs-keyword">var</span> instance2 = <span class="hljs-keyword">new</span> Sub(<span class="hljs-string">'xyz2'</span>, <span class="hljs-number">22</span>)
instance2.colors	<span class="hljs-comment">// ['red']</span>

<span class="hljs-comment">// 高效率体现在只调用了一次Super构造函数，并且因此避免了在Sub.prototype上创建不必要的、多余的属性。而且原型链不变</span>

</code></pre><p>ES5的继承 是通过原型或构造函数机制来实现，实质上是先创建子类的实例对象，然后再将父类的方法添加到this上（Parent.apply(this)）。</p>
<p>5、es6中的class
ES6封装了class，extends关键字来实现继承，实质上是先创建父类的实例对象this（所以必须先调用父类的super()方法），然后再用子类的构造函数修改this。</p>
<pre><code class="hljs javascript" lang="javascript"><span class="hljs-comment">// class</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Super</span> </span>{
  <span class="hljs-keyword">constructor</span> (name) {
    <span class="hljs-keyword">this</span>.name = name
    <span class="hljs-keyword">this</span>.colors = [<span class="hljs-string">'red'</span>]
  }
	
  getName () {
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.name
  }
}

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Sub</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Super</span> </span>{
  <span class="hljs-keyword">constructor</span> (name, age) {
    <span class="hljs-keyword">super</span>(name)
    <span class="hljs-keyword">this</span>.age = age
  }
  getAge () {
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.age
  }
}

<span class="hljs-keyword">var</span> instance1 = <span class="hljs-keyword">new</span> Sub(<span class="hljs-string">'xyz'</span>, <span class="hljs-number">18</span>)
instance1.colors.push(<span class="hljs-string">'white'</span>)
instance1.colors	<span class="hljs-comment">// ['red', 'white']</span>
instance1.getName()	<span class="hljs-comment">// xyz</span>

<span class="hljs-keyword">var</span> instance2 = <span class="hljs-keyword">new</span> Sub(<span class="hljs-string">'xyz2'</span>, <span class="hljs-number">22</span>)
instance2.colors	<span class="hljs-comment">// ['red']</span>
instance2.getAge()	<span class="hljs-comment">// 22</span>

</code></pre>