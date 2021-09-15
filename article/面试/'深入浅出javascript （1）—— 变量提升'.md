标题:深入浅出javascript （1）—— 变量提升
描述:提到前端面试，对于 javascript 语言层面的考察，这几个概念是避不开的：执行上下文，变量提升，闭包，This，作用域，作用域链，原型链，Event Loop等。 与其说面试很机械，倒不如说这就是 javascript 语音最最核心的概念，弄不清楚这些概念，那你一定不是一…

<p>提到前端面试，对于 javascript 语言层面的考察，这几个概念是避不开的：执行上下文，变量提升，闭包，This，作用域，作用域链，原型链，Event Loop等。
与其说面试很机械，倒不如说这就是 javascript 语音最最核心的概念，弄不清楚这些概念，那你一定不是一名合格的前端开发er。
所以，接下来我会分几篇文章来讲这几个核心概念，并将他们串起来，让大家可以更好的全方位理解。
下面进入正题，今天第一批文章我们来说 —— 变量提升。</p>
<p>先看代码：</p>
<pre><code class="hljs bash" lang="bash">showName() 
console.log(myname) 
var myname = <span class="hljs-string">'wens'</span> 
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">showName</span></span>() { 
    console.log(<span class="hljs-string">'函数showName被执行'</span>); 
}
</code></pre><p>使用过 JavaScript 开发的程序员应该都知道，JavaScript 是按顺序执行的。若按照这个逻辑来理解的话，那么：</p>
<ul>
<li>当执行到第 1 行的时候，由于函数 showName 还没有定义，所以执行应该会报错；</li>
<li>执行第 2 行的时候，由于变量 myname 也未定义，所以同样也会报错。然而实际执行结果却并非如此， 如下图：</li>
</ul>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/6/8/17293d8ab0ae4374~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>第 1 行输出“函数 showName 被执行”，第 2 行输出“undefined”，这和想象中的顺序执行有点不一样啊！</p>
<p>通过上面的执行结果，我们已经知道了函数或者变量可以在定义之前使用，那如果使用没有定义的变量或者函数，JavaScript 代码还能继续执行吗？为了验证这点，我们可以删除第 3 行变量 myname 的定义，如下所示：</p>
<pre><code class="hljs bash" lang="bash">showName() 
console.log(myname) 
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">showName</span></span>() { 
    console.log(<span class="hljs-string">'函数showName被执行'</span>); 
}
</code></pre><p>这时候 JavaScript 引擎就会报错，结果如下：</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/6/8/17293db33945ef8a~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>从上面两段代码的执行结果来看，我们可以得出如下三个结论。</p>
<ol>
<li>在执行过程中，若使用了未声明的变量，那么 JavaScript 执行会报错。</li>
<li>在一个变量定义之前使用它，不会出错，但是该变量的值会为 undefined，而不是定义时的值。</li>
<li>在一个函数定义之前使用它，不会出错，且函数能正确执行。</li>
</ol>
<p>第一个结论很好理解，因为变量没有定义，这样在执行 JavaScript 代码时，就找不到该变量，所以 JavaScript 会抛出错误。</p>
<p>但是对于后两个结论，就挺让人费解的：</p>
<ul>
<li>变量和函数为什么能在其定义之前使用？这似乎表明 JavaScript 代码并不是一行一行执行的。</li>
<li>同样的方式，变量和函数的处理结果为什么不一样？比如上面的执行结果，提前使用的 showName 函数能打印出来完整结果，但是提前使用的 myname 变量值却是 undefined，而不是定义时使用的“wens”这个值。</li>
</ul>
<h2 class="heading">变量提升（Hoisting）</h2>
<p>要解释这两个问题，我们需要先了解下什么是变量提升。</p>
<p>不过在介绍变量提升之前，我们先通过下面这段代码，来看看什么是 JavaScript 中的声明和赋值。</p>
<pre><code class="hljs bash" lang="bash">var myname = <span class="hljs-string">'wens'</span>
</code></pre><p>这行代码需要这样理解：</p>
<pre><code class="hljs bash" lang="bash">var myname //声明部分 
myname = <span class="hljs-string">'wens'</span> //赋值部分
</code></pre><p>上面是变量的声明和赋值，那接下来我们再来结合代码看看函数的声明和赋值：</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">foo</span></span>(){ 
    console.log(<span class="hljs-string">'foo'</span>) 
} 
var bar = <span class="hljs-function"><span class="hljs-title">function</span></span>(){ 
    console.log(<span class="hljs-string">'bar'</span>) 
}
</code></pre><p>第一个函数 foo 是一个完整的函数声明，也就是说没有涉及到赋值操作；
第二个函数和上面那一行变量的赋值一样，是先声明变量 bar，再把function(){console.log('bar')}赋值给 bar。</p>
<p>好了，理解了声明和赋值操作，那接下来我们就可以聊聊什么是变量提升了。</p>
<p>所谓的变量提升，是指在 JavaScript 代码执行过程中，JavaScript 引擎把变量的声明部分和函数的声明部分提升到代码开头的行为。变量被提升后，会给变量设置默认值，这个默认值就是我们熟悉的 undefined。</p>
<p>针对第一个代码片段，我们来模拟一下变量提升：</p>
<pre><code class="hljs bash" lang="bash">// 把变量 myname提升到开头， 
// 同时给myname赋值为undefined 
var myname = undefined 

// 把函数showName提升到开头 
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">showName</span></span>() { 
    console.log(<span class="hljs-string">'showName被调用'</span>); 
} 

showName() // 所以这里可以正常执行
console.log(myname) // 所以这里可以正常打印myname的值

// 去掉var声明部分，保留赋值语句 
myname = <span class="hljs-string">'wens'</span>
</code></pre><p>从代码中可以看出，对原来的代码主要做了两处调整：</p>
<ul>
<li>第一处是把声明的部分都提升到了代码开头，如变量 myname 和函数 showName，并给变量设置默认值 undefined；</li>
<li>第二处是移除原本声明的变量和函数，如var myname = 'wens'的语句，移除了 var 声明，整个移除 showName 的函数声明。</li>
</ul>
<p>通过这两步，就可以实现变量提升的效果。你也可以执行这段模拟变量提升的代码，其输出结果和第一段代码是完全一样的。</p>
<h2 class="heading">JavaScript 代码的执行流程</h2>
<p>从字面意义上来看，“变量提升”意味着变量和函数的声明会移动到代码的最前面，就像我们所模拟的那样。其实这并不准确。实际上变量和函数声明在代码里的位置是不会改变的。因为一段 JavaScript 的可执行代码(executable code) 在真正被执行之前还要先经历引擎的编译</p>
<h3 class="heading">编译阶段</h3>
<p>上面说到 JavaScript 的可执行代码(executable code)，那么哪些是可执行代码呢？</p>
<p>其实很简单，就三种，全局代码、函数代码、eval代码。</p>
<p>那么编译阶段和变量提升存在什么关系呢？</p>
<p>为了搞清楚这个问题，我们还是回过头来看上面那段模拟变量提升的代码，为了方便介绍，可以把这段代码分成两部分。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/6/9/172975ad96d1d0b8~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>从上图可以看出，输入一段代码，经过编译后，会生成两部分内容：执行上下文（Execution context）和可执行代码。</p>
<p>执行上下文是 JavaScript 执行一段代码时的运行环境，比如调用一个函数，就会进入这个函数的执行上下文，在这里确定该函数在执行期间用到的诸如 this、变量、对象以及函数等。</p>
<p>关于执行上下文的细节，我会在下一篇文章做详细介绍，现在我们只需要知道，在执行上下文中存在一个变量环境的对象（Viriable Environment），该对象中保存了变量提升的内容，比如上面代码中的变量 myname 和函数 showName，都保存在该对象中。</p>
<p>我们可以简单地把变量环境对象看成是如下结构：</p>
<pre><code class="hljs bash" lang="bash">VariableEnvironment: 
    myname -&gt; undefined, 
    showName -&gt; <span class="hljs-keyword">function</span> {console.log(myname)}
</code></pre><p>接下来，我们再结合代码来分析下是如何生成变量环境对象的:</p>
<pre><code class="hljs bash" lang="bash">showName() 
console.log(myname) 
var myname = <span class="hljs-string">'wens'</span> 
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">showName</span></span>() { 
    console.log(<span class="hljs-string">'函数showName被执行'</span>); 
}
</code></pre><p>我们逐行分析上述代码：</p>
<ul>
<li>第 1 行和第 2 行，由于这两行代码不是声明操作，所以 JavaScript 引擎不会做任何处理；</li>
<li>第 3 行，由于这行是经过 var 声明的，因此 JavaScript 引擎将在环境对象中创建一个名为 myname 的属性，并使用 undefined 对其初始化；</li>
<li>第 4 行，JavaScript 引擎发现了一个通过 function 定义的函数，所以它将函数定义存储到堆 (HEAP）中，并在环境对象中创建一个 showName 的属性，然后将该属性值指向堆中函数的位置。</li>
</ul>
<p>这样就生成了变量环境对象。接下来 JavaScript 引擎会把声明以外的代码编译为字节码，至于字节码的细节，我也会在后面文章中做详细介绍。现在有了执行上下文和可执行代码了，那么接下来就到了执行阶段了。</p>
<h3 class="heading">执行阶段</h3>
<p>JavaScript 引擎开始执行“可执行代码”，按照顺序逐行执行。下面我们就分析下这个执行过程：</p>
<ul>
<li>当执行到 showName 函数时，JavaScript 引擎便开始在变量环境对象中查找该函数，由于变量环境对象中存在该函数的引用，所以 JavaScript 引擎便开始执行该函数，并输出“函数 showName 被执行”结果。</li>
<li>接下来打印“myname”信息，JavaScript 引擎继续在变量环境对象中查找该对象，由于变量环境存在 myname 变量，并且其值为 undefined，所以这时候就输出 undefined。</li>
<li>接下来执行第 3 行，把“wens”赋给 myname 变量，赋值后变量环境中的 myname 属性值变为“wens”，变量环境如下所示：</li>
</ul>
<pre><code class="hljs bash" lang="bash">VariableEnvironment: 
    myname -&gt; wens, 
    showName -&gt; <span class="hljs-keyword">function</span> {console.log(myname)}
</code></pre><p>好了，以上就是一段代码的编译和执行流程。实际上，编译阶段和执行阶段都是非常复杂的，包括了词法分析、语法解析、代码优化、代码生成等，所有的这些内容我都会在接下来的文章中介绍，在本篇文章中我们暂时只介绍变量提升相关内容。</p>
<h2 class="heading">代码中出现相同的变量或者函数怎么办？</h2>
<p>现在我们知道了，在执行一段 JavaScript 代码之前，会编译代码，并将代码中的函数和变量保存到执行上下文的变量环境中，那么如果代码中出现了重名的函数或者变量，JavaScript 引擎会如何处理？</p>
<h3 class="heading">相同变量</h3>
<p>我们看下面的代码：</p>
<pre><code class="hljs bash" lang="bash">console.log(myName);
var myName = <span class="hljs-string">'wens'</span>;
console.log(myName);
var myName = <span class="hljs-string">'leon'</span>;
console.log(myName);
</code></pre><p>我们来分析下其完整执行流程：</p>
<ul>
<li>首先是编译阶段。遇到了第一个 myName 变量，在环境对象中创建 myName 并赋予undefined 初始值。接下来是第二个 myName 变量，此时变量环境对象中已经存在 myName ，所以跳过这个过程。</li>
<li>接下来是执行阶段。第一个log输出 undefined ，因为这时候没有给 myName 再次赋值。第二行myName变量被赋值 wens， 所以第二个log输出 wens。同理，第三个log输出leon。</li>
</ul>
<p>综上所述，一段代码如果定义了两个相同名字的值，那么最终的值取决于被赋予的最新的值，如果没有就是初始值undefined。</p>
<h3 class="heading">相同函数</h3>
<p>我们先看下面这样一段代码：</p>
<pre><code class="hljs bash" lang="bash"><span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">showName</span></span>() { 
    console.log(<span class="hljs-string">'wens'</span>); 
} 
showName(); 
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">showName</span></span>() { 
    console.log(<span class="hljs-string">'leon'</span>); 
} 
showName();
</code></pre><p>在上面代码中，我们先定义了一个 showName 的函数，该函数打印出来“wens”；然后调用 showName，又定义了一个 showName 函数，这个 showName 函数打印出来的是“leon”；一段代码中出现了同名的函数，并分别调用。
我们来分析下其完整执行流程：</p>
<ul>
<li>首先是编译阶段。遇到了第一个 showName 函数，将函数定义存储到堆中，并在环境对象中创建一个 showName 的属性指向堆中定义的函数。接下来是第二个 showName 函数，发现变量环境中已经存在一个 showName 函数了，此时，堆中定义的 showName 函数会被这个 showName 函数覆盖掉。这样变量环境中的 showName 函数就指向了第二个 showName 函数了。</li>
<li>接下来是执行阶段。先执行第一个 showName 函数，但由于是从变量环境中查找 showName 函数，而变量环境中只保存了第二个 showName 函数，所以最终调用的是第二个函数，打印的内容是“leon”。第二次执行 showName 函数也是走同样的流程，所以输出的结果也是“leon”。</li>
</ul>
<p>综上所述，一段代码如果定义了两个相同名字的函数，那么最终生效的是最后一个函数。</p>
<h2 class="heading">总结</h2>
<p>好了，今天就到这里，下面我来简单总结下今天的主要内容：</p>
<ul>
<li>JavaScript 代码执行过程中，需要先做变量提升，而之所以需要实现变量提升，是因为 JavaScript 代码在执行之前需要先编译。</li>
<li>在编译阶段，变量和函数会被存放到变量环境中，变量的默认值会被设置为 undefined；在代码执行阶段，JavaScript 引擎会从变量环境中去查找自定义的变量和函数。</li>
<li>如果在编译阶段，存在两个相同的变量，那么值取决于被赋予的最新的值，如果没有就是初始值undefined。</li>
<li>如果在编译阶段，存在两个相同的函数，那么最终存放在变量环境中的是最后定义的那个，这是因为后定义的会覆盖掉之前定义的。</li>
</ul>
<p>以上就是今天所讲的主要内容，接下来的文章我们会重点介绍执行上下文。</p>
