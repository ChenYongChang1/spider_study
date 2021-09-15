标题:2020年大前端面试题库+答案（第3章） javaScript判断对象类型
描述:从上面可以看出，typeof 判断对象和数组都返回object,因此它无法区分对象和数组。 因为数组属于Object的一种， 所以[] instanceof object,也是成立的。 instanceof 不能区分基本类型string 和 boolean,除非是字符串对象和布…

<h3 class="heading">1.typeof</h3>
<p><code>typeof</code>只能判断区分基本类型，如：number、string、boolean、undefined和object、function</p>
<pre><code class="hljs bash" lang="bash">    typeof 0; //number
    typeof <span class="hljs-literal">true</span>; //boolean
    typeof undefined; //undefined
    typeof <span class="hljs-string">"hello world"</span>; //string
    typeof <span class="hljs-function"><span class="hljs-title">function</span></span>(){}; //<span class="hljs-keyword">function</span>
    
    typeof null; //object
    typeof {}; //object
    typeof []; //object
</code></pre><p>从上面可以看出，typeof 判断对象和数组都返回object,因此它无法区分对象和数组。</p>
<h3 class="heading">2.instanceof</h3>
<pre><code class="hljs bash" lang="bash">    var a = {};
    a instanceof Array //<span class="hljs-literal">false</span>
    a instanceof Object //<span class="hljs-literal">true</span>
    var b = []
    b instanceof Array //<span class="hljs-literal">true</span>
    b instanceof Object //<span class="hljs-literal">true</span>
</code></pre><p>因为数组属于Object的一种， 所以<code>[] instanceof object</code>,也是成立的。</p>
<pre><code class="hljs bash" lang="bash">    var c = <span class="hljs-string">'abc'</span>;
    c instanceif String //<span class="hljs-literal">false</span>
    var d = new String();
    d instanceof String //<span class="hljs-literal">true</span>
</code></pre><p>instanceof 不能区分基本类型string 和 boolean,除非是字符串对象和布尔对象。 如上例所示。</p>
<h3 class="heading">3.constructor</h3>
<pre><code class="hljs bash" lang="bash">    var o = {};
    o.constructor == Object //<span class="hljs-literal">true</span>
    var arr = [];
    arr.constructor == Array // <span class="hljs-literal">true</span>
    arr.constructor == Object //<span class="hljs-literal">false</span>
</code></pre><p>可以看出constructor可以区分Array和Object.</p>
<pre><code class="hljs bash" lang="bash">    var n = <span class="hljs-literal">true</span>;
    n.constructor == Boolean //<span class="hljs-literal">true</span>
    var num = 1;
    num.constructor == Number //<span class="hljs-literal">true</span>
    var str = <span class="hljs-string">'hello world'</span>
    str.constructor == String
    
    var num = new Number();
    
    num.constructor == Number //<span class="hljs-literal">true</span>
</code></pre><p>不过要注意，constructor 属性是可以被修改的，会导致检测出的结果不正确</p>
<pre><code class="hljs bash" lang="bash">    <span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">Person</span></span>(){}
    <span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">Student</span></span>(){}
    Student.prototype = new Person();
    var John = new Student();
    console.log(John.constructor == Student) //<span class="hljs-literal">false</span>
    console.log(john.constructor == Person) //<span class="hljs-literal">true</span>
</code></pre><p>除了undefined 和 null,其他类型变量均能使用constructor判断出类型.</p>
<h3 class="heading">4.Object.prototype.toString.call()------------最好用</h3>
<pre><code class="hljs bash" lang="bash">Object.prototype.toString.call(123) //<span class="hljs-string">"[object Number]"</span>

object.prototype.toString.call(<span class="hljs-string">'str'</span>)  //<span class="hljs-string">"[object String]"</span>

object.prototype.toString.call(<span class="hljs-string">'true'</span>)  //<span class="hljs-string">"[object Boolean]"</span>

object.prototype.toString.call({})  //<span class="hljs-string">"[object Object]"</span>

object.prototype.toString.call([])  //<span class="hljs-string">'[object Array]'</span>
</code></pre><p>这里可以封装一个判断数组和对象的方法</p>
<pre><code class="hljs bash" lang="bash">    <span class="hljs-keyword">function</span> <span class="hljs-built_in">type</span>Obj(obj){
        var <span class="hljs-built_in">type</span> = Object.prototype.toString.call(obj);
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">type</span> == <span class="hljs-string">'[object Array]'</span>){
            <span class="hljs-built_in">return</span> <span class="hljs-string">"Array"</span>
        }<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">type</span> == <span class="hljs-string">"[object Object]"</span>){
            <span class="hljs-built_in">return</span> <span class="hljs-string">"Object"</span>
        }<span class="hljs-keyword">else</span>{
            <span class="hljs-built_in">return</span> <span class="hljs-string">"obj is not object or array"</span>
        }
    }
</code></pre><p><code>Object.prototype.toString()</code>方法在被调用的时候，会执行如下的操作步骤：</p>
<ul>
<li>1.获取对象的类名 （对象类型）<br>
<code>[[Class]]</code>是一个内部属性，所有的对象（原生对象和宿主对象）都有该属性，在规范中，[[Class]]是这么定义的：<br>
内部属性，<code>[[Class]]</code> 一个字符串值，表明该对象的类型。</li>
<li>2.然后将[object 获取的对象类型的名] 组合为字符串</li>
<li>3.返回字符串 <code>"[object Array]"</code></li>
</ul>
<h3 class="heading">5.jQuery中的<code>$.type</code>接口</h3>
<ul>
<li>$.type(obj)</li>
<li>$.isArray(obj)</li>
<li>$.isFunction(obj)</li>
<li>$.isPlainObjext(obj)</li>
</ul>
<pre><code class="hljs bash" lang="bash">    $.type([]) //array
    $.isArray([]) //<span class="hljs-literal">true</span>
    $.isFunction(<span class="hljs-function"><span class="hljs-title">function</span></span>(){}) <span class="hljs-literal">true</span>
    $.isPlainObject({}) //<span class="hljs-literal">true</span>
    $.isPlanObject([]) //<span class="hljs-literal">false</span>
</code></pre><p>每章语录：不要吹灭你的灵感和你的想象力; 不要成为你的模型的奴隶。<br>
——文森特・梵高<br>
摘自：<a target="_blank" href="">cnblogs.com/sunmarvell/p/9386075.html</a></p>
