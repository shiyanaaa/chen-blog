---
date: 2024-03-18
category:
    - 前端框架
tag:
    - 前端框架
    - javascript
    - 前端
    - vue.js
---
 # Vue-组件详解
> 查看 [ 原文站点 ]() ，更多扩展内容及更佳阅读体验！

##  组件详解

###  组件与复用

Vue组件需要注册后才可以使用。注册有全局注册和局部注册两种方式。

**全局注册**

    
 ```js   
    Vue.component('my-component', {});
```

要在父实例中使用这个组件，必须要在实例创建前注册，之后就可以用 ` <my-component></my-component> ` 的形式来使用组件。
```js
    
    
    Vue.component('my-component', {
        template: `<div>这是一个组件</div>`
    });
```

` template ` 的DOM结构必须被一个元素包含，缺少 ` <div></div> ` 会无法渲染并报错。

在Vue实例中，使用 ` components ` 选项可以局部注册组件，注册后的组件只在该实例作用域下有效。

组件中也可以使用 ` components ` 选项来注册组件，使组件可以嵌套。
```js
    
    
    var Child = {
        template: `<div>局部注册组件的内容</div>`
    };
    
    new Vue({
        el: '#app',
        components: {
            'my-component': Child
        },
    });
 ```

Vue组件的模板在某些情况下会受到HTML的限制，比如 ` <table> ` 内规定只允许是 ` <tr> ` 、 ` <td> ` 、 ` <th> `
等这些表格元素，所以在 ` <table> ` 内直接使用组件时无效的。 **这种情况下，可以使用特殊的` is ` 属性来挂载组件 ** 。
```html
    
    
    <div id="app">
        <table>
            <tbody is="my-component"></tbody>
        </table>
    </div>
    
    Vue.component('my-component', {
        template: `<div>这里是组件内容</div>`
    });
 ```   

常见的限制元素还有 ` <ul> ` 、 ` <ol> ` 、 ` <select> ` 。

除了 ` template ` 选项外，组件中还可以像Vue实例那样使用其他的选项，比如 ` data ` 、 ` computed ` 、 `
methods ` 等。

**但是在使用` data ` 时， ` data ` 必须是函数，然后将数据 ` return ` 出去 ** 。

JavaScript对象是引用关系，如果 ` return ` 的对象引用了外部的一个对象，那这个对象就是共享的，任何一方修改都会同步。

###  使用 ` props ` 传递数据

组件不仅要把模板的内容进行复用，更重要的是组件间进行通信。

通常父组件的模板中包含子组件，父组件要正向地向子组件传递数据或参数，子组件接收后根据参数的不同渲染不同的内容或者执行操作。这个正向传递数据的过程通过 `
props ` 来实现。

在组件中，使用选项 ` props ` 声明需要从父级接收的数据， ` props ` 的值可以是两种，一种是 **字符串数组** ，一种是 **对象**
。
```js
    
    
    <my-component message="来自父组件的数据"></my-component>
    
    props: ['message'],
    template: `<div>{{message}}</div>`,
    
```
` props ` 中声明的数据与组件 ` data ` 函数中 ` return ` 的数据主要区别就是 ` props ` 的数据来自父级，而 `
data ` 中的是组件自己的数据，作用域是组件本身，这两种数据都可以在模板 ` template ` 及计算属性 ` computed ` 和方法 `
methods ` 中使用。

由于HTML特性不区分大小写，当使用DOM模板时，驼峰命名的 ` props ` 名称要转为短横线分割命名。

```js    
    
    <my-component warning-text="提示信息"></my-component>
    
```
有时候，传递的数据并不是直接写死，而是来自父级的动态数据，这时可以使用指令 ` v-bind ` 动态绑定 ` props `
的值，当父组件的数据变化时，也会传递子组件。
```js
    
    
    <div id="app">
        <input type="text" v-model="parentMessage">
        <my-component :message="parentMessage"></my-component>
    </div>
    
    props: ['message'],
    template: `<div>{{message}}</div>`,
    
    data: {
        parentMessage: ''
    }
    
```
这里用 ` v-model ` 绑定了父级的数据 ` parentMessage ` ，当通过输入框任意输入时，子组件接收到的 `
props["message"] ` 也会实时响应，并更新组件模板。

###  单向数据流

业务中会经常遇到两种需要改变 ` prop `
的情况，一种是父组件传递初始值进来，子组件将它作为初始值保存起来，在自己的作用域下可以随意使用和修改。这种情况可以在组件 ` data `
内再声明一个数据，引用父组件的 ` prop ` 。
```js
    
    
    <div id="app">
        <my-component :init-count="1"></my-component>
    </div>
    
    Vue.component('my-component', {
        props: ['initCount'],
        template: `<div>{{count}}</div>`,
        data() {
            return {
                count:this.initCount
            }
        }
    });
 ```   

组件中声明了数据 ` count ` ，它在组件初始化时会获取来自父组件的 ` initCount ` ，之后就与之无关了，只用维护 ` count `
，这样就可以避免直接操作 ` initCount ` 。

另一种情况就是 ` prop ` 作为需要被转变的原始值传入，这种情况用计算属性就可以。
```js
    
    
    <div id="app">
        <my-component :width="100"></my-component>
    </div>
    
    Vue.component('my-component', {
        props: ['width'],
        template: `<div :style="style">组件内容</div>`,
        computed: {
            style: function () {
                return {
                    width: this.width + 'px'
                }
            }
        }
    });
 ```   

因为用CSS传递宽度要带单位（px），数值计算一般不带单位，所以统一在组件内使用计算属性。

> 在JavaScript中对象和数组时引用类型，指向同一个内存空间，所以 ` props ` 是对象和数组时，在子组件内改变是会影响父组件。

###  数组验证

当 ` prop ` 需要验证时，需要对象写法。

一般当组件需要提供给别人使用时，推荐都进行数据验证。比如某个数据必须是数字类型，如果传入字符串，就会在控制台弹出警告。
```js
    
    
    Vue.component('my-component', {
        props: {
            // 必须是数字
            propA: Number,
            // 必须是字符串或数字类型
            propB: [String, Number],
            // 布尔值，如果没有定义，默认值是true
            propC: {
                type: Boolean,
                default: true
            },
            // 数字，而且是必传
            propD: {
                type: Number,
                default: true
            },
            // 如果是数组或对象，默认值必须是一个函数来返回
            propE: {
                type: Array,
                default: function () {
                    return []
                }
            },
            // 自定义一个验证函数
            propF: {
                validator: function (value) {
                    return value > 10
                }
            }
        }
    });
```
验证的 ` type ` 类型可以是：

  * ` String `
  * ` Number `
  * ` Boolean `
  * ` Object `
  * ` Array `
  * ` Function `

` type ` 也可以是一个自定义构造器，使用 ` instanceof ` 检测。

###  组件通信

组件关系可分为父组件通信、兄弟组件通信、跨级组件通信。

####  自定义事件

当子组件需要向父组件传递数据时，就要用到自定义事件。

` v-on ` 除了监听DOM事件外，还可以用于组件之间的自定义事件。

JavaScript的设计模式——观察者模式方法：

  * ` dispatchEvent `
  * ` addEventListener `

Vue组件的子组件用 ` $emit() ` 来触发事件，父组件用 ` $on() ` 来监听子组件的事件。

父组件也可以直接在子组件的自定义标签上使用 ` v-on ` 来监听子组件触发的自定义事件。
```js
    
    
    <div id="app">
        <p>总数:{{total}}</p>
        <my-component
                @increase="handleGetTotal" @reduce="handleGetTotal"></my-component>
    </div>
    
    Vue.component('my-component', {
        template: `
            <div>
                <button @click="handleIncrease">+</button>
                <button @click="handlereduce">-</button>
            </div>
            `,
        data() {
            return {
                counter: 0
            }
        },
        methods: {
            handleIncrease: function () {
                this.counter++;
                this.$emit('increase', this.counter);
            },
            handlereduce: function () {
                this.counter--;
                this.$emit('reduce', this.counter)
            }
        }
    });
    
    new Vue({
        el: '#app',
        data: {
            total: 0
        },
        methods: {
            handleGetTotal: function (total) {
                this.total = total;
            }
        }
    });
```
在改变组件的 ` data "counter" ` 后，通过 ` $emit() ` 再把它传递给父组件，父组件用 ` @increase ` 和 `
@reduce ` 。 ` $emit() ` 方法的第一个参数是自定义事件的名称。

除了用 ` v-on ` 在组件上监听自定义事件外，也可以监听DOM事件，这时可以用 ` .native `
修饰符表示监听时一个原生事件，监听的是该组件的根元素。
```js
    
    
    <my-component @click:native="handleClick"></my-component>
    
```
####  使用 ` v-model `

Vue可以在自定义组件上使用 ` v-model ` 指令。
```js
    
    
    <my-component v-model="total"></my-component>
    
```
组件 ` $emit() ` 的事件名时特殊的 ` input ` ，在使用组件的父级，并没有在 ` <my-component> ` 上使用 `
@input="handler" ` ，而是直接用了 ` v-model ` 绑定的一个数据 ` total ` 。
```js
    
    
    <my-component @input="handleGetTotal"></my-component>
    
```
` v-model ` 还可以用来创建自定义的表单输入组件，进行数据双向绑定。
```js
    
    
    <div id="app">
        <p>总数：{{total}}</p>
        <my-component v-model="total"></my-component>
        <button @click="handleReduce">-</button>
    </div>
    
    Vue.component('my-component', {
        props: ['value'],
        template: `<input :value="value" @input="updateValue">`,
        methods: {
            updateValue: function () {
                this.$emit('input', event.target.value)
            }
        }
    });
    
    new Vue({
        el: '#app',
        data: {
            total: 10
        },
        methods: {
            handleReduce: function () {
                this.total--;
            }
        }
    });
```
实现这样一个具有双向绑定的 ` v-model ` 组件要满足下面两个要求：

  1. 接收一个 ` value ` 属性 
  2. 在有新的 ` value ` 时触发 ` input ` 事件 

####  非父子组件通信

在实际业务中，除了父子组件通信外，还有很多非父子组件通信的场景，非父子组件一般有两种， **兄弟组件** 和 **跨多级组件** 。

在 **Vue 1.x** 版本中，除了 ` $emit() ` 方法外，还提供了 ` ￥dispatch() ` 和 ` $broadcast() ` 。

` $dispatch() ` 用于向上级派发事件，只要是它的父级（一级或多级以上），都可以在Vue实例的 ` events ` 选项内接收。

此实例只在Vue 1.x版本中有效：
```js
    
    
    <div id="app">
        <p>{{message}}</p>
        <my-component></my-component>
    </div>
    
    Vue.component('my-component', {
        template: `<button @click="handleDispatch">派发事件</button>`,
        methods: {
            handleDispatch: function () {
                this.$dispatch('on-message', '来自内部组件的数据')
            }
        }
    });
    new Vue({
        el: '#app',
        data: {
            message: ''
        },
        events: {
            'on-message': function (msg) {
                this.message = msg;
            }
        }
    });
```
` $broadcast() ` 是由上级向下级广播事件，用法完全一致，方向相反。

这两种方法一旦发出事件后，任何组件都可以接收到，就近原则，而且会在第一次接收到后停止冒泡，除非返回 ` true ` 。

**这些方法在Vue 2.x版本中已废弃。**

在Vue 2.x中，推荐任何一个空的Vue实例作为中央事件总线（ ` bus ` ），也就是一个中介。
```js
    
    
    <div id="app">
        <p>{{message}}</p>
        <component-a></component-a>
    </div>
    
    var bus = new Vue();
    
    Vue.component('component-a', {
        template: `<button @click="handleEvent">传递事件</button>`,
        methods: {
            handleEvent: function () {
                bus.$emit('on-message', '来自组件component-a的内容')
            }
        }
    });
    var app = new Vue({
        el: '#app',
        data: {
            message: ''
        },
        mounted: function () {
            var _this = this;
            // 在实例初始化时，监听来自bus实例的事件
            bus.$on('on-message', function (msg) {
                _this.message = msg;
            })
        }
    });
```
首先创建了一个名为 ` bus ` 的空的Vue实例；然后全局定义了组件 ` component-a ` ；最后创建了Vue实例 ` app ` 。

在 ` app ` 初始化时，也就是在生命周期 ` mounted ` 钩子函数里监听了来自 ` bus ` 的事件 ` on-message `
，而在组件 ` component-a ` 中，点击按钮后会通过 ` bus ` 把事件 ` on-message ` 发出去。此时 ` app `
就会接收到来自 ` bus ` 的事件，进而在回调里完成自己的业务逻辑。

这种方法巧妙而轻量地实现了任何组件间的通信，包括父子、兄弟、跨级。

如果深入使用，可以扩展 ` bus ` 实例，给它添加 ` data ` 、 ` methods ` 、 ` computed `
等选项，这些都是可以公用的。

在业务中，尤其是协同开发时非常有用，因为经常需要共享一些通用的信息，比如用户登录的昵称、性别、邮箱等，还有用户的授权 ` token ` 等。

只需在初始化时让 ` bus ` 获取一次，任何时间、任何组件就可以从中直接使用，在单页面富应用（SPA）中会很实用。

除了中央事件总线 ` bus ` 外，还有两种方法可以实现组件间通信：父链和子组件索引。

####  父链

在子组件中，使用 ` this.$parent ` 可以直接访问该组件的父实例或组件，父组件也可以通过 ` this.$children `
访问它所有的子组件，而且可以递归向上或向下无限访问，直到根实例或最内层的组件。
```js
    
    
    <div id="app">
        <p>{{message}}</p>
        <component-a></component-a>
    </div>
    
    Vue.component('component-a', {
        template: `<button @click="handleEvent">通过父链直接修改数据</button>`,
        methods: {
            handleEvent: function () {
                this.$parent.message = '来自组件component-a的内容'
            }
        }
    });
    var app = new Vue({
        el: '#app',
        data: {
            message: ''
        }
    });
    
```
尽管Vue允许这样操作，但在业务中，子组件应该尽可能地避免依赖父组件的数据，更不应该去主动修改它的数据，因为这样使得父子组件紧耦合，只看父组件，很难理解父组件的状态，因为它可能被任意组件修改，理想状态下，只有组件自己能修改它的状态。

**父子组件最好还是通过` props ` 和 ` $emit() ` 来通信。 **

####  子组件索引

当子组件较多时，通过 ` this.$children ` 来遍历出需要的一个组件实例是比较困难的，尤其是组件动态渲染时，它们的序列是不固定的。

Vue提供了子组件索引的方法，用特殊的属性 ` ref ` 来为子组件指定一个索引名称。
```js
    
    
    <div id="app">
        <button @click="handleRef">通过ref获取子组件实例</button>
        <component-a ref="comA"></component-a>
    </div>
    
    Vue.component('component-a', {
        template: `<div>子组件</div>`,
        data() {
            return {
                message: '子组件内容'
            }
        },
    });
    var app = new Vue({
        el: '#app',
        methods: {
            handleRef: function () {
                // 通过$refs来访问指定的实例
                var msg = this.$refs.comA.message;
                console.log(msg);
            }
        }
    });
```
在父组件模板中，子组件标签上使用 ` ref ` 指定一个名称，并在父组件内通过 ` this.$refs ` 来访问指定名称的子组件。

> ` $refs ` 只在组件渲染完成后才填充，并且它是非响应式的。它仅仅作为一个直接访问子组件的应急方案，应当避免在模板或计算属性中使用 ` $refs
> ` 。

Vue 2.x将 ` v-el ` 和 ` v-ref ` 合并成 ` ref ` ，Vue会自动去判断是普通标签还是组件。

##  使用 ` slot ` 分发内容

当需要让组件组合使用，混合父组件的内容与子组件的模板时，就会用到 ` slot ` ，这个过程叫做 **内容分发** 。

  * ` <app> ` 组件不知道它的挂载点会有什么内容。挂载点的内容是由 ` <app> ` 的父组件决定的。 
  * ` <app> ` 组件很可能有它自己的模板。 

` props ` 传递数据、 ` events ` 触发事件和 ` slot `
内容分发就构成了Vue组件的3个API来源，再复杂的组件也是由这3部分构成。

###  作用域

父组件中的模板：
```js
    
    
    <child-component>
        {{message}}
    </child-component>
    
```
这里的 ` message ` 就是一个 ` slot ` ，但是它绑定的是父组件的数据，而不是组件 ` <child-component> ` 的数据。

父组件模板的内容是在父组件作用域内编译，子组件模板的内容是在子组件作用域内编译。
```js
    
    
    <div id="app">
        <child-component v-modle="showChild"></child-component>
    </div>
    
    Vue.component('child-component', {
        template: `<div>子组件1</div>`,
    });
    var app = new Vue({
        el: '#app',
        data: {
            showChild: true
        }
    });
    
```
这里的状态 ` showChild ` 绑定的是父组件的数据。

在子组件上绑定数据：
```js
    
    
    <div id="app">
        <child-component></child-component>
    </div>
    
    Vue.component('child-component', {
        template: `<div v-model="showChild">子组件</div>`,
        data() {
            return {
                showChild: true
            }
        }
    });
    var app = new Vue({
        el: '#app',
    });
    
```
因此， **` slot ` 分发的内容，作用域是在父组件上 ** 。

###  单个 ` slot `

在子组件内使用特殊的 ` <slot> ` 元素就可以为这个组件开启一个 ` slot `
（插槽），在父组件模板里，插入在子组件标签内的所有内容将替代子组件的 ` <slot> ` 标签及它的内容。
```js
    
    
    <div id="app">
        <child-component>
            <p>分发的内容</p>
            <p>更多分发的内容</p>
        </child-component>
    </div>
    
    Vue.component('child-component', {
        template: `
        <div>
            <slot>
               <p>如果没有父组件插入内容，我将作为默认出现。</p>
            </slot>
        </div>
                `,
    });
    var app = new Vue({
        el: '#app',
    });
    
```
子组件 ` child-component ` 的模板内定义了一个 ` <slot> ` 元素，并且用一个 ` <p> ` 作为默认的内容，在父组件没有使用
` slot ` 时，会渲染这段默认的文本；如果写入了 ` slot ` ，就会替换整个 ` <slot> ` 。

> 子组件 ` <slot> ` 内的备用内容，它的作用域是子组件本身。

###  具名 ` Slot `

给 ` <slot> ` 元素指定一个 ` name ` 后可以分发多个内容，具名 ` slot ` 可以与单个 ` slot ` 共存。
```js
    
    
    <div id="app">
        <child-component>
            <h2 slot="header">标题</h2>
            <p>正文的内容</p>
            <p>更多正文的内容</p>
            <div slot="footer">底部信息</div>
        </child-component>
    </div>
    
    Vue.component('child-component', {
        template: `
    <div class="container">
        <div class="header">
            <slot name="header"></slot>
        </div>
        <div class="main">
            <slot></slot>
        </div>
        <div class="footer">
            <slot name="footer"></slot>
        </div>
    </div>    
        `,
    });
    var app = new Vue({
        el: '#app',
    });
```
子组件内声明了3个 ` <slot> ` 元素，其中在 ` <div class="main"> ` 内的 ` <slot> ` 没有使用 ` name `
特性，它将作为默认 ` slot ` 出现，父组件没有使用 ` slot ` 特性的元素与内容都将出现在这里。

如果没有指定默认的匿名 ` slot ` ，父组件内多余的内容都将被抛弃。

**在组合使用组件时，内容分发API至关重要。**

###  作用域插槽

作用域插槽是一种特殊的 ` slot ` ，使用一个可以复用的模板替换已渲染元素。
```js
    
    
    <div id="app">
        <child-component>
            <template scope="props">
                <p>来自父组件的内容</p>
                <p>{{props.msg}}</p>
            </template>
        </child-component>
    </div>
    
    Vue.component('child-component', {
        template: `
    <div class="container">
        <slot msg="来自子组件的内容"></slot>
    </div> 
        `,
    });
    var app = new Vue({
        el: '#app',
    });
    
```
子组件的模板，在 ` <slot> ` 元素上有一个类似 ` props ` 传递数据给组件的写法 ` msg="xxx" ` ，将数据传递到插槽。

父组件中使用了 ` <template> ` 元素，而且拥有一个 ` scope="props" ` 的特性，这里的 ` props ` 是一个临时变量。

` template ` 内可以通过临时变量 ` props ` 访问来自子组件插槽的数据 ` msg ` 。

**作用域插槽更具代表性的用例是列表组件，允许组件自定义应该如何渲染列表每一项。**
```js
    
    
    <div id="app">
        <my-list :book="books">
            <!--作用域插槽也可以是具名的Slot-->
            <template slot="book" scope="props">
                <li>{{props.bookName}}</li>
            </template>
        </my-list>
    </div>
    
    Vue.component('my-list', {
        props: {
            books: {
                type: Array,
                default: function () {
                    return [];
    
                }
            }
        },
        template: `
    <ul>
        <slot name="book" v-for="book in books" :book-name="book.name"></slot>
    </ul>
        `,
    });
    
```
子组件 ` my-list ` 接收一个来自父级的 ` prop ` 数组 ` books ` ，并且将它在 ` name ` 为 ` book ` 的 `
slot ` 上使用 ` v-for ` 指令循环，同时暴露一个变量 ` bookName ` 。

**作用域插槽的使用场景是既可以复用子组件的` slot ` ，又可以使 ` slot ` 内容不一致。 **

###  访问 ` slot `

Vue 2.x提供了用来访问被 ` slot ` 分发的内容的方法 ` $slots ` 。
```js
    
    
    <div id="app">
        <child-component>
            <h2 slot="header">标题</h2>
            <p>正文的内容</p>
            <p>更多正文的内容</p>
            <div slot="footer">底部信息</div>
        </child-component>
    </div>
    
    Vue.component('child-component', {
        template: `
    <div class="container">
        <div class="header">
            <slot name="header"></slot>
        </div>
        <div class="main">
            <slot></slot>
        </div>
        <div class="footer">
            <slot name="footer"></slot>
        </div>
    </div>    
        `,
        mounted: function () {
            var header = this.$slots.header;
            var main = this.$slots.default;
            var footer = this.$slots.footer;
            console.log(footer);
            console.log(footer[0].elm.innerHTML);
        }
    });
    var app = new Vue({
        el: '#app',
    });
```
通过 ` $slots ` 可以访问某个具名 ` slot ` , ` this.$slots.default ` 包括了所有没有被包含在具名 ` slot
` 中的节点。

##  组件高级用法

###  递归组件

给组件设置 ` name ` 选项，组件在它的模板内可以递归地调用自己。
```js
    
    
    <div id="app">
        <child-component :count="1"></child-component>
    </div>
    
    Vue.component('child-component', {
        name: 'child-component',
        props: {
            count: {
                type: Number,
                default: 1
            }
        },
        template: `
    <div class="child">
        <child-component :count="count+1" v-if="count<3"></child-component>
    </div>
        `,
    });
    
```
组件递归使用可以用来开发一些具有未知层级关机的独立组件，比如级联选择器和树形控件等。

###  内联模板

组件的模板一般都是在 ` template ` 选项内定义的，Vue提供了一个内联模板的功能，在使用组件时，给组件标签使用 ` inline-
template ` 特性，组件就会把它的内容当做模板，而不是把它当内容分发，这让模板更灵活。
```js
    
    
    <div id="app">
        <child-component inline-template>
            <div>
                <h2>在父组件中定义子组件的模板</h2>
                <p>{{message}}</p>
                <p>{{msg}}</p>
            </div>
        </child-component>
    </div>
    
    Vue.component('child-component', {
        data() {
            return {
                msg: '在子组件中声明的数据'
            }
        }
    });
    var app = new Vue({
        el: '#app',
        data: {
            message: '在父组件中声明的数据'
        }
    });
```
在父组件中声明的数据 ` message ` 和子组件中声明的数据 ` msg ` ，两个都可以渲染（如果同名，优先使用子组件的数据）。
**这是内联模板的缺点，就是作用域比较难理解，如果不是非常特殊的场景，建议不要轻易使用内联模板** 。

###  动态组件

Vue.js提供了一个特殊的元素 ` <component> ` 用来动态地挂载不同的组件，使用 ` is ` 特性来选择要挂载的组件。
```js
    
    
    <div id="app">
        <button @click="handleChangeView('A')">切换到A</button>
        <button @click="handleChangeView('B')">切换到B</button>
        <button @click="handleChangeView('C')">切换到C</button>
        <component :is="currentView"></component>
    </div>
    
    var app = new Vue({
        el: '#app',
        data: {
            currentView: 'comA'
        },
        components: {
            comA: {
                template: `<div>组件A</div>`
            },
            comB: {
                template: `<div>组件B</div>`
            },
            comC: {
                template: `<div>组件C</div>`
            },
        },
        methods: {
            handleChangeView: function (component) {
                this.currentView = 'com' + component
            }
        }
    });
```
可以直接绑定在组件对象上：
```js
    
    
    <div id="app">
        <component :is="currentView"></component>
    </div>
    
    var Home = {
        template: `<p>Welcome home!</p>`
    };
    
    var app = new Vue({
        el: '#app',
        data: {
            currentView: Home
        }
    });
    
```
###  异步组件

Vue.js允许将组件定义为一个工厂函数，动态地解析组件。

Vue.js只在组件需要渲染时触发工厂函数，并且把结果缓存起来，用于后面的再次渲染。
```js
    
    
    <div id="app">
        <child-component></child-component>
    </div>
    
    Vue.component('child-component', function (resolve, reject) {
        window.setTimeout(function () {
            resolve({
                template: `<div>我是异步渲染的！</div>`
            })
        }, 1000)
    });
    
    var app = new Vue({
        el: '#app',
    });
    
```
工厂函数接收一个 ` resolve ` 回调，在收到从服务器下载的组件定义时调用。也可以调用 ` reject(reason) ` 指示加载失败。

##  其他

###  ` $nextTick `

**异步更新队列**

Vue在观察到数据变化时并不是直接更新DOM，而是开启一个队列，并缓冲在同一个事件循环中发生的所有数据变化。在缓冲时会去除重复数据，从而避免不必要的计算和DOM操作。然后，在一下个事件循环
` tick ` 中，Vue刷新队列并执行实际（已去重的）工作。

Vue会根据当前浏览器环境优先使用原生的 ` Promise.then ` 和 ` MutationObserver ` ，如果都不支持，就会采用 `
setTimeout ` 代替。

**` $nextTick ` 就是用来确定什么时候DOM更新已经完成 ** 。
```js
    
    
    <div id="app">
        <div id="div" v-if="showDiv">这是一段文本</div>
        <button @click="getText">获取div内容</button>
    </div>
    
    var app = new Vue({
        el: '#app',
        data: {
            showDiv: false
        },
        methods: {
            getText: function () {
                this.showDiv = true;
                this.$nextTick(function () {
                    var text = document.getElementById('div');
                    console.log(text.innerHTML);
                })
            }
        }
    });
```
###  ` X-Templates `

Vue提供了另一种定义模板的方式，在 ` <script> ` 标签中使用 ` text/x-template ` 类型，并且指定一个 ` id `
，将这个 ` id ` 赋给 ` template ` 。
```js
    
    
    <div id="app">
        <my-component></my-component>
        <script type="text/x-template" id="my-component">
            <div>这是组件的内容</div>
        </script>
    </div>
    
    Vue.component('my-component', {
        template: `#my-component`,
    });
    var app = new Vue({
        el: '#app',
    });
    
```
###  手动挂载实例

在一些非常特殊的情况下，需要动态地创建Vue实例，Vue提供了 ` Vue.extend ` 和 ` $mount ` 两个方法来手动挂载一个实例。

` Vue.extend ` 是基础Vue构造器，创建一个“子类”，参数是一个包含组件选项的对象。

如果Vue实例在实例化时没有收到 ` el ` 选项，它就处于“未挂载”状态，没有关联的DOM元素。可以使用 ` $mount `
手动地挂载一个未挂载的实例。这个方法返回实例自身，因而可以链式调用其他实例方法。
```js
    
    
    <div id="app"></div>
    
    var MyComponent = Vue.extend({
        template: `<div>Hello {{name}}</div>`,
        data() {
            return {
                name: 'Andy'
            }
        }
    });
    new MyComponent().$mount('#app');
```
除了以上写法外，还有两种写法：
```js
    
    
    new MyComponent().$mount("#app");
    
    new MyComponent({
        el: '#app'
    })
    
```
**手动挂载实例（组件）是一种比较极端的高级用法，在业务中几乎用不到，只在开发一些复杂的独立组件时可能会使用。**

