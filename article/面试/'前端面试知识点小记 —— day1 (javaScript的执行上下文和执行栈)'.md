标题:前端面试知识点小记 —— day1 (javaScript的执行上下文和执行栈)
描述:什么是执行上下文 执行上下文是评估和执行 JavaScript 代码的环境的抽象概念。每当JavaScript代码在运行的时候，它都是在执行上下文中运行。 执行上下文类型 全局执行上下文： 这是默认的

## 什么是执行上下文
执行上下文是评估和执行 JavaScript 代码的环境的抽象概念。每当JavaScript代码在运行的时候，它都是在执行上下文中运行。
### 执行上下文类型
- **全局执行上下文：** 这是默认的上下文， 任何不在浏览器内部的代码都在全局上下文中。一个程序中只会存在一个全局执行上下文，它会执行两件事：1. 创建一个全局window对象（浏览器的情况下）；2. 设置```this```的值对于这个全局对象。
- **函数执行上下文：** 每当一个```函数被调用```的时候，都会为该函数创建一个新的上下文。每个函数都有自己的执行上下文，不过是在函数被调用的时创建的。函数上下文可以有任意多个，每当一个新的执行上下文被创建，它会按定义的顺序执行一系列步骤。
- **Eval函数执行上下文：** 执行在```eval```函数内部的代码也会有属于自己的执行上下文

## 执行栈
执行栈，也就是在其它编程语言中所说的“调用栈”，是一种拥有 LIFO（后进先出）数据结构的栈，被用来存储代码运行时创建的所有执行上下文。

当 JavaScript 引擎第一次遇到你的脚本时，它会创建一个全局的执行上下文并且压入当前执行栈。每当引擎遇到一个函数调用，它会为该函数创建一个新的执行上下文并压入栈的顶部。

引擎会执行那些执行上下文位于栈顶的函数。当该函数执行结束时，执行上下文从栈中弹出，控制流程到达当前栈中的下一个上下文。

**示例：**
```
let a = 'Hello World!'; 

function first() { 
  console.log('Inside first function'); 
  second(); 
  console.log('Again inside first function'); 
}

function second() { 
  console.log('Inside second function'); 
} 

first(); 
console.log('Inside Global Execution Context');
```

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/411db704e71a48a084595930d27237c5~tplv-k3u1fbpfcp-watermark.image)

1. 上述代码在浏览器加载时，JavaScript 引擎创建了一个全局执行上下文并把它压入当前执行栈。
2. ```first()```被调用时，JavaScript 引擎为该函数创建一个新的执行上下文并把它压入当前执行栈的顶部。
3.  ```first()```内```second()```被调用时，JavaScript 引擎为```second()```函数创建一个新的函数执行上下文并将其压入栈顶。
4. ```second()```执行完成以后， 它的执行上下文会从当前执行栈中弹出，并且控制流程到达下一个执行上下文，即 `first()` 函数的执行上下文。
5. ```first()```执行完成以后，它的执行上下文从栈弹出，控制流程到达全局执行上下文。一旦所有代码执行完毕，JavaScript 引擎从当前栈中移除全局执行上下文。

## 怎么创建执行上下文？
到现在，我们已经看过 JavaScript 怎样管理执行上下文了，现在让我们了解 JavaScript 引擎是怎样创建执行上下文的。

创建执行上下文有两个阶段：**1) 创建阶段**   **2) 执行阶段**。

### 创建阶段
在 JavaScript 代码执行前，执行上下文将经历创建阶段。在创建阶段会发生三件事：
1. this的绑定
2. 创建**词法环境**组件
3. 创建**变量环境**组件

所以执行上下文在概念上表示如下：
```
ExecutionContext = { 
  ThisBinding = <this value>, 
  LexicalEnvironment = { ... }, 
  VariableEnvironment = { ... }, 
}
```
#### This绑定
在全局执行上下文中，`this` 的值指向全局对象。(在浏览器中，`this`引用 Window 对象)。

在函数执行上下文中，`this` 的值取决于该函数是如何被调用的。如果它被一个引用对象调用，那么 `this` 会被设置成那个对象，否则 `this` 的值被设置为全局对象或者 `undefined`（在严格模式下）。

#### 词法环境
在介绍`Lexical Environment`之前，我们先看下在V8里JS的编译执行过程，大致上可以分为三个阶段：
1. 第一步：V8引擎刚拿到`执行上下文`的时候，会把代码从上到下一行一行的先做分词/词法分析(Tokenizing/Lexing)。分词是指：比如`var a = 2；`这段代码，会被分词为：`var` `a` `2`和`;`这样的原子符号(atomic token)；词法分析是指：登记变量声明、函数声明、函数声明的形参。
2. 第二步：在分词结束以后，会做代码解析，引擎将 token 解析翻译成一个AST(抽象语法树)， 在这一步的时候，如果发现语法错误，就会直接报错不会再往下执行。
```
var greeting = "Hello";
console.log(greeting);
greeting = ."Hi";
// SyntaxError: unexpected token .
// 没有打印出 hello，而是先报错，说明JS引擎在真正执行代码之前，会做代码解析。
```
3. 第三步：引擎生成CPU可以执行的机器码。

第一步里有个词法分析，它用来登记变量声明、函数声明、函数声明的形参，后续代码执行的时候就知道去哪里拿变量的值和函数了，这个登记的地方就是`Lexical Environment（词法环境）`。

在词法环境的**内部**有两个组件:
1. **环境记录（Environment Record）** ，这个就是真正登记变量的地方;
     - **声明式环境记录（Declarative Environment Record）**: 用来记录直接有标识符定义的元素，比如变量、常量、let、class、module、import以及函数声明。
     - **对象式环境记录（Object Environment Record）** ：主要用于with和global的词法环境。  
2. **对外部词法环境的引用（outer）** ，它是作用域链能够连起来的关键。

其中 **声明式环境记录（Declarative Environment Record）** ，又分为两种类型：

-   **函数环境记录（Function Environment Record）** ：用于函数作用域。
-   **模块环境记录（Module Environment Record）** ：模块环境记录用于体现一个模块的外部作用域，即模块export所在环境。

词法环境与我们自己写的代码结构相对应，也就是我们自己代码写成什么样子，词法环境就是什么样子。词法环境是在代码定义的时候决定的，跟代码在哪里调用没有关系。所以说JavaScript采用的是词法作用域（静态作用域）。

示例：
```
var a = 2;
let x = 1;
const y = 5;

function foo() {
    console.log(a);

    function bar() {
        var b = 3;
        console.log(a * b);
    }

    bar();
}
function baz() {
    var a = 10;
    foo();
}
baz();
```
它的词法环境关系图如下：

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f716a0bd50e5427cb082cb908311440e~tplv-k3u1fbpfcp-watermark.image)
我们可以用伪代码来模拟上面代码的词法环境：
```
// 全局词法环境
GlobalEnvironment = {
    outer: null, //全局环境的外部环境引用为null
    GlobalEnvironmentRecord: {
        //全局this绑定指向全局对象
        [[GlobalThisValue]]: ObjectEnvironmentRecord[[BindingObject]],
        //声明式环境记录，除了全局函数和var，其他声明都绑定在这里
        DeclarativeEnvironmentRecord: {
            x: 1,
            y: 5
        },
        //对象式环境记录，绑定对象为全局对象
        ObjectEnvironmentRecord: {
            a: 2,
            foo:<< function>>,
            baz:<< function>>,
            isNaNl:<< function>>,
            isFinite: << function>>,
            parseInt: << function>>,
            parseFloat: << function>>,
            Array: << construct function>>,
            Object: << construct function>>
            ...
            ...
        }
    }
}
//foo函数词法环境
fooFunctionEnviroment = {
    outer: GlobalEnvironment,//外部词法环境引用指向全局环境
    FunctionEnvironmentRecord: {
        [[ThisValue]]: GlobalEnvironment,//this绑定指向全局环境
        bar:<< function>> 
    }
}
//bar函数词法环境
barFunctionEnviroment = {
    outer: fooFunctionEnviroment,//外部词法环境引用指向foo函数词法环境
    FunctionEnvironmentRecord: {
        [[ThisValue]]: GlobalEnvironment,//this绑定指向全局环境
        b: 3
    }
}

//baz函数词法环境
bazFunctionEnviroment = {
    outer: GlobalEnvironment,//外部词法环境引用指向全局环境
    FunctionEnvironmentRecord: {
        [[ThisValue]]: GlobalEnvironment,//this绑定指向全局环境
        a: 10
    }
}
```

#### 变量环境
它同样是一个词法环境，其环境记录器持有**变量声明语句**在执行上下文中创建的绑定关系。

如上所述，变量环境也是一个词法环境，所以它有着上面定义的词法环境的所有属性。

在 ES6 中，**词法环境**组件和**变量环境**的一个不同就是前者被用来存储函数声明和变量（`let` 和 `const`）绑定，而后者只用来存储 `var` 变量绑定。
示例：
```
let a = 20;  
const b = 30;  
var c;

function multiply(e, f) {  
 var g = 20;  
 return e * f * g;  
}

c = multiply(20, 30);
```
我们用伪代码来描述上述代码中执行上下文的创建过程：
```
//全局执行上下文
GlobalExectionContext = {
    // this绑定为全局对象
    ThisBinding: <Global Object>,
    // 词法环境
    LexicalEnvironment: {  
        //环境记录
      EnvironmentRecord: {  
        Type: "Object",  // 对象环境记录
        // 标识符绑定在这里 let const创建的变量a b在这
        a: < uninitialized >,  
        b: < uninitialized >,  
        multiply: < func >  
      }
      // 全局环境外部环境引入为null
      outer: <null>  
    },
  
    VariableEnvironment: {  
      EnvironmentRecord: {  
        Type: "Object",  // 对象环境记录
        // 标识符绑定在这里  var创建的c在这
        c: undefined,  
      }
      // 全局环境外部环境引入为null
      outer: <null>  
    }  
}

// 函数执行上下文
FunctionExectionContext = {
     //由于函数是默认调用 this绑定同样是全局对象
    ThisBinding: <Global Object>,
    // 词法环境
    LexicalEnvironment: {  
      EnvironmentRecord: {  
        Type: "Declarative",  // 声明性环境记录
        // 标识符绑定在这里  arguments对象在这
        Arguments: {0: 20, 1: 30, length: 2},  
      },  
      // 外部环境引入记录为</Global>
      outer: <GlobalEnvironment>  
    },
  
    VariableEnvironment: {  
      EnvironmentRecord: {  
        Type: "Declarative",  // 声明性环境记录
        // 标识符绑定在这里  var创建的g在这
        g: undefined  
      },  
      // 外部环境引入记录为</Global>
      outer: <GlobalEnvironment>  
    }  
 }
```























