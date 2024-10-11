---
date: 2024-06-25
category:
    - javascript
tag:
    - javascript
---
 # JS常用方法函数
##  JS常用方法函数

  1. [ 字符串长度截取 ]()
  2. [ 惰性求值 ]()
  3. [ 闭包 ]()
  4. [ 基本包装类型(包装对象) ]()
  5. [ 对象遍历（最佳方法） ]()
  6. [ 数组遍历（内置方法） ]()
  7. [ 怎么判断一个object是否是数组(array)？ ]()
  8. [ 加法操作表 ]()
  9. [ 排序方法 ]()
  10. [ 前缀规范 ]()
  11. [ 道格拉斯的object方法（等同于object.create方法） ]()

###  1\. 字符串长度截取

    
    
    function cutstr(str, len) {
        var temp,
            icount = 0,
            patrn = /[^\x00-\xff]/,
            strre = "";
    
        for (var i = 0; i < str.length; i++) {
            if (icount < len - 1) {
                temp = str.substr(i, 1);
                if (patrn.exec(temp) === null) {
                    icount += 1;
                } else {
                    icount += 2;
                }
                strre += temp;
            } else {
                break;
            }
        }
        return strre + "...";
    }

###  2\. 惰性求值

    
    
    const range = function* (from, to) {
        for (let i = from; i < to; i++) {
            console.log('range\t', i);
            yield i;
        }
    };
    
    const map = function* (flow, transform) {
        for (const data of flow) {
            console.log('map\t', data);
            yield (transform(data));
        }
    };
    
    const filter = function* (flow, condition) {
        for (const data of flow) {
            console.log('filter\t', data);
            if (condition(data)) {
                yield data;
            }
        }
    };
    
    const stop = function* (flow, condition) {
        for (const data of flow) {
            yield data;
            if (condition(data)) {
                break;
            }
        }
    };
    
    const take = function (flow, num) {
        let count = 0;
        const _filter = function (data) {
            count++;
            return count >= num;
        };
        return stop(flow, _filter);
    };
    
    class _Lazy {
        constructor() {
            this.iterator = null;
        }
    
        range(...args) {
            this.iterator = range(...args);
            return this;
        }
    
        map(...args) {
            this.iterator = map(this.iterator, ...args);
            return this;
        }
    
        filter(...args) {
            this.iterator = filter(this.iterator, ...args);
            return this;
        }
    
        take(...args) {
            this.iterator = take(this.iterator, ...args);
            return this;
        }
    
        [Symbol.iterator]() {
            return this.iterator;
        }
    }
    
    function lazy() {
        return new _Lazy();
    }
    
    const nums = lazy().range(0, 100).map(n => n * 10).filter(n => n % 3 === 0).take(2);
    for (let n of nums) {
        console.log('num:\t', n, '\n');
    }

###  3\. 闭包

    
    
    const Greeters = [];
    
    //方法一
    for (let i = 0; i < 10; i++) {
        Greeters.push(function () {
            return console.log(i);
        })
    }
    //方法二
    for (var i = 0; i < 10; i++) {
        Greeters.push(console.log.bind(null, i))
    }
    Greeters[0]();//0
    Greeters[1]();//1
    Greeters[2]();//2

###  4\. 惰性求值

    
    
    var s1 = "hello world";
    var s2 = s1.substr(4);

` ECMAScript ` 还提供了三个特殊的引用类型 ` Boolean ` ， ` String ` ， ` Number `
。我们称这三个特殊的引用类型为基本包装类型，也叫包装对象。

也就是说当读取 ` string ` ， ` boolean ` 和 ` number `
这三个基本数据类型的时候，后台就会创建一个对应的基本包装类型对象，从而让我们能够调用一些方法来操作这些数据。

所以当第二行代码访问 ` s1 ` 的时候，后台会自动完成下列操作：

  1. 创建 ` String ` 类型的一个实例；// ` var s1 = new String(“helloworld”); `
  2. 在实例上调用指定方法；// ` var s2 = s1.substr(4); `
  3. 销毁这个实例；// ` s1 = null; `

正因为有第三步这个销毁的动作，所以你应该能够明白为什么基本数据类型不可以添加属性和方法，这也正是基本装包类型和引用类型主要区别： **对象的生存期** 。

使用 ` new `
操作符创建的引用类型的实例，在执行流离开当前作用域之前都是一直保存在内存中。而自动创建的基本包装类型的对象，则只存在于一行代码的执行瞬间，然后立即被销毁。

###  5\. 对象遍历（最佳方法）

    
    
    //为 Object 设置三个自定义属性（可枚举）
    Object.prototype.userProp = 'userProp';
    Object.prototype.getUserProp = function () {
        return Object.prototype.userProp;
    };
    
    //定义一个对象，隐式地继承自 Object.prototype
    var obj = {
        name: 'percy',
        age: 21,
        [Symbol('symbol 属性')]: 'symbolProp',
        unEnumerable: '我是一个不可枚举属性',
        skills: ['html', 'css', 'js'],
        getSkills: function () {
            return this.skills;
        }
    };
    
    //设置 unEnumerable 属性为不可枚举属性
    Object.defineProperty(obj, 'unEnumerable', {
        enumerable: false
    });
    
    //利用 Object.create() 新建一个对象，并且这个对象没有任何原型链
    var obj2 = Object.create(null, {
        name: {value: 'percy'},
        age: {value: 21},
        skills: {value: ['html', 'css', 'js']}
    });
    /*
    * 针对上面的情况，我们用一个更完善的解决方案来解决。
    * 使用 Object.prototype.hasOwnProperty.call(obj,’prop’…)
    * */
    Object.prototype.hasOwnProperty.call(obj2, 'name');//true
    Object.prototype.hasOwnProperty.call(obj2, 'skills');//true
    Object.prototype.hasOwnProperty.call(obj2, 'userProp');//false

###  6\. 数组遍历（内置方法）

> **Array.prototype.forEach()** ： 对数组的每个元素执行一次提供的函数
    
    
    //如果数组在迭代时被修改了，则按照索引继续遍历修改后的数组
    var words = ["one", "two", "three", "four"];
    words.forEach(function (word) {
        console.log(word);
        if (word === 'two') {
            words.shift();
        }
    });

> **Array.prototype.map()** ： 返回一个新数组，每个元素都是回调函数返回的值
    
    
    // map 的一个坑
    [1,2,3].map(parseInt);//[1, NaN, NaN]

**一些有用的数组内置方法**

  * **Array.prototype.every(callback[,thisArg])** ： 测试数组的各个元素是否通过了回调函数的测试，若都通过，返回 ` true ` ，否则返回 ` false ` （说得本质点儿，就是如果回调函数每次返回的值都是 ` true ` 的话，则 ` every() ` 返回 ` true ` ，否则为 ` false ` ） 
  * **Array.prototype.filter(callback[,thisArg])** ： 返回一个新数组，数组的元素是原数组中通过测试的元素（就是回调函数返回 ` true ` 的话，对应的元素会进入新数组） 
  * **Array.prototype.find(callback[,thisArg])** ： 返回第一个通过测试的元素 
  * **Array.prototype.findIndex(callback[,thisArg])** ： 与上面函数类似，只不过这个是返回索引 
  * **Array.prototype.some(callback[,thisArg])** ： 类似 ` find() ` ，只不过它不返回元素，只返回一个 **布尔值** 。只要找到一个通过测试的，就返回 ` true `
  * **Array.prototype.reduce(callback,[initialValue])** ： 习惯性称之为 **累加器函数** ，对数组的每个元素 **执行回调函数** ，最后返回一个值（这个值是最后一次调用回调函数时返回的值） 

**这个函数的回调函数有 4 个参数**

  1. ` accumulator ` ： 上一次调用回调函数返回的值 
  2. ` currentValue ` ： 当前在处理的值 
  3. ` currentIndex `
  4. ` array `

` initialValue ` ： 可选项，其值用于第一次调用 ` callback ` 的第一个参数

  * **Array.prototype.reduceRight(callback[, initialValue])** ： 用法和上面的函数一样，只不过遍历方向正好相反 

> **总结一下上面这些函数的共性**
>
>   * 都是通过每次的回调函数的返回值进行逻辑操作或判断的
>   * 回调函数都可以写成更简洁的箭头函数（推荐）
>   * 都可以通过形如 **Array.prototype.map.call(str,callback)** 的方式来操作字符串
>

###  7\. 怎么判断一个object是否是数组(array)

> **方法一：** 使用 ` Object.prototype.toString ` 来判断是否是数组
    
    
    function isArray(obj) {
        return Object.prototype.toString.call(obj) === '[object Array]';
    }

这里使用 ` call ` 来使 ` toString ` 中 ` this ` 指向 ` obj ` ，进而完成判断。

> **方法二：** 使用 **原型链** 来完成判断
    
    
    function isArray(obj) {
        return obj.__proto__ === Array.prototype;
    }

基本思想是利用实例如果是某个构造函数构造出来的，那么它的 ` __proto__ ` 是指向构造函数的 ` prototype ` 属性。

> **方法三：** 利用 ` JQuery `
    
    
    function isArray(obj){
        return $.isArray(obj)
    }

` JQuery isArray ` 的实现其实就是方法一。

###  8\. 加法操作表

  * Number + Number -> 加法 
  * Boolean + Number -> 加法 
  * Boolean + Boolean -> 加法 
  * Number + String -> 连接 
  * String + Boolean -> 连接 
  * String + String -> 连接 

###  9\. 排序方法

**冒泡排序**

    
    
    function bubbleSort(arr) {
        var len = arr.length;
        for (var i = 0; i < len - 1; i++) {
            for (var j = 0; j < len - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    var temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        return arr;
    }

**选择排序**

  1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置 
  2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾 
  3. 重复第二步，直到所有元素均排序完毕 

    
    
    function selectionSort(arr) {
        var len = arr.length,
            minIndex, temp;
    
        for (var i = 0; i < len - 1; i++) {
            minIndex = i;
            for (var j = i + 1; j < len; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
        return arr;
    }

**插入排序**

  1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置 
  2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。） 

    
    
    function insertionSort(arr) {
        var len = arr.length,
            preIndex, current;
    
        for (var i = 1; i < len; i++) {
            preIndex = i - 1;
            current = arr[i];
            while (preIndex >= 0 && arr[preIndex] > current) {
                arr[preIndex + 1] = arr[preIndex];
                preIndex--;
            }
            arr[preIndex + 1] = current;
        }
        return arr;
    }

**归并排序**

基本原理是分治法，就是分开并且递归来排序。

  1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列； 
  2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置； 
  3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置； 
  4. 重复步骤 3 直到某一指针达到序列尾； 
  5. 将另一序列剩下的所有元素直接复制到合并序列尾。 

    
    
    function insertionSort(arr) {
        var len = arr.length,
            preIndex, current;
    
        for (var i = 1; i < len; i++) {
            preIndex = i - 1;
            current = arr[i];
            while (preIndex >= 0 && arr[preIndex] > current) {
                arr[preIndex + 1] = arr[preIndex];
                preIndex--;
            }
            arr[preIndex + 1] = current;
        }
        return arr;
    }

###  10\. 前缀规范

每个局部变量都需要有一个类型前缀，按照类型可以分为：

> s：表示字符串。例如：sName，sHtml；  
>  n：表示数字。例如：nPage，nTotal；  
>  b：表示逻辑。例如：bChecked，bHasLogin；  
>  a：表示数组。例如：aList，aGroup；  
>  r：表示正则表达式。例如：rDomain，rEmail；  
>  f：表示函数。例如：fGetHtml，fInit；  
>  o：表示以上未涉及到的其他对象，例如：oButton，oDate；  
>  g：表示全局变量，例如：gUserName，gLoginTime；

###  11\. 道格拉斯的object方法（等同于object.create方法）

    
    
    function object(o) {
        var F = function () {
        };
        F.prototype = o;
        return new F();
    }

