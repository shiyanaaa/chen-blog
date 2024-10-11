---
date: 2023-10-14
category:
    - javascript
tag:
    - javascript
---
 # 【重温基础】JS中的常用高阶函数介绍
Ps. 晚上加班到快十点，回来赶紧整理整理这篇文章，今天老大给我推荐了一篇文章， [ 我从写技术博客中收获到了什么？- J_Knight_ ]()
，感受也是很多，自己也需要慢慢养成记录博客的习惯，即使起步艰难，难以坚持，但还是要让自己加油加油。  
前两天把我整理的 [ 【复习资料】ES6/ES7/ES8/ES9资料整理(个人整理) ]() 要分享给大家啦。

正文内容开始：

##  1.介绍

个人简单理解为，一个函数可以接收其他函数作为参数，这种函数便称为 **高阶函数** ，而主要目的就是为了能接收其他函数作为参数。

> Q： 为什么可以接收一个函数作为参数？  
>  A： 因为函数可以接收变量作为参数，而变量可以声明一个方法。

**简单实例：**

    
    
    function a (x){
        return 'hi ' + x;
    }
    function f (a, b){
        return a(b);
    }
    f(a, 'leo');   // "hi leo"

**这段代码的意思** ：定义方法 ` f ` ，接收两个参数，方法 ` a ` 和变量 ` b ` ，在方法 ` a ` 中返回一段字符串，当执行方法 `
f ` 并传入参数方法 ` a ` 和参数 ` b ` 的时候，返回 ` "hi leo" ` 。

也可以直接调用JS内置方法：

    
    
    let a = 3, b = -2;
    function my_abs (val, fun){
        return fun(val);
    }
    my_abs(a, Math.abs);  // 3
    my_abs(b, Math.abs);  // 2

##  2.常用高阶函数

###  2.1 map()

` map() ` 方法的作用是：接收一个函数作为参数，对数组中每个元素按顺序调用一次传入的函数并返回结果， **不改变原数组，返回一个新数组** 。  
通常使用方式： ` arr.map(callback()) ` ，更多详细介绍可以参考 [ MDN Array.map() ]() 。  
**参数** ：

  * ` arr ` : 需要操作的数组； 
  * ` callback(currentValue, index, array, thisArg) ` : 处理的方法，四个参数； 

    *       1. ` currentValue ` 当前处理的元素的 **值**
    *       1. ` index ` 当前处理的元素的 **索引** ，可选 
    *       1. ` array ` 调用 ` map() ` 方法的 **数组** ，可选 
    *       1. ` currentVthisArgalue ` 执行 ` callback ` 函数时使用的 ` this ` 值，可选 

**返回值** ：  
返回一个处理后的新数组。

**实例** ：

    
    
    let arr = [1, 3, -5];
    let a1 = arr.map(Math.abs);  
    // a1 => [1, 3, 5];
    
    let a2 = arr.map(String);
    // a2 => ["1", "3", "-5"]
    
    let a3 = arr.map(function (x){
        return x + 1;
    })
    // 等价于 a3=arr.map(x => x+1)
    // a3 => [2, 4, -4]

对比 ` for...in ` 循环， ` map() ` 书写起来更加简洁：

    
    
    let arr = [1, 3, -5];
    let a1 = [];
    for (var i=0; i<arr.length; i++){
        a1.push(arr[i] + 1); 
    }
    // a1 => [2, 4, -4]

` map() ` 作为高阶函数，事实上它把运算规则抽象了。

###  2.2 reduce()

` reduce() ` 方法的作用是：接收一个函数，对数组进行累加操作，把累计结果和下一个值进行操作，最后返回最终的单个结果值。

通常使用方式： ` arr.reduce(callback(), initValue) ` ，更多详细介绍可以参考 [ MDN Array.reduce()
]()

**参数** ：

  * ` callback(returnValue, currentValue, currentIndex, array) ` : 累记器的方法，四个参数： 

    *       1. ` returnValue ` 上一次处理的返回值，或者初始值 
    *       1. ` currentValue ` 当前处理的元素的 **值** ，可选 
    *       1. ` currentIndex ` 当前处理的元素的 **索引** ，可选 
    *       1. ` array ` 调用 ` reduce() ` 方法的 **数组** ，可选 
  * ` initValue ` 初次调用 ` callback() ` 时候 ` returnValue ` 参数的初始值，默认数组第一个元素，可选 

**返回值** ：  
返回一个最终的累计值。

**实例** ：

  1. 数组求和 

    
    
    let arr = [1, 3, -5];
    let sum1 = arr.reduce((res, cur) => res + cur);
    // sum1 => -1
    
    let sum2 = arr.reduce((res, cur) => res + cur , 1);
    // sum1 => 0

  1. 二维数组转化为一维 

    
    
    let arr = [[1, 2], [3, 4], [5, 6]];
    let con = arr.reduce((res, cur) => res.concat(cur));
    // con => [1, 2, 3, 4, 5, 6]

###  2.3 filter()

` filter() ` 方法的作用是：接收一个函数，依次作用数组每个元素，并过滤符合函数条件的元素，将剩下的数组作为一个新数组返回。

通常使用方式： ` arr.filter(callback(), thisArg) ` ，更多详细介绍可以参考 [ MDN Array.filter()
]()

**参数** ：

  * ` callback(ele, index, array) ` : 过滤条件的方法，当返回 ` true ` 则保存该元素，反之不保留，三个参数： 

    *       1. ` ele ` 当前处理的元素 
    *       1. ` index ` 当前处理的元素的 **索引** ，可选 
    *       1. ` array ` 调用 ` filter() ` 方法的 **数组** ，可选 
  * ` thisArg ` 执行 ` callback ` 时的用于 ` this ` 的值，可选 

**返回值** ：  
返回一个过滤剩下的元素组成的新数组。

**实例** ：

  1. 过滤奇数值 

    
    
    let arr = [1, 2, 3, 4, 5, 6];
    let res = arr.filter(x => x % 2 != 0);
    // res => [1, 3, 5]

  1. 过滤不满足条件的值 

    
    
    let arr = [1, 2, 3, 4, 5, 6];
    let res = arr.filter(x => x > 3);
    // res => [4, 5, 6]

  1. 过滤空字符串 

    
    
    let arr = ['a', '', null, undefined, 'b', ''];
    let tri = arr.filter(x => x && x.trim());
    // tri => ["a", "b"]

总结下： ` filter() ` 主要作为 **筛选功能** ，因此核心就是正确实现一个“筛选”函数。

###  2.4 sort()

` sort() ` 方法的作用是：接收一个函数，对数组的元素进行排序，并返回排序后的新数组。 **默认排序顺序是根据字符串Unicode码点** 。

通常使用方式： ` arr.sort(fun()) ` ，更多详细介绍可以参考 [ MDN Array.sort() ]()  
compareFunction 可选  
用来指定按某种顺序进行排列的函数。如果省略，元素按照转换为的字符串的各个字符的Unicode位点进行排序。  
**参数** ：

  * ` fun(a, b) ` : 指定按某种顺序进行排列的函数，若省略则按照转换为的字符串的各个字符的Unicode位点进行排序，两个可选参数： 

` fun() ` 返回 ` a ` 和 ` b ` 两个值的大小的比较结果， ` sort() ` 根据返回结果进行排序：

  * 若 ` fun(a, b) ` 小于 0 ，则 ` a ` 排在 ` b ` 前面； 
  * 若 ` fun(a, b) ` 等于 0 ，则 ` a ` ` b ` 位置不变； 
  * 若 ` fun(a, b) ` 大于 0 ，则 ` a ` 排在 ` b ` 后面； 

**返回值** ：  
返回排序后的新数组，并 **修改原数组** 。

**实例** ：

  1. 升序降序数组 

    
    
    let arr = [1,5,2,3];
    let sort1 = arr.sort();
    // 等同于 let sort1 = arr.sort((a, b) => a - b);
    // sort1 => [1, 2, 3, 5]
    
    let sort2 = arr.sort((a, b) => b - a);
    // sort2 => [5, 3, 2, 1]

  1. 字符串排序 

    
    
    let arr1 = ['AA', 'CC', 'BB'];
    let sort1 = arr1.sort();
    // sort1 => ["AA", "BB", "CC"]
    
    let arr2 = ['AA', 'aa', 'BB'];
    let sort2 = arr2.sort();
    // sort2 => ["AA", "BB", "aa"]
    
    let arr3 = ['AA', 'aa', 'BB'];
    let sort3 = arr3.sort((a, b) => a.toLowerCase() > b.toLowerCase());
    // sort3 => ["AA", "aa", "BB"]
    // 也可以写成：
    let sort3 = arr3.sort((a, b) => {
        let s1 = a.toLowerCase();
        let s2 = b.toLowerCase();
        return s1 > s2 ? 1 : s1 < s2 ? -1 : 0;
    })

总结下： ` sort() ` 主要作为 **排序功能** ，因此核心就是正确实现一个“排序”函数。

##  3\. 参考文章

  * [ 阮一峰 JS高阶函数 ]()

分享的内容比较简单，但是还是希望能帮助到需要的人哈。~~感谢

Author  |  王平安   
---|---  
E-mail  |  pingan8787@qq.com   
博 客  |  www.pingan8787.com   
微 信  |  pingan8787   
每日文章推荐  |  [ https://github.com/pingan8787... ]()  
ES小册  |  es.pingan8787.com   
  
欢迎关注微信公众号【前端自习课】每天早晨，与您一起学习一篇优秀的前端技术博文 .

