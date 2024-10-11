---
date: 2023-01-10
category:
    - webpack
tag:
    - webpack
    - javascript
    - 前端
    - 前端工程化
    - 前端构建
---
 # Webpack附录
##  Webpack附录

> 查看所有文档页面： [ 全栈开发 ]() ，获取更多信息。  
>  原文链接： [ webpack原理 ]() ，原文广告模态框遮挡，阅读体验不好，所以整理成本文，方便查找。

##  常用 Loaders

###  加载文件

  * [ raw-loader ]() ：把文本文件的内容加载到代码中去，在 [ 3-20加载SVG ]() 中有介绍。 
  * [ file-loader ]() ：把文件输出到一个文件夹中，在代码中通过相对 URL 去引用输出的文件，在 [ 3-19加载图片 ]() 、 [ 3-20加载 SVG ]() 、 [ 4-9 CDN 加速 ]() 中有介绍。 
  * [ url-loader ]() ：和 ` file-loader ` 类似，但是能在文件很小的情况下以 ` base64 ` 的方式把文件内容注入到代码中去，在 [ 3-19加载图片 ]() 、 [ 3-20加载 SVG ]() 中有介绍。 
  * [ source-map-loader ]() ：加载额外的 Source Map 文件，以方便断点调试，在 [ 3-21加载 Source Map ]() 中有介绍。 
  * [ svg-inline-loader ]() ：把压缩后的 SVG 内容注入到代码中，在 [ 3-20加载 SVG ]() 中有介绍。 
  * [ node-loader ]() ：加载 Node.js 原生模块 .node 文件。 
  * [ image-loader ]() ：加载并且压缩图片文件。 
  * [ json-loader ]() ：加载 JSON 文件。 
  * [ yaml-loader ]() ：加载 YAML 文件。 

###  编译模版

  * [ pug-loader ]() ：把 Pug 模版转换成 JavaScript 函数返回。 
  * [ handlebars-loader ]() ：把 Handlebars 模版编译成函数返回。 
  * [ ejs-loader ]() ：把 EJS 模版编译成函数返回。 
  * [ haml-loader ]() ：把 HAML 代码转换成 HTML。 
  * [ markdown-loader ]() ：把 Markdown 文件转换成 HTML。 

###  转换脚本语言

  * [ babel-loader ]() ：把 ES6 转换成 ES5，在 [ 3-1使用 ES6 语言 ]() 中有介绍。 
  * [ ts-loader ]() ：把 TypeScript 转换成 JavaScript，在 [ 3-2使用 TypeScript 语言 ]() 中有遇到。 
  * [ awesome-typescript-loader ]() ：把 TypeScript 转换成 JavaScript，性能要比 ` ts-loader ` 好。 
  * [ coffee-loader ]() ：把 CoffeeScript 转换成 JavaScript。 

###  转换样式文件

  * [ css-loader ]() ：加载 CSS，支持模块化、压缩、文件导入等特性。 
  * [ style-loader ]() ：把 CSS 代码注入到 JavaScript 中，通过 DOM 操作去加载 CSS。 
  * [ sass-loader ]() ：把 SCSS/SASS 代码转换成 CSS，在 [ 3-4使用 SCSS 语言 ]() 中有介绍。 
  * [ postcss-loader ]() ：扩展 CSS 语法，使用下一代 CSS，在 [ 3-5使用 PostCSS ]() 中有介绍。 
  * [ less-loader ]() ：把 Less 代码转换成 CSS 代码。 
  * [ stylus-loader ]() ：把 Stylus 代码转换成 CSS 代码。 

###  检查代码

  * [ eslint-loader ]() ：通过 ESLint 检查 JavaScript 代码，在 [ 3-16检查代码 ]() 中有介绍。 
  * [ tslint-loader ]() ：通过 TSLint 检查 TypeScript 代码。 
  * [ mocha-loader ]() ：加载 Mocha 测试用例代码。 
  * [ coverjs-loader ]() ：计算测试覆盖率。 

###  其它

  * [ vue-loader ]() ：加载 Vue.js 单文件组件，在 [ 3-7使用 Vue 框架 ]() 中有介绍。 
  * [ i18n-loader ]() ：加载多语言版本，支持国际化。 
  * [ ignore-loader ]() ：忽略掉部分文件，在 [ 3-11构建同构应用 ]() 中有介绍。 
  * [ ui-component-loader ]() ：按需加载 UI 组件库，例如在使用 antd UI 组件库时，不会因为只用到了 Button 组件而打包进所有的组件。 

##  常用 Plugins

###  用于修改行为

  * [ define-plugin ]() ：定义环境变量，在 [ 4-7区分环境 ]() 中有介绍。 
  * [ context-replacement-plugin ]() ：修改 require 语句在寻找文件时的默认行为。 
  * [ ignore-plugin ]() ：用于忽略部分文件。 

###  用于优化

  * [ commons-chunk-plugin ]() ：提取公共代码，在 [ 4-11提取公共代码 ]() 中有介绍。 
  * [ extract-text-webpack-plugin ]() ：提取 JavaScript 中的 CSS 代码到单独的文件中，在 [ 1-5使用 Plugin ]() 中有介绍。 
  * [ prepack-webpack-plugin ]() ：通过 Facebook 的 Prepack 优化输出的 JavaScript 代码性能，在 [ 4-13使用 Prepack ]() 中有介绍。 
  * [ uglifyjs-webpack-plugin ]() ：通过 UglifyES 压缩 ES6 代码，在 [ 4-8压缩代码 ]() 中有介绍。 
  * [ webpack-parallel-uglify-plugin ]() ：多进程执行 UglifyJS 代码压缩，提升构建速度。 
  * [ imagemin-webpack-plugin ]() ：压缩图片文件。 
  * [ webpack-spritesmith ]() ：用插件制作雪碧图。 
  * [ ModuleConcatenationPlugin ]() ：开启 Webpack Scope Hoisting 功能，在 [ 4-14开启 ScopeHoisting ]() 中有介绍。 
  * [ dll-plugin ]() ：借鉴 DDL 的思想大幅度提升构建速度，在 [ 4-2使用 DllPlugin ]() 中有介绍。 
  * [ hot-module-replacement-plugin ]() ：开启模块热替换功能。 

###  其它

  * [ serviceworker-webpack-plugin ]() ：给网页应用增加离线缓存功能，在 [ 3-14 构建离线应用 ]() 中有介绍。 
  * [ stylelint-webpack-plugin ]() ：集成 ` stylelint ` 到项目中，在 [ 3-16检查代码 ]() 中有介绍。 
  * [ i18n-webpack-plugin ]() ：给你的网页支持国际化。 
  * [ provide-plugin ]() ：从环境中提供的全局变量中加载模块，而不用导入对应的文件。 
  * [ web-webpack-plugin ]() ：方便的为单页应用输出 HTML，比 html-webpack-plugin 好用。 

