---
date: 2024-05-07
category:
    - vue.js
tag:
    - vue.js
    - 前端框架
    - javascript
    - 前端
---
 # Vue.js-计算属性和class与style绑定
> 学习笔记： [ 前端开发文档 ]()

##  计算属性

所有的计算属性都以函数的形式写在Vue实例中的 ` computed ` 选项内，最终返回计算后的结果。

###  计算属性的用法

在一个计算属性中可以完成各种复杂的逻辑，包括运算、函数调用等，只要最终返回一个结果即可。

计算属性还可以依赖多个Vue实例的数据，只要其中任一数据变化，计算属性就会重新执行，视图也会更新。

每一个计算属性都包含一个 ` getter ` 和一个 ` setter ` 。

绝大多数情况下，只会用默认的 ` getter ` 方法读取一个计算属性，在业务中很少用到 ` setter `
，所以在声明一个计算属性时，可以直接使用默认的写法，不必将 ` getter ` 和 ` setter ` 都声明。

计算属性除了简单的文本插值外，还经常用于动态地设置元素的样式名称 ` class ` 和内联样式 ` style `
。当使用组件时，计算属性也经常用来动态传递 ` props ` 。

计算属性还有两个很实用的小技巧容易被忽略：

  1. 一是计算属性可以依赖其他计算属性； 
  2. 二是计算属性不仅可以依赖当前Vue实例的数据，还可以依赖其他实例的数据。 

    
    
    <div id="app1"></div>
        <div id="app2">
        {{reverseText}}
    </div>
    
    var app1 = new Vue({
        el: "#app1",
        data: {
            text: '123,456'
        },
    });
    var app2 = new Vue({
        el: "#app2",
        computed: {
            reverseText: function () {
                //这里依赖的是实例app1的数据text
                return app1.text.split(',').reverse().join(',');
            }
        }
    });

###  计算属性缓存

没有使用计算属性，在 ` methods ` 中定义了一个方法实现了相同的效果，甚至该方法还可以接受参数，使用起来更灵活。

**使用计算属性的原因在于它的依赖缓存** 。一个计算属性所依赖的数据发生变化时，它才会重新取值，在上例中只要 ` text `
值不改变，计算属性也就不更新。但是 ` methods ` 则不同，只要重新渲染，它就会被调用，因此函数也会被执行。

使用计算属性还是 ` methods ` 取决于你是否需要缓存，当遍历大数组和做大量计算时，应当使用计算属性，除非你不希望得到缓存。

##  v-bind及class与style绑定

` v-bind ` 的主要用法是动态更新HTML元素上的属性。

在数据绑定中， ` v-bind ` 最常见的两个应用就是元素的样式名称 ` class ` 和内联样式 ` style ` 的动态绑定。

###  绑定 ` class ` 的几种方式

####  对象语法

给 ` v-bind:class ` 设置一个对象，可以动态地切换 ` class ` ：

    
    
    <div id="app">
        <div :class="{'active':'isActive'}">测试文字</div>
    </div>
    
    new Vue({
        el: "#app",
        data: {
            isActive: true
        },
    });
    

对象中也可以传入多个属性，动态切换 ` class ` 。另外， ` :class ` 可以与普通 ` class ` 共存。

    
    
    <div class="static" :class="{'active':'isActive','error':isError}">测试文字</div>
    
    data: {
        isActive: true,
        isError: false
    }
    

当 ` :class ` 的表达式过长或逻辑复杂时，还可以绑定一个计算属性。当条件多于两个时，都可以使用 ` data ` 或 ` computed ` 。

除了计算属性，也可以直接绑定一个Object类型的数据，或者使用类似计算属性的 ` methods ` 。

####  数组语法

当需要应用多个 ` class ` 时，可以使用数组语法，给 ` :class ` 绑定一个数组，应用一个 ` class ` 列表：

    
    
    <div id="app">
        <div :class="[activeCls,errorCls]">测试文字</div>
    </div>
    
    new Vue({
        el: "#app",
        data: {
            activeCls: 'active',
            errorCls: 'error'
        }
    });
    
    // 结果
    <div class="active error">测试文字</div>
    

也可以使用三元表达式来根据条件切换 ` class ` ：

    
    
    <div :class="[isActive ? activeCls : '',errorCls]">测试文字</div>
    
    new Vue({
        el: "#app",
        data: {
            isActive: true,
            activeCls: 'active',
            errorCls: 'error'
        }
    });
    

当 ` class ` 有多个条件时，可以在数组语法中使用对象语法：

    
    
    <div id="app">
        <div :class="[{'active':isActive},errorCls]">测试文字</div>
    </div>
    

使用计算属性给元素动态设置类名，在业务中经常用到，尤其是在写复用的组件时，所以在开发过程中， **如果表达式较长或逻辑复杂，应该尽可能地优先使用计算属性**
。

####  在组件中使用

如果直接在自定义组件上使用 ` class ` 或 ` :class ` ，样式规则会直接应用到这个组件的根元素上。

    
    
    Vue.component('my-component', {
        template: `<p class="article">一些文本</p>`
    });
    

然后在调用这个组件时，应用对象语法或数组语法给组件绑定 ` class ` ：

    
    
    <div id="app">
        <my-component :class="{'active':isActive}"></my-component>
    </div>
    

这种用法仅适用于自定义组件的最外层是一个根元素，否则会无效。当不满足这种条件或需要给具体的子元素设置类名时，应当使用组件的 ` props ` 来传递。

###  绑定内联样式

使用 ` :style ` 可以给元素绑定内联样式，方法与 ` :class ` 类似，也有对象语法和数组语法，很像直接在元素上写CSS。

    
    
    <div id="app">
        <div :style="{'color':color, 'fontSize':fontSize+'px'}">文本</div>
    </div>
    
    new Vue({
        el: "#app",
        data: {
            color: 'red',
            fontSize: 14
        }
    });
    

一般把样式写在 ` data ` 或 ` computed ` 中：

    
    
    <div id="app">
        <div :style="styles">文本</div>
    </div>
    
    new Vue({
        el: "#app",
        data: {
            styles: {
                color: 'red',
                fontSize: 16 + 'px'
            }
        }
    });
    

在实际业务中， ` :style ` 的数组语法并不常用，可以写在一个对象里面，而较为常用的是计算属性。

另外，使用 ` :style ` 时，Vue.js会自动给特殊的CSS属性名称增加前缀，比如 ` transform ` 。

