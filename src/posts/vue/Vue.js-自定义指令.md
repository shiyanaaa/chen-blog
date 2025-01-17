---
date: 2024-07-17
category:
    - vue.js
tag:
    - vue.js
    - 前端
    - 前端框架
    - javascript
---
 # Vue.js-自定义指令
> 学习笔记： [ 自定义指令 ]()

##  自定义指令

自定义指令的注册方法分为 **全局注册** 和 **局部注册** ，比如注册一个 ` v-focus ` 指令，用于在 ` <input> ` 、 `
<textarea> ` 元素初始化时自动获得焦点，两种写法分别是：

    
    
    //全局注册
    Vue.directive('focus', {});
    
    //局部注册
    new Vue({
        el: '#app',
        directives: {
            focus: {}
        }
    });
    

自定义指令的选项是由几个钩子函数组成，每个都是可选的：

  * ` bind ` ：只调用一次，指令第一次绑定到元素时调用，用这个钩子函数可以定义一个在绑定时执行一次的初始化动作。 
  * ` inserted ` ：被绑定元素插入父节点时调用（父节点存在即可调用，不必存在于 ` document ` 中）。 
  * ` update ` ：被绑定元素所在的模板更新时调用，而不论绑定值是否变化。通过比较更新前后的绑定值，可以忽略不必要的模板更新。 
  * ` componentUpdate ` ：被绑定元素所在模板完成一次更新周期时调用。 
  * ` unbind ` ：只调用一次，指令与元素解绑时调用。 

可以根据需求在不同的钩子函数内完成逻辑代码。在元素插入父节点时就调用，用到的最好是 ` inserted ` 。

    
    
    <div id="app">
        <input type="text" v-focus>
    </div>
    
    Vue.directive('focus', {
        inserted(el) {
            el.focus();
        }
    });
    new Vue({
        el: '#app',
    });
    

打开页面， ` input ` 输入框自动获得焦点，成为可输入状态。

每个钩子函数都有几个参数可用：

  * ` el ` 指令所绑定的元素，可以用来直接操作DOM 
  * ` binding ` 一个对象，包含以下属性： 

    * ` name ` 指令名，不包括 ` v- ` 前缀 
    * ` value ` 指令的绑定值 
    * ` oldValue ` 指令绑定的前一个值，仅在 ` update ` 和 ` componentUpdate ` 钩子中可用。无论值是否改变都可用。 
    * ` expression ` 绑定值的字符串形式。 
    * ` arg ` 传给指令的参数。 
    * ` modifiers ` 一个包含修饰符的对象。 
  * ` vnode ` Vue编译生成的虚拟节点。 
  * ` oldVnode ` 上一个虚拟节点仅在 ` update ` 和 ` componentUpdate ` 钩子中可用。 

<p data-height="265" data-theme-id="0" data-slug-hash="QxKQqY" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="Vue-自定义指令" class="codepen">See the Pen [ Vue-自定义指令 ]() by whjin ( [
@whjin ]() ) on [ CodePen ]() .</p>  


如果需要多个值，自定义指令可以传入一个JavaScript对象字面量。

    
    
    <div id="app">
        <div v-test="{msg:'hello',name:'Andy}"></div>
    </div>
    

##  开发一个实时时间转换指令 ` v-time `

<p data-height="265" data-theme-id="0" data-slug-hash="wXoMpg" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="Vue-实时时间转换指令" class="codepen">See the Pen [ Vue-实时时间转换指令 ]() by whjin (
[ @whjin ]() ) on [ CodePen ]() .</p>  


` Time.getFormatTime() ` 方法就是自定义指令 ` v-time ` 所需要的，入参为毫秒级时间戳，返回已经整理好时间格式的字符串。

在 ` bind ` 钩子里，将指令 ` v-time ` 表达式的值 ` binding.value ` 作为参数传入 `
TimeFormatTime() ` 方法得到格式化时间，再通过 ` el.innerHTML ` 写入指令所在元素。定时器 `
el.__timeout__ ` 每分钟触发一次，更新时间，并且在 ` unbind ` 钩子里清除掉。

**总结：** 在编写自定义指令时，给DOM绑定一次性事件等初始动作，建议在 ` bind ` 钩子内完成，同时要在 ` unbind ` 内解除相关绑定。

