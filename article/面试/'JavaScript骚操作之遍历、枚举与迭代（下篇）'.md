标题:JavaScript骚操作之遍历、枚举与迭代（下篇）
描述:JavaScript 遍历、枚举与迭代的骚操作（上篇）总结了一些常用对象的遍历方法，大部分情况下是可以满足工作需求的。但下篇介绍的内容，在工作中95%的情况下是用不到的，仅限装逼。俗话说：装得逼多必翻车！若本文有翻车现场，请轻喷。 上一篇提到，for of循环是依靠对象的迭…

<h2 class="heading">前言</h2>
<p><a href="https://juejin.cn/post/6844903724897271816">JavaScript 遍历、枚举与迭代的骚操作（上篇）</a>总结了一些常用对象的遍历方法，大部分情况下是可以满足工作需求的。但下篇介绍的内容，在工作中95%的情况下是用不到的，仅限装逼。俗话说：装得逼多必翻车！若本文有翻车现场，请轻喷。</p>
<h2 class="heading">ES6 迭代器（iterator）、生成器（generator）</h2>
<p>上一篇提到，for of循环是依靠对象的迭代器工作的，如果用for of循环遍历一个非可迭代对象（即无默认迭代器的对象），for of循环就会报错。那迭代器到底是何方神圣？<br></p>
<p>迭代器是一种特殊的对象，其有一个next方法，每一次枚举（for of每循环一次）都会调用此方法一次，且返回一个对象，此对象包含两个值：</p>
<ul>
<li>value属性，表示此次调用的返回值（for of循环只返回此值）;</li>
<li>done属性，Boolean值类型，标志此次调用是否已结束。</li>
</ul>
<p>生成器，顾名思义，就是迭代器他妈；生成器是返回迭代器的特殊函数，迭代器由生成器生成。<br></p>
<p>生成器声明方式跟普通函数相似，仅在函数名前面加一个*号（*号左右有空格也是可以正确运行的，但为了代码可读性，建议左边留空格，右边不留）；函数内部使用yield关键字指定每次迭代返回值。</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-comment">// 生成器</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">iteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'we'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'are'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'the BlackGold team!'</span>;
    }

    <span class="hljs-comment">// 迭代器</span>
    <span class="hljs-keyword">let</span> iterator = iteratorMother();

    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: "we", done: false }</span>
    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: "are", done: false }</span>
    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: "the BlackGold team!", done: false }</span>

    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: undefined, done: true }</span>
    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: undefined, done: true }</span>
</code></pre><p>上面的例子展示声明了一个生成器函数iteratorMother的方式，调用此函数返回一个迭代器iterator。<br></p>
<p>yield是ES6中的关键字，它指定了iterator对象每一次调用next方法时返回的值。如第一个yield关键字后面的字符串"we"即为iterator对象第一次调用next方法返回的值，以此类推，直到所有的yield语句执行完毕。<br></p>
<p>注意：<strong>当yield语句执行完毕后，调用iterator.next()会一直返回{ value: undefined, done: true }，so，别用for of循环遍历同一个迭代器两次</strong></p>
<pre><code class="hljs js" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">iteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'we'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'are'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'the BlackGold team!'</span>;
    }

    <span class="hljs-keyword">let</span> iterator = iteratorMother();

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> element <span class="hljs-keyword">of</span> iterator) {
        <span class="hljs-built_in">console</span>.log(element);
    }

    <span class="hljs-comment">// we</span>
    <span class="hljs-comment">// are</span>
    <span class="hljs-comment">// the BlackGold team!</span>

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> element <span class="hljs-keyword">of</span> iterator) {
        <span class="hljs-built_in">console</span>.log(element);
    }

    <span class="hljs-comment">// nothing to be printed</span>
    <span class="hljs-comment">// 这个时候迭代器iterator已经完成他的使命，如果想要再次迭代，应该生成另一个迭代器对象以进行遍历操作</span>
</code></pre><p>注意：<strong>可以指定生成器的返回值，当运行到return语句时，无论后面的代码是否有yield关键字都不会再执行；且返回值只返回一次，再次调用next方法也只是返回{ value: undefined, done: true }</strong></p>
<pre><code class="hljs js" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">iteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'we'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'are'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'the BlackGold team!'</span>;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'done'</span>;

        <span class="hljs-comment">// 不存在的，这是不可能的</span>
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'0 error(s), 0 warning(s)'</span>
    }

    <span class="hljs-comment">// 迭代器</span>
    <span class="hljs-keyword">let</span> iterator = iteratorMother();

    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: "we", done: false }</span>
    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: "are", done: false }</span>
    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: "the BlackGold team!", done: false }</span>

    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: "done", done: true }</span>
    <span class="hljs-built_in">console</span>.log(iterator.next());  <span class="hljs-comment">// { value: undefined, done: true }</span>
</code></pre><p>注意third time：<strong>yield关键字仅可在生成器函数内部使用，一旦在生成器外使用（包括在生成器内部的函数例使用）就会报错，so，使用时注意别跨越函数边界</strong></p>
<pre><code class="hljs js" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">iteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'we'</span>, <span class="hljs-string">'are'</span>, <span class="hljs-string">'the BlackGold team!'</span>];

        <span class="hljs-comment">// 报错了</span>
        <span class="hljs-comment">// 以下代码实际上是在forEach方法的参数函数里面使用yield</span>
        arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =&gt;</span> <span class="hljs-keyword">yield</span> item);
    }
</code></pre><p>上面的例子，在JavaScript引擎进行函数声明提升的时候就报错了，而非在实例化一个迭代器实例的时候才报错。</p>
<p>注意fourth time：<strong>别尝试在生成器内部获取yield指定的返回值，否则会得到一个undefined</strong></p>
<pre><code class="hljs js" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">iteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">let</span> a = <span class="hljs-keyword">yield</span> <span class="hljs-string">'we'</span>;
        <span class="hljs-keyword">let</span> b = <span class="hljs-keyword">yield</span> a + <span class="hljs-string">' '</span> +  <span class="hljs-string">'are'</span>;
        <span class="hljs-keyword">yield</span> b + <span class="hljs-string">' '</span> + <span class="hljs-string">'the BlackGold team!'</span>;
    }

    <span class="hljs-keyword">let</span> iterator = iteratorMother();

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> element <span class="hljs-keyword">of</span> iterator) {
        <span class="hljs-built_in">console</span>.log(element);
    }

    <span class="hljs-comment">// we</span>
    <span class="hljs-comment">// undefined are</span>
    <span class="hljs-comment">// undefined the BlackGold team!</span>
</code></pre><blockquote>
<p>note：可以使用匿名函数表达式声明一个生成器，只要在function关键字后面加个可爱的*号就好，例子就不写了；<strong>但是不可以使用箭头函数声明生成器</strong>。</p>
</blockquote>
<h2 class="heading">为对象添加生成器</h2>
<p>使用for of循环去遍历一个对象的时候，会先去寻找此对象有没有生成器，若有则使用其默认的生成器生成一个迭代器，然后遍历此迭代器；若无，报错！</p>
<p>上篇也提到，像Set、Map、Array等特殊的对象类型，都有多个生成器，但是自定义的对象是没有内置生成器的，不知道为啥；就跟别人有女朋友而我没有女朋友一样，不知道为啥。没关系，自己动手，丰衣足食；我们为自定义对象添加一个生成器（至于怎么解决女朋友的问题，别问我）</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-keyword">let</span> obj = {
        <span class="hljs-attr">arr</span>: [<span class="hljs-string">'we'</span>, <span class="hljs-string">'are'</span>, <span class="hljs-string">'the BlackGold team!'</span>],
        *[<span class="hljs-built_in">Symbol</span>.iterator]() {
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> element <span class="hljs-keyword">of</span> <span class="hljs-keyword">this</span>.arr) {
                <span class="hljs-keyword">yield</span> element;
            }
        }
    }

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> obj) {
        <span class="hljs-built_in">console</span>.log(key);
    }

    <span class="hljs-comment">// we</span>
    <span class="hljs-comment">// are</span>
    <span class="hljs-comment">// the BlackGold team!</span>
</code></pre><p>好吧，我承认上面的例子有点脱了裤子放P的味道，当然不是说这个例子臭，而是有点多余；毕竟我们希望遍历的是对象的属性，那就换个方式搞一下吧</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-keyword">let</span> father = {
        *[<span class="hljs-built_in">Symbol</span>.iterator]() {
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> <span class="hljs-built_in">Reflect</span>.ownKeys(<span class="hljs-keyword">this</span>)) {
                <span class="hljs-keyword">yield</span> key;
            }
        }
    };

    <span class="hljs-keyword">let</span> obj = <span class="hljs-built_in">Object</span>.create(father);

    obj.a = <span class="hljs-number">1</span>;
    obj[<span class="hljs-number">0</span>] = <span class="hljs-number">1</span>;
    obj[<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'PaperCrane'</span>)] = <span class="hljs-number">1</span>;
    <span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-string">'b'</span>, {
        <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>
    });

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> obj) {
        <span class="hljs-built_in">console</span>.log(key);
    }

    <span class="hljs-comment">/* 看起来什么鬼属性都能被Reflect.ownKeys方法获取到 */</span>
    <span class="hljs-comment">// 0</span>
    <span class="hljs-comment">// a</span>
    <span class="hljs-comment">// b</span>
    <span class="hljs-comment">// Symbol(PaperCrane)</span>
</code></pre><p>通过上面例子的展示的方式包装对象，确实可以使用for of来遍历对象的属性，但是使用起来还是有点点的麻烦，目前没有较好的解决办法。我们在创建自定义的类（构造器）的时候，可以加上Symbol.iterator生成器，那么类的实例就可以使用for of循环遍历了。</p>
<blockquote>
<p>note：Reflect对象是反射对象，其提供的方法默认特性与底层提供的方法表现一致，如Reflect.ownKeys的表现就相当于Object.keys、Object.getOwnPropertyNames、Object.getOwnPropertySymbols三个操作加起来的操作。上篇有一位ID为“webgzh907247189”的朋友提到还有这种获取对象属性名的方法，这一篇就演示一下，同时也非常感谢这位朋友的宝贵意见。</p>
</blockquote>
<h2 class="heading">迭代器传值</h2>
<p>上面提到过，如果在迭代器内部获取yield指定的返回值，将会得到一个undefined，但代码逻辑如果依赖前面的返回值的话，就需要通过给迭代器的next方法传参达到此目的</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">iteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">let</span> a = <span class="hljs-keyword">yield</span> <span class="hljs-string">'we'</span>;
        <span class="hljs-keyword">let</span> b = <span class="hljs-keyword">yield</span> a + <span class="hljs-string">' '</span> +  <span class="hljs-string">'are'</span>;
        <span class="hljs-keyword">yield</span> b + <span class="hljs-string">' '</span> + <span class="hljs-string">'the BlackGold team!'</span>;
    }

    <span class="hljs-keyword">let</span> iterator = iteratorMother(),
        first, second, third;

    <span class="hljs-comment">// 第一次调用next方法时，传入的参数将不起任何作用</span>
    first = iterator.next(<span class="hljs-string">'anything，even an Error instance'</span>);
    <span class="hljs-built_in">console</span>.log(first.value);                <span class="hljs-comment">// we</span>
    second = iterator.next(first.value);
    <span class="hljs-built_in">console</span>.log(second.value);               <span class="hljs-comment">// we are</span>
    third = iterator.next(second.value);
    <span class="hljs-built_in">console</span>.log(third.value);                <span class="hljs-comment">// we are the BlackGold team!</span>
</code></pre><p>往next方法传的参数，将会成为上一次调用next对应的yield关键字的返回值，在生成器内部可以获得此值。所以调用next方法时，会执行对应yield关键字右侧至上一个yield关键字左侧的代码块；生成器内部变量a的声明和赋值是在第二次调用next方法的时候进行的。</p>
<blockquote>
<p>note：往第一次调用的next方法传参时，将不会对迭代有任何的影响。此外，也可以往next方法传递一个Error实例，当迭代器报错时，后面的代码将不会执行。</p>
</blockquote>
<h2 class="heading">解决回调地狱</h2>
<p>每当面试时问到如何解决回调地狱问题时，我们的第一反应应该是使用Promise对象；如果你是大牛，可以随手甩面试官Promise的实现原理；但是万一不了解Promise原理，又想装个逼，可以试试使用迭代器解决回调地狱问题</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-comment">// 执行迭代器的函数，参数iteratorMother是一个生成器</span>
    <span class="hljs-keyword">let</span> iteratorRunner = <span class="hljs-function"><span class="hljs-params">iteratorMother</span> =&gt;</span> {
        <span class="hljs-keyword">let</span> iterator = iteratorMother(),
            result = iterator.next(); <span class="hljs-comment">// 开始执行迭代器</span>
        
        <span class="hljs-keyword">let</span> run = <span class="hljs-function"><span class="hljs-params">()</span> =&gt;</span> {
            <span class="hljs-keyword">if</span> (!result.done) {
                <span class="hljs-comment">// 假如上一次迭代的返回值是一个函数</span>
                <span class="hljs-comment">// 执行result.value，传入一个回调函数，当result.value执行完毕时执行下一次迭代</span>
                <span class="hljs-keyword">if</span> ((<span class="hljs-keyword">typeof</span> result.value).toUpperCase() === <span class="hljs-string">'FUNCTION'</span>) {
                    result.value(<span class="hljs-function"><span class="hljs-params">params</span> =&gt;</span> {
                        result = iterator.next(params);

                        <span class="hljs-comment">// 继续迭代</span>
                        run();
                    });
                } <span class="hljs-keyword">else</span> {
                    <span class="hljs-comment">// 上一次迭代的返回值不是一个函数，直接进入下一次迭代</span>
                    result = iterator.next(result.value);
                    run();
                }
            }
        }

        <span class="hljs-comment">// 循环执行迭代器，直到迭代器迭代完毕</span>
        run();
    }

        <span class="hljs-comment">// 异步函数包装器，为了解决向异步函数传递参数问题</span>
    <span class="hljs-keyword">let</span> asyncFuncWrapper = <span class="hljs-function">(<span class="hljs-params">asyncFunc, param</span>) =&gt;</span> resolve =&gt; asyncFunc(param, resolve),
        <span class="hljs-comment">// 模拟的异步函数</span>
        asyncFunc = <span class="hljs-function">(<span class="hljs-params">param, callback</span>) =&gt;</span> setTimeout(<span class="hljs-function"><span class="hljs-params">()</span> =&gt;</span> callback(param), <span class="hljs-number">1000</span>);

    iteratorRunner(<span class="hljs-function"><span class="hljs-keyword">function</span> *(<span class="hljs-params"></span>) </span>{
        <span class="hljs-comment">// 按照同步的方式快乐的写代码</span>
        <span class="hljs-keyword">let</span> a = <span class="hljs-keyword">yield</span> asyncFuncWrapper(asyncFunc, <span class="hljs-number">1</span>);
        a += <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> b = <span class="hljs-keyword">yield</span> asyncFuncWrapper(asyncFunc, a);
        b += <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> c = <span class="hljs-keyword">yield</span> asyncFuncWrapper(asyncFunc, b);

        <span class="hljs-keyword">let</span> d = <span class="hljs-keyword">yield</span> c + <span class="hljs-number">1</span>;
        <span class="hljs-built_in">console</span>.log(d);          <span class="hljs-comment">// 4</span>
    });
</code></pre><p>上面的例子中，使用setTimeout来模拟一个异步函数asyncFunc，此异步函数接受两个参数：param和回调函数callback；在生成器内部，每一个yield关键字返回的值都为一个包装了异步函数的函数，用于往异步函数传入参数；执行迭代器的函数iteratorRunner，用于循环执行迭代器，并运行迭代器返回的函数。最后，我们可以在匿名生成器里面以同步的方式处理我们的代码逻辑。</p>
<p>以上的方式虽然解决了回调地狱的问题，但本质上依然是使用回调的方式调用代码，只是换了代码的组织方式。生成器内部的代码组织方式，有点类似ES7的async、await语法；所不同的是，async函数可以返回一个promise对象，搬砖工作者可以继续使用此promise对象以同步方式调用异步函数。</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-keyword">let</span> asyncFuncWrapper = <span class="hljs-function">(<span class="hljs-params">asyncFunction, param</span>) =&gt;</span> {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =&gt;</span> {
                asyncFunction(param, data =&gt; {
                    resolve(data);
                });
            });
        },
        asyncFunc = <span class="hljs-function">(<span class="hljs-params">param, callback</span>) =&gt;</span> setTimeout(<span class="hljs-function"><span class="hljs-params">()</span> =&gt;</span> callback(param), <span class="hljs-number">1000</span>);

    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncFuncRunner</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">let</span> a = <span class="hljs-keyword">await</span> asyncFuncWrapper(asyncFunc, <span class="hljs-number">1</span>);
        a += <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> b = <span class="hljs-keyword">await</span> asyncFuncWrapper(asyncFunc, a);
        b += <span class="hljs-number">1</span>;
        <span class="hljs-keyword">let</span> c = <span class="hljs-keyword">await</span> asyncFuncWrapper(asyncFunc, b);

        <span class="hljs-keyword">let</span> d = <span class="hljs-keyword">await</span> c + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">return</span> d;
    }

    asyncFuncRunner().then(<span class="hljs-function"><span class="hljs-params">data</span> =&gt;</span> <span class="hljs-built_in">console</span>.log(data));    <span class="hljs-comment">// 三秒后输出 4</span>
</code></pre><h2 class="heading">委托生成器</h2>
<p>在这个讲求DRY（Don't Repeat Yourself）的时代，生成器也可以进行复用。</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">iteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'we'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'are'</span>;
    }

    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">anotherIteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'the BlackGold team!'</span>;
        <span class="hljs-keyword">yield</span> <span class="hljs-string">'get off work now!!!!!!'</span>;
    }

    <span class="hljs-function"><span class="hljs-keyword">function</span> *<span class="hljs-title">theLastIteratorMother</span>(<span class="hljs-params"></span>) </span>{
        <span class="hljs-keyword">yield</span> *iteratorMother();
        <span class="hljs-keyword">yield</span> *anotherIteratorMother();
    }

    <span class="hljs-keyword">let</span> iterator = theLastIteratorMother();

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> iterator) {
        <span class="hljs-built_in">console</span>.log(key);
    }

    <span class="hljs-comment">// we</span>
    <span class="hljs-comment">// are</span>
    <span class="hljs-comment">// the BlackGold team!</span>
    <span class="hljs-comment">// get off work now!!!!!!</span>
</code></pre><p>上面的例子中，生成器theLastIteratorMother定义里面，复用了生成器iteratorMother、anotherIteratorMother两个生成器，相当于在生成器theLastIteratorMother内部声明了两个相关的迭代器，然后进行迭代。需要注意的是，复用生成器是，yield关键字后面有星号。</p>
<h2 class="heading">几个循环语句性能</h2>
<p>上一篇有小伙伴提到对比一下遍历方法的性能，我这边简单对比一下各个循环遍历数组的性能，测试数组长度为1000万，测试代码如下：</p>
<pre><code class="hljs js" lang="js">    <span class="hljs-keyword">let</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">10</span> * <span class="hljs-number">1000</span> * <span class="hljs-number">1000</span>).fill({ <span class="hljs-attr">test</span>: <span class="hljs-number">1</span> });

    <span class="hljs-built_in">console</span>.time();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, len = arr.length; i &lt; len; i++) {}
    <span class="hljs-built_in">console</span>.timeEnd();

    <span class="hljs-built_in">console</span>.time();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> arr) {}
    <span class="hljs-built_in">console</span>.timeEnd();

    <span class="hljs-built_in">console</span>.time();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> arr) {}
    <span class="hljs-built_in">console</span>.timeEnd();

    <span class="hljs-built_in">console</span>.time();
    arr.forEach(<span class="hljs-function"><span class="hljs-params">()</span> =&gt;</span> {});
    <span class="hljs-built_in">console</span>.timeEnd();
</code></pre><p>结果如下图（单位为ms，不考虑IE）：</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/12/5/1677e256cdcdb8e1~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>以上的结果可能在不同的环境下略有差异，但是基本可以说明，原生的循环速度最快，forEach次之，for of循环再次之，forin循环又次之。其实，如果数据量不大，遍历的方法基本不会成为性能的瓶颈，考虑如何减少循环遍历或许更实际一点。</p>
<h2 class="heading">总结</h2>
<p>含泪写完这一篇，我要下班了，再见各位。</p>
<blockquote>
<p>@Author: PaperCrane</p>
</blockquote>
