---
date: 2023-12-07
category:
    - css
tag:
    - css
    - css3
    - 前端
    - 开发
    - 样式
---
 # CSS3开发文档
> 站点： [ 前端开发文档 ]()  
>  原文： [ CSS选择器 ]()  
>  原文： [ CSS继承属性 ]()  
>  原文： [ CSS3核心模块 ]()  
>  原文： [ CSS盒子模型 ]()  
>  原文： [ CSS背景图像 ]()  
>  原文： [ CSS清除浮动 ]()  
>  原文： [ CSS定位 ]()

##  CSS选择器

  * 并集：对选择器进行分组，被分组的选择器可以分享相同的声明。用 **逗号** 将需要分组的选择器开分。 

    * ` h1,h2,h3,h4,h5,h6{} `
  * 交集：两种属性同属一个元素 

    * ` p.name{} ` 、 ` p#id{} ` 、 ` .name1.name2{} `
  * 后代（派生）：根据元素在位置上的关系定义样式，使用 **空格** 隔开，后代选择器尽量不要超过3个，不必把每个层级都列出，只需要写关键点即可 

    * ` li strong {} `
  * 子代：只能选择作为某元素的子元素，只选择子代，往后孙子一代不选择 

    * ` h1 > strong {} `
  * 兄弟和相邻兄弟：选择紧接在另一元素后的，并且二者有相同父元素 

    * ` h1 + p {} `
  * 属性：对带有指定属性的HTML元素设置样式，权重为10 

    * **属性选择器** ：为带有 ` title ` 属性的所有元素设置样式， ` [title] {} `
    * **属性和值选择器** ：为 ` title="name" ` 的所有元素设置样式， ` [title=name] {} `
    * **设置表单的样式** ： ` input[type="text"] {} `
  * 伪类： 

    * ` :active ` ：被激活的元素 
    * ` :focus ` ：有键盘输入焦点的元素 
    * ` :hover ` ：鼠标悬停 
    * ` :link ` ：未被访问的链接 
    * ` :visited ` ：已被访问的链接 
    * ` :first-child ` ：元素的第一个子元素 
    * ` :lang ` ：带有指定 ` lang ` 属性的元素 
  * 权重： 

    * ` div ` （1） 
    * ` class/类选择器 ` （10） 
    * ` id ` （100） 
  * 结构选择器（新增伪类（面试题）） 

    * ` :not ` ：排除 
    * ` :nth-child(n) ` ：第几个元素 从1开始设置 
    * ` :nth-child(2n) ` ：偶数元素 从0开始设置 
    * ` :nth-child(2n+1) ` ：奇数元素 
    * ` :nth-of-type(n) ` ：某个元素下同类型的第几个元素 
    * ` :nth-last-child ` ：倒数第几个元素 
    * ` :first-child->:nth-child(1) ` ： 
    * ` :fisrt-of-type ` ：第一个同级兄弟元素 
    * ` :last-of-type ` ：最后一个同级兄弟元素 
    * ` :nth-of-type(n) ` ：第几个同级兄弟元素 
    * ` :last-child ` ：最后一个子元素 
    * ` :only-child ` ：仅有一个子元素 
    * ` :only-of-type ` ：只有一个同类型的子元素 
    * ` :empty ` ：空内容 
    * ` :checked ` ：被选中 主要用在 ` input ` 表单元素 
  * 属性选择器 

    * ` E[attr=val] ` ： 
    * ` E[attr|=val] ` ：只能等于 ` val ` 或只能以 ` val- ` 开头 
    * ` E[attr*=val] ` ：包含 ` val ` 字符串 
    * ` E[attr~=val] ` ：属性值有多个，其中一个是 ` val `
    * ` E[attr^=val] ` ：以 ` val ` 开头 
    * ` E[attr$=val] ` ：以 ` val ` 结尾 
  * 目标伪类选择器 

    * ` :target() ` ：用来匹配URL指向的目标元素（存在URL指向该匹配元素时，样式效果才会生效） 
  * 伪元素： 

    * ` :first-line ` ：匹配首行文本，只能用于块级元素 
    * ` :first-letter ` ：匹配首字符 
    * ` :before/:after ` ：DOM元素前后插入额外的内容 

      * 遇到伪元素 ` before/after ` 就要加上 ` content='' `
      * ` display: block; ` ：独占一行 
      * ` display: inline-block; ` ：不独占一行 

##  CSS继承属性

  * **无继承性的属性**

    1. ` display ` ：规定元素应该生成的框的类型 
    2. 文本属性： 

       * ` vertical-align ` ：垂直文本对齐 
       * ` text-decoration ` ：添加文本装饰 
       * ` text-shadow ` ：文本阴影效果 
       * ` white-space ` ：空白符的处理 
       * ` unicode-bidi ` ：设置文本的方向 
    3. 盒子模型的属性： 

       * ` width ` 、 ` height `
       * ` margin ` 、 ` margin-top/right/bottom/left `
       * ` border ` 、 ` border-top/right/bottom/left `
       * ` border-style ` 、 ` border-top/right/bottom/left-style `
       * ` border-width ` 、 ` border-top/right/bottom/left-width `
       * ` border-color ` 、 ` border-top/right/bottom/left-color `
       * ` padding ` 、 ` padding-top/right/bottom/left `
    4. 背景属性： 

       * ` background `
       * ` background-color `
       * ` background-image `
       * ` background-repeat `
       * ` background-position `
       * ` background-attachment `
    5. 定位属性： 

       * ` float `
       * ` clear `
       * ` position `
       * ` top/right/bottom/left `
       * ` min-width/min-height ` 、 ` max-width/max-height `
       * ` overflow `
       * ` clip `
       * ` z-index `
    6. 生成内容属性： 

       * ` content `
       * ` counter-reset `
       * ` counter-increment `
    7. 轮廓样式属性： 

       * ` outline-style `
       * ` outline-width `
       * ` counter-color `
       * ` outline `
  * **有继承性的属性**

    1. 字体系列属性 

       * ` font ` ：组合字体 
       * ` font-family ` ：字体系列 
       * ` font-weight ` ：字体粗细 
       * ` font-size ` ：字体尺寸 
       * ` font-style ` ：字体风格 
       * ` font-variant ` ：小写字母转换为大写，字体尺寸更小 
       * ` font-stretch ` ：对当前 ` font-family ` 进行伸缩变形。所有主流浏览器不支持。 
       * ` font-size-adjust ` ：为某个元素规定一个 ` aspect ` 值，保持首选字体的 ` x-height `
    2. 文本系列属性 

       * ` text-indent ` ：文本缩进 
       * ` text-align ` ：文本水平对齐 
       * ` line-height ` ：行高 
       * ` word-spacing ` ：字间距 
       * ` letter-spacing ` ：字符间距 
       * ` text-transform ` ：控制文本大小写 
       * ` direction ` ：文本书写方向 
       * ` color ` ：文本颜色 
    3. 元素可见性： ` visibility `
    4. 表格布局属性 

       * ` caption-side `
       * ` border-collapse `
       * ` border-spacing `
       * ` empty-cells `
       * ` table-layout `
    5. 列表布局属性 

       * ` list-style-type `
       * ` list-style-image `
       * ` list-style-position `
       * ` list-style `
    6. 生成内容属性： ` quotes `
    7. 光标属性： ` cursor `
    8. 页面样式属性 

       * ` page `
       * ` page-break-inside `
       * ` windows `
       * ` orphans `

##  CSS3核心模块

**过渡动画**

  * ` transition ` ：过渡动画 

    * ` transition-property ` ：过渡属性 ` all[attr] `
    * ` transition-duration ` ：过渡时间 
    * ` transition-delay ` ：延迟时间 
    * ` transition-timing-function ` ：运行类型 

      * ` ease ` ：（逐渐变慢）默认值 
      * ` linear ` ：匀速 
      * ` ease-in ` ：加速 
      * ` ease-out ` ：减速 
      * ` cubic-bezier ` ：贝塞尔曲线 

过渡动画效果思考步骤：

  1. 找到过渡属性 
  2. 找到过渡属性起始值和结束值 
  3. 在合适的位置上增加 ` transition ` 属性 

**2D变换**

  * ` transform ` ：变形属性 

    * ` rotate() ` ：旋转函数 

      * ` deg ` ：度数 
      * ` transform-origin ` ：旋转的基点 
    * ` skew() ` ：倾斜函数 

      * ` skewX() `
      * ` skewY() `
    * ` scale() ` ：缩放函数 默认值是1 

      * ` scaleX() `
      * ` scaleY() `
    * ` translate() ` ：位移函数 

      * ` translateX() `
      * ` translateY() `

**animation-声明关键帧**

  * 关键帧—— ` @keyframes `

    * 类似于 ` flash `

      * 定义动画在每个阶段的样式，即帧动画 
    * 关键帧的时间单位 

      * 数字： ` 0% ` 、 ` 25% ` 、 ` 100% ` 等（设置某个时间段内任意时间点的样式） 
      * 字符： ` from(0%) ` 、 ` to(100%) ` ： 
    * 格式 

      * ` @keyframes ` ：动画名称 
      * ` {动画状态} `

**animation-调用动画**

  * 必要属性 

    * ` animation-name ` ：动画名称（关键帧名称） 
    * ` animation-duration ` ：动画执行时间 
  * 可选属性： 

    * ` animation-timing-function `

      * ` linear ` ：匀速 
      * ` ease ` ：缓冲 
      * ` ease-in ` ：由慢到快 
      * ` ease-out ` ：由快到慢 
      * ` ease-in-out ` ：由慢到快再到慢 
      * ` ease-bezier(num,num,num,num) ` ：特定的贝塞尔曲线类型，4个数值需在[0,1]区间内 
    * ` animation-delay ` ：动画延迟 
    * ` animation-iteration-count ` ：重复次数 
    * ` animation-direction ` ：动画运行的方向 ` normal|reverse|alternate|alternate-reverse `
    * ` animation-play-state ` ：动画状态 ` running|paused `
    * ` animation-fill-mode ` ：动画结束后的状态 ` none|forwards|backwards|both `

**3D变换**

  * ` transform-style: flat|preserve-3d ` ：3D空间展示 
  * ` perspective ` ：景深效果 
  * ` transform: persective(800px) ` ：直接作用在子元素上 
  * ` transform ` ：新增函数 

    * ` translate3d(tx, ty, tz) ` ： ` translateX() ` ` translateY() ` ` translateZ() `
    * ` rotate3d(rx, ry, rz, a) ` ： ` rotateX() ` ` rotateY() ` ` rotateZ() `
    * ` scale3d(sx, sy, sz) ` ： ` sacleX() ` ` sacleY() ` ` sacleZ() `

**圆角 border-radius**

  * ` border-radius ` ：1-4个数字/1-4个数字 

    * 水平半径/垂直半径 
    * 四个数字方向分别是 **左上 右上 右下 左下**
    * 没有 ` / ` 则水平半径和垂直半径一样 

      * ` border-radius: 10px/5px; `
      * border-radius: 60px 40px 30px 30px/30px 20px 10px 5px 
      * 例子：圆 椭圆 半圆 扇形 

**线性渐变 linear-gradient**

  * ` linear-gradient ` ：（[<起点>||<角度>,]?<点>,<点>...） 
  * 只能用在背景上 
  * 颜色是沿着一条直线轴变化 
  * 参数 

    * 起点：开始渐变方向 
    * 角度：开始渐变角度 
    * 点：渐变点的颜色和位置 
  * 重复线性渐变 

**径向渐变 radial-gradient**

  * ` radial-gradient `
  * 从“一点”向多个方向颜色渐变 
  * ` shape ` 形状： ` ellipse ` 、 ` circle ` 或设置水平半径，垂直半径 
  * ` size ` ：渐变的大小，即渐变停止位置： 

    * ` closet-side ` ：最左边 
    * ` farthest-side ` ：最远边 
    * ` closet-corner ` ：最近角 
    * ` farthest-corner ` ：最远角（默认值） 
  * ` position ` ：关键词|数值|百分比 
  * 重复的径向渐变 

**背景**

  * ` background-origin `

    * ` padding-box ` ：从 ` padding ` 区域显示 
    * ` border-box ` ：从 ` border ` 区域显示 
    * ` content-box ` ：从 ` content ` 区域显示 
  * ` background-clip `

    * ` padding-box ` ：从 ` padding ` 区域向外裁剪 
    * ` border- box ` ：从 ` border ` 区域向外裁剪 
    * ` content-box ` ：从 ` content ` 区域向外裁剪 
    * ` text ` ：文本裁剪 
  * ` background-size `

    * ` 100% 100% ` ：百分比 
    * ` 10px 10px ` ：数值 
    * ` contain ` ：按原始比例收缩，背景图显示完整，但不一定铺满整个容器 
    * ` cover ` ：按原比例收缩，背景图可能显示不完整，但铺满整个容器 
  * ` background-attachment `

    * 背景图片是滚动/固定 ` fixed ` (固定的) 默认是滚动的 

**盒子阴影**

  * ` box-shadow ` ：h v blur spread color inset; 

    * ` h ` ：水平方向偏移 
    * ` v ` ：垂直方向偏移 
    * ` blur ` ：模糊半径 
    * ` spread ` ：扩展半径 
    * ` color ` ：颜色 
    * ` inset ` ：内阴影，默认是外阴影 

**文本阴影**

  * ` text-shadow ` ：x y blur color 

    * ` x ` 轴偏移 ` y ` 轴偏移 模糊度 颜色 
    * 多层阴影制作文字立体效果，设置多种颜色，中间以逗号隔开 
  * 文字添加边框 

    * ` text-stroke ` ：2px blue 

      * 通过设定 ` 1px ` 的透明边框，可以让文字变得平滑 
      * 颜色设成透明能够创建镂空字体 

**滤镜**

  * ` -webkit-filter:normal; ` ：正常 
  * ` -webkit-filter:grayscale(1); ` ：灰度，取值范围0-1 
  * ` -webkit-filter:brightness(0); ` ：亮度，取值范围0-1 
  * ` -webkit-filter:invert(1); ` ：反色，取值范围0-1，0为原图，1为彻底反色 
  * ` -webkit-filter:sepia(0.5); ` ：叠加褐色，取值范围0-1 
  * ` -webkit-filter:hue-rotate(30deg); ` ：色相（按照色相环旋转，顺时针方向）（红-橙-黄-黄绿-绿-蓝绿-蓝-蓝紫-紫-紫红-红）此处为叠加黄色滤镜 
  * ` -webkit-filter:saturate(4); ` ：饱和度，取值范围0-*，0为无饱和度，1为原图，值越高，饱和度越大 
  * ` -webkit-filter:contrast(2); ` ：对比度，取值范围0-*，0为无对比度（灰色），1为原图，值越高对比度越大 
  * ` -webkit-filter:opacity(0.8); ` ：透明度，取值范围0-1，0为全透明，1为原图 

**遮罩**

  * ` mask-image ` ： 
  * ` mask-position ` ： 
  * ` mask-repeat ` ： 

##  CSS盒子模型

**` border ` 边框 **

  * 三角形箭头： 

    * 正方形的任意相邻两条边，然后旋转一定的角度，得到我们需要的任意方向的箭头 
    * ` border ` 、 ` border-width ` 、 ` border-style ` 、 ` border-color `
  * 三角形： 

    * ` border ` 的3个属性： ` border-width/border-style/border-color ` ，宽度和高度都为 ` 0 ` ，三角形箭头方向设定颜色，其余方向颜色设为透明 ` transparent `

**` margin ` 边距 **

  * **` margin ` 边距重叠 ** ： 取大值，不是两者相加之和。 
  * **` margin-top ` 的传递 ** ：大盒嵌套小盒，小盒加 ` margin-top ` 值，传递到大盒，导致整体下移。 

    * 解决 ` margin ` 的兼容性问题： 

      1. ` float: left; `
      2. ` overflow: hidden; `
      3. ` padding-top: 0/1px; `
      4. ` border-top: 1px solid transparent; `

##  CSS背景图像

**` background ` 背景 **

主要属性：

  * ` background-color ` ：背景颜色，简写 ` background `

    * 不能继承，默认是 ` transparent `
    * ` inherit ` 指定背景颜色，从父元素继承 
  * ` background-image ` ：背景图片 

    * ` url ` ：图片URL地址 
    * ` node ` ：默认值 背景上未放置图片 
    * ` inherit ` ：指定背景图片从父元素继承 
    * 一个元素可以引入多张背景图片； 

      * 指定要使用的一个或多个背景图片，默认情况下， ` background-image ` 放置在元素的左上角，并重复垂直和水平方向 
    * 属性不能继承 
  * ` background-repeat ` ：背景重复 

    * 默认重复 ` background-image ` 的垂直和水平方向 
    * ` repeat ` 默认 
    * ` repeat-x ` 只有水平位置重复 
    * ` repear-y ` 只有垂直位置重复 
    * ` no-repeat ` 不重复 
    * ` inherit ` 从父元素继承 
  * ` background-position ` ：背景定位 

    * 设置背景图片的起始位置 
    * ` x ` 、 ` y ` 水平位置，垂直位置。左上角是 ` 0 ` 。单位（px，关键字，百分数） 
    * 关键字成对出现 ` left right top bottom center ` ，仅指定一个关键字，其他值将会是 ` center `
    * 只设定 ` x ` 轴方向，默认 ` y ` 轴为 ` center `
    * ` inherit ` 从父元素继承 
  * ` background-attachment ` ：背景关联 

    * 设置背景图片固定或随页面的其余部分滚动 
    * ` scroll ` 默认 
    * ` fixed ` 固定 
    * ` inherit ` 从父元素继承 
  * ` background-size ` ：背景图像的尺寸大小 

    * ` <length> ` 长度值指定图像大小。不允许负值 
    * ` <percentage> ` 百分比指定图像大小。不允许负值 
    * ` auto ` 图像的真实大小 
    * ` cover ` 将背景图像等比例缩放到完全覆盖容器，有可能超出容器 
    * ` contain ` 等比例所放到宽/高与容器的宽/高相等，背景图像始终被包含在容器内 
  * ` background-origin ` ：设置背景图像的参考原点（位置） 

    * ` padding-box ` ：从 ` padding ` 区域（含 ` padding ` ）开始显示背景 
    * ` border-box ` ：从 ` border ` 区域（含 ` border ` ）开始显示背景 
    * ` content-box ` ：从 ` content ` 区域开始显示背景 
  * ` background-clip ` ：设置对象的背景图像向外裁剪的区域 

    * ` padding-box ` ：从 ` padding ` 区域（不含 ` padding ` ）开始向外裁剪背景 
    * ` border-box ` ：从 ` border ` 区域（不含 ` border ` ）开始向外裁剪背景 
    * ` content-box ` ：从 ` content ` 区域开始向外裁剪背景 
    * ` text ` ：从前景内容的形状（比如文字）作为裁剪区向外裁剪，实现使用背景作为填充色之类的遮罩效果。 
  * 雪碧图： ` background-position: x y `

##  CSS清除浮动

**` overflow: hidden ` **

  1. ` overflow ` 溢出隐藏 
  2. 清除浮动 
  3. 解决 ` margin-top ` 的传递问题 

**（面试题）** ：

  * 单行文本出现省略号（4个必备条件，缺一不可） 

    * ` width ` 宽度（不写宽度，默认继承父元素宽度） 
    * ` overflow: hidden; ` （溢出隐藏） 
    * ` white-space: nowrap; `
    * ` text-overflow: ellipsis; ` 文字隐藏的方式，以省略号的方式隐藏 
  * 多行文本出现省略号（必备条件，主要应用在移动端） 

    * ` display: -webkit-box; ` 弹性盒模型 
    * ` -webkit-box-orient: vertical; ` 规定元素的排列方式：垂直排列 
    * ` -webkit-line-clamp: 2; ` ：文字的行数（自定义） 
    * ` overflow: hidden; ` 溢出隐藏 
  * 多个元素在一行显示的方法 

    * ` display: inline; `
    * ` display: inline-block; `
    * ` float: left/right; `

**` display: inline-block; ` 元素的特点 **

  * 盒子横向排列 
  * ` verticle-align ` 属性会影响 ` inline-block ` 元素，值可能会设为 ` top `
  * 需要设置每一列的宽度 
  * 如果HTML源码中元素间有空格，列与列之间会产生空隙 

    * **解决方法** ： 

      * 如果元素添加了 ` dispay: inline-block; ` ，父元素增加一个属性 ` font-size: 0; ` ，同时在元素本身增加 ` font-size ` 属性进行覆盖 
  * ` display:inline-block; ` 在IE6/7下不兼容的解决方法 

    * 增加 ` display: inline; zoom: 1; ` 属性 

**IE7下块元素兼容` display: inline-block; ` ** 写法？

  * 直接让块元素设置为内联对象（设置属性 ` display: inline; ` ），然后触发块元素的 ` layout ` （如： ` zoom: 1; ` 等）。 
  * 兼容各浏览器的代码如下： ` div {display: inline-block; *display: inline; *zoom: 1;} `

##  ` float ` 浮动

**` float ` 元素的特点 **

  1. 在一行显示 
  2. 设置属性值为 ` left ` 时，浮动元素依次从父级盒子的左侧向右排列 
  3. 自动具有块级元素的属性，不需要添加 ` display: block; `
  4. 脱离文档流 
  5. 子元素不会继承浮动属性 
  6. 浮动元素下面的元素不能识别浮动元素的高度和位置，占据浮动元素的位置 
  7. 所有的元素都可以使用浮动属性 

**文档流和脱离文档流**

  * 文档流：元素排版布局过程中，元素自动从左往右，从上往下的流式排列。 
  * 每个非浮动元素块级元素独占一行，浮动元素按规则浮在行的一端。当前行容量满则另起一行浮动。 
  * 内联元素不会独占一行 
  * 几乎所有元素（包括块级、内敛和列表元素）均可生成子行，用于摆放子元素 
  * 标准文档流等级：分为两个等级，块级元素和行内元素 
  * 脱离文档流：文档流内的正常元素识别不到这个元素（脱离文档流的元素相当于平行漂浮于文档流之上） 

**` float ` 元素产生的影响 **

  1. 父元素设置背景颜色 ` background-color ` 不起作用 
  2. 父元素设置内边距属性 ` padding ` 不会被撑开 
  3. 父元素设置边框属性 ` border ` 不会被撑开 

##  清除浮动 ` float `

**清除浮动的方法**

  1. 给浮动元素的父级元素添加固定的高度 ` height ` （不推荐） 
  2. 给浮动元素的父级元素添加溢出隐藏属性 ` overflow: hidden; ` ； 
  3. 给最后一个浮动元素后面添加一个块级元素，这个块级元素带有 ` clear: both; ` 属性 

     * ` clear ` 清除浮动元素对文档流内元素的影响（可以让文档流内的元素识别到浮动元素的高度） 
     * ` left ` 清除 ` float ` 为 ` left ` 的影响 
     * ` right ` 清除 ` float ` 为 ` right ` 的影响 
     * ` both ` 清除 ` float ` 所有的影响 
     * ` inherit ` 从父级元素上继承该属性值 
  4. ` clearfix ` 清除浮动（固定代码） 

     * **利用伪元素` :after ` 清除浮动必备条件，缺一不可 **
     * ` display: block; ` 确保元素是一个块级元素 
     * ` clear: both; ` 不允许左右两边有浮动对象 
     * ` content: ''; ` 伪元素 ` :brfore/:after ` 自带的属性，如果不写，伪元素不起作用 
     * **写全的样式属性；不是必备条件**
     * ` height: 0; ` 防止在低版本浏览器中默认 ` height: 1px; ` 的情况，用 ` height: 0; ` 去覆盖 
     * ` font-size: 0; ` 字体大小 
     * ` overflow: hidden; ` 溢出隐藏 
     * ` visibility: hidden; ` 让所有可见性的元素隐藏 

**` overflow: hidden; ` 和 ` visibility: hidden; ` 有什么区别？ **

**（面试题）：如何让一个元素消失？**

  1. ` opacity: 0; ` [0-1] 透明度 
  2. ` display: none; ` 隐藏 
  3. ` widht/height/line-height + overflow ` ：宽/高/行高 + 溢出隐藏 
  4. ` visibility: hidden; ` 让所有可见性的元素隐藏 

**` clear: both; ` 的特点 **

  1. 元素需要是块级元素 
  2. 元素不能带有浮动属性 
  3. 元素必须放在最后一个浮动元素的后面 

##  CSS定位

  * **相对定位-` position: relative; ` **

    * 没有脱离文档流 
    * 参照物是元素本身位置 
    * 当 ` top ` 和 ` bottom ` 同时有值的情况下， ` top ` 值生效，支持负值 
    * 当 ` left ` 和 ` right ` 同时有值的情况下， ` left ` 值生效，支持负值 
    * 任何元素都可以设置相对定位属性 
    * 相对定位元素位移发生改变，但元素原来的位置还会被占用，其他元素还是正常识别这个元素原来的位置 
  * **绝对定位-` position: absolute; ` **

    * 脱离文档流 
    * 可以设置参照物，参照物必须是其父级元素（直系父级），如果没有直接父级会一直往上查找直到找到最外层的根元素为止； 
    * 有宽度和高度的情况下， ` top ` 和 ` bottom ` 同时有值， ` top ` 生效； ` left ` 和 ` right ` 同时有值， ` left ` 生效。 
    * 没有宽度和高度的情况下， ` top ` 和 ` bottom ` 同时设置值的情况下，会将这个盒子拉大，上下值都起作用，左右同理。 
    * 可以设置层级关系 ` z-index ` 属性，必须要和定位元素（绝对，相对，固定）同时使用，才会起作用。 
    * 一个元素定位在另一个元素上或者两个元素叠加的情况，都可以使用定位（绝对定位） 
    * 绝对定位一定要设置相对参照物 
  * **固定定位-` position: fixed; ` **

    * 脱离文档流 
    * 参照物是浏览器的可视窗口 
    * 任何元素都可以设置固定定位 
    * 可设置 ` top/bottom/left/right ` 四个方位 
    * 可通过 ` z-index ` 改变层级 
  * **` z-index ` 属性的特点 **

    * 默认是书写顺序在后的定位元素覆盖顺序在前的定位元素 
    * 可以使用 ` z-index ` 属性修改定位元素的层级关系 
    * 所有定位元素的 ` z-index ` 默认值都一样 
    * ` z-index ` 值是数字没有单位，支持负数 
    * 一般都是同级元素进行层级的比较 
    * 当参照物是相对定位或绝对定位的时候，父级元素之间没有 ` z-index ` 值，子元素的 ` z-index ` 值进行比较 

