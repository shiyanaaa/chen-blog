---
date: 2023-11-01
category:
    - javascript
tag:
    - javascript
---
 # [译]正确使用 sort() 方法
> 英文原文： [ 《Usar correctamente el método sort()》 ]()  
>  注意：内容有做精简和调整。

在过去的几个星期里，我们在不同的团队中看到，一般来说都没有使用 ` Array.prototype.sort() `
的习惯，并且不知道这种方法是如何工作的。今天我们将尝试简要描述它是如何工作的 ` .sort() ` ，揭示它的一些秘密。

###  1\. 修改原数组

在这种情况下，我们必须记住，此方法通过 **对数组进行排序来修改数组** ， **返回相同的有序数组，但不返回新数组**
。如果我们想要保持数组不可变并获得另一个排序，这一点很重要，我们必须在排序之前制作数组的拷贝。

###  2\. 字符串在 Unicode 代码中的位置比较

默认情况下， ` .sort() ` 方法会根据 ` Unicode ` 代码中 **每个字母的位置**
将数组值排序为字符串，因此您可以对此数组进行排序而不会出现问题：

    
    
    console.log(["Zaragoza", "Madrid", "Barcelona"].sort());
    // [ 'Barcelona', 'Madrid', 'Zaragoza' ]

这似乎是正确的，但是如果和一些名称 **以小写字母开头** ，那么排序似乎不正确：

    
    
    console.log(["Zaragoza", "madrid", "Barcelona"].sort());
    // [ 'Barcelona', 'Zaragoza', 'madrid' ]

在这种情况下，排序是在 Unicode 代码表中的每个字母的位置之后完成的，并且 ` m ` 落后 ` Z ` ，因此它已经以这种方式排序。

如果我们想对 **数字排序** ，事情就会变得复杂起来:

    
    
    console.log([80, 9, 100].sort());
    // [ 100, 80, 9 ]

结果似乎很荒谬，但这是有道理的，发生的事情是 **数字已被转换为字符串** ，因此被比较的是字符串 ` "100" ` ， ` "80" ` 并且 `
"9" ` 。由于它们在 Unicode 代码中的位置是按顺序的，因此排序是正确的，即使它不是我们最初的预期。

这些情况的产生导致一些人放弃使用 ` .sort() ` 产生混乱的行为。这有点草率，因为只需一点帮助，这种方法可以毫无问题地运行。

###  3\. Sort() 方法参数

该 ` .sort() ` 有 **一个可选参数** ， **允许此方法帮助对内容进行排序** 。这是此方法的关键，因为我们对每种情况都感兴趣。

此函数接收 **两个要比较的值** ，因此也会有这么三种情况：

  * 如果第一个值大于第二个值，则返回 **正值** ( ` 1 ` ); 
  * 如果第一个值小于第二个值，则返回 **负值** ( ` -1) ` ; 
  * 如果两个值相等或等效于排序，则返回 **零值** ( ` 0 ` ); 

这个函数由 ` Javascript ` 调用，只要您需要对数组中的元素进行排序，我们就可以进行必要的 **比较和**
调整。例如，为了比较数字，我们可以使用类似方法：

    
    
    console.log([80, 9, 100].sort((a, b) => a - b));
    // [ 9, 80, 100 ]

另外， ` (a, b) => a – b ` 还可以这么使用：使用其中一个值 ` a ` 去判断是否大于另一个值 ` b ` 来返回排序结果：

    
    
    const data = [ "Zaragoza", "madrid", "Barcelona" ];
    data.sort ((a, b) => a.toLowerCase () > b.toLowerCase ());
    console.log (data);
    // [ 'Zaragoza', 'madrid', 'Barcelona' ]

显然结果不正确，因为我们草率的将函数比较的结果 ` true ` 或者 ` false ` 返回，我们必须记住支持 **函数` .sort() `
希望我们返回 ` -1 ` ， ` 1 ` 或者 ` 0 ` ** 。为了使它正常运行，我们必须做修改：

    
    
    const data = [ "Zaragoza", "madrid", "Barcelona" ];
    data.sort ((a, b) =>
      a.toLowerCase() > b.toLowerCase() ? 1 :
      a.toLowerCase() < b.toLowerCase() ? -1:
      0
    );
    console.log (data);
    // [ 'Barcelona', 'madrid', 'Zaragoza' ]

**现在的结果是我们需要的** ，因为我们已经对小写和大写也进行了比较，并且我们已经返回 ` -1 ` ， ` 1 ` 或者 ` 0 ` 根据每种情况。

我们还没有真正完成，因为如果我们 **加入一些重音字母** ，我们会得到一个不希望的结果：

    
    
    const data = [ "Zaragoza", "madrid", "Barcelona", "Ávila" ];
    
    data.sort ((a, b) =>
      a.toLowerCase() > b.toLowerCase() ? 1 :
      a.toLowerCase() < b.toLowerCase() ? -1:
      0
    );
    console.log (data);
    // [ 'Barcelona', 'madrid', 'Zaragoza', 'Ávila' ]

当我们想对文本字符串进行排序，就非常有必要使用 ` .localeCompare() ` 方法，也是非常重要。

###  4\. 用对象属性排序数组

通常，如果数组包含对象，我们可以使用对象的属性进行比较，例如：

    
    
    const data = require ('./municipios.json');
    data.sort ((a, b) => a.municipio.localeCompare (b.municipio));

我们可以对数据结构中的日期和任何其他类型的对象执行相同的操作。

###  5\. 关于性能方面

如果我们想对 **非常大的数组** 进行排序，我们必须记住。 ` sort() ` 方法的 **支持函数将被多次调用** ，我们必须
**避免在这个函数中执行许多操作或非常重的操作** 。我们必须尽可能有效地进行比较。

例如，在非常大的数组中，可以使用新的方法 ` Int.Collate().compare ` 来获得更有效的排序函数，而不是使用 `
.localecompare() ` 。 ` Int ` 对象是名为 ` International API ` ，也是 ` ECMA-402 `
的标准的一部分，

该标准侧重于 **国际化功能** ，包括 **每种语言的正确排序** 。 ` Int ` 在浏览器和节点中以全局对象的形式呈现，并具有广泛的支持(包括
**IE11** )。

    
    
    const data    = [ "Zaragoza", "Ávila", "madrid", "Barcelona" ];
    const compare = new Intl.Collator ().compare;
    data.sort (compare);
    console.log (data);
    // [ 'Ávila', 'Barcelona', 'madrid', 'Zaragoza' ]

排序操作很复杂，性能也很差，因此对于非常大的数组，排序方法支持函数速度的任何改进都将对性能产生非常显著的影响。

###  6\. 总结

一般来说，我们应该利用 ` .sort() ` 功能和一个支持函数来控制排序应该如何执行：

  * 数字： ` (a, b) => a – b `
  * 链式： ` (a, b) => a.localeCompare(b) `

在没有函数参数的情况下使用 ` .sort() ` 是没有意义的，也许在少数情况下是这样，但是如果我们用一个 **简单的函数** 支持它，那么 `
.sort ` 是一个非常有用的工具。

**在许多情况下，排序是一个基本的操作，我们不应该放弃在Javascript中进行这种排序。**

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

