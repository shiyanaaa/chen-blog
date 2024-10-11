---
date: 2024-07-11
category:
    - websocket
tag:
    - websocket
    - socket.io
---
 # WebSocket技术讲解
##  WebSocket

` WebSocket ` 是 ` HTML5 ` 开始提供的一种浏览器与服务器间进行全双工通讯的网络技术。

现很多网站为了实现即时通讯，所用的技术都是 ` 轮询(polling) ` 。 ` 轮询 ` 是在特定的的时间间隔（如每1秒），由浏览器对服务器发出 `
HTTP请求 ` ，然后由服务器返回最新的数据给客服端的浏览器，这种方式有一个很大的弊端，就是会 ` 占用很多的带宽 ` 。

最新的轮询效果是 ` Comet – 用了AJAX ` 。但这种技术虽然可达到 ` 全双工通信 ` ，但依然需要发出请求。

使用 ` WebSocket ` ，浏览器和服务器只需要要 ` 做一个握手的动作 ` ，然后，浏览器和服务器之间就 ` 形成了一条快速通道 ` ，两者之间就
` 直接可以数据互相传送 ` 。而且它为我们实现即时服务带来了两大好处：

> ` 节省资源 ` ：互相沟通的 ` Header ` 是很小的-大概 ` 只有 2 Bytes ` 。  
>  ` 推送信息 ` ：不需要客户端请求，服务器可以 ` 主动传送数据给客户端 ` 。

##  socket.io

` Socket.IO ` 是一个 ` WebSocket库 ` ，包括了 ` 客户端的js和服务器端的nodejs ` ，它的目标是 `
构建可以在不同浏览器和移动设备上使用的实时应用 ` 。

**socket.io的特点**

  * **易用性** ： ` socket.io ` 封装了服务端和客户端，使用起来非常简单方便。 

  * **跨平台** ： ` socket.io ` 支持跨平台，这就意味着你有了更多的选择，可以在自己喜欢的平台下开发实时应用。 

  * **自适应** ：它会自动根据浏览器从 ` WebSocket ` 、 ` AJAX长轮询 ` 、 ` Iframe流 ` 等等各种方式中选择最佳的方式来实现网络实时应用，非常方便和人性化，而且支持的浏览器最低达IE5.5。 

###  安装部署

    
    
    npm install socket.io

###  服务监听

` socket.io ` 的服务端启动非常的简单，引用 ` socket.io模块 ` 。

    
    
    var io = require('socket.io');

然后调用 ` listen函数 ` ，传入 ` 监听的端口号 ` ，开始服务监听。启用了80端口用于测试：

    
    
    var io = require('socket.io')(80);

###  注册事件

    
    
    io.on('connection', function (socket) {
        socket.on('disconnect', function () {
    
        })
    })

` connection ` 事件在客户端成功连接到服务端时触发，有了这个事件，我们可以随时掌握用户连接到服务端的信息。

当客户端成功建立连接时，在 ` connection ` 事件的回调函数中，我们还是可以为 ` socket `
注册一些常用的事件,如：disconnect事件，它在客户端连接断开是触发，这时候我就知道用户已经离开了。

###  启动服务

目前为止，我们已经搭建好了一个最简单的 ` socket ` 服务器，为了在浏览器中能够访问到我们的服务，我们还需要在服务端搭建一个简单的 ` web服务器
` ，让浏览器能够访问我们的客户端页面。

为了便捷，我们选用 ` node.js ` 中常用的 ` express框架 ` 来实现 ` web服务 ` ，示例如下：

    
    
    var express = require('express');
    var app = express();
    app.get('/', function (req, res) {
        res.status(200).send('成功连接！')
    });
    var server = require('http').createServer(app);
    var io = require('socket.io')(server);
    io.on('connection', function (socket) {
    
    });
    server.listen(80);

##  客户端引用

服务端构建完毕，下面看一看客户端应该如何使用。

服务端运行后会在根目录动态生成socket.io的客户端js文件，客户端可以通过固定路径/socket.io/socket.io.js添加引用。

首先添加网页index.html,并在网页中引用客户端js文件：

    
    
    <script src="//cdn.bootcss.com/socket.io/2.0.2/socket.io.js"></script>

##  连接服务

当客户端成功加载socket.io客户端文件后会获取到一个全局对象io，我们将通过io.connect函数来向服务端发起连接请求。

    
    
    var socket = io.connect('/');
    socket.on('connect',function(){
        //连接成功
    });
    socket.on('disconnect',function(data){
        //连接断开
    });

` connect ` 函数可以接受一个 ` url参数 ` ，url可以 ` socket服务的http完整地址 ` ，也可以是 ` 相对路径 `
，如果省略则表示默认连接当前路径。与服务端类似，客户端也需要注册相应的事件来捕获信息，不同的是 ` 客户端连接成功的事件是connect ` 。

了解了客户端如何使用，下面我们创建网页 ` index.html ` ，并添加如下内容(保存):

    
    
    <html>
    <head>
        <script src="//cdn.bootcss.com/socket.io/2.0.2/socket.io.js"></script>
        <script>
            window.onload = function(){
                var socket = io.connect('/');
                socket.on('connect',function(){
                    document.write('连接成功!');
                });
            };
        </script>
    </head>
    <body>
    </body>
    </html>

页面添加完毕还要记得在服务端 ` app.js ` 中为它添加路由，让我们可以访问测试网页：

    
    
    app.get('/index',function(req,res){
       res.sendFile('index.html',{root:__dirname});
    });

##  实时通讯

服务端和客户端都构建完毕了，下面开始发送消息。

当我们成功建立连接后，我们可以通过 ` socket对象 ` 的 ` send函数 ` 来互相发送消息，示例-客户端向服务端发送消息( `
index.html ` )：

    
    
    var socket = io.connect('/');
    socket.on('connect',function(){
       //客户端连接成功后发送消息'hello world!'
       socket.send('hello world!');
    });
    socket.on('message',function(data){
       alert(data);
    });

连接成功后，我们向服务端发送消息 ` hello world! ` ，还为 ` socket ` 注册了 ` message事件 ` ，它是 `
send函数 ` 对应的接收消息的事件，当服务端向客户端send消息时，我们就可以在 ` message ` 事件中接收到发送过来的消息。

服务端向客户端发送消息也可以通过 ` send ` 的方式，示例 - 服务端向客户端发送消息( ` app.js ` )：

    
    
    var io = require('scoket.io');
    io.on('connection', function (socket) {
        socket.send('Hello World!');
        socket.on('message', function (data) {
            console.log(data);
        })
    });

与客户端相同，服务端也需要为 ` socket ` 注册 ` message事件 ` 来接收客户端发送过来的消息。

##  发送信息

` socket.io ` 既然是用来实现通讯的，那么如何发送、接收信息才是根本。

在 ` socket.io ` 中， ` emit函数 ` 用于 ` 发送数据 ` ，我们使用 ` send ` 的方式实现了信息的互发，其实 `
send函数 ` 只是 ` emit的封装 ` ，实际上还是使用了emit，且看send函数是如何实现的：

    
    
    function send(){
      var args = toArray(arguments);
      args.unshift('message');
      this.emit.apply(this, args);
      return this;
    }

在 ` send函数 ` 中，获取到原来的参数，并在原来的基础上插入了一个参数 ` message ` ，然后调用了 ` emit函数 ` 。通过 `
send ` 函数的实现，我们也学会了emit函数的用法，它有多个参数， **第一个参数是事件名称**
，在接收端注册该事件就可以接收到发送过去的信息，事件名称可以自由定义，在不同的场景下，我们可以定义不同的事件来接收消息。 **第二个参数才是发送的数据**
。了解清楚了工作原理，下面来将send替换成emit函数发送信息：

    
    
    //app.js
    io.on('connection',function(socket){
         socket.emit('message','连接成功！');
         socket.on('message',function(data){
        });
    });

##  服务端事件

事件监听是实现通讯的基础，因此充分了解socket.io的事件，学习如何在正确的时候使用它们至关重要。在一些关键的的状态下，socket.io可以注册相应的事件，通过事件监听，我们可以在这些事件中作出反应，常用的事件如下：

  * ` connection ` ——客户端成功连接到服务器。 

  * ` message ` ——捕获客户端 ` send ` 信息。。 

  * ` disconnect ` ——客户端断开连接。 

  * ` error ` ——发生错误。 

##  客户端

较服务端而言，客户端提供更多的监听事件，在实时应用中，我们可以为这些事件注册监听并作出反应，例如： ` connect ` 提示用户连接成功， `
disconnect ` 时提示用户停止服务等等。

  * ` connection ` ——成功连接到服务器。 

  * ` connecting ` ——正在连接。 

  * ` disconnect ` ——断开连接。 

  * ` connect_failed ` ——连接失败。 

  * ` error ` ——连接错误。 

  * ` message ` ——监听服务端send的信息。 

  * ` reconnect_failed ` ——重新连接失败。 

  * ` reconnect ` ——重新连接成功。 

  * ` reconnecting ` ——正在重连。 

那么客户端 ` socket ` 发起连接时的顺序是怎么样的呢？当第一次连接时，事件触发顺序为： ` connecting ` → ` connect `
；

当失去连接时，事件触发顺序为： ` disconnect → reconnecting → connecting → reconnect → connect
` 。

##  命名空间

命名空间着实是一个非常实用好用的功能。我们可以通过命名空间，划分出不同的房间，在房间里的广播和通信都不会影响到房间以外的客户端。

那么如何创建房间呢？在服务端，通过 ` of("") ` 的方式来划分新的命名空间：

    
    
    io.of('chat').on('connection',function(socket){
    });

示例中，我们创建一个名为 ` chat ` 的房间，客户端可以通过如下方式连接到指定的房间：

    
    
    var socket = io.connect('/chat');

虽然连接到指定的房间，但是我们也可以在服务端操作，自由的进出房间：

    
    
    socket.join('chat');//进入chat房间
    socket.leave('chat');//离开chat房间

##  广播消息

在实时应用中，广播是一个不可或缺的功能，socket.io提供两种服务端广播方式。

第一种广播方式可以称之为' ` 全局广播 ` '，顾名思义，全局广播就是所有连接到服务器的客户端都会受到广播的信息：

    
    
    socket.broadcast.emit('DATA',data);

但是，在实际应用场景中，我们很多时候并不需要所有用户都收到广播信息，有的广播信息只发送给一部分客户端，比如某个房间里面的用户，那么可以使用如下方式：

    
    
    socket.broadcast.to('chat').emit('DATA',data);

##  中间件

` socket.io ` 提供中间件功能，我们可以通过中间件来对请求进行预处理，比如身份验证：

    
    
    io.use(function(socket, next){
      if (socket.request.headers.cookie) return next();
      next(new Error('Authentication error'));
    });

示例中展示了通过中间件进行身份验证，当没有 ` cookie ` 的时候抛出异常。

##  传递参数

在很多应用场景中，客户端发起连接请求时都需要传递参数，这些参数可能是 ` 身份验证、初始化设置 ` 等等，那么 ` socket.io `
发起连接时如何传递参数呢？

    
    
    var socket = io.connect('/');

由于 ` connect函数 ` 发起连接的参数是一个 ` url ` ，你可能会想到把参数拼接到url上，如 ` http://xxxx?xx=xxxx
` ，但是很遗憾这样是行不通的，我们可以通过这样的方式来传递参数：

    
    
    var socket = io.connect('/',{ _query:'sid=123456' });

在服务端可以这样获取到传递的参数:

    
    
    io.use(function(socket){
         var query = socket.request._query;
         var sid = query.sid; 
    });

客户端传递的参数已经被解析成了一个 ` json对象 ` ，这个对象就是 ` _query ` 。

