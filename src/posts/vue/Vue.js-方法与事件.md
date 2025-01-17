---
date: 2024-06-02
category:
    - vue.js
tag:
    - vue.js
    - 前端
    - 前端框架
    - javascript
---
 # Vue.js-方法与事件
> 学习笔记： [ 方法与事件 ]()

##  方法与事件

@click调用得方法名后可以不跟括号 ` () ` ，如果该方法有参数，默认会将原生事件对象 ` event ` 传入。

这种在HTML元素上监听事件的设计看似将DOM与JavaScript紧耦合，违背分离的原理，实则刚好相反。因为通过HTML就可以知道调用的是哪个方法，将逻辑与DOM解耦，便于维护。

**最重要的是，当` viewModel ` 销毁时，所有的事件处理器都会自动销毁，无需自己处理。 **

Vue提供了一个特殊变量 ` $event ` ，用于访问原生DOM事件。

    
    
    <div id="app">
        <a href="https://www.apple.com/" @click="handleClick('禁止打开',$event)">打开链接</a>
    </div>
    

###  修饰符

Vue支持以下修饰符：

  * ` .stop `
  * ` .prevent `
  * ` .capture `
  * ` .self `
  * ` .once `

具体用法如下：

修饰符功能  |  使用示例   
---|---  
阻止单击事件冒泡  |  ` <a @click.stop="handle"></a> `  
提交事件不再重载页面  |  ` <form @submit.prevent="handle"></form> `  
修饰符可以串联  |  ` <a @click.stop.prevent="handle"></a> `  
只有修饰符  |  ` <form @submit.prevent></form> `  
添加事件侦听器时使用事件捕获模式  |  ` <div @click.capture="handle">...</div> `  
只当事件在该元素本身（不是子元素）触发时执行回调  |  ` <div @click.self="handle">...</div> `  
只触发一次，组件同样适用  |  ` <div @click.once="handle">...</div> `  
  
在表单元素上监听键盘事件时，还可以使用按键修饰符。

修饰符功能  |  使用示例   
---|---  
只有在 ` keyCode ` 是 ` 13 ` 时调用 ` vm.submit() ` |  ` <input @keyup.13="submit"> `  
  
除了具体的某个 ` keyCode ` 外，Vue还提供了一些快捷名称：

  * ` .enter `
  * ` .tab `
  * ` .delete ` （补货“删除”和“退格”键） 
  * ` .esc `
  * ` .space `
  * ` .up `
  * ` .down `
  * ` .left `
  * ` .right `

这些按键修饰符也可以组合使用，或和鼠标一起配合使用：

  * ` .ctrl `
  * ` .alt `
  * ` .shift `
  * ` .meta `

