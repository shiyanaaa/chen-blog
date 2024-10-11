---
date: 2024-01-05
category:
    - http-2
tag:
    - http-2
    - server
---
 # HTTP2服务器推送（Server Push）
##  引言

> 一直想要深入学习 **HTTP2**
> 的技术细节，但是内容太多，很繁复，需要花很多时间，所以选择采用片段式的学习方法，把看到的知识点记录下来，当作一种学习过程。
>
> 文章来自网络，这里是 [ 原文 ]() ，方便备查。

###  HTTP2的特点

  * 二进制传输 
  * 头部压缩 
  * 多路复用 
  * 服务器推送（Server Push） 

###  网站加在过程

  1. 首先是浏览器请求主页面 ` index.html ` ，服务端相应内容； 
  2. 获取到主页应答，浏览器开始解析主页的 ` html ` 标签，发现构建 ` DOM ` 树还需要 ` CSS ` 、 ` PNG ` 、 ` JS `

等资源；

  1. 发起针对 ` CSS ` 、 ` PNG ` 、 ` JS ` 的内容请求； 
  2. 获取并解析 ` JS ` 和 ` CSS ` 等内容，然后继续请求依赖资源。 

###  Server Push

服务端接收到客户端主请求，“预测”主请求的依赖资源，在相应主请求的同时，主动并发推送依赖资源到客户端。客户端解析主请求响应后，可以“无延时”从本地缓存中获取依赖资源，减少访问延时，提高访问体验，加大了链路的并发能力。

###  推送实现

1、 **标识依赖资源**

推荐依赖资源标识方式：文件内 ` <link> ` 标签和 **HTTP** 头部携带，表示该资源后续会被使用，可以预请求，关键字 ` preload `
修饰这个资源。

  * **静态Link标签法：**

    
    
    Link: <push.css>; rel=preload; as=style

  * **HTTP头表示法：**

    
    
    <link rel="preload" href="push.css" as="style">

其中 ` rel ` 表明了资源 ` </push.css> ` 是预加载的， ` as ` 表明了资源的文件类型。另外， ` link ` 还可以用 `
nopush ` 修饰，表示浏览器可能已经有该资源缓存，指示有推送能力的服务端不主动推送资源，只有当浏览器先检查到没有缓存，才去指示服务端推送资源， `
nopush ` 格式写成：

    
    
    Link: </app/script.js>; rel=preload; as=script;nopush

2、 **推送资源**

用户访问 **CDN** ，主要包括直接访问的边缘节点, 若干中间节点和客户源站，路径中的每层都可以对请求做分析，预测可能的依赖资源，通过插入静态 `
<link> ` 标签或者增加响应头部返回给浏览器。 **CDN** 的推送主要采用头部携带推送信息。

  * **客户端指定推送资源**

客户端通过 ` url ` 或者请求头说明需要的资源 ` url ` ，写法如下：

    
    
    Url：http://http2push.gtimg.com/simple_push.html?req-push=simple_push.js

或者：

    
    
    GET /simple_push.html HTTP/1.1
    Host: http2push.gtimg.com
    User-Agent: curl/7.49.1
    Accept: */*
    X-Push-Url: simple_push.js

  * **CDN节点指定推送资源**

CDN节点针对请求资源配置推送资源, 基础配置如下:

    
    
    location ~ “/simple_push.html$” {
    http2_server_push_url /simple_push.js
    }

  * **源站指定推送资源**

通过增加响应头 ` link ` 通知客户端或者 **CDN** 节点，后续希望推送的依赖资源，中间具有推送功能的节点(如 **CDN**
节点)可以基于此信息进行资源请求与推送。

