---
date: 2023-04-23
category:
    - material-design
tag:
    - material-design
    - material-design-lite
---
 # MDL布局组件
##  MDL布局组件

> ###  [ 参考代码 ]()

###  1\. 布局/Layout

` MDL ` 的 ` 布局/Layout组件 ` 用来作为整个页面其他元素的容器，可以自动适应不同的浏览器、 屏幕尺寸和设备。

` 布局/Layout组件 ` 需要按特定的 ` HTML ` 结构进行声明：

    
    
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <header class="mdl-layout__header"></header>
        <div class="mdl-layout__drawer"></div>
        <main class="mdl-layout__content"></main>
    </div>
    

需要指出的是，在一个布局声明中， ` header ` 等子元素不一定全部使用，比如你可以不要侧栏菜单：

    
    
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
        <header class="mdl-layout__header"></header>
        <main class="mdl-layout__content"></main>
    </div>
    

布局组件简化了创建可伸缩页面的过程。确切的说， ` MDL ` 可以根据屏幕的尺寸设定样式类的不同显示效果：

  * 桌面 - 当屏幕宽度 ` 大于840px ` 时， ` MDL ` 按桌面环境应对 

  * 平板 - 当屏幕尺寸 ` 大于480px ` ，但 ` 小于840px ` 时， ` MDL ` 按平板环境应对。比如，自动隐藏 ` header ` 、 ` drawer ` 区域等 

  * 手机 - 当屏幕尺寸 ` 小于480px ` 时， ` MDL ` 按手机环境应对 

###  2\. 头部/Header

布局组件的 ` header ` 子元素由一系列 ` header-row ` 组成：

###  3\. 头部 - 导航/Navigation

在 ` header ` 子元素内可以使用 ` 导航/navigation ` ，导航块由一个 ` 导航容器 ` 和 ` 若干导航链接 ` 构成：

    
    
    <div class="mdl-layout__header-row">
        <!--导航容器-->
        <nav class="mdl-navigation">
            <!--导航链接-->
            <a class="mdl-navigation__link" href="javascript:void (0);">Link</a>
            <a class="mdl-navigation__link" href="javascript:void (0);">Link</a>
            <a class="mdl-navigation__link" href="javascript:void (0);">Link</a>
        </nav>
    </div>
    

如上例所示，导航块使用 ` nav元素 ` 建立。在头部的导航块 ` 自动按水平排列各链接项 ` 。

一个常见的 ` UI模式 ` 是 ` 标题居左，导航居右 ` ，如下图所示：

` mdl-layout-spacer ` 可以自动地填充行容器（ ` mdl-layout__header-row ` ） 的剩余空间（扣除 ` titl
` e和 ` navigation ` 的宽度），因此可以简单地实现为：

    
    
    <div class="mdl-layout__header-row">
        <span class="mdl-layout-title">title</span>
        <div class="mdl-layout-spacer"></div>
        <nav class="mdl-navigation">...</nav>
    </div>
    

###  4\. 头部 - 选项卡/Tabs

在布局的头部可以嵌入 ` 选项栏/tab-bar ` ，内容区域可以嵌入 ` 选项面板/tab-panel ` 。当用户点击选项栏中的 ` 链接/tab*
` 时，自动显示对应的选项面板：

在布局 ` 头部声明选项栏 ` ，需要遵循特定的 ` HTML ` 结构：

    
    
    <header class="mdl-layout__header">
        <!--声明选项栏-->
        <div class="mdl-layout__tab-bar">
            <!--声明选项，通过href绑定对应的面板，对要激活的选项声明is-active-->
            <a class="mdl-layout__tab is-active" href="#panel-1">tab-1</a>
            <a class="mdl-layout__tab" href="#panel-2">tab-2</a>
            <a class="mdl-layout__tab" href="#panel-3">tab-3</a>
        </div>
    </header>
    

在布局的 ` 内容区域声明选项面板 ` ，也依赖于特定的 ` HTML ` 结构：

    
    
    <main class="mdl-layout__content">
        <!--声明选项面板，使用id属性指定锚点，对要初始显示的面板声明is-active-->
        <div class="mdl-layout__tab-panel is-active" id="panel-1">...</div>
        <div class="mdl-layout__tab-panel" id="panel-2">...</div>
        <div class="mdl-layout__tab-panel" id="panel-3">...</div>
    </main>
    

###  5\. 侧拉菜单/Drawer

侧拉菜单默认情况下是隐藏的，需要用户点击按钮：

可以设置修饰样式类 ` mdl-layout--fixed-drawer ` 来 ` 强制显示侧拉菜单 ` （在 ` 小尺寸屏幕 `
下，侧拉菜单总是隐藏的）:

    
    
    <div class="mdl-layout mdl-layout--fixed-drawer">
        <div class="mdl-layout__drawer">...</div>
    </div>
    

在侧拉菜单中也可以使用导航，这时所有的链接 ` 自动按垂直方向排列 ` ：

    
    
    <div class="mdl-layout__drawer">
        <span class="mdl-layout-title">Title</span>
        <div class="mdl-navigation">
            <a class="mdl-navigation__link" href="javascript:void(0);">Link 1</a>
            <a class="mdl-navigation__link" href="javascript:void(0);">Link 2</a>
        </div>
    </div>
    

