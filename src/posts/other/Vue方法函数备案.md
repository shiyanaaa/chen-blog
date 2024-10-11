---
date: 2023-09-08
category:
    - vue.js
tag:
    - vue.js
---
 # Vue方法函数备案
[ 文章 ]() 已经发布在个人博客，不断进行更新欢迎收藏订阅，或者提出批评意见。

> 有一些方法函数可能并不经常使用，但是遇到特定场景需要的时候却想不起来，所以需要把平时碰到的这些方法和函数进行备案，在需要的时候可以查询。

  1. [ 字符串反转 ]()
  2. [ Todos ]()
  3. [ 复选表单 ]()
  4. [ 动态选项，用 v-for 渲染 ]()
  5. [ 指令实例属性 ]()
  6. [ 对象字面量 ]()
  7. [ MVVM 数据绑定 ]()
  8. [ 利用v-if或者v-show进行条件判定 ]()
  9. [ Directive ]()
  10. [ 动态组件 ]()
  11. [ 使用script或template标签 ]()
  12. [ 使用props ]()
  13. [ 使用script或template标签 ]()

####  字符串反转

    
    
    reverseMessage: function () {
        this.msg = this.msg.split('').reverse().join('')
    }

####  Todos

    
    
    <div id="app">
        <input v-model="newTodo" v-on:keyup.enter="addTodo">
        <ul>
            <li v-for="(todo,index) in todos">
                <span>{{todo.text}}</span>
                <button v-on:click="removeTodo(index)">X</button>
            </li>
        </ul>
    </div>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <!--<script src="https://cdn.bootcss.com/vue-router/2.7.0/vue-router.js"></script>-->
    <script>
        new Vue({
            data: {
                newTodo: '',
                todos: [
                    {text: 'Add some todos'}
                ]
            },
            methods: {
                addTodo: function () {
                    var text = this.newTodo.trim();
                    if (text) {
                        this.todos.push({text: text});
                        this.newTodo = ''
                    }
                },
                removeTodo: function (index) {
                    this.todos.splice(index, 1)
                }
            }
        }).$mount('#app')
    </script>

####  复选表单

    
    
    <div id="app">
        <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
        <label for="jack">Jack</label>
        <input type="checkbox" id="john" value="john" v-model="checkedNames">
        <label for="john">John</label>
        <input type="checkbox" id="mike" value="mike" v-model="checkedNames">
        <label for="mike">Mike</label>
        <br>
        <span>Checked names: {{checkedNames}}</span>
    </div>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                checkedNames:[]
            }
        })
    </script>

####  动态选项，用 v-for 渲染

    
    
    <div id="app">
        <select v-model="selected">
            <option v-for="option in options" v-bind:value="option.value">
                {{option.text}}
            </option>
        </select>
        <br>
        <span>Selected: {{selected}}</span>
    </div>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                selected:'A',
                options:[
                    {text:'One',value:'A'},
                    {text:'Two',value:'B'},
                    {text:'Three',value:'C'}
                ]
            }
        })
    </script>

###  指令实例属性

    
    
    <div id="app">
        <div id="demo" v-demo:hello.a.b="msg"></div>
    </div>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        Vue.directive('demo', {
            bind() {
                document.write('demo bound! This is a test dialog.')
            },
            update(value) {
                this.el.innerHTML =
                    `name - ` + this.name + `<br>` +
                    `expression - ` + this.expression + `<br>` +
                    `argument - ` + this.arg + `<br>` +
                    `modifiers - ` + JSON.stringify(this.modifiers) + `<br>` +
                    `value - ` + value
            }
        });
    
        var vm = new Vue({
            el: '#app',
            data: {
                msg: 'Hello Vue.js!'
            }
        })
    </script>

####  对象字面量

    
    
    <div id="app">
        <div v-demo="styleObj"></div>
    </div>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        Vue.directive('demo', () => {
            console.log(styleObj.color);
            console.log(styleObj.text)
        });
        var styleObj = {
            color: 'red',
            text: 'Hello!'
        };
        var vm = new Vue({
            el: '#app',
            data: {
                styleObj: styleObj
            }
        })
    </script>

####  MVVM 数据绑定

    
    
    <!-- 指令 -->
    <span v-text="msg"></span>
    <!-- 插值 -->
    <span>{{msg}}</span>
    <!-- 双向绑定 -->
    <input v-model="msg"> 

####  利用v-if或者v-show进行条件判定

    
    
    <div id="app">
        <section v-if="loginStatus">
            输入您的姓名:<input type="text" v-model="name">
            <button @click="say">欢迎点击</button>
            <button @click="switchLoginStatus">退出登录</button>
        </section>
    
        <section v-if="!loginStatus">
            登录用户:<input type="text">
            登录密码:<input type="password">
            <button @click="switchLoginStatus">登录</button>
        </section>
    </div>
    
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        var vm = new Vue({
            data: {
                name: '_Appian',
                loginStatus: true
            },
            methods: {
                say: function () {
                    alert('欢迎' + this.name)
                },
                switchLoginStatus: function () {
                    this.loginStatus = !this.loginStatus;
                }
            }
        }).$mount('#app')
    </script>

####  Directive

> 对 Todo List 输入的内容进行校验（表单校验）。基本逻辑就在在 ` bind ` 阶段的时候就绑定事件，然后根据 ` update `
> 时候传入的 minlength 值来进行判断。

**Directive 基本结构如下：**

    
    
    Vue.directive("minlength", {
        bind: function () {
        },
        update: function (value) {
        },
        unbind: function () {
        }
    });
    
    
    Vue.directive("minlength", {
        bind: function () {
            var self = this,
                el = this.el;
            el.addEventListener("keydown", function (e) {
                if (e.keyCode === 13) {
                    if (el.value.length < self.minlength) {
                        e.preventDefault();
                    }
                }
            });
            var submit = el.parentNode.querySelector("button,[type='submit']");
            submit.disabled = true;
            el.addEventListener("keyup", function (e) {
                submit.disabled = (el.value.length < self.minlength);
            })
        },
        update: function (value) {
            this.minlength = parseInt(value);
        },
        unbind: function () {
    
        }
    });

####  动态组件

    
    
    <div id="app">
        <button id="home">Home</button>
        <button id="posts">Posts</button>
        <button id="archive">Archive</button>
        <br>
        <component :is="currentView"></component>
    </div>
    
    
    var vm = new Vue({
        data: {
            currentView: "home"
        },
        components: {
            home: {
                template: `<div>Home</div>`
            },
            posts: {
                template: `<div>Posts</div>`
            },
            archive: {
                template: `<div>Archive</div>`
            }
        }
    }).$mount('#app');
    
    document.getElementById('home').onclick = function () {
        vm.currentView = "home";
    };
    document.getElementById('posts').onclick = function () {
        vm.currentView = "posts";
    };
    document.getElementById('archive').onclick = function () {
        vm.currentView = "archive";
    };

####  使用script或template标签

#####  使用script标签

    
    
    <div id="app">
        <my-component></my-component>
    </div>
    <script type="text/x-template" id="myComponent">
        <div>This is a test component.</div>
    </script>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        Vue.component('my-component', {
            template: `#myComponent`
        });
    
        new Vue({
            el: "#app"
        });
    </script>

#####  使用template标签

    
    
    <div id="app">
        <my-component></my-component>
    </div>
    <template id="myComponent">
        <div>This is a test component.</div>
    </template>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        Vue.component('my-component', {
            template: `#myComponent`
        });
    
        new Vue({
            el: "#app"
        });
    </script>

##  使用props

**组件实例的作用域是孤立的** 。这意味着不能并且不应该在子组件的模板内直接引用父组件的数据。可以使用 ` props ` 把数据传给子组件。

###  props基础示例

    
    
    // 将父组件数据通过已定义好的props属性传递给子组件
    <div id="app">
        <my-component :my-name="name" :my-age="age"></my-component>
    </div>
    <template id="myComponent">
        <table>
            <thead>
            <tr>
                <th colspan="2">
                    子组件数据
                </th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>my name</td>
                <td>{{myName}}</td>
            </tr>
            <tr>
                <td>my age</td>
                <td>{{myAge}}</td>
            </tr>
            </tbody>
        </table>
    </template>
    <script src="https://cdn.bootcss.com/vue/2.4.4/vue.js"></script>
    <script>
        new Vue({
            el: "#app",
            data: {
                name: 'keepfool',
                age: 28
            },
            components: {
                'my-component': {
                    template: `#myComponent`,
                    props: ['myName', 'myAge']
                }
            }
        });
    </script>

如果我们想使用父组件的数据，则必须先在子组件中定义 ` props ` 属性，也就是 ` props: [‘myName', ‘myAge'] `
这行代码。

> **注意：** 在子组件中定义 ` prop ` 时，使用了 ` camelCase ` 命名法。由于HTML特性不区分大小写， ` camelCase
> ` 的 ` prop ` 用于特性时，需要转为 ` kebab-case ` （短横线隔开）。例如，在 ` prop ` 中定义的 ` myName `
> ，在用作特性时需要转换为 ` my-name ` 。

在父组件中使用子组件时，通过以下语法将数据传递给子组件：

    
    
    <child-component v-bind:子组件prop="父组件数据属性"></child-component>

##  prop的绑定类型

###  单向绑定

  1. **修改了子组件的数据，没有影响父组件的数据。**
  2. **修改了父组件的数据，同时影响了子组件。**

` prop ` 默认是单向绑定：当父组件的属性变化时，将传导给子组件，但是反过来不会。这是为了防止子组件无意修改了父组件的状态。

###  双向绑定

可以使用 ` .sync ` 显式地指定双向绑定，这使得子组件的数据修改会回传给父组件。

