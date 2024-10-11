---
date: 2023-04-20
category:
    - material-design-lite
tag:
    - material-design-lite
---
 # MDL容器组件
##  MDL容器组件

> ###  [ 参考代码 ]()

###  1\. 单行页脚/Mini footer

` MDL ` 的 ` 单行页脚/Mini footer组件 ` 以单行水平方式组织所有的信息：

单行页脚同样采用 ` flexbox ` 布局，将整行分割为左右两种区域，并以空格填充剩余的行空间：

    
    
    <footer class="mdl-mini-footer">
        <div class="mdl-mini-footer--left-section">Left session</div>
        <div class="mdl-mini-footer--right-section">Right session</div>
    </footer>
    

` left-section ` 总是向左边对齐，而 ` right-section ` 总是向右边对齐。 单行页脚内可以放置多个 ` left-
section或right-section ` 。

在每个区域内， ` MDL ` 预定义了两种交互元素：链接和社交按钮。

` 链接/link-list ` 样式应用在列表元素 ` ul ` 上，自动将列表成员水平排列：

    
    
    <div class="mdl-mini-footer--left-section">
        <ul class="mdl-mini-footer--link-list">
            <li><a href="javascript:void(0)">Link 1</a></li>
            <li><a href="javascript:void(0)">Link 2</a></li>
            <li><a href="javascript:void(0)">Link 3</a></li>
        </ul>
    </div>
    

` 社交按钮/social-btn ` 样式将元素修饰为 ` 36px ` 正方大小的容器，可以设置其背景图片来构造图标式按钮。

###  2\. 多行页脚/Mega footer

` MDL ` 的 ` 多行页脚/Mega footer `
组件可以包含多个垂直排列的区域。当我们需要一个复杂的页脚区域来呈现信息及提供交互手段时，可以使用这个组件：

从上图容易看出， ` 单行页脚/Mini footer组件 ` 相当于仅适用 ` 多行页脚/Mega footer 组件 ` 的 ` bottom-
section ` 区域。

当声明为 ` mdl-mega-footer--link-list ` 样式的列表元素出现在 ` drop-down-section `
区域时，其列表项是垂直排列的。

###  3\. 栅格/Grid

` MDL ` 的 ` 栅格/Grid组件 ` 是 ` 响应式 ` 的，可以适应不同屏幕分辨率的布局要求：

` 栅格/Grid ` 组件根据屏幕尺寸大小，自动地分割行宽：

  * 桌面（ > 840px） - 12个单元格 

  * 平板（ 480px ~ 840px）- 8个单元格 

  * 手机（ < 480px）- 4个单元格 

可以使用 ` mdl-cell--N-col ` 样式声明单元格的宽度：

    
    
    <div class="mdl-grid">
        <div class="mdl-cell mdl-cell--4-col"></div>
        <div class="mdl-cell mdl-cell--4-col"></div>
        <div class="mdl-cell mdl-cell--4-col"></div>
    </div>
    

在不同的分辨率下，示例栅格将呈现如下：

如果我们希望在任何情况下，示例栅格总是显示为相同的列数，那么 可以声明单元格在不同环境下的样式：

    
    
    <div class="mdl-grid">
        <div class="mdl-cell mdl-cell--6-col-desktop mdl-cell--4-col-tablet mdl-cell--2-col-phone"></div>
        <div class="mdl-cell mdl-cell--6-col-desktop mdl-cell--4-col-tablet mdl-cell--2-col-phone"></div>
    </div>
    

在同一行的各单元格，默认情况下总是 ` 拉伸/stretch ` 其高度（ ` 采用同一行中最高单元格的高度 ` ），可以使用 ` mdl-cell--
bottom ` 样式使单元格不拉伸，并将底部对齐：

与之类似， ` mdl-cell--top ` 使单元格顶部对齐， ` mdl-cell--middle ` 使单元格居中对齐：

    
    
    <div class="mdl-grid">
        <!--顶部对齐-->
        <div class="mdl-cell mdl-cell--top">...</div>
        <!--居中对齐-->
        <div class="mdl-cell mdl-cell--middle">...</div>
        <!--底部对齐-->
        <div class="mdl-cell mdl-cell--bottom">...</div>
    </div>
    

###  4\. 选项卡/Tabs

` MDL ` 的 ` 选项卡/Tabs ` 组件用来在多个内容间进行切换：

` 选项卡/Tabs ` 组件具有固定的 ` HTML ` 结构，由选项栏、选项面板等元素构成：

    
    
    <!--1. 声明组件-->
    <div class="mdl-tabs mdl-js-tabs">
        <!--2. 声明选项栏-->
        <div class="mdl-tabs__tab-bar">
            <!--2.1 声明选项，使用href属性指向选项面板，为要激活的选项应用is-active样式-->
            <a class="mdl-tabs__tab is-active" href="#panel-1">tab-1</a>
            <a class="mdl-tabs__tab" href="#panel-2">tab-2</a>
        </div>
        <!--3. 声明选项面板，使用id属性声明锚点 , 为要显示的面板应用is-active样式-->
        <div class="mdl-tabs__panel is-active" id="panel-1">...</div>
        <div class="mdl-tabs__panel" id="panel-2">...</div>
    </div>
    

可以为组件元素应用 ` mdl-js-ripple-effect ` 样式，使点击时具有水纹动效。

###  5\. 卡片/Cards

` MDL ` 的 ` 卡片/Card ` 组件非常适合显示复杂的、包含多种类型信息的内容：

卡片通常具有固定的宽度，而高度则根据场景不同，可以固定，也可以变化。 卡片是一种新型的界面元素，它为用户提供了通过单一访问点访问复杂信息的手段。

使用 ` mdl-card ` 样式类将外层元素声明为卡片组件，使用 ` mdl-card__title `
等样式类将内层元素声明为标题、媒体、动作等容器：

    
    
    <any class="mdl-card">
        <any class="mdl-card__title">...</any>
        <any class="mdl-card__media">...</any>
        <any class="mdl-card__supporting-text">...</any>
        <any class="mdl-card__actions">...</any>
        <any class="mdl-card__menu">...</any>
    </any>
    

卡片组件默认为 ` 330px宽，最小200px高 ` ，是一个 ` 主轴为竖向的flex容器 ` 。可以显式地设置其宽度和高度。

` title ` 、 ` media ` 、 ` supporting-text ` 和 ` actions ` 作为 ` flex容器 `
成员在垂直方向上依次排列，其高度是由内容决定，或者被显式地设定。例如，很多时候，我们希望给 ` title `
区域增加背景图片以增强感染力，那么将照片设置为 ` title ` 区域的背景之后，还需要设置 ` title ` 区域的高度：

    
    
    <div class="mdl-card">
        <div class="mdl-card__title" 
            style="background:url("img/bg.jpg") no-repeat;backgroud-size:cover;height:150px;">
            ...
        </div>
    </div>
    

` menu ` 块被设置为绝对定位，总是居于卡片组件的右上角。

