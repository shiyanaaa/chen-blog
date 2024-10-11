---
date: 2024-08-02
category:
    - css
tag:
    - css
---
 # CSS技巧
**1、兼容所有浏览器显示半透明效果的方法**

    
    
    <div class="transparent"></div>
    
    
    .transparent {
        filter: progid:DXImageTransform.Microsoft.Alpha(opacity=50);
        -moz-opacity: 0.5;
        -khtml-opacity: 0.5;
        opacity: .5;
        width: 200px;
        height: 200px;
        margin: 0 auto;
        background: url("../img/pic.jpg");
    }

**2、` _height ` , ` _width ` 的作用 **

使用 ` _height ` 解决 ` float ` 的 ` div ` 不闭合的问题，可以将 ` _height ` 属性去掉就可以达到效果。

    
    
    <div id="wrap">
        <div class="column_left">
            <h1>Float left</h1>
        </div>
        <div class="column_right">
            <h1>Float right</h1>
        </div>
    </div>
    
    
    #wrap {
        border: 6px solid #ccc;
        overflow: auto;
        _height: 1%;
    }
    
    .column_left {
        width: 20%;
        padding: 10px;
        float: left;
    }
    
    .column_right {
        float: right;
        width: 75%;
        padding: 10px;
        border-left: 6px solid #ccc;
    }

**3、使用` min-height ` ` min-width ` 解决 ` div ` ，或者 ` span ` 的固定高度问题 **

有时候我们需要设定某个元素固定高度，但是在 ` firefox ` 或者 ` opera `
下面只设置高度，在内容不够多的时候，达不到预想的效果，这时候我们可以使用 ` min-height `

**4、 使用` media ` 指令引入两种 ` css ` ：打印版本的 ` css ` 和屏幕显示的 ` css ` **

    
    
    <link type="text/css" rel="stylesheet" href="url" media="screen" charset="utf-8">
    <link type="text/css" rel="stylesheet" href="url" media="print" charset="utf-8">

**5、用` .fixTable{ table-layout: fixed; overflow:hidden; } ` 加上 ` nobr ` 标签实现隐藏
**

**6、可以使用` page-break-after ` ， ` page-break-before ` 控制打印时的分页 **

**7、` *html{} ` 的作用是为了兼容6.0以下的IE版本，对 ` html ` 节点的选取，其他的浏览器都认为 ` html `
标签是文档的根节点，而ie6以下的ie版本却认为在 ` html ` 标签的上面还有一个根节点 **

**8、使用` text-indent ` 显示图片，而隐藏文字 **

    
    
    h1 {
        background: url(../img/pic.jpg) no-repeat;
        width: 200px;
        height: 200px;
        text-indent: -2000px
    }

