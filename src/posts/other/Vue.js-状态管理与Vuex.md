---
date: 2023-02-25
category:
    - vue.js
tag:
    - vue.js
    - 前端
    - 前端框架
    - javascript
---
 # Vue.js-状态管理与Vuex
> 学习笔记： [ 状态管理与Vuex ]()

##  状态管理与Vuex

非父子组件（跨级组件和兄弟组件）通信时，使用了 ` bus ` （中央事件总线）的一个方法，用来触发和接收事件，进一步起到通信的作用。

一个组件可以分为数据（ ` model ` ）和视图（ ` view ` ），数据更新时，视图也会自动更新。在视图中又可以绑定一个事件，它们触发 `
methods ` 里指定的方法，从而可以改变数据、更新视图，这是一个组件基本的运行模式。

    
    
    const store = new Vuex.Store({});
    

仓库 ` store ` 包含了应用的数据（状态）和操作过程。Vuex里的数据都是响应式的，任何组件使用同一 ` store ` 的数据时，只要 `
store ` 的数据变化，对应的组件也会立即更新。

数据保存在Vuex选项的 ` state ` 字段内。

    
    
    const store = new Vuex.Store({
        state: {
            count: 0
        }
    });
    

在任何组件内，可以直接通过 ` $store.state.count ` 读取。

    
    
    <template>
        <div>
            <h1>首页</h1>
            {{$store.state.count}}
        </div>
    </template>
    

直接卸载 ` template ` 里显得有点乱，可以用一个计算属性来显示：

    
    
    <div>
        <h1>首页</h1>
        {{count}}
    </div>
    
    export default {
        computed: {
            count() {
                return $store.state.count;
            }
        }
    }
    

在组件内来自 ` store ` 的数据只能读取，不能手动修改，修改 ` store ` 中数据的唯一途径是显式地提交 ` mutations ` 。

` mutations ` 是Vuex的第二个选项，用来直接修改 ` state ` 里的数据。

在组件内，通过 ` this.$store.commit ` 方法来执行 ` mutations ` 。

` mutations ` 还可以接受第二个参数，可以是数字、字符串或对象等类型。

**ES6语法**

函数的参数可以设定默认值，当没有传入该参数时，使用设置的值。

    
    
    increment(state,n=1)等同于：
        increment(state,n){
            n=n||1;
        }

提交 ` mutations ` 的另一种方式是直接使用包含 ` type ` 属性的对象。

> ` mutations ` 里尽量不要异步操作数据，否则组件在 ` commit ` 后数据不能立即改变，而且不知道什么时候会改变。

###  高级用法

Vuex还有其他3个选项可以使用： ` getter ` 、 ` actions ` 、 ` modules ` 。

` getter ` 能将 ` computed ` 的方法提取出来，也可以依赖其他的 ` getter ` ，把 ` getter ` 作为第二个参数。

` action ` 与 ` mutation ` 很像，不同的是 ` action ` 里面提交的是 ` mutation `
，并且可以一步操作业务逻辑。

` action ` 在组件内通过 ` $store.dispatch ` 触发。

` modules ` 用来将 ` store ` 分割到不同模块，当项目足够大时， ` store ` 里的 ` state ` 、 ` getters
` 、 ` mutations ` 、 ` actions ` 会非常多，使用 ` modules ` 可以把它们写到不同的文件中。

` module ` 的 ` mutation ` 和 ` getter ` 接收的第一个参数 ` state ` 是当前模块的状态。在 ` actions
` 和 ` getters ` 中还可以接收一个参数 ` rootState ` ，来访问根节点的状态。

##  实战：中央事件总线插件 ` vue-bus `

中央事件总线 ` bus ` 作为一个简单的组件传递事件，用于解决跨级和兄弟组件通信的问题。

` vue-bus ` 插件给Vue添加一个属性 ` $bus ` ，并代理 ` $emit ` 、 ` $on ` 、 ` $off ` 三个方法。

**ES6语法**

> ` emit(event,..args) ` 中的 ` ... ` 是函数参数的解构。因为不知道组件会传递多少个参数进来，使用 ` ...args `
> 可以把从当前参数到最后的参数都获取到。

使用 ` vue-bus ` 有两点需要注意：

  1. 第一是 ` $bus.on ` 应该在 ` created ` 钩子内使用，如果在 ` mounted ` 使用，它可能接收不到其他组件来自 ` created ` 钩子内发出的事件； 
  2. 第二点是使用了 ` $bus.on ` 在 ` beforeDestroy ` 钩子里应该再使用 ` $bus.off ` 解除，因为组件销毁后，就没有必要把监听的句柄存储在 ` vue-bus ` 中。 

##  Vue插件

注册插件需要一个公开的方法 ` install ` ，它的第一个参数时Vue构造器，第二个参数是一个可选的选项对象。

<p data-height="350" data-theme-id="0" data-slug-hash="RJVOXd" data-default-
tab="js" data-user="whjin" data-embed-version="2" data-pen-title="Vue插件"
class="codepen">See the Pen [ Vue插件 ]() by whjin ( [ @whjin ]() ) on [ CodePen
]() .</p>  


##  前端路由与 ` vue-router `

SPA的核心就是前端路由，对于一个网址，每次GET或POST等请求在服务端有一个专门的正则配置列表，然后匹配到具体的一条路径后，分发到不同的Controller，进行各种操作，最终将
` html ` 或数据返回给前端，这样就完成了一次IO。

前端路由，即由前端来维护一个路由规则。实现方式有两种；

  1. 一种是利用 ` url ` 的 ` hash ` ，就是常说的锚点（ ` # ` ），JavaScript通过 ` hashChange ` 事件来监听 ` url ` 的改变； 
  2. 另一种就是HTML5的 ` history ` 模式，它使 ` url ` 看起来像普通网站那样，以 ` / ` 分割，没有 ` # ` ，但也没并没有跳转，不过使用这种模式需要服务端支持，服务端在接收到所有的请求后，都指向同一个 ` html ` 文件，不然会出现 **404** 。 

因此，SPA只有一个 ` html ` ，整个网站所有的内容都在这个 ` html ` 里，通过JavaScript来处理。

> 如果要独立开发一个前端路由，需要考虑到页面的可插拔、生命周期、内存管理等问题。

###  ` vue-router `

` vue-router ` 的实现原理与 **通过` is ` 特性实现动态组件 ** 的方法类似，路由不同的页面事实上就是动态加载不同的组件。

创建一个数组来指定路由匹配列表，每一个路由映射一个组件：

    
    
    const Routers = [
        {
            path: '/index',
            component: (resolve) => require(['./views/index.vue'], resolve)
        },
        {
            path: '/about',
            component: (resolve) => require(['./views/about.vue'], resolve)
        }
    ];
    

Routers里每一项的 ` path ` 属性就是指定当前匹配的路径， ` component ` 是映射的组件。

` webpack ` 会把每一个路由都打包为一个 ` js ` 文件，在请求道该页面时，再去加载这个页面的 ` js `
，也就是异步实现的懒加载（按需加载）。这样做的好处是不需要在打开首页的时候就把所有的页面内容全部加载进来，只在访问时才加载。

> 使用了异步路由后，变移除的每个页面的 ` js ` 都叫做 ` chunk ` （块），它们命名默认是 ` 0.main.js ` 、 `
> 1.main.js ` ...  
>  可以在 ` webpack ` 配置的出口 ` output ` 里通过设置 ` chunkFilename ` 字段修改 ` chunk ` 命名。
    
    
    output: {
        publicPath: "/dist/",
            filename: "[name].js",
            chunkFilename: "[name].chunk.js"
    }

有了 ` chunk ` 后，在每个页面（ ` .vue ` 文件）里写的样式也需要配置后才会打包进 ` main.css `
，否则仍然会通过JavaScript动态创建 ` <style> ` 标签的形式写入。

    
    
    const RouterConfig = {
        //使用HTML5的History路由模式
        mode: 'history',
        routes: Routers
    };
    
    const router = new VueRouter(RouterConfig);
    
    new Vue({
        el: "#app",
        router: router,
        render: h => {
            return h(App)
        }
    });
    

在RouterConfig里设置 ` mode ` 为 ` history ` 会开启HTML5的History路由模式，通过 ` / `
设置路径。如果不配置 ` mode ` ，就会使用 ` # ` 来设置路径。

开启History路由，在生产环境时必须进行配置，将所有路由都指向同一个 ` html ` ，或设置 **404** 页面，否则刷新时页面就会出现
**404** 。

在路由列表里，可以在最后新加一项，当访问的路径不存在时，重定向到首页：

    
    
    {
        path: '*',
        redirect: '/index'
    }
    

路由列表的 ` path ` 可以带参数，比如 ` /user/123 ` ，其中用户ID ` 123 `
是动态的，但它们路由到同一个页面，在这个页面里，期望获取这个ID，然互殴请求相关数据。

###  跳转

` vue-router ` 有两种跳转页面的方法，第一种是使用内置的 ` <router-link> ` 组件，它会被渲染为一个 ` <a> ` 标签。

    
    
    <template>
        <div>
            <h1>首页</h1>
            <router-link to="/about">跳转到about</router-link>
        </div>
    </template>
    

它的用法与一般的组件一样， ` to ` 是一个 ` prop ` ，指定需要跳转的路径，也可以用 ` v-bind ` 动态设置。

使用 ` <router-link> ` ，在HTML5的History模式下会拦截点击，避免浏览器重新加载页面。

<router-view>还有其他一些 ` prop ` ，常用的有：

  * ` tag ` 可以指定渲染成什么标签，比如 ` <router-link to="/about" tag="li"> ` 渲染的结果就是 ` <li> ` ，而不是 ` <a> `
  * ` replace ` 使用 ` replace ` 不会留下History记录，所以导航后不能用后退键返回上一个页面，如 ` <router-link to="/about" replace> `
  * ` active-class ` 当 ` <router-link> ` 对应的路由匹配成功时，会自定给当前元素设置一个名为 ` router-link-active ` 的 ` class ` ，设置 ` prop:active-class ` 可以修改默认的名称。在做类似导航栏时，可以使用该功能高亮显示当前页面对应的导航栏单项，但是一般不会修改 ` active-class ` ，直接使用默认值 ` router-link-active ` 。 

有时候，跳转页面可能需要在JavaScript中进行，类似于 ` window.location.href ` 。这时可以使用第二种跳转方法，使用 `
router ` 实例的方法。

    
    
    <template>
        <div>
            <h1>介绍页</h1>
            <button @click="handleRouter">跳转到user</button>
        </div>
    </template>
    
    <script>
        export default {
            methods: {
                handleRouter() {
                    this.$router.push('/user/123');
                }
            }
        }
    </script>
    

` $router ` 还有其他一些方法：

  * ` replace ` 类似于 ` <router-link> ` 的 ` replace ` 功能，它不会向 ` history ` 添加新纪录，而是替换掉当前的 ` history ` 记录，如 ` this.$router.replace('/user/123') `
  * ` go ` 类似于 ` window.history.go() ` ，在 ` history ` 记录中向前或后退多少步，参数是整数 

###  高级用法

**在SPA项目中，如何修改网页的标题？**

在页面发生路由变化时，统一设置。

` vue-router ` 提供了导航钩子 ` beforeEach ` 和 ` afterEach `
，它们会在路由即将改变前和改变后触发，所以设置标题可以在 ` beforeEach ` 钩子完成。

<p data-height="365" data-theme-id="0" data-slug-hash="gKRaLm" data-default-
tab="js" data-user="whjin" data-embed-version="2" data-pen-title="vue-
router导航钩子" class="codepen">See the Pen [ vue-router导航钩子 ]() by whjin ( [
@whjin ]() ) on [ CodePen ]() .</p>  


导航钩子有3个参数：

  * ` to ` 即将要进入的目标的路由对象 
  * ` from ` 当前导航即将要离开的路由对象 
  * ` next ` 调用该方法后，才能进入下一个钩子 

路由列表的 ` meta ` 字段可以自定义一些信息，将每个页面的 ` title ` 写入 ` meta ` 来统一维护， ` beforeEach `
钩子可以从路由对象 ` to ` 里获取 ` meta ` 信息，从而改变标题。

某些页面需要校验是否登录，如果登录就可以访问，否则跳转到登录页。通过 ` localStorage ` 来简单判断是否登录。

    
    
    router.beforeEach((to, from, next) => {
        if (window.localStorage.getItem('token')) {
            next()
        } else {
            next('/login')
        }
    });
    

` next() ` 的参数设置为 ` false ` ，可以取消导航，设置为具体的路径可以导航到指定的页面。

##  使用webpack构建

webpack的主要适用场景时单页面富应用（SPA）。SPA通过是由一个 ` html ` 文件和一堆按需加载的 ` js ` 文件组成。

` export ` 和 ` import ` 是用来导出和导入模块的。一个模块就是一个 ` js `
文件，它拥有独立的作用域，里面定义的变量外部是无法获取的。

在 ` module ` 对象的 ` rules ` 属性中可以指定一系列的 ` loaders ` ，每一个 ` loader ` 都必须包含 `
test ` 和 ` use ` 两个选项。

当 ` webpack ` 编译过程中遇到 ` require() ` 或 ` import ` 语句导入一个后缀名为 ` .css `
的文件时，先将它通过 ` css-loader ` 转换，再通过 ` style-loader ` 转换，然后继续打包。 ` use `
选项的值可以是数组或字符串，如果是数组，它的编译顺序就是从后往前。

> webpack的主要核心部分包括 **入口（Entry）** 、 **出口（Output）** 、 **加载器（Loaders）** 、
> **插件（Plugin）** 。

##  单文件组件与 ` vue-loader `

` <style> ` 标签使用 ` scoped ` 属性，表示当前的CSS只在这个组件有效，如果不加，name ` div ` 的样式会应用到整个项目。

使用 ` .vue ` 文件需要先安装 ` vue-loader ` 、 ` vue-style-loader `
等加载器并做配置。如果要使用ES6语法，还需要安装 ` babel ` 和 ` babel-loader ` 等加载器。

<p data-height="465" data-theme-id="0" data-slug-hash="NzjNgp" data-default-
tab="js" data-user="whjin" data-embed-version="2" data-pen-title="Vue-
webpack.config.js" class="codepen">See the Pen [ Vue-webpack.config.js ]() by
whjin ( [ @whjin ]() ) on [ CodePen ]() .</p>  


新建 ` .babelrc ` 文件，并写入 ` babel ` 的配置，webpack会依赖此配置文件来使用 ` babel ` 编译ES6代码。

    
    
    {
      "presets": ["es2015"],
      "plugins": ["transform-runtime"],
      "comments": false
    }
    

**每个` .vue ` ** 文件代表一个组件，组件之间可以相互依赖。

**ES语法：**

` => ` 是箭头函数

    
    
    render: h=>h(App)等同于
        render: function(h) {
            return h(App)
        }
        
    也等同于：
        render: h=>{
            return h(App)
        }
        

箭头函数里的 ` this ` 指向与普通函数不一样，箭头函数体内的 ` this ` 对象就是定义时所在的对象，而不是使用时所在的对象。

