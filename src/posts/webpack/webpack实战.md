---
date: 2023-03-28
category:
    - 前端构建
tag:
    - 前端构建
    - 前端工程化
    - 前端
    - javascript
    - webpack
---
 # webpack实战
##  webpack实战

> 查看所有文档页面： [ 全栈开发 ]() ，获取更多信息。
>
>
> 快马加鞭，加班加点，终于把这个文档整理出来了，顺便深入地学习一番，巩固知识，就是太累人，影响睡眠时间和质量。极客就是想要把事情做到极致，开始了就必须到达终点。
>
> 原文链接： [ webpack实战 ]() ，原文广告模态框遮挡，阅读体验不好，所以整理成本文，方便查找。

本章教你如何用 Webpack 去解决实际项目中常见的场景。

按照不同场景划分成以下几类：

  * 使用新语言来开发项目： 

    * 使用 ES6 语言 
    * 使用 TypeScript 语言 
    * 使用 Flow 检查器 
    * 使用 SCSS 语言 
    * 使用 PostCSS 
  * 使用新框架来开发项目： 

    * 使用 React 框架 
    * 使用 Vue 框架 
    * 使用 Angular2 框架 
  * 用 Webpack 构建单页应用： 

    * 为单页应用生成 HTML 
    * 管理多个单页应用 
  * 用 Webpack 构建不同运行环境的项目： 

    * 构建同构应用 
    * 构建 Electron 应用 
    * 构建 Npm 模块 
    * 构建离线应用 
  * Webpack 结合其它工具搭配使用，各取所长： 

    * 搭配 Npm Script 
    * 检查代码 
    * 通过 Node.js API 启动 Webpack 
    * 使用 Webpack Dev Middleware 
  * 用 Webpack 加载特殊类型的资源： 

    * 加载图片 
    * 加载SVG 
    * 加载 Source Map 

###  使用 TypeScript 语言

由于本文不推荐使用TypeScript，ES6就足够完成大部分任务。原文链接： [ 使用 TypeScript 语言 ]()

###  使用 Angular2 框架

Angular2不在我的技术栈范围，所以这一章不加入，有兴趣的查看原文： [ 使用 Angular2 框架 ]()

##  使用ES6语言

通常我们需要把采用 ES6 编写的代码转换成目前已经支持良好的 ES5 代码，这包含2件事：

  1. 把新的 ES6 语法用 ES5 实现，例如 ES6 的 ` class ` 语法用 ES5 的 ` prototype ` 实现。 
  2. 给新的 API 注入 polyfill ，例如使用新的 ` fetch ` API 时注入对应的 polyfill 后才能让低端浏览器正常运行。 

###  Babel

Babel 可以方便的完成以上2件事。

Babel 是一个 JavaScript 编译器，能将 ES6 代码转为 ES5
代码，让你使用最新的语言特性而不用担心兼容性问题，并且可以通过插件机制根据需求灵活的扩展。

在 Babel 执行编译的过程中，会从项目根目录下的 ` .babelrc ` 文件读取配置。 ` .babelrc ` 是一个 JSON
格式的文件，内容大致如下：

    
    
    {
      "plugins": [
        [
          "transform-runtime",
          {
            "polyfill": false
          }
        ]
       ],
      "presets": [
        [
          "es2015",
          {
            "modules": false
          }
        ],
        "stage-2",
        "react"
      ]
    }
    

###  Plugins

` plugins ` 属性告诉 Babel 要使用哪些插件，插件可以控制如何转换代码。

以上配置文件里的 ` transform-runtime ` 对应的插件全名叫做 ` babel-plugin-transform-runtime `
，即在前面加上了 ` babel-plugin- ` ，要让 Babel 正常运行我们必须先安装它：

    
    
    npm i -D babel-plugin-transform-runtime
    

` babel-plugin-transform-runtime ` 是 Babel 官方提供的一个插件，作用是减少冗余代码。

Babel 在把 ES6 代码转换成 ES5 代码时通常需要一些 ES5 写的辅助函数来完成新语法的实现，例如在转换 ` class extent `
语法时会在转换后的 ES5 代码里注入 ` _extent ` 辅助函数用于实现继承：

    
    
    function _extent(target) {
      for (var i = 1; i < arguments.length; i++) {
        var source = arguments[i];
        for (var key in source) {
          if (Object.prototype.hasOwnProperty.call(source, key)) {
            target[key] = source[key];
          }
        }
      }
      return target;
    }
    

这会导致每个使用了 ` class extent ` 语法的文件都被注入重复的 ` _extent ` 辅助函数代码， ` babel-plugin-
transform-runtime ` 的作用在于不把辅助函数内容注入到文件里，而是注入一条导入语句：

    
    
    var _extent = require('babel-runtime/helpers/_extent');
    

这样能减小 Babel 编译出来的代码的文件大小。

同时需要注意的是由于 ` babel-plugin-transform-runtime ` 注入了 ` require('babel-
runtime/helpers/_extent') ` 语句到编译后的代码里，需要安装 ` babel-runtime `
依赖到你的项目后，代码才能正常运行。 也就是说 ` babel-plugin-transform-runtime ` 和 ` babel-runtime `
需要配套使用，使用了 ` babel-plugin-transform-runtime ` 后一定需要 ` babel-runtime ` 。

###  Presets

` presets ` 属性告诉 Babel 要转换的源码使用了哪些新的语法特性，一个 ` Presets ` 对一组新语法特性提供支持，多个 `
Presets ` 可以叠加。

` Presets ` 其实是一组 Plugins 的集合，每一个 Plugin 完成一个新语法的转换工作。Presets 是按照 ECMAScript
草案来组织的，通常可以分为以下三大类：

  1. 已经被写入 ECMAScript 标准里的特性，由于之前每年都有新特性被加入到标准里； 

     * env 包含当前所有 ECMAScript 标准里的最新特性。 
  2. 被社区提出来的但还未被写入 ECMAScript 标准里特性，这其中又分为以下四种： 

     * ` stage0 ` 只是一个美好激进的想法，有 Babel 插件实现了对这些特性的支持，但是不确定是否会被定为标准； 
     * ` stage1 ` 值得被纳入标准的特性； 
     * ` stage2 ` 该特性规范已经被起草，将会被纳入标准里； 
     * ` stage3 ` 该特性规范已经定稿，各大浏览器厂商和 Node.js 社区开始着手实现； 
     * ` stage4 ` 在接下来的一年将会加入到标准里去。 
  3. 为了支持一些特定应用场景下的语法，和 ECMAScript 标准没有关系，例如 ` babel-preset-react ` 是为了支持 React 开发中的 JSX 语法。 

在实际应用中，你需要根据项目源码所使用的语法去安装对应的 Plugins 或 Presets。

###  接入 Babel

由于 Babel 所做的事情是转换代码，所以应该通过 Loader 去接入 Babel，Webpack 配置如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.js$/,
            use: ['babel-loader'],
          },
        ]
      },
      // 输出 source-map 方便直接调试 ES6 源码
      devtool: 'source-map'
    };
    

配置命中了项目目录下所有的 JavaScript 文件，通过 ` babel-loader ` 去调用 Babel 完成转换工作。
在重新执行构建前，需要先安装新引入的依赖：

    
    
    # Webpack 接入 Babel 必须依赖的模块
    npm i -D babel-core babel-loader 
    # 根据你的需求选择不同的 Plugins 或 Presets
    npm i -D babel-preset-env
    

##  使用SCSS语言

SCSS 可以让你用更灵活的方式写 CSS。 它是一种 CSS 预处理器，语法和 CSS 相似，但加入了变量、逻辑等编程元素，代码类似这样：

    
    
    $blue: #1875e7;　
    
    div {
      color: $blue;
    }
    

SCSS 又叫 SASS，区别在于 SASS 语法类似 Ruby，而 SCSS 语法类似 CSS，对于熟悉 CSS 的前端工程师来说会更喜欢 SCSS。

采用 SCSS 去写 CSS 的好处在于可以方便地管理代码，抽离公共的部分，通过逻辑写出更灵活的代码。 和 SCSS 类似的 CSS 预处理器还有 LESS
等。

使用 SCSS 可以提升编码效率，但是必须把 SCSS 源代码编译成可以直接在浏览器环境下运行的 CSS 代码。

` node-sass ` 核心模块是由 C++ 编写，再用 Node.js 封装了一层，以供给其它 Node.js 调用。 ` node-sass `
还支持通过命令行调用，先安装它到全局：

    
    
    npm i -g node-sass
    

再执行编译命令：

    
    
    # 把 main.scss 源文件编译成 main.css
    node-sass main.scss main.css
        

你就能在源码同目录下看到编译后的 ` main.css ` 文件。

###  接入 Webpack

Webpack 接入 ` sass-loader ` 相关配置如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            // 增加对 SCSS 文件的支持
            test: /\.scss/,
            // SCSS 文件的处理顺序为先 sass-loader 再 css-loader 再 style-loader
            use: ['style-loader', 'css-loader', 'sass-loader'],
          },
        ]
      },
    };
    

以上配置通过正则 ` /\.scss/ ` 匹配所有以 ` .scss ` 为后缀的 SCSS 文件，再分别使用3个 Loader
去处理。具体处理流程如下：

  1. 通过 ` sass-loader ` 把 SCSS 源码转换为 CSS 代码，再把 CSS 代码交给 ` css-loader ` 去处理。 
  2. ` css-loader ` 会找出 CSS 代码中的 ` @import ` 和 ` url() ` 这样的导入语句，告诉 Webpack 依赖这些资源。同时还支持 CSS Modules、压缩 CSS 等功能。处理完后再把结果交给 ` style-loader ` 去处理。 
  3. ` style-loader ` 会把 CSS 代码转换成字符串后，注入到 JavaScript 代码中去，通过 JavaScript 去给 DOM 增加样式。如果你想把 CSS 代码提取到一个单独的文件而不是和 JavaScript 混在一起，可以使用1-5 使用Plugin 中介绍过的 ExtractTextPlugin。 

由于接入 ` sass-loader ` ，项目需要安装这些新的依赖：

    
    
    # 安装 Webpack Loader 依赖
    npm i -D  sass-loader css-loader style-loader
    # sass-loader 依赖 node-sass
    npm i -D node-sass
        

##  使用Flow检查器

Flow 是一个 Facebook 开源的 JavaScript 静态类型检测器，它是 JavaScript 语言的超集。

你所需要做的就是在需要的地方加上类型检查，例如在两个由不同人开发的模块对接的接口出加上静态类型检查，能在编译阶段就指出部分模块使用不当的问题。 同时
Flow 也能通过类型推断检查出 JavaScript 代码中潜在的 Bug。

Flow 使用效果如下：

    
    
    // @flow
    
    // 静态类型检查
    function square1(n: number): number {
      return n * n;
    }
    square1('2'); // Error: square1 需要传入 number 作为参数
    
    // 类型推断检查
    function square2(n) {
      return n * n; // Error: 传入的 string 类型不能做乘法运算
    }
    square2('2');
    
    
    

> 需要注意的时代码中的第一行 ` // @flow ` 告诉 Flow 检查器这个文件需要被检查。

###  使用 Flow

Flow 检测器由高性能跨平台的 OCaml 语言编写，它的可执行文件可以通过：

    
    
    npm i -D flow-bin
    

安装，安装完成后通过先配置 Npm Script：

    
    
    "scripts": {
       "flow": "flow"
    }
    

再通过 ` npm run flow ` 去调用 Flow 执行代码检查。

除此之外你还可以通过：

    
    
    npm i -g flow-bin
    

把 Flow 安装到全局后，再直接通过 ` flow ` 命令去执行代码检查。

安装成功后，在项目根目录下执行 Flow 后，Flow 会遍历出所有需要检查的文件并对其进行检查，输出错误结果到控制台。

采用了 Flow 静态类型语法的 JavaScript 是无法直接在目前已有的 JavaScript
引擎中运行的，要让代码可以运行需要把这些静态类型语法去掉。

    
    
    // 采用 Flow 的源代码
    function foo(one: any, two: number, three?): string {}
    
    // 去掉静态类型语法后输出代码
    function foo(one, two, three) {}
    

有两种方式可以做到这点：

  1. ` flow-remove-types ` 可单独使用，速度快。 
  2. ` babel-preset-flow ` 与 Babel 集成。 

###  集成 Webpack

由于使用了 Flow 项目一般都会使用 ES6 语法，所以把 Flow 集成到使用 Webpack 构建的项目里最方便的方法是借助 Babel。

  1. 安装 ` npm i -D babel-preset-flow ` 依赖到项目。 
  2. 修改 ` .babelrc ` 配置文件，加入 Flow Preset： 
    
        "presets": [
    ...[],
    "flow"
    ]

往源码里加入静态类型后重新构建项目，你会发现采用了 Flow 的源码还是能正常在浏览器中运行。

> 要明确构建的目的只是为了去除源码中的 Flow 静态类型语法，而代码检查和构建无关。 许多编辑器已经整合 Flow，可以实时在代码中高亮指出 Flow
> 检查出的问题。

##  使用PostCSS

PostCSS 是一个 CSS 处理工具，和 SCSS 不同的地方在于它通过插件机制可以灵活的扩展其支持的特性，而不是像 SCSS 那样语法是固定的。
PostCSS 的用处非常多，包括给 CSS 自动加前缀、使用下一代 CSS 语法等，目前越来越多的人开始用它，它很可能会成为 CSS 预处理器的最终赢家。

> PostCSS 和 CSS 的关系就像 Babel 和 JavaScript
> 的关系，它们解除了语法上的禁锢，通过插件机制来扩展语言本身，用工程化手段给语言带来了更多的可能性。
>
> PostCSS 和 SCSS 的关系就像 Babel 和 TypeScript 的关系，PostCSS 更加灵活、可扩张性强，而 SCSS
> 内置了大量功能而不能扩展。

给 CSS 自动加前缀，增加各浏览器的兼容性：

    
    
    /*输入*/
    h1 {
      display: flex;
    }
    
    /*输出*/
    h1 {
      display: -webkit-box;
      display: -webkit-flex;
      display: -ms-flexbox;
      display: flex;
    }
    

使用下一代 CSS 语法：

    
    
    /*输入*/
    :root {
      --red: #d33;
    }
    
    h1 {
      color: var(--red);
    }
    
    
    /*输出*/
    h1 { 
      color: #d33;
    }
    

PostCSS 全部采用 JavaScript 编写，运行在 Node.js 之上，即提供了给 JavaScript 代码调用的模块，也提供了可执行的文件。

在 PostCSS 启动时，会从目录下的 ` postcss.config.js ` 文件中读取所需配置，所以需要新建该文件，文件内容大致如下：

    
    
    module.exports = {
      plugins: [
        // 需要使用的插件列表
        require('postcss-cssnext')
      ]
    }
    

其中的 ` postcss-cssnext ` 插件可以让你使用下一代 CSS 语法编写代码，再通过 PostCSS 转换成目前的浏览器可识别的
CSS，并且该插件还包含给 CSS 自动加前缀的功能。

> 目前 Chrome 等现代浏览器已经能完全支持 ` cssnext ` 中的所有语法，也就是说按照 ` cssnext ` 语法写的 CSS
> 在不经过转换的情况下也能在浏览器中直接运行。

###  接入 Webpack

虽然使用 PostCSS 后文件后缀还是 ` .css ` 但这些文件必须先交给 ` postcss-loader ` 处理一遍后再交给 ` css-
loader ` 。

接入 PostCSS 相关的 Webpack 配置如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            // 使用 PostCSS 处理 CSS 文件
            test: /\.css/,
            use: ['style-loader', 'css-loader', 'postcss-loader'],
          },
        ]
      },
    };
    

接入 PostCSS 给项目带来了新的依赖需要安装，如下：

    
    
    # 安装 Webpack Loader 依赖
    npm i -D postcss-loader css-loader style-loader
    # 根据你使用的特性安装对应的 PostCSS 插件依赖
    npm i -D postcss-cssnext
        

##  使用React框架

###  React 语法特征

使用了 React 项目的代码特征有 JSX 和 Class 语法，例如：

    
    
    class Button extends Component {
      render() {
        return <h1>Hello,Webpack</h1>
      }
    }   
    

> 在使用了 React 的项目里 JSX 和 Class 语法并不是必须的，但使用新语法写出的代码看上去更优雅。

其中 JSX 语法是无法在任何现有的 JavaScript 引擎中运行的，所以在构建过程中需要把源码转换成可以运行的代码，例如：

    
    
    // 原 JSX 语法代码
    return <h1>Hello,Webpack</h1>
    
    // 被转换成正常的 JavaScript 代码
    return React.createElement('h1', null, 'Hello,Webpack')
    

###  React 与 Babel

要在使用 Babel 的项目中接入 React 框架是很简单的，只需要加入 React 所依赖的 Presets ` babel-preset-react
` 。

通过以下命令：

    
    
    # 安装 React 基础依赖
    npm i -D react react-dom
    # 安装 babel 完成语法转换所需依赖
    npm i -D babel-preset-react
    

安装新的依赖后，再修改 ` .babelrc ` 配置文件加入 React Presets

    
    
    "presets": [
        "react"
    ],
    

就完成了一切准备工作。

再修改 ` main.js ` 文件如下：

    
    
    import * as React from 'react';
    import { Component } from 'react';
    import { render } from 'react-dom';
    
    class Button extends Component {
      render() {
        return <h1>Hello,Webpack</h1>
      }
    }
    
    render(<Button/>, window.document.getElementById('app'));
    

重新执行构建打开网页你将会发现由 React 渲染出来的 ` Hello,Webpack ` 。

###  React 与 TypeScript

TypeScript 相比于 Babel 的优点在于它原生支持 JSX 语法，你不需要重新安装新的依赖，只需修改一行配置。 但 TypeScript
的不同在于：

  * 使用了 JSX 语法的文件后缀必须是 ` tsx ` 。 
  * 由于 React 不是采用 TypeScript 编写的，需要安装 ` react ` 和 ` react-dom ` 对应的 TypeScript 接口描述模块 ` @types/react ` 和 ` @types/react-dom ` 后才能通过编译。 

修改 TypeScript 编译器配置文件 ` tsconfig.json ` 增加对 JSX 语法的支持，如下：

    
    
    {
      "compilerOptions": {
        "jsx": "react" // 开启 jsx ，支持 React
      }
    }
    

由于 ` main.js ` 文件中存在 JSX 语法，再把 ` main.js ` 文件重命名为 ` main.tsx ` ，同时修改文件内容为在上面
React 与 Babel 里所采用的 React 代码。 同时为了让 Webpack 对项目里的 ` ts ` 与 ` tsx ` 原文件都采用 `
awesome-typescript-loader ` 去转换， 需要注意的是 Webpack Loader 配置的 ` test ` 选项需要匹配到 `
tsx ` 类型的文件，并且 ` extensions ` 中也要加上 ` .tsx ` ，配置如下：

    
    
    module.exports = {
      // TS 执行入口文件
      entry: './main',
      output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, './dist'),
      },
      resolve: {
        // 先尝试 ts，tsx 后缀的 TypeScript 源码文件 
        extensions: ['.ts', '.tsx', '.js',] 
      },
      module: {
        rules: [
          {
            // 同时匹配 ts，tsx 后缀的 TypeScript 源码文件 
            test: /\.tsx?$/,
            loader: 'awesome-typescript-loader'
          }
        ]
      },
      devtool: 'source-map',// 输出 Source Map 方便在浏览器里调试 TypeScript 代码
    };
    

通过 ` npm i react react-dom @types/react @types/react-dom `
安装新的依赖后重启构建，重新打开网页你将会发现由 React 渲染出来的 ` Hello,Webpack ` 。

##  使用Vue框架

Vue是一个渐进式的 MVVM 框架，相比于 React、Angular 它更灵活轻量。
它不会强制性地内置一些功能和语法，你可以根据自己的需要一点点地添加功能。 虽然采用 Vue
的项目能用可直接运行在浏览器环境里的代码编写，但为了方便编码大多数项目都会采用 Vue 官方的单文件组件的写法去编写项目。

Vue 的单文件组件通过一个类似 HTML 文件的 ` .vue ` 文件就能描述清楚一个组件所需的模版、样式、逻辑。

` main.js ` 入口文件：

    
    
    import Vue from 'vue'
    import App from './App.vue'
    
    new Vue({
      el: '#app',
      render: h => h(App)
    });
    

入口文件创建一个 Vue 的根实例，在 ID 为 ` app ` 的 DOM 节点上渲染出上面定义的 App 组件。

###  接入 Webpack

目前最成熟和流行的开发 Vue 项目的方式是采用 ES6 加 Babel 转换，这和基本的采用 ES6 开发的项目很相似，差别在于要解析 ` .vue `
格式的单文件组件。 好在 Vue 官方提供了对应的 ` vue-loader ` 可以非常方便的完成单文件组件的转换。

修改 Webpack 相关配置如下：

    
    
    module: {
      rules: [
        {
          test: /\.vue$/,
          use: ['vue-loader'],
        },
      ]
    }
    

安装新引入的依赖：

    
    
    # Vue 框架运行需要的库
    npm i -S vue
    # 构建所需的依赖
    npm i -D vue-loader css-loader vue-template-compiler
    

在这些依赖中，它们的作用分别是：

  * ` vue-loader ` ：解析和转换 ` .vue ` 文件，提取出其中的逻辑代码 ` script ` 、样式代码 ` style ` 、以及 HTML 模版 ` template ` ，再分别把它们交给对应的 Loader 去处理。 
  * ` css-loader ` ：加载由 ` vue-loader ` 提取出的 CSS 代码。 
  * ` vue-template-compiler ` ：把 ` vue-loader ` 提取出的 HTML 模版编译成对应的可执行的 JavaScript 代码，这和 React 中的 JSX 语法被编译成 JavaScript 代码类似。预先编译好 HTML 模版相对于在浏览器中再去编译 HTML 模版的好处在于性能更好。 

###  使用 TypeScript 编写 Vue 应用

从 Vue 2.5.0+ 版本开始，提供了对 TypeScript 的良好支持，使用 TypeScript 编写 Vue 是一个很好的选择，因为
TypeScript 能检查出一些潜在的错误。

新增 ` tsconfig.json ` 配置文件，内容如下：

    
    
    {
      "compilerOptions": {
        // 构建出 ES5 版本的 JavaScript，与 Vue 的浏览器支持保持一致
        "target": "es5",
        // 开启严格模式，这可以对 `this` 上的数据属性进行更严格的推断
        "strict": true,
        // TypeScript 编译器输出的 JavaScript 采用 es2015 模块化，使 Tree Shaking 生效
        "module": "es2015",
        "moduleResolution": "node"
      }
    }
    

修改 ` App.vue ` 脚本部分内容如下：

    
    
    <!--组件逻辑-->
    <script lang="ts">
      import Vue from "vue";
    
      // 通过 Vue.extend 启用 TypeScript 类型推断
      export default Vue.extend({
        data() {
          return {
            msg: 'Hello,Webpack',
          }
        },
      });
    </script>
    

注意 ` script ` 标签中的 ` lang="ts" ` 是为了指明代码的语法是 TypeScript。

修改 main.ts 执行入口文件为如下：

    
    
    import Vue from 'vue'
    import App from './App.vue'
    
    new Vue({
      el: '#app',
      render: h => h(App)
    });
    

由于 TypeScript 不认识 ` .vue ` 结尾的文件，为了让其支持 ` import App from './App.vue' `
导入语句，还需要以下文件 ` vue-shims.d.ts ` 去定义 ` .vue ` 的类型：

    
    
    // 告诉 TypeScript 编译器 .vue 文件其实是一个 Vue  
    declare module "*.vue" {
      import Vue from "vue";
      export default Vue;
    }
    

Webpack 配置需要修改两个地方，如下：

    
    
    const path = require('path');
    
    module.exports = {
      resolve: {
        // 增加对 TypeScript 的 .ts 和 .vue 文件的支持
        extensions: ['.ts', '.js', '.vue', '.json'],
      },
      module: {
        rules: [
          // 加载 .ts 文件
          {
            test: /\.ts$/,
            loader: 'ts-loader',
            exclude: /node_modules/,
            options: {
              // 让 tsc 把 vue 文件当成一个 TypeScript 模块去处理，以解决 moudle not found 的问题，tsc 本身不会处理 .vue 结尾的文件
              appendTsSuffixTo: [/\.vue$/],
            }
          },
        ]
      },
    };
    

除此之外还需要安装新引入的依赖： ` npm i -D ts-loader typescript `

##  为单页应用生成HTML

###  引入问题

在使用 React 框架中，是用最简单的 ` Hello,Webpack ` 作为例子让大家理解， 这个例子里因为只输出了一个 ` bundle.js `
文件，所以手写了一个 ` index.html ` 文件去引入这个 ` bundle.js ` ，才能让应用在浏览器中运行起来。

在实际项目中远比这复杂，一个页面常常有很多资源要加载。接下来举一个实战中的例子，要求如下：

  1. 项目采用 ES6 语言加 React 框架。 
  2. 给页面加入 Google Analytics，这部分代码需要内嵌进 HEAD 标签里去。 
  3. 给页面加入 Disqus 用户评论，这部分代码需要异步加载以提升首屏加载速度。 
  4. 压缩和分离 JavaScript 和 CSS 代码，提升加载速度。 

在开始前先来看看该应用最终发布到线上的 [ 代码 ]() 。

可以看到部分代码被内嵌进了 HTML 的 HEAD 标签中，部分文件的文件名称被打上根据文件内容算出的 Hash 值，并且加载这些文件的 URL
地址也被正常的注入到了 HTML 中。

###  解决方案

推荐一个用于方便地解决以上问题的 Webpack 插件 [ web-webpack-plugin ]() 。
该插件已经被社区上许多人使用和验证，解决了大家的痛点获得了很多好评，下面具体介绍如何用它来解决上面的问题。

首先，修改 [ Webpack 配置 ]() 。

以上配置中，大多数都是按照前面已经讲过的内容增加的配置，例如：

  * 增加对 CSS 文件的支持，提取出 Chunk 中的 CSS 代码到单独的文件中，压缩 CSS 文件； 
  * 定义 ` NODE_ENV ` 环境变量为 ` production ` ，以去除源码中只有开发时才需要的部分； 
  * 给输出的文件名称加上 Hash 值； 
  * 压缩输出的 JavaScript 代码。 

但最核心的部分在于 ` plugins ` 里的：

    
    
    new WebPlugin({
      template: './template.html', // HTML 模版文件所在的文件路径
      filename: 'index.html' // 输出的 HTML 的文件名称
    })
    

其中 ` template: './template.html' ` 所指的模版文件 ` template.html ` 的内容是：

    
    
    <head>
      <meta charset="UTF-8">
      <!--注入 Chunk app 中的 CSS-->
      <link rel="stylesheet" href="app?_inline">
      <!--注入 google_analytics 中的 JavaScript 代码-->
      <script src="./google_analytics.js?_inline"></script>
      <!--异步加载 Disqus 评论-->
      <script src="https://dive-into-webpack.disqus.com/embed.js" async></script>
    </head>
    <body>
    <div id="app"></div>
    <!--导入 Chunk app 中的 JS-->
    <script src="app"></script>
    <!--Disqus 评论容器-->
    <div id="disqus_thread"></div>
    </body>
    

该文件描述了哪些资源需要被以何种方式加入到输出的 HTML 文件中。

以 ` <link rel="stylesheet" href="app?_inline"> ` 为例，按照正常引入 CSS 文件一样的语法来引入
Webpack 生产的代码。 ` href ` 属性中的 ` app?_inline ` 可以分为两部分，前面的 ` app ` 表示 CSS 代码来自名叫
` app ` 的 Chunk 中，后面的 ` _inline ` 表示这些代码需要被内嵌到这个标签所在的位置。

同样的 ` <script src="./google_analytics.js?_inline"></script> ` 表示 JavaScript
代码来自相对于当前模版文件 ` template.html ` 的本地文件 ` ./google_analytics.js ` ， 而且文件中的
JavaScript 代码也需要被内嵌到这个标签所在的位置。

也就是说资源链接 URL 字符串里问号前面的部分表示资源内容来自哪里，后面的 ` querystring ` 表示这些资源注入的方式。

除了 ` _inline ` 表示内嵌外，还支持以下属性：

  * ` _dist ` 只有在生产环境下才引入该资源; 
  * ` _dev ` 只有在开发环境下才引入该资源； 
  * ` _ie ` 只有IE浏览器才需要引入的资源，通过 ` [if IE]>resource<![endif] ` 注释实现。 

这些属性之间可以搭配使用，互不冲突。例如 ` app?_inline&_dist ` 表示只在生产环境下才引入该资源，并且需要内嵌到 HTML 里去。

` WebPlugin ` 插件还支持一些其它更高级的用法，详情可以访问该 [ 项目主页 ]() 阅读文档。

##  管理多个单页应用

###  引入问题

在开始前先来看看该应用最终发布到线上的代码。

    
    
    <html>
    <head>
    <meta charset="UTF-8">
    <!--从多个页面中抽离出的公共 CSS 代码-->
    <link rel="stylesheet" href="common_7cc98ad0.css">
    <!--只有这个页面需要的 CSS 代码-->
    <link rel="stylesheet" href="login_e31e214b.css">
    <!--注入 google_analytics 中的 JS 代码-->
    <script>(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
    ga('create', 'UA-XXXXX-Y', 'auto');
    ga('send', 'pageview');</script>
    <!--异步加载 Disqus 评论-->
    <script async="" src="https://dive-into-webpack.disqus.com/embed.js"></script>
    </head>
    <body>
    <div id="app"></div>
    <!--从多个页面中抽离出的公共 JavaScript 代码-->
    <script src="common_a1d9142f.js"></script>
    <!--只有这个页面需要的 JavaScript 代码-->
    <script src="login_f926c4e6.js"></script>
    <!--Disqus 评论容器-->
    <div id="disqus_thread"></div>
    </body>
    </html>

构建出的目录结构为：

    
    
    dist
    ├── common_029086ff.js
    ├── common_7cc98ad0.css
    ├── index.html
    ├── index_04c08fbf.css
    ├── index_b3d3761c.js
    ├── login.html
    ├── login_0a3feca9.js
    └── login_e31e214b.css
    

如果按照上节的思路，可能需要为每个单页应用配置一段如下代码：

    
    
    new WebPlugin({
      template: './template.html', // HTML 模版文件所在的文件路径
      filename: 'login.html' // 输出的 HTML 的文件名称
    })
    

并且把页面对应的入口加入到 ` enrty ` 配置项中，就像这样：

    
    
    entry: {
      index: './pages/index/index.js',// 页面 index.html 的入口文件
      login: './pages/login/index.js',// 页面 login.html 的入口文件
    }
    

当有新页面加入时就需要修改 Webpack 配置文件，新插入一段以上代码，这会导致构建代码难以维护而且易错。

###  解决方案

项目源码目录结构如下：

    
    
    ├── pages
    │   ├── index
    │   │   ├── index.css // 该页面单独需要的 CSS 样式
    │   │   └── index.js // 该页面的入口文件
    │   └── login
    │       ├── index.css
    │       └── index.js
    ├── common.css // 所有页面都需要的公共 CSS 样式
    ├── google_analytics.js
    ├── template.html
    └── webpack.config.js
    

从目录结构中可以看成出下几点要求：

  * 所有单页应用的代码都需要放到一个目录下，例如都放在 ` pages ` 目录下； 
  * 一个单页应用一个单独的文件夹，例如最后生成的 ` index.html ` 相关的代码都在 ` index ` 目录下， ` login.html ` 同理； 
  * 每个单页应用的目录下都有一个 ` index.js ` 文件作为入口执行文件。 

> 虽然 ` AutoWebPlugin `
> 强制性的规定了项目部分的目录结构，但从实战经验来看这是一种优雅的目录规范，合理的拆分了代码，又能让新人快速的看懂项目结构，也方便日后的维护。

Webpack 配置文件修改如下：

<p data-height="465" data-theme-id="0" data-slug-hash="gzJWwB" data-default-
tab="js,result" data-user="whjin" data-embed-version="2" data-pen-
title="webpack管理多个单页应用" class="codepen">See the Pen [ webpack管理多个单页应用 ]() by
whjin ( [ @whjin ]() ) on [ CodePen ]() .</p>  


` AutoWebPlugin ` 会找出 ` pages ` 目录下的2个文件夹 ` index ` 和 ` login `
，把这两个文件夹看成两个单页应用。 并且分别为每个单页应用生成一个 Chunk 配置和 WebPlugin 配置。 每个单页应用的 Chunk
名称就等于文件夹的名称，也就是说 ` autoWebPlugin.entry() ` 方法返回的内容其实是：

    
    
    {
      "index":["./pages/index/index.js","./common.css"],
      "login":["./pages/login/index.js","./common.css"]
    }
    

但这些事情 ` AutoWebPlugin ` 都会自动为你完成，你不用操心，明白大致原理即可。

` template.html ` 模版文件如下：

    
    
    <html>
    <head>
      <meta charset="UTF-8">
      <!--在这注入该页面所依赖但没有手动导入的 CSS-->
      <!--STYLE-->
      <!--注入 google_analytics 中的 JS 代码-->
      <script src="./google_analytics.js?_inline"></script>
      <!--异步加载 Disqus 评论-->
      <script src="https://dive-into-webpack.disqus.com/embed.js" async></script>
    </head>
    <body>
    <div id="app"></div>
    <!--在这注入该页面所依赖但没有手动导入的 JavaScript-->
    <!--SCRIPT-->
    <!--Disqus 评论容器-->
    <div id="disqus_thread"></div>
    </body>
    </html>
    

由于这个模版文件被当作项目中所有单页应用的模版，就不能再像上一节中直接写 Chunk 的名称去引入资源，因为需要被注入到当前页面的 Chunk
名称是不定的，每个单页应用都会有自己的名称。 ` <!--STYLE--> ` 和 ` <!--SCRIPT--> `
的作用在于保证该页面所依赖的资源都会被注入到生成的 HTML 模版里去。

` web-webpack-plugin ` 能分析出每个页面依赖哪些资源，例如对于 ` login.html ` 来说，插件可以确定该页面依赖以下资源：

  * 所有页面都依赖的公共 CSS 代码 ` common.css ` ； 
  * 所有页面都依赖的公共 JavaScrip 代码 ` common.js ` ； 
  * 只有这个页面依赖的 CSS 代码 ` login.css ` ； 
  * 只有这个页面依赖的 JavaScrip 代码 ` login.css ` 。 

由于模版文件 ` template.html ` 里没有指出引入这些依赖资源的 HTML 语句，插件会自动将没有手动导入但页面依赖的资源按照不同类型注入到
` <!--STYLE--> ` 和 ` <!--SCRIPT--> ` 所在的位置。

  * CSS 类型的文件注入到 ` <!--STYLE--> ` 所在的位置，如果 ` <!--STYLE--> ` 不存在就注入到 HTML HEAD 标签的最后； 
  * JavaScrip 类型的文件注入到 ` <!--SCRIPT--> ` 所在的位置，如果 ` <!--SCRIPT--> ` 不存在就注入到 HTML BODY 标签的最后。 

如果后续有新的页面需要开发，只需要在 ` pages ` 目录下新建一个目录，目录名称取为输出 HTML
文件的名称，目录下放这个页面相关的代码即可，无需改动构建代码。

由于 ` AutoWebPlugin ` 是间接的通过上一节提到的 ` WebPlugin ` 实现的， ` WebPlugin ` 支持的功能 `
AutoWebPlugin ` 都支持。

##  构建同构应用

同构应用是指写一份代码但可同时在浏览器和服务器中运行的应用。

###  认识同构应用

现在大多数单页应用的视图都是通过 JavaScript 代码在浏览器端渲染出来的，但在浏览器端渲染的坏处有：

  * 搜索引擎无法收录你的网页，因为展示出的数据都是在浏览器端异步渲染出来的，大部分爬虫无法获取到这些数据。 
  * 对于复杂的单页应用，渲染过程计算量大，对低端移动设备来说可能会有性能问题，用户能明显感知到首屏的渲染延迟。 

为了解决以上问题，有人提出能否将原本只运行在浏览器中的 JavaScript 渲染代码也在服务器端运行，在服务器端渲染出带内容的 HTML 后再返回。
这样就能让搜索引擎爬虫直接抓取到带数据的 HTML，同时也能降低首屏渲染时间。 由于 Node.js 的流行和成熟，以及虚拟 DOM
提出与实现，使这个假设成为可能。

实际上现在主流的前端框架都支持同构，包括 React、Vue2、Angular2，其中最先支持也是最成熟的同构方案是 React。 由于 React
使用者更多，它们之间又很相似，本节只介绍如何用 Webpack 构建 React 同构应用。

同构应用运行原理的核心在于虚拟 DOM，虚拟 DOM 的意思是不直接操作 DOM 而是通过 JavaScript Object 去描述原本的 DOM 结构。
在需要更新 DOM 时不直接操作 DOM 树，而是通过更新 JavaScript Object 后再映射成 DOM 操作。

虚拟 DOM 的优点在于：

  * 因为操作 DOM 树是高耗时的操作，尽量减少 DOM 树操作能优化网页性能。而 DOM Diff 算法能找出2个不同 Object 的最小差异，得出最小 DOM 操作； 
  * 虚拟 DOM 的在渲染的时候不仅仅可以通过操作 DOM 树来表示出结果，也能有其它的表示方式，例如把虚拟 DOM 渲染成字符串(服务器端渲染)，或者渲染成手机 App 原生的 UI 组件( React Native)。 

以 React 为例，核心模块 react 负责管理 React 组件的生命周期，而具体的渲染工作可以交给 ` react-dom ` 模块来负责。

` react-dom ` 在渲染虚拟 DOM 树时有2中方式可选：

  * 通过 ` render() ` 函数去操作浏览器 DOM 树来展示出结果。 
  * 通过 ` renderToString() ` 计算出表示虚拟 DOM 的 HTML 形式的字符串。 

构建同构应用的最终目的是从一份项目源码中构建出2份 JavaScript 代码，一份用于在浏览器端运行，一份用于在 Node.js 环境中运行渲染出
HTML。 其中用于在 Node.js 环境中运行的 JavaScript 代码需要注意以下几点：

  * 不能包含浏览器环境提供的 API，例如使用 ` document ` 进行 DOM 操作，因为 Node.js 不支持这些 API； 
  * 不能包含 CSS 代码，因为服务端渲染的目的是渲染出 HTML 内容，渲染出 CSS 代码会增加额外的计算量，影响服务端渲染性能； 
  * 不能像用于浏览器环境的输出代码那样把 ` node_modules ` 里的第三方模块和 Node.js 原生模块(例如 ` fs ` 模块)打包进去，而是需要通过 CommonJS 规范去引入这些模块。 
  * 需要通过 CommonJS 规范导出一个渲染函数，以用于在 HTTP 服务器中去执行这个渲染函数，渲染出 HTML 内容返回。 

###  解决方案

用于构建浏览器环境代码的 ` webpack.config.js ` 配置文件保留不变，新建一个专门用于构建服务端渲染代码的配置文件 `
webpack_server.config.js ` ，内容如下：

    
    
    const path = require('path');
    const nodeExternals = require('webpack-node-externals');
    
    module.exports = {
      // JS 执行入口文件
      entry: './main_server.js',
      // 为了不把 Node.js 内置的模块打包进输出文件中，例如 fs net 模块等
      target: 'node',
      // 为了不把 node_modules 目录下的第三方模块打包进输出文件中
      externals: [nodeExternals()],
      output: {
        // 为了以 CommonJS2 规范导出渲染函数，以给采用 Node.js 编写的 HTTP 服务调用
        libraryTarget: 'commonjs2',
        // 把最终可在 Node.js 中运行的代码输出到一个 bundle_server.js 文件
        filename: 'bundle_server.js',
        // 输出文件都放到 dist 目录下
        path: path.resolve(__dirname, './dist'),
      },
      module: {
        rules: [
          {
            test: /\.js$/,
            use: ['babel-loader'],
            exclude: path.resolve(__dirname, 'node_modules'),
          },
          {
            // CSS 代码不能被打包进用于服务端的代码中去，忽略掉 CSS 文件
            test: /\.css/,
            use: ['ignore-loader'],
          },
        ]
      },
      devtool: 'source-map' // 输出 source-map 方便直接调试 ES6 源码
    };

以上代码有几个关键的地方，分别是：

  * ` target: 'node' ` 由于输出代码的运行环境是 Node.js，源码中依赖的 Node.js 原生模块没必要打包进去； 
  * ` externals: [nodeExternals()] ` ` webpack-node-externals ` 的目的是为了防止 ` node_modules ` 目录下的第三方模块被打包进去，因为 Node.js 默认会去 ` node_modules ` 目录下寻找和使用第三方模块； 
  * ` {test: /\.css/, use: ['ignore-loader']} ` 忽略掉依赖的 CSS 文件，CSS 会影响服务端渲染性能，又是做服务端渲不重要的部分； 
  * ` libraryTarget ` : ` 'commonjs2' ` 以 CommonJS2 规范导出渲染函数，以供给采用 Node.js 编写的 HTTP 服务器代码调用。 

为了最大限度的复用代码，需要调整下目录结构：

把页面的根组件放到一个单独的文件 ` AppComponent.js `
，该文件只能包含根组件的代码，不能包含渲染入口的代码，而且需要导出根组件以供给渲染入口调用， ` AppComponent.js ` 内容如下：

    
    
    import React, { Component } from 'react';
    import './main.css';
    
    export class AppComponent extends Component {
      render() {
        return <h1>Hello,Webpack</h1>
      }
    }
    

分别为不同环境的渲染入口写两份不同的文件，分别是用于浏览器端渲染 DOM 的 ` main_browser.js ` 文件，和用于服务端渲染 HTML
字符串的 ` main_server.js ` 文件。

` main_browser.js ` 文件内容如下：

    
    
    import React from 'react';
    import { render } from 'react-dom';
    import { AppComponent } from './AppComponent';
    
    // 把根组件渲染到 DOM 树上
    render(<AppComponent/>, window.document.getElementById('app'));
    

` main_server.js ` 文件内容如下：

为了能把渲染的完整 HTML 文件通过 HTTP 服务返回给请求端，还需要通过用 Node.js 编写一个 HTTP 服务器。 由于本节不专注于将 HTTP
服务器的实现，就采用了 ExpressJS 来实现， ` http_server.js ` 文件内容如下：

    
    
    const express = require('express');
    const { render } = require('./dist/bundle_server');
    const app = express();
    
    // 调用构建出的 bundle_server.js 中暴露出的渲染函数，再拼接下 HTML 模版，形成完整的 HTML 文件
    app.get('/', function (req, res) {
      res.send(`
    <html>
    <head>
      <meta charset="UTF-8">
    </head>
    <body>
    <div id="app">${render()}</div>
    <!--导入 Webpack 输出的用于浏览器端渲染的 JS 文件-->
    <script src="./dist/bundle_browser.js"></script>
    </body>
    </html>
      `);
    });
    
    // 其它请求路径返回对应的本地文件
    app.use(express.static('.'));
    
    app.listen(3000, function () {
      console.log('app listening on port 3000!')
    });
    

再安装新引入的第三方依赖：

    
    
    # 安装 Webpack 构建依赖
    npm i -D css-loader style-loader ignore-loader webpack-node-externals
    # 安装 HTTP 服务器依赖
    npm i -S express
    

以上所有准备工作已经完成，接下来执行构建，编译出目标文件：

  * 执行命令 ` webpack --config webpack_server.config.js ` 构建出用于服务端渲染的 ` ./dist/bundle_server.js ` 文件。 
  * 执行命令 ` webpack ` 构建出用于浏览器环境运行的 ` ./dist/bundle_browser.js ` 文件，默认的配置文件为 ` webpack.config.js ` 。 

构建执行完成后，执行 ` node ./http_server.js ` 启动 HTTP 服务器后，再用浏览器去访问 [ http://localhost
]() :3000 就能看到 Hello,Webpack 了。
但是为了验证服务端渲染的结果，你需要打开浏览器的开发工具中的网络抓包一栏，再重新刷新浏览器后，就能抓到请求 HTML 的包了，抓包效果图如下：

可以看到服务器返回的是渲染出内容后的 HTML 而不是 HTML 模版，这说明同构应用的改造完成。

> 本实例提供 [ 项目完整代码 ]()

##  构建Electron应用

Electron 是 Node.js 和 Chromium 浏览器的结合体，用 Chromium 浏览器显示出的 Web 页面作为应用的 GUI，通过
Node.js 去和操作系统交互。 当你在 Electron 应用中的一个窗口操作时，实际上是在操作一个网页。当你的操作需要通过操作系统去完成时，网页会通过
Node.js 去和操作系统交互。

采用这种方式开发桌面端应用的优点有：

  * 降低开发门槛，只需掌握网页开发技术和 Node.js 即可，大量的 Web 开发技术和现成库可以复用于 Electron； 
  * 由于 Chromium 浏览器和 Node.js 都是跨平台的，Electron 能做到写一份代码在不同的操作系统运行。 

在运行 Electron 应用时，会从启动一个主进程开始。主进程的启动是通过 Node.js 去执行一个入口 JavaScript 文件实现的，这个入口文件
` main.js ` 内容如下：

<p data-height="565" data-theme-id="0" data-slug-hash="vjweQv" data-default-
tab="js" data-user="whjin" data-embed-version="2" data-pen-title="Electron-
main.js" class="codepen">See the Pen [ Electron-main.js ]() by whjin ( [
@whjin ]() ) on [ CodePen ]() .</p>  


主进程启动后会一直驻留在后台运行，你眼睛所看得的和操作的窗口并不是主进程，而是由主进程新启动的窗口子进程。

应用从启动到退出有一系列生命周期事件，通过 ` electron.app.on() ` 函数去监听生命周期事件，在特定的时刻做出反应。 例如在 `
app.on('ready') ` 事件中通过 ` BrowserWindow ` 去展示应用的主窗口。

启动的窗口其实是一个网页，启动时会去加载在 ` loadURL ` 中传入的网页地址。
每个窗口都是一个单独的网页进程，窗口之间的通信需要借助主进程传递消息。

总体来说开发 Electron 应用和开发 Web 应用很相似，区别在于 Electron 的运行环境同时内置了浏览器和 Node.js 的
API，在开发网页时除了可以使用浏览器提供的 API 外，还可以使用 Node.js 提供的 API。

###  接入 Webpack

接下来做一个简单的 Electron 应用，要求为应用启动后显示一个主窗口，在主窗口里有一个按钮，点击这个按钮后新显示一个窗口，且使用 React
开发网页。

由于 Electron 应用中的每一个窗口对应一个网页，所以需要开发2个网页，分别是主窗口的 ` index.html ` 和新打开的窗口 `
login.html ` 。

需要改动的地方如下：

  * 在项目根目录下新建主进程的入口文件 ` main.js ` ，内容和上面提到的一致； 
  * 主窗口网页的代码如下： 

    
    
    import React, { Component } from 'react';
    import { render } from 'react-dom';
    import { remote } from 'electron';
    import path from 'path';
    import './index.css';
    
    class App extends Component {
    
      // 在按钮被点击时
      handleBtnClick() {
        // 新窗口对应的页面的 URI 地址
        const modalPath = path.join('file://', remote.app.getAppPath(), 'dist/login.html');
        // 新窗口的大小
        let win = new remote.BrowserWindow({ width: 400, height: 320 })
        win.on('close', function () {
          // 窗口被关闭时清空资源
          win = null
        })
        // 加载网页
        win.loadURL(modalPath)
        // 显示窗口
        win.show()
      }
      
      render() {
        return (
          <div>
            <h1>Page Index</h1>
            <button onClick={this.handleBtnClick}>Open Page Login</button>
          </div>
        )
      }
    }
    
    render(<App/>, window.document.getElementById('app'));

其中最关键的部分在于在按钮点击事件里通过 ` electron ` 库里提供的 API 去新打开一个窗口，并加载网页文件所在的地址。

页面部分的代码已经修改完成，接下来修改构建方面的代码。 这里构建需要做到以下几点：

  * 构建出2个可在浏览器里运行的网页，分别对应2个窗口的界面； 
  * 由于在网页的 JavaScript 代码里可能会有调用 Node.js 原生模块或者 electron 模块，也就是输出的代码依赖这些模块。但由于这些模块都是内置支持的，构建出的代码不能把这些模块打包进去。 

要完成以上要求非常简单，因为 Webpack 内置了对 Electron 的支持。 只需要给 Webpack 配置文件加上一行代码即可，如下：

    
    
    target: 'electron-renderer',
    

以上修改都完成后重新执行 Webpack 构建，对应的网页需要的代码都输出到了项目根目录下的 ` dist ` 目录里。

为了以 Electron 应用的形式运行，还需要安装新依赖：

    
    
    # 安装 Electron 执行环境到项目中
    npm i -D electron
    

##  构建Npm模块

发布到 Npm 仓库的模块有以下几个特点：

  * 每个模块根目录下都必须有一个描述该模块的 ` package.json ` 文件。该文件描述了模块的入口文件是哪个，该模块又依赖哪些模块等。 
  * 模块中的文件以 JavaScript 文件为主，但不限于 JavaScript 文件。例如一个 UI 组件模块可能同时需要 JavaScript、CSS、图片文件等。 
  * 模块中的代码大多采用模块化规范，因为你的这个模块可能依赖其它模块，而且别的模块又可能依赖你的这个模块。因为目前支持比较广泛的是 CommonJS 模块化规范，上传到 Npm 仓库的代码最好遵守该规范。 

###  抛出问题

Webpack 不仅可用于构建运行的应用，也可用于构建上传到 Npm 的模块。 接下来用教大家如何用 Webpack 构建一个可上传的 Npm 仓库的
React 组件，具体要求如下：

  1. 源代码采用 ES6 写，但发布到 Npm 仓库的需要是 ES5 的，并且遵守 CommonJS 模块化规范。如果发布到 Npm 上去的 ES5 代码是经过转换的，请同时提供 Source Map 以方便调试。 
  2. 该 UI 组件依赖的其它资源文件例如 CSS 文件也需要包含在发布的模块里。 
  3. 尽量减少冗余代码，减少发布出去的组件的代码文件大小。 
  4. 发布出去的组件的代码中不能含有其依赖的模块的代码，而是让用户可选择性的去安装。例如不能内嵌 React 库的代码，这样做的目的是在其它组件也依赖 React 库时，防止 React 库的代码被重复打包。 

在开始前先看下最终发布到 Npm 仓库的模块的目录结构：

    
    
    node_modules/hello-webpack
    ├── lib
    │   ├── index.css (组件所有依赖的 CSS 都在这个文件中)
    │   ├── index.css.map
    │   ├── index.js (符合 CommonJS 模块化规范的 ES5 代码)
    │   └── index.js.map
    ├── src (ES6 源码)
    │   ├── index.css
    │   └── index.js
    └── package.json (模块描述文件)
    

` src/index.js ` 文件，内容如下：

    
    
    import React, { Component } from 'react';
    import './index.css';
    
    // 导出该组件供给其它模块使用
    export default class HelloWebpack extends Component {
      render() {
        return <h1 className="hello-component">Hello,Webpack</h1>
      }
    }
    

要使用该模块时只需要这样：

    
    
    // 通过 ES6 语法导入
    import HelloWebpack from 'hello-webpack';
    import 'hello-webpack/lib/index.css';
    
    // 或者通过 ES5 语法导入
    var HelloWebpack = require('hello-webpack');
    require('hello-webpack/lib/index.css');
    
    // 使用 react-dom 渲染
    render(<HelloWebpack/>);
    

###  使用 Webpack 构建 Npm 模块

**对于要求1，可以这样做到：**

  * 使用 ` babel-loader ` 把 ES6 代码转换成 ES5 的代码。 
  * 通过开启 ` devtool: 'source-map' ` 输出 Source Map 以发布调试。 
  * 设置 ` output.libraryTarget='commonjs2' ` 使输出的代码符合CommonJS2 模块化规范，以供给其它模块导入使用。 

相关的 Webpack 配置代码如下：

    
    
    module.exports = {
      output: {
        // 输出的代码符合 CommonJS 模块化规范，以供给其它模块导入使用。
        libraryTarget: 'commonjs2',
      },
      // 输出 Source Map
      devtool: 'source-map',
    };
    

**对于要求2，需要通过` css-loader ` 和 ` extract-text-webpack-plugin ` 实现，相关的 Webpack
配置代码如下： **

    
    
    const ExtractTextPlugin = require('extract-text-webpack-plugin');
    
    module.exports = {
      module: {
        rules: [
          {
            // 增加对 CSS 文件的支持
            test: /\.css/,
            // 提取出 Chunk 中的 CSS 代码到单独的文件中
            use: ExtractTextPlugin.extract({
              use: ['css-loader']
            }),
          },
        ]
      },
      plugins: [
        new ExtractTextPlugin({
          // 输出的 CSS 文件名称
          filename: 'index.css',
        }),
      ],
    };
    

此步引入了3个新依赖：

    
    
    # 安装 Webpack 构建所需要的新依赖
    npm i -D style-loader css-loader extract-text-webpack-plugin
    

**对于要求3，需要注意的是 Babel 在把 ES6 代码转换成 ES5 代码时会注入一些辅助函数。**

例如下面这段 ES6 代码：

    
    
    class HelloWebpack extends Component{
    }
    

在被转换成能正常运行的 ES5 代码时需要以下2个辅助函数：

  * ` babel-runtime/helpers/createClass ` 用于实现 ` class ` 语法 
  * ` babel-runtime/helpers/inherits ` 用于实现 ` extends ` 语法 

默认的情况下 Babel
会在每个输出文件中内嵌这些依赖的辅助函数的代码，如果多个源代码文件都依赖这些辅助函数，那么这些辅助函数的代码将会重复的出现很多次，造成代码冗余。

为了不让这些辅助函数的代重复出现，可以在依赖它们的时候通过 ` require('babel-runtime/helpers/createClass') `
的方式去导入，这样就能做到只让它们出现一次。 ` babel-plugin-transform-runtime ` 插件就是用来做这个事情的。

修改 ` .babelrc ` 文件，为其加入 ` transform-runtime ` 插件：

    
    
    {
      "plugins": [
        [
          "transform-runtime",
          {
            // transform-runtime 默认会自动的为你使用的 ES6 API 注入 polyfill
            // 假如你在源码中使用了 Promise，输出的代码将会自动注入 require('babel-runtime/core-js/Promise') 语句
            // polyfill 的注入应该交给模块使用者，因为使用者可能在其它地方已经注入了其它的 Promise polyfill 库
            // 所以关闭该功能
            "polyfill": false
          }
        ]
      ]
    }
    

由于加入 ` babel-plugin-transform-runtime ` 后生成的代码中会大量出现类似 ` require('babel-
runtime/helpers/createClass') ` 这样的语句，所以输出的代码将依赖 ` babel-runtime ` 模块。

此步引入了3个新依赖：

    
    
    # 安装 Webpack 构建所需要的新依赖
    npm i -D babel-plugin-transform-runtime
    # 安装输出代码运行时所需的新依赖
    npm i -S babel-runtime
    

**对于要求4，需要通过在[ 其它配置项 ]() 中介绍过的 ` Externals ` 来实现。 **

Externals 用来告诉 Webpack 要构建的代码中使用了哪些不用被打包的模块，也就是说这些模版是外部环境提供的，Webpack
在打包时可以忽略它们。

相关的 Webpack 配置代码如下：

    
    
    module.exports = {
      // 通过正则命中所有以 react 或者 babel-runtime 开头的模块
      // 这些模块通过注册在运行环境中的全局变量访问，不用被重复打包进输出的代码里
      externals: /^(react|babel-runtime)/,
    };
    

开启以上配置后，输出的代码中会存在导入 ` react ` 或者 ` babel-runtime ` 模块的代码，但是它们的 ` react ` 或者 `
babel-runtime ` 的内容不会被包含进去，如下：

    
    
    [
        (function (module, exports) {
            module.exports = require("babel-runtime/helpers/inherits");
        }),
        (function (module, exports) {
            module.exports = require("react");
        })
    ]
    

这样就做到了在保持代码正确性的情况下，输出文件不存放 react 或者 babel-runtime 模块的代码。

实际上当你在开发 Npm 模块时，不只需要对 react 和 babel-runtime
模块做这样的处理，而是需要对所有正在开发的模块所依赖的模块进行这样的处理。 因为正在开发的模块所依赖的模块也可能被其它模块所依赖。
当一个项目中一个模块被依赖多次时，Webpack 只会将其打包一次。

完成以上4步后最终的 Webpack 完整配置代码如下：

    
    
    const path = require('path');
    const ExtractTextPlugin = require('extract-text-webpack-plugin');
    
    module.exports = {
      // 模块的入口文件
      entry: './src/index.js',
      output: {
        // 输出文件的名称
        filename: 'index.js',
        // 输出文件的存放目录
        path: path.resolve(__dirname, 'lib'),
        // 输出的代码符合 CommonJS 模块化规范，以供给其它模块导入使用。
        libraryTarget: 'commonjs2',
      },
      // 通过正则命中所有以 react 或者 babel-runtime 开头的模块，
      // 这些模块使用外部的，不能被打包进输出的代码里，防止它们出现多次。
      externals: /^(react|babel-runtime)/,
      module: {
        rules: [
          {
            test: /\.js$/,
            use: ['babel-loader'],
            // 排除 node_modules 目录下的文件，
            // node_modules 目录下的文件都是采用的 ES5 语法，没必要再通过 Babel 去转换。
            exclude: path.resolve(__dirname, 'node_modules'),
          },
          {
            // 增加对 CSS 文件的支持
            test: /\.css/,
            // 提取出 Chunk 中的 CSS 代码到单独的文件中
            use: ExtractTextPlugin.extract({
              use: ['css-loader']
            }),
          },
        ]
      },
      plugins: [
        new ExtractTextPlugin({
          // 输出的 CSS 文件名称
          filename: 'index.css',
        }),
      ],
      // 输出 Source Map
      devtool: 'source-map',
    };

重新执行构建后，你将会在项目目录下看到一个新目录 ` lib ` ，里面放着要发布到 Npm 仓库的最终代码。

###  发布到 Npm

在把构建出的代码发布到 Npm 仓库前，还需要确保你的模块描述文件 ` package.json ` 是正确配置的。

由于构建出的代码的入口文件是 ` ./lib/index.js ` ，需要修改 ` package.json ` 中的 ` main ` 字段如下：

    
    
    {
      "main": "lib/index.js",
      "jsnext:main": "src/index.js"
    }
    

其中 ` jsnext:main ` 字段用于指出采用 ES6 编写的模块入口文件所在的位置。

修改完毕后在项目目录下执行 ` npm publish ` 就能把构建出的代码发布到 Npm 仓库中(确保已经 ` npm login ` 过)。

> 如果你想让发布到 Npm 上去的代码保持和源码的目录结构一致，那么用 Webpack 将不在适合。 因为源码是一个个分割的模块化文件，而 Webpack
> 会把这些模块组合在一起。 虽然 Webpack 输出的文件也可以是采用 CommonJS 模块化语法的，但在有些场景下把所有模块打包成一个文件发布到
> Npm 是不适合的。 例如像 Lodash
> 这样的工具函数库在项目中可能只用到了其中几个工具函数，如果所有工具函数打包在一个文件中，那么所有工具函数都会被打包进去，而保持模块文件的独立能做到只打包进使用到的。
> 还有就是像 UI 组件库这样由大量独立组件组成的库也和 Lodash 类似。  
>  所以 Webpack 适合于构建完整不可分割的 Npm 模块。

##  构建离线应用

离线应用的核心是离线缓存技术，历史上曾先后出现2种离线离线缓存技术，它们分别是：

  1. AppCache 又叫 Application Cache，目前已经从 Web 标准中删除，请尽量不要使用它。 
  2. [ Service Workers ]() 是目前最新的离线缓存技术，是 Web Worker 的一部分。 它通过拦截网络请求实现离线缓存，比 AppCache 更加灵活。它也是构建 [ PWA ]() 应用的关键技术之一。 

###  认识 Service Workers

Service Workers 是一个在浏览器后台运行的脚本，它生命周期完全独立于网页。它无法直接访问 DOM，但可以通过 postMessage
接口发送消息来和 UI 进程通信。 拦截网络请求是 Service Workers 的一个重要功能，通过它能完成离线缓存、编辑响应、过滤响应等功能。

###  Service Workers 兼容性

目前 Chrome、Firefox、Opera 都已经全面支持 Service Workers，但对于移动端浏览器就不太乐观了，只有高版本的 Android
支持。 由于 Service Workers 无法通过注入 ` polyfill ` 去实现兼容，所以在你打算使用它前请先调查清楚你的网页的运行场景。

判断浏览器是否支持 Service Workers 的最简单的方法是通过以下代码：

    
    
    // 如果 navigator 对象上存在 serviceWorker 对象，就表示支持
    if (navigator.serviceWorker) {
      // 通过 navigator.serviceWorker 使用
    }
    

###  注册 Service Workers

要给网页接入 Service Workers，需要在网页加载后注册一个描述 Service Workers 逻辑的脚本。 代码如下：

    
    
    if (navigator.serviceWorker) {
      window.addEventListener('DOMContentLoaded',function() {
        // 调用 serviceWorker.register 注册，参数 /sw.js 为脚本文件所在的 URL 路径
          navigator.serviceWorker.register('/sw.js');
      });
    }
    

一旦这个脚本文件被加载，Service Workers 的安装就开始了。这个脚本被安装到浏览器中后，就算用户关闭了当前网页，它仍会存在。
也就是说第一次打开该网页时 Service Workers 的逻辑不会生效，因为脚本还没有被加载和注册，但是以后再次打开该网页时脚本里的逻辑将会生效。

在 Chrome 中可以通过打开网址 ` chrome://inspect/#service-workers ` 来查看当前浏览器中所有注册了的
Service Workers。

###  使用 Service Workers 实现离线缓存

Service Workers 在注册成功后会在其生命周期中派发出一些事件，通过监听对应的事件在特点的时间节点上做一些事情。

在 Service Workers 脚本中，引入了新的关键字 ` self ` 代表当前的 Service Workers 实例。

在 Service Workers 安装成功后会派发出 ` install ` 事件，需要在这个事件中执行缓存资源的逻辑，实现代码如下：

    
    
    // 当前缓存版本的唯一标识符，用当前时间代替
    var cacheKey = new Date().toISOString();
    
    // 需要被缓存的文件的 URL 列表
    var cacheFileList = [
      '/index.html',
      '/app.js',
      '/app.css'
    ];
    
    // 监听 install 事件
    self.addEventListener('install', function (event) {
      // 等待所有资源缓存完成时，才可以进行下一步
      event.waitUntil(
        caches.open(cacheKey).then(function (cache) {
          // 要缓存的文件 URL 列表
          return cache.addAll(cacheFileList);
        })
      );
    });
    

接下来需要监听网络请求事件去拦截请求，复用缓存，代码如下：

    
    
    self.addEventListener('fetch', function(event) {
      event.respondWith(
        // 去缓存中查询对应的请求
        caches.match(event.request).then(function(response) {
            // 如果命中本地缓存，就直接返回本地的资源
            if (response) {
              return response;
            }
            // 否则就去用 fetch 下载资源
            return fetch(event.request);
          }
        )
      );
    });
    

以上就实现了离线缓存。

###  更新缓存

线上的代码有时需要更新和重新发布，如果这个文件被离线缓存了，那就需要 Service Workers 脚本中有对应的逻辑去更新缓存。 这可以通过更新
Service Workers 脚本文件做到。

浏览器针对 Service Workers 有如下机制：

  1. 每次打开接入了 Service Workers 的网页时，浏览器都会去重新下载 Service Workers 脚本文件（所以要注意该脚本文件不能太大），如果发现和当前已经注册过的文件存在字节差异，就将其视为“新服务工作线程”。 
  2. 新 Service Workers 线程将会启动，且将会触发其 ` install ` 事件。 
  3. 当网站上当前打开的页面关闭时，旧 Service Workers 线程将会被终止，新 Service Workers 线程将会取得控制权。 
  4. 新 Service Workers 线程取得控制权后，将会触发其 activate 事件。 

新 Service Workers 线程中的 activate 事件就是最佳的清理旧缓存的时间点，代码如下：

    
    
    // 当前缓存白名单，在新脚本的 install 事件里将使用白名单里的 key 
    var cacheWhitelist = [cacheKey];
    
    self.addEventListener('activate', function(event) {
      event.waitUntil(
        caches.keys().then(function(cacheNames) {
          return Promise.all(
            cacheNames.map(function(cacheName) {
              // 不在白名单的缓存全部清理掉
              if (cacheWhitelist.indexOf(cacheName) === -1) {
                // 删除缓存
                return caches.delete(cacheName);
              }
            })
          );
        })
      );
    });
    

最终完整的代码 Service Workers 脚本代码如下：

    
    
    // 当前缓存版本的唯一标识符，用当前时间代替
    var cacheKey = new Date().toISOString();
    
    // 当前缓存白名单，在新脚本的 install 事件里将使用白名单里的 key
    var cacheWhitelist = [cacheKey];
    
    // 需要被缓存的文件的 URL 列表
    var cacheFileList = [
      '/index.html',
      'app.js',
      'app.css'
    ];
    
    // 监听 install 事件
    self.addEventListener('install', function (event) {
      // 等待所有资源缓存完成时，才可以进行下一步
      event.waitUntil(
        caches.open(cacheKey).then(function (cache) {
          // 要缓存的文件 URL 列表
          return cache.addAll(cacheFileList);
        })
      );
    });
    
    // 拦截网络请求
    self.addEventListener('fetch', function (event) {
      event.respondWith(
        // 去缓存中查询对应的请求
        caches.match(event.request).then(function (response) {
            // 如果命中本地缓存，就直接返回本地的资源
            if (response) {
              return response;
            }
            // 否则就去用 fetch 下载资源
            return fetch(event.request);
          }
        )
      );
    });
    
    // 新 Service Workers 线程取得控制权后，将会触发其 activate 事件
    self.addEventListener('activate', function (event) {
      event.waitUntil(
        caches.keys().then(function (cacheNames) {
          return Promise.all(
            cacheNames.map(function (cacheName) {
              // 不在白名单的缓存全部清理掉
              if (cacheWhitelist.indexOf(cacheName) === -1) {
                // 删除缓存
                return caches.delete(cacheName);
              }
            })
          );
        })
      );
    });

###  接入 Webpack

用 Webpack 构建接入 Service Workers 的离线应用要解决的关键问题在于如何生成上面提到的 ` sw.js ` 文件， 并且 `
sw.js ` 文件中的 ` cacheFileList ` 变量，代表需要被缓存文件的 URL 列表，需要根据输出文件列表所对应的 URL
来决定，而不是像上面那样写成静态值。

假如构建输出的文件目录结构为：

    
    
    ├── app_4c3e186f.js
    ├── app_7cc98ad0.css
    └── index.html
    

那么 ` sw.js ` 文件中 ` cacheFileList ` 的值应该是：

    
    
    var cacheFileList = [
      '/index.html',
      'app_4c3e186f.js',
      'app_7cc98ad0.css'
    ];
    

Webpack 没有原生功能能完成以上要求，幸好庞大的社区中已经有人为我们做好了一个插件 [ serviceworker-webpack-plugin
]() 可以方便的解决以上问题。 使用该插件后的 Webpack 配置如下：

    
    
    const path = require('path');
    const ExtractTextPlugin = require('extract-text-webpack-plugin');
    const { WebPlugin } = require('web-webpack-plugin');
    const ServiceWorkerWebpackPlugin = require('serviceworker-webpack-plugin');
    
    module.exports = {
      entry: {
        app: './main.js'// Chunk app 的 JS 执行入口文件
      },
      output: {
        filename: '[name].js',
        publicPath: '',
      },
      module: {
        rules: [
          {
            test: /\.css/,// 增加对 CSS 文件的支持
            // 提取出 Chunk 中的 CSS 代码到单独的文件中
            use: ExtractTextPlugin.extract({
              use: ['css-loader'] // 压缩 CSS 代码
            }),
          },
        ]
      },
      plugins: [
        // 一个 WebPlugin 对应一个 HTML 文件
        new WebPlugin({
          template: './template.html', // HTML 模版文件所在的文件路径
          filename: 'index.html' // 输出的 HTML 的文件名称
        }),
        new ExtractTextPlugin({
          filename: `[name].css`,// 给输出的 CSS 文件名称加上 Hash 值
        }),
        new ServiceWorkerWebpackPlugin({
          // 自定义的 sw.js 文件所在路径
          // ServiceWorkerWebpackPlugin 会把文件列表注入到生成的 sw.js 中
          entry: path.join(__dirname, 'sw.js'),
        }),
      ],
      devServer: {
        // Service Workers 依赖 HTTPS，使用 DevServer 提供的 HTTPS 功能。
        https: true,
      }
    };

以上配置有2点需要注意：

  * 由于 Service Workers 必须在 HTTPS 环境下才能拦截网络请求实现离线缓存，使用在 DevServer https 中提到的方式去实现 HTTPS 服务。 
  * ` serviceworker-webpack-plugin ` 插件为了保证灵活性，允许使用者自定义 ` sw.js ` ，构建输出的 ` sw.js ` 文件中会在头部注入一个变量 ` serviceWorkerOption.assets ` 到全局，里面存放着所有需要被缓存的文件的 URL 列表。 

需要修改上面的 ` sw.js ` 文件中写成了静态值的 ` cacheFileList ` 为如下：

    
    
    // 需要被缓存的文件的 URL 列表
    var cacheFileList = global.serviceWorkerOption.assets;
    

以上已经完成所有文件的修改，在重新构建前，先安装新引入的依赖：

    
    
    npm i -D serviceworker-webpack-plugin webpack-dev-server
    

安装成功后，在项目根目录下执行 ` webpack-dev-server ` 命令后，DevServer 将以 HTTPS 模式启动。

##  搭配Npm Script

Npm Script 是一个任务执行者。 Npm 是在安装 Node.js 时附带的包管理器，Npm Script 则是 Npm 内置的一个功能，允许在 `
package.json ` 文件里面使用 ` scripts ` 字段定义任务：

    
    
    {
      "scripts": {
        "dev": "node dev.js",
        "pub": "node build.js"
      }
    }
    

里面的 ` scripts ` 字段是一个对象，每一个属性对应一段脚本，以上定义了两个任务 ` dev ` 和 ` pub ` 。 Npm Script
底层实现原理是通过调用 Shell 去运行脚本命令，例如执行 ` npm run pub ` 命令等同于执行命令 ` node build.js ` 。

Npm Script 还有一个重要的功能是能运行安装到项目目录里的 ` node_modules ` 里的可执行模块，例如在通过命令：

    
    
    npm i -D webpack
    

将 Webpack 安装到项目中后，是无法直接在项目根目录下通过命令 webpack 去执行 Webpack 构建的，而是要通过命令 `
./node_modules/.bin/webpack ` 去执行。

Npm Script 能方便的解决这个问题，只需要在 ` scripts ` 字段里定义一个任务，例如：

    
    
    {
      "scripts": {
        "build": "webpack"
      }
    }
    

Npm Script 会先去项目目录下的 ` node_modules ` 中寻找有没有可执行的 ` webpack `
文件，如果有就使用本地的，如果没有就使用全局的。 所以现在执行 Webpack 构建只需要通过执行 ` npm run build ` 去实现。

###  Webpack 为什么需要 Npm Script

Webpack 只是一个打包模块化代码的工具，并没有提供任何任务管理相关的功能。 但在实际场景中通常不会是只通过执行 webpack
就能完成所有任务的，而是需要多个任务才能完成。

  1. 在开发阶段为了提高开发体验，使用 DevServer 做开发，并且需要输出 Source Map 以方便调试，同时还需要开启自动刷新功能。 
  2. 为了减小发布到线上的代码尺寸，在构建出发布到线上的代码时，需要压缩输出的代码。 
  3. 在构建完发布到线上的代码后，需要把构建出的代码提交给发布系统。 

可以看出要求1和要求2是相互冲突的，其中任务3又依赖任务2。要满足以上三个要求，需要定义三个不同的任务。

接下来通过 Npm Script 来定义上面的3个任务：

    
    
    "scripts": {
      "dev": "webpack-dev-server --open",
      "dist": "NODE_ENV=production webpack --config webpack_dist.config.js",
      "pub": "npm run dist && rsync dist"
    },
    

含义分别是：

  * ` dev ` 代表用于开发时执行的任务，通过 DevServer 去启动构建。所以在开发项目时只需执行 ` npm run dev ` 。 
  * ` dist ` 代表构建出用于发布到线上去的代码，输出到 ` dist ` 目录中。其中的 ` NODE_ENV=production ` 是为了在运行任务时注入环境变量。 
  * ` pub ` 代表先构建出用于发布到线上去的代码，再同步 ` dist ` 目录中的文件到发布系统(如何同步文件需根据你所使用的发布系统而定)。所以在开发完后需要发布时只需执行 ` npm run pub ` 。 

使用 Npm Script 的好处是把一连串复杂的流程简化成了一个简单的命令，需要时只需要执行对应的那个简短的命令，而不用去手动的重复整个流程。
这会大大的提高我们的效率和降低出错率。

##  检查代码

检查代码和 Code Review 很相似，都是去审视提交的代码可能存在的问题。 但 Code Review
一般通过人去执行，而检查代码是通过机器去执行一些自动化的检查。 自动化的检查代码成本更低，实施代价更小。

检查代码主要检查以下几项：

  * 代码风格：让项目成员强制遵守统一的代码风格，例如如何缩紧、如何写注释等，保障代码可读性，不把时间浪费在争论如何写代码更好看上； 
  * 潜在问题：分析出代码在运行过程中可能出现的潜在 Bug。 

目前已经有成熟的工具可以检验诸如 JavaScript、TypeScript、CSS、SCSS 等常用语言。

###  检查 JavaScript

目前最常用的 JavaScript 检查工具是 ESlint ，它不仅内置了大量常用的检查规则，还可以通过插件机制做到灵活扩展。

ESlint 的使用很简单，在通过： ` npm i -g eslint `

按照到全局后，再在项目目录下执行： ` eslint init `

来新建一个 ESlint 配置文件 ` .eslintrc ` ，该文件格式为 JSON。

如果你想覆盖默认的检查规则，或者想加入新的检查规则，你需要修改该文件，例如使用以下配置：

    
    
    {
        // 从 eslint:recommended 中继承所有检查规则
        "extends": "eslint:recommended",
        // 再自定义一些规则     
        "rules": {
            // 需要在每行结尾加 ;        
            "semi": ["error", "always"],
            // 需要使用 "" 包裹字符串         
            "quotes": ["error", "double"]
        }
    }
    

写好配置文件后，再执行：

    
    
    eslint yourfile.js
    

去检查 ` yourfile.js ` 文件，如果你的文件没有通过检查，ESlint 会输出错误原因，例如：

###  检查 TypeScript

TSLint 是一个和 ESlint 相似的 TypeScript 代码检查工具，区别在于 TSLint 只专注于检查 TypeScript 代码。

TSLint 和 ESlint 的使用方法很相似，首先通过： ` npm i -g tslint `

安装到全局，再去项目根目录下执行： ` tslint --init `

生成配置文件 ` tslint.json ` ，在配置好后，再执行： ` tslint yourfile.ts ` 去检查 ` yourfile.ts `
文件。

###  检查 CSS

stylelint 是目前最成熟的 CSS 检查工具，内置了大量检查规则的同时也提供插件机制让用户自定义扩展。 stylelint 基于
PostCSS，能检查任何 PostCSS 能解析的代码，诸如 SCSS、Less 等。

首先通过 ` npm i -g stylelint `

安装到全局后，去项目根目录下新建 ` .stylelintrc ` 配置文件， 该配置文件格式为 JSON，其格式和 ESLint 的配置相似，例如：

    
    
    {
      // 继承 stylelint-config-standard 中的所有检查规则
      "extends": "stylelint-config-standard",
      // 再自定义检查规则  
      "rules": {
        "at-rule-empty-line-before": null
      }
    }
    

配置好后，再执行 ` stylelint "yourfile.css" ` 去检查 ` yourfile.css ` 文件。

###  结合 Webpack 检查代码

####  结合 ESLint

` eslint-loader ` 可以方便的把 ESLint 整合到 Webpack 中，使用方法如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.js$/,
            // node_modules 目录的下的代码不用检查
            exclude: /node_modules/,
            loader: 'eslint-loader',
            // 把 eslint-loader 的执行顺序放到最前面，防止其它 Loader 把处理后的代码交给 eslint-loader 去检查
            enforce: 'pre',
          },
        ],
      },
    }
    

接入 eslint-loader 后就能在控制台中看到 ESLint 输出的错误日志了。

####  结合 TSLint

` tslint-loader ` 是一个和 ` eslint-loader ` 相似的 Webpack Loader， 能方便的把 TSLint 整合到
Webpack，其使用方法如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.js$/,
            // node_modules 目录的下的代码不用检查
            exclude: /node_modules/,
            loader: 'tslint-loader',
            // 把 tslint-loader 的执行顺序放到最前面，防止其它 Loader 把处理后的代码交给 tslint-loader 去检查
            enforce: 'pre',
          },
        ],
      },
    }
    

####  结合 stylelint

StyleLintPlugin 能把 stylelint 整合到 Webpack，其使用方法很简单，如下：

    
    
    const StyleLintPlugin = require('stylelint-webpack-plugin');
    
    module.exports = {
      // ...
      plugins: [
        new StyleLintPlugin(),
      ],
    }
    

###  一些建议

把代码检查功能整合到 Webpack 中会导致以下问题：

  * 由于执行检查步骤计算量大，整合到 Webpack 中会导致构建变慢； 
  * 在整合代码检查到 Webpack 后，输出的错误信息是通过行号来定位错误的，没有编辑器集成显示错误直观； 

为了避免以上问题，还可以这样做：

  * 使用集成了代码检查功能的编辑器，让编辑器实时直观地显示错误； 
  * 把代码检查步骤放到代码提交时，也就是说在代码提交前去调用以上检查工具去检查代码，只有在检查都通过时才提交代码，这样就能保证提交到仓库的代码都是通过了检查的。 

如果你的项目是使用 Git 管理，Git 提供了 Hook 功能能做到在提交代码前触发执行脚本。

husky 可以方便快速地为项目接入 Git Hook， 执行 ` npm i -D husky `

安装 husky 时，husky 会通过 ` Npm Script Hook ` 自动配置好 Git Hook，你需要做的只是在 `
package.json ` 文件中定义几个脚本，方法如下：

    
    
    {
      "scripts": {
        // 在执行 git commit 前会执行的脚本  
        "precommit": "npm run lint",
        // 在执行 git push 前会执行的脚本  
        "prepush": "lint",
        // 调用 eslint、stylelint 等工具检查代码
        "lint": "eslint && stylelint"
      }
    }
    

` precommit ` 和 ` prepush ` 你需要根据自己的情况选择一个，无需两个都设置。

##  通过 Node.js API 启动 Webpack

Webpack 除了提供可执行的命令行工具外，还提供可在 Node.js 环境中调用的库。 通过 Webpack 暴露的 API，可直接在 Node.js
程序中调用 Webpack 执行构建。

通过 API 去调用并执行 Webpack 比直接通过可执行文件启动更加灵活，可用在一些特殊场景，下面将教你如何使用 Webpack 提供的 API。

> Webpack 其实是一个 Node.js 应用程序，它全部通过 JavaScript 开发完成。 在命令行中执行 ` webpack `
> 命令其实等价于执行 ` node ./node_modules/webpack/bin/webpack.js ` 。

###  安装和使用 Webpack 模块

在调用 Webpack API 前，需要先安装它：

    
    
    npm i -D webpack
    

安装成功后，可以采用以下代码导入 Webpack 模块：

    
    
    const webpack = require('webpack');
    
    // ES6 语法
    import webpack from "webpack";
    

导出的 ` webpack ` 其实是一个函数，使用方法如下：

    
    
    webpack({
      // Webpack 配置，和 webpack.config.js 文件一致
    }, (err, stats) => {
      if (err || stats.hasErrors()) {
        // 构建过程出错
      }
      // 成功执行完构建
    });
    

如果你的 Webpack 配置写在 ` webpack.config.js ` 文件中，可以这样使用：

    
    
    // 读取 webpack.config.js 文件中的配置
    const config = require('./webpack.config.js');
    webpack(config , callback);
    

###  以监听模式运行

以上使用 Webpack API 的方法只能执行一次构建，无法以监听模式启动 Webpack，为了在使用 API 时以监听模式启动，需要获取
Compiler 实例，方法如下：

    
    
    // 如果不传 callback 回调函数，就会返回一个 Compiler 实例，用于让你去控制启动，而不是像上面那样立即启动
    const compiler = webpack(config);
    
    // 调用 compiler.watch 以监听模式启动，返回的 watching 用于关闭监听
    const watching = compiler.watch({
      // watchOptions
      aggregateTimeout: 300,
    },(err, stats)=>{
      // 每次因文件发生变化而重新执行完构建后
    });
    
    // 调用 watching.close 关闭监听 
    watching.close(()=>{
      // 在监听关闭后
    });

##  使用 Webpack Dev Middleware

DevServer 是一个方便开发的小型 HTTP 服务器， DevServer 其实是基于 [ webpack-dev-middleware ]() 和
Expressjs 实现的， 而 webpack-dev-middleware 其实是 Expressjs 的一个中间件。

也就是说，实现 DevServer 基本功能的代码大致如下：

    
    
    const express = require('express');
    const webpack = require('webpack');
    const webpackMiddleware = require('webpack-dev-middleware');
    
    // 从 webpack.config.js 文件中读取 Webpack 配置 
    const config = require('./webpack.config.js');
    // 实例化一个 Expressjs app
    const app = express();
    
    // 用读取到的 Webpack 配置实例化一个 Compiler
    const compiler = webpack(config);
    // 给 app 注册 webpackMiddleware 中间件
    app.use(webpackMiddleware(compiler));
    // 启动 HTTP 服务器，服务器监听在 3000 端口 
    app.listen(3000);

从以上代码可以看出，从 ` webpack-dev-middleware ` 中导出的 ` webpackMiddleware `
是一个函数，该函数需要接收一个 Compiler 实例。Webpack API 导出的 ` webpack ` 函数会返回一个Compiler 实例。

` webpackMiddleware ` 函数的返回结果是一个 Expressjs 的中间件，该中间件有以下功能：

  * 接收来自 Webpack Compiler 实例输出的文件，但不会把文件输出到硬盘，而是保存在内存中； 
  * 往 Expressjs app 上注册路由，拦截 HTTP 收到的请求，根据请求路径响应对应的文件内容； 

通过 ` webpack-dev-middleware ` 能够将 DevServer 集成到你现有的 HTTP 服务器中，让你现有的 HTTP
服务器能返回 Webpack 构建出的内容，而不是在开发时启动多个 HTTP 服务器。 这特别适用于后端接口服务采用 Node.js 编写的项目。

###  Webpack Dev Middleware 支持的配置项

在 Node.js 中调用 webpack-dev-middleware 提供的 API 时，还可以给它传入一些配置项，方法如下：

    
    
    // webpackMiddleware 函数的第二个参数为配置项
    app.use(webpackMiddleware(compiler, {
        // webpack-dev-middleware 所有支持的配置项
        // 只有 publicPath 属性为必填，其它都是选填项
    
        // Webpack 输出资源绑定在 HTTP 服务器上的根目录，
        // 和 Webpack 配置中的 publicPath 含义一致 
        publicPath: '/assets/',
    
        // 不输出 info 类型的日志到控制台，只输出 warn 和 error 类型的日志
        noInfo: false,
    
        // 不输出任何类型的日志到控制台
        quiet: false,
    
        // 切换到懒惰模式，这意味着不监听文件变化，只会在请求到时再去编译对应的文件，
        // 这适合页面非常多的项目。
        lazy: true,
    
        // watchOptions
        // 只在非懒惰模式下才有效
        watchOptions: {
            aggregateTimeout: 300,
            poll: true
        },
    
        // 默认的 URL 路径, 默认是 'index.html'.
        index: 'index.html',
    
        // 自定义 HTTP 头
        headers: {'X-Custom-Header': 'yes'},
    
        // 给特定文件后缀的文件添加 HTTP mimeTypes ，作为文件类型映射表
        mimeTypes: {'text/html': ['phtml']},
    
        // 统计信息输出样式
        stats: {
            colors: true
        },
    
        // 自定义输出日志的展示方法
        reporter: null,
    
        // 开启或关闭服务端渲染
        serverSideRender: false,
    }));

###  Webpack Dev Middleware 与模块热替换

DevServer 提供了一个方便的功能，可以做到在监听到文件发生变化时自动替换网页中的老模块，以做到实时预览。

DevServer 虽然是基于 ` webpack-dev-middleware ` 实现的，但 ` webpack-dev-middleware `
并没有实现模块热替换功能，而是 DevServer 自己实现了该功能。

为了在使用 ` webpack-dev-middleware ` 时也能使用模块热替换功能去提升开发效率，需要额外的再接入 [ webpack-hot-
middleware ]() 。 需要做以下修改才能实现模块热替换。

第1步：修改 ` webpack.config.js ` 文件，加入 ` HotModuleReplacementPlugin ` 插件，修改如下：

    
    
    const HotModuleReplacementPlugin = require('webpack/lib/HotModuleReplacementPlugin');
    
    module.exports = {
      entry: [
        // 为了支持模块热替换，注入代理客户端
        'webpack-hot-middleware/client',
        // JS 执行入口文件
        './src/main.js'
      ],
      output: {
        // 把所有依赖的模块合并输出到一个 bundle.js 文件
        filename: 'bundle.js',
      },
      plugins: [
        // 为了支持模块热替换，生成 .hot-update.json 文件
        new HotModuleReplacementPlugin(),
      ],
      devtool: 'source-map',
    };

第2步：修改 HTTP 服务器代码 ` server.js ` 文件，接入 ` webpack-hot-middleware ` 中间件，修改如下：

    
    
    const express = require('express');
    const webpack = require('webpack');
    const webpackMiddleware = require('webpack-dev-middleware');
    
    // 从 webpack.config.js 文件中读取 Webpack 配置
    const config = require('./webpack.config.js');
    // 实例化一个 Expressjs app
    const app = express();
    
    // 用读取到的 Webpack 配置实例化一个 Compiler
    const compiler = webpack(config);
    // 给 app 注册 webpackMiddleware 中间件
    app.use(webpackMiddleware(compiler));
    // 为了支持模块热替换，响应用于替换老模块的资源
    app.use(require('webpack-hot-middleware')(compiler));
    // 把项目根目录作为静态资源目录，用于服务 HTML 文件
    app.use(express.static('.'));
    // 启动 HTTP 服务器，服务器监听在 3000 端口
    app.listen(3000, () => {
      console.info('成功监听在 3000');
    });

第3步：修改执行入口文件 ` main.js ` ，加入替换逻辑，在文件末尾加入以下代码：

    
    
    if (module.hot) {
      module.hot.accept();
    }
    

第4步：安装新引入的依赖：

    
    
    npm i -D webpack-dev-middleware webpack-hot-middleware express
    

安装成功后，通过 ` node ./server.js ` 就能启动一个类似于 DevServer 那样支持模块热替换的自定义 HTTP 服务了。

> 本实例提供 [ 项目完整代码 ]()

##  加载图片

在网页中不可避免的会依赖图片资源，例如 PNG、JPG、GIF，下面来教你如何用 Webpack 加载图片资源。

###  使用 ` file-loader `

[ file-loader ]() 可以把 JavaScript 和 CSS 中导入图片的语句替换成正确的地址，并同时把文件输出到对应的位置。

例如 CSS 源码是这样写的：

    
    
    #app {
      background-image: url(./imgs/a.png);
    }
    

被 ` file-loader ` 转换后输出的 CSS 会变成这样：

    
    
    #app {
      background-image: url(5556e1251a78c5afda9ee7dd06ad109b.png);
    }
    

并且在输出目录 ` dist ` 中也多出 ` ./imgs/a.png ` 对应的图片文件 ` hash.png ` ，
输出的文件名是根据文件内容的计算出的 Hash 值。

同理在 JavaScript 中导入图片的源码如下：

    
    
    import imgB from './imgs/b.png';
    
    window.document.getElementById('app').innerHTML = `
    <img src="${imgB}"/>
    `;
    

经过 ` file-loader ` 处理后输出的 JavaScript 代码如下：

    
    
    module.exports = __webpack_require__.p + "0bcc1f8d385f78e1271ebfca50668429.png";
    

也就是说 ` imgB ` 的值就是图片对应的 URL 地址。

在 Webpack 中使用 ` file-loader ` 非常简单，相关配置如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.png$/,
            use: ['file-loader']
          }
        ]
      }
    };
    

###  使用 ` url-loader `

[ url-loader ]() 可以把文件的内容经过 ` base64 ` 编码后注入到 JavaScript 或者 CSS 中去。

例如 CSS 源码是这样写的：

    
    
    #app {
      background-image: url(./imgs/a.png);
    }
    

被 ` url-loader ` 转换后输出的 CSS 会变成这样：

    
    
    #app {
      background-image: url(data:image/png;base64,iVBORw01afer...); /* 结尾省略了剩下的 base64 编码后的数据 */
    }
    

同理在 JavaScript 中效果也类似。

从上面的例子中可以看出 ` url-loader ` 会把根据图片内容计算出的 ` base64 `
编码的字符串直接注入到代码中，由于一般的图片数据量巨大，这会导致 JavaScript、CSS 文件也跟着变大。 所以在使用 ` url-loader `
时一定要注意图片体积不能太大，不然会导致 JavaScript、CSS 文件过大而带来的网页加载缓慢问题。

一般利用 ` url-loader ` 把网页需要用到的小图片资源注入到代码中去，以减少加载次数。因为在 HTTP/1 协议中，每加载一个资源都需要建立一次
HTTP 链接， 为了一个很小的图片而新建一次 HTTP 连接是不划算的。

` url-loader ` 考虑到了以上问题，并提供了一个方便的选择 ` limit ` ，该选项用于控制当文件大小小于 ` limit ` 时才使用 `
url-loader ` ，否则使用 ` fallback ` 选项中配置的 ` loader ` 。 相关 Webpack 配置如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.png$/,
            use: [{
              loader: 'url-loader',
              options: {
                // 30KB 以下的文件采用 url-loader
                limit: 1024 * 30,
                // 否则采用 file-loader，默认值就是 file-loader 
                fallback: 'file-loader',
              }
            }]
          }
        ]
      },
    };
    

除此之外，你还可以做以下优化：

  * 通过 [ imagemin-webpack-plugin ]() 压缩图片； 
  * 通过 [ webpack-spritesmith ]() 插件制作雪碧图。 

以上加载图片的方法同样适用于其它二进制类型的资源，例如 PDF、SWF 等等。

> 本实例提供 [ 项目完整代码 ]()

##  加载 SVG

SVG 作为矢量图的一种标准格式，已经得到了各大浏览器的支持，它也成为了 Web 中矢量图的代名词。 在网页中采用 SVG 代替位图有如下好处：

  1. SVG 相对于位图更清晰，在任意缩放的情况下后不会破坏图形的清晰度，SVG 能方便地解决高分辨率屏幕下图像显示不清楚的问题。 
  2. 在图形线条比较简单的情况下，SVG 文件的大小要小于位图，在扁平化 UI 流行的今天，多数情况下 SVG 会更小。 
  3. 图形相同的 SVG 比对应的高清图有更好的渲染性能。 
  4. SVG 采用和 HTML 一致的 XML 语法描述，灵活性很高。 

画图工具能导出一个个 ` .svg ` 文件，SVG 的导入方法和图片类似，既可以像下面这样在 CSS 中直接使用：

    
    
    body {
      background-image: url(./svgs/activity.svg);
    }
    

也可以在 HTML 中使用：

    
    
    <img src="./svgs/activity.svg"/>
    

也就是说可以直接把 SVG 文件当成一张图片来使用，方法和使用图片时完全一样。

使用 ` file-loader ` 和使用 ` url-loader ` 对 SVG 来说同样有效，只需要把 Loader test 配置中的文件后缀改成
` .svg ` ，代码如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.svg/,
            use: ['file-loader']
          }
        ]
      },
    };
    

由于 SVG 是文本格式的文件，除了以上两种方法外还有其它方法，下面来一一说明。

###  使用 ` raw-loader `

[ raw-loader ]() 可以把文本文件的内容读取出来，注入到 JavaScript 或 CSS 中去。

例如在 JavaScript 中这样写：

    
    
    import svgContent from './svgs/alert.svg';
    

经过 ` raw-loader ` 处理后输出的代码如下：

    
    
    module.exports = "<svg xmlns=\"http://www.w3.org/2000/svg\"... </svg>" // 末尾省略 SVG 内容
    

也就是说 ` svgContent ` 的内容就等于字符串形式的 SVG，由于 SVG 本身就是 HTML 元素，在获取到 SVG
内容后，可以直接通过以下代码将 SVG 插入到网页中：

    
    
    window.document.getElementById('app').innerHTML = svgContent;
    

使用 ` raw-loader ` 时相关的 Webpack 配置如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.svg$/,
            use: ['raw-loader']
          }
        ]
      }
    };
    

由于 ` raw-loader ` 会直接返回 SVG 的文本内容，并且无法通过 CSS 去展示 SVG 的文本内容，因此采用本方法后无法在 CSS 中导入
SVG。 也就是说在 CSS 中不可以出现 ` background-image: url(./svgs/activity.svg) ` 这样的代码，因为
` background-image: url(<svg>...</svg>) ` 是不合法的。

###  使用 ` svg-inline-loader `

[ svg-inline-loader ]() 和上面提到的 ` raw-loader ` 非常相似， 不同在于 ` svg-inline-loader `
会分析 SVG 的内容，去除其中不必要的部分代码，以减少 SVG 的文件大小。

在使用画图工具如 Adobe Illustrator、Sketch 制作 SVG 后，在导出时这些工具会生成对网页运行来说不必要的代码。 举个例子，以下是
Sketch 导出的 SVG 的代码：

    
    
    <svg class="icon" verison="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
         stroke="#000">
      <circle cx="12" cy="12" r="10"/>
    </svg>
    

被 ` svg-inline-loader ` 处理后会精简成如下：

    
    
    <svg viewBox="0 0 24 24" stroke="#000"><circle cx="12" cy="12" r="10"/></svg>
    

也就是说 ` svg-inline-loader ` 增加了对 SVG 的压缩功能。

使用 ` svg-inline-loader ` 时相关的 Webpack 配置如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.svg$/,
            use: ['svg-inline-loader']
          }
        ]
      }
    };   
    

##  加载 Source Map

由于在开发过程中经常会使用新语言去开发项目，最后会把源码转换成能在浏览器中直接运行的 JavaScript 代码。
这样做虽能提升开发效率，在调试代码的过程中你会发现生成的代码可读性非常差，这给代码调试带来了不便。

Webpack 支持为转换生成的代码输出对应的 Source Map 文件，以方便在浏览器中能通过源码调试。 控制 Source Map 输出的
Webpack 配置项是 ` devtool ` ，它有很多选项，下面来一一详细介绍。

devtool  |  含义   
---|---  
空  |  不生成 Source Map   
` eval ` |  每个 ` module ` 会封装到 ` eval ` 里包裹起来执行，并且会在每个 ` eval ` 语句的末尾追加注释 ` //# sourceURL=webpack:///./main.js `  
` source-map ` |  会额外生成一个单独 Source Map 文件，并且会在 JavaScript 文件末尾追加 ` //# sourceMappingURL=bundle.js.map `  
` hidden-source-map ` |  和 ` source-map ` 类似，但不会在 JavaScript 文件末尾追加 ` //# sourceMappingURL=bundle.js.map `  
` inline-source-map ` |  和 ` source-map ` 类似，但不会额外生成一个单独 Source Map 文件，而是把 Source Map 转换成 ` base64 ` 编码内嵌到 JavaScript 中   
` eval-source-map ` |  和 ` eval ` 类似，但会把每个模块的 Source Map 转换成 ` base64 ` 编码内嵌到 ` eval ` 语句的末尾，例如 ` //# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW... `  
` cheap-source-map ` |  和 ` source-map ` 类似，但生成的 Source Map 文件中没有列信息，因此生成速度更快   
` cheap-module-source-map ` |  和 ` cheap-source-map ` 类似，但会包含 Loader 生成的 Source Map   
  
其实以上表格只是列举了 ` devtool ` 可能取值的一部分， 它的取值其实可以由 ` source-map ` 、 ` eval ` 、 `
inline ` 、 ` hidden ` 、 ` cheap ` 、 ` module ` 这六个关键字随意组合而成。
这六个关键字每个都代表一种特性，它们的含义分别是：

  * ` eval ` ：用 ` eval ` 语句包裹需要安装的模块； 
  * ` source-map ` ：生成独立的 Source Map 文件； 
  * ` hidden ` ：不在 JavaScript 文件中指出 Source Map 文件所在，这样浏览器就不会自动加载 Source Map； 
  * ` inline ` ：把生成的 Source Map 转换成 ` base64 ` 格式内嵌在 JavaScript 文件中； 
  * ` cheap ` ：生成的 Source Map 中不会包含列信息，这样计算量更小，输出的 Source Map 文件更小；同时 Loader 输出的 Source Map 不会被采用； 
  * ` module ` ：来自 Loader 的 Source Map 被简单处理成每行一个模块； 

###  该如何选择

如果你不关心细节和性能，只是想在不出任何差错的情况下调试源码，可以直接设置成 ` source-map ` ，但这样会造成两个问题：

  * ` source-map ` 模式下会输出质量最高最详细的 Source Map，这会造成构建速度缓慢，特别是在开发过程需要频繁修改的时候会增加等待时间； 
  * ` source-map ` 模式下会把 Source Map 暴露出去，如果构建发布到线上的代码的 Source Map 暴露出去就等于源码被泄露； 

为了解决以上两个问题，可以这样做：

  * 在开发环境下把 ` devtool ` 设置成 ` cheap-module-eval-source-map ` ，因为生成这种 Source Map 的速度最快，能加速构建。由于在开发环境下不会做代码压缩，Source Map 中即使没有列信息也不会影响断点调试； 
  * 在生产环境下把 ` devtool ` 设置成 ` hidden-source-map ` ，意思是生成最详细的 Source Map，但不会把 Source Map 暴露出去。由于在生产环境下会做代码压缩，一个 JavaScript 文件只有一行，所以需要列信息。 

> 在生产环境下通常不会把 Source Map 上传到 HTTP 服务器让用户获取，而是上传到 JavaScript 错误收集系统，在错误收集系统上根据
> Source Map 和收集到的 JavaScript 运行错误堆栈计算出错误所在源码的位置。
>
> 不要在生产环境下使用 ` inline ` 模式的 Source Map， 因为这会使 JavaScript 文件变得很大，而且会泄露源码。

###  加载现有的 Source Map

有些从 Npm 安装的第三方模块是采用 ES6 或者 TypeScript 编写的，它们在发布时会同时带上编译出来的 JavaScript 文件和对应的
Source Map 文件，以方便你在使用它们出问题的时候调试它们；

默认情况下 Webpack 是不会去加载这些附加的 Source Map 文件的，Webpack 只会在转换过程中生成 Source Map。 为了让
Webpack 加载这些附加的 Source Map 文件，需要安装 [ source-map-loader ]() 。 使用方法如下：

    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.js$/,
            // 只加载你关心的目录下的 Source Map，以提升构建速度
            include: [path.resolve(root, 'node_modules/some-components/')],
            use: ['source-map-loader'],
            // 要把 source-map-loader 的执行顺序放到最前面，如果在 source-map-loader 之前有 Loader 转换了该 JavaScript 文件，会导致 Source Map 映射错误
            enforce: 'pre'
          }
        ]
      }
    };
    
    
    

> 由于 ` source-map-loader ` 在加载 Source Map 时计算量很大，因此要避免让该 Loader
> 处理过多的文件，不然会导致构建速度缓慢。 通常会采用 ` include ` 去命中只关心的文件。

再安装新引入的依赖：

    
    
    npm i -D source-map-loader
    

重启 Webpack 后，你就能在浏览器中调试 ` node_modules/some-components/ ` 目录下的源码了。

##  实战总结

在实际应用中，会遇到各种各样的需求，虽然前面的小节中已经给出了大部分场景需求的解决方案，但还是很难涵盖所有的可能性。
所以你自己需要有能力去分析遇到的问题，然后去寻找对应的解决方案，你可以按照以下思路去分析和解决问题：

  1. 对所面临的问题本身要了解。例如在用 Webpack 去构建 React 应用时你需要先掌握 React 的基础知识。 
  2. 找出现实和目标之间的差异。例如在 React 应用的源码中用到了 JSX 语法和 ES6 语法，需要把源码转换成 ES5。 
  3. 找出从现实到目标的可能路径。例如把新语法转换成 ES5 可以使用 Babel 去转换源码。 
  4. 搜索社区中有没有现成的针对可能路径的 Webpack 集成方案。例如社区中已经有 ` babel-loader ` 。 
  5. 如果找不到现成的方案说明你的需求非常特别，这时候你就需要编写自己的 Loader 或者 Plugin 了。 

在解决问题的过程中有以下2点能力很重要：

  1. 从一个知识你需要尽可能多的联想到其相关连的知识，这有利于打通你的知识体系,从经验中更快地得出答案。 
  2. 善于使用搜索引擎去寻找你所面临的问题，这有利于借助他人的经验更快地得出答案，而不是自己重新探索。 

最重要的是你需要多实战，自己去解决问题，这有利于加深你的影响和理解，而不是只看不做。

