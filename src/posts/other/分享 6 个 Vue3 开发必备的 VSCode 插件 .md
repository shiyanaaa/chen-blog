---
date: 2023-07-19
category:
    - 前端
tag:
    - 前端
    - javascript
    - vue.js
---
 # 分享 6 个 Vue3 开发必备的 VSCode 插件 
今天分享 6 个 Vue3 开发必备的 VSCode 插件，可以直接用过 VSCode 的插件中心直接安装使用。

如果有觉得有帮助，还请点赞👍支持一下~

##  1\. Volar

_🔥 下载数 153 万+_

相信使用 VSCode 开发 Vue2 的同学一定对 Vetur 插件不会陌生，作为 Vue2 配套的 VSCode 插件，它的主要作用是对 Vue
单文件组件提供高亮、语法支持以及语法检测。

而随着 Vue3 正式版发布，Vue 团队官方推荐 [ Volar ]() 插件来代替 Vetur 插件，不仅支持 Vue3 语言高亮、语法检测，还支持
TypeScript 和基于 [ vue-tsc ]() 的类型检查功能。

使用时需要注意：

  1. 首先要禁用 Vetur 插件，避免冲突； 
  2. 推荐使用 ` css ` / ` less ` / ` scss ` 作为 ` <style> ` 的语言，因为这些基于 [ vscode-css-language ]() 服务提供了可靠的语言支持； 
  3. 如果使用 ` postcss ` / ` stylus ` / ` sass ` 的话，需要安装额外的语法高亮扩展。postcss 使用 [ language-postcss ]() ，stylus 使用 [ language-stylus ]() 拓展，sass 使用 [ Sass ]() 拓展； 
  4. Volar 不包含 ESLint 和 Prettier，而官方的 [ ESLint ]() 和 [ Prettier ]() 扩展支持 Vue，所以需要自行安装。 

##  2\. Vue VSCode Snippets

_🔥 下载数 152 万+_

[ Vue VSCode Snippets ]() 插件旨在为开发者提供最简单快速的生成 Vue 代码片段的方法，通过各种快捷键就可以在 ` .vue `
文件中快速生成各种代码片段。简直是 Vue3 开发必备神器。

该插件支持：Volar、Vue2 和 Vue3。

使用方式如下：

  * 新建一个 ` .vue ` 文件，输入 ` vbase ` 会提示生成的模版内容： 

  * 输入 ` vfor ` 快速生成 ` v-for ` 指令模版： 

  * 输入 ` v3onmounted ` 快速生成 ` onMounted ` 生命周期函数： 

其他就不再演示啦，功能实在太强大，常用快捷键非常多，具体可以查看 [ 文档 ]() 。

##  3\. Auto Close Tag

_🔥 下载数 769 万+_

[ Auto Close Tag ]() 插件是一个很好用的 VS Code
扩展，它对生产率有很大影响。顾名思义，当我们在结束标记中键入结束括号时，它将添加结束标记。它支持HTML，Handlebars，XML，PHP，Vue，JavaScript，Typescript，JSX等。

##  4\. Vue Peek

_🔥 下载数 49 万+_

[ Vue Peek ]() 插件用来拓展 Vue 代码编辑的体验，可以让我们快速跳转到组件、模块定义的文件。

使用方式如下：

  * 右键组件标签，跳转到组件定义的文件： 

  * 右键组件标签，弹窗显示组件定义的文件： 

##  5\. Vue Theme

_🔥 下载数 34 万+_

[ Vue Theme ]() 插件提供了不错的 Vue 主题，还支持配置不同颜色，感觉还不错。

##  6\. Vite

_🔥 下载数 8.9 万+_

[ Vite ]() 插件可以让我们打开项目后，就能自动启动开发服务器，允许开发者无需离开编辑器即可预览和调试应用。支持一键启动、构建和重启项目。

##  总结

今天分享的 6 个插件，大家可以按需安装使用。

我比较强烈推荐实用 [ Volar ]() 和 [ Vue VSCode Snippets ]() 这 2 个插件。  
如果觉得不错，还请点赞支持。👍

大家有更好的插件，欢迎评论分享~🔥

欢迎关注我的微信公众号“前端自习课”。

