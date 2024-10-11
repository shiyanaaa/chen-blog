---
date: 2023-11-20
category:
    - es10
tag:
    - es10
    - ecmascript
    - javascript
---
 # 【CuteJavaScript】ES2019 新特性汇总
最近 ECMAScript2019，最新提案完成： [ tc39 Finished Proposals ]()
，我这里也是按照官方介绍的顺序进行整理，如有疑问，可以查看官方介绍啦~

另外之前也整理了 [ 《ES6/ES7/ES8/ES9系列》 ]() ，可以一起看哈。

##  1\. 可选的 catch 绑定

###  1.1 介绍

在 ECMAScript2019 最新提案中，支持我们在使用 ` try catch ` 错误异常处理时，选择性的给 ` catch ` 传入参数。

即我们可以不传入 ` catch ` 参数。

正常使用 ` try catch ` ：

    
    
    try {
        // todo 
    } catch (err){
        console.log('err：',err)
    }

在 ES10 中可以这么使用：

    
    
    try {
        // todo 
    } catch {
        // todo 
    }

###  1.2 使用场景

当我们不需要对 ` catch `
返回的错误信息进行处理时，比如：我们对于一些数据处理，经常会出现格式报错，但是我们并不关心这个错误，我们只需要继续处理，或重新请求数据等。

这种情况，我们就可以使用这个新特性，当然，还是需要根据实际情况考虑。

##  2\. JSON.superset

###  2.1 介绍

  * **来源背景** ： 

由于在 ES2019 之前不支持转义 **行分隔符** ( ` \u2028 ` ) 和 **段落分隔符** ( ` \u2029 ` )
字符，并且在解析过程中会报错: ` SyntaxError: Invalid or unexpected token ` 。

    
    
    const LS = "";
    const PS = eval("'\u2029'");// SyntaxError: Invalid or unexpected token

  * **解决方案** ： 

JSON 语法由 **ECMA-404** 定义并由 **RFC 7159** 永久修复，允许 **行分隔符** ( ` \u2028 ` ) 和
**段落分隔符** ( ` \u2029 ` ) 字符，直接出现在字符串中。

###  2.2 使用

在 ES10 中，我们就可以直接使用 ` eval("'\u2029'"); ` 而不会再提示错误。

##  3\. Symbol.prototype.description

###  3.1 介绍

在 ES6 中引入 Symbol 这个 **基本数据类型** ，可以实现一些数据内省等高级功能。

这次 ES10 中，为 Symbol 类型增加 ` Symbol.prototype.description ` 的一个访问器属性，用来获取 `
Symbol ` 类型数据的描述信息（description）。

###  3.2 使用

MDN 上的案例介绍：

    
    
    console.log(Symbol('pingan8787').description);
    // expected output: "pingan8787"
    
    console.log(Symbol.iterator.description);
    // expected output: "Symbol.iterator"
    
    console.log(Symbol.for('leo').description);
    // expected output: "leo"
    
    console.log(Symbol('pingan8787').description + ' and leo!');
    // expected output: "pingan8787 and leo!"

另外我们也可以这么使用：

    
    
    let pingan = Symbol('pingan8787').description;
    console.log(pingan === 'pingan8787'); // true

##  4\. Function.prototype.toString

###  4.1 介绍

在 ES10 之前，我们对一个函数调用 ` toString() ` 方法，返回的结果中会将注释信息去除。

在 ES10 之后，函数再调用 ` toString() ` 方法，将准确返回原有内容，包括 **空格** 和 **注释** 等：

    
    
    let pingan8787 = function(){
        // do something
        console.log('leo')
    }
    pingan8787.toString();
    /**
    "function(){
        // do something
        console.log('leo')
    }"
    */

##  5\. Object.fromEntries

###  5.1 介绍

` Object.fromEntries ` 是 ES10 中新的静态方法，用于 **将键值对列表转换为对象** 。

` Object.fromEntries() ` 方法接收一个 **键值对的列表参数** ，并返回一个带有这些键值对的 **新对象** 。

这个迭代参数应该是一个能够实现 ` @iterator ` 方法的的对象，返回一个迭代器对象。它生成一个具有两个元素的类数组的对象，第一个元素是
**将用作属性键的值** ，第二个元素是 **与该属性键关联的值** 。

` Object.fromEntries() ` 是 ` Object.entries ` 的反转。

###  5.2 使用

  * ` Object.entries ` 和 ` Object.fromEntries() ` 互转 

    
    
    let leo = { name: 'pingan8787', age: 10};
    let arr = Object.entries(leo);
    console.log(arr);// [["name", "pingan8787"],["age", 10]]
    
    let obj = Object.fromEntries(arr);
    console.log(obj);// {name: "pingan8787", age: 10}

  * ` Map ` 转化为 ` Object `

    
    
    const map = new Map([ ['name', 'pingan8787'], ['age', 10] ]);
    const obj = Object.fromEntries(map);
    console.log(obj); // {name: "pingan8787", age: 10}

  * ` Array ` 转化为 ` Object `

    
    
    const arr = [ ['name', 'pingan8787'], ['age', 10] ];
    const obj = Object.fromEntries(arr);
    console.log(obj); // {name: "pingan8787", age: 10}

##  6\. 更友好的 JSON.stringify

###  6.1 介绍

更友好的 ` JSON.stringify ` ，对于一些超出范围的 Unicode 字符串，为其输出转义序列，使其成为有效 Unicode 字符串。

###  6.2 使用

    
    
    // Non-BMP characters still serialize to surrogate pairs.
    JSON.stringify('?')
    // → '"?"'
    JSON.stringify('\uD834\uDF06')
    // → '"?"'
    
    // Unpaired surrogate code units will serialize to escape sequences.
    JSON.stringify('\uDF06\uD834')
    // → '"\\udf06\\ud834"'
    JSON.stringify('\uDEAD')
    // → '"\\udead"'

##  7\. String.prototype.{trimStart,trimEnd}

###  7.1 String.prototype.trimStart

` trimStart() ` 方法从字符串的开头删除空格，返回一个 **新字符串** ，表示从其开头（左端）剥离空格的调用字符串，
**不会直接修改原字符串本身** 。

` trimLeft() ` 是此方法的别名。

    
    
    let pingan8787 = '   Hello pingan8787!   ';
    console.log(pingan8787);        // "   Hello pingan8787!   ";
    console.log(pingan8787.length); // 23;
    
    console.log(pingan8787.trimStart());        // "Hello pingan8787!   ";
    console.log(pingan8787.trimStart().length); // 20;
    

###  7.2 String.prototype.trimEnd

` trimEnd() ` 方法从一个字符串的右端移除空白字符，返回一个 **新字符串** ，表示从其（右）端剥去空白的调用字符串，
**不会直接修改原字符串本身** 。

` trimRight() ` 是此方法的别名。

    
    
    let pingan8787 = '   Hello pingan8787!   ';
    console.log(pingan8787);        // "   Hello pingan8787!   ";
    console.log(pingan8787.length); // 23;
    
    console.log(pingan8787.trimEnd());        // "   Hello pingan8787!";
    console.log(pingan8787.trimEnd().length); // 20;
    

##  8\. Array.prototype.{flat,flatMap}

在 ES10 之前，我们要将一个数组打平，由于官方没有对应 API，我们可能需要 lodash  
活着手写循环去操作。

###  8.1 Array.prototype.flat

在 ES10 中，官方新增一个 ` Array.prototype.flat `
方法，将数组第一层数据打平，也仅限第一层。如果我们需要将多层递归，则需要显式传入参数：

    
    
    [1,2,3,[1,2,[3, [4]]]].flat(2);
    // [1, 2, 3, 1, 2, 3, [4]]

###  8.2 Array.prototype.flatMap

在 ES10 中，官方还增加了 ` Array.prototype.flatMap ` 方法，其实就是 ` flat ` 和 ` map ` 一起组合操作：

    
    
    [1,3,5].map(x => [x * x]); // [[1],[9],[25]]
    
    [1,3,5].flatMap(x => [x * x]); // [1,9,25]

##  参考文章：

1\. [ ES2019 新特性简介 ]()  
2\. [ ES2019 新特性简介 ]()

Author  |  王平安   
---|---  
E-mail  |  pingan8787@qq.com   
博 客  |  www.pingan8787.com   
微 信  |  pingan8787   
每日文章推荐  |  [ https://github.com/pingan8787... ]()  
ES小册  |  js.pingan8787.com   
  
##  微信公众号

