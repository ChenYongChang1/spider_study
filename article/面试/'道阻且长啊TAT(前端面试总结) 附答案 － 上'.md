标题:道阻且长啊TAT(前端面试总结) 附答案 － 上
描述:渲染引擎－ 渲染界面:Firefox、Chrome和Safari是基于两种渲染引擎构建的，Firefox使用Geoko——Mozilla自主研发的渲染引擎，Safari和Chrome都使用webkit. ...... 类似百度搜索的提示框，兼容各大浏览器，可用键盘控制. 勉强憋…

<p>之前在 <a href="https://segmentfault.com/a/1190000010631325">https://segmentfault.com/a/1190000010631325</a> 看到过这篇文章，最近闲下来就做着玩了一下， 如有误，还请斧正</p>
<h2 id="-">腾讯一面</h2>
<ul>
<li><p>1.浏览器工作原理 </p>
<ul>
<li>用户界面－ 包括地址栏、后退/前进按钮、书签目浏览器引擎－ 用来查询及操作渲染引擎的接口</li>
<li>渲染引擎－ 渲染界面:Firefox、Chrome和Safari是基于两种渲染引擎构建的，Firefox使用Geoko——Mozilla自主研发的渲染引擎，Safari和Chrome都使用webkit.</li>
<li>网络－ 用来完成网络调用，例如http请求 UI 后端－ 用来绘制类似组合选择框及对话框等基本组件，具有不特定于某个平台的通用接口，底层使用操作系统的用户接口</li>
<li>JS解释器－ 解释执行JS代码</li>
<li>数据存储－ 属于持久层，浏览器需要在硬盘中保存类似cookie的各种数据</li>
</ul>
</li>
<li><p>2.Web安全,举例说明</p>
<ul>
<li>xss</li>
<li>https</li>
<li>混合内容</li>
<li>同源策略 </li>
</ul>
</li>
<li>3.状态码<ul>
<li>1xx 信息</li>
<li>2xx 成功</li>
<li>3xx 重定向</li>
<li>4xx 客户端错误</li>
<li>5xx 服务端错误</li>
</ul>
</li>
<li>4.同源<ul>
<li>同端口</li>
<li>同域名</li>
<li>同协议</li>
</ul>
</li>
<li><p>5.对象继承 </p>
<ul>
<li>所有继承都是基于原型(prorotype)的,由于js继承机制并不是明确规定的,所以继承的方式也特别多<ul>
<li>原型链继承<pre><code class="hljs bash">  Child.prototype = new Parent();</code></pre></li>
<li>原型继承<pre><code class="hljs bash">  Child.prototype = Parent.prototype;
  Child.prototype.constructor = Child;</code></pre></li>
<li>拷贝继承(extend)</li>
<li>call,apply</li>
</ul>
</li>
</ul>
</li>
<li><p>6.ES6历史以及新特性有哪些?</p>
<ul>
<li>......</li>
</ul>
</li>
<li>7.promise原理<ul>
<li>理解promise 主要使用场景，理解promise 几个状态(pending,fulilled,rejected)</li>
</ul>
</li>
<li><p>8.事件模型</p>
<ul>
<li>DOM0级模型 <code>div.onclick = fn()</code></li>
<li>DOM2级模型 <code>addEventListener(eventType, handler, useCapture)</code></li>
<li>IE事件模型 <code>attachEvent( "eventType","handler")</code></li>
</ul>
</li>
<li><p>9.常见兼容性问题,列举(移动端/PC端)</p>
</li>
<li>10.性能优化<ul>
<li>减少http请求</li>
<li>静态资源压缩</li>
<li>CDN加速</li>
<li>减少全局变量</li>
<li>script标签放至body后</li>
</ul>
</li>
</ul>
<p>腾讯二面（机试）<br>类似百度搜索的提示框，兼容各大浏览器，可用键盘控制. 勉强憋了出来，但是挂掉了，犯了一些低级错误，显示经验不足． 面试官建议多看书，多写组件.</p>
<h2 id="-">阿里一面</h2>
<ul>
<li>1.Ajax原理<ul>
<li>create =&gt; open =&gt; send =&gt; onchange</li>
</ul>
</li>
<li>2.浏览器解析过程<ul>
<li>流程： 解析html =&gt; 构建dom树-&gt;构建render树-&gt;布局render树-&gt;绘制render树</li>
</ul>
</li>
<li>3.垂直居中<ul>
<li>flex</li>
<li>line-height, text-center</li>
<li>postion , margin</li>
<li>display: table, vertical-align: middle</li>
<li>position, top:0, bottom: 0</li>
</ul>
</li>
<li>4.数据类型判断<ul>
<li>typeof</li>
<li>instanceof</li>
<li>toString</li>
</ul>
</li>
<li>5.路由实现<ul>
<li>location.hash+hashchange</li>
<li>history.pushState()+popState</li>
</ul>
</li>
<li>6.数据本地存储<ul>
<li>localStorage</li>
<li>indexDB</li>
<li>cookie</li>
<li>seesionStorage</li>
</ul>
</li>
<li>7.跨域<ul>
<li>jsonp</li>
<li>cors</li>
</ul>
</li>
<li>8.数据双向绑定单向绑定优缺点<ul>
<li>双向绑定是自动管理状态的，对处理有用户交互的场景非常合适，代码量少，当项目越来越大的时候，调试也变得越来越复杂，难以跟踪问题</li>
<li>单向绑定是无状态的, 程序调试相对容易, 可以避免程序复杂度上升时产生的各种问题, 当然写代码时就没有双向绑定那么爽了 </li>
</ul>
</li>
</ul>
<h2 id="-">阿里二面</h2>
<ul>
<li>1.无线性能优化<ul>
<li>往上翻，有同样的问题</li>
</ul>
</li>
<li>2.Tap事件,Touch<ul>
<li>Tap 是zepto库封装好的事件，在移动端上可以替代click 事件，从而规避300ms问题</li>
<li>Touch 是移动端上的手势事件, 如 touchstart , touchend , touchmove</li>
</ul>
</li>
<li>3.数据存储<ul>
<li>往上翻，有同样的问题<br>搜狐一面</li>
</ul>
</li>
<li>1.Dom操作<ul>
<li>增删改查, 如：<ul>
<li>document.elementById</li>
<li>document.querySelectAll</li>
<li>document.appendChild</li>
<li>docuemnt.removeChild</li>
<li>......</li>
</ul>
</li>
</ul>
</li>
<li>2.移动布局方案<ul>
<li>Rem, Em</li>
<li>flex</li>
<li>百分比</li>
<li>media query</li>
</ul>
</li>
<li>3.前后端协作<ul>
<li>.....</li>
</ul>
</li>
<li>4.原生Ajax实现过程<ul>
<li>往上翻，有同样的问题<br>搜狐二面</li>
</ul>
</li>
<li>1.单链表反转<pre><code class="hljs bash">  <span class="hljs-keyword">function</span> ReverseList(pHead) {
      var pre = null;
      var next = null;
      <span class="hljs-keyword">while</span> (pHead != null) {
      next = pHead.next;
      pHead.next = pre;
      pre = pHead;
      pHead = next;
      }
      <span class="hljs-built_in">return</span> pre;
  }</code></pre></li>
<li><p>2.快排</p>
<pre><code class="hljs bash">  const quickSort = (arr) =&gt; {
      <span class="hljs-keyword">if</span>(arr.length &lt; 1) <span class="hljs-built_in">return</span> arr;
      <span class="hljs-built_in">let</span> inx = Math.floor(arr.length/2);
      <span class="hljs-built_in">let</span> pivot = arr.splice(inx,1)[0];
      <span class="hljs-built_in">let</span> left = [];
      <span class="hljs-built_in">let</span> right = [];
      <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i=0; i&lt;arr.length; i++){
      <span class="hljs-keyword">if</span>(arr[i] &lt; pivot){
          left.push(arr[i])
      }<span class="hljs-keyword">else</span>{
          right.push(arr[i])
      }
      }

      <span class="hljs-built_in">return</span> quickSort(left).concat(pivot,quickSort(right))
  }</code></pre></li>
<li>3.即时通信(除了Ajax和websocket)<ul>
<li>Comet技术：基于HTTP长连接的Web端实时通信技术</li>
<li>SSE：服务器发送事件,使用长链接进行通讯</li>
</ul>
</li>
<li>4.服务器代理转发如何处理cookie(nginx) <pre><code class="hljs bash">  proxy_cookie_domain localhost example.org;
  proxy_cookie_domain ~\.([a-z]+\.[a-z]+)$ <span class="hljs-variable">$1</span>;
  proxy_cookie_path /one/ /;
  proxy_cookie_path / /two/;</code></pre></li>
<li>5.对象继承<ul>
<li><strong>proto</strong></li>
<li>prototype</li>
<li>Object</li>
</ul>
</li>
<li>6.this<ul>
<li>构造函数调用</li>
<li>apply,call使用</li>
<li>对象的方法调用</li>
<li>普通函数调用</li>
</ul>
</li>
<li>7.rem布局的优缺点 </li>
</ul>
<h2 id="-alloy-team">腾讯Alloy Team</h2>
<p>一面(记录两个,其他都还好)</p>
<ul>
<li>实现动画有哪些途径 <ul>
<li>CSS3</li>
<li>JS帧动画,定时器,requestAnimateFrame</li>
<li>Canvas动画</li>
<li>SVG</li>
<li>图片</li>
</ul>
</li>
<li>web安全<ul>
<li>https加密过程,证书用途<ul>
<li>服务端配置证书 -&gt; 传送证书 -&gt; 客户端解析证书 -&gt; 传送加密信息 -&gt; 服务端解密信息 -&gt; 传输加密后信息 -&gt; 客户端解密信息</li>
</ul>
</li>
<li>xss几种形式,防范手段,过滤哪些字符?<ul>
<li>形式<ul>
<li>数据从一个不可靠的链接进入到一个web应用程序</li>
<li>没有过滤掉恶意代码的动态内容被发送给web用户</li>
</ul>
</li>
<li>防范手段<ul>
<li>不信任任何用户的输入(过滤，转义)</li>
<li>使用HTTP头指定类型</li>
</ul>
</li>
<li>过滤字符<ul>
<li>&lt;,&gt;,",&amp;quot</li>
</ul>
</li>
</ul>
</li>
<li>xsrf原理,实例,防范手段(Laravel的token)</li>
<li>Sql注入<ul>
<li>前端恶意提交sql代码,来篡改服务端的sql执行代码</li>
</ul>
</li>
</ul>
</li>
<li>性能优化<ul>
<li>代码优化(html,css,js)</li>
<li>网络性能优化:<ol>
<li>Cache缓存之强制缓存和协商缓存</li>
<li>CDN原理及应用</li>
<li>HTTP压缩之gzip</li>
</ol>
</li>
</ul>
</li>
<li>上下文环境对象</li>
<li><p>设计模式(要求说出如何实现,应用,优缺点): </p>
<ul>
<li><p>单例模式</p>
<ul>
<li>定义: 产生一个类的唯一实例</li>
<li><p>实现: </p>
<pre><code class="hljs bash">  const createMask = ()=&gt;{
      <span class="hljs-built_in">let</span> mask = null;
      <span class="hljs-built_in">return</span> ()=&gt; mask || document.appendChild(document.createElement(<span class="hljs-string">'div'</span>))
  }

  const mask = createMask();</code></pre></li>
<li>优点:<ol>
<li>提供了对唯一实例的受控访问</li>
<li>避免对共享资源的多重占用</li>
<li>节约系统资源</li>
</ol>
</li>
<li>缺点:<ol>
<li>扩展性差</li>
<li>职责过重</li>
</ol>
</li>
</ul>
</li>
<li>工厂模式<ul>
<li>定义: 创建对象时无须指定创建对象的具体灯</li>
<li>实现: <pre><code class="hljs bash">  const Example = <span class="hljs-keyword">function</span>(name,age){
      this.name = name || <span class="hljs-string">'Tom'</span>,
      this.age = age || <span class="hljs-string">'18'</span>
      this.say = <span class="hljs-function"><span class="hljs-title">function</span></span>(){
          console.log(`name:<span class="hljs-variable">${this.name}</span>,age:<span class="hljs-variable">${this.age}</span>`)
      }
  }</code></pre></li>
<li>优点:<ol>
<li>结构清淅,有效的封装变化 </li>
<li>对调用者屏蔽具体实现， 调用者只需关心产品的接口</li>
<li>降低耦合度</li>
</ol>
</li>
<li>缺点:<ol>
<li>添加新的类，需要改写工厂类</li>
</ol>
</li>
</ul>
</li>
<li><p>发布订阅模式</p>
<ul>
<li>定义: 定义对象间一种一对多的依赖关系，使得当每一个对象改变状态，则所有依赖于它的对象都会得到通知并自动更新。</li>
<li><p>实现: </p>
<pre><code class="hljs bash">  const Example = {};
  Example.clientList = [];
  Example.listen = <span class="hljs-keyword">function</span>(fn){
      this.clientList.push(fn)
  }
  Example.trigger = <span class="hljs-function"><span class="hljs-title">function</span></span>(){
      <span class="hljs-keyword">for</span>(<span class="hljs-built_in">let</span> i=0,fn; fn=this.clientList[i++]){
          fn.apply(this,arguments)
      }
  }

  Example.listen(<span class="hljs-keyword">function</span>(message){
      console.log(message) // 我发布了一个消息，此时订阅者会收到消息
  })  

  Example.trigger(<span class="hljs-function"><span class="hljs-title">function</span></span>(){
      console.log(<span class="hljs-string">'我发布了一个消息，此时订阅者会收到消息'</span>)
  })</code></pre></li>
<li>优点:<ol>
<li>时间上的解藕 </li>
<li>对象之间的解藕</li>
<li>支持广播通信</li>
</ol>
</li>
<li>缺点:<ol>
<li>如果一个观察目标对象有很多直接和间接的观察者的话，将所有的观察者都通知到会花费很多时间</li>
<li>如果在观察者和观察目标之间有循环依赖的话，观察目标会触发它们之间进行循环调用，可能导致系统崩溃</li>
<li>观察者模式没有相应的机制让观察者知道所观察的目标对象是怎么发生变化的，而仅仅只是知道观察目标发生了变化</li>
</ol>
</li>
</ul>
</li>
</ul>
</li>
<li>跨域(产生原因)<ul>
<li>JSONP原理<ul>
<li>利用script标签没有跨域的漏洞进行第三方通信，第三方的响应数据为json，故称之为jsonp (json padding)</li>
</ul>
</li>
<li>CORS如何设置<ul>
<li>通过改变response headers 设置白名单,来允许指定origin进行通信</li>
</ul>
</li>
<li>Nginx代理<pre><code class="hljs bash">  location / {
      proxy_pass  xxx
  }</code></pre></li>
</ul>
</li>
<li>读过哪些框架源码?</li>
<li>如何写一个CSS库,要注意哪些东西?<ol>
<li>总是类名优先</li>
<li>组件代码放在一起</li>
<li>使用一致的类命名空间</li>
<li>维护命名空间和文件名之间的严格映射</li>
<li>避免组件外的样式泄露</li>
<li>避免组件内的样式泄露</li>
<li>遵守组件边界</li>
<li>松散地整合外部样式</li>
</ol>
</li>
</ul>
