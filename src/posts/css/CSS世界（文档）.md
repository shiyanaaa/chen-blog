---
date: 2023-10-03
category:
    - 样式
tag:
    - 样式
    - 前端
    - css3
    - css
---
 # CSS世界（文档）
**整理完了《高性能JavaScript》这本书，往下就需要快速处理《CSS世界》，这本讲解CSS特性的书非常值得一读，内容完整，重点突出，实战性强，就是语言啰嗦。由于全书内容太多，而且需要一点一点的整理，所以放到了站点上，方便大家查看。**

> 站点地址： [ 前端开发文档 ]()  
>  原文链接： [ CSS世界 ]() ，豆瓣读书： [ CSS世界 ]()

##  CSS世界

##  第1章 概述

  1. 流体布局 
  2. ` table `
  3. CSS3 

##  第2章 术语和概念

  1. 未定义行为 

##  第3章 流、元素和基本概念

  1. 块级元素 

     * 为什么 ` list-item ` 元素会出现项目符号 
     * ` display: inline-table; ` 的盒子是怎样组成的 
     * ` width/height ` 作用在哪个盒子上 
  2. ` width/height ` 作用的具体细节 

     * 深藏不漏的 ` width:auto `
     * ` width ` 值作用的细节 
     * CSS流体布局下的宽度分离原则 
     * 改变 ` width/height ` 作用细节的 ` box-sizing `
     * 相对简单的 ` height:auto `
     * 关于 ` height:100% `
  3. ` min-width/max-width ` 和 ` min-height/max-height `

     * 为流体而生的 ` min-width/max-width `
     * 与众不同的初始值 
     * 超越 ` !important ` ，超越最大 
     * 任意高度元素的展开收起动画技术 
  4. 内联元素 

     * 哪些元素是内联元素 
     * 内联盒模型 
     * 幽灵空白节点 

##  第4章 盒尺寸四大家族

  1. 深入理解 ` content `

     * ` content ` 与替换元素 
     * ` content ` 内容生成技术 
  2. 温和的 ` padding ` 属性 

     * ` padding ` 与元素的尺寸 
     * ` padding ` 的百分比值 
     * 标签元素内置的 ` padding `
     * ` padding ` 与图形绘制 
  3. 激进的 ` margin ` 属性 

     * ` margin ` 与元素尺寸以及相关布局 
     * ` margin ` 的百分比值 
     * ` margin ` 合并 
     * ` margin:auto `
     * ` margin ` 无效情形解析 
  4. 功勋卓著的 ` border ` 属性 

     * 为什么 ` border-width ` 不支持百分比值 
     * 了解各种 ` border-style ` 类型 
     * ` border-color ` 和 ` color `
     * ` border ` 与透明边框技巧 
     * ` border ` 与图形构建 
     * ` border ` 等高布局技术 

##  第5章 内联元素与流

  1. 字母 ` x `

     * 字母 ` x ` 与CSS世界的基线 
     * 字母 ` x ` 与CSS中的 ` x-height `
     * 字母 ` x ` 与CSS中的 ` ex `
  2. 内联元素的基石 ` line-height `

     * 内联元素的高度之本—— ` line-height `
     * 为什么 ` line-height ` 可以让内联元素“垂直居中” 
     * 深入 ` line-height ` 的各类属性值 
     * 内联元素 ` line-height ` 的“大值特性” 
  3. ` line-height ` 的好朋友 ` vertical-align `

     * ` vertical-align ` 家族基本认识 
     * ` vertical-align ` 作用前提 
     * ` vertical-align ` 和 ` line-height ` 之间的关系 
     * 深入理解 ` vertical-align ` 线性类属性值 
     * 深入理解 ` vertical-align ` 文本类属性值 
     * 简单了解深入理解 ` vertical-align ` 线性类属性值上标下标类属性值 
     * 无处不在的 ` vertical-align `
     * 基于 ` vertical-align ` 属性的水平垂直居中弹框 

##  第6章 流的破坏与保护

  1. 魔鬼属性 ` float `

     * ` float ` 的本质与特性 
     * ` float ` 的作用机制 
     * ` float ` 更深入的作用机制 
     * ` float ` 与流体布局 
  2. ` float ` 的天然克星 ` clear `

     * 什么是 ` clear ` 属性 
     * 成事不足败事有余的 ` clear `
  3. CSS世界的结界—— **BFC**

     * **BFC** 的定义 
     * **BFC** 与流体布局 
  4. 最佳结界 ` overflow `

     * ` overflow ` 裁剪界线 ` border box `
     * 了解 ` overflow-x ` 和 ` overflow-y `
     * ` overflow ` 与滚动条 
     * 依赖 ` overflow ` 的样式表现 
     * ` overflow ` 与锚点定位 
  5. ` float ` 的兄弟 ` position:absolute ` 绝对定位 

     * ` absolute ` 的包含块 
     * 具有相对特性的无依赖 ` absolute ` 绝对定位 
     * ` absolute ` 与 ` text-align `
  6. ` absolute ` 与 ` overflow `
  7. ` absolute ` 与 ` clip `

     * 重新认识的 ` clip ` 属性 
     * 深入了解 ` clip ` 的渲染 
  8. ` absolute ` 的流体特性 

     * 当 ` absolute ` 遇到 ` left/top/right/bottom ` 属性 
     * ` absolute ` 的流体特性 
     * ` absolute ` 的 ` margin:auto ` 居中 
  9. ` position:relative ` 才是大哥 

     * ` relative ` 对 ` absolute ` 的限制 
     * ` relative ` 与定位 
     * ` relative ` 的最小化影响原则 
  10. 强悍的 ` position:fixed ` 固定定位 

     * ` position:fixed ` 不一样的“包含块” 
     * ` position:fixed ` 的 ` absolute ` 模拟 
     * ` position:fixed ` 与背景锁定 

##  第7章 层叠规则

  1. ` z-index `
  2. 层叠上下文和层叠水平 
  3. 理解元素的层叠顺序 
  4. 牢记层叠准则 
  5. 深入了解层叠上下文 

     * 特定 
     * 创建 
     * 层叠上下文与层叠顺序 
  6. ` z-index ` 负值深入理解 
  7. ` z-index ` 准则 

##  第8章 文本处理能力

  1. ` line-height ` 的另一个朋友 ` font-size `

     * ` font-size ` 和 ` vertical-align ` 的隐秘故事 
     * 理解 ` font-size ` 与 ` ex ` 、 ` em ` 和 ` rem ` 的关系 
     * 理解 ` font-size ` 的关键字属性值 
     * ` font-size:0 ` 与文本的隐藏 
  2. 字体属性家族 ` font-family `

     * 了解衬线字体和无衬线字体 
     * 等宽字体的实践价值 
     * 中文字体和英文名称 
     * 一些补充说明 
  3. 字体家族其他成员 

     * ` font-weight `
     * ` font-style `
     * ` font-variant `
  4. ` font ` 属性 

     * 缩写的 ` font ` 属性 
     * 使用关键字值得 ` font ` 属性 
     * ` font ` 关键字属性值的应用价值 
  5. ` @font face ` 规则 

     * ` @font face ` 的本质是变量 
     * ` @font face ` 与字体图标技术 
  6. 文本的控制 

     * ` text-indent ` 与内联元素缩进 
     * ` letter-spacing ` 与字符间距 
     * ` word-spacing ` 与单词间距 
     * 了解 ` word-break ` 和 ` word-wrap ` 的区别 
     * ` white-space ` 与换行和空格的控制 
     * ` text-align ` 与元素对齐 
     * 如何解决 ` text-decoration ` 下划线和文本重叠的问题 
     * ` text-transform ` 字符大小写 
  7. 了解 ` :first-letter/:first-line ` 伪元素 

     * 深入 ` :first-letter ` 伪元素及其实例 
     * ` :first-line ` 伪元素 

##  第9章 元素的修饰与美化

  1. ` color `

     * 颜色关键字 
     * 不支持的 ` transparent ` 关键字 
     * 不支持的 ` currentColor ` 变量 
     * 不支持的 ` rgba ` 颜色和 ` hsla ` 颜色 
     * 支持却鸡肋的系统颜色 
  2. ` background `

     * 隐藏元素的 ` background-image ` 到底加不加载 
     * 与众不同的 ` background-position ` 百分比计算方式 
     * ` background-repeat ` 与渲染性能 
     * 外强中干的 ` background-attachment:fixed `
     * ` background-color ` 背景色永远是最低的 
     * 利用多背景的属性 **hack** 小技巧 
     * 渐变背景和 ` rgba ` 背景色的兼容处理 

##  第10章 元素的显示与隐藏

  1. ` display ` 与元素的显示/隐藏 
  2. ` visibility ` 与元素的显示/隐藏 

     * 不仅仅是保留空间 
     * 了解 ` visibility:collapse `

##  第11章 用户界面样式

  1. 和 ` border ` 形似的 ` outline ` 属性 

     * 绝不可以在全局设置 ` outline:0 none `
     * 真正不占据空间的 ` outline ` 及其应用 
  2. 光标属性 ` cursor `

     * 琳琅满目的 ` cursor ` 属性值 
     * 自定义光标 

##  第12章 流向的改变

  1. 改变水平流向的 ` direction `

     * ` direction ` 简介 
     * ` direction ` 的黄金搭档 ` unicode-bidi `
  2. ` writing-mode `

     * ` writing-mode ` 原来的作用 
     * ` writing-mode ` 改变了哪些规则 
     * ` writing-mode ` 和 ` direction ` 的关系 

