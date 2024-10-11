---
date: 2024-09-02
category:
    - javascript
tag:
    - javascript
    - hybrid-app
    - 混合app
---
 #  Hybrid App 应用 开发中 9 个必备知识点复习(WebView  调试 等)
###  前言

我们大前端团队内部 📖 **每周一练** 的知识复习计划继续加油，本篇文章是 **《Hybrid APP 混合应用专题》** 主题的第二期和第三期的合集。

这一期共整理了 10 个问题，和相应的参考答案，文字和图片较多， **建议大家可以收藏，根据文章目录来阅读** 。

之前分享的每周内容，我都整理到掘金收藏集 [ 📔《EFT每周一练》 ]() 上啦，欢迎点赞收藏咯💕💕。

**内容回顾：**

  1. [ 《EFT 每周分享 —— Hybrid App 应用开发中 5 个必备知识点复习》 ]()
  2. [ 《EFT 每周分享 —— HTTP 的15个常见知识点复习》 ]()
  3. [ 《EFT 每周分享 —— 数据结构与算法合集》 ]()

**文章收录：**

本系列所有文章，都将收录在 Github 上， [ 欢迎点击查阅 ]() 。

> 注：本文整理部分资料来源网络，有些图片/段落找不到原文出处，如有侵权，联系删除。

###  一、iOS 平台中 UIWebView 与 WKWebView 有什么区别？

> 参考文章： [ 《UIWebView与WKWebView》 ]()

` UIWebView ` 是苹果继承于 ` UIView ` 封装的一个加载 web
内容的类,它可以加载任何远端的web数据展示在你的页面上，你可以像浏览器一样前进后退刷新等操作。不过苹果在 iOS8 以后推出了 ` WKWebView `
来加载 Web，并应用于 iOS 和 OSX 中，它取代了 ` UIWebView ` 和 ` WebView ` ，在两个平台上支持同一套 API。

它脱离于 ` UIWebView `
的设计，将原本的设计拆分成14个类，和3个代理协议，虽然是这样但是了解之后其实用法比较简单，依照职责单一的原则，每个协议做的事情根据功能分类。

` WKWebView ` 与 ` UIWebView ` 的区别：

  * ` WKWebView ` 的内存远远没有 ` UIWebView ` 的开销大,而且没有缓存； 
  * ` WKWebView ` 拥有高达 60FPS 滚动刷新率及内置手势； 
  * ` WKWebView ` 支持了更多的 HTML5 特性； 
  * ` WKWebView ` 高效的 app 和 web 信息交换通道； 
  * ` WKWebView ` 允许 ` JavaScript ` 的 ` Nitro ` 库加载并使用, ` UIWebView ` 中限制了； 
  * ` WKWebView ` 目前缺少关于页码相关的 API； 
  * ` WKWebView ` 提供加载网页进度的属性； 
  * ` WKWebView ` 使用 Safari 相同的 JavaScript 引擎； 
  * ` WKWebView ` 增加加载进度属性： ` estimatedProgress ` ； 
  * ` WKWebView ` 不支持页面缓存，需要自己注入 ` cookie ` , 而 ` UIWebView ` 是自动注入 ` cookie ` ； 
  * ` WKWebView ` 无法发送 ` POST ` 参数问题； 
  * ` WKWebView ` 可以和js直接互调函数，不像 ` UIWebView ` 需要第三方库 ` WebViewJavascriptBridge ` 来协助处理和 js 的交互； 

**注意：**

大多数App需要支持 ` iOS7 ` 以上的版本，而 ` WKWebView ` 只在 ` iOS8 ` 后才能用，所以需要一个兼容性方案，既 `
iOS7 ` 下用 ` UIWebView ` ， ` iOS8 ` 后用 ` WKWebView ` 。但是目前 ` IOS10 `
以下的系统以及很少了，

**小结：**

` WKWebView ` 相较于 ` UIWebView ` 在整体上有较大的提升，满足 iOS
上面使用同一套控件的功能，同时对整个内存的开销以及滚动刷新率和 JS 交互做了优化的处理。

依据 **职责单一原则** ，拆分成了三个协议去实现 ` WebView ` 的响应，解耦了 JS 交互和加载进度的响应处理。

` WKWebView ` 没有做缓存处理,所以 **对网页需要缓存的加载性能要求没那么高** 的还是可以考虑 ` UIWebView ` 。

###  二、WKWebView 有哪一些坑？

> 参考文章： [ 《WKWebView 那些坑》 ]()

####  1\. WKWebView 白屏问题

` WKWebView ` 实际上是个多进程组件，这也是它加载速度更快，内存暂用更低的原因。

在 ` UIWebView ` 上当内存占用太大的时候，App Process 会 crash；而在 ` WKWebView `
上当总体的内存占用比较大的时候，WebContent Process 会 crash，从而出现白屏现象。

**解决办法：**

  1. **借助 WKNavigtionDelegate**

当 ` WKWebView ` 总体内存占用过大，页面即将白屏的时候，系统会调用上面的回调函数，我们在该函数里执行 ` [webView reload] `
(这个时候 ` webView.URL ` 取值尚不为 ` nil `
）解决白屏问题。在一些高内存消耗的页面可能会频繁刷新当前页面，H5侧也要做相应的适配操作。

  1. **检测 webView.title 是否为空**

并不是所有 H5 页面白屏的时候都会调用上面的回调函数，比如，最近遇到在一个高内存消耗的 H5 页面上 present
系统相机，拍照完毕后返回原来页面的时候出现白屏现象（拍照过程消耗了大量内存，导致内存紧张，WebContent Process
被系统挂起），但上面的回调函数并没有被调用。在 ` WKWebView ` 白屏的时候，另一种现象是 ` webView.titile ` 会被置空,
因此，可以在 ` viewWillAppear ` 的时候检测 ` webView.title ` 是否为空来 ` reload ` 页面。

####  2\. WKWebView Cookie 问题

` WKWebView ` ` Cookie ` 问题在于 ` WKWebView ` 发起的请求不会自动带上存储于 `
NSHTTPCookieStorage ` 容器中的 ` Cookie ` ，而在 ` UIWebView ` 会自动带上 ` Cookie ` 。

**原因是：**

` WKWebView ` 拥有自己的私有存储，不会将 ` Cookie ` 存入到标准的 ` Cookie ` 容器 `
NSHTTPCookieStorage ` 中。

实践发现 ` WKWebView ` 实例其实也会将 ` Cookie ` 存储于 ` NSHTTPCookieStorage ` 中，但存储时机有延迟，在
` iOS 8 ` 上，当页面跳转的时候，当前页面的 ` Cookie ` 会写入 ` NSHTTPCookieStorage ` 中，而在 ` iOS
10 ` 上，JS 执行 ` document.cookie ` 或服务器 ` set-cookie ` 注入的 ` Cookie ` 会很快同步到 `
NSHTTPCookieStorage ` 中，FireFox 工程师曾建议通过 ` reset WKProcessPool ` 来触发 ` Cookie
` 同步到 ` NSHTTPCookieStorage ` 中，实践发现不起作用，并可能会引发当前页面 ` session cookie ` 丢失等问题。

**解决办法1：**

` WKWebView loadRequest ` 前，在 ` request header ` 中设置 ` Cookie ` , 解决首个请求 `
Cookie ` 带不上的问题；

**解决办法2：**

通过 ` document.cookie ` 设置 ` Cookie ` 解决后续页面(同域) ` Ajax ` `、iframe ` 请求的 `
Cookie ` 问题；(注意： ` document.cookie() ` 无法跨域设置 ` cookie`)。

####  3\. WKWebView loadRequest 问题

在 ` WKWebView ` 上通过 ` loadRequest ` 发起的 ` post ` 请求 ` body ` 数据会丢失，同样是由于
**进程间通信性能问题** ， ` HTTPBody ` 字段被丢弃。

####  4\. WKWebView NSURLProtocol问题

` WKWebView ` 在独立于 app 进程之外的进程中执行网络请求，请求数据不经过主进程，因此，在 ` WKWebView ` 上直接使用 `
NSURLProtocol ` 无法拦截请求。

**解决办法：**

由于 ` WKWebView ` 在独立进程里执行网络请求。一旦注册 ` http(s) scheme ` 后，网络请求将从 ` Network
Process ` 发送到 ` App Process ` ，这样 ` NSURLProtocol ` 才能拦截网络请求。在 ` webkit2 `
的设计里使用 ` MessageQueue ` 进行进程之间的通信，Network Process 会将请求 ` encode ` 成一个 `
Message ` ,然后通过 IPC 发送给 ` App Process ` 。出于性能的原因， ` encode ` 的时候 ` HTTPBody `
和 ` HTTPBodyStream ` 这两个字段会被丢弃掉了。

####  5\. WKWebView 页面样式问题

在 ` WKWebView ` 适配过程中，我们发现部分 H5 页面元素位置向下偏移或被拉伸变形，追踪后发现主要是 H5 页面高度值异常导致。

**解决办法：**

调整 ` WKWebView ` 布局方式，避免调整 ` webView.scrollView.contentInset ` 。实际上，即便在 `
UIWebView ` 上也不建议直接调整 ` webView.scrollView.contentInset `
的值，这确实会带来一些奇怪的问题。如果某些特殊情况下非得调整 ` contentInset ` 不可的话，可以通过下面方式让H5页面恢复正常显示。

####  6\. WKWebView 截屏问题

WKWebView 下通过 -[CALayer renderInContext:]实现截屏的方式失效，需要通过以下方式实现截屏功能：

    
    
    @implementation UIView (ImageSnapshot) 
    - (UIImage*)imageSnapshot { 
        UIGraphicsBeginImageContextWithOptions(self.bounds.size,YES,self.contentScaleFactor);
        [self drawViewHierarchyInRect:self.bounds afterScreenUpdates:YES]; 
        UIImage* newImage = UIGraphicsGetImageFromCurrentImageContext(); 
        UIGraphicsEndImageContext(); 
        return newImage; 
    } 
    @end

然而这种方式依然解决不了 ` webGL ` 页面的截屏问题，截屏结果不是空白就是纯黑图片。

**解决办法：**

无奈之下，我们只能约定一个JS接口，让游戏开发商实现该接口，具体是通过 ` canvas ` ` getImageData() ` 方法取得图片数据后返回
` base64 ` 格式的数据，客户端在需要截图的时候，调用这个JS接口获取 ` base64 String ` 并转换成 ` UIImage ` 。

####  7\. WKWebView crash问题

如果 ` WKWebView ` 退出的时候，JS刚好执行了 ` window.alert() ` , alert 框可能弹不出来， `
completionHandler ` 最后没有被执行，导致 ` crash ` ；

另一种情况是在 ` WKWebView ` 一打开，JS就执行 ` window.alert() ` ，这个时候由于 ` WKWebView ` 所在的 `
UIViewController ` 出现（ ` push ` 或 ` present ` ）的动画尚未结束，alert 框可能弹不出来， `
completionHandler ` 最后没有被执行，导致 ` crash ` 。

####  8\. 视频自动播放

` WKWebView ` 需要通过 ` WKWebViewConfiguration.mediaPlaybackRequiresUserAction `
设置是否允许自动播放，但一定要在 ` WKWebView ` 初始化之前设置，在 ` WKWebView ` 初始化之后设置无效。

####  9\. goBack API问题

` WKWebView ` 上调用 ` -[WKWebView goBack] ` , 回退到上一个页面后不会触发 ` window.onload() `
函数、不会执行JS。

####  10\. 页面滚动速率

` WKWebView ` 需要通过 ` scrollView delegate ` 调整滚动速率：

    
    
    - (void)scrollViewWillBeginDragging:(UIScrollView *)scrollView {
        scrollView.decelerationRate = UIScrollViewDecelerationRateNormal; 
    }

###  三、Crosswalk 是什么，它有什么作用？

> 参考网站： [ 《Crosswalk Github》 ]()  
>  参考文章： [ 《Crosswalk入门》 ]()

**Crosswalk** 是一款开源的 web 引擎。目前 **Crosswalk** 正式支持的移动操作系统包括 Android 和 Tizen ，在
Android 4.0 及以上的系统中使用 **Crosswalk** 的 Web 应用程序在 HTML5 方面可以有一致的体验，
**同时和系统的整合交互方面（比如启动画面、权限管理、应用切换、社交分享等等）可以做到类似原生应用** 。

现在 **Crosswalk** 已经成为众多知名 HTML5 平台和应用的推荐引擎，包括 Google Mobile Chrome App 、 Intel
XDK 、 Famo.us 和 Construct2 等等，未来的 Cordova 4.0 也计划集成 **Crosswalk** 。

###  四、常见的 WebView 性能优化方案有哪一些？

####  0\. 问题分析

首先需要了解，对于一个普通用户来讲，打开一个 WebView 通常会经历哪几个阶段，一般有这些：

  1. 交互无反馈; 
  2. 到达新的页面，页面白屏; 
  3. 页面基本框架出现，但是没有数据；页面处于loading状态; 
  4. 出现所需的数据; 

当 App 首次打开时，默认是并不初始化浏览器内核的；只有当创建 ` WebView ` 实例的时候，才会创建 ` WebView ` 的基础框架。

所以与浏览器不同，App 中打开 ` WebView ` 的第一步并不是建立连接，而是启动浏览器内核。

于是我们找到了“ **为什么WebView总是很慢** ”的原因之一：

  * 在浏览器中，我们输入地址时（甚至在之前），浏览器就可以开始加载页面。 
  * 而在客户端中，客户端需要先花费时间初始化 ` WebView ` 完成后，才开始加载。 

而这段时间，由于WebView还不存在，所有后续的过程是完全阻塞的。因此由于这段过程发生在 native
的代码中，单纯靠前端代码是无法优化的；大部分的方案都是前端和客户端协作完成，以下是几个业界采用过的方案：

####  1\. 全局 WebView

在客户端刚启动时，就初始化一个全局的 ` WebView ` 待用，并隐藏，当用户访问了 ` WebView ` 时，直接使用这个 ` WebView `
加载对应网页，并展示。

这种方法可以 **比较有效的减少 WebView 在App中的首次打开时间** 。当用户访问页面时，不需要初始化 WebView 的时间。

当然这也带来了一些问题，包括：

  * 额外的内存消耗。 
  * 页面间跳转需要清空上一个页面的痕迹，更容易内存泄露。 

####  2\. WebView 动态加载

> 参考文章： [ 《WebView常用优化方案》 ]()

` WebView ` 动态加载。就是不在 ` xml ` 中写 ` WebView ` ，写一个 ` layout ` ，然后把 ` WebView `
add 进去。

    
    
    WebView mWebView = new WebView(getApplicationgContext());
    LinearLayout mll = findViewById(R.id.xxx);
    mll.addView(mWebView);
    
    protected void onDestroy() {
        super.onDestroy();
        mWebView.removeAllViews();
        mWebView.destroy()
    }

这里用的 ` getApplicationContext() ` 也是防止内存溢出，这种方法有一个问题。如果你需要在 ` WebView `
中打开链接或者你打开的页面带有 flash，获得你的 ` WebView ` 想弹出一个 ` dialog ` ，都会导致从 `
ApplicationContext ` 到 ` ActivityContext ` 的强制类型转换错误，从而导致你应用崩溃。

这是因为在加载 flash 的时候，系统会首先把你的 ` WebView ` 作为父控件，然后在该控件上绘制 flash ，他想找一个 ` Activity
` 的 ` Context ` 来绘制他，但是你传入的是 ` ApplicationContext ` 。然后就崩溃了。

####  3\. 独立的web进程，与主进程隔开

> 参考文章： [ 《WebView常用优化方案》 ]()

这个方法被运用于类似 qq ，微信这样的超级 app 中，这也是解决任何 ` WebView ` 内存问题屡试不爽的方法 对于封装的 `
webactivity ` ，在 ` manifest.xml ` 中设置。

    
    
    <activity 
        android:name=".webview.WebViewActivity" 
        android:launchMode="singleTop" 
        android:process=":remote" 
        android:screenOrientation="unspecified" 
    />

然后在关闭 ` webactivity ` 时销毁进程：

    
    
    @Overrideprotected void onDestroy() {                
    super.onDestroy(); 
        System.exit(0);
    }

关闭浏览器后便销毁整个进程，这样一般 95% 的情况下不会造成内存泄漏之类的问题，但这就涉及到 android
进程间通讯，比较不方便处理，优劣参半，也是可选的一个方案。

####  4\. WebView 释放

> 参考文章： [ 《WebView常用优化方案》 ]()
    
    
    public void destroy() {
        if (mWebView != null) {
            // 如果先调用destroy()方法，则会命中if (isDestroyed()) return;这一行代码，需要先onDetachedFromWindow()，再
            // destory()
            ViewParent parent = mWebView.getParent();
            if (parent != null) {
                ((ViewGroup) parent).removeView(mWebView);
            }
    ​
            mWebView.stopLoading();
            // 退出时调用此方法，移除绑定的服务，否则某些特定系统会报错
            mWebView.getSettings().setJavaScriptEnabled(false);
            mWebView.clearHistory();
            mWebView.clearView();
            mWebView.removeAllViews();
    ​
            try {
                mWebView.destroy();
            } catch (Throwable ex) {
    ​
            }
        }
    }

###  五、在 Android 平台下如何调试 WebView？

####  1\. 在 Chrome 浏览器上调试

> 参考文章： [ 《Android调试webview》 ]()

**1.1 条件：**

  * 在 Android 设备或模拟器运行 Android4.4 或更高版本，Android 设备上启用 **USB调试模式** 。 
  * Chrome 30 或更高版本。更强大的 WebView 界面调试功能需要 Chrome31 或更高版本。 
  * Android 应用程序中的 WebView 配置为 **可调试模式** 。 

**1.2 Android 代码中配置 WebView 为可调试：**

    
    
    if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {  
        WebView.setWebContentsDebuggingEnabled(true);  
    }  

注意 web 调测不受 ` app manifest ` 文件中 ` debuggable ` 标记状态的影响，如果希望仅 ` debuggable ` 为
` true ` 时才能使用 web 调测，那么运行时检测此标记，如下：

    
    
    if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {  
        if ( 0 != ( getApplcationInfo().flags &= ApplicationInfo.FLAG_DEBUGGABLE ) ) {  
            WebView.setWebContentsDebuggingEnabled(true);  
        }  
    }  

**1.3 手机开启 USB 调试选项，并用 USB 连接电脑：**

开启 Android 手机的开发者选项，一般在 **系统设置** \- **Android版本**
进行多次点击会触发开启开发者选项，然后进入开发者选项页面，开启USB调试。

为了避免每次调试时看到此警告，勾选“ **总是允许从这台计算机** ”，并单击“ **确定** ”。

**1.4 在 Chrome 中启用设置“USB web debugging”（不会影响WebView）：**

在 Chrome 上访问 ` chrome://inspect/#devices ` 或 ` about:inspect ` 访问已启用调试的
WebView 列表， **需要翻墙** 。

然后在 WebView 列表中选择你要调试的页面，点击“ ` Inspect ` ”选项，跟调试 PC 网页一样，使用 Chrome 控制台进行调试。

**1.5 小技巧：**

（1）访问 ` chrome://inspect/#devices ` 如果 chrome 没有检测到 ` Remote Target `
中的页面，可能需要安装一下 Chrome 的 ADB 插件，也可以在 Chrome 翻墙访问 ` https://chrome-devtools-
frontend.appspot.com ` ；

（2）对于腾讯系的 APP，默认采用 X5内核 ，需要将 ` WebViewDebugHook ` 的 git 目录下的 ` debug.conf `
文件拷贝到 SD卡 的根目录下即可。

####  2\. 使用 DebugGap 调试

> 参考文章： [ 《Android下的webview调试》 ]()

**2.1 Windows 下载 DebugGap 并配置：**

在电脑上面下载 Windows 版本的 ` DebugGap ` 软件包（下载链接： [ DebugGap ]() ），下载完成后解压下来。

安装完成后，运行 ` DebugGap ` ，开始配置：

  * 通常情况下， ` DebugGap ` 可以自动获取IP，并设置默认的端口，如果没有，你可以手动设置； 
  * 点击“ **连接** ”按钮启动各种客户端的侦听器； 

**2.2 在客户端上配置：**

在调试项目中要进行测试的 HTML 界面中引入 ` debuggap.js ` 。

    
    
    <script src="debuggap.js" type="text/javascript"></script>

当调试项目的加载时，您的应用程序将会有一个蓝色的地方，点击会出现一个四叶三叶草的东西，点击“ **配置** ”，显示配置页面。输入与远程 DebugGap
上的主机和端口相同的主机和端口，例如 ` 192.168.1.4:11111 ` ，然后点击“ **连接** ”按钮。

1.4电脑端远程 DebugGap 将检测即将到来的客户端，开发人员可以单击每个客户端进行调试。

###  六、在 iOS 平台下如何调试 WebView？

> 参考文章： [ 《iOS之Safari调试webView/H5页面》 ]()

一般我们通过 Mac 的 Safari浏览器 来调试，但是要注意两点：

  * 如果调试的是 APP 中 WebView 的页面，则需要这个 APP 的包支持调试，如果不能调试，需要让 iOS 开发人员重签名 APP（可能需要将我们 iOS 设备的 ID 写入到可信任设备列表中，然后使用 iTunes 安装客户端提供的测试包即可）。 
  * 如果调试的是 H5 页面，可以直接在手机的 Safari浏览器 打开直接调试。 

下面开始说说在 Mac 上如何调试：

####  1\. 开启 Safari 开发菜单

先将 iPhone 连接到 Mac，在 Mac 的 Safari 偏好设置中，开启开发菜单。具体步骤为：Safari -> 偏好设置… -> 高级 ->
勾选在菜单栏显示“ **开发** ”菜单。

####  2\. iPhone 开启 Web检查器

具体步骤为：设置 -> Safari -> 高级 -> Web 检查器。

####  3\. 调试 APP 内的 WebView

> 参考文章： [ 《前端 WEBVIEW 指南之 IOS 调试篇》 ]()

在 Safari-> 开发中，看到自己的设备以及 WebView 中网页，点击后即可开启对应页面的 ` Inspector ` ，可以用来进行断点调试。

###  七、在内嵌版调试过程中，Fiddler 或 Charles 能起到什么作用？

这两者都是强大的抓包工具，原理是以 **web代理服务器** 的形式进行工作的，使用的代理地址是： ` 127.0.0.1 ` ，端口默认为 ` 8888
` ，我们也可以通过设置进行修改。

**代理**
就是在客户端和服务器之间设置一道关卡，客户端先将请求数据发送出去后，代理服务器会将数据包进行拦截，代理服务器再冒充客户端发送数据到服务器；同理，服务器将响应数据返回，代理服务器也会将数据拦截，再返回给客户端。

Fiddler 或 Charles 的主要作用有：

  * 可以代理请求，用来查看页面发送的请求和接收的响应； 
  * 可以修改请求的响应，用来模拟自己想要的数据； 
  * 可以模拟网络请求的速度； 
  * 可以代理服务器的静态资源请求，指向本地文件，省去频繁发布 H5 包，达到快速调试目的； 

> 补充链接： [ 《Fiddler工具使用介绍一》 ]()

###  八、调试企业微信、微信和钉钉版时，可以使用哪些工具？

####  1\. 调试企业微信、微信

  * **[ 微信开发者工具 ]() ** ，可以用来调试页面基本功能； 
  * **[ 企业微信接口调试工具 ]() ** ，可以用来调试企业微信的接口； 

####  2\. 调试钉钉

  * **[ 钉钉Android开发版 ]() ** ，用来调试Android上的钉钉应用； 

####  3\. 通用

  * **Fiddler 或 Charles** ，可以拦截接口替换文件，来调试应用； 

###  九、常见的调试技巧有哪些？

####  1\. Chrome 控制台调试

> 参考文章： [ 《前端常见调试技巧篇总结（持续更新...）》 ]()

**1.1 Source 面板断点调试 JS**  
从左到右，各个图标表示的功能分别为：

  * ` Pause/Resume script execution ` ：暂停/恢复脚本执行（程序执行到下一断点停止）。 
  * ` Step over next function call ` ：执行到下一步的函数调用（跳到下一行）。 
  * ` Step into next function call ` ：进入当前函数。 
  * ` Step out of current function ` ：跳出当前执行函数。 
  * ` Deactive/Active all breakpoints ` ：关闭/开启所有断点（不会取消）。 
  * ` Pause on exceptions ` ：异常情况自动断点设置。 

**1.2 Element 面板调试 DOM：**

右击元素，选择 ` break on ` 选项：

  * ` Subtree modifications ` 选项，是指 **当节点内部子节点变化时断点** ； 

  * ` Attributes modifications ` 选项，是指 **当节点属性发生变化时断点** ； 

  * ` node removal ` 选项，是指 **当节点被移除时断点** ； 

####  2\. console 调试

> 参考文章： [ 《Console调试常用用法》 ]()

**2.1 显示信息的命令：**

    
    
    console.log("normal");         // 用于输出普通信息
    console.info("information");   // 用于输出提示性信息
    console.error("error");        // 用于输出错误信息
    console.warn("warn");          // 用于输出警示信息
    console.clear();               // 清空控制台信息

**2.2 计时功能：**

` console.time() ` 和 ` console.timeEnd() ` ：

    
    
    console.time("控制台计时器");
    for(var i = 0; i < 10000; i++){
        for(var j = 0; j < 10000; j++){}       
    }
    console.timeEnd("控制台计时器")

**2.3 信息分组：**

` console.group() ` 和 ` console.groupEnd() ` ：

    
    
    console.group("第一组信息");
        console.log("第一组第一条：我的博客");
        console.log("第一组第二条：CSDN");
    console.groupEnd();
    
    console.group("第二组信息");
        console.log("第二组第一条：程序爱好者QQ群");
        console.log("第二组第二条：欢迎你加入");
    console.groupEnd();

**2.4 将对象以树状结构展现：**

` console.dir() ` 可以显示一个对象所有的属性和方法：

    
    
    var info = {
        name : "Alan",
        age : "27",
        grilFriend : "nothing",
        getName : function(){
            return this.name;
        }
    }
    console.dir(info);

**2.5 显示某个节点的内容：**

` console.dirxml() ` 用来显示网页的某个节点( ` node ` ) 所包含的 ` html/xml ` 代码：

    
    
    var node = document.getElementById("info");
    node.innerHTML += "<p>追加的元素显示吗</p>";
    console.dirxml(node);

**2.5 统计代码被执行的次数：**

使用 ` console.count() ` ：

    
    
    function myFunction(){
        console.count("myFunction 被执行的次数");
    }
    myFunction();       //myFunction 被执行的次数: 1
    myFunction();       //myFunction 被执行的次数: 2
    myFunction();       //myFunction 被执行的次数: 3

**2.6 输出表格：**

    
    
    console.table(mytable);

####  3\. 调试各种页面尺寸

虽然把各种各样的手机都摆在桌子上看起来很酷，但却很不现实。但是，浏览器内却提供了你所需要的一切。进入检查面板点击“ **切换设备模式**
”按钮。这样，就可以在窗口内调整视窗的大小。

####  4\. debugger 断点

具体的说就是通过在代码中添加" ` debugger; ` "语句，当代码执行到该语句的时候就会自动断点。

###  结语

对于初入混合应用开发的小伙伴，还有经常需要调试混合应用的小伙伴，相信会有帮助😁

大家加油~

###  关于我

> 本文首发在 [ pingan8787个人博客 ]() ，如需转载请保留个人介绍。

Author  |  王平安   
---|---  
E-mail  |  pingan8787@qq.com   
博 客  |  www.pingan8787.com   
微 信  |  pingan8787   
每日文章推荐  |  [ https://github.com/pingan8787... ]()  
ES小册  |  js.pingan8787.com   
  
###  微信公众号

