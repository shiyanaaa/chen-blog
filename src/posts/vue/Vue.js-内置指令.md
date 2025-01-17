---
date: 2023-03-28
category:
    - vue.js
tag:
    - vue.js
    - 前端
    - 前端框架
    - javascript
---
 # Vue.js-内置指令
> 学习笔记： [ 内置指令 ]()

##  内置指令

###  基本指令

####  ` v-cloak `

` v-cloak ` 不需要表达式，它会在Vue实例结束编译时从绑定的HTML元素上移除，经常和CSS的 ` display: none; ` 配合使用：
```js
    
    
    <div id="app" v-cloak>
        {{message}}
    </div>
    
```
当网速较慢、Vue.js文件还没加载完时，在页面上会显示 ` {{message}} `
的字样，直到Vue创建实例、编译模板时，DOM才会被替换，所以这个过程屏幕有闪。只要加一句CSS就可以解决这个问题：

    
    
    [v-cloak] {
        display: none;
    }
    

v-cloak是一个解决初始化慢导致页面闪动的最佳实践，对于简单的项目很实用。

在工程化的项目中，项目的HTML结构只有一个空的 ` div ` 元素，剩下的内容都由路由挂载不同组件完成，这时不再需要 ` v-cloak ` 。

####  ` v-once `

` v-once `
是一个不需要表达式的指令，作用是定义它的元素或者组件只渲染一次，包括元素或组件的所有子节点。首次渲染后，不再随数据的变化重新渲染，将被视为静态内容。

` v-once ` 在业务中很少使用，如果需要进一步优化性能时，可能会用到。

###  条件渲染指令

####  ` v-if ` 、 ` v-else-if ` 、 ` v-else `

Vue.js的条件指令可以根据表达式的值在DOM中渲染或销毁元素/组件。

` v-else-if ` 要紧跟 ` v-if ` ， ` v-else ` 要紧跟 ` v-else-if ` 或 ` v-if `
，表达式的值为真时，当前元素/组件及所有子节点将被渲染，为假时被移除。

如果一次判断的是多个元素，可以在Vue.js内置的 ` <template> ` 元素上使用条件指令，最终渲染的结果不会包含该元素。

Vue在渲染元素时，处于效率考虑，会尽可能地复用已有的元素，而非重新渲染。

<p data-height="265" data-theme-id="0" data-slug-hash="KewYmd" data-default-
tab="html,result" data-user="whjin" data-embed-version="2" data-pen-
title="条件渲染指令" class="codepen">See the Pen [ 条件渲染指令 ]() by whjin ( [ @whjin
]() ) on [ CodePen ]() .</p>  


示例中键入内容后，点击切换按钮，虽然DOM改变了，但是之前在输入框键入的内容并没有改变，只是替换了 ` placeholder ` 的内容，说明 `
<input> ` 元素被复用了。

使用Vue.js提供的 ` key ` 属性，可以让你自己决定是否要复用元素， ` key ` 的值必须是唯一的。
```js
    
    
    <input type="text" placeholder="输入用户名" key="name-input">
    
```
给两个 ` <input> ` 元素都增加了 ` key ` 后，就不会复用了。切换类型时键入的内容也会被删除，不过 ` <label> `
元素仍然会被复用，因为没有添加 ` key ` 属性。

####  ` v-show `

` v-show ` 的用法与 ` v-if ` 基本一致，只不过 ` v-show ` 是改变元素的CSS属性 ` display ` 。

当 ` v-show ` 表达式的值为 ` false ` 时元素会隐藏，DOM结构元素上加载了内联样式 ` display:none; ` 。

**` v-show ` 不能在 ` <template> ` 上使用 ** 。

####  ` v-if ` 与 ` v-show ` 的选择

` v-if ` 和 ` v-show ` 具有类似的功能，不过 ` v-if ` 才是真正的条件渲染，它会根据表达式适当地 **销毁或重建**
元素及绑定的事件或子组件。

若表达式初始值为 ` false ` ，则一开始元素/组件并不会渲染，只有当条件第一次变为真时才开始编译。

而 ` v-show ` 只是简单的CSS属性切换，无论条件真与否，都会被编译。

相比之下， ` v-if ` 更适合条件不经常改变的场景，因为它的切换开销相对较大，而 ` v-show ` 适用于频繁切换条件。

###  列表渲染指令 ` v-for `

####  基本用法

当需要将一个数组遍历或枚举一个对象循环显示时，就会用到列表渲染指令 ` v-for ` 。它的表达式需结合 ` in ` 来使用，类似 ` item in
items ` 的形式。

列表渲染也支持用 ` of ` 代替 ` in ` 作为分隔符，它更接近JavaScript迭代器的语法：
```js
    
    
    <li v-for="book of books">{{book.name}}</li>
    
```
` v-for ` 的表达式支持一个可选参数作为当前项的索引。
```js
    
    
    <li v-for="(book,index) of books">{{index}} - {{book.name}}</li>
    
```
分隔符 ` in ` 前的语句使用括号，第二项就是 ` books ` 当前项的索引。

与 ` v-if ` 一样， ` v-for ` 也可以用在内置标签 ` <template> ` 上，将多个元素进行渲染。

除了数组外，对象的属性也是可以遍历的。

遍历对象属性时，有两个可选参数，分别是键名和索引：
```js
    
    
    <div id="app">
        <ul>
            <li v-for="(value,key,index) of users">
                {{index}} - {{key}} - {{value}}
            </li>
        </ul>
    </div>
    
```
` v-for ` 还可以迭代整数：
```js
    
    
    <div id="app">
        <span v-for="n in 10">{{n}}</span>
    </div>
    
```
###  数组更新

Vue的核心是数据与视图的双向绑定，包含了一组观察数组变化的方法，使用它们改变数组也会触发视图更新：

  * ` push() `
  * ` pop() `
  * ` shift() `
  * ` unshift() `
  * ` splice() `
  * ` sort() `
  * ` reverse() `

使用以上方法会改变被这些方法调用的原始数组。

以下方法不会改变原数组：

  * ` filter() `
  * ` concat() `
  * ` slice() `

它们返回的是一个新数组，在使用这些非变异方法时，可以用新数组来替换元素组。

Vue在检测到数组变化时，并不是直接重新渲染整个列表，而是最大化地复用DOM元素。替换的数组中，含有相同元素的项不会被重新渲染，因此可以大胆地用新数组来替换旧数组，不用担心性能问题。

需要注意的是，以下变动的数组中，Vue时不能检测到的，也不会触发视图更新：

  * 通过索引直接设置项， ` app.books[3]={} `
  * 修改数组长度， ` app.books.length=1 `

解决第一个问题可以用两种方法实现同样的效果，第一种是使用Vue内置的 ` set ` 方法：

    
    
    Vue.set(app.books, 3, {
        name: '《CSS秘密花园》',
        author: '无名氏'
    });
    

如果是在webpack中使用组件化的方式，默认是没有导入Vue的，这时可以使用 ` this.$set ` 。

另一种方法： ` app.books.splice(3,1,{}) `

###  过滤与排序

如果不希望改变原数组，想通过一个数组的副本来做过滤或排序的显示时，可以使用计算属性返回过滤或排序后的数组。

