---
date: 2023-12-08
category:
    - javascript
tag:
    - javascript
---
 # 《JavaScript 模式》知识点小抄本（下）
##  介绍

最近开始给自己每周订个学习任务，学习结果反馈为一篇文章的输出，做好学习记录。  
这一周(02.25-03.03)我定的目标是 [ 《JavaScript 模式》 ]() 的第七章学习一遍，学习结果的反馈就是本篇文章啦。  
由于内容实在太长，我将本文分为两部分：

  * [ 《JavaScript 模式》知识点整理（上） ]()
  * **《JavaScript 模式》知识点整理（下）**

本文内容中主要参考《JavaScript 模式》，其中也有些案例是来自网上资料，有备注出处啦，如造成不便，请联系我删改。

过两天我会把这篇文章收录到我整理的知识库 [ 【Cute-JavaScript】 ]() 中，并已经同步到 [ 【github】 ]() 上面。

##  六.外观模式(Facade Pattern)

###  1.概念介绍

**外观模式(Facade Pattern)** 是一种简单又常见的模式，它为一些复杂的子系统接口提供一个更高级的统一接口，方便对这些子系统的接口访问。

它不仅简化类中的接口，还对接口和调用者进行解耦，外观模式也常被认为是开发者必备，它可以将一些复杂操作封装起来，并创建一个简单接口用于调用。

###  2.优缺点和应用场景

####  2.1优点

  * 轻量级，减少系统相互依赖。 
  * 提高灵活性。 
  * 提高了安全性。 

####  2.2缺点

  * 不符合开闭原则，如果要改东西很麻烦，继承重写都不合适。 

####  2.3应用场景

  * 为复杂的模块或子系统提供外界访问的模块。 
  * 子系统相对独立。 
  * 预防低水平人员带来的风险。 
  * 项目重构。 

###  3.基本案例

经常我们在处理一些特殊情况的时候，需要一起调用好几个方法，我们使用外观模式，就可以将多个方法包装成一个方法，哪里需要使用直接调用这个包装好的方法就可以。  
比如我们经常处理浏览器事件，需要同时调用 ` stopPropagation() ` 和 ` preventDefault() `
，于是我们就可以新建一个外观方法，实现这两个方法同时调用：

    
    
    let myEvent = {
        // ...
        stop: e => {
            e.stopPropagation();
            e.preventDefault();
        }
    };

然后我们也可以使用外观模式，来做IE事件的兼容性：

    
    
    let myEvent = {
        // ...
        stop: e => {
            // 其他 
            if(typeof e.preventDefault === 'function'){
                e.preventDefault();
            }
            if(typeof e.stopPropagation === 'function'){
                e.stopPropagation();
            }
            // IE
            if(typeof e.returnValue === 'boolean'){
                e.returnValue = false;
            }
            if(typeof e.cancelBubble === 'boolean'){
                e.cancelBubble = true;
            }
        }
    };

##  七、代理模式(Proxy Pattern)

###  1.概念介绍

**代理模式(Proxy Pattern)** 为其他对象提供一种代理，来控制这个对象的访问，代理是在客户端和真实对象之间的介质。

简单的理解：如我们需要请明星来做广告，我们会先通过联系Ta的经纪人，谈好条件才会给明星签合同。

###  2.优缺点和应用场景

####  2.1优点

  * 职责单一且清晰。 
  * 保护真实对象。 
  * 开闭原则，高拓展性。 

####  2.2缺点

  * 由于在客户端和真实对象间添加代理对象，导致请求处理速度变慢。 
  * 实现代理模式需要额外工作，有些代理模式实现起来非常复杂。 

####  2.3应用场景

  * 需要隐藏或保护某个类，则为这个类添加代理。 
  * 需要给不同访问者提供不同权限，则在代理类上做判断。 
  * 需要为某个类添加功能，如添加日志缓存等，我们可以在代理的类做添加，而不管去改原来封装好的类。 

###  3.基本案例

这里我们以吃午饭问题来学习 **代理模式** 。通常情况下，我们会有两种方式解决午饭问题：“去餐厅吃”和“叫外卖”。  
去餐厅吃的话，我们就是自己过去吃饭了呗，如果是叫外卖，我们就会通过外卖小哥来拿到午饭才能吃起来。

  * **去餐厅吃** （没有使用代理模式） 

    
    
    // 定义午饭类 参数 菜名
    let Lunch = function(greens){
        this.greens = greens;
    }
    Lunch.prototype.getGreens = function(){
        return this.greens;
    }
    // 定义我这个对象
    let leo = {
        buy: function(greens){
            console.log(`午饭吃${greens.getGreens()}`);
        }
    }
    // 去餐厅吃
    leo.buy(new Lunch('青椒炒肉')); // 午饭吃青椒炒肉

  * **叫外卖** （有使用代理模式） 

    
    
    // 定义午饭类 参数 菜名
    let Lunch = function(greens){
        this.greens = greens;
    }
    Lunch.prototype.getGreens = function(){
        return this.greens;
    }
    // 定义外卖小哥这个对象
    let brother = {
        buy: function(lunch){
            leo.buy(lunch.getGreens());
        }
    }
    // 定义我这个对象
    let leo = {
        buy: function(greens){
            console.log(`午饭吃${greens}`);
        }
    }
    // 叫外卖
    brother.buy(new Lunch('青椒炒肉')); // 午饭吃青椒炒肉

并且外卖小哥还会帮我们做一些其他事，比如帮我们带瓶可乐，我们改造 ` brother ` 和 ` leo ` 这2个对象，再看看效果：

    
    
    let brother = {
        buy: function(lunch){
            if(leo.needCola) leo.buyCola();
            leo.buy(lunch.getGreens());
        }
    }
    
    let leo = {
        needCola: true,
        buy: function(greens){
            console.log(`午饭吃${greens}`);
        },
        buyCola: function(){
            console.log(`顺手买瓶可乐！`);
        }
    }
    brother.buy(new Lunch('青椒炒肉'));
    // 顺手买瓶可乐！
    // 午饭吃青椒炒肉

###  4.保护代理

还是借用 **3.基本案例** 的叫外卖的例子，我们现在要实现保护代理，而我们需要外卖小哥为了我们的身体健康，超过晚上9点，就不帮我们买可乐。  
还是改造上面买可乐的 ` brother ` 对象代码：

    
    
    let brother = {
        buy: function(lunch){
            let nowDate = new Date();
            if(nowDate.getHours() >= 21){
                console.log('亲，这么晚不要喝可乐哟！');
            }else{
                if(leo.needCola) leo.buyCola();
                leo.buy(lunch.getGreens());
            }
        }
    }
    brother.buy(new Lunch('青椒炒肉'));
    // 顺手买瓶可乐！
    // 午饭吃青椒炒肉

###  5.虚拟代理

虚拟代理能把一些开销大的对象，延迟到真正需要的时候才去创建和执行。  
我们这里举个图片懒加载的例子：  
这个案例参考自 [ JS设计模式-代理模式 ]() .

    
    
    // 图片加载
    let ele = (function(){
        let node = document.createElement('img');
        document.body.appendChild(node);
        return{
            setSrc : function(src){
                node.src = src;
            }
        }
    })()
    
    // 代理对象
    let proxy = (function(){
        let img = new Image();
        img.onload = function(){
            ele.setSrc(this.src);
        }
        return {
            setSrc : function(src){
                img.src = src;
                ele.setSrc('loading.png');
            }
        }
    })()
    
    proxy.setSrc('example.png');

###  6.缓存代理

缓存代理是将一些开销大的运算结果提供暂存功能，当下次计算时，参数和之前一直，则将缓存的结果返回：  
这个案例参考自 [ JS设计模式-代理模式 ]() .

    
    
    //计算乘积
    let mult = function(){
        let result = 1;
        for(let i = 0; i<arguments.length; i++){
            result *= arguments[i];
        }
        return result;
    }
    
    // 缓存代理
    let proxy = (function(){
        let cache = {};
        return function(){
            let args = Array.prototype.join.call(arguments, '',);
            if(args in cache){
                return cache[args];
            }
            return cache[args] = mult.apply(this,arguments);
        }
    })();

##  八、中介者模式(Mediator Pattern)

###  1.概念介绍

**中介者模式(Mediator Pattern)** 是用来降低多个对象和类之间的通信复杂性，促进形成松耦合，提高可维护性。

在这种模式下，独立的对象之间不能直接通信，而是需要中间对象（ ` mediator ` 对象），当其中一个对象（ ` colleague `
对象）状态改变后，它会通知 ` mediator ` 对象，  
然后 ` mediator ` 对象会把该变换通知到任意需要知道此变化的 ` colleague ` 对象。

###  2.优缺点和应用场景

####  2.1优点

  * 降低类的复杂度，从一对多转成一对一。 
  * 为各个类之间解耦。 
  * 提高代码可维护性。 

####  2.2缺点

中介者会越来越庞大，变得难以维护。

####  2.3应用场景

  * 系统中对象之间存在比较复杂的引用关系，而且难以复用该对象。 
  * 需要生成最少的子类，实现一个中间类封装多个类中的行为的时候。 

另外： 不要在职责混乱的时候使用。

###  3.基本案例

这里我们实现一个简单的案例，一场测试结束后，公布结果，告知解答出题目的人挑战成功，否则挑战失败：  
这个案例来自 [ JavaScript 中常见设计模式整理 ]()

    
    
    const player = function(name) {
        this.name = name;
        playerMiddle.add(name);
    }
    
    player.prototype.win = function() {
        playerMiddle.win(this.name);
    }
    
    player.prototype.lose = function() {
        playerMiddle.lose(this.name);
    }
    
    const playerMiddle = (function() { // 将就用下这个 demo，这个函数当成中介者
        const players = [];
        const winArr =  [];
        const loseArr = [];
        return {
            add: function(name) {
                players.push(name)
            },
            win: function(name) {
                winArr.push(name)
                if (winArr.length + loseArr.length === players.length) {
                    this.show()
                }
            },
            lose: function(name) {
                loseArr.push(name)
                if (winArr.length + loseArr.length === players.length) {
                    this.show()
                }
            },
            show: function() {
                for (let winner of winArr) {
                    console.log(winner + '挑战成功;')
                }
                for (let loser of loseArr) {
                    console.log(loser + '挑战失败;')
                }
            },
        }
    }())
    
    const a = new player('A 选手');
    const b = new player('B 选手');
    const c = new player('C 选手');
    
    a.win()
    b.win()
    c.lose()
    
    // A 选手挑战成功;
    // B 选手挑战成功;
    // C 选手挑战失败;

###  4.书本案例

这个案例来自 《JavaScript 模式》第七章 中介者模式 的案例。  
这里我们有这么一个游戏例子，规则是两个玩家在规定时间内，比比谁点击按钮次数更多，玩家1按按键2，玩家2按按键0，并且计分板实时更新。

这里的中介者需要知道所有其他对象信息，并且它需要知道哪个玩家点击了一次，随后通知玩家。玩家进行游戏的时候，还要通知中介者它做的事情，中介者更新分数并显示比分。

这里的 ` player ` 对象都是通过 ` Player() ` 构造函数生成，并且都有 ` points ` 和 ` name ` 属性，每次调用 `
play() ` 都会增加1分并通知中介者。

    
    
    function Player(name){
        this.points = 0;
        this.name   = name;
    }
    Player.prototype.play = function(){
        this.points += 1;
        mediator.played();
    }

计分板有个 ` update() ` 方法，当玩家回合结束就会调用，它不知道任何玩家的信息也没有保存分值，只是实现展示当前分数。

    
    
    let scoreboard = {
        // 待更新HTML元素
        ele: document.getElementById('result');
        // 更新比分
        update: function (score){
            let msg = '';
            for(let k in score){
                if(score.hasOwnProperty(k)){
                    msg = `<p>${k} : ${score[k]}<\/p>`
                }
            }
            this.ele.innerHTML = msg;
        }
    }

接下来创建 ` mediator ` 对象：

    
    
    let mediator = {
        players: {},       // 所有玩家
        setup: function(){ // 初始化
            let players = this.players;
            players.homw = new Player('Home');
            players.guest = new Player('Guest');
        },
        // 当有人玩时 更新分数
        played: function(){
            let players = this.players 
            let score = {
                Home: players.home.points,
                Guest: players.guest.points,
            }
            scoreboard.update(score);
        }
        // 处理用户交互
        keypress: function(e){
            e = e || window.event;  // 兼容IE
            if(e.which === 49){     // 按键1
                mediator.players.home.play();
            }
            if(e.which === 48){     // 按键0
                mediator.players.guest.play();
            }
        }
    }

最后就是需要运行和卸载游戏了：

    
    
    mediator.setup();
    window.onkeypress = mediator.keypress;
    // 游戏30秒后结束
    setTimeout(function(){
        window.onkeypress = null;
        alert('游戏结束');
    }, 30000)

##  九、观察者模式(Observer Patterns)

###  1.概念介绍

**观察者模式(Observer Patterns)** 也称 **订阅/发布（subscriber/publisher）模式**
，这种模式下，一个对象订阅定一个对象的特定活动，并在状态改变后获得通知。  
这里的订阅者称为观察者，而被观察者称为发布者，当一个事件发生，发布者会发布通知所有订阅者，并常常以事件对象形式传递消息。

所有浏览器事件（鼠标悬停，按键等事件）都是该模式的例子。

我们还可以这么理解：这就跟我们订阅微信公众号一样，当公众号（发布者）群发一条图文消息给所有粉丝（观察者），然后所有粉丝都会接受到这篇图文消息（事件），这篇图文消息的内容是发布者自定义的（自定义事件），粉丝阅读后可能就会买买买（执行事件）。

###  2.观察者模式 VS 发布订阅模式

####  2.1观察者模式

一种一对多的依赖关系，多个观察者对象同时监听一个主题对象。这个主题对象在状态上发生变化时，会通知所有观察者对象，使它们能够自动更新自己。

####  2.2发布订阅模式

发布订阅模式理念和观察者模式相同，但是处理方式上不同。  
在发布订阅模式中，发布者和订阅者不知道对方的存在，他们通过调度中心串联起来。  
订阅者把自己想订阅的事件注册到调度中心，当该事件触发时候，发布者发布该事件到调度中心（并携带上下文），由调度中心统一调度订阅者注册到调度中心的处理代码。

####  2.3两者异同点

  * 观察者模式中，观察者知道发布者是谁，并发布者保持对观察者进行记录。而发布订阅模式中，发布者和订阅者不知道对方的存在。它们只是通过调度中心进行通信。 
  * 发布订阅模式中，组件是松散耦合的，正好和观察者模式相反。 
  * 观察者模式大多是同步，如当事件触发，发布者就会去调用观察者的方法。而发布订阅模式大多是异步的（使用消息队列）。 
  * 观察者模式需要在单个应用程序地址空间中实现，而发布-订阅更像交叉应用模式。 

尽管存在差异，但也有人说发布-订阅模式是观察者模式的变异，因为它们概念上相似。

####  2.4两者优缺点

**相同优点：**

  * 都可以一对多 
  * 程序便于扩展 

**不同优点：**

  * 观察者模式：单向解耦，发布者不需要清楚订阅者何时何地订阅，只需要维护订阅队列，发送消息即可 
  * 发布订阅模式：双向解耦，发布者和订阅者都不用清楚对方，全部由订阅中心做处理 

**缺点：**

  * 如果一个被观察者和多个观察者的话，会增加维护的难度，并且会消耗很多时间。 
  * 如果观察者和发布者之间有循环依赖，可能会导致循环调用引起系统奔溃。 
  * 观察者无法得知观察的目标对象是如何发生变化，只能知道目标对象发生了变化。 
  * 发布订阅模式，中心任务过重，一旦崩溃，所有订阅者都会受到影响。 

###  4.基本案例

我们平常一直使用的给DOM节点绑定事件，也是观察者模式的案例：

    
    
    document.body.addEventListener('click', function(){
        alert('ok');
    },false);
    document.body.click();

这里我们订阅了 ` document.body ` 的 ` click ` 事件，当 ` body ` 点击它就向订阅者发送消息，就会弹框 ` ok `
。我们也可以添加很多的订阅。

###  4.观察者模式 案例

本案例来自 [ javascript 观察者模式和发布订阅模式 ]() 。

    
    
    class Dom {
        constructor() {
            // 订阅事件的观察者
            this.events = {}
        }
    
        /**
        * 添加事件的观察者
        * @param {String} event  订阅的事件
        * @param {Function} callback 回调函数(观察者)
        */
        addEventListener(event, callback) {
            if (!this.events[event]) {
                this.events[event] = []
            }
            this.events[event].push(callback)
        }
    
        removeEventListener(event, callback) {
            if (!this.events[event]) {
                return
            }
            const callbackList = this.events[event]
            const index = callbackList.indexOf(callback)
                if (index > -1) {
                callbackList.splice(index, 1)
            }
        }
    
        /**
        * 触发事件
        * @param {String} event
        */
        fireEvent(event) {
            if (!this.events[event]) {
                return
            }
            this.events[event].forEach(callback => {
                callback()
            })
        }
    }
    
    const handler = () => {
        console.log('fire click')
    }
    const dom = new Dom()
    
    dom.addEventListener('click', handler)
    dom.addEventListener('move', function() {
        console.log('fire click2')
    })
    dom.fireEvent('click')

###  5.发布订阅模式 案例

本案例来自 [ javascript 观察者模式和发布订阅模式 ]() 。

    
    
    class EventChannel {
        constructor() {
            // 主题
            this.subjects = {}
        }
    
        hasSubject(subject) {
            return this.subjects[subject] ? true : false
        }
    
        /**
        * 订阅的主题
        * @param {String} subject 主题
        * @param {Function} callback 订阅者
        */
        on(subject, callback) {
            if (!this.hasSubject(subject)) {
                this.subjects[subject] = []
            }
            this.subjects[subject].push(callback)
        }
    
        /**
        * 取消订阅
        */
        off(subject, callback) {
            if (!this.hasSubject(subject)) {
                return
            }
            const callbackList = this.subjects[subject]
            const index = callbackList.indexOf(callback)
            if (index > -1) {
                callbackList.splice(index, 1)
            }
        }
    
        /**
        * 发布主题
        * @param {String} subject 主题
        * @param {Argument} data 参数
        */
        emit(subject, ...data) {
            if (!this.hasSubject(subject)) {
                return
            }
            this.subjects[subject].forEach(callback => {
                callback(...data)
            })
        }
    }
    
    const channel = new EventChannel()
    
    channel.on('update', function(data) {
        console.log(`update value: ${data}`)
    })
    channel.emit('update', 123)

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

