标题:Ajax 简介、封装、同步异步 & 相关面试题
描述:什么是 Ajax ？ Ajax = 异步 JavaScript 和 XML； Ajax 是一种用于创建快速动态网页的技术；

#### 一、Ajax 简介

**（1）什么是 Ajax ？**
- Ajax  = 异步 JavaScript 和 XML；
- Ajax 是一种用于创建快速动态网页的技术；
- 通过在后台与服务器进行少量数据交换，Ajax  可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新；

**（2）工作原理**：

![](https://upload-images.jianshu.io/upload_images/25341256-2caf9ec0ec6149bd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**（3）Ajax 的优点和缺点**：

优点：
- 实现异步通信效果
- 实现页面局部刷新
- 带来更好的用户体验
- 按需获取数据
- 节约带宽资源

缺点：
- Ajax  不支持浏览器 back 按钮
- 安全问题 Ajax 暴露了与服务器交互的细节
- 对搜索引擎的支持比较弱
- 破坏了程序的异常机制

#### 二、创建 XMLHttpRquest 对象

XMLHttpRequest 是 Ajax  的基础。

**语法**：
```js
variable = new XMLHttpRequest();
```

为了应对所有的现代浏览器，包括 IE5 和 IE6，请检查浏览器是否支持 XMLHttpRequest 对象。如果支持，则创建 XMLHttpRequest 对象。如果不支持，则创建 ActiveXObject ：

示例：
```js
function loadXMLDoc() {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp=new XMLHttpRequest();
    } else {
        // IE6, IE5 浏览器执行代码
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {
            document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET","/try/ajax/ajax_info.txt",true);
    xmlhttp.send();
}
```
#### 三、封装 Ajax 

```js
//封装ajax
function ajax(obj) {
      
    //创建XMLHttpRequest对象
    if(window.XMLHttpRequest) {
        var xhr = new XMLHttpRequest();
    }else{
        var xhr = new ActiveXObject("Microsoft.XMLHTTP");
    }
    
    obj.url = obj.url+'?rand='+Math.random();      //使用js随机字符串解决IE第二次它就默认获取缓存数据，导致数据不更新
    
    obj.data = (function(data){                         //名值对转换为字符串闭包的方式调用
        var arr = [];
        for(var i in data){
            arr.push(encodeURIComponent(i)+'='+encodeURIComponent(data[i]));
        }
        return arr.join('&');
    })(obj.data);
    if(obj.method === 'get')obj.url += obj.url.indexOf('?') == -1?'?'+obj.data:'&'+obj.data;
    
    if(obj.async === true){
        xhr.onreadystatechange = function(){
            if(xhr.readyState == 4){
                callback();
            }
        };
    }

    xhr.open(obj.method,obj.url,obj.async);
    if(obj.method === 'post'){
        xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded');        //模仿表单提交
        xhr.send(obj.data);
    }else{
        xhr.send(null);
    }
    if(obj.async === false){
        callback();
    }
        
    function callback(){
        if(xhr.status == 200){
            obj.success(xhr.responseText);                                        //函数回调
        }else{
            alert('获取数据失败!错误代号：'+xhr.status+',错误信息：'+xhr.statusText);
        }
    }
}

//调用ajax
$(document).click(function(){
    ajax({
    method : 'post',
    url : 'demo.php',
    data : {
        'name' : 'Lee',
        'age' : 100
    },
    success : function (text) {
        alert(text);
    },
    async : true
    });
});
```

#### 四、同步和异步
Ajax  中根据 async 的值不同分为同步（async = false）和异步（async = true）

```js
$.ajax({ 
    type: "post", 
    url: "path", 
    cache:false, 
    async:false, 
    dataType: ($.browser.msie) ? "text" : "xml", 

    success: function(xmlobj){ 
        function1(){};
    } 
});
 function2(){};
```
- 默认情况下 async 是 true；

**（1）概念：**

- 同步请求：(false)
同步请求即是当前发出请求后，浏览器什么都不能做，必须得等到请求完成返回数据之后，才会执行后续的代码，相当于是排队，前一个人办理完自己的事务，下一个人才能接着办。

- 异步请求：(true)
异步请求就当发出请求的同时，浏览器可以继续做任何事，Ajax发送请求并不会影响页面的加载与用户的操作，相当于是在两条线上，各走各的，互不影响。
一般默认值为true，异步。异步请求可以完全不影响用户的体验效果，无论请求的时间长或者短，用户都在专心的操作页面的其他内容，并不会有等待的感觉。

**（2）区别：**
- 同步是所有的操作都做完，才返回给用户结果。即写完数据库之后，再响应用户，用户体验不好。
- 异步不用等所有操作都做完，就相应用户请求。即先响应用户请求，然后慢慢去写数据库，用户体验较好。


#### 五、Ajax 相关面试题
- 什么是Ajax ? 如何创建一个 Ajax 以及请求状态，从0-4的变化
- 同步和异步的区别?
- 简述 Ajax 的过程
- 页面编码和被请求的资源编码如果不一致如何处理？
- 阐述一下异步加载
- GET和POST的区别，何时使用POST？
- Ajax  属于 javascript？
- Ajax-GET-IE兼容问题
- Ajax-GET 封装
- POST 请求
- Ajax-POST 基本使用
- jQuery 中的 Ajax
- Ajax-XML
- Ajax-json
- 工作当中会和后台交互吗？ 那你能说说封装好的 ajax里的几个参数吗 ？
- 为什么要用ajax
- ajax最大的特点是什么？
- Ajax主要包含了哪些技术？
- ajax应用和传统Web应用有什么不同
- Ajax 请求总共有多少种CALLBACK
- 介绍一下Prototype的$()函数，$F()函数，$A()函数都是什么作用
- Ajax 都有哪些优点和缺点？
- 常用的 Ajax 框架有哪些？
- Ajax 的核心对象是什么？
- 如何实现 Ajax 请求
- Ajax 解决浏览器缓存问题

![](https://upload-images.jianshu.io/upload_images/25341256-177d9089ff0250e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```js
  想要领取 Ajax 面试题和学习前端的小伙伴们，可以加入这边的Q裙：【624369675】
  更多`前端学习资料 + 前端大厂面试真题`，均可免费领取！
```