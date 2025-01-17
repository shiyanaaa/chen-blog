---
date: 2024-05-05
category:
    - javascript
tag:
    - javascript
    - 前端框架
    - 前端
    - vue.js
---
 # Vue常用组件的开发
> 查看 [ 原文站点 ]() ，更多扩展内容及更佳阅读体验！

##  实战：常用组件的开发

数字输入框只能输入数字，而且有两个快捷按钮，可以直接减1或加1。除此之外，还可以设置初始值、最大/小值，在数值改变时，触发一个自定义事件来通知父组件。

目录文件：

  * ` index.html ` 入口页 
  * ` input-number.js ` 数字输入框组件 
  * ` index.js ` 根实例 

先在 ` template ` 里定义组件的根节点，因为是独立组件，所以应该对每个 ` prop ` 进行校验。

接下来，先在父组件引入 ` input-number ` 组件。

` value ` 是一个关键的绑定值，使用 ` v-model ` 。大多数的表单组件都应该有一个 ` v-model `
，比如输入框、单选框、多选框、下拉选择器等。

Vue组件时单向数据流，无法从组件内部直接修改 ` prop value ` 的值。

解决办法是给组件声明一个 ` data ` ，默认引用 ` value ` 的值，然后在组件内部维护这个 ` data ` 。

    
    
    Vue.component('input-number', {
        data() {
            return {
                currentValue: this.value
            }
        }
    });
    

这样只解决了初始化时引用父组件 ` value ` 的问题，但是如果从父组件修改了 ` value ` ， ` input-number ` 组件的 `
currentValue ` 也要一起更新。

监听（ ` watch ` ）， ` watch ` 选项用来监听某个 ` prop ` 或 ` data ` 的改变，当它们发生变化时，就会触发 `
watch ` 配置的函数，从而完成业务逻辑。

从父组件传递过来的 ` value ` 可能不符合当前条件（大于 ` max ` ，或小于 ` min ` ），所以在 ` methods `
中写了一个方法 ` updateValue ` ，用来过滤出一个正确的 ` currentValue ` 。

` watch ` 监听的数据的回调函数有2个参数可用，第一个是新的值，第二个是旧的值。

在回调函数里， ` this ` 指向当前组件实例。所以可以直接调用 ` this.updateValue() ` ，因为Vue代理了 ` props `
、 ` data ` 、 ` computed ` 及 ` methods ` 。

监听 ` currentValue ` 的回调里， ` this.$emit('input',val) ` 在使用 ` v-model ` 时改变 `
value ` ， ` this.$emit('on-change',val) ` 是触发自定义事件 ` on-change `
，用于告知父组件数字输入框的值有所变化。

在生命周期 ` mounted ` 钩子里也调用了 ` updateValue() ` 方法，是因为第一次初始化时，也对 ` value ` 进行了过滤。

` input ` 绑定了数据 ` currentValue ` 和原生的 ` change ` 事件，在句柄 ` handleChange `
函数中，判断了当前输入的是否时数字。

<p data-height="365" data-theme-id="0" data-slug-hash="oyzBWM" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="Vue组件实例" class="codepen">See the Pen [ Vue组件实例 ]() by whjin ( [ @whjin
]() ) on [ CodePen ]() .</p>  


##  标签页组件

每个标签页的主体内容由使用组件的父级控制，这部分是一个 ` slot ` ，而且 ` slot ` 的数量决定标签切换按钮的数量。

文件目录：

  * ` index.html ` 入口页 
  * ` style.css ` 样式表 
  * ` tabs.js ` 标签页外层的组件tabs 
  * ` pane.js ` 标签页嵌套的组件pane 

` pane ` 需要控制标签页内容的显示与隐藏，设置一个 ` data:show ` ，并且用 ` v-show ` 指令来控制元素。

` getTabs ` 是一个公用的方法，使用 ` this.$children ` 来取到所有的 ` pane ` 组件实例。

在 ` methods ` 中使用了有 ` function ` 回调的方法时，在回调内的 ` this ` 不再执行当前的Vue实例，也就是 ` tabs
` 组件本身，需要在外层设置一个 ` _this=this ` 的局部变量来间接使用 ` this ` 。

遍历每一个 ` pane ` 组件后，把它的 ` label ` 和 ` name ` 提取出来，构成一个 ` Object ` 并添加到数据 `
navList ` 数组里。

在使用 ` v-for ` 指令循环显示 ` tab ` 标题时，使用 ` v-bind:class ` 指向了一个名为 ` tabCls ` 的 `
methods ` 来动态设置 ` class ` 名称。

点击每个 ` tab ` 标题时，会触发 ` handleChange ` 方法来改变当前选中 ` tab ` 的索引，也就是 ` pane ` 组件的 `
name ` 。在 ` watch ` 选项中监听了 ` currentValue ` ，当其发生变化时，触发 ` updateStatus ` 方法来更新
` pane ` 组件的显示状态。

> 使用组件嵌套的方式，将一系列 ` pane ` 组件作为 ` tabs ` 组件的 ` slot ` ； ` tabs ` 组件和 ` pane `
> 组件通信上，使用了 ` $parent ` 和 ` $children ` 的方法访问父链和子链；定义了 ` prop:value ` 和 `
> data:currentValue ` ，使用 ` $emit('input') ` 来实现 ` v-model ` 的用法。

<p data-height="365" data-theme-id="0" data-slug-hash="vrXWQw" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="Vue-tabs" class="codepen">See the Pen [ Vue-tabs ]() by whjin ( [
@whjin ]() ) on [ CodePen ]() .</p>  


