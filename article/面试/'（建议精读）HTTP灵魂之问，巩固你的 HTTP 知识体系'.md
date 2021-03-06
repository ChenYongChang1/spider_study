标题:（建议精读）HTTP灵魂之问，巩固你的 HTTP 知识体系
描述:上回就已经承诺过大家，一定会出 HTTP 的系列文章，今天终于整理完成了。作为一个 web 开发，HTTP 几乎是天天要打交道的东西，但我发现大部分人对 HTTP 只是浅尝辄止，对更多的细节及原理就了解不深了，在面试的时候感觉非常吃力。这篇文章就是为了帮助大家树立完整的 HTT…

<p>上回就已经承诺过大家，一定会出 HTTP 的系列文章，今天终于整理完成了。作为一个 web 开发，HTTP 几乎是天天要打交道的东西，但我发现大部分人对 HTTP 只是浅尝辄止，对更多的细节及原理就了解不深了，在面试的时候感觉非常吃力。这篇文章就是为了帮助大家树立完整的 HTTP 知识体系，并达到一定的深度，从容地应对各种灵魂之问，也同时提升自己作为一个 web 开发的专业素养吧。这是本文的思维导图:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/23/17104ea1fdee5669~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h2 class="heading">001. HTTP 报文结构是怎样的？</h2>
<p>对于 TCP 而言，在传输的时候分为两个部分:<strong>TCP头</strong>和<strong>数据部分</strong>。</p>
<p>而 HTTP 类似，也是<code>header + body</code>的结构，具体而言:</p>
<pre><code class="hljs bash" lang="bash">起始行 + 头部 + 空行 + 实体
</code></pre><p>由于 http <code>请求报文</code>和<code>响应报文</code>是有一定区别，因此我们分开介绍。</p>
<h3 class="heading">起始行</h3>
<p>对于请求报文来说，起始行类似下面这样:</p>
<pre><code class="hljs js" lang="js">GET /home HTTP/<span class="hljs-number">1.1</span>
</code></pre><p>也就是<strong>方法 + 路径 + http版本</strong>。</p>
<p>对于响应报文来说，起始行一般张这个样:</p>
<pre><code class="hljs js" lang="js">HTTP/<span class="hljs-number">1.1</span> <span class="hljs-number">200</span> OK
</code></pre><p>响应报文的起始行也叫做<code>状态行</code>。由<strong>http版本、状态码和原因</strong>三部分组成。</p>
<p>值得注意的是，在起始行中，每两个部分之间用<strong>空格</strong>隔开，最后一个部分后面应该接一个<strong>换行</strong>，严格遵循<code>ABNF</code>语法规范。</p>
<h3 class="heading">头部</h3>
<p>展示一下请求头和响应头在报文中的位置:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd6012e2fc88~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd62af8538e4~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>不管是请求头还是响应头，其中的字段是相当多的，而且牵扯到<code>http</code>非常多的特性，这里就不一一列举的，重点看看这些头部字段的格式：</p>
<ul>
<li>
<ol>
<li>字段名不区分大小写</li>
</ol>
</li>
<li>
<ol start="2">
<li>字段名不允许出现空格，不可以出现下划线<code>_</code></li>
</ol>
</li>
<li>
<ol start="3">
<li>字段名后面必须<strong>紧接着<code>:</code></strong></li>
</ol>
</li>
</ul>
<h3 class="heading">空行</h3>
<p>很重要，用来区分开<code>头部</code>和<code>实体</code>。</p>
<p>问: 如果说在头部中间故意加一个空行会怎么样？</p>
<p>那么空行后的内容全部被视为实体。</p>
<h3 class="heading">实体</h3>
<p>就是具体的数据了，也就是<code>body</code>部分。请求报文对应<code>请求体</code>, 响应报文对应<code>响应体</code>。</p>
<h2 class="heading">002. 如何理解 HTTP 的请求方法？</h2>
<h3 class="heading">有哪些请求方法？</h3>
<p><code>http/1.1</code>规定了以下请求方法(注意，都是大写):</p>
<ul>
<li>GET: 通常用来获取资源</li>
<li>HEAD: 获取资源的元信息</li>
<li>POST: 提交数据，即上传数据</li>
<li>PUT: 修改数据</li>
<li>DELETE: 删除资源(几乎用不到)</li>
<li>CONNECT: 建立连接隧道，用于代理服务器</li>
<li>OPTIONS: 列出可对资源实行的请求方法，用来跨域请求</li>
<li>TRACE: 追踪请求-响应的传输路径</li>
</ul>
<h3 class="heading">GET 和 POST 有什么区别？</h3>
<p>首先最直观的是语义上的区别。</p>
<p>而后又有这样一些具体的差别:</p>
<ul>
<li>从<strong>缓存</strong>的角度，GET 请求会被浏览器主动缓存下来，留下历史记录，而 POST 默认不会。</li>
<li>从<strong>编码</strong>的角度，GET 只能进行 URL 编码，只能接收 ASCII 字符，而 POST 没有限制。</li>
<li>从<strong>参数</strong>的角度，GET 一般放在 URL 中，因此不安全，POST 放在请求体中，更适合传输敏感信息。</li>
<li>从<strong>幂等性</strong>的角度，<code>GET</code>是<strong>幂等</strong>的，而<code>POST</code>不是。(<code>幂等</code>表示执行相同的操作，结果也是相同的)</li>
<li>从<strong>TCP</strong>的角度，GET 请求会把请求报文一次性发出去，而 POST 会分为两个 TCP 数据包，首先发 header 部分，如果服务器响应 100(continue)， 然后发 body 部分。(<strong>火狐</strong>浏览器除外，它的 POST 请求只发一个 TCP 包)</li>
</ul>
<h2 class="heading">003: 如何理解 URI？</h2>
<p><strong>URI</strong>, 全称为(Uniform Resource Identifier), 也就是<strong>统一资源标识符</strong>，它的作用很简单，就是区分互联网上不同的资源。</p>
<p>但是，它并不是我们常说的<code>网址</code>, 网址指的是<code>URL</code>, 实际上<code>URI</code>包含了<code>URN</code>和<code>URL</code>两个部分，由于 URL 过于普及，就默认将 URI 视为 URL 了。</p>
<h3 class="heading">URI 的结构</h3>
<p>URI 真正最完整的结构是这样的。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd677629b70d~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>可能你会有疑问，好像跟平时见到的不太一样啊！先别急，我们来一一拆解。</p>
<p><strong>scheme</strong> 表示协议名，比如<code>http</code>, <code>https</code>, <code>file</code>等等。后面必须和<code>://</code>连在一起。</p>
<p><strong>user:passwd</strong>@ 表示登录主机时的用户信息，不过很不安全，不推荐使用，也不常用。</p>
<p><strong>host:port</strong>表示主机名和端口。</p>
<p><strong>path</strong>表示请求路径，标记资源所在位置。</p>
<p><strong>query</strong>表示查询参数，为<code>key=val</code>这种形式，多个键值对之间用<code>&amp;</code>隔开。</p>
<p><strong>fragment</strong>表示 URI 所定位的资源内的一个<strong>锚点</strong>，浏览器可以根据这个锚点跳转到对应的位置。</p>
<p>举个例子:</p>
<pre><code class="hljs js" lang="js">https:<span class="hljs-comment">//www.baidu.com/s?wd=HTTP&amp;rsv_spt=1</span>
</code></pre><p>这个 URI 中，<code>https</code>即<code>scheme</code>部分，<code>www.baidu.com</code>为<code>host:port</code>部分（注意，http 和 https 的默认端口分别为80、443），<code>/s</code>为<code>path</code>部分，而<code>wd=HTTP&amp;rsv_spt=1</code>就是<code>query</code>部分。</p>
<h3 class="heading">URI 编码</h3>
<p>URI 只能使用<code>ASCII</code>, ASCII 之外的字符是不支持显示的，而且还有一部分符号是界定符，如果不加以处理就会导致解析出错。</p>
<p>因此，URI 引入了<code>编码</code>机制，将所有<strong>非 ASCII 码字符</strong>和<strong>界定符</strong>转为十六进制字节值，然后在前面加个<code>%</code>。</p>
<p>如，空格被转义成了<code>%20</code>，<strong>三元</strong>被转义成了<code>%E4%B8%89%E5%85%83</code>。</p>
<h2 class="heading">004: 如何理解 HTTP 状态码？</h2>
<p>RFC 规定 HTTP 的状态码为<strong>三位数</strong>，被分为五类:</p>
<ul>
<li><strong>1xx</strong>: 表示目前是协议处理的中间状态，还需要后续操作。</li>
<li><strong>2xx</strong>: 表示成功状态。</li>
<li><strong>3xx</strong>: 重定向状态，资源位置发生变动，需要重新请求。</li>
<li><strong>4xx</strong>: 请求报文有误。</li>
<li><strong>5xx</strong>: 服务器端发生错误。</li>
</ul>
<p>接下来就一一分析这里面具体的状态码。</p>
<h3 class="heading">1xx</h3>
<p><strong>101 Switching Protocols</strong>。在<code>HTTP</code>升级为<code>WebSocket</code>的时候，如果服务器同意变更，就会发送状态码 101。</p>
<h3 class="heading">2xx</h3>
<p><strong>200 OK</strong>是见得最多的成功状态码。通常在响应体中放有数据。</p>
<p><strong>204 No Content</strong>含义与 200 相同，但响应头后没有 body 数据。</p>
<p><strong>206 Partial Content</strong>顾名思义，表示部分内容，它的使用场景为 HTTP 分块下载和断点续传，当然也会带上相应的响应头字段<code>Content-Range</code>。</p>
<h3 class="heading">3xx</h3>
<p><strong>301 Moved Permanently</strong>即永久重定向，对应着<strong>302 Found</strong>，即临时重定向。</p>
<p>比如你的网站从 HTTP 升级到了 HTTPS 了，以前的站点再也不用了，应当返回<code>301</code>，这个时候浏览器默认会做缓存优化，在第二次访问的时候自动访问重定向的那个地址。</p>
<p>而如果只是暂时不可用，那么直接返回<code>302</code>即可，和<code>301</code>不同的是，浏览器并不会做缓存优化。</p>
<p><strong>304 Not Modified</strong>: 当协商缓存命中时会返回这个状态码。详见<a target="_blank" href="http://47.98.159.95/my_blog/perform/001.html">浏览器缓存</a></p>
<h3 class="heading">4xx</h3>
<p><strong>400 Bad Request</strong>: 开发者经常看到一头雾水，只是笼统地提示了一下错误，并不知道哪里出错了。</p>
<p><strong>403 Forbidden</strong>: 这实际上并不是请求报文出错，而是服务器禁止访问，原因有很多，比如法律禁止、信息敏感。</p>
<p><strong>404 Not Found</strong>: 资源未找到，表示没在服务器上找到相应的资源。</p>
<p><strong>405 Method Not Allowed</strong>: 请求方法不被服务器端允许。</p>
<p><strong>406 Not Acceptable</strong>: 资源无法满足客户端的条件。</p>
<p><strong>408 Request Timeout</strong>: 服务器等待了太长时间。</p>
<p><strong>409 Conflict</strong>: 多个请求发生了冲突。</p>
<p><strong>413 Request Entity Too Large</strong>: 请求体的数据过大。</p>
<p><strong>414 Request-URI Too Long</strong>: 请求行里的 URI 太大。</p>
<p><strong>429 Too Many Request</strong>: 客户端发送的请求过多。</p>
<p><strong>431 Request Header Fields Too Large</strong>请求头的字段内容太大。</p>
<h3 class="heading">5xx</h3>
<p><strong>500 Internal Server Error</strong>: 仅仅告诉你服务器出错了，出了啥错咱也不知道。</p>
<p><strong>501 Not Implemented</strong>: 表示客户端请求的功能还不支持。</p>
<p><strong>502 Bad Gateway</strong>: 服务器自身是正常的，但访问的时候出错了，啥错误咱也不知道。</p>
<p><strong>503 Service Unavailable</strong>: 表示服务器当前很忙，暂时无法响应服务。</p>
<h2 class="heading">005: 简要概括一下 HTTP 的特点？HTTP 有哪些缺点？</h2>
<h3 class="heading">HTTP 特点</h3>
<p>HTTP 的特点概括如下:</p>
<ol>
<li>
<p>灵活可扩展，主要体现在两个方面。一个是语义上的自由，只规定了基本格式，比如空格分隔单词，换行分隔字段，其他的各个部分都没有严格的语法限制。另一个是传输形式的多样性，不仅仅可以传输文本，还能传输图片、视频等任意数据，非常方便。</p>
</li>
<li>
<p>可靠传输。HTTP 基于 TCP/IP，因此把这一特性继承了下来。这属于 TCP 的特性，不具体介绍了。</p>
</li>
<li>
<p>请求-应答。也就是<code>一发一收</code>、<code>有来有回</code>， 当然这个请求方和应答方不单单指客户端和服务器之间，如果某台服务器作为代理来连接后端的服务端，那么这台服务器也会扮演<strong>请求方</strong>的角色。</p>
</li>
<li>
<p>无状态。这里的状态是指<strong>通信过程的上下文信息</strong>，而每次 http 请求都是独立、无关的，默认不需要保留状态信息。</p>
</li>
</ol>
<h3 class="heading">HTTP 缺点</h3>
<h4 class="heading">无状态</h4>
<p>所谓的优点和缺点还是要分场景来看的，对于 HTTP 而言，最具争议的地方在于它的<strong>无状态</strong>。</p>
<p>在需要长连接的场景中，需要保存大量的上下文信息，以免传输大量重复的信息，那么这时候无状态就是 http 的缺点了。</p>
<p>但与此同时，另外一些应用仅仅只是为了获取一些数据，不需要保存连接上下文信息，无状态反而减少了网络开销，成为了 http 的优点。</p>
<h4 class="heading">明文传输</h4>
<p>即协议里的报文(主要指的是头部)不使用二进制数据，而是文本形式。</p>
<p>这当然对于调试提供了便利，但同时也让 HTTP 的报文信息暴露给了外界，给攻击者也提供了便利。<code>WIFI陷阱</code>就是利用 HTTP 明文传输的缺点，诱导你连上热点，然后疯狂抓你所有的流量，从而拿到你的敏感信息。</p>
<h4 class="heading">队头阻塞问题</h4>
<p>当 http 开启长连接时，共用一个 TCP 连接，同一时刻只能处理一个请求，那么当前请求耗时过长的情况下，其它的请求只能处于阻塞状态，也就是著名的<strong>队头阻塞</strong>问题。接下来会有一小节讨论这个问题。</p>
<h2 class="heading">006: 对 Accept 系列字段了解多少？</h2>
<p>对于<code>Accept</code>系列字段的介绍分为四个部分: <strong>数据格式</strong>、<strong>压缩方式</strong>、<strong>支持语言</strong>和<strong>字符集</strong>。</p>
<h3 class="heading">数据格式</h3>
<p>上一节谈到 HTTP 灵活的特性，它支持非常多的数据格式，那么这么多格式的数据一起到达客户端，客户端怎么知道它的格式呢？</p>
<p>当然，最低效的方式是直接猜，有没有更好的方式呢？直接指定可以吗？</p>
<p>答案是肯定的。不过首先需要介绍一个标准——<strong>MIME</strong>(Multipurpose Internet Mail Extensions, <strong>多用途互联网邮件扩展</strong>)。它首先用在电子邮件系统中，让邮件可以发任意类型的数据，这对于 HTTP 来说也是通用的。</p>
<p>因此，HTTP 从<strong>MIME type</strong>取了一部分来标记报文 body 部分的数据类型，这些类型体现在<code>Content-Type</code>这个字段，当然这是针对于发送端而言，接收端想要收到特定类型的数据，也可以用<code>Accept</code>字段。</p>
<p>具体而言，这两个字段的取值可以分为下面几类:</p>
<ul>
<li>text： text/html, text/plain, text/css 等</li>
<li>image: image/gif, image/jpeg, image/png 等</li>
<li>audio/video: audio/mpeg, video/mp4 等</li>
<li>application: application/json, application/javascript, application/pdf, application/octet-stream</li>
</ul>
<h3 class="heading">压缩方式</h3>
<p>当然一般这些数据都是会进行编码压缩的，采取什么样的压缩方式就体现在了发送方的<code>Content-Encoding</code>字段上， 同样的，接收什么样的压缩方式体现在了接受方的<code>Accept-Encoding</code>字段上。这个字段的取值有下面几种：</p>
<ul>
<li>gzip: 当今最流行的压缩格式</li>
<li>deflate: 另外一种著名的压缩格式</li>
<li>br: 一种专门为 HTTP 发明的压缩算法</li>
</ul>
<pre><code class="hljs js" lang="js"><span class="hljs-comment">// 发送端</span>
Content-Encoding: gzip
<span class="hljs-comment">// 接收端</span>
Accept-Encoding: gzip
</code></pre><h3 class="heading">支持语言</h3>
<p>对于发送方而言，还有一个<code>Content-Language</code>字段，在需要实现国际化的方案当中，可以用来指定支持的语言，在接受方对应的字段为<code>Accept-Language</code>。如:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-comment">// 发送端</span>
Content-Language: zh-CN, zh, en
<span class="hljs-comment">// 接收端</span>
Accept-Language: zh-CN, zh, en
</code></pre><h3 class="heading">字符集</h3>
<p>最后是一个比较特殊的字段, 在接收端对应为<code>Accept-Charset</code>，指定可以接受的字符集，而在发送端并没有对应的<code>Content-Charset</code>, 而是直接放在了<code>Content-Type</code>中，以<strong>charset</strong>属性指定。如:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-comment">// 发送端</span>
Content-Type: text/html; charset=utf<span class="hljs-number">-8</span>
<span class="hljs-comment">// 接收端</span>
Accept-Charset: charset=utf<span class="hljs-number">-8</span>
</code></pre><p>最后以一张图来总结一下吧:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd6bb6d09c2d~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h2 class="heading">007: 对于定长和不定长的数据，HTTP 是怎么传输的？</h2>
<h3 class="heading">定长包体</h3>
<p>对于定长包体而言，发送端在传输的时候一般会带上
<code>Content-Length</code>, 来指明包体的长度。</p>
<p>我们用一个<code>nodejs</code>服务器来模拟一下:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

<span class="hljs-keyword">const</span> server = http.createServer();

server.on(<span class="hljs-string">'request'</span>, (req, res) =&gt; {
  <span class="hljs-keyword">if</span>(req.url === <span class="hljs-string">'/'</span>) {
    res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'text/plain'</span>);
    res.setHeader(<span class="hljs-string">'Content-Length'</span>, <span class="hljs-number">10</span>);
    res.write(<span class="hljs-string">"helloworld"</span>);
  }
})

server.listen(<span class="hljs-number">8081</span>, () =&gt; {
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"成功启动"</span>);
})
</code></pre><p>启动后访问: <strong>localhost:8081</strong>。</p>
<p>浏览器中显示如下:</p>
<pre><code class="hljs bash" lang="bash">helloworld
</code></pre><p>这是长度正确的情况，那不正确的情况是如何处理的呢？</p>
<p>我们试着把这个长度设置的小一些:</p>
<pre><code class="hljs js" lang="js">res.setHeader(<span class="hljs-string">'Content-Length'</span>, <span class="hljs-number">8</span>);
</code></pre><p>重启服务，再次访问，现在浏览器中内容如下:</p>
<pre><code class="hljs bash" lang="bash">hellowor
</code></pre><p>那后面的<code>ld</code>哪里去了呢？实际上在 http 的响应体中直接被截去了。</p>
<p>然后我们试着将这个长度设置得大一些:</p>
<pre><code class="hljs js" lang="js">res.setHeader(<span class="hljs-string">'Content-Length'</span>, <span class="hljs-number">12</span>);
</code></pre><p>此时浏览器显示如下:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd6f598bea62~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>直接无法显示了。可以看到<code>Content-Length</code>对于 http 传输过程起到了十分关键的作用，如果设置不当可以直接导致传输失败。</p>
<h3 class="heading">不定长包体</h3>
<p>上述是针对于<code>定长包体</code>，那么对于<code>不定长包体</code>而言是如何传输的呢？</p>
<p>这里就必须介绍另外一个 http 头部字段了:</p>
<pre><code class="hljs bash" lang="bash">Transfer-Encoding: chunked
</code></pre><p>表示分块传输数据，设置这个字段后会自动产生两个效果:</p>
<ul>
<li>Content-Length 字段会被忽略</li>
<li>基于长连接持续推送动态内容</li>
</ul>
<p>我们依然以一个实际的例子来模拟分块传输，nodejs 程序如下:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-keyword">const</span> http = <span class="hljs-built_in">require</span>(<span class="hljs-string">'http'</span>);

<span class="hljs-keyword">const</span> server = http.createServer();

server.on(<span class="hljs-string">'request'</span>, (req, res) =&gt; {
  <span class="hljs-keyword">if</span>(req.url === <span class="hljs-string">'/'</span>) {
    res.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'text/html; charset=utf8'</span>);
    res.setHeader(<span class="hljs-string">'Content-Length'</span>, <span class="hljs-number">10</span>);
    res.setHeader(<span class="hljs-string">'Transfer-Encoding'</span>, <span class="hljs-string">'chunked'</span>);
    res.write(<span class="hljs-string">"&lt;p&gt;来啦&lt;/p&gt;"</span>);
    setTimeout(<span class="hljs-function"><span class="hljs-params">()</span> =&gt;</span> {
      res.write(<span class="hljs-string">"第一次传输&lt;br/&gt;"</span>);
    }, <span class="hljs-number">1000</span>);
    setTimeout(<span class="hljs-function"><span class="hljs-params">()</span> =&gt;</span> {
      res.write(<span class="hljs-string">"第二次传输"</span>);
      res.end()
    }, <span class="hljs-number">2000</span>);
  }
})

server.listen(<span class="hljs-number">8009</span>, () =&gt; {
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"成功启动"</span>);
})
</code></pre><p>访问效果入下:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd728ba3840d~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>用 telnet 抓到的响应如下:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd78332368a0~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>注意，<code>Connection: keep-alive</code>及之前的为响应行和响应头，后面的内容为响应体，这两部分用换行符隔开。</p>
<p>响应体的结构比较有意思，如下所示:</p>
<pre><code class="hljs bash" lang="bash">chunk长度(16进制的数)
第一个chunk的内容
chunk长度(16进制的数)
第二个chunk的内容
......
0

</code></pre><p>最后是留有有一个<code>空行</code>的，这一点请大家注意。</p>
<p>以上便是 http 对于<strong>定长数据</strong>和<strong>不定长数据</strong>的传输方式。</p>
<h2 class="heading">008: HTTP 如何处理大文件的传输？</h2>
<p>对于几百 M 甚至上 G 的大文件来说，如果要一口气全部传输过来显然是不现实的，会有大量的等待时间，严重影响用户体验。因此，HTTP 针对这一场景，采取了<code>范围请求</code>的解决方案，允许客户端仅仅请求一个资源的一部分。</p>
<h3 class="heading">如何支持</h3>
<p>当然，前提是服务器要支持<strong>范围请求</strong>，要支持这个功能，就必须加上这样一个响应头:</p>
<pre><code class="hljs bash" lang="bash">Accept-Ranges: none
</code></pre><p>用来告知客户端这边是支持范围请求的。</p>
<h3 class="heading">Range 字段拆解</h3>
<p>而对于客户端而言，它需要指定请求哪一部分，通过<code>Range</code>这个请求头字段确定，格式为<code>bytes=x-y</code>。接下来就来讨论一下这个 Range 的书写格式:</p>
<ul>
<li><strong>0-499</strong>表示从开始到第 499 个字节。</li>
<li><strong>500</strong>- 表示从第 500 字节到文件终点。</li>
<li><strong>-100</strong>表示文件的最后100个字节。</li>
</ul>
<p>服务器收到请求之后，首先验证范围<strong>是否合法</strong>，如果越界了那么返回<code>416</code>错误码，否则读取相应片段，返回<code>206</code>状态码。</p>
<p>同时，服务器需要添加<code>Content-Range</code>字段，这个字段的格式根据请求头中<code>Range</code>字段的不同而有所差异。</p>
<p>具体来说，请求<code>单段数据</code>和请求<code>多段数据</code>，响应头是不一样的。</p>
<p>举个例子:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-comment">// 单段数据</span>
Range: bytes=<span class="hljs-number">0</span><span class="hljs-number">-9</span>
<span class="hljs-comment">// 多段数据</span>
Range: bytes=<span class="hljs-number">0</span><span class="hljs-number">-9</span>, <span class="hljs-number">30</span><span class="hljs-number">-39</span>

</code></pre><p>接下来我们就分别来讨论着两种情况。</p>
<h3 class="heading">单段数据</h3>
<p>对于<code>单段数据</code>的请求，返回的响应如下:</p>
<pre><code class="hljs bash" lang="bash">HTTP/1.1 206 Partial Content
Content-Length: 10
Accept-Ranges: bytes
Content-Range: bytes 0-9/100

i am xxxxx
</code></pre><p>值得注意的是<code>Content-Range</code>字段，<code>0-9</code>表示请求的返回，<code>100</code>表示资源的总大小，很好理解。</p>
<h3 class="heading">多段数据</h3>
<p>接下来我们看看多段请求的情况。得到的响应会是下面这个形式:</p>
<pre><code class="hljs bash" lang="bash">HTTP/1.1 206 Partial Content
Content-Type: multipart/byteranges; boundary=00000010101
Content-Length: 189
Connection: keep-alive
Accept-Ranges: bytes


--00000010101
Content-Type: text/plain
Content-Range: bytes 0-9/96

i am xxxxx
--00000010101
Content-Type: text/plain
Content-Range: bytes 20-29/96

eex jspy e
--00000010101--
</code></pre><p>这个时候出现了一个非常关键的字段<code>Content-Type: multipart/byteranges;boundary=00000010101</code>，它代表了信息量是这样的:</p>
<ul>
<li>请求一定是多段数据请求</li>
<li>响应体中的分隔符是 00000010101</li>
</ul>
<p>因此，在响应体中各段数据之间会由这里指定的分隔符分开，而且在最后的分隔末尾添上<code>--</code>表示结束。</p>
<p>以上就是 http 针对大文件传输所采用的手段。</p>
<h2 class="heading">009: HTTP 中如何处理表单数据的提交？</h2>
<p>在 http 中，有两种主要的表单提交的方式，体现在两种不同的<code>Content-Type</code>取值:</p>
<ul>
<li>application/x-www-form-urlencoded</li>
<li>multipart/form-data</li>
</ul>
<p>由于表单提交一般是<code>POST</code>请求，很少考虑<code>GET</code>，因此这里我们将默认提交的数据放在请求体中。</p>
<h3 class="heading">application/x-www-form-urlencoded</h3>
<p>对于<code>application/x-www-form-urlencoded</code>格式的表单内容，有以下特点:</p>
<ul>
<li>其中的数据会被编码成以<code>&amp;</code>分隔的键值对</li>
<li>字符以<strong>URL编码方式</strong>编码。</li>
</ul>
<p>如：</p>
<pre><code class="hljs js" lang="js"><span class="hljs-comment">// 转换过程: {a: 1, b: 2} -&gt; a=1&amp;b=2 -&gt; 如下(最终形式)</span>
<span class="hljs-string">"a%3D1%26b%3D2"</span>
</code></pre><h3 class="heading">multipart/form-data</h3>
<p>对于<code>multipart/form-data</code>而言:</p>
<ul>
<li>请求头中的<code>Content-Type</code>字段会包含<code>boundary</code>，且<code>boundary</code>的值有浏览器默认指定。例: <code>Content-Type: multipart/form-data;boundary=----WebkitFormBoundaryRRJKeWfHPGrS4LKe</code>。</li>
<li>数据会分为多个部分，每两个部分之间通过分隔符来分隔，每部分表述均有 HTTP 头部描述子包体，如<code>Content-Type</code>，在最后的分隔符会加上<code>--</code>表示结束。</li>
</ul>
<p>相应的<code>请求体</code>是下面这样:</p>
<pre><code class="hljs bash" lang="bash">Content-Disposition: form-data;name=<span class="hljs-string">"data1"</span>;
Content-Type: text/plain
data1
----WebkitFormBoundaryRRJKeWfHPGrS4LKe
Content-Disposition: form-data;name=<span class="hljs-string">"data2"</span>;
Content-Type: text/plain
data2
----WebkitFormBoundaryRRJKeWfHPGrS4LKe--
</code></pre><h3 class="heading">小结</h3>
<p>值得一提的是，<code>multipart/form-data</code> 格式最大的特点在于:<strong>每一个表单元素都是独立的资源表述</strong>。另外，你可能在写业务的过程中，并没有注意到其中还有<code>boundary</code>的存在，如果你打开抓包工具，确实可以看到不同的表单元素被拆分开了，之所以在平时感觉不到，是以为浏览器和 HTTP 给你封装了这一系列操作。</p>
<p>而且，在实际的场景中，对于图片等文件的上传，基本采用<code>multipart/form-data</code>而不用<code>application/x-www-form-urlencoded</code>，因为没有必要做 URL 编码，带来巨大耗时的同时也占用了更多的空间。</p>
<h2 class="heading">010: HTTP1.1 如何解决 HTTP 的队头阻塞问题？</h2>
<h3 class="heading">什么是 HTTP 队头阻塞？</h3>
<p>从前面的小节可以知道，HTTP 传输是基于<code>请求-应答</code>的模式进行的，报文必须是一发一收，但值得注意的是，里面的任务被放在一个任务队列中串行执行，一旦队首的请求处理太慢，就会阻塞后面请求的处理。这就是著名的<code>HTTP队头阻塞</code>问题。</p>
<h3 class="heading">并发连接</h3>
<p>对于一个域名允许分配多个长连接，那么相当于增加了任务队列，不至于一个队伍的任务阻塞其它所有任务。在RFC2616规定过客户端最多并发 2 个连接，不过事实上在现在的浏览器标准中，这个上限要多很多，Chrome 中是 6 个。</p>
<p>但其实，即使是提高了并发连接，还是不能满足人们对性能的需求。</p>
<h3 class="heading">域名分片</h3>
<p>一个域名不是可以并发 6 个长连接吗？那我就多分几个域名。</p>
<p>比如 content1.sanyuan.com 、content2.sanyuan.com。</p>
<p>这样一个<code>sanyuan.com</code>域名下可以分出非常多的二级域名，而它们都指向同样的一台服务器，能够并发的长连接数更多了，事实上也更好地解决了队头阻塞的问题。</p>
<h2 class="heading">011: 对 Cookie 了解多少？</h2>
<h3 class="heading">Cookie 简介</h3>
<p>前面说到了 HTTP 是一个无状态的协议，每次 http 请求都是独立、无关的，默认不需要保留状态信息。但有时候需要保存一些状态，怎么办呢？</p>
<p>HTTP 为此引入了 Cookie。Cookie 本质上就是浏览器里面存储的一个很小的文本文件，内部以键值对的方式来存储(在chrome开发者面板的Application这一栏可以看到)。向同一个域名下发送请求，都会携带相同的 Cookie，服务器拿到 Cookie 进行解析，便能拿到客户端的状态。而服务端可以通过响应头中的<code>Set-Cookie</code>字段来对客户端写入<code>Cookie</code>。举例如下:</p>
<pre><code class="hljs bash" lang="bash">// 请求头
Cookie: a=xxx;b=xxx
// 响应头
Set-Cookie: a=xxx
<span class="hljs-built_in">set</span>-Cookie: b=xxx
</code></pre><h3 class="heading">Cookie 属性</h3>
<h4 class="heading">生存周期</h4>
<p>Cookie 的有效期可以通过<strong>Expires</strong>和<strong>Max-Age</strong>两个属性来设置。</p>
<ul>
<li><strong>Expires</strong>即<code>过期时间</code></li>
<li><strong>Max-Age</strong>用的是一段时间间隔，单位是秒，从浏览器收到报文开始计算。</li>
</ul>
<p>若 Cookie 过期，则这个 Cookie 会被删除，并不会发送给服务端。</p>
<h4 class="heading">作用域</h4>
<p>关于作用域也有两个属性: <strong>Domain</strong>和<strong>path</strong>, 给 <strong>Cookie</strong> 绑定了域名和路径，在发送请求之前，发现域名或者路径和这两个属性不匹配，那么就不会带上 Cookie。值得注意的是，对于路径来说，<code>/</code>表示域名下的任意路径都允许使用 Cookie。</p>
<h4 class="heading">安全相关</h4>
<p>如果带上<code>Secure</code>，说明只能通过 HTTPS 传输 cookie。</p>
<p>如果 cookie 字段带上<code>HttpOnly</code>，那么说明只能通过 HTTP 协议传输，不能通过 JS 访问，这也是预防 XSS 攻击的重要手段。</p>
<p>相应的，对于 CSRF 攻击的预防，也有<code>SameSite</code>属性。</p>
<p><code>SameSite</code>可以设置为三个值，<code>Strict</code>、<code>Lax</code>和<code>None</code>。</p>
<p><strong>a.</strong> 在<code>Strict</code>模式下，浏览器完全禁止第三方请求携带Cookie。比如请求<code>sanyuan.com</code>网站只能在<code>sanyuan.com</code>域名当中请求才能携带 Cookie，在其他网站请求都不能。</p>
<p><strong>b.</strong> 在<code>Lax</code>模式，就宽松一点了，但是只能在 <code>get 方法提交表单</code>况或者<code>a 标签发送 get 请求</code>的情况下可以携带 Cookie，其他情况均不能。</p>
<p><strong>c.</strong> 在<code>None</code>模式下，也就是默认模式，请求会自动携带上 Cookie。</p>
<h3 class="heading">Cookie 的缺点</h3>
<ol>
<li>
<p>容量缺陷。Cookie 的体积上限只有<code>4KB</code>，只能用来存储少量的信息。</p>
</li>
<li>
<p>性能缺陷。Cookie 紧跟域名，不管域名下面的某一个地址需不需要这个 Cookie ，请求都会携带上完整的 Cookie，这样随着请求数的增多，其实会造成巨大的性能浪费的，因为请求携带了很多不必要的内容。但可以通过<code>Domain</code>和<code>Path</code>指定<strong>作用域</strong>来解决。</p>
</li>
<li>
<p>安全缺陷。由于 Cookie 以纯文本的形式在浏览器和服务器中传递，很容易被非法用户截获，然后进行一系列的篡改，在 Cookie 的有效期内重新发送给服务器，这是相当危险的。另外，在<code>HttpOnly</code>为 false 的情况下，Cookie 信息能直接通过 JS 脚本来读取。</p>
</li>
</ol>
<h2 class="heading">012: 如何理解 HTTP 代理？</h2>
<p>我们知道在 HTTP 是基于<code>请求-响应</code>模型的协议，一般由客户端发请求，服务器来进行响应。</p>
<p>当然，也有特殊情况，就是代理服务器的情况。引入代理之后，作为代理的服务器相当于一个中间人的角色，对于客户端而言，表现为服务器进行响应；而对于源服务器，表现为客户端发起请求，具有<strong>双重身份</strong>。</p>
<p>那代理服务器到底是用来做什么的呢？</p>
<h3 class="heading">功能</h3>
<ol>
<li>
<p><strong>负载均衡</strong>。客户端的请求只会先到达代理服务器，后面到底有多少源服务器，IP 都是多少，客户端是不知道的。因此，这个代理服务器可以拿到这个请求之后，可以通过特定的算法分发给不同的源服务器，让各台源服务器的负载尽量平均。当然，这样的算法有很多，包括<strong>随机算法</strong>、<strong>轮询</strong>、<strong>一致性hash</strong>、<strong>LRU</strong><code>(最近最少使用)</code>等等，不过这些算法并不是本文的重点，大家有兴趣自己可以研究一下。</p>
</li>
<li>
<p><strong>保障安全</strong>。利用<strong>心跳</strong>机制监控后台的服务器，一旦发现故障机就将其踢出集群。并且对于上下行的数据进行过滤，对非法 IP 限流，这些都是代理服务器的工作。</p>
</li>
<li>
<p><strong>缓存代理</strong>。将内容缓存到代理服务器，使得客户端可以直接从代理服务器获得而不用到源服务器那里。下一节详细拆解。</p>
</li>
</ol>
<h3 class="heading">相关头部字段</h3>
<h4 class="heading">Via</h4>
<p>代理服务器需要标明自己的身份，在 HTTP 传输中留下自己的痕迹，怎么办呢？</p>
<p>通过<code>Via</code>字段来记录。举个例子，现在中间有两台代理服务器，在客户端发送请求后会经历这样一个过程:</p>
<pre><code class="hljs bash" lang="bash">客户端 -&gt; 代理1 -&gt; 代理2 -&gt; 源服务器
</code></pre><p>在源服务器收到请求后，会在<code>请求头</code>拿到这个字段:</p>
<pre><code class="hljs bash" lang="bash">Via: proxy_server1, proxy_server2
</code></pre><p>而源服务器响应时，最终在客户端会拿到这样的<code>响应头</code>:</p>
<pre><code class="hljs bash" lang="bash">Via: proxy_server2, proxy_server1
</code></pre><p>可以看到，<code>Via</code>中代理的顺序即为在 HTTP 传输中报文传达的顺序。</p>
<h4 class="heading">X-Forwarded-For</h4>
<p>字面意思就是<code>为谁转发</code>, 它记录的是<strong>请求方</strong>的<code>IP</code>地址(注意，和<code>Via</code>区分开，<code>X-Forwarded-For</code>记录的是请求方这一个IP)。</p>
<h4 class="heading">X-Real-IP</h4>
<p>是一种获取用户真实 IP 的字段，不管中间经过多少代理，这个字段始终记录最初的客户端的IP。</p>
<p>相应的，还有<code>X-Forwarded-Host</code>和<code>X-Forwarded-Proto</code>，分别记录<strong>客户端</strong>(注意哦，不包括代理)的<code>域名</code>和<code>协议名</code>。</p>
<h3 class="heading">X-Forwarded-For产生的问题</h3>
<p>前面可以看到，<code>X-Forwarded-For</code>这个字段记录的是请求方的 IP，这意味着每经过一个不同的代理，这个字段的名字都要变，从<code>客户端</code>到<code>代理1</code>，这个字段是客户端的 IP，从<code>代理1</code>到<code>代理2</code>，这个字段就变为了代理1的 IP。</p>
<p>但是这会产生两个问题:</p>
<ol>
<li>
<p>意味着代理必须解析 HTTP 请求头，然后修改，比直接转发数据性能下降。</p>
</li>
<li>
<p>在 HTTPS 通信加密的过程中，原始报文是不允许修改的。</p>
</li>
</ol>
<p>由此产生了<code>代理协议</code>，一般使用明文版本，只需要在 HTTP 请求行上面加上这样格式的文本即可:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-comment">// PROXY + TCP4/TCP6 + 请求方地址 + 接收方地址 + 请求端口 + 接收端口</span>
PROXY TCP4 <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span> <span class="hljs-number">0.0</span><span class="hljs-number">.0</span><span class="hljs-number">.2</span> <span class="hljs-number">1111</span> <span class="hljs-number">2222</span>
GET / HTTP/<span class="hljs-number">1.1</span>
...
</code></pre><p>这样就可以解决<code>X-Forwarded-For</code>带来的问题了。</p>
<h2 class="heading">013: 如何理解 HTTP 缓存及缓存代理？</h2>
<p>关于<code>强缓存</code>和<code>协商缓存</code>的内容，我已经在<a target="_blank" href="http://47.98.159.95/my_blog/perform/001.html">能不能说一说浏览器缓存</a>做了详细分析，小结如下:</p>
<p>首先通过 <code>Cache-Control</code> 验证强缓存是否可用</p>
<ul>
<li>如果强缓存可用，直接使用</li>
<li>否则进入协商缓存，即发送 HTTP 请求，服务器通过请求头中的<code>If-Modified-Since</code>或者<code>If-None-Match</code>这些<strong>条件请求</strong>字段检查资源是否更新
<ul>
<li>若资源更新，返回资源和200状态码</li>
<li>否则，返回304，告诉浏览器直接从缓存获取资源</li>
</ul>
</li>
</ul>
<p>这一节我们主要来说说另外一种缓存方式: <strong>代理缓存</strong>。</p>
<h3 class="heading">为什么产生代理缓存？</h3>
<p>对于源服务器来说，它也是有缓存的，比如<strong>Redis, Memcache</strong>，但对于 HTTP 缓存来说，如果每次客户端缓存失效都要到源服务器获取，那给源服务器的压力是很大的。</p>
<p>由此引入了<strong>缓存代理</strong>的机制。让<code>代理服务器</code>接管一部分的服务端HTTP缓存，客户端缓存过期后<strong>就近</strong>到代理缓存中获取，代理缓存过期了才请求源服务器，这样流量巨大的时候能明显降低源服务器的压力。</p>
<p>那缓存代理究竟是如何做到的呢？</p>
<p>总的来说，缓存代理的控制分为两部分，一部分是<strong>源服务器</strong>端的控制，一部分是<strong>客户端</strong>的控制。</p>
<h3 class="heading">源服务器的缓存控制</h3>
<h4 class="heading">private 和 public</h4>
<p>在源服务器的响应头中，会加上<code>Cache-Control</code>这个字段进行缓存控制字段，那么它的值当中可以加入<code>private</code>或者<code>public</code>表示是否允许代理服务器缓存，前者禁止，后者为允许。</p>
<p>比如对于一些非常私密的数据，如果缓存到代理服务器，别人直接访问代理就可以拿到这些数据，是非常危险的，因此对于这些数据一般是不会允许代理服务器进行缓存的，将响应头部的<code>Cache-Control</code>设为<code>private</code>，而不是<code>public</code>。</p>
<h4 class="heading">proxy-revalidate</h4>
<p><code>must-revalidate</code>的意思是<strong>客户端</strong>缓存过期就去源服务器获取，而<code>proxy-revalidate</code>则表示<strong>代理服务器</strong>的缓存过期后到源服务器获取。</p>
<h4 class="heading">s-maxage</h4>
<p><code>s</code>是<code>share</code>的意思，限定了缓存在代理服务器中可以存放多久，和限制客户端缓存时间的<code>max-age</code>并不冲突。</p>
<p>讲了这几个字段，我们不妨来举个小例子，源服务器在响应头中加入这样一个字段:</p>
<pre><code class="hljs bash" lang="bash">Cache-Control: public, max-age=1000, s-maxage=2000
</code></pre><p>相当于源服务器说: 我这个响应是允许代理服务器缓存的，客户端缓存过期了到代理中拿，并且在客户端的缓存时间为 1000 秒，在代理服务器中的缓存时间为 2000 s。</p>
<h3 class="heading">客户端的缓存控制</h3>
<h4 class="heading">max-stale 和 min-fresh</h4>
<p>在客户端的请求头中，可以加入这两个字段，来对代理服务器上的缓存进行<strong>宽容</strong>和<strong>限制</strong>操作。比如：</p>
<pre><code class="hljs bash" lang="bash">max-stale: 5
</code></pre><p>表示客户端到代理服务器上拿缓存的时候，即使代理缓存过期了也不要紧，只要过期时间在<strong>5秒之内</strong>，还是可以从代理中获取的。</p>
<p>又比如:</p>
<pre><code class="hljs bash" lang="bash">min-fresh: 5
</code></pre><p>表示代理缓存需要一定的新鲜度，不要等到缓存刚好到期再拿，一定要在<strong>到期前 5 秒</strong>之前的时间拿，否则拿不到。</p>
<h4 class="heading">only-if-cached</h4>
<p>这个字段加上后表示客户端只会接受代理缓存，而不会接受源服务器的响应。如果代理缓存无效，则直接返回<code>504（Gateway Timeout）</code>。</p>
<p>以上便是缓存代理的内容，涉及的字段比较多，希望能好好回顾一下，加深理解。</p>
<h2 class="heading">014: 什么是跨域？浏览器如何拦截响应？如何解决？</h2>
<p>在前后端分离的开发模式中，经常会遇到跨域问题，即 Ajax 请求发出去了，服务器也成功响应了，前端就是拿不到这个响应。接下来我们就来好好讨论一下这个问题。</p>
<h3 class="heading">什么是跨域</h3>
<p>回顾一下 URI 的组成:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd7ac23846fe~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>浏览器遵循<strong>同源政策</strong>(<code>scheme(协议)</code>、<code>host(主机)</code>和<code>port(端口)</code>都相同则为<code>同源</code>)。非同源站点有这样一些限制:</p>
<ul>
<li>不能读取和修改对方的 DOM</li>
<li>不读访问对方的 Cookie、IndexDB 和 LocalStorage</li>
<li>限制 XMLHttpRequest 请求。(后面的话题着重围绕这个)</li>
</ul>
<p>当浏览器向目标 URI 发 Ajax 请求时，只要当前 URL 和目标 URL 不同源，则产生跨域，被称为<code>跨域请求</code>。</p>
<p>跨域请求的响应一般会被浏览器所拦截，注意，是被浏览器拦截，响应其实是成功到达客户端了。那这个拦截是如何发生呢？</p>
<p>首先要知道的是，浏览器是多进程的，以 Chrome 为例，进程组成如下：</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd8131a4628f~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p><img style="margin-left: 150px;" src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd83a20647db~tplv-t2oaga2asx-image.image"></p>
<p><strong>WebKit 渲染引擎</strong>和<strong>V8 引擎</strong>都在渲染进程当中。</p>
<p>当<code>xhr.send</code>被调用，即 Ajax 请求准备发送的时候，其实还只是在渲染进程的处理。为了防止黑客通过脚本触碰到系统资源，浏览器将每一个渲染进程装进了沙箱，并且为了防止 CPU 芯片一直存在的<strong>Spectre</strong> 和 <strong>Meltdown</strong>漏洞，采取了<code>站点隔离</code>的手段，给每一个不同的站点(一级域名不同)分配了沙箱，互不干扰。具体见<a target="_blank" href="https://www.youtube.com/watch?v=dBuykrdhK-A&amp;feature=emb_logo">YouTube上Chromium安全团队的演讲视频</a>。</p>
<p>在沙箱当中的渲染进程是没有办法发送网络请求的，那怎么办？只能通过网络进程来发送。那这样就涉及到进程间通信(IPC，Inter Process Communication)了。接下来我们看看 chromium 当中进程间通信是如何完成的，在 chromium 源码中调用顺序如下:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd924eaecb41~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>可能看了你会比较懵，如果想深入了解可以去看看 chromium 最新的源代码，<a target="_blank" href="https://chromium.googlesource.com/chromium/src/+/refs/heads/master/ipc/">IPC源码地址</a>及<a target="_blank" href="https://blog.csdn.net/Luoshengyang/article/details/47822689">Chromium IPC源码解析文章</a>。</p>
<p>总的来说就是利用<code>Unix Domain Socket</code>套接字，配合事件驱动的高性能网络并发库<code>libevent</code>完成进程的 IPC 过程。</p>
<p>好，现在数据传递给了浏览器主进程，主进程接收到后，才真正地发出相应的网络请求。</p>
<p>在服务端处理完数据后，将响应返回，主进程检查到跨域，且没有cors(后面会详细说)响应头，将响应体全部丢掉，并不会发送给渲染进程。这就达到了拦截数据的目的。</p>
<p>接下来我们来说一说解决跨域问题的几种方案。</p>
<h3 class="heading">CORS</h3>
<p>CORS 其实是 W3C 的一个标准，全称是<code>跨域资源共享</code>。它需要浏览器和服务器的共同支持，具体来说，非 IE 和 IE10 以上支持CORS，服务器需要附加特定的响应头，后面具体拆解。不过在弄清楚 CORS 的原理之前，我们需要清楚两个概念: <strong>简单请求</strong>和<strong>非简单请求</strong>。</p>
<p>浏览器根据请求方法和请求头的特定字段，将请求做了一下分类，具体来说规则是这样，凡是满足下面条件的属于<strong>简单请求</strong>:</p>
<ul>
<li>请求方法为 GET、POST 或者 HEAD</li>
<li>请求头的取值范围: Accept、Accept-Language、Content-Language、Content-Type(只限于三个值<code>application/x-www-form-urlencoded</code>、<code>multipart/form-data</code>、<code>text/plain</code>)</li>
</ul>
<p>浏览器画了这样一个圈，在这个圈里面的就是<strong>简单请求</strong>, 圈外面的就是<strong>非简单请求</strong>，然后针对这两种不同的请求进行不同的处理。</p>
<h4 class="heading">简单请求</h4>
<p>请求发出去之前，浏览器做了什么？</p>
<p>它会自动在请求头当中，添加一个<code>Origin</code>字段，用来说明请求来自哪个<code>源</code>。服务器拿到请求之后，在回应时对应地添加<code>Access-Control-Allow-Origin</code>字段，如果<code>Origin</code>不在这个字段的范围中，那么浏览器就会将响应拦截。</p>
<p>因此，<code>Access-Control-Allow-Origin</code>字段是服务器用来决定浏览器是否拦截这个响应，这是必需的字段。与此同时，其它一些可选的功能性的字段，用来描述如果不会拦截，这些字段将会发挥各自的作用。</p>
<p><strong>Access-Control-Allow-Credentials</strong>。这个字段是一个布尔值，表示是否允许发送 Cookie，对于跨域请求，浏览器对这个字段默认值设为 false，而如果需要拿到浏览器的 Cookie，需要添加这个响应头并设为<code>true</code>, 并且在前端也需要设置<code>withCredentials</code>属性:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.withCredentials = <span class="hljs-literal">true</span>;
</code></pre><p><strong>Access-Control-Expose-Headers</strong>。这个字段是给 XMLHttpRequest 对象赋能，让它不仅可以拿到基本的 6 个响应头字段（包括<code>Cache-Control</code>、<code>Content-Language</code>、<code>Content-Type</code>、<code>Expires</code>、<code>Last-Modified</code>和<code>Pragma</code>）, 还能拿到这个字段声明的<strong>响应头字段</strong>。比如这样设置:</p>
<pre><code class="hljs bash" lang="bash">Access-Control-Expose-Headers: aaa
</code></pre><p>那么在前端可以通过 <code>XMLHttpRequest.getResponseHeader('aaa')</code> 拿到 <code>aaa</code> 这个字段的值。</p>
<h4 class="heading">非简单请求</h4>
<p>非简单请求相对而言会有些不同，体现在两个方面: <strong>预检请求</strong>和<strong>响应字段</strong>。</p>
<p>我们以 PUT 方法为例。</p>
<pre><code class="hljs js" lang="js"><span class="hljs-keyword">var</span> url = <span class="hljs-string">'http://xxx.com'</span>;
<span class="hljs-keyword">var</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.open(<span class="hljs-string">'PUT'</span>, url, <span class="hljs-literal">true</span>);
xhr.setRequestHeader(<span class="hljs-string">'X-Custom-Header'</span>, <span class="hljs-string">'xxx'</span>);
xhr.send();
</code></pre><p>当这段代码执行后，首先会发送<strong>预检请求</strong>。这个预检请求的请求行和请求体是下面这个格式:</p>
<pre><code class="hljs bash" lang="bash">OPTIONS / HTTP/1.1
Origin: 当前地址
Host: xxx.com
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: X-Custom-Header
</code></pre><p>预检请求的方法是<code>OPTIONS</code>，同时会加上<code>Origin</code>源地址和<code>Host</code>目标地址，这很简单。同时也会加上两个关键的字段:</p>
<ul>
<li>Access-Control-Request-Method, 列出 CORS 请求用到哪个HTTP方法</li>
<li>Access-Control-Request-Headers，指定 CORS 请求将要加上什么请求头</li>
</ul>
<p>这是<code>预检请求</code>。接下来是<strong>响应字段</strong>，响应字段也分为两部分，一部分是对于<strong>预检请求</strong>的响应，一部分是对于 <strong>CORS 请求</strong>的响应。</p>
<p><strong>预检请求的响应</strong>。如下面的格式:</p>
<pre><code class="hljs bash" lang="bash">HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT
Access-Control-Allow-Headers: X-Custom-Header
Access-Control-Allow-Credentials: <span class="hljs-literal">true</span>
Access-Control-Max-Age: 1728000
Content-Type: text/html; charset=utf-8
Content-Encoding: gzip
Content-Length: 0
</code></pre><p>其中有这样几个关键的<strong>响应头字段</strong>:</p>
<ul>
<li>Access-Control-Allow-Origin: 表示可以允许请求的源，可以填具体的源名，也可以填<code>*</code>表示允许任意源请求。</li>
<li>Access-Control-Allow-Methods: 表示允许的请求方法列表。</li>
<li>Access-Control-Allow-Credentials: 简单请求中已经介绍。</li>
<li>Access-Control-Allow-Headers: 表示允许发送的请求头字段</li>
<li>Access-Control-Max-Age: 预检请求的有效期，在此期间，不用发出另外一条预检请求。</li>
</ul>
<p>在预检请求的响应返回后，如果请求不满足响应头的条件，则触发<code>XMLHttpRequest</code>的<code>onerror</code>方法，当然后面真正的<strong>CORS请求</strong>也不会发出去了。</p>
<p><strong>CORS 请求的响应</strong>。绕了这么一大转，到了真正的 CORS 请求就容易多了，现在它和<strong>简单请求</strong>的情况是一样的。浏览器自动加上<code>Origin</code>字段，服务端响应头返回<strong>Access-Control-Allow-Origin</strong>。可以参考以上简单请求部分的内容。</p>
<h3 class="heading">JSONP</h3>
<p>虽然<code>XMLHttpRequest</code>对象遵循同源政策，但是<code>script</code>标签不一样，它可以通过 src 填上目标地址从而发出 GET 请求，实现跨域请求并拿到响应。这也就是 JSONP 的原理，接下来我们就来封装一个 JSONP:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-keyword">const</span> jsonp = <span class="hljs-function">(<span class="hljs-params">{ url, params, callbackName }</span>) =&gt;</span> {
  <span class="hljs-keyword">const</span> generateURL = <span class="hljs-function"><span class="hljs-params">()</span> =&gt;</span> {
    <span class="hljs-keyword">let</span> dataStr = <span class="hljs-string">''</span>;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> params) {
      dataStr += <span class="hljs-string">`<span class="hljs-subst">${key}</span>=<span class="hljs-subst">${params[key]}</span>&amp;`</span>;
    }
    dataStr += <span class="hljs-string">`callback=<span class="hljs-subst">${callbackName}</span>`</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">${url}</span>?<span class="hljs-subst">${dataStr}</span>`</span>;
  };
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =&gt;</span> {
    <span class="hljs-comment">// 初始化回调函数名称</span>
    callbackName = callbackName || <span class="hljs-built_in">Math</span>.random().toString.replace(<span class="hljs-string">','</span>, <span class="hljs-string">''</span>); 
    <span class="hljs-comment">// 创建 script 元素并加入到当前文档中</span>
    <span class="hljs-keyword">let</span> scriptEle = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
    scriptEle.src = generateURL();
    <span class="hljs-built_in">document</span>.body.appendChild(scriptEle);
    <span class="hljs-comment">// 绑定到 window 上，为了后面调用</span>
    <span class="hljs-built_in">window</span>[callbackName] = <span class="hljs-function">(<span class="hljs-params">data</span>) =&gt;</span> {
      resolve(data);
      <span class="hljs-comment">// script 执行完了，成为无用元素，需要清除</span>
      <span class="hljs-built_in">document</span>.body.removeChild(scriptEle);
    }
  });
}
</code></pre><p>当然在服务端也会有响应的操作, 以 express 为例:</p>
<pre><code class="hljs js" lang="js"><span class="hljs-keyword">let</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">let</span> app = express()
app.get(<span class="hljs-string">'/'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req, res</span>) </span>{
  <span class="hljs-keyword">let</span> { a, b, callback } = req.query
  <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 1</span>
  <span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">// 2</span>
  <span class="hljs-comment">// 注意哦，返回给script标签，浏览器直接把这部分字符串执行</span>
  res.end(<span class="hljs-string">`<span class="hljs-subst">${callback}</span>('数据包')`</span>);
})
app.listen(<span class="hljs-number">3000</span>)
</code></pre><p>前端这样简单地调用一下就好了:</p>
<pre><code class="hljs js" lang="js">jsonp({
  <span class="hljs-attr">url</span>: <span class="hljs-string">'http://localhost:3000'</span>,
  <span class="hljs-attr">params</span>: { 
    <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>
  }
}).then(<span class="hljs-function"><span class="hljs-params">data</span> =&gt;</span> {
  <span class="hljs-comment">// 拿到数据进行处理</span>
  <span class="hljs-built_in">console</span>.log(data); <span class="hljs-comment">// 数据包</span>
})
</code></pre><p>和<code>CORS</code>相比，JSONP 最大的优势在于兼容性好，IE 低版本不能使用 CORS 但可以使用 JSONP，缺点也很明显，请求方法单一，只支持 GET 请求。</p>
<h3 class="heading">Nginx</h3>
<p>Nginx 是一种高性能的<code>反向代理</code>服务器，可以用来轻松解决跨域问题。</p>
<p>what？反向代理？我给你看一张图你就懂了。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd97d0b1cf15~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>正向代理帮助客户端<strong>访问</strong>客户端自己访问不到的服务器，然后将结果返回给客户端。</p>
<p>反向代理拿到客户端的请求，将请求转发给其他的服务器，主要的场景是维持服务器集群的<strong>负载均衡</strong>，换句话说，反向代理帮<strong>其它的服务器</strong>拿到请求，然后选择一个合适的服务器，将请求转交给它。</p>
<p>因此，两者的区别就很明显了，正向代理服务器是帮<strong>客户端</strong>做事情，而反向代理服务器是帮其它的<strong>服务器</strong>做事情。</p>
<p>好了，那 Nginx 是如何来解决跨域的呢？</p>
<p>比如说现在客户端的域名为<strong>client.com</strong>，服务器的域名为<strong>server.com</strong>，客户端向服务器发送 Ajax 请求，当然会跨域了，那这个时候让 Nginx 登场了，通过下面这个配置:</p>
<pre><code class="hljs bash" lang="bash">server {
  listen  80;
  server_name  client.com;
  location /api {
    proxy_pass server.com;
  }
}
</code></pre><p>Nginx 相当于起了一个跳板机，这个跳板机的域名也是<code>client.com</code>，让客户端首先访问 <code>client.com/api</code>，这当然没有跨域，然后 Nginx 服务器作为反向代理，将请求转发给<code>server.com</code>，当响应返回时又将响应给到客户端，这就完成整个跨域请求的过程。</p>
<p>其实还有一些不太常用的方式，大家了解即可，比如<code>postMessage</code>，当然<code>WebSocket</code>也是一种方式，但是已经不属于 HTTP 的范畴，另外一些奇技淫巧就不建议大家去死记硬背了，一方面从来不用，名字都难得记住，另一方面临时背下来，面试官也不会对你印象加分，因为看得出来是背的。当然没有背并不代表减分，把跨域原理和前面三种主要的跨域方式理解清楚，经得起更深一步的推敲，反而会让别人觉得你是一个靠谱的人。</p>
<h2 class="heading">015: TLS1.2 握手的过程是怎样的？</h2>
<p>之前谈到了 HTTP 是明文传输的协议，传输保文对外完全透明，非常不安全，那如何进一步保证安全性呢？</p>
<p>由此产生了 <code>HTTPS</code>，其实它并不是一个新的协议，而是在 HTTP 下面增加了一层 SSL/TLS 协议，简单的讲，<strong>HTTPS = HTTP + SSL/TLS</strong>。</p>
<p>那什么是 SSL/TLS 呢？</p>
<p>SSL 即安全套接层（Secure Sockets Layer），在 OSI 七层模型中处于会话层(第 5 层)。之前 SSL 出过三个大版本，当它发展到第三个大版本的时候才被标准化，成为 TLS（传输层安全，Transport Layer Security），并被当做 TLS1.0 的版本，准确地说，<strong>TLS1.0 = SSL3.1</strong>。</p>
<p>现在主流的版本是 TLS/1.2, 之前的 TLS1.0、TLS1.1 都被认为是不安全的，在不久的将来会被完全淘汰。因此我们接下来主要讨论的是 TLS1.2, 当然在 2018 年推出了更加优秀的 TLS1.3，大大优化了 TLS 握手过程，这个我们放在下一节再去说。</p>
<p>TLS 握手的过程比较复杂，写文章之前我查阅了大量的资料，发现对 TLS 初学者非常不友好，也有很多知识点说的含糊不清，可以说这个整理的过程是相当痛苦了。希望我下面的拆解能够帮你理解得更顺畅些吧 : ）</p>
<h3 class="heading">传统 RSA 握手</h3>
<p>先来说说传统的 TLS 握手，也是大家在网上经常看到的。我之前也写过这样的文章，<a target="_blank" href="http://47.98.159.95/my_blog/browser-security/003.html">(传统RSA版本)HTTPS为什么让数据传输更安全</a>，其中也介绍到了<code>对称加密</code>和<code>非对称加密</code>的概念，建议大家去读一读，不再赘述。之所以称它为 RSA 版本，是因为它在加解密<code>pre_random</code>的时候采用的是 RSA 算法。</p>
<h3 class="heading">TLS 1.2 握手过程</h3>
<p>现在我们来讲讲主流的 TLS 1.2 版本所采用的方式。</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffd9b35c7a81b~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>刚开始你可能会比较懵，先别着急，过一遍下面的流程再来看会豁然开朗。</p>
<h4 class="heading">step 1: Client Hello</h4>
<p>首先，浏览器发送 client_random、TLS版本、加密套件列表。</p>
<p>client_random 是什么？用来最终 secret 的一个参数。</p>
<p>加密套件列表是什么？我举个例子，加密套件列表一般张这样:</p>
<pre><code class="hljs bash" lang="bash">TLS_ECDHE_WITH_AES_128_GCM_SHA256
</code></pre><p>意思是<code>TLS</code>握手过程中，使用<code>ECDHE</code>算法生成<code>pre_random</code>(这个数后面会介绍)，128位的<code>AES</code>算法进行对称加密，在对称加密的过程中使用主流的<code>GCM</code>分组模式，因为对称加密中很重要的一个问题就是如何分组。最后一个是哈希摘要算法，采用<code>SHA256</code>算法。</p>
<p>其中值得解释一下的是这个哈希摘要算法，试想一个这样的场景，服务端现在给客户端发消息来了，客户端并不知道此时的消息到底是服务端发的，还是中间人伪造的消息呢？现在引入这个哈希摘要算法，将服务端的证书信息通过<strong>这个算法</strong>生成一个摘要(可以理解为<code>比较短的字符串</code>)，用来<strong>标识</strong>这个服务端的身份，用私钥加密后把<strong>加密后的标识</strong>和<strong>自己的公钥</strong>传给客户端。客户端拿到<strong>这个公钥</strong>来解密，生成另外一份摘要。两个摘要进行对比，如果相同则能确认服务端的身份。这也就是所谓<strong>数字签名</strong>的原理。其中除了哈希算法，最重要的过程是<strong>私钥加密，公钥解密</strong>。</p>
<h4 class="heading">step 2: Server Hello</h4>
<p>可以看到服务器一口气给客户端回复了非常多的内容。</p>
<p><code>server_random</code>也是最后生成<code>secret</code>的一个参数, 同时确认 TLS 版本、需要使用的加密套件和自己的证书，这都不难理解。那剩下的<code>server_params</code>是干嘛的呢？</p>
<p>我们先埋个伏笔，现在你只需要知道，<code>server_random</code>到达了客户端。</p>
<h4 class="heading">step 3: Client 验证证书，生成secret</h4>
<p>客户端验证服务端传来的<code>证书</code>和<code>签名</code>是否通过，如果验证通过，则传递<code>client_params</code>这个参数给服务器。</p>
<p>接着客户端通过<code>ECDHE</code>算法计算出<code>pre_random</code>，其中传入两个参数:<strong>server_params</strong>和<strong>client_params</strong>。现在你应该清楚这个两个参数的作用了吧，由于<code>ECDHE</code>基于<code>椭圆曲线离散对数</code>，这两个参数也称作<code>椭圆曲线的公钥</code>。</p>
<p>客户端现在拥有了<code>client_random</code>、<code>server_random</code>和<code>pre_random</code>，接下来将这三个数通过一个伪随机数函数来计算出最终的<code>secret</code>。</p>
<h4 class="heading">step4: Server 生成 secret</h4>
<p>刚刚客户端不是传了<code>client_params</code>过来了吗？</p>
<p>现在服务端开始用<code>ECDHE</code>算法生成<code>pre_random</code>，接着用和客户端同样的伪随机数函数生成最后的<code>secret</code>。</p>
<h4 class="heading">注意事项</h4>
<p>TLS的过程基本上讲完了，但还有两点需要注意。</p>
<p><strong>第一</strong>、实际上 TLS 握手是一个<strong>双向认证</strong>的过程，从 step1 中可以看到，客户端有能力验证服务器的身份，那服务器能不能验证客户端的身份呢？</p>
<p>当然是可以的。具体来说，在 <code>step3</code>中，客户端传送<code>client_params</code>，实际上给服务器传一个验证消息，让服务器将相同的验证流程(哈希摘要 + 私钥加密 + 公钥解密)走一遍，确认客户端的身份。</p>
<p><strong>第二</strong>、当客户端生成<code>secret</code>后，会给服务端发送一个收尾的消息，告诉服务器之后的都用对称加密，对称加密的算法就用第一次约定的。服务器生成完<code>secret</code>也会向客户端发送一个收尾的消息，告诉客户端以后就直接用对称加密来通信。</p>
<p>这个收尾的消息包括两部分，一部分是<code>Change Cipher Spec</code>，意味着后面加密传输了，另一个是<code>Finished</code>消息，这个消息是对之前所有发送的数据做的<strong>摘要</strong>，对摘要进行加密，让对方验证一下。</p>
<p>当双方都验证通过之后，握手才正式结束。后面的 HTTP 正式开始传输加密报文。</p>
<h4 class="heading">RSA 和 ECDHE 握手过程的区别</h4>
<ol>
<li>
<p>ECDHE 握手，也就是主流的 TLS1.2 握手中，使用<code>ECDHE</code>实现<code>pre_random</code>的加密解密，没有用到 RSA。</p>
</li>
<li>
<p>使用 ECDHE 还有一个特点，就是客户端发送完收尾消息后可以提前<code>抢跑</code>，直接发送 HTTP 报文，节省了一个 RTT，不必等到收尾消息到达服务器，然后等服务器返回收尾消息给自己，直接开始发请求。这也叫<code>TLS False Start</code>。</p>
</li>
</ol>
<h2 class="heading">016: TLS 1.3 做了哪些改进？</h2>
<p>TLS 1.2 虽然存在了 10 多年，经历了无数的考验，但历史的车轮总是不断向前的，为了获得更强的安全、更优秀的性能，在<code>2018年</code>就推出了 TLS1.3，对于<code>TLS1.2</code>做了一系列的改进，主要分为这几个部分:<strong>强化安全</strong>、<strong>提高性能</strong>。</p>
<h3 class="heading">强化安全</h3>
<p>在 TLS1.3 中废除了非常多的加密算法，最后只保留五个加密套件:</p>
<ul>
<li>TLS_AES_128_GCM_SHA256</li>
<li>TLS_AES_256_GCM_SHA384</li>
<li>TLS_CHACHA20_POLY1305_SHA256</li>
<li>TLS_AES_128_GCM_SHA256</li>
<li>TLS_AES_128_GCM_8_SHA256</li>
</ul>
<p>可以看到，最后剩下的对称加密算法只有 <strong>AES</strong> 和 <strong>CHACHA20</strong>，之前主流的也会这两种。分组模式也只剩下 <strong>GCM</strong> 和 <strong>POLY1305</strong>, 哈希摘要算法只剩下了 <strong>SHA256</strong> 和 <strong>SHA384</strong> 了。</p>
<p>那你可能会问了, 之前<code>RSA</code>这么重要的非对称加密算法怎么不在了？</p>
<p>我觉得有两方面的原因:</p>
<p><strong>第一</strong>、2015年发现了<code>FREAK</code>攻击，即已经有人发现了 RSA 的漏洞，能够进行破解了。</p>
<p><strong>第二</strong>、一旦私钥泄露，那么中间人可以通过私钥计算出之前所有报文的<code>secret</code>，破解之前所有的密文。</p>
<p>为什么？回到 RSA 握手的过程中，客户端拿到服务器的证书后，提取出服务器的公钥，然后生成<code>pre_random</code>并用<strong>公钥</strong>加密传给服务器，服务器通过<strong>私钥</strong>解密，从而拿到真实的<code>pre_random</code>。当中间人拿到了服务器私钥，并且截获之前所有报文的时候，那么就能拿到<code>pre_random</code>、<code>server_random</code>和<code>client_random</code>并根据对应的随机数函数生成<code>secret</code>，也就是拿到了 TLS 最终的会话密钥，每一个历史报文都能通过这样的方式进行破解。</p>
<p>但<code>ECDHE</code>在每次握手时都会生成临时的密钥对，即使私钥被破解，之前的历史消息并不会收到影响。这种一次破解并不影响历史信息的性质也叫<strong>前向安全性</strong>。</p>
<p><code>RSA</code> 算法不具备前向安全性，而 <code>ECDHE</code> 具备，因此在 TLS1.3 中彻底取代了<code>RSA</code>。</p>
<h3 class="heading">提升性能</h3>
<h4 class="heading">握手改进</h4>
<p>流程如下:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffda75857d404~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>大体的方式和 TLS1.2 差不多，不过和 TLS 1.2 相比少了一个 RTT， 服务端不必等待对方验证证书之后才拿到<code>client_params</code>，而是直接在第一次握手的时候就能够拿到, 拿到之后立即计算<code>secret</code>，节省了之前不必要的等待时间。同时，这也意味着在第一次握手的时候客户端需要传送更多的信息，一口气给传完。</p>
<p>这种 TLS 1.3 握手方式也被叫做<strong>1-RTT握手</strong>。但其实这种<code>1-RTT</code>的握手方式还是有一些优化的空间的，接下来我们来一一介绍这些优化方式。</p>
<h4 class="heading">会话复用</h4>
<p>会话复用有两种方式: <strong>Session ID</strong>和<strong>Session Ticket</strong>。</p>
<p>先说说最早出现的<strong>Seesion ID</strong>，具体做法是客户端和服务器首次连接后各自保存会话的 ID，并存储会话密钥，当再次连接时，客户端发送<code>ID</code>过来，服务器查找这个 ID 是否存在，如果找到了就直接复用之前的会话状态，会话密钥不用重新生成，直接用原来的那份。</p>
<p>但这种方式也存在一个弊端，就是当客户端数量庞大的时候，对服务端的存储压力非常大。</p>
<p>因而出现了第二种方式——<strong>Session Ticket</strong>。它的思路就是: 服务端的压力大，那就把压力分摊给客户端呗。具体来说，双方连接成功后，服务器加密会话信息，用<strong>Session Ticket</strong>消息发给客户端，让客户端保存下来。下次重连的时候，就把这个 Ticket 进行解密，验证它过没过期，如果没过期那就直接恢复之前的会话状态。</p>
<p>这种方式虽然减小了服务端的存储压力，但与带来了安全问题，即每次用一个固定的密钥来解密 Ticket 数据，一旦黑客拿到这个密钥，之前所有的历史记录也被破解了。因此为了尽量避免这样的问题，密钥需要定期进行更换。</p>
<p>总的来说，这些会话复用的技术在保证<code>1-RTT</code>的同时，也节省了生成会话密钥这些算法所消耗的时间，是一笔可观的性能提升。</p>
<h4 class="heading">PSK</h4>
<p>刚刚说的都是<code>1-RTT</code>情况下的优化，那能不能优化到<code>0-RTT</code>呢？</p>
<p>答案是可以的。做法其实也很简单，在发送<strong>Session Ticket</strong>的同时带上应用数据，不用等到服务端确认，这种方式被称为<code>Pre-Shared Key</code>，即 PSK。</p>
<p>这种方式虽然方便，但也带来了安全问题。中间人截获<code>PSK</code>的数据，不断向服务器重复发，类似于 TCP 第一次握手携带数据，增加了服务器被攻击的风险。</p>
<h3 class="heading">总结</h3>
<p>TLS1.3 在 TLS1.2 的基础上废除了大量的算法，提升了安全性。同时利用会话复用节省了重新生成密钥的时间，利用 PSK 做到了<code>0-RTT</code>连接。</p>
<h2 class="heading">017: HTTP/2 有哪些改进？</h2>
<p>由于 HTTPS 在安全方面已经做的非常好了，HTTP 改进的关注点放在了性能方面。对于 HTTP/2 而言，它对于性能的提升主要在于两点:</p>
<ul>
<li>头部压缩</li>
<li>多路复用</li>
</ul>
<p>当然还有一些颠覆性的功能实现:</p>
<ul>
<li>设置请求优先级</li>
<li>服务器推送</li>
</ul>
<p>这些重大的提升本质上也是为了解决 HTTP 本身的问题而产生的。接下来我们来看看 HTTP/2 解决了哪些问题，以及解决方式具体是如何的。</p>
<h3 class="heading">头部压缩</h3>
<p>在 HTTP/1.1 及之前的时代，<strong>请求体</strong>一般会有响应的压缩编码过程，通过<code>Content-Encoding</code>头部字段来指定，但你有没有想过头部字段本身的压缩呢？当请求字段非常复杂的时候，尤其对于 GET 请求，请求报文几乎全是请求头，这个时候还是存在非常大的优化空间的。HTTP/2 针对头部字段，也采用了对应的压缩算法——HPACK，对请求头进行压缩。</p>
<p>HPACK 算法是专门为 HTTP/2 服务的，它主要的亮点有两个：</p>
<ul>
<li>首先是在服务器和客户端之间建立哈希表，将用到的字段存放在这张表中，那么在传输的时候对于之前出现过的值，只需要把<strong>索引</strong>(比如0，1，2，...)传给对方即可，对方拿到索引查表就行了。这种<strong>传索引</strong>的方式，可以说让请求头字段得到极大程度的精简和复用。</li>
</ul>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffdaa6f41c004~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<blockquote class="warning"><p>HTTP/2 当中废除了起始行的概念，将起始行中的请求方法、URI、状态码转换成了头字段，不过这些字段都有一个":"前缀，用来和其它请求头区分开。
</p></blockquote><ul>
<li>其次是对于整数和字符串进行<strong>哈夫曼编码</strong>，哈夫曼编码的原理就是先将所有出现的字符建立一张索引表，然后让出现次数多的字符对应的索引尽可能短，传输的时候也是传输这样的<strong>索引序列</strong>，可以达到非常高的压缩率。</li>
</ul>
<h3 class="heading">多路复用</h3>
<h4 class="heading">HTTP 队头阻塞</h4>
<p>我们之前讨论了 HTTP 队头阻塞的问题，其根本原因在于HTTP 基于<code>请求-响应</code>的模型，在同一个 TCP 长连接中，前面的请求没有得到响应，后面的请求就会被阻塞。</p>
<p>后面我们又讨论到用<strong>并发连接</strong>和<strong>域名分片</strong>的方式来解决这个问题，但这并没有真正从 HTTP 本身的层面解决问题，只是增加了 TCP 连接，分摊风险而已。而且这么做也有弊端，多条 TCP 连接会竞争<strong>有限的带宽</strong>，让真正优先级高的请求不能优先处理。</p>
<p>而 HTTP/2 便从 HTTP 协议本身解决了<code>队头阻塞</code>问题。注意，这里并不是指的<code>TCP队头阻塞</code>，而是<code>HTTP队头阻塞</code>，两者并不是一回事。TCP 的队头阻塞是在<code>数据包</code>层面，单位是<code>数据包</code>，前一个报文没有收到便不会将后面收到的报文上传给 HTTP，而HTTP 的队头阻塞是在 <code>HTTP 请求-响应</code>层面，前一个请求没处理完，后面的请求就要阻塞住。两者所在的层次不一样。</p>
<p>那么 HTTP/2 如何来解决所谓的队头阻塞呢？</p>
<h4 class="heading">二进制分帧</h4>
<p>首先，HTTP/2 认为明文传输对机器而言太麻烦了，不方便计算机的解析，因为对于文本而言会有多义性的字符，比如回车换行到底是内容还是分隔符，在内部需要用到状态机去识别，效率比较低。于是 HTTP/2 干脆把报文全部换成二进制格式，全部传输<code>01</code>串，方便了机器的解析。</p>
<p>原来<code>Headers + Body</code>的报文格式如今被拆分成了一个个二进制的帧，用<strong>Headers帧</strong>存放头部字段，<strong>Data帧</strong>存放请求体数据。分帧之后，服务器看到的不再是一个个完整的 HTTP 请求报文，而是一堆乱序的二进制帧。这些二进制帧不存在先后关系，因此也就不会排队等待，也就没有了 HTTP 的队头阻塞问题。</p>
<p>通信双方都可以给对方发送二进制帧，这种二进制帧的<strong>双向传输的序列</strong>，也叫做<code>流</code>(Stream)。HTTP/2 用<code>流</code>来在一个 TCP 连接上来进行多个数据帧的通信，这就是<strong>多路复用</strong>的概念。</p>
<p>可能你会有一个疑问，既然是乱序首发，那最后如何来处理这些乱序的数据帧呢？</p>
<p>首先要声明的是，所谓的乱序，指的是不同 ID 的 Stream 是乱序的，但同一个 Stream ID 的帧一定是按顺序传输的。二进制帧到达后对方会将 Stream ID 相同的二进制帧组装成完整的<strong>请求报文</strong>和<strong>响应报文</strong>。当然，在二进制帧当中还有其他的一些字段，实现了<strong>优先级</strong>和<strong>流量控制</strong>等功能，我们放到下一节再来介绍。</p>
<h3 class="heading">服务器推送</h3>
<p>另外值得一说的是 HTTP/2 的服务器推送(Server Push)。在 HTTP/2 当中，服务器已经不再是完全被动地接收请求，响应请求，它也能新建 stream 来给客户端发送消息，当 TCP 连接建立之后，比如浏览器请求一个 HTML 文件，服务器就可以在返回 HTML 的基础上，将 HTML 中引用到的其他资源文件一起返回给客户端，减少客户端的等待。</p>
<h3 class="heading">总结</h3>
<p>当然，HTTP/2 新增那么多的特性，是不是 HTTP 的语法要重新学呢？不需要，HTTP/2 完全兼容之前 HTTP 的语法和语义，如<strong>请求头、URI、状态码、头部字段</strong>都没有改变，完全不用担心。同时，在安全方面，HTTP 也支持 TLS，并且现在主流的浏览器都公开只支持加密的 HTTP/2, 因此你现在能看到的 HTTP/2 也基本上都是跑在 TLS 上面的了。最后放一张分层图给大家参考:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffdc6783132a5~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<h2 class="heading">018: HTTP/2 中的二进制帧是如何设计的？</h2>
<h3 class="heading">帧结构</h3>
<p>HTTP/2 中传输的帧结构如下图所示:</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffdc9e9c25e93~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>每个帧分为<code>帧头</code>和<code>帧体</code>。先是三个字节的帧长度，这个长度表示的是<code>帧体</code>的长度。</p>
<p>然后是帧类型，大概可以分为<strong>数据帧</strong>和<strong>控制帧</strong>两种。数据帧用来存放 HTTP 报文，控制帧用来管理<code>流</code>的传输。</p>
<p>接下来的一个字节是<strong>帧标志</strong>，里面一共有 8 个标志位，常用的有 <strong>END_HEADERS</strong>表示头数据结束，<strong>END_STREAM</strong>表示单方向数据发送结束。</p>
<p>后 4 个字节是<code>Stream ID</code>, 也就是<code>流标识符</code>，有了它，接收方就能从乱序的二进制帧中选择出 ID 相同的帧，按顺序组装成请求/响应报文。</p>
<h3 class="heading">流的状态变化</h3>
<p>从前面可以知道，在 HTTP/2 中，所谓的<code>流</code>，其实就是二进制帧的<strong>双向传输的序列</strong>。那么在 HTTP/2 请求和响应的过程中，流的状态是如何变化的呢？</p>
<p>HTTP/2 其实也是借鉴了 TCP 状态变化的思想，根据帧的标志位来实现具体的状态改变。这里我们以一个普通的<code>请求-响应</code>过程为例来说明：</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/3/22/170ffdcd0abdd1ba~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>最开始两者都是空闲状态，当客户端发送<code>Headers帧</code>后，开始分配<code>Stream ID</code>, 此时客户端的<code>流</code>打开, 服务端接收之后服务端的<code>流</code>也打开，两端的<code>流</code>都打开之后，就可以互相传递数据帧和控制帧了。</p>
<p>当客户端要关闭时，向服务端发送<code>END_STREAM</code>帧，进入<code>半关闭状态</code>, 这个时候客户端只能接收数据，而不能发送数据。</p>
<p>服务端收到这个<code>END_STREAM</code>帧后也进入<code>半关闭状态</code>，不过此时服务端的情况是只能发送数据，而不能接收数据。随后服务端也向客户端发送<code>END_STREAM</code>帧，表示数据发送完毕，双方进入<code>关闭状态</code>。</p>
<p>如果下次要开启新的<code>流</code>，流 ID 需要自增，直到上限为止，到达上限后开一个新的 TCP 连接重头开始计数。由于流 ID 字段长度为 4 个字节，最高位又被保留，因此范围是 0 ~ 2的 31 次方，大约 21 亿个。</p>
<h3 class="heading">流的特性</h3>
<p>刚刚谈到了流的状态变化过程，这里顺便就来总结一下<code>流</code>传输的特性:</p>
<ul>
<li>并发性。一个 HTTP/2 连接上可以同时发多个帧，这一点和 HTTP/1 不同。这也是实现<strong>多路</strong>复用的基础。</li>
<li>自增性。流 ID 是不可重用的，而是会按顺序递增，达到上限之后又新开 TCP 连接从头开始。</li>
<li>双向性。客户端和服务端都可以创建流，互不干扰，双方都可以作为<code>发送方</code>或者<code>接收方</code>。</li>
<li>可设置优先级。可以设置数据帧的优先级，让服务端先处理重要资源，优化用户体验。</li>
</ul>
<p>以上就是对 HTTP/2 中二进制帧的介绍，希望对你有所启发。</p>
<h2 class="heading">最后</h2>
<p>文章首发于<a target="_blank" href="https://github.com/sanyuan0704/my_blog">我的博客</a>，如果觉得对你有帮助的话，希望能帮忙点一个 star，非常感谢~</p>
<p></p><figure><img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/2/23/1707243edbc87a13~tplv-t2oaga2asx-image.image"><figcaption></figcaption></figure><p></p>
<p>参考:</p>
<p><a target="_blank" href="https://time.geekbang.org/course/intro/175">《web协议详解与抓包实战——陶辉》</a></p>
<p><a target="_blank" href="https://time.geekbang.org/column/intro/100029001">《透视 HTTP 协议》——chrono</a></p>
<p><a target="_blank" href="https://chromium.googlesource.com/chromium/src/+/refs/heads/master/ipc/">Chromium IPC 源码</a></p>
<p><a target="_blank" href="https://juejin.cn/post/6844903793918738440">前端开发者必备的Nginx知识 ——conardli</a></p>
