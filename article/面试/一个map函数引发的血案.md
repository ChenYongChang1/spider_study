url:https://juejin.cn/post/6844903822347730951
标题:一个map函数引发的血案
描述:本文写作目的在于，对上次面试中未手写出来的map函数做一个收尾工作。其内容以map函数作为线，将其涉及到的众多知识点穿针引线梳理一下，并赋予本人学习及写作时的所感所想。既是所感所想，想必难免存在一些个人拙见，望各位大佬不吝指正，还望轻喷！！！ 大学简单学过C语言后，第一次看到这…

<h3 class="heading">前言</h3>
<hr>
<p>本文写作目的在于，对上次面试中未手写出来的map函数做一个收尾工作。其内容以map函数作为线，将其涉及到的众多知识点穿针引线梳理一下，并赋予本人学习及写作时的所感所想。既是所感所想，想必难免存在一些个人拙见，<strong>望各位大佬不吝指正，还望轻喷</strong>！！！</p>
<h3 class="heading">map函数是个黑盒</h3>
<hr>
<p>还记得初识JS的map函数时</p>
<pre><code class="hljs bash" lang="bash">[1,2,3].map((e, i, arr) =&gt; {
    <span class="hljs-built_in">return</span> 2*e;  //[2,4,6]
})
</code></pre><p>大学简单学过C语言后，第一次看到这个用法就感觉特别神奇，完全不知道它怎么运作，仅对它形成了一个大致的轮廓：你想基于原数组生成一个怎样的新数组，只要把逻辑写在回调函数里就好了。对我而言它完全就像一个黑盒。但不觉间潜意识里却模糊了一些概念(<strong>已然与未然/主动与被动的关系</strong>)。</p>
<h3 class="heading">对不起，map函数实现不来</h3>
<hr>
<ul>
<li>上次面试时终于被这个黑盒给安排了。面试官让我手写map函数，我懵逼！尽管感觉好像能怼出来，却总差了点什么。被摁在地板摩擦之后，发现自己没做出来确实是有原因。</li>
<li>一方面，写这篇文章的时候发现，实现map所需要的知识点我都有涉猎，但却仅把它当作理论指导，没有把它与实践联系起来。今天就让我来学以致用一下。</li>
<li>另一方面，对于一些概念有些许误区，尽管这些误区看似可有可无微乎其微，但却真真切切的影响我很多。那就让这篇文章欢送这些不速之客。</li>
</ul>
<h3 class="heading">map黑盒背后的利益集团</h3>
<hr>
<p>以我个人入门JS的心路历程来看，倘若对以下知识有所涉猎了解，就算不是十分熟练也能轻松实现map函数。知识点如下: (<strong>仅以实现map而做简单讲解，详情内容请自阅其他文献</strong>)</p>
<h4 class="heading">1. 数据类型与存储</h4>
<p>JS中基本数据类型和引用数据类型是不同的。当我们把一个存储基本数据类型值的变量A赋值给另一个变量B时，本质是值传递，两个变量存储两个独立的值。但若是引用数据类型，本质是地址传递，那么此时两个变量存储的是同一个数据的地址，因此A、B会互相影响。</p>
<ul>
<li><strong>而函数是引用数据类型，其存储在堆内存中，将其赋值给一变量，则该变量存储的是函数在堆内存中的起始地址，以此来引用函数。</strong></li>
<li>在这里还想多扯一下，关于赋值，深、浅拷贝的问题，对比研究一下能很快掌握。另外说到存储不得不提提垃圾回收机制，都可以偷偷学一下，串一下。</li>
</ul>
<h4 class="heading">2. 函数是一等公民</h4>
<p>我们知道JS是一门多范式语言，其中就包括函数式编程。因此在JS中函数就像任何其他引用数据类型一样可以把它们存在数组里，<strong>当作函数参数传递</strong>，赋值给变量，<strong>作为对象的属性值</strong>等。</p>
<ul>
<li>作为对象的属性值
<figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/15/16a1fb88e2a159f1~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
我们定义了一个对象f，并将一个函数myFn赋值给了f中的属性fn，则此时我们的f.fn属性就已经指向了该函数，并可以通过f.fn()完成对函数的调用。</li>
<li>当作函数参数传递
<figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/15/16a1fbfcd8538eba~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
<strong>这里我们声明了一个fn函数，其接受一个函数作为参数并执行。我们又声明了一个callback函数。接着将callback作为参数传入fn中，并执行fn函数，其结果就是callback在fn函数中执行了。</strong> 如果你真的会意该部分，那么对你而言，map函数的金钟罩将会变成最后一块遮羞布了。</li>
</ul>
<h4 class="heading">3. 原型与原型链 / new构造函数调用的过程</h4>
<p>在JS中，当我们用 var arr = [1,2,3] 创建一个数组并将其赋值给变量arr时，该方式本质上与var arr = new Array(1,2,3) 是没有区别的。<strong>（这里突然意识到，还涉及到new构造函数调用的知识,优秀的你应该是知道该知识点的！！）</strong> 那么此时arr表示的数组就可以称为Array的一个实例，该实例的_proto_属性是指向构造函数Array的原型对象(也就是Array.prototype所表示的一个对象)</p>
<ul>
<li><strong>现在就让我们一步步揭开map的神秘面纱</strong></li>
</ul>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/15/16a1ff40eaed35ec~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
想想我第一次看到上图的时候很是懵逼，明明我只声明了一个数组，怎么它居然拥有map函数这样的属性？还有_proto_这个属性是什么？不行我晕了。(相信聪明的你一定没问题！！！)后来学习了原型链后才明白。<p></p>
<ul>
<li><strong>当访问属性的时候，会先在本实例对象(arr)中搜索属性，若未找到则会通过原型链继续搜索其指针指向的原型对象(Array.prototype)是否有该属性，OK找到了。没错我们平常用的map函数一般都是通过原型链查找到的Array.prototype.map所指向的函数。</strong></li>
<li>这里再多扯一些，我们创建一个数组并将其起始地址赋值给h，同理得g。但是h却不等于g。因为对于引用数据类型，g、h变量存储的是堆内存中该数据的起始地址，而内存中同时开辟了两个数据地址，因此不等。<strong>那么也就是说，这里arr._proto_指向的对象与Array.prototype指向的对象是堆内存中同一个引用数据类型。而arr.map通过原型链查找到的即是Array.prototype.map指向的函数因此也必然是相等的。</strong></li>
<li>再多扯一点，关于对象中属性的读取与修改，与作用域变量的读取与修改还是有很大不同的。感兴趣的话可以研究一下，对比记忆很快就掌握了。</li>
</ul>
<h4 class="heading">4. this的指向性问题</h4>
<p>关于JS函数里this的指向问题就不再概述了，大致分为四个规则加一个特殊的箭头函数。现在对于 <strong>[1，2，3].map(callback)</strong> 我们大概明白了，通过[1,2,3].map以原型链查询的方式找到了在Array.prototype.map里的函数，然后将callback函数作为参数传入map函数中以达到后期调用并执行相关逻辑的目的，但是我们怎么在调用的函数中找到原数组？没错通过函数中的this。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/15/16a201ce38ec63bd~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<ul>
<li>由this指向规则中的隐含转换知(this本质是函数执行时创建的执行上下文里的一个对象，因此this的指向由调用点决定)，当我们通过a.fn()调用a.fn指向的函数时，函数中的this就指向对象a。<strong>同理，当实现map函数时也可通过此原理来找到原数组,即实现的map函数里的this就指向实例数组本身。[1,2,3].map()则函数里的this指向该[1,2,3]数组。</strong></li>
</ul>
<h4 class="heading">5. 回调函数</h4>
<p>学习JS时才第一次接触回调函数，一度觉得自己挺懂回调，后来发现自己真的是根本不懂，还以为自己很懂！现在让我们看看map中回调的真容吧。</p>
<ul>
<li>
<p>一直以来我都把回调函数理解成<strong>主动性</strong>，但事实上传入的回调函数是<strong>被动性的</strong>。想一下平时我们为了实现某个功能定义了一个函数，然后传参执行该函数。<strong>但回调函数本质只是一个函数声明，之所以会执行相关的逻辑是因为之后会给该回调函数传入参数并调用该回调函数，它是被调用的。</strong></p>
</li>
<li>
<p>那么这里又涉及到<strong>已然性和未然性</strong>。原生的map函数是被定义过的，当调用map函数实现相关逻辑时，它内部执行流程就会将数组每个元素的(item/元素值, index/元素索引, arr/原数组)传入回调函数callback并以callback(item, index, arr)的形式调用。<strong>因此，我们知道该回调会被传入指定的参数并调用。所以，我们在仅需要做的声明传入的回调函数时，可以把此时回调函数的参数当做对应的数组中元素的值，在此基础上实现相关逻辑。实际上，就是把声明回调里的参数当做map执行时内部调用回调时传入的参数(item, index, arr)进行操作</strong></p>
</li>
<li>
<p>其实以上两点总结来说就是<strong>以往我们都是先声明函数，再传参调用</strong>。而现在我们在理解map函数时遇到的事实却是，已经确定了将回调函数传入map中调用时，将会在map函数内调用该回调函数，且该回调函数是被传入了固定参数的状态下调用的。<strong>因此可以说我们已经确定了内部会自动执行该回调，就差声明回调并传入map中执行了</strong>。所以现在对回调函数的理解是，<strong>会(hui)被调用的函数</strong>。</p>
</li>
</ul>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/4/15/16a2075974425d81~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<ul>
<li>如上图，我们定义了一个sumTwoItemFlag函数，它接受一个回调函数并将对象a,b传入该回调执行，所以当我们执行sumTwoItemFlag函数时要传入一个声明的回调函数，并在回调里完成相应的逻辑。<strong>这就是之前赘述的，已经确定好回调函数调用时传入的参数，我们已经知道此时回调里的参数就是sumTwoItemFlag中的a,b对象。在此基础上，我们只需要传入回调的时候把回调里的参数当做是a、b，并执行我们想要的逻辑就可以了。</strong></li>
<li><strong>其本质上就是反其道而行之。但却能达到我们思维里的先声明再调用的正常逻辑，且其更加灵活。因为虽然回调函数执行时传入的参数是固定的，但是对于map函数来说传入的回调函数却是灵活多变的，所以可以根据个人传入回调的不同，达到灵活实现数组操作的目的，真正是一本万利呀！回调牛逼！！！</strong></li>
<li>再啰嗦一局，该部分知识点配合上篇文章推荐知识清单中的用promise实现jsonp更丝滑哦。(<strong>该部分好像很啰嗦很重复，但还是选择了啰嗦重复，那你就把它当做强调吧</strong>)</li>
</ul>
<h3 class="heading">手写代码</h3>
<hr>
<p>相信看完内容的你已经对map这个有了很清晰的认识了吧。其实我觉得如果以上能掌握，那么以后绝大多数手写方法的题应该都不成问题了。那么接下来就让我贴出手写map的代码吧。(写文章真是个累人的活啊，贴出来把，写不动了！)</p>
<h4 class="heading">map实现</h4>
<pre><code>Array.prototype.myMap = function(callback, context) {
    var arr = this;
    var res = [];
    context = context ? context : window;
    for(let i = 0; i &lt; arr.length; i++) {
        let tem = callback.call(context, arr[i], i, arr);
        res.push(tem); 
    }
    return res;
}
</code></pre>
<h4 class="heading">reduce的实现</h4>
<p>相信只要你稍微动动灵活的小脑袋肯定也能实现一个reduce函数吧。</p>
<pre><code>Array.prototype.myReduce = function(callback) {
    var arr = this;
    var res; &lt;!--用arguments捕获第二个参数因为其值可能是null,NaN之类--&gt;
    if(typeof(callback) !== "function")  throw new Error("not a function");
    if(arguments.length &lt; 2 &amp;&amp; arr.length === 0) throw new Error("empty array with no initial value");
    if(arguments.length &lt; 2 &amp;&amp; arr.length === 1) return arr[0];
    if(arguments.length &gt; 1 &amp;&amp; arr.length === 0) return arguments[1];
    res = arguments.length &gt; 1? arguments[1] : arr.shift();
    for(let i = 0; i &lt; arr.length; i++) {
        res = callback(res, arr[i], i, arr);
    }
    return res;
}
</code></pre>
<h4 class="heading">map的reduce实现</h4>
<pre><code>Array.prototype._myMap = function(callback, context) {
    context = context ? context : window;
    return this.reduce((accum, item, index, arr) =&gt; 
        [...accum, callback.call(context, item, index, arr)]
    , []);
}
</code></pre>
<h3 class="heading">总结</h3>
<hr>
<ul>
<li><strong>千万别钻进牛角尖</strong>。相信你也看出来了，上述只是map函数等的简易版实现，关于该方法实现map函数，其边界情况真的是太多了。而我就有幸((┬＿┬))钻入了牛角尖，意图实现一个理想的map。其结果就是花费了太多时间却收效甚微。看了源码之后顿感自己真是傻！</li>
<li><strong>学习的时候方向不能搞错啊！</strong> 为什么说自己傻呢？我在实现的时候还是在用原生map手动测试边界情况，花费来大量时间之后，终于觉得搞不定了，要去看看源码。看了源码之后就开始怀疑人生了。其实仔细想想也能明白，没必要实现一个完美的map啊，你就算仿了一个完美的map又能说明什么？想搞明白就去看<strong>源码</strong>啊，还在那跟个××一样意图从表面探测真相，还是手动的。另一方面，面试官出这个题也是想考察你的基本功，也不可能真是让你完美实现啊。<strong>所以学习的时候千万不能搞错方向，更不要钻进不错误的牛角尖</strong>。</li>
<li><strong>想探究一个技术的真容，如果不懂，真的搞不定的话，就去学习源码。</strong> 这可以说是唯一欣慰的一点收获吧。以前学习webpack的时候也想弄明白这个黑盒的真容，当时也是手动由表入里的探索，结果最后实在是进行不下去了，结果就收工了，好在当时还是有所收获的。这篇文章后将更加坚定了我以研究源码作为日后学习各种黑盒的决心。</li>
</ul>
<h3 class="heading">展望</h3>
<hr>
<ul>
<li>感觉对箭头函数还是有一点不熟练，准备再研究一哈。</li>
<li>接下来想再探探webpack的真容，目前想的是从源码方面入手，如果太难的话就再补充补充涉及到的前置知识，再继续攻略源码。</li>
<li>昨天在看node开发实战里的爬虫实战时，惊觉以前似懂非懂的模块调用并掺杂着一些回调的逻辑业务，居然能看懂，不再半遮半掩了。感觉写文章真的是对以前纯输入的一种很好的输出方式。不仅能认识新朋友，更能对多所学知识进行一个梳理，总结。现在已经从纯输入过渡到想输出的阶段了，以后会继续坚持下去。但是也要深深的明白，根据能量守恒，<strong>这些输出是建立在以前输入的基础上，所以未来的日子也不能忘记充电呀</strong>！！！</li>
<li>本以为QQ截图会保留在本地，但在写这篇文章的时候居然惊奇地发现用QQ截图拖入该编辑页面居然会有该图片的地址，且在非本地情况下输入网址后真的有该图片，感觉自己真的对网络一无所知。粗略的想了一下(<strong>瞎猜的</strong>)，大概是截图成功就会将该图片放入存储我QQ对应数据的数据库中吧，然后可以通过该url访问此图片。之后会想要了解清楚。<strong>原来习以为常的QQ截图背后竟有如此不为人知的操作，真是该对日常理所应当的事更上上心了呀</strong>。</li>
</ul>
<hr>
