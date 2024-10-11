---
date: 2024-03-17
category:
    - material-design-lite
tag:
    - material-design-lite
    - material-design
---
 # Material Design
##  Material Design

> ###  [ 参考代码 ]()

###  1\. 设计语言

**拟真 vs. 扁平**

在 ` iso7 ` 之前，Apple采用的是 ` 拟真化 ` 设计语言，期望通过模拟现实世界的物体，给用户身临其境的感觉。自 ` metro ` 和 `
ios7 ` 开始的 ` 扁平化 `
设计语言则相反，它着意去掉冗余的装饰效果（比如透视、纹理、渐变等等能做出3D效果的元素），让“信息”本身重新作为核心被凸显出来。

**Material Design**

如果说 ` 拟真 ` 代表设计语言的一个极端，而 ` 扁平 ` 代表设计语言的另一个极端，那么 ` Material Design `
则居于两者之间更偏右的位置。

在 ` Material Design ` 中，屏幕里看上去平整的一个 ` App `
界面，事实上不同控件之间都拥有着层级关系。不同控件之间的层级关系会使用阴影作为表示，而阴影的深浅，代表的正是这个控件在 ` Z ` 轴的高度：

###  2\. 材料/Material

` Material Design ` 里的材料 ` Material ` 实际上是一种虚构出来的材料，：厚度无限薄（1dp），面积
无限大，能变换造型，也能按照规律移动 —— 你可以把它当做一张纸（事实上， ` Material Design ` 曾一度传说要改名为 ` Quantum
Paper ` \- 量子纸）。

虽然每一块 ` Material ` 都是扁的，但他们所处的环境，其实是一个 ` 3D ` 空间，这意味着所有处于 ` Material Design `
设置的这个三维环境里的控件，都拥有 ` XYZ ` 三个维度， ` Z轴 ` 垂直于屏幕，使用阴影表现材料的高度，阴影越重， ` Z值 `
越高，距离用户越近。

因此， ` Material Design ` 并不是单纯的扁平化，它在保留了扁的控件的同时，采用了立体的虚拟空间， 简言之， ` Material
Design ` 的核心是：扁而不平。

**Material Design Lite**

**MDL** 中定义了一组样式类 ` mdl-shadow--Ndp ` ，用于声明材料的阴影， ` N ` 的有效取值为： ` 2/3/4/6/8/16
` 。

为元素应用阴影样式类很简单：

    
    
    <!--为元素声明2dp的阴影-->
    <any class="mdl-shadow--2dp">...</any>
    

###  3\. 色彩/Color

` Material Design ` 中的色彩灵感来自于现代建筑、道路标识、路面标记及运动场等 大胆运用色调、高光和阴影，充满动感的场景。

` Material Design ` 使用 ` 19 ` 个调色板（ ` red、pink、purple等 ` ）用来约束设计中色彩的使用。
在每个调色板中， ` 色调为500的颜色为基准色 ` ，其他颜色是基准色在不同色调（ ` 50-900, A100-700 ` ） 下的表现。

**Material Design Lite**

在 ` MDL ` 中，我们可以使用样式类 ` mdl-color--{palette}-{hue} ` 来设置背景色，使用样式类 ` mdl-color-
text--{palette}-{hue} ` 来设置前景色：

    
    
    <div class="mdl-color--red mdl-color-text--grey-50">
        this is a gray text on red background.
    </div>
    

###  4\. 色彩运用

**Material Design** 给出了一些色彩运用在通常条件下的约束：

**1\. 最多用两个调色板**

在一个界面中最多使用两个调色板，从主调色板选择最多三个色调，从辅调色板选择一个强调色。下面的示例选择 ` indigo ` 调色板中的三个色调（ `
100、500和700 ` ），从 ` pink ` 调色板中选择色调 ` A200 ` 作为强调色：

**2\. 为文本、图标和分割线应用透明度**

通过为文本设置 ` 透明度 ` 来表达文本的 ` 相对 ` 重要性：

对于深色背景的浅色文字，最重要的文本使用 ` 87%的透明度 ` ，次重要的文本使用 ` 54%的透明度 `
。提示性文本，例如输入框、标签、被禁止的文字等使用 ` 26%的透明度 ` 。

对于浅色背景的深色文字，最重要的文本使用 ` 100%的透明度 ` ，次重要的文本使用 ` 70%的透明度 ` ，其他文本使用 ` 30%的透明度 ` 。

**3\. 工具栏和状态栏**

` 工具栏 ` 和 ` 大色块 ` 应当使用调色板中色调为 ` 500 ` 的颜色为基准色。状态栏应当选择 调色板中比基准色略深的色调为 ` 700 `
的颜色。

**4\. 使用强调色**

在大色块上绝对不要使用强调色，对动作按钮、开关或滑动条之类的组件应当使用 ` 强调色 ` 。

###  5\. 图标/Icon

` Google ` 提供了适用于 ` Material Design ` 的图标字体，我们可以直接在前端样式表中使用 ` @font-face `
引用这些字体。

` face ` 用来指定要显示的图标，也可以 使用其对应的数字编码：

    
    
    <i class="material-icons">&#xE87C;</i>
    

###  6\. 排版/Typography

` Material Design ` 提供了 ` 11 ` 种规格的文字样式供不同场景下排版使用:

在 ` MDL ` 中，使用样式类 ` mdl-typography--{name} ` 声明文本的排版样式：

    
    
    <h1 class="mdl-typography--title">Hello,Material Design</h1>
    <p class="mdl-typography--body-2">this is a demo</p>

