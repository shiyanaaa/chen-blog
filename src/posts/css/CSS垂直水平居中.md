---
date: 2023-05-24
category:
    - css3
tag:
    - css3
---
 # CSS垂直水平居中
1.居中一个浮动元素，父元素和子元素同时左浮动，然后父元素相对左移动50%，子元素相对右移动50%，或者子元素相对左移动-50%

    
    
    <div class="p">
        <div class="c">
            <span>水平居中浮动元素</span>
        </div>
    </div>
    
    
    .p {
        position: relative;
        float: left;
        left: 50%;
    }
    
    .c {
        position: relative;
        float: left;
        right: 50%;
    }

2.垂直水平居中

    
    
    <div class="center">
        <span>水平垂直居中</span>
    </div>
    
    
    .center {
        position: absolute;
        width: 200px;
        height: 100px;
        left: 50%;
        top: 50%;
        margin-top: -50px;
        margin-left: -100px;
    }

3.图片水平垂直居中tabel_cell

    
    
    <div class="test_box">
        <img src="img/head.png" alt="">
    </div>
    
    
    .test_box {
        width: 200px;
        height: 200px;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -100px;
        margin-left: -100px;
        border: 1px solid #000;
    }
    
    .test_box img {
        margin: auto;
        position: absolute;
        right: 0;
        bottom: 0;
        left: 0;
        top: 0;
    }

4.图片水平垂直居中span

    
    
    <div class="test_box">
        <span class="hook"></span>
        <img src="img/book.jpg" alt="">
    </div>
    
    
    .test_box {
        width: 200px;
        height: 200px;
        text-align: center;
        border: 1px solid #000;
        position: absolute;
        left: 50%;
        top: 50%;
        margin-left: -100px;
        margin-top: -100px;
    }
    
    .test_box .hook {
        display: inline-block;
        height: 100%;
        margin-left: -1px;
        vertical-align: middle;
    }
    
    .test_box img {
        vertical-align: middle;
    }

5.水平垂直居中（适用于父级元素只有一个子元素的情况，比如全屏的效果）

    
    
    <div class="outer">
        <h1 class="inner">适用于父级元素只有一个子元素的情况，比如全屏的效果。</h1>
    </div>
    
    
    .outer {
        position: absolute;
        width: 400px;
        height: 400px;
        background: #f80;
        top: 50%;
        left: 50%;
        margin-top: -200px;
        margin-left: -200px;
    }
    
    .inner {
        border: 3px solid green;
        position: absolute;
        margin: auto;
        overflow: hidden;
        width: 50%;
        height: 50%;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
    }

6.水平垂直居中（方法一、使用 line-height）

    
    
    <div class="box">
        <div class="content">水平垂直居中</div>
    </div>
    
    
    .box {
        width: 200px;
        height: 200px;
        margin: 0 auto;
        background: #ddf;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -100px;
        margin-left: -100px;
    }
    
    .content {
        line-height: 200px;
        vertical-align: middle;
        text-align: center;
        overflow: hidden;
    }

7.水平垂直居中（方法二、把容器当作表格单元）

    
    
    <div class="box">
        <div class="content">水平垂直居中</div>
    </div>
    
    
    .box {
        width: 200px;
        height: 200px;
        background: #ddf;
        display: table;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -100px;
        margin-left: -100px;
    }
    
    .content {
        display: table-cell;
        vertical-align: middle;
        text-align: center;
    }

8.水平垂直居中（方法三、IE6下的解决方案）

    
    
    <div class="box">
        <div class="content">水平垂直居中</div>
    </div>
    
    
    .box {
        width: 200px;
        height: 200px;
        background: #ddf;
        display: table;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -100px;
        margin-left: -100px;
    }
    
    .content {
        _position: relative;
        _top: 50%;
        display: table-cell;
        vertical-align: middle;
        text-align: center;
    }
    
    .content > div {
        _position: relative;
        _top: -50%;
    }

9.水平垂直居中（方法四、负边距margin的使用）

    
    
    <div class="box">
        <div class="content">水平垂直居中</div>
    </div>
    
    
    .box {
        width: 200px;
        height: 200px;
        background: #ddf;
        display: table;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -100px;
        margin-left: -100px;
    }
    
    .content {
        width: 100px;
        height: 80px;
        padding: 10px;
        background: #abc;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-left: -60px;
        margin-top: -50px;
    }
    
    .content > div {
        _position: relative;
        _top: -50%;
    }

