标题:前端面试之理解原型/构造函数/实例(JavaScript篇)
描述:构造函数：用来初始化新创建的对象的函数是构造函数。 每一个构造函数都有一个原型对象即prototype(指针)指向的对象。 而原型对象也有一个属性constructor(构造器)指向构造函数。 通过构造函数的new操作创建的对象是实例对象。可以用一个构造函数，构造多个实例对象。…

<h2 class="heading">图解</h2>
<p></p><figure><img alt="图" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/20/16a3a02995caef31~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h2 class="heading">概念</h2>
<blockquote>
<p>构造函数</p>
</blockquote>
<p>构造函数：用来初始化新创建的对象的函数是构造函数。</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">Foo</span></span> () {
    ...
}
</code></pre><p>每一个构造函数都有一个原型对象即prototype(指针)指向的对象。
而原型对象也有一个属性constructor(构造器)指向构造函数。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/20/16a3a07adbbb037a~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<blockquote>
<p>实例对象</p>
</blockquote>
<p>通过构造函数的new操作创建的对象是实例对象。可以用一个构造函数，构造多个实例对象。</p>
<pre><code class="hljs bash" lang="bash">const f1 = new Foo()
const f2 = new Foo()
</code></pre><p>实例对象也有有一个__proto__(非标准顺序)属性。该属性指向实例对象的原型对象。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/20/16a3a0e8f7fb437a~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<blockquote>
<p>原型</p>
</blockquote>
<p>构造函数通过 new 操作符来创建一个实例 ， 实例又可以通过内部指针 proto 指向原型对象。
proto 连接的这一条原型对象就构成了原型链。</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">A</span></span> () {
}

<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">B</span></span> () {

}
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">C</span></span> () {

}

B.prototype = new A()
C.prototype = new B()

const c = new C()

console.log(
  c.__proto__ ===  C.prototype,  //  <span class="hljs-literal">true</span>
  C.prototype.__proto__ === B.prototype,  // <span class="hljs-literal">true</span>
  B.prototype.__proto__ === A.prototype,  // <span class="hljs-literal">true</span>
  A.prototype.__proto__ === Object.prototype, // <span class="hljs-literal">true</span>
  Object.prototype.__proto__ === null // <span class="hljs-literal">true</span>
)


</code></pre><p>原型链最顶端就是Object.prototype。
而Object.prototype的原型对象是null。</p>
