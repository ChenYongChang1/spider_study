url:https://juejin.cn/post/6844903967059607565
标题:动画：用动画技巧记忆常见笔试 JS 类型转换
描述:这部分的面试知识点是和前几天发的那篇基础知识点是一起的，小鹿按照分类把它分成两篇进行分享。 暑假去面试，进门先做笔试题，笔试题的基础部分大多都是这样 JS 基础问题，做的时候总是含含糊糊，感觉对也感觉不对。其实回来总接到，还是这些基础点没有掌握牢靠，看了过一段时间就忘，有没有一…

<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce96a78054a61~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h3 class="heading">写在前边</h3>
<p>这部分的面试知识点是和前几天发的那篇基础知识点是一起的，小鹿按照分类把它分成两篇进行分享。</p>
<p><a target="_blank" href="https://juejin.cn/post/6844903960080285709">动画：面试官问我 0.1 + 0.2 __ 0.3 ? 为什么？该如何正确回答？</a></p>
<p>暑假去面试，进门先做笔试题，笔试题的基础部分大多都是这样 JS 基础问题，做的时候总是含含糊糊，感觉对也感觉不对。其实回来总接到，还是这些基础点没有掌握牢靠，看了过一段时间就忘，有没有一种方法把这些零散知识理解记住呢？</p>
<p>试一下动画方式，看看有没有好的效果，进入今天的正题。</p>
<h3 class="heading">思维导图</h3>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce987d1e45ee1~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h3 class="heading">一、转 Boolean 类型</h3>
<p>任何的值如果转化为布尔类型时，我们只记住其中几个转化为<code>false</code>即可，因为如果转化为<code>true</code>一块记的话，较容易引起混乱。</p>
<p>只有<code>null(小写的 n)、undefined、””(中间没有空格)、NAN、0、-0、false</code>再进行类型转换时，可以转化为<code>false</code>。所有对象类型都会转化为<code>true</code>。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce99779ff0b16~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>为了更好的准备面试，小鹿送你一套动画记忆法：</p>
<h4 class="heading">1、<code>null与 unefined</code></h4>
<p>它俩什么到底区别？初学者最容易弄不懂。</p>
<blockquote>
<p>null 表示"没有对象"，即该处不应该有值。undefined 表示"缺少值"，就是此处应该有一个值，但是还没有定义。</p>
</blockquote>
<p>在细节上，null是一个表示"无"的对象，转为数值时为 0；undefined是一个表示"无"的原始值，转为数值时为NaN。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce9a8de947f1c~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>两者转化为<code>boolean</code>时，可以记忆为无，都会转化为<code>false</code>。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce9bd29a35900~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce9bef534dbf5~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h4 class="heading">2、<code>NaN 与 ""</code></h4>
<blockquote>
<p>NaN 属性是代表非数字值的特殊值。该属性用于指示某个值不是数字。可以把 Number 对象设置为该值，来指示其不是数字值。</p>
</blockquote>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce9d89af7144c~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce9daae12a54e~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<blockquote>
<p>注意：这里的空字符串没有空格，如果面试的时候加空格了，比如这样“ ”，它就返回 true 了。</p>
</blockquote>
<h4 class="heading"><code>3、+0 与 -0</code></h4>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce9e1745bf97b~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dce9e35421b7b7~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<blockquote>
<p>如果此处有忽略，请给予补充！</p>
</blockquote>
<h3 class="heading">二、对象转原始类型</h3>
<p>对象类型转原始类型时，它会根据不同的转换对象调用不同的转化方法（回顾一下我们之前写的文章，对象类型和原始类型的区别）。</p>
<p>如果转化为字符串，就会调用<code>toString</code>方法；</p>
<p>如果转化非字符串，则会优先调用<code>valueOf</code>方法（返回自身类型）。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea1303a0f03c~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
<figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea1414de8e07~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<blockquote>
<p>注意：toString 方法和 valueOf 方法是可以改写的。</p>
</blockquote>
<h4 class="heading">2.1 对象类型转字符串</h4>
<p>对象转字符串类型的话，直接调用原有的toString方法。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea20927efe0d~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea21728a03ca~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h4 class="heading">2.2 对象类型转原始类型</h4>
<p>除 <code>String</code> 类型外，<code>Object</code> 转其他类型的话，直接调用<code>valueOf</code>方法。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea2884017657~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>如果调用<code>valueOf</code>返回的不是原始类型的值，会调用<code>toString</code>方法，<code>toString</code>如果返回的不是原始值，就会报错。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea2ea4f0e6cb~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea2f7e8d8d15~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h3 class="heading">三、四则运算</h3>
<h4 class="heading">3.1 加法运算</h4>
<blockquote>
<p>加法运算符是在运行时决定，到底是执行相加，还是执行连接。运算数的不同，导致了不同的语法行为，这种现象称为“重载”。</p>
</blockquote>
<p>1、如果双方都不是字符串，则将转化为数字或字符串。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea38c8e00d53~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
2、字符串和字符串以及字符串和非字符串相加都会进行连接。<p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea3e2b475453~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
3、对于无效格式，则会转化为NaN。<p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea4125aa4a35~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h4 class="heading">3.2  其他运算</h4>
<p>其他算术运算符（比如减法、除法和乘法）都不会发生重载。它们的规则是：所有运算子一律转为数值，再进行相应的数学运算。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea44c384ac61~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h3 class="heading">四、逻辑运算符</h3>
<h4 class="heading">5.1 条件判断</h4>
<p><code>&amp;&amp;:</code>所有条件为真，整体才为真。</p>
<p><code>||:</code>只有一个条件为真，整体就为真。</p>
<h4 class="heading">5.2 赋值操作</h4>
<p><strong>1、A &amp;&amp; B</strong></p>
<p>首先看 A 的真假，A 为假，返回 A 的值，A 为真返回 B 的值。（不管B 是啥）</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea52b5ff951a~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h3 class="heading">五、类型判断</h3>
<h4 class="heading">6.1 typeOf</h4>
<p><code>typeOf</code>一直有一个问题就是能够正确的判断类型吗？除了<code>null</code>都显示正确的类型，但是并不能准确的判断对象的具体类型。</p>
<blockquote>
<p>对于为什么 <code>typeOf null</code> 判断为对象类型，上一篇文章已经分享过，可以看之前的一篇文章。</p>
</blockquote>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea710b756b2b~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure>
那我们用什么准确的判断呢？要想正确的判断一个对象类型是通过内部机制的原型链判断的，instanceOf能够正确的判断对象的原理是什么？这个问题不在这里说，因为后期会出一个用动画形式去讲解 JS 的原型和原型链，到时候初学者就更容易懂了。<p></p>
<h3 class="heading">六、== 和 === 有什么区别？</h3>
<p>对于==和===之间的区别，使用==，如果比较的双方的数据类型不一样的话，就进行类型转换。如上所述，类型转换之后再进行对比。</p>
<h4 class="heading">7.1==的比较步骤</h4>
<p>首先比较双方的类型是否相等，如果类型相同，就比较大小，否则将会以下面步骤进行，首先进行类型转换。</p>
<p>1、判断两者是否为null和undefined，是则返回 true。</p>
<p>2、判断两者类型是否分别为字符串和数字，是的话将字符串转化为number类型，然后比较大小。</p>
<p>3、如果两者其中一个是布尔类型，就把先把布尔类型转化为number再进行判断大小。</p>
<p>4、如果对象类型和原始类型比较，先把对象类型转化为原始类型再进行比较。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea7cd435c71d~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h4 class="heading">7.2 ===</h4>
<p>对于===来说，只比较数值大小就可以了。</p>
<h3 class="heading">小结</h3>
<p>以上我们对数据类型转换进行了全面的总结，尤其是其中的一些细节问题考的特别的细，所以小鹿以动画的形式展现出来，便于在面试的时候牢记使用，更重要的一点就是在实际开发中遇到这些问题不用到处翻找，从而使你快速的定位问题，节省开发时间。</p>
<p>上边的代码例子，都是小鹿亲自在控制台输出查得出的结果，但是也避免不了有错误的情况，如果有错误可以给小鹿提出来哦！</p>
<br>
<h2 class="heading">❤️ 不要忘记留下你学习的脚印 <span style="color:red">[点赞 + 收藏 + 评论]</span></h2>
<p>文章都看完了，为何不妨点个赞呢？嘻嘻，那就说明你很自私，你怕那么好的文章让别人也看到。开个小小玩笑。</p>
<p>其实我也很自私，我把我的一直以来坚持原创的公众号:「小鹿动画学编程」偷偷给你，里边汇聚了小鹿以动画形式讲解的数据结构与算法、网络原理、Web 等技术文章。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2019/10/15/16dcea9ae6519a46~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p><strong>作者Info：</strong></p>
<blockquote>
<p>【作者】：小鹿</p>
<p>【原创公众号】小鹿动画学编程</p>
<p>【简介】：和小鹿同学一起用动画的方式从零基础学编程，将Web前端领域、数据结构与算法、网络原理等通俗易懂的呈献给小伙伴。<strong>公众号回复 “资料” 送一从零自学资料大礼包！</strong></p>
<p>【转载说明】：转载请说明出处，谢谢合作！~</p>
</blockquote>
