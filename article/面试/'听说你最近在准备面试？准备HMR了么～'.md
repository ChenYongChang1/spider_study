标题:听说你最近在准备面试？准备HMR了么～
描述:之前面试的时候，很多次面试官都有提到过HMR的原理，正好最近的react项目当中需要调试这一块，就做一个总结。

&emsp;&emsp;之前面试的时候，很多次面试官都有提到过HMR的原理，正好最近的react项目当中需要调试这一块，就做一个总结。   

&emsp;&emsp;在开发过程中，我们经常会用到webpack-dev-server，它有一个默认自带的功能就是live reloading（实时重新加载）功能。在命令行中运行 webpack serve，如果你更改任何源文件并保存它们，webpack-dev-server将在编译代码后自动刷新浏览器。  

&emsp;&emsp;但是这样有一个缺点，就是如果我们需要先进行一些操作，比如打开一个对话框，再调试对话框的样式。或者经过一些特定的查询后，来调试一个列表的样式。如果浏览器在改完代码后直接刷新了，那么我们还需要去通过打开对话框或者再去做特定的查询来验证刚才的修改效果。HMR即hot module replacement（模块热更新）就解决了这个问题，它保留了在完全重新加载页面期间丢失的应用程序状态，允许在运行时只更新被修改的模块，而无需完全刷新。webpack-dev-server 支持 hot 模式，在试图重新加载整个页面之前，hot 模式会尝试使用 HMR 来更新。

&emsp;&emsp;本文将从配置原理和实现原理两个方面来讲解模块热更新。

**配置原理**

从官方文档《指南》的 [热模块更新](https://webpack.docschina.org/guides/hot-module-replacement/#enabling-hmr) 部分中我们可以看出想要应用webpack的热模块更新能力，总共分两步：  

&emsp;&emsp;1.在devServer的配置中，加上 hot: true。
```
devServer: {
  contentBase: './dist',
+ hot: true,
},
```

&emsp;&emsp;2.引入模块时，通过 module.hot.accept 检查更新。
```
  if (module.hot) {
    module.hot.accept('./print.js', function() {
     document.body.removeChild(element);
     element = component(); // 重新渲染 "component"，以便更新 click 事件处理函数
     document.body.appendChild(element);
    })
  }
```

&emsp;&emsp;但是像style-loader、css-loader之中，其实在内部调用了module.hot.accept这样的HMR API来检查样式更新，所以就不用我们再额外加代码来加载更新后的代码。在css依赖模块更新之后，会将其patch到\<style\>标签中。

&emsp;&emsp;同样原理，社区还提供许多其他loader和示例，可以使HMR与各种框架和库平滑地进行交互，包括：React Hot Loader、Vue loader、Angular HMR。

&emsp;&emsp;Vue loader实现了在引入vue文件更新的时候，自动加载vue文件的更新。这里再来重点讲一下React框架中的HMR应用方式。React框架一开始用的React Hot Loader在官方声明中已经宣布将要被[react-refresh-webpack-plugin](https://github.com/pmmmwh/react-refresh-webpack-plugin)所取代。在它的官网中我们可以看到他的引入方式，这里需要强调的有两点：  

&emsp;&emsp;1.启动命令中的--hot 和 webpack配置中的 new webpack.HotModuleReplacementPlugin()不能同时使用。（https://github.com/webpack/webpack-dev-server/issues/87）  

&emsp;&emsp;2.在webpack调试环境的配置中不能使用externals配置。不然会让react-refresh-webpack-plugin失效。

**实现原理**

&emsp;&emsp;这里我们首先通过一张网图来总览：


![HMR全过程.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8c3fa22d3840bfafc58aa2dfbcf9ed~tplv-k3u1fbpfcp-watermark.image)

1. 编辑器中修改和保存代码。  
2. HotModuleReplacementPlugin会产生相应的更新代码的patch文件。  
3. 通过Webpack传给webpack-dev-server有文件更新的信息和更新后的相应patch文件。   
4. webpack-dev-server通过ws协议接口，向运行在浏览器中的webpack-dev-server/client发送消息，告诉浏览器有文件更新。  
5. webpack-dev-server/client将之前打包的hash值传给hot/dev-server，hot/dev-server相当于所有打包后js文件的主接口。   
6. hot/dev-server告知webpack引入的JSONP请求库来向webpack-dev-server请求manifest文件和chunk文件。  
7. HMR runtime将请求到的文件传送给相应的React-loader hmr或者Style-loader hmr来更新运行时App的相应的模块。
8. 如果更新失败，降级为刷新页面。

&emsp;&emsp;下面我们来举个例子看一下具体的请求，首先我们用create-react-app脚手架来初始化一个react项目：

![启动.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eae3d74c129847cdb9124b76123a5167~tplv-k3u1fbpfcp-watermark.image)

&emsp;&emsp;在初始化的过程中，webpack-dev-server与webpack-dev-server/client建立了ws连接，并且在连接中向webpack-dev-server/client传送了初始化的消息，其中比较重要的是画红框的这个hash值，表示下次HotModuleReplacementPlugin在打包patch文件的时候，会用到的hash。  

![截屏2021-07-11 下午10.07.30.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aa995bac82a4a24ae920a380f1921fc~tplv-k3u1fbpfcp-watermark.image)

&emsp;&emsp;当编辑器中的代码改变的时候，webpack-dev-server会发送给webpack-dev-server/client两个invalid消息，并且再传一个下次打包用的hash值。  

&emsp;&emsp;之后webpack-dev-server/client会触发hot/dev-server调用JSONP发送请求，来请求初始化时传来的hash值组成的本次代码更新的patch文件。patch文件一共有两个：hash.hot-update.json、chunk名.hash.hot-update.js。从下面两个图可以看出hash.hot-update.json文件中也是包含了下次打包会用到的hash值，而chunk名.hash.hot-update.js这个文件就包含了已经更新的包组成的webpackHotUpdate函数，这个函数将会传递给相应的loader来更新相应的包。

![截屏2021-07-11 下午10.09.31.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbba6a61d8334098b2519a7c576b5b1a~tplv-k3u1fbpfcp-watermark.image)


![截屏2021-07-11 下午10.09.48.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23449a5f12f47219f43d6393db83747~tplv-k3u1fbpfcp-watermark.image)

至此，就大概分析完了HMR的流程。

参考：https://rajaraodv.medium.com/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg

***********


