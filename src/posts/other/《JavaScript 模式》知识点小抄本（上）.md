---
date: 2024-07-01
category:
    - javascript
tag:
    - javascript
---
 # 《JavaScript 模式》知识点小抄本（上）
##  介绍

最近开始给自己每周订个学习任务，学习结果反馈为一篇文章的输出，做好学习记录。  
这一周(02.25-03.03)我定的目标是 [ 《JavaScript 模式》 ]() 的第七章学习一遍，学习结果的反馈就是本篇文章啦。  
由于内容实在太长，我将本文分为两部分：

  * **《JavaScript 模式》知识点整理（上）**
  * **[ 《JavaScript 模式》知识点整理（下） ]() **

本文内容中主要参考《JavaScript 模式》，其中也有些案例是来自网上资料，有备注出处啦，如造成不便，请联系我删改。

过两天我会把这篇文章收录到我整理的知识库 [ 【Cute-JavaScript】 ]() 中，并已经同步到 [ 【github】 ]() 上面。

##  一、单体模式(Singleton Pattern)

###  1.概念介绍

**单体模式(Singleton Pattern)** 的思想在于 **保证一个特定类仅有一个实例** ，即不管使用这个类创建多少个新对象，都会得到
**与第一次创建的对象完全相同** 。

它让我们能将代码组织成一个逻辑单元，并可以通过单一变量进行访问。

单体模式有以下优点：

  * 用来划分命名空间，减少全局变量数量。 
  * 使代码组织的更一致，提高代码阅读性和维护性。 
  * 只能被实例化一次。 

但在JavaScript中没有类，只有对象。当我们创建一个新对象，它都是个新的单体，因为JavaScript中永远不会有完全相等的对象，除非它们是同一个对象。  
因此， **我们每次使用对象字面量创建对象的时候，实际上就是在创建一个单例** 。

    
    
    let a1 = { name : 'leo' };
    let a2 = { name : 'leo' };
    a1 === a2;  // false
    a1 == a2;   // false

这里需要注意，单体模式有个条件，是该对象能被实例化，比如下面这样就不是单体模式，因为它不能被实例化：

    
    
    let a1 = {
        b1: 1, b2: 2,
        m1: function(){
            return this.b1;
        },
        m2: function(){
            return this.b2;
        }
    }
    new a1();  // Uncaught TypeError: a1 is not a constructor

下面展示一个单体模式的基本结构：

    
    
    let Singleton = function (name){
        this.name = name;
        this.obj = null;
    }
    Singleton.prototype.getName = function(){
        return this.name;
    }
    function getObj(name){
        return this.obj || (this.obj = new Singleton(name));
    }
    let g1 = getObj('leo');
    let g2 = getObj('pingan');
    g1 === g2;    // true
    g1 == g2;     // true
    g1.getName(); // 'leo'
    g2.getName(); // 'leo'

从这里可以看出，单体模式只能实例化一次，后面再调用的话，都是使用第一次实例化的结果。

###  2.应用场景

单例模式只允许实例化一次，能提高对象访问速度并且节约内存，通常被用于下面场景：

  * 需要频繁创建再销毁的对象，或频繁使用的对象：如：弹窗，文件； 
  * 常用的工具类对象； 
  * 常用的资源消耗大的对象； 

###  3.实现弹框案例

这里我们要用单体模式，创建一个弹框，大概需要实现：元素值创建一次，使用的时候直接调用。  
因此我们这么做：

    
    
    let create = (() => {
        let div;
        return () => {
            if(!div){
                div = document.createElement('div');
                div.innderHTML = '我是leo创建的弹框';
                div.style.display = 'none';
                div.setAttribute("id", "leo");
                document.body.appendChild(div);
            }
            return div;
        }
    })();
    // 触发事件
    document.getElementById('otherBtn').onclick = () => {
        let first = create();
        first.style.display = 'block';
    }

###  4.使用new操作符

由于JavaScript中没有类，但JavaScript有 ` new ` 语法来用构造函数创建对象，并可以使用这种方法实现单体模式。  
当使用同一个构造函数以 ` new ` 操作符创建多个对象，获得的是指向完全相同的对象的新指针。

通常我们使用 ` new ` 操作符创建单体模式的三种选择，让构造函数总返回最初的对象：

  * 使用全局对象来存储该实例（不推荐，容易全局污染）。 
  * 使用静态属性存储该实例，无法保证该静态属性的私有性。 

    
    
    function Leo(name){
        if(typeof Leo.obj === 'object'){
            return Leo.obj;
        }
        this.name = name;
        Leo.obj = this;
        return this;
    }
    let a1 = new Leo('leo');
    let a2 = new Leo('pingan');
    a1 === a2 ; // true
    a1 ==  a2 ; // true

唯一的缺点就是 ` obj ` 属性是公开的，容易被修改。

  * 使用闭包将该实例包裹，保证实例是私有性并不会被外界修改。 

我们这通过重写上面的方法，加入闭包：

    
    
    function Leo(name){
        let obj;
        this.name = name;
        obj = this;       // 1.存储第一次创建的对象
        Leo = function(){ // 2.修改原来的构造函数
            return obj;
        }
    }
    let a1 = new Leo('leo');
    let a2 = new Leo('pingan');
    a1 === a2 ; // true
    a1 ==  a2 ; // true

当我们第一次调用构造函数，像往常一样返回this，而后面再调用的话，都将重写构造函数，并访问私有变量 ` obj ` 并返回。

##  二、工厂模式(Factory Pattern)

###  1.概念介绍

**工厂模式** 的目的在于创建对象，实现下列目标：

  * 可重复执行，来创建相似对象； 
  * 当编译时位置具体类型（类）时，为调用者提供一种创建对象的接口； 

通过工厂方法（或类）创建的对象，都继承父对象，下面一个简单工厂方法理解：

    
    
    function Person(name, age, sex){
        let p = {}; // 或 let p = new Object(); 创建一个初始对象
        p.name = name;
        p.age = age;
        p.sex = sex;
        p.ask = function(){
            return 'my name is' + this.name;
        }
        return p;
    }
    let leo = new Person('leo', 18, 'boy');
    let pingan = new Person('pingan', 18, 'boy');
    console.log(leo.name, leo.age, leo.sex);          // 'leo', 18, 'boy'
    console.log(pingan.name, pingan.age, pingan.sex); // 'pingan', 18, 'boy'

通过调用 ` Person ` 构造函数，我们可以像工厂那样，生产出无数个包含三个属性和一个方法的对象。  
可以看出， **工厂模式** 可以解决创建多个类似对象的问题。

###  2.优缺点

####  2.1优点

  * 一个调用者想创建一个对象，只要知道其名称就可以了。 
  * 扩展性高，如果想增加一个产品，只要扩展一个工厂类就可以。 
  * 屏蔽产品的具体实现，调用者只关心产品的接口。 

####  2.2缺点

每次增加一个产品时，都需要增加一个具体类和对象实现工厂，使得系统中类的个数成倍增加，在一定程度上增加了系统的复杂度，同时也增加了系统具体类的依赖。这并不是什么好事。

###  3.实现复杂工厂模式

在复杂工厂模式中，我们将其成员对象的实列化推迟到子类中，子类可以重写父类接口方法以便创建的时候指定自己的对象类型。  
父类类似一个公共函数，只处理创建过程中的问题，并且这些处理将被子类继承，然后在子类实现专门功能。

比如这里我们需要实现这么一个实例：

  * 需要一个公共父函数 ` CarMaker ` ； 
  * 父函数 ` CarMaker ` 有个 ` factor ` 静态方法，用于创建 ` car ` 对象； 
  * 定义三个静态属性，值为三个函数，用于继承父函数 ` CarMaker ` ； 

然后我们希望这么使用这个函数：

    
    
    let c1 = CarMaker.factory('Car1');
    let c2 = CarMaker.factory('Car2');
    let c3 = CarMaker.factory('Car3');
    c1.drirve();  // '我的编号是6'
    c2.drirve();  // '我的编号是3'
    c3.drirve();  // '我的编号是12'

可以看出，调用时接收以字符串形式指定类型，并返回请求类型的对象，并且这样使用是不需要用 ` new ` 操作符。

下面看代码实现：

    
    
    // 创建父构造函数
    function CarMaker(){};
    CarMaker.prototype.drive = function(){
        return `我的编号是${this.id}`;
    }
    // 添加静态工厂方法
    CarMaker.factory = function (type){
        let types = type, newcar;
        // 若构造函数不存在 则发生错误
        if(typeof CarMaker[types] !== 'function'){
            throw{ name: 'Error', message: `${types}不存在`};
        }
        // 若构造函数存在，则让原型继承父类，但仅继承一次
        if(CarMaker[types].prototype.drive !== 'function'){
            CarMaker[types].prototype = new CarMaker();
        }
        // 创建新实例，并返回
        newcar = new CarMaker[types]();
        return newcar;
    }
    // 调用
    CarMaker.c1 = function(){
        this.id = 6;
    }
    CarMaker.c2 = function(){
        this.id = 3;
    }
    CarMaker.c3 = function(){
        this.id = 12;
    }

定义完成后，我们再执行前面的代码：

    
    
    let c1 = CarMaker.factory('Car1');
    let c2 = CarMaker.factory('Car2');
    let c3 = CarMaker.factory('Car3');
    c1.drirve();  // '我的编号是6'
    c2.drirve();  // '我的编号是3'
    c3.drirve();  // '我的编号是12'

就能正常打印结果了。

实现该工厂模式并不困难，主要是要找到能够穿件所需类型对象的构造函数。  
这里使用简单的映射来创建该对象的构造函数。

###  4.内置对象工厂

内置的对象工厂，就像全局的 ` Object() ` 构造函数，也是工厂模式的行为，根据输入类型创建不同对象。  
如传入一个原始数字，返回一个 ` Number() ` 构造函数创建一个对象，传入一个字符串或布尔值也成立。  
对于传入任何其他值，包括无输入的值，都会创建一个常规的对象。

无论是否使用 ` new ` 操作符，都可以调用 ` Object() ` ，我们这么测试：

    
    
    let a = new Object(), b = new Object(1),
        c = Object('1'),  d = Object(true);
    
    a.constructor === Object;  // true 
    b.constructor === Number;  // true 
    c.constructor === String;  // true 
    d.constructor === Boolean; // true 

事实上， ` Object() ` 用途不大，这里列出来是因为它是我们比较常见的工厂模式。

##  三、迭代器模式(Iterator Pattern)

###  1.概念介绍

**迭代器模式(Iterator Pattern)** 是提供一种方法，顺序访问一个聚合对象中每个元素，并且不暴露该对象内部。

这种模式属于行为型模式，有以下几个特点：

  * 访问一个聚合对象的内容，而无需暴露它的内部表示。 
  * 提供统一接口来遍历不同结构的数据集合。 
  * 遍历的同事更改迭代器所在的集合结构可能会导致问题。 

在迭代器模式中，通常包含有一个包含某种数据集合的对象，需要提供一种简单的方法来访问每个元素。  
这里对象需要提供一个 ` next() ` 方法，每次调用都必须返回下一个连续的元素。

这里假设创建一个对象 ` leo ` ，我们通过调用它的 ` next() ` 方法访问下一个连续的元素：

    
    
    let obj;
    while(obj = leo.next()){
        // do something
        console.log(obj);
    }

另外迭代器模式中，聚合对象还会提供一个更为渐变的 ` hasNext() ` 方法，来检查是否已经到达数据末尾，我们这么修改前面的代码：

    
    
    while(leo.hasNext()){
        // do something
        console.log(obj);
    }

###  2.优缺点和应用场景

####  2.1优点

  * 它简化了聚合类，并支持以不同的方式遍历一个聚合对象。 
  * 在同一个聚合上可以有多个遍历。 
  * 在迭代器模式中，增加新的聚合类和迭代器类都很方便，无须修改原有代码。 

####  2.2缺点

由于迭代器模式将存储数据和遍历数据的职责分离，增加新的聚合类需要对应增加新的迭代器类，类的个数成对增加，这在一定程度上增加了系统的复杂性。

####  2.3应用场景

  * 访问一个聚合对象的内容而无须暴露它的内部表示。 
  * 需要为聚合对象提供多种遍历方式。 
  * 为遍历不同的聚合结构提供一个统一的接口。 

###  3.简单案例

根据上面的介绍，我们这里实现一个简单案例，将设我们数据只是普通数组，然后每次检索，返回的是间隔一个的数组元素（即不是连续返回）：

    
    
    let leo = (function(){
        let index = 0, data = [1, 2, 3, 4, 5],
            len = data.length;
        return {
            next: function(){
                let obj;
                if(!this.hasNext()){
                    return null;
                };
                obj = data[index];
                index = index + 2;
                return obj;
            },
            hasNext: function(){
                return index < len;
            }
        }
    })()

然后我们还要给它提供更简单的访问方式和多次迭代数据的能力，我们需要添加下面两个方法：

  * ` rewind() ` 重置指针到初始位置； 
  * ` current() ` 返回当前元素，因为当指针步前进时无法使用 ` next() ` 操作； 

代码变成这样：

    
    
    let leo = (function(){
        //.. 
        return {
             // .. 
             rewind: function(){
                 index = 0;
             },
             current: function(){
                 return data[index];
             }
        }
    })();

这样这个案例就完整了，接下来我们来测试：

    
    
    // 读取记录
    while(leo.hasNext()){
        console.log(leo.next());
    };  // 打印 1 3 5
    // 回退
    leo.rewind();
    // 获取当前
    console.log(leo.current()); // 回到初始位置，打印1

###  4.应用场景

迭代器模式通常用于：对于集合内部结果常常变化各异，我们不想暴露其内部结构的话，但又响让客户代码透明底访问其中的元素，这种情况下我们可以使用迭代器模式。

**简单理解：** 遍历一个聚合对象。

  * jQuery应用例子： 

jQuery中的 ` $.each() ` 方法，可以让我们传入一个方法，实现对所有项的迭代操作：

    
    
    $.each([1,2,3,4,5],function(index, value){
        console.log(`${index}: ${value}`)
    })

  * 使用迭代器模式实现 ` each() ` 方法 

    
    
    let myEach = function(arr, callback){
        for(var i = 0; i< arr.length; i++){
            callback(i, arr[i]);
        }
    }

###  4.小结

迭代器模式是一种相对简单的模式，目前绝大多数语言都内置了迭代器。而且迭代器模式也是非常常用，有时候不经意就是用了。

##  四、装饰者模式(Decorator Pattern)

###  1.概念介绍

**装饰者模式（Decorator Pattern）**
：在不改变原类和继承情况下，动态添加功能到对象中，通过包装一个对象实现一个新的具有原对象相同接口的新对象。

装饰者模式有以下特点：

  1. **添加功能时不改变原对象结构** 。 
  2. **装饰对象和原对象提供的接口相同** ，方便按照源对象的接口来使用装饰对象。 
  3. **装饰对象中包含原对象的引用** 。即装饰对象是真正的原对象包装后的对象。 

实际上，装饰着模式的一个比较方便的特征在于其预期行为的可定制和可配置特性。从只有基本功能的普通对象开始，不断增强对象的一些功能，并按照顺序进行装饰。

###  2.优缺点和应用场景

####  2.1优点

  * 装饰类和被装饰类可以独立发展，不会相互耦合，装饰模式是继承的一个替代模式，装饰模式可以动态扩展一个实现类的功能。 

####  2.2缺点

  * 多层装饰比较复杂。 

####  2.3应用场景

  * 扩展一个类的功能。 
  * 动态增加功能，动态撤销。 

###  3.基本案例

我们这里实现一个基本对象 ` sale ` ，可以通过 ` sale ` 对象获取不同项目的价格，并通过调用 ` sale.getPrice() `
方法返回对应价格。并且在不同情况下，用额外的功能来装饰它，会得到不同情况下的价格。

####  3.1创建对象

这里我们假设客户需要支付国家税和省级税。按照装饰者模式，我们就需要使用国家税和省级税两个装饰者来装饰这个 ` sale `
对象，然后在对使用价格格式化功能的装饰者装饰。实际看起来是这样：

    
    
    let sale = new Sale(100);
    sale = sale.decorate('country');
    sale = sale.decorate('privince');
    sale = sale.decorate('money');
    sale.getPrice();

使用装饰者模式后，每个装饰都非常灵活，主要根据其装饰者顺序，于是如果客户不需要上缴国家税，代码就可以这么实现：

    
    
    let sale = new Sale(100);
    sale = sale.decorate('privince');
    sale = sale.decorate('money');
    sale.getPrice();

####  3.2实现对象

接下来我们需要考虑的是如何实现 ` Sale ` 对象了。

**实现装饰者模式的其中一个方法是使得每个装饰者成为一个对象，并且该对象包含了应该被重载的方法**
。每个装饰者实际上继承了目前已经被前一个装饰者进行装饰后的对象，每个装饰方法在 ` uber `
（继承的对象）上调用同样的方法并获取值，此外还继续执行一些操作。

> ` uber ` 关键字类似Java的 ` super ` ，它可以让某个方法调用父类的方法， ` uber ` 属性指向父类原型。

即：当我们调用 ` sale.getPrice() ` 方法时，会调用 ` money `
装饰者的方法，然后每个装饰方法都会先调用父对象的方法，因此一直往上调用，直到开始的 ` Sale ` 构造函数实现的未被装饰的 ` getPrice() `
方法。理解如下图：

我们这里可以先实现构造函数 ` Sale() ` 和原型方法 ` getPrice() ` ：

    
    
    function Sale (price){
        this.price = price || 100;
    }
    Sale.prototype.getPrice = function (){
        return this.price;
    }

并且装饰者对象都将以构造函数的属性来实现：

    
    
    Sale.decorators = {};

接下来实现 ` country ` 这个装饰者并实现它的 ` getPrice() ` ，改方法首先从父对象的方法获取值再做修改：

    
    
    Sale.decorators.country = {
        getPrice: function(){
            let price = this.uber.getPrice(); // 获取父对象的值
            price += price * 5 / 100;
            return price;
        }
    }

按照相同方法，实现其他装饰者：

    
    
    Sale.decorators.privince = {
        getPrice: function(){
            let price = this.uber.getPrice();
            price += price * 7 / 100;
            return price;
        }
    }
    Sale.decorators.money = {
        getPrice: function(){
            return "￥" + this.uber.getPrice().toFixed(2);
        }
    }

最后我们还需要实现前面的 ` decorate() ` 方法，它将我们所有装饰者拼接一起，并且做了下面的事情：  
创建了个新对象 ` newobj ` ，继承目前我们所拥有的对象( ` Sale ` )，无论是原始对象还是最后装饰后的对象，这里就是对象 ` this `
，并设置 ` newobj ` 的 ` uber ` 属性，便于子对象访问父对象，然后将所有装饰者的额外属性复制到 ` newobj ` 中，返回 `
newobj ` ，即成为更新的 ` sale ` 对象：

    
    
    Sale.prototype.decorate = function(decorator){
        let F = function(){}, newobj,
            overrides = this.constructor.decorators[decorator];
        F.prototype = this;
        newobj = new F();
        newobj.user = F.prototype;
        for(let k in overrides){
            if(overrides.hasOwnProperty(k)){
                newobj[k] = overrides[k];
            }
        }
        return newobj;
    }

###  4.改造基本案例

这里我们使用列表实现相同功能，这个方法利用JavaScript语言的动态性质，并且不需要使用继承，也不需要让每个装饰方法调用链中前面的方法，可以简单的将前面方法的结果作为参数传递给下一个方法。

这样实现也有个好处，支持反装饰或撤销装饰，我们还是实现以下功能：

    
    
    let sale = new Sale(100);
    sale = sale.decorate('country');
    sale = sale.decorate('privince');
    sale = sale.decorate('money');
    sale.getPrice();

现在的 ` Sale() ` 构造函数中多了个装饰者列表的属性：

    
    
    function Sale(price){
        this.price = (price > 0) || 100;
        this.decorators_list = [];
    }

然后还是需要实现 ` Sale.decorators ` ，这里的 ` getPrice() ` 将变得更简单，也没有去调用父对象的 `
getPrice() ` ，而是将结果作为参数传递：

    
    
    Sale.decorators = {};
    Sale.decorators.country = {
        getPrice: function(price){
            return price + price * 5 / 100;
        }
    }
    Sale.decorators.privince = {
        getPrice: function(price){
            return price + price * 7 / 100;
        }
    }
    Sale.decorators.money = {
        getPrice: function(price){
            return "￥" + this.uber.getPrice().toFixed(2);
        }
    }

而这时候父对象的 ` decorate() ` 和 ` getPrice() ` 变得复杂， ` decorate() ` 用于追加装饰者列表， `
getPrice() ` 需要完成包括遍历当前添加的装饰者一级调用每个装饰者的 ` getPrice() ` 方法、传递从前一个方法获得的结果：

    
    
    Sale.prototype.decorate = function(decorators){
        this.decorators_list.push(decorators);
    }
    
    Sale.propotype.getPrice = function(){
        let price = this.price, name;
        for(let i = 0 ;i< this.decorators_list.length; i++){
            name = this.decorators_list[i];
            price = Sale.decorators[name].getPrice(price);
        }
        return price;
    }

###  5.对比两个方法

很显然，第二种列表实现方法会更简单，不用设计继承，并且装饰方法也简单。  
案例中 ` getPrice() `
是唯一可以装饰的方法，如果想实现更多可以被装饰的方法，我们可以抽一个方法，来将每个额外的装饰方法重复遍历装饰者列表中的这块代码，通过它来接收方法并使其成为“可装饰”的方法。这样实现，
` sale ` 的 ` decorators_list ` 属性会成为一个对象，且该对象每个属性都是以装饰者对象数组中的方法和值命名。

##  五、策略模式(Strategy Pattern)

###  1.概念介绍

**策略模式(Strategy Pattern)** ：封装一系列算法，支持我们在运行时，使用相同接口，选择不同算法。它的目的是为了
**将算法的使用与算法的实现分离开来** 。

策略模式通常会有两部分组成，一部分是 **策略类** ，它负责实现通用的算法，另一部分是 **环境类** ，它用户接收客户端请求并委托给策略类。

###  2.优缺点

####  2.1优点

  * 有效地避免多重条件选择语句； 
  * 支持开闭原则，将算法独立封装，使得更加便于切换、理解和扩展； 
  * 更加便于代码复用； 

####  2.2缺点

  * 策略类会增多； 
  * 所有策略类都需要对外暴露； 

###  3.基本案例

我们可以很简单的将策略和算法直接做映射：

    
    
    let add = {
        "add3" : (num) => num + 3,
        "add5" : (num) => num + 5,
        "add10": (num) => num + 10,
    }
    let demo = (type, num) => add[type](num);
    console.log(demo('add3', 10));  // 13
    console.log(demo('add10', 12)); // 22

然后我们再把每个策略的算法抽出来：

    
    
    let fun3  = (num) => num + 3;
    let fun5  = (num) => num + 5;
    let fun10 = (num) => num + 10;
    let add = {
        "add3" : (num) => fun3(num),
        "add5" : (num) => fun5(num),
        "add10": (num) => fun10(num),
    }
    let demo = (type, num) => add[type](num);
    console.log(demo('add3', 10));  // 13
    console.log(demo('add10', 12)); // 22
    

###  4.表单验证案例

我们需要使用策略模式，实现一个处理表单验证的方法，无论表单的具体类型是什么都会调用验证方法。我们需要让验证器能选择最佳的策略来处理任务，并将具体的验证数据委托给适当算法。

我们假设需要验证下面的表单数据的有效性：

    
    
    let data = {
        name    : 'pingan',
        age     : 'unknown',
        nickname: 'leo',
    }

这里需要先配置验证器，对表单数据中不同的数据使用不同的算法：

    
    
    validator.config = {
        name    : 'isNonEmpty',
        age     : 'isNumber',
        nickname: 'isAlphaNum',
    }

并且我们需要将验证的错误信息打印到控制台：

    
    
    validator.validate(data);
    if(validator.hasErrors()){
        console.log(validator.msg.join('\n'));
    }

接下来我们才要实现 ` validator ` 中具体的验证算法，他们都有一个相同接口 ` validator.types ` ，提供 `
validate() ` 方法和 ` instructions ` 帮助信息：

    
    
    // 非空值检查
    validator.types.isNonEmpty = {
        validate: function(value){
            return value !== '';
        }
        instructions: '该值不能为空'
    }
    
    // 数值类型检查
    validator.types.isNumber = {
        validate: function(value){
            return !isNaN(value);
        }
        instructions: '该值只能是数字'
    }
    
    // 检查是否只包含数字和字母
    validator.types.isAlphaNum = {
        validate: function(value){
            return !/[^a-z0-9]/i.test(value);
        }
        instructions: '该值只能包含数字和字母，且不包含特殊字符'
    }

最后就是要实现最核心的 ` validator ` 对象：

    
    
    let validator = {
        types: {}, // 所有可用的检查
        msg:[],    // 当前验证的错误信息
        config:{}, // 验证配置
        validate: function(data){ // 接口方法
            let type, checker, result;
            this.msg = []; // 清空错误信息
            for(let k in data){
                if(data.hasOwnProperty(k)){
                    type = this.config[k];
                    checker = this.types[type];
                    if(!type) continue;  // 不存在类型 则 不需要验证
                    if(!checker){
                        throw {
                            name: '验证失败',
                            msg: `不能验证类型：${type}`
                        }
                    }
                    result = checker.validate(data[k]);
                    if(!result){
                        this.msg.push(`无效的值：${k}，${checker.instructions}`);
                    }
                }
            }
            return this.hasErrors();
        }
        hasErrors: function(){
            return this.msg.length != 0;
        }
    }

总结这个案例，我们可以看出 ` validator ` 对象是通用的，需要增强 ` validator `
对象的方法只需添加更多的类型检查，后续针对每个新的用例，只需配置验证器和运行 ` validator() ` 方法就可以。

###  5.小结

日常开发的时候，还是需要根据实际情况来选择设计模式，而不能为了设计模式而去设计模式。通过上面的学习，我们使用策略模式来避免多重条件判断，并且通过开闭原则来封装方法。我们应该多在开发中，逐渐积累自己的开发工具库，便于以后使用。

##  参考资料

  1. 《JavaScript Patterns》 

Author  |  王平安   
---|---  
E-mail  |  pingan8787@qq.com   
博 客  |  www.pingan8787.com   
微 信  |  pingan8787   
每日文章推荐  |  [ https://github.com/pingan8787... ]()  
JS小册  |  js.pingan8787.com   
微信公众号  |  前端自习课 

