---
date: 2023-12-12
category:
    - react.js
tag:
    - react.js
    - ecmascript-6
---
 # React 组件
##  React 组件

一个 ` React ` 应用就是构建在 ` React组件 ` 之上的。

组件有两个核心概念：

  * ` props `

  * ` state `

一个组件就是通过这两个属性的值在 ` render ` 方法里面生成这个组件对应的 ` HTML ` 结构。

> **注意：组件生成的` HTML ` 结构只能有一个单一的根节点。 **

**props**

` props ` 就是组件的属性，由外部通过 ` JSX ` 属性传入设置，一旦初始设置完成，就可以认为 ` this.props `
是不可更改的，所以不要轻易更改设置 ` this.props ` 里面的值（虽然对于一个 ` JS ` 对象你可以做任何事）。

**state**

` state ` 是组件的当前状态，可以把组件简单看成一个 ` “状态机” ` ，根据状态 ` state ` 呈现不同的 ` UI ` 展示。

一旦状态（数据）更改，组件就会自动调用 ` render ` 重新渲染 ` UI ` ，这个更改的动作会通过 ` this.setState `
方法来触发。

###  划分状态数据

一条原则：让组件尽可能地少状态。

这样组件逻辑就越容易维护。

> 什么样的数据属性可以当作状态？

当更改这个状态（数据）需要更新组件 ` UI ` 的就可以认为是 ` state ` ，下面这些可以认为不是状态：

  * 可计算的数据：比如一个数组的长度 

  * 和 ` props ` 重复的数据：除非这个数据是要做变更的 

###  无状态组件

你也可以用纯粹的函数来定义 ` 无状态的组件(stateless function) ` ， ` 这种组件没有状态，没有生命周期 ` ，只是简单的接受 `
props ` 渲染生成 ` DOM ` 结构。无状态组件非常简单，开销很低，如果可能的话尽量使用无状态组件。比如使用箭头函数定义：

    
    
    const HelloMessage = (props) => <div>Hello {props.name}</div>;
    render(<HelloMessage name="Jim"/>, app);
    

因为无状态组件 ` 只是函数 ` ，所以它 ` 没有实例返回 ` ，这点在想用 ` refs ` 获取无状态组件的时候要注意。

##  组件生命周期

一般来说，一个组件类由 ` extends Component ` 创建，并且提供一个 ` render ` 方法以及其他 ` 可选的生命周期函数 ` 、
` 组件相关的事件或方法 ` 来定义。

**getInitialState**

初始化 ` this.state ` 的值，只在组件装载之前调用一次。

如果是使用 ` ES6 ` 的语法，你也可以 ` 在构造函数中初始化状态 ` ，比如：

    
    
    class Counter extends Component {
        constructor(props) {
            super(props);
            this.state = {count: props.initialCount};
        }
    
        render() {
            
        }
    }
    

###  getDefaultProps

只在组件 ` 创建时调用一次并缓存返回的对象 ` （即在 ` React.createClass ` 之后就会调用）。

因为这个方法在实例初始化之前调用，所以在这个方法里面不能依赖 ` this ` 获取到这个组件的实例。

在组件装载之后，这个方法缓存的结果会用来保证访问 ` this.props ` 的属性时，当这个属性没有在父组件中传入（在这个组件的 ` JSX `
属性里设置），也总是有值的。

如果是使用 ` ES6 ` 语法，可以直接定义 ` defaultProps ` 这个类属性来替代，这样能更直观的知道 ` default props `
是预先定义好的对象值：

    
    
    Counter.defaultProps = {initialCount: 0};
    

**render**

组装生成这个组件的 ` HTML ` 结构（使用原生 ` HTML ` 标签或者子组件），也可以返回 ` null ` 或者 ` false ` ，这时候
` ReactDOM.findDOMNode(this) ` 会返回 ` null ` 。

##  生命周期函数

###  装载组件触发

**componentWillMount**

只会在装载之前调用一次，在 ` render ` 之前调用，你可以在这个方法里面调用 ` setState ` 改变状态，并且不会导致额外调用一次 `
render ` 。

**componentDidMount**

只会在装载完成之后调用一次，在 ` render ` 之后调用，从这里开始可以通过 ` ReactDOM.findDOMNode(this) `
获取到组件的 ` DOM ` 节点。

###  更新组件触发

这些方法不会在首次 ` render ` 组件的周期调用

  * ` componentWillReceiveProps `

  * ` shouldComponentUpdate `

  * ` componentWillUpdate `

  * ` componentDidUpdate `

###  卸载组件触发

  * ` componentWillUnmount `

##  事件处理

可以看到 ` React ` 里面绑定事件的方式和在 ` HTML ` 中绑定事件类似，使用驼峰式命名指定要绑定的 ` onClick `
属性为组件定义的一个方法 ` {this.handleClick.bind(this)} ` 。

注意要显式调用 ` bind(this) ` ` 将事件函数上下文绑定要组件实例上 ` ，这也是 ` React `
推崇的原则：没有黑科技，尽量使用显式的容易理解的 ` JavaScript ` 代码。

###  “合成事件”和“原生事件”

` React ` 实现了一个“合成事件”层（ ` synthetic event system ` ），这个事件模型保证了和 **W3C**
标准保持一致，所以不用担心有什么诡异的用法，并且这个事件层消除了 **IE** 与 **W3C** 标准实现之间的兼容问题。

**“合成事件”还提供了额外的好处：**

**事件委托**

“合成事件”会以 ` 事件委托 ` （ ` event delegation ` ）的方式绑定到 ` 组件最上层 ` ，并且在 ` 组件卸载 ` （ `
unmount ` ）的时候 ` 自动销毁绑定的事件 ` 。

**什么是“原生事件”？**

比如你在 ` componentDidMount ` 方法里面通过 ` addEventListener ` 绑定的事件就是浏览器原生事件。

使用原生事件的时候注意在 ` componentWillUnmount ` 解除绑定 ` removeEventListener ` 。

所有通过 ` JSX ` 这种方式绑定的事件都是绑定到“合成事件”，除非你有特别的理由，建议总是用 ` React ` 的方式处理事件。

**Tips**

如果混用“合成事件”和“原生事件”，比如一种常见的场景是用原生事件在 ` document ` 上绑定，然后在组件里面绑定的合成事件想要通过 `
e.stopPropagation() ` 来阻止事件冒泡到 ` document ` ，这时候是行不通的，参见 [ Event delegation
]() ，因为 ` e.stopPropagation ` 是内部“合成事件” 层面的，解决方法是要用 `
e.nativeEvent.stopImmediatePropagation() `

“合成事件” 的 ` event ` 对象只在当前 ` event loop ` 有效，比如你想在事件里面调用一个 ` promise ` ，在 `
resolve ` 之后去拿 ` event ` 对象会拿不到（并且没有错误抛出）：

    
    
    handleClick(e) {
      promise.then(() => doSomethingWith(e));
    }
    

###  参数传递

给事件处理函数传递额外参数的方式： ` bind(this, arg1, arg2, ...) `

    
    
    render: function() {
        return <p onClick={this.handleClick.bind(this, 'extra param')}>;
    },
    handleClick: function(param, event) {
        // handle click
    }
    

##  DOM 操作

大部分情况下你不需要通过查询 ` DOM ` 元素去更新组件的 ` UI ` ，你只要关注设置组件的状态（ ` setState `
）。但是可能在某些情况下你确实需要直接操作 ` DOM ` 。

首先我们要了解 ` ReactDOM.render ` 组件返回的是什么？

它会返回 ` 对组件的引用 ` 也就是 ` 组件实例 ` （对于 ` 无状态状态组件 ` 来说返回 ` null ` ），注意 ` JSX `
返回的不是组件实例，它只是一个 ` ReactElement ` 对象（还记得我们用纯 ` JS ` 来构建 ` JSX ` 的方式吗），比如这种：

    
    
    // A ReactElement
    const myComponent = <MyComponent />
    
    // render
    const myComponentInstance = ReactDOM.render(myComponent, mountNode);
    myComponentInstance.doSomething();
    

**findDOMNode()**

当组件加载到页面上之后（ ` mounted ` ），你都可以通过 ` react-dom ` 提供的 ` findDOMNode() `
方法拿到组件对应的 ` DOM ` 元素。

    
    
    import { findDOMNode } from 'react-dom';
    
    // Inside Component class
    componentDidMound() {
      const el = findDOMNode(this);
    }
    

` findDOMNode() ` 不能用在无状态组件上。

**Refs**

另外一种方式就是通过在要引用的 ` DOM ` 元素上面设置一个 ` ref ` 属性指定一个名称，然后通过 ` this.refs.name `
来访问对应的 ` DOM ` 元素。

比如有一种情况是必须 ` 直接操作 DOM ` 来实现的，你希望一个 ` <input/> ` 元素在你清空它的值时 ` focus ` ，你没法仅仅靠 `
state ` 来实现这个功能。

    
    
    class App extends Component {
      constructor() {
        return { userInput: '' };
      }
    
      handleChange(e) {
        this.setState({ userInput: e.target.value });
      }
    
      clearAndFocusInput() {
        this.setState({ userInput: '' }, () => {
          this.refs.theInput.focus();
        });
      }
    
      render() {
        return (
          <div>
            <div onClick={this.clearAndFocusInput.bind(this)}>
              Click to Focus and Reset
            </div>
            <input
              ref="theInput"
              value={this.state.userInput}
              onChange={this.handleChange.bind(this)}
            />
          </div>
        );
      }
    }
    

如果 ` ref ` 是设置在原生 ` HTML ` 元素上，它拿到的就是 ` DOM `
元素，如果设置在自定义组件上，它拿到的就是组件实例，这时候就需要通过 ` findDOMNode ` 来拿到组件的 ` DOM ` 元素。

因为无状态组件没有实例，所以 ` ref ` 不能设置在无状态组件上，一般来说这没什么问题，因为无状态组件没有实例方法，不需要 ` ref `
去拿实例调用相关的方法，但是如果想要拿无状态组件的 ` DOM ` 元素的时候，就需要用一个状态组件封装一层，然后通过 ` ref ` 和 `
findDOMNode ` 去获取。

**总结**

  * 你可以使用 ` ref ` 到的组件定义的任何公共方法，比如 ` this.refs.myTypeahead.reset() `

  * ` Refs ` 是访问到组件内部 ` DOM ` 节点唯一 **可靠** 的方法 

**注意事项**

  * 不要在 ` render ` 或者 ` render 之前 ` 访问 ` refs `

  * 不要滥用 ` refs ` ，比如只是用它来按照传统的方式操作界面 ` UI ` ：找到 ` DOM ` -> 更新 ` DOM `

##  组合组件

使用组件的目的就是通过构建模块化的组件，相互组合组件最后组装成一个复杂的应用。

在 ` React ` 组件中要包含其他组件作为子组件，只需要把组件当作一个 ` DOM ` 元素引入就可以了。

###  循环插入子元素

如果组件中包含通过循环插入的子元素，为了保证重新渲染 ` UI ` 的时候能够正确显示这些子元素，每个元素都需要通过一个特殊的 ` key `
属性指定一个唯一值。

` key ` 必须直接在循环中设置：

    
    
    const MyComponent = (props) => {
        return (
            <ul>
                {props.results.map((result) => {
                    return <ListItemWrapper key={result.id} data={result}/>;
                })}
            </ul>
        );
    };
    

你也可以用一个 ` key ` 值作为属性，子元素作为属性值的对象字面量来显示子元素列表。

实际上浏览器在遍历一个字面量对象的时候会保持顺序一致，除非存在属性值可以被转换成整数值，这种属性值会排序并放在其他属性之前被遍历到，所以为了防止这种情况发生，可以在构建这个字面量的时候在
` key ` 值前面加字符串前缀。

` HTML ` 元素会作为 ` React ` 组件对象、 ` JS ` 表达式结果是一个文字节点，都会存入 ` Parent ` 组件的 `
props.children ` 。

一般来说，可以直接将这个属性作为父组件的子元素 ` render ` ：

    
    
    const Parent = (props) => <div>{props.children}</div>;
    

` props.children ` 通常是一个组件对象的数组，但是当只有一个子元素的时候， ` props.children `
将是这个唯一的子元素，而不是数组了。

` React.Children ` 提供了额外的方法方便操作这个属性。

##  组件间通信

###  父子组件间通信

这种情况下很简单，就是通过 ` props ` 属性传递，在父组件给子组件设置 ` props ` ，然后子组件就可以通过 ` props `
访问到父组件的数据／方法，这样就搭建起了父子组件间通信的桥梁。

` div ` 可以看作一个子组件，指定它的 ` onClick ` 事件调用父组件的方法。

    
    
    import React, {Component} from 'react';
    import {render} from 'react-dom';
    
    class GroceryList extends Component {
        handleClick(i) {
            console.log('You clicked: ' + this.props.items[i]);
        }
    
        render() {
            return (
                <ul>
                    {this.props.items.map((item, i) => {
                        return (
                            <li onClick={this.handleClick.bind(this, i)} key={i}>{item}</li>
                        )
                    })}
                </ul>
            )
        }
    }
    render(
        <GroceryList items={['Apple', 'Banana', 'Cranberry']}/>,
        mountNode
    );
    

` div ` 可以看作一个子组件，指定它的 ` onClick ` 事件调用父组件的方法。

###  非父子组件间的通信

使用 ` 全局事件 Pub/Sub 模式 ` ，在 ` componentDidMount ` 里面 ` 订阅事件 ` ，在 `
componentWillUnmount ` 里面 ` 取消订阅 ` ，当收到事件触发的时候调用 ` setState ` 更新 ` UI ` 。

这种模式在复杂的系统里面可能会变得难以维护，所以看个人权衡是否将组件封装到大的组件，甚至整个页面或者应用就封装到一个组件。

一般来说，对于比较复杂的应用，推荐使用类似 ` Flux ` 这种单项数据流架构。

