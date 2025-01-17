---
date: 2024-02-05
category:
    - vue.js
tag:
    - vue.js
    - 前端
    - 前端框架
    - javascript
---
 # Vue.js-函数化组件
> 学习笔记： [ 函数化组件 ]()

##  函数化组件

Vue提供了一个 ` functional ` 的布尔值选项，设置为 ` true ` 可以使组件无状态和无实例，也就是没有 ` data ` 和 `
this ` 上下文。这样用 ` render ` 函数返回虚拟节点可以更容易渲染，因为函数化组件只是一个函数，渲染开销要小很多。

使用函数化组件时，Render函数提供了第二个参数 ` context ` 来提供临时上下文。组件需要的 ` data ` 、 ` prop ` 、 `
slots ` 、 ` children ` 、 ` parent ` 都是通过这个上下文来传递。比如 ` this.level ` 要改写为 `
context.props.level ` ， ` this.$slots.default ` 改变为 ` context.children ` 。

用函数化组件展示一个根据数据智能选择不同组件的场景：

<p data-height="365" data-theme-id="0" data-slug-hash="mKRKGm" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="Vue-函数化组件-根据数据选择组件" class="codepen">See the Pen [ Vue-函数化组件-根据数据选择组件
]() by whjin ( [ @whjin ]() ) on [ CodePen ]() .</p>  


函数化组件主要适用于以下两个场景：

  1. 程序化地在多个组件中选择一个。 
  2. 在将 ` children ` 、 ` props ` 、 ` data ` 传递给子组件之前操作它们。 

##  JSX

为了让Render函数更好地书写和阅读，Vue提供了插件 ` babel-plugin-transform-vue-jsx ` 来支持JSX语法。

使用 ` createElement ` 时，常用配置：

<p data-height="365" data-theme-id="0" data-slug-hash="Vdpwpz" data-default-
tab="js" data-user="whjin" data-embed-version="2" data-pen-title="Vue-
createElement" class="codepen">See the Pen [ Vue-createElement ]() by whjin (
[ @whjin ]() ) on [ CodePen ]() .</p>  


JSX写法：

<p data-height="300" data-theme-id="0" data-slug-hash="eKvYvm" data-default-
tab="js" data-user="whjin" data-embed-version="2" data-pen-title="Vue-JSX"
class="codepen">See the Pen [ Vue-JSX ]() by whjin ( [ @whjin ]() ) on [
CodePen ]() .</p>  


##  实战：使用Render函数开发可排序的表格组件

表格组件的所有的内容（表头和行数据）由两个 ` prop ` 构成： ` columns ` 和 ` data ` 。两者都是数组， ` columns `
用来描述每列的信息，并渲染在表头 ` <head> ` 内，可以指定某一列是否需要排序； ` data ` 时每一行的数据，由 ` columns `
决定每一行里各列的顺序。

为了让排序后的 ` columns ` 和 ` data ` 不影响原始数据，给 ` v-table ` 组件的 ` data `
选项添加两个对应的数据，组件所有的操作将在这两个数据上完成，不对原始数据做任何处理。

` columns ` 的每一项是一个对象，其中 ` title ` 和 ` key ` 字段是必填的，用来标识这列的表头标题， ` key ` 的对应 `
data ` 中列内容的字段名。 ` sortable ` 是选填字段，如果值为 ` true ` ，说明该列需要排序。

` v-talbe ` 组件的 ` prop:columns ` 和 ` data ` 的数据已经从父级传递过来， ` v-table `
不直接使用它们，而是使用 ` data ` 选项的 ` currentColumns ` 和 ` currentData ` 。所以在 ` v-table
` 初始化时，需要把 ` columns ` 和 ` data ` 赋值给 ` currentColumns ` 和 ` currentData ` 。在
` v-table ` 的 ` methods ` 选项里定义两个方法用来复制，并在 ` mounted ` 钩子内调用。

` map() ` 是JavaScript数组的一个方法，根据传入的函数重新构造一个新数组。

排序分升序( ` asc ` )和降序( ` desc ` )两种，而且同时只能对一列数据进行排序，与其他列互斥，为了标识当前列的排序状态，在 ` map
` 列添加数据时，默认给每列都添加一个 ` _sortType ` 的字段，并且赋值为 ` normal ` ，表示默认排序（也就是不排序）。

在排序后， ` currentData ` 每项的顺序可能都会发生变化，所以给 ` currentColumns ` 和 ` currentData `
的每个数据都添加 ` _index ` 字段，代表当前数据在原始数据中的索引。

    
    
    render(h) {
        var ths = [],
            trs = [];
        return h('table', [
            h('thead', [
                h('tr', ths)
            ]),
            h('tbody', trs)
        ])
    }
    

这里的 ` h ` 就是 ` createElement ` ，只是换了个名称。

表格主题 ` trs ` 是一个二维数组，数据由 ` currentColumns ` 和 ` currentData ` 组成。

先遍历所有的行，然后再每一行内再遍历各列，最终组合出主题内容节点 ` trs ` 。

如果 ` col.sortable ` 没有定义，或值为 ` false ` ，就直接把 ` col.title ` 渲染出来，否则除了渲染 ` title
` ，还加了两个 ` <a> ` 元素来实现升序和降序的操作。

排序使用了JavaScript数组的 ` sort() ` 方法，这里之所以返回 ` 1 ` 或 ` -1 ` ，而不直接返回 `
a[key]<b[key] ` ，也就是 ` true ` 或 ` false ` ，是因为在部分浏览器对 ` sort() ` 的处理不同，而 ` 1 `
和 ` -1 ` 可以做到兼容。

排序前，先将所有列的排序状态都重置为 ` normal ` ，然后设置当前列的排序状态（ ` asc ` 或 ` desc ` ），对用到render的 `
<a> ` 元素的 ` class ` 名称 ` on ` ，后面通过CSS来高亮显示当前列的排序状态。

当渲染完表格后，父级修改了 ` data ` 数据，比如增加或删除， ` v-table ` 的 ` currentData `
也应该更新，如果某列已经存在排序状态，更新后应该直接处理一次排序。

通过遍历 ` currentColumns ` 来找出是否按某一列进行过排序，如果有，就按照当前排序状态对更新后的数据做一次排序操作。

<p data-height="365" data-theme-id="0" data-slug-hash="XYMmJr" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="Vue-可排序表格组件" class="codepen">See the Pen [ Vue-可排序表格组件 ]() by whjin ( [
@whjin ]() ) on [ CodePen ]() .</p>  


##  实战：留言列表

发布一条留言，需要的数据有昵称和留言内容，发布操作应该在根实例 ` app ` 内完成。留言列表的数据也是从 ` app ` 获取。

数组 ` list ` 存储了所有的留言内容，通过函数 ` handleSend ` 给 ` list ` 添加一项留言数据，添加成后把 `
texrarea ` 文本框置空。

Render函数内的节点使用 ` v-model ` ：动态绑定 ` value ` ，并且监听 ` input ` 事件，把输入的内容通过 `
$emit('input') ` 派发给父组件。

列表数据 ` list ` 为空时，渲染一个“列表为空”的信息提示节点；不为空时，每个 ` list-item `
赢包含昵称、留言内容和回复按钮3个子节点。

` this.list.forEach ` 相当于 ` template ` 里的 ` v-for ` 指令，遍历出每条留言。句柄 `
handleReply ` 直接向父组件派发一个事件 ` reply ` ，父组件( ` app ` )接收后，将当前 ` list-item `
的昵称提取，并设置到 ` v-textarea ` 内。

<p data-height="365" data-theme-id="0" data-slug-hash="ZRKGrR" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="Vue-留言列表" class="codepen">See the Pen [ Vue-留言列表 ]() by whjin ( [
@whjin ]() ) on [ CodePen ]() .</p>  


