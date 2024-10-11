---
date: 2024-08-17
category:
    - javascript
tag:
    - javascript
    - 前端
    - ecmascript-6
    - html
---
 # 【前端知乎系列】ArrayBuffer 和 Blob 对象
> 本文首发在我的【 [ 个人博客 ]() 】  
>  更多丰富的前端学习资料，可以查看我的 **Github** : [ 《Leo-JavaScript》 ]() ，内容涵盖 **数据结构与算法** 、
> **HTTP** 、 **Hybrid** 、 **面试题** 、 **React** 、 **Angular** 、 **TypeScript** 和
> **Webpack** 等等。  
>  点个 Star 不迷路~

` ArrayBuffer ` 对象与 ` Blob ` 对象大家或许不太陌生，常见于文件上传操作处理（如处理图片上传预览等问题）。

那么本文将与大家深入介绍两者。

##  一、ArrayBuffer 对象

` ArrayBuffer ` 对象是 ES6 才纳入正式 ECMAScript 规范，是 JavaScript **操作二进制数据** 的一个接口。 `
ArrayBuffer ` 对象是以数组的语法处理二进制数据，也称二进制数组。

介绍 ` ArrayBuffer ` 对象还需介绍 ` TypedArray ` 视图和 ` DataView `
视图，本文不具体介绍，详细可以查看阮一峰老师 [ 《ECMAScript 6 入门 ArrayBuffer》 ]() 章节。

###  1\. 概念介绍

` ArrayBuffer ` 对象代表储存二进制数据的一段内存，它不能直接读写，只能通过视图（ ` TypedArray ` 视图和 ` DataView
` 视图）来读写，视图的作用是以指定格式解读二进制数据。

关于 ` TypedArray ` 视图和 ` DataView ` 视图 ，可以查看阮一峰老师 [ 《ECMAScript 6 入门
ArrayBuffer》 ]() 章节的介绍。

###  2\. 对象使用

浏览器原生提供 ` ArrayBuffer() ` 构造函数，用来生成实例。

参数：

  * 整数，表示二进制数据占用的字节长度。 

返回值：

  * 一个指定大小的 ` ArrayBuffer ` 对象，其内容被初始化为 0。 

    
    
    const buffer = new ArrayBuffer(32);

上面代码表示实例对象 ` buffer ` 占用 32 个字节。

###  3\. 实例属性和方法

` ArrayBuffer ` 对象有实例属性 ` byteLength ` ，表示当前实例 **占用的内存字节长度** （单位字节），
**一单创建就不可变更（只读）** ：

    
    
    const buffer = new ArrayBuffer(32);
    buffer.byteLength; // 32

` ArrayBuffer ` 对象有实例方法 ` slice() ` ，用来复制一部分内存。

参数如下：

  * start，整数类型，表示开始复制的位置。默认从 0 开始。 
  * end，整数类型，表示结束复制的位置（不包括结束的位置）。如果省略，则表示复制到结束。 

    
    
    const buffer = new ArrayBuffer(32);
    const buffer2 = buffer.slice(0);

###  4\. 兼容性

图片来自 MDN

##  二、Blob 对象

###  1\. 概念介绍

` Blob ` 全称： ` Binary Large Object ` （二进制大型对象）。

` Blob ` 对象表示一个二进制文件的数据内容，通常用来 **读写文件** ，比如一个图片文件的内容就可以通过 ` Blob ` 对象读写。

与 ` ArrayBuffer ` 区别：

  * ` Blob ` 用于操作 **二进制文件**
  * ` ArrayBuffer ` 用于操作 **内存**

###  2\. 对象使用

浏览器原生提供 ` Blob() ` 构造函数，用来生成实例。

` Blob ` 的内容由参数数组中给出的值的串联组成。

    
    
    const leoBlob = new Blob(array [, options]);

参数：

  * ` array ` ，必填，成员是字符串或二进制对象，表示新生成的Blob实例对象的内容； 

成员可以是一个由 ` ArrayBuffer ` , ` ArrayBufferView ` , ` Blob ` , ` DOMString `
等对象构成的 ` Array ` ，或者其他类似对象的混合体，它将会被放进 ` Blob ` 。 ` DOMStrings ` 会被编码为 ` UTF-8
` 。

  * ` options ` ，可选，是一个配置对象，这里介绍常用的属性 ` type ` ，表示数据的 MIME 类型，默认空字符串； 

` options ` 目前可能有两个属性： ` type ` 和 ` endings ` 。

` endings ` 用于指定包含行结束符 ` \n ` 的字符串如何被写入，默认值 ` transparent ` 。它只有这两个值： ` native
` （代表行结束符会被更改为适合宿主操作系统文件系统的换行符）和 ` transparent ` （代表会保持blob中保存的结束符不变）。

使用案例：

    
    
    const leoHtmlFragment = ['<a id="a"><b id="b">hey leo！</b></a>']; // 一个包含 DOMString 的数组
    const leoBlob = new Blob(leoHtmlFragment, {type : 'text/html'});   // 得到 blob

该代码中，实例对象 ` leoBlob ` 包含的是字符串。生成实例时，指定数据类型为 ` text/html ` 。

还可以使用 Blob 保存 JSON 数据：

    
    
    const obj = { hello: 'leo' };
    const blob = new Blob([ JSON.stringify(obj) ], {type : 'application/json'});

###  3\. 实例属性和方法

` Blob ` 具有两个实例属性：

  * ` size ` ：文件的大小，单位为字节。 
  * ` type ` ：文件的 MIME 类型。如果类型无法确定，则返回空字符串。 

    
    
    const leoHtmlFragment = ['<a id="a"><b id="b">hey leo！</b></a>']; // 一个包含 DOMString 的数组
    const leoBlob = new Blob(leoHtmlFragment, {type : 'text/html'});   // 得到 blob
    
    leoBlob.size; // 38
    leoBlob.type; // "text/html"

` Blob ` 实例方法：

  * ` clice ` ：方法用于创建一个包含源 ` Blob ` 的指定字节范围内的数据的新 ` Blob ` 对象。 

    
    
    const newBlob = oldBlob.slice([start [, end [, contentType]]])

包含三个参数：

` start ` ，可选，起始的字节位置，默认 0；

` end ` ，可选，结束的字节位置，默认 ` size ` 属性的值，不包含该位置；

` contentType ` ，可选，新实例的数据类型（默认为空字符串）；

###  4\. 兼容性

图片来自 MDN

###  5\. 实际案例

####  5.1 获取文件信息

文件选择器 ` <input type="file"> ` 用来让用户选取文件。出于安全考虑，浏览器不允许脚本自行设置这个控件的 ` value `
属性，即 **文件必须是用户手动选取的，不能是脚本指定的** 。一旦用户选好了文件，脚本就可以读取这个文件。

文件选择器返回一个 ` FileList ` 对象，该对象是个类数组对象，每个成员都是一个 ` File ` 实例对象。 ` File `
实例对象是一个特殊的 ` Blob ` 实例，增加了 ` name ` 和 ` lastModifiedDate ` 属性。

也包括 **拖放 API** 的 ` dataTransfer.files ` 返回的也是一个 ` FileList ` 对象，成员也是 ` File `
实例对象。

    
    
    // HTML 代码如下
    // <input type="file" accept="image/*" multiple onchange="fileinfo(this.files)"/>
    
    function fileinfo(files) {
      for (let i = 0; i < files.length; i++) {
        let f = files[i];
        console.log(
          f.name, // 文件名，不含路径
          f.size, // 文件大小，Blob 实例属性
          f.type, // 文件类型，Blob 实例属性
          f.lastModifiedDate // 文件的最后修改时间
        );
      }
    }

####  5.2 下载文件

在 AJAX 请求中，指定 ` responseType ` 属性为 ` blob ` ，皆可以下下载一个 Blob 对象。

    
    
    function getBlob(url, callback) {
      const xhr = new XMLHttpRequest();
      xhr.open('GET', url);
      xhr.responseType = 'blob';
      xhr.onload = function () {
        callback(xhr.response);
      }
      xhr.send(null);
    }

然后， ` xhr.response ` 拿到的就是一个 ` Blob ` 对象。

####  5.3 生成 URL

浏览器允许使用 ` URL.createObjectURL() ` 方法，针对 ` Blob ` 对象生成一个临时 ` URL ` ，以便于某些 ` API
` 使用。

如作为图片预览的 URL。

这个 URL 以 ` blob:// ` 开头，表明对应一个 ` Blob ` 对象，协议头后面是一个识别符，用来唯一对应内存里面的 Blob
对象。这一点与 ` data://URL ` （URL 包含实际数据）和 ` file://URL ` （本地文件系统里面的文件）都不一样。

    
    
    const droptarget = document.getElementById('droptarget');
    
    droptarget.ondrop = function (e) {
      const files = e.dataTransfer.files;
      for (let i = 0; i < files.length; i++) {
        let type = files[i].type;
        if (type.substring(0,6) !== 'image/')
          continue;
        let img = document.createElement('img');
        img.src = URL.createObjectURL(files[i]);
        img.onload = function () {
          this.width = 100;
          document.body.appendChild(this);
          URL.revokeObjectURL(this.src);
        }
      }
    }

代码中，通过为拖放的图片文件生成一个 URL，作为预览的缩略图。

浏览器处理 Blob URL 就跟普通的 URL 一样，如果 ` Blob ` 对象不存在，返回404状态码；如果跨域请求，返回403状态码。Blob
URL 只对 ` GET ` 请求有效，如果请求成功，返回200状态码。由于 Blob URL 就是普通 URL，因此可以下载。

####  5.4 读取文件

取得 ` Blob ` 对象以后，可以通过 ` FileReader ` 对象，读取 ` Blob ` 对象的内容，即文件内容。

` FileReader ` 对象提供四个方法。将 Blob 对象作为参数传入，然后以指定的格式返回。

  * ` FileReader.readAsText() ` ：返回文本，需要指定文本编码，默认为 UTF-8。 
  * ` FileReader.readAsArrayBuffer() ` ：返回 ArrayBuffer 对象。 
  * ` FileReader.readAsDataURL() ` ：返回 Data URL。 
  * ` FileReader.readAsBinaryString() ` ：返回原始的二进制字符串。 

下面是 ` FileReader.readAsText() ` 方法的例子，用来读取文本文件：

    
    
    // HTML 代码如下
    // <input type='file' onchange='readfile(this.files[0])'></input>
    // <pre id='output'></pre>
    function readfile(f) {
      let reader = new FileReader();
      reader.readAsText(f);
      reader.onload = function () {
        let text = reader.result;
        let out = document.getElementById('output');
        out.innerHTML = '';
        out.appendChild(document.createTextNode(text));
      }
      reader.onerror = function(e) {
        console.log('Error', e);
      };
    }

下面是 ` FileReader.readAsArrayBuffer() ` 方法的例子，用于读取二进制文件：

    
    
    // HTML 代码如下
    // <input type="file" onchange="typefile(this.files[0])"></input>
    function typefile(file) {
      // 文件开头的四个字节，生成一个 Blob 对象
      let slice = file.slice(0, 4);
      let reader = new FileReader();
      // 读取这四个字节
      reader.readAsArrayBuffer(slice);
      reader.onload = function (e) {
        let buffer = reader.result;
        // 将这四个字节的内容，视作一个32位整数
        let view = new DataView(buffer);
        let magic = view.getUint32(0, false);
        // 根据文件的前四个字节，判断它的类型
        switch(magic) {
          case 0x89504E47: file.verified_type = 'image/png'; break;
          case 0x47494638: file.verified_type = 'image/gif'; break;
          case 0x25504446: file.verified_type = 'application/pdf'; break;
          case 0x504b0304: file.verified_type = 'application/zip'; break;
        }
        console.log(file.name, file.verified_type);
      };
    }

##  三、参考资料

  1. [ 《ArrayBuffer 对象，Blob 对象》 ]()
  2. [ 《ECMAScript 6 入门 ArrayBuffer》 ]()

##  四、关于我

> 本文首发在 [ pingan8787个人博客 ]() ，如需转载请保留个人介绍。

Author  |  王平安   
---|---  
E-mail  |  pingan8787@qq.com   
博 客  |  www.pingan8787.com   
微 信  |  pingan8787   
每日文章推荐  |  [ https://github.com/pingan8787... ]()  
ES小册  |  js.pingan8787.com 

