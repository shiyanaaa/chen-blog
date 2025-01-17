---
date: 2023-03-18
category:
    - html
tag:
    - html
    - html5
    - 前端
---
 # HTML5元素和语义化标签
> 站点： [ 前端开发文档 ]()  
>  原文： [ HTML元素 ]()  
>  原文： [ 语义化标签 ]()

##  HTML元素

###  元素分类

  * **块级元素** ： ` div ` 、 ` h1-h6 ` 、 ` hr ` 、 ` menu ` 、 ` ol ` 、 ` ul ` 、 ` li ` 、 ` dl ` 、 ` dt ` 、 ` dd ` 、 ` table ` 、 ` p ` 、 ` form `

    * 自身属性为 ` display: block; ` 的元素，通常使用块级元素进行布局（结构）的搭建。 
  * 块级元素的特点 

    * 独占一行 
    * 从上到下依次排列 
    * 直接控制宽度、高度以及盒子模型的相关CSS属性 
    * 不设置宽度，块级元素的宽度是它的父元素内容的宽度，高度是自身内容的高度 
    * 可以嵌套行内元素 
    * ` ul/ol ` 下面只能是 ` li ` ， ` dl ` 下面只能是 ` dt dd ` ； ` p ` 不能包含其他块级元素包括自身 
  * **内联元素** ： ` span ` 、 ` a ` 、 ` strong ` 、 ` i ` 、 ` em ` ， ` s ` 、 ` u ` ， ` textarea ` 、 ` input ` 、 ` select ` ， ` label ` 、 ` img ` 、 ` sup ` ， ` sub `

    * 自身属性为 ` display: inline; ` 的元素，通常使用行内元素进行文字、小图标（小结构）的搭建。 
  * 内联元素的特点 

    * 不独占一行，和其他内联元素从左到右在一行显示 
    * 不能直接控制宽度、高度以及盒子模型的相关CSS属性，可以直接设置内外边距的左右值 
    * 宽高由自身内容的大小决定（文字、图片等） 
    * 只能容纳文本或其他内联元素（不能在内联元素中嵌套块级元素） 

**CSS外链引入方式**

  * ` link ` 是 ` html ` 标签， ` @import ` 是 ` css ` 提供的方式，写在 ` css ` 文件或 ` style ` 标签中。 
  * 加载顺序有区别，当一个页面被加载时， ` link ` 引用的 ` css ` 文件会被同时加载，而 ` @import ` 引入的 ` css ` 文件会等页面全部下载完成后再加载。 
  * 使用 ` js ` 控制DOM改变CSS样式，只能使用 ` link ` 标签，因为 ` import ` 不能被DOM控制。 

**CSS命名规范**

  * 头部： ` header `
  * 内容： ` content/container `
  * 尾部： ` footer `
  * 导航： ` nav `
  * 侧栏： ` sidebar `
  * 栏目： ` column `
  * 页面外围控制整体布局宽度： ` wrapper `
  * 左右中： ` left right center `
  * 登陆条： ` loginbar `
  * 标志： ` logo `
  * 广告： ` banner `
  * 页面主体： ` main `
  * 热点： ` hot `
  * 新闻： ` news `
  * 下载： ` download `
  * 子导航： ` subnav `
  * 菜单： ` menu `
  * 子菜单： ` submenu `
  * 搜索： ` search `
  * 友情链接： ` friendlink `
  * 页脚： ` footer `
  * 版权： ` copyright `
  * 投票： ` vote `
  * 合作伙伴： ` partner `
  * 滚动： ` scroll `
  * 内容： ` content `
  * 标签页： ` tab `
  * 文章列表： ` list `
  * 提示信息： ` msg `
  * 小技巧： ` tips `
  * 栏目标题： ` title `
  * 加入： ` joinus `
  * 指南： ` guild `
  * 服务： ` service `
  * 注册： ` register `
  * 状态： ` status `

##  语义化标签

  1. 尽量减少使用无意义标签，如 ` span ` 和 ` div `
  2. 尽量不使用标签本身的CSS属性，如 ` b ` 、 ` font ` 、 ` s `
  3. 需要强调的部分，使用 ` strong ` 、 ` em `
  4. 表格搭建时，使用 ` <thead> ` 表格头部 ` </thead> ` 、 ` <tbody> ` 表格主体 ` </tbody> ` 、 ` <tfoot> ` 表格尾部 ` </tfoot> `
  5. 列表搭建时，使用 ` <ul> ` 无序列表 ` </ul> ` 、 ` <ol> ` 有序列表 ` </ol> ` 、 ` <dl> ` 定义列表 ` </dl> `

  * ` section ` ：划分网页，表示页面中的一个内容区块，比如章节、页眉、页脚或页面其它部分。可以和 ` h1，h2，h3... ` 等其他标签结合使用，表示文档结构。 
  * ` hgroup ` ：对整个页面/页面中的一个内容区块的标题进行组合。 
  * ` header ` ：一个内容区块或整个页面的头部部分。 
  * ` footer ` ：整个页面或页面区块的尾部。 
  * ` nav ` ：页面中导航连接的部分。 
  * ` article ` ：独立于内容其余部分的完整独立内容块。 ` article ` 元素专门为摘要设计。 
  * ` aside ` ：表示 ` article ` 标签内容之外的，与 ` article ` 标签内容相关的辅助信息， ` aside ` 元素被用于无关内容。 

    * 应该与主内容分开的内容 
    * ` aside ` 元素中的内容可以被独立开来而不会影响文档或 ` section ` 中主内容的含义 
    * 可以用在主要内容相关的引用，如侧边栏、广告、 ` nav ` 元素组等 
    * ` aside ` 的内容如果被删除，剩下的内容仍然很合理 
  * ` figure ` ：表示一段独立的流内容，一般表示文档主体流内容中的一个独立单元（ ` figure ` 元素经常用于图片） 
  * ` figcaption ` ： 

    * 一个图例的说明 
    * ` figure ` 元素的一个标题或相关解释 
    * 使用 ` figcaption ` 时，最好是 ` figure ` 块的第一个或最后一个元素 

**新增标签的兼容问题**

  * HTML5语义化标签在IE6-8下，默认当成行内元素展示。 
  * 通过引入 ` js ` 解决IE9以下新增标签的兼容问题 

**Forms**

  * 新增 ` input ` 元素的种类： 

    * ` search ` ：搜索输入框 
    * ` tel ` ：电话号码输入框 
    * ` url ` ：输入URL地址 
    * ` email ` ：邮件输入框 
    * ` number ` ：数字输入框 
    * ` rang ` ：特定范围内的数值选择器 
    * ` color ` ：颜色选择器 只在Opera和Blackberry浏览器 
    * ` datetime ` ：显示完整日期和时间 UTC标准时间 
    * ` datetime-local ` ：显示完整日期和时间 
    * ` time ` ：显示时间 
    * ` month ` ：显示月份 
    * ` week ` ：显示周 
  * 表单新特性： 

    * ` placeholder ` ：输入框占位符，用作输入提示 
    * ` autocomplete ` ：是否保存用户输入值，默认为 ` on ` ，关闭为 ` off `
    * ` autofocus ` ：自动聚焦 
    * ` required ` ：此项必填，不能为空 
    * ` pattern ` ：正则验证 ` pattern="\d{1,5}" `
    * ` form ` ：加上 ` form ` 属性，表单元素可以放在页面的任意位置 
    * ` formnovalidate/novalidate ` ： 

      * 表示不需要验证表单，直接提交（ ` novalidate ` 用户 ` form ` 标签） 
      * ` formnovalidate ` 用于 ` submit ` 类型的提交按钮 
  * 表单验证 

    * ` validity ` 对象，通过下面的 ` valid ` 可以查看验证是否通过 

      * ` oText.addEventListener("invalid"fn1,false); `
      * ` valid ` ：验证不通过时返回 ` false `
      * ` valueMissing ` ：输入值为空时 
      * ` typeMismatch ` ：控件值与预期类型不匹配 
      * ` patternMismatch ` ：输入值不满足 ` pattern ` 正则 
      * ` customError ` ：不符合自定义验证 

        * ` setCustomValidity(); ` 自定义验证 

