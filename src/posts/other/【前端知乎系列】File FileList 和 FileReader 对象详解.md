---
date: 2023-05-23
category:
    - javascript
tag:
    - javascript
    - typescript
---
 # 【前端知乎系列】File FileList 和 FileReader 对象详解
> 本文首发在我的【 [ 个人博客 ]() 】  
>  更多丰富的前端学习资料，可以查看我的 **Github** : [ 《Leo-JavaScript》 ]() ，内容涵盖 **数据结构与算法** 、
> **HTTP** 、 **Hybrid** 、 **面试题** 、 **React** 、 **Angular** 、 **TypeScript** 和
> **Webpack** 等等。  
>  点个 Star 不迷路~

欢迎阅读《前端知乎系列》：

  * [ 《【前端知乎】443- ArrayBuffer 与 Blob 对象详解》 ]()

` File ` 对象、 ` FileList ` 对象与 ` FileReader `
对象大家或许不太陌生，常见于文件上传下载操作处理（如处理图片上传预览，读取文件内容，监控文件上传进度等问题）。

那么本文将与大家深入介绍两者。

##  一、File 对象

###  1\. 概念介绍

` File ` 对象提供有关文件的信息，并允许网页中的 JavaScript 读写文件。

最常见的使用场合是表单的文件上传控件，用户在一个 ` <input type="file"> `
元素上选择文件后，浏览器会生成一个数组，里面是每一个用户选中的文件，它们都是 ` File ` 实例对象。

另外值得提到一点： ` File ` 对象是一种特殊 ` Blob ` 对象，并且可以用在任意的 ` Blob ` 对象的 ` context `
中。比如说， ` FileReader ` , ` URL.createObjectURL() ` , ` createImageBitmap() ` ,
及 ` XMLHttpRequest.send() ` 都能处理 ` Blob ` 和 ` File ` 。

    
    
    // HTML 代码如下
    // <input id="fileItem" type="file">
    const file = document.getElementById('fileItem').files[0];
    file instanceof File // true

###  2\. 对象使用

浏览器原生提供一个 ` File() ` 构造函数，用来生成 ` File ` 实例对象。

    
    
    const myFile = new File(bits, name[, options]);

参数：

  * ` bits ` ： 

一个数组，表示文件的内容。成员可以是 ` ArrayBuffer ` ， ` ArrayBufferView ` ， ` Blob ` ，或者 `
DOMString ` 对象的 ` Array ` ，或者任何这些对象的组合。

通过这个参数，也可以实现 ` ArrayBuffer ` ， ` ArrayBufferView ` ， ` Blob ` 转换为 ` File ` 对象。

  * ` name ` ： 

字符串，表示文件名或文件路径。

  * ` options ` ： 

配置对象，设置实例的属性。该参数可选。可选值有如下两种：

` type ` : ` DOMString ` ，表示将要放到文件中的内容的 MIME 类型。默认值为 ` "" ` 。  
` lastModified ` : 数值，表示文件最后修改时间的 Unix 时间戳（毫秒）。默认值为 ` Date.now() ` 。

示例：

    
    
    const myFile = new File(['leo1', 'leo2'], 'leo.txt', {type: 'text/plain'});

根据已有的 blob 对象创建 File 对象:

    
    
    const myFile = new File([blob], 'leo.png', {type: 'image/png'});

###  3\. 实例属性和方法

####  3.1 实例属性

实例有以下几个属性：

  * ` File.lastModified ` ：最后修改时间。只读 

自 UNIX 时间起始值（1970年1月1日 00:00:00 UTC）以来的毫秒数

  * ` File.name ` ：文件名或文件路径。只读 

出于安全考虑，返回值不包含文件路径 。

  * ` File.size ` ：文件大小（单位字节）。只读 
  * ` File.type ` ：文件的 MIME 类型。只读 

    
    
    // HTML 代码如下
    // <input id="fileItem" type="file">
    const myFile = document.getElementById('fileItem')
    myFile.addEventListener('change', function(e){
        const file = this.files[0];
        console.log(file.name);
        console.log(file.size);
        console.log(file.lastModified);
        console.log(file.lastModifiedDate);
    });

####  3.2 实例方法

` File ` 对象没有定义任何方法，但是它从 Blob 接口继承了以下方法：

  * ` Blob.slice([start[, end[, contentType]]]) `

返回一个新的 ` Blob ` 对象，它包含有源 ` Blob ` 对象中指定范围内的数据。

###  4\. 兼容性

##  二、FileList 对象

###  1\. 概念介绍

` FileList ` 对象是一个类数组对象，每个成员都是一个 ` File ` 实例，主要出现在两种场合：

  * 通过 ` <input type="file"> ` 控件的 ` files ` 属性，返回一个 ` FileList ` 实例。 

另外，当 ` input ` 元素拥有 ` multiple ` 属性，则可以用它来选择多个文件。

  * 通过拖放文件，查看 ` DataTransfer.files ` 属性，返回一个 ` FileList ` 实例。 

    
    
    // HTML 代码如下
    // <input id="fileItem" type="file">
    const files = document.getElementById('fileItem').files;
    files instanceof FileList // true
    
    const firstFile = files[0];

###  2\. 对象使用

所有 ` type ` 属性为 ` file ` 的 ` <input> ` 元素都有一个 ` files ` 属性， **用来存储用户所选择的文件** .
例如:

###  3\. 实例属性和方法

####  3.1 实例属性

实例只有一个属性：

  * ` FileList.length ` ：返回列表中的文件数量。只读 

####  3.2 实例方法

实例只有一个方法：

  * ` FileList.item() ` ：用来返回指定位置的实例，从 0 开始。 

由于 ` FileList ` 实例是个类数组对象，可以直接用方括号运算符，即 ` myFileList[0] ` 等同于 `
myFileList.item(0) ` ，所以一般用不到 ` item() ` 方法。

###  4\. 兼容性

###  5\. 实例

选择多个文件，并获取每个文件信息：

    
    
    // HTML 代码如下
    // <input id="myfiles" multiple type="file">
    const myFile = document.querySelector("#myfiles");
    myFile.addEventListener('change', function(e){
        let files = this.files;
        let fileLength = files.length;
        let i = 0;
        while ( i < fileLength) {
            let file = files[i];
            console.log(file.name);
            i++;
        }    
    });

##  三、FileReader 对象

###  1\. 概念介绍

` FileReader ` 对象允许 Web 应用程序异步读取存储在用户计算机上的文件（或原始数据缓冲区）的内容，使用 ` File ` 或 ` Blob
` 对象指定要读取的文件或数据。

简单理解，就是用于读取 ` File ` 对象或 ` Blob ` 对象所包含的文件内容。

###  2\. 对象使用

浏览器原生提供一个 ` FileReader ` 构造函数，用来生成 ` FileReader ` 实例。

    
    
    const reader = new FileReader();

###  3\. 实例属性和方法

` FileReader ` 对象拥有的属性和方法较多。

####  3.1 实例属性

  * ` FileReader.error ` : 表示在读取文件时发生的错误。只读 
  * ` FileReader.readyState ` : 整数，表示读取文件时的当前状态。只读 

共有三种状态：  
0 : EMPTY，表示尚未加载任何数据；  
1 : LOADING，表示数据正在加载；  
2 : DONE，表示加载完成；

  * ` FileReader.result ` 读取完成后的文件内容。只读 

仅在读取操作完成后才有效，返回的数据格式 **取决于使用哪个方法来启动读取操作** 。

####  3.2 事件处理

  * ` FileReader.onabort ` : 处理 ` abort ` 事件。该事件在读取操作 **被中断** 时触发。 
  * ` FileReader.onerror ` : 处理 ` error ` 事件。该事件在读取操作 **发生错误** 时触发。 
  * ` FileReader.onload ` : 处理 ` load ` 事件。该事件在读取操作 **完成** 时触发。 
  * ` FileReader.onloadstart ` : 处理 ` loadstar ` t事件。该事件在读取操作 **开始** 时触发。 
  * ` FileReader.onloadend ` : 处理 ` loadend ` 事件。该事件在读取操 **作结束** 时（要么成功，要么失败）触发。 
  * ` FileReader.onprogress ` : 处理 ` progress ` 事件。该事件在读取 **Blob** 时触发。 

####  3.3 实例方法

  * ` FileReader.abort() ` ：终止读取操作， ` readyState ` 属性将变成2。 
  * ` FileReader.readAsArrayBuffer() ` ：以 ` ArrayBuffer ` 的格式读取文件，读取完成后 ` result ` 属性将返回一个 ` ArrayBuffer ` 实例。 
  * ` FileReader.readAsBinaryString() ` ：读取完成后， ` result ` 属性将 **返回原始的二进制字符串** 。 
  * ` FileReader.readAsDataURL() ` ：读取完成后， ` result ` 属性将返回一个 Data URL 格式（Base64 编码）的字符串，代表文件内容。 

对于图片文件，这个字符串可以用于 ` <img> ` 元素的 ` src ` 属性。注意，这个字符串不能直接进行 Base64 解码，必须把前缀 `
data:*/*;base64 ` ,从字符串里删除以后，再进行解码。

  * ` FileReader.readAsText() ` ：读取完成后， ` result ` 属性将返回文件内容的文本字符串。 

该方法的第一个参数是代表文件的 Blob 实例，第二个参数是可选的，表示文本编码，默认为 ` UTF-8 ` 。

###  4\. 兼容性

###  5\. 实例

这里举一个图片预览的实例：

    
    
    /* HTML 代码如下
      <input type="file" onchange="previewFile()">
      <img src="" height="200">
    */
    
    function previewFile() {
      let preview = document.querySelector('img');
      let file    = document.querySelector('input[type=file]').files[0];
      let reader  = new FileReader();
    
      reader.addEventListener('load', function () {
        preview.src = reader.result;
      }, false);
    
      if (file) {
        reader.readAsDataURL(file);
      }
    }

##  四、参考资料

  1. [ 《File 对象，FileList 对象，FileReader 对象》 ]()
  2. [ MDN ]()

##  五、关于我

> 本文首发在 [ pingan8787个人博客 ]() ，如需转载请保留个人介绍。

Author  |  王平安   
---|---  
E-mail  |  pingan8787@qq.com   
博 客  |  www.pingan8787.com   
微 信  |  pingan8787   
每日文章推荐  |  [ https://github.com/pingan8787... ]()  
ES小册  |  js.pingan8787.com 

