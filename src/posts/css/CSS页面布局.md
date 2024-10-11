---
date: 2023-08-02
category:
    - css
tag:
    - css
---
 # CSS页面布局
  * 实现三栏布局，中间自适应（margin负值法） 

    
    
    <!--放第一行-->
    <div class="middle">middle</div>
    <div class="left">left</div>
    <div class="right">right</div>
    
    
    body {
        margin: 0;
        padding: 0;
    }
    
    .left, .right {
        height: 300px;
        width: 200px;
        float: left;
    }
    
    .right {
        margin-left: -200px;
        background-color: red;
    }
    
    .left {
        margin-left: -100%;
        background-color: #00ff00;
    }
    
    .middle {
        height: 300px;
        width: 100%;
        float: left;
        background-color: blue;
    }

  * 首尾高度固定、中间自适应的DIV布局（兼容IE6） 

    
    
    <div class="container">
        <div class="top">头部</div>
        <div class="middle">
            <ul>
                <li>中间置顶</li>
                <li>中间</li>
                ...
                <li>中间到底</li>
            </ul>
        </div>
        <div class="bottom">尾部</div>
    </div>
    
    
    html, body {
        margin: 0;
        /*padding: 0;*/
        height: 100%;
        overflow: hidden;
    }
    
    .top, .bottom {
        width: 100%;
        height: 50px;
        position: absolute;
    }
    
    /** {
        margin: 0;
        padding: 0;
    }
    
    html, body, .container {
        height: 100%;
        width: 100%;
    }
    
    div {
        position: absolute;
    }
    
    .top, .bottom {
        width: 100%;
        height: 100px;
        z-index: 5;
    }*/
    
    .top {
        background: red;
        top: 0;
    }
    
    .bottom {
        background: #00ff00;
        bottom: 0;
    }
    
    .middle {
        width: 100%;
        top: 50px;
        bottom: 50px;
        background: #a7fad7;
        overflow: auto;
        position: absolute;
        /*针对ie6设定的hack*/
        _height: 100%;
        _border-top: -100px solid #eee;
        _border-bottom: -100px solid #eee;
        _top: 0;
    }

  * flex-box布局 

    
    
    <div class="page-wrap">
        <section class="main-content">
            <h1>Main Content</h1>
            <p><strong>I'm first in the source order.</strong></p>
            <p>The key to victory is discipline, and that means a well made bed. You will practice until you can make your
                bed in your sleep. Fry, we have a crate to deliver. Hey, guess what you're accessories to.</p>
            <p>I'll get my kit! That's not soon enough! Oh, all right, I am. But if anything happens to me, tell them I died
                robbing some old man.</p>
        </section>
        <nav class="main-nav">
            <h2>Nav</h2>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Clients</a></li>
                <li><a href="#">Contact Us</a></li>
            </ul>
        </nav>
        <aside class="main-sidebar">
            <h2>Sidebar</h2>
            <p>I am a rather effortless column of equal height.</p>
        </aside>
    </div>
    
    
    body {
        padding: 2em;
    }
    
    * {
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
    }
    
    h1, h2 {
        font: bold 2em Sans-serif;
        margin: 0 0 1em 0;
    }
    
    h2 {
        font-size: 1.5em;
    }
    
    p {
        margin: 0 0 1em 0;
    }
    
    .page-wrap {
        display: flex;
        display: -webkit-flex;
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
    }
    
    .main-content,
    .main-sidebar,
    .main-nav {
        padding: 1em;
    }
    
    .main-content {
        -webkit-box-ordinal-group: 2;
        -moz-box-ordinal-group: 2;
        -ms-flex-order: 2;
        order: 2;
        width: 60%;
        -moz-box-flex: 1;
        background: white;
    }
    
    .main-nav {
        -webkit-box-ordinal-group: 1;
        -moz-box-ordinal-group: 1;
        -ms-flex-order: 1;
        order: 1;
        -webkit-box-flex: 1;
        -moz-box-flex: 1;
        width: 20%;
        -webkit-flex: 1;
        -ms-flex: 1;
        flex: 1;
        background: #ccc;
    }
    
    .main-sidebar {
        -webkit-box-ordinal-group: 3;
        -moz-box-ordinal-group: 3;
        -ms-flex-order: 3;
        order: 3;
        -webkit-box-flex: 1;
        -moz-box-flex: 1;
        width: 20%;
        -ms-flex: 1;
        -webkit-flex: 1;
        flex: 1;
        background: #ccc;
    }

  * 粘连 Footer 置于底部-方法一 

    
    
    HTML
    
    <div class="content">
        <h1>在 wrapper 上用负的 margin-bottom</h1>
        <p>
            <button id="add">Add Content</button>
        </p>
        <div class="push"></div>
    </div>
    <footer class="footer">
        Footer
    </footer>
    
    
    CSS
    
    html, body {
        height: 100%;
        margin: 0;
    }
    
    .content {
        min-height: 100%;
        padding: 20px;
        margin: 0 auto -50px;
    }
    
    .footer,
    .push {
        height: 50px;
        padding: 20px;
    }
    
    
    JS
    
    $("#add").on("click", function () {
        $("<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>").insertBefore(".push");
    });

  * 粘连 Footer 置于底部-方法二 

    
    
    HTML
    
    <div class="content">
        <div class="content-inside">
            <h1>在 footer 上用负的 margin-top</h1>
            <p>
                <button id="add">Add Content</button>
            </p>
        </div>
    </div>
    
    <footer class="footer">
        Footer
    </footer>
    
    
    CSS
    
    html, body {
        height: 100%;
        margin: 0;
    }
    
    .content {
        min-height: 100%;
    }
    
    .content-inside {
        padding: 20px;
        padding-bottom: 50px;
    }
    
    .footer {
        height: 50px;
        margin-top: -50px;
    }
    
    
    JS
    
    $("#add").on("click", function () {
        $("<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.</p>").appendTo(".content-inside");
    });

