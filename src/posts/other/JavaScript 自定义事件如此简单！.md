---
date: 2024-01-21
category:
    - javascript
tag:
    - javascript
    - 前端
    - node.js
---
 # JavaScript 自定义事件如此简单！
在前端开发世界中，JavaScript 和 HTML 之间往往通过 **事件** 来实现交互。其中多数为内置事件，本文主要介绍 JS
**自定义事件概念和实现方式** ，并结合案例详细分析自定义事件的原理、功能、应用及注意事项。

##  ?一、什么是自定义事件

在日常开发中，我们习惯监听页面许多事件，诸如：点击事件（ ` click ` ）、鼠标移动事件（ ` mousemove ` ）、元素失去焦点事件（ `
blur ` ）等等。  
  
  
事件本质是一种通信方式，是一种消息，只有在多对象多模块时，才有可能需要使用事件进行通信。在多模块化开发时，可以使用 **自定义事件** 进行模块间通信。  
  
  
当某些基础事件无法满足我们业务，就可以尝试 **自定义事件** 来解决。

##  ?二、实现方式介绍

目前实现 **自定义事件** 的两种主要方式是 JS 原生的 ` Event() ` 构造函数和 ` CustomEvent() ` 构造函数来创建。  

###  1\. Event()

` Event() ` 构造函数, 创建一个新的事件对象 ` Event ` 。

####  1.1 语法

    
    
    let myEvent = new Event(typeArg, eventInit);

####  1.2 参数

` typeArg ` ： ` DOMString ` 类型，表示创建事件的名称；  
` eventInit ` ：可选配置项，包括：

字段名称  |  说明  |  是否可选  |  类型  |  默认值   
---|---|---|---|---  
` bubbles ` |  表示该事件 **是否冒泡** 。  |  可选  |  ` Boolean ` |  false   
` cancelable ` |  表示该事件 **能否被取消** 。  |  可选  |  ` Boolean ` |  false   
` composed ` |  指示事件是否会在 **影子DOM根节点之外** 触发侦听器。  |  可选  |  ` Boolean ` |  false   
  
####  1.3 演示示例

    
    
    // 创建一个支持冒泡且不能被取消的 pingan 事件
    let myEvent = new Event("pingan", {"bubbles":true, "cancelable":false});
    document.dispatchEvent(myEvent);
    
    // 事件可以在任何元素触发，不仅仅是document
    testDOM.dispatchEvent(myEvent);

####  1.4 兼容性

  
图片来源： [ https://caniuse.com/ ]()

###  2\. CustomEvent()

` CustomEvent() ` 构造函数, 创建一个新的事件对象 ` CustomEvent ` 。

####  2.1 语法

    
    
    let myEvent = new CustomEvent(typeArg, eventInit);

####  2.2 参数

` typeArg ` ： ` DOMString ` 类型，表示创建事件的名称；  
` eventInit ` ：可选配置项，包括：

字段名称  |  说明  |  是否可选  |  类型  |  默认值   
---|---|---|---|---  
` detail ` |  表示该事件中需要被传递的数据，在 ` EventListener ` 获取。  |  可选  |  ` Any ` |  null   
` bubbles ` |  表示该事件 **是否冒泡** 。  |  可选  |  ` Boolean ` |  false   
` cancelable ` |  表示该事件 **能否被取消** 。  |  可选  |  ` Boolean ` |  false   
  
####  2.3 演示示例

    
    
    // 创建事件
    let myEvent = new CustomEvent("pingan", {
        detail: { name: "wangpingan" }
    });
    
    // 添加适当的事件监听器
    window.addEventListener("pingan", e => {
        alert(`pingan事件触发，是 ${e.detail.name} 触发。`);
    });
    document.getElementById("leo2").addEventListener(
      "click", function () {
        // 派发事件
        window.dispatchEvent(myEvent);
      }
    )

  
  
  
我们也可以给自定义事件添加属性：

    
    
    myEvent.age = 18;

####  2.4 兼容性

  
图片来源： [ https://caniuse.com/ ]()

####  2.5 IE8 兼容

分发事件时，需要使用 ` dispatchEvent ` 事件触发，它在 IE8 及以下版本中需要进行使用 ` fireEvent ` 方法兼容：

    
    
    if(window.dispatchEvent) {  
        window.dispatchEvent(myEvent);
    } else {
        window.fireEvent(myEvent);
    }

###  3\. Event() 与 CustomEvent() 区别

从两者支持的参数中，可以看出：  
` Event() ` 适合创建简单的自定义事件，而 ` CustomEvent() ` 支持参数传递的自定义事件，它支持 ` detail `
参数，作为事件中 **需要被传递的数据** ，并在 ` EventListener ` 获取。

**注意:**  
当一个事件触发时，若相应的元素及其上级元素没有进行事件监听，则不会有回调操作执行。  
当需要对于子元素进行监听，可以在其父元素进行事件托管，让事件在事件冒泡阶段被监听器捕获并执行。此时可以使用 ` event.target `
获取到具体触发事件的元素。

##  ?三、使用场景

**事件本质是一种消息** ，事件模式本质上是 **观察者模式** 的实现，即能用 **观察者模式** 的地方，自然也能用 **事件模式** 。  

###  1.场景介绍

比如这两种场景：  

  * **场景1：单个目标对象发生改变，需要通知多个观察者一同改变。**

如：当微博列表中点击“关注”，此时会同时发生很多事：推荐更多类似微博，个人关注数增加...  

  * **场景2：解耦多模块开协作。**

如：小王负责A模块开发，小陈负责B模块开发，模块B需要模块A正常运行之后才能执行。

###  2\. 代码实现

####  2.1 场景1实现

**场景1：单个目标对象发生改变，需要通知多个观察者一同改变。**  
本例子模拟三个页面进行演示：  
1.微博列表页（Weibo.js）  
2.粉丝列表页（User.js）  
3.微博首页（Home.js）

在 **微博列表页（Weibo.js）** 中，我们导入其他两个页面，并且监听【关注微博】按钮的点击事件，在回调事件中，创建一个自定义事件 `
focusUser ` ，并在 ` document ` 上使用 ` dispatchEvent ` 方法派发自定义事件。

    
    
    // Weibo.js
    import UserModule from "./User.js";
    import HomeModule from "./Home.js";
    const eventButton = document.getElementById("eventButton");
    eventButton.addEventListener("click", event => {
        const focusUser = new Event("focusUser");
      document.dispatchEvent(focusUser);
    })

接下来两个页面实现的代码基本一致，这里为了方便观察，设置了两者不同输出日志。

    
    
    // User.js
    const eventButton = document.getElementById("eventButton");
    document.addEventListener("focusUser", event => {
        console.log("【粉丝列表页】监听到自定义事件触发，event：",event);
    })
    
    // Home.js
    const eventButton = document.getElementById("eventButton");
    document.addEventListener("focusUser", event => {
        console.log("【微博首页】监听到自定义事件触发，event：",event);
    })

点击【关注微博】按钮后，看到控制台输出如下日志信息：

最终实现了，在 **微博列表页（Weibo.js）** 组件负责派发事件，其他组价负责监听事件，这样三个组件之间耦合度非常低，完全不用关系对方，互相不影响。  
**其实这也是实现了观察者模式。**

####  2.2 场景2实现

**场景2：解耦多模块开协作。**  
举个更直观的例子，当微博需要加入【 **一键三连** 】新功能，需要产品原型和UI设计完后，程序员才能开发。  
本例子模拟四个模块：  
1.流程控制（Index.js）  
2.产品设计（Production.js）  
3.UI设计（Design.js）  
4.程序员开发（Develop.js）

在 **流程控制（Index.js）模块**
中，我们需要将其他三个流程的模块都导入进来，然后监听【开始任务】按钮的点击事件，在回调事件中，创建一个自定义事件 ` startTask ` ，并在 `
document ` 上使用 ` dispatchEvent ` 方法派发自定义事件。

    
    
    // Index.js
    import ProductionModule from "./Production.js";
    import DesignModule from "./Design.js";
    import DevelopModule from "./Develop.js";
    
    const start = document.getElementById("start");
    start.addEventListener("click", event => {
        console.log("开始执行任务")
        const startTask = new Event("startTask");
        document.dispatchEvent(startTask);
    })

在 Production 产品设计模块中，监听任务开始事件 ` startTask ` 后，模拟1秒后原型设计完成，并派发一个新的事件 `
productionSuccess ` ，开始接下来的UI稿设计。

    
    
    // Production.js
    document.addEventListener("startTask", () => {
        console.log("产品开始设计...");
        setTimeout(() => {
            console.log("产品原型设计完成");
            console.log("--------------");
            document.dispatchEvent(new Event("productionSuccess"));
        }, 1000);
    });

在UI稿设计和程序开发模块，其实也类似，代码实现：

    
    
    // Dedign.js
    document.addEventListener("productionSuccess", () => {
        console.log("UI稿开始设计...");
        setTimeout(() => {
            console.log("UI稿设计完成");
            console.log("--------------");
            document.dispatchEvent(new Event("designSuccess"));
        }, 1000);
    });
    
    // Production.js
    document.addEventListener("designSuccess", function (e) {
        console.log("开始开发功能...");
        setTimeout(function () {
            console.log("【一键三连】开发完成");
        }, 2000)
    });

开发完成后，我们点击【开始任务】按钮后，看到控制台输出如下日志信息：

最终实现了在 **流程控制（Index.js）模块** 负责派发事件，其他组件负责监听事件，按流程完成其他任务。  
**可以看出，原型设计、UI稿设计和程序开发任务，互不影响，易于任务拓展。**

##  ?四、总结

本文详细介绍 JS **自定义事件概念和实现方式** ，并结合两个实际场景进行代码演示。细心的小伙伴会发现，这两个实际场景都是用 ` Event() `
构造函数实现，当然也是可以使用 ` CustomEvent ` 构造函数来代替。  
另外本文也详细介绍两种实现方式，包括其区别和兼容性。  
最后也希望大家能在实际开发中，多思考代码解耦，适当使用 **自定义事件** 来提高代码质量。

如有错误，欢迎指点。

##  ?五、参考文章

  * 《 [ javascript自定义事件功能与用法实例分析 ]() 》 
  * 《 [ Event - MDN ]() 》 
  * 《 [ CustomEvent - MDN ]() 》 

##  推荐阅读

  * [ 《1.2w字 ｜ 初中级前端 JavaScript 自测清单 - 1》 ]()
  * [ 《了不起的 Webpack 构建流程学习指南》 ]()
  * [ 《了不起的 Webpack HMR 学习指南（含源码分析）》 ]()
  * [ 《你不知道的 WeakMap》番外篇 ]()
  * [ 《你不知道的 Blob》番外篇 ]()
  * [ 《了不起的 tsconfig.json 指南》 ]()

