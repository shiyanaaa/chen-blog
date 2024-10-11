---
date: 2024-07-18
category:
    - 原型链
tag:
    - 原型链
    - 继承
    - javascript
---
 # JavaScript继承
1、原型链继承

    
    
    function Parent() {
        this.name = 'Mike'
    }
    function Child() {
        this.age = 12;
    }
    Child.prototype = new Parent();//Child继承Parent，通过原型，形成链条
    
    var test = new Child();
    console.log(test.age);
    console.log(test.name);//得到被继承的属性
    
    //继续原型链继承
    function Brother() {//brother构造
        this.weight = 60;
    }
    Brother.prototype = new Child();//继续原型链继承
    var brother = new Brother();
    console.log(brother.name);
    console.log(brother.age);
    

2、借用构造函数（类式继承）

    
    
    function Parent(age) {
        this.name = ['Mike', 'Bill', 'Andy'];
        this.age = age;
    }
    function Child(age) {
        Parent.call(this, age);//把this指向Parent,同时还可以传递参数
    }
    var test = new Child(21);
    console.log(test.name);
    console.log(test.age);
    test.name.push('Bill');
    console.log(test.name);
    

3、组合继承

    
    
    function Parent(age) {
        this.name = ["Mike", "Jack", "Bill"];
        this.age = age;
    }
    Parent.prototype.run = function () {
        return this.name + " are both " + this.age;
    };
    function Child(age) {
        Parent.call(this, age);//对象冒充，给超类型传参
    }
    Child.prototype = new Parent();//原型链继承
    var child = new Child(12);//写new Parent(12)也行
    console.log(child.run() + " years old.");
    

4、原型式继承

    
    
    function obj(o) {
        function F() {
        }
    
        F.prototype = o;
        return new F();
    }
    var box = {
        name: "Andy",
        arr: ["brother", "sister", "father"]
    };
    var b1 = obj(box);
    console.log(b1.name);
    console.log(b1.arr);
    
    b1.name = "Mike";
    console.log(b1.name);
    
    b1.arr.push("mother");
    console.log(b1.arr);
    
    var b2 = obj(box);
    console.log(b2.name);
    console.log(b2.arr);
    

5、寄生组合式继承

    
    
    function obj(o) {
        function F() {
        }
    
        F.prototype = o;
        return new F();
    }
    function create(parent, test) {
        var f = obj(parent.prototype);//创建对象
        v.constructor = test;//增强对象
    }
    function Parent(name) {
        this.name = name;
        this.arr = ["brother", "sister", "father"]
    }
    Parent.prototype.run = function () {
        return this.name;
    };
    function Child(name, age) {
        Parent.call(this, name);
        this.age = age;
    }
    Child.prototype = new Parent();
    
    var test = new Child("Andy", 12);
    console.log(test.run());
    
    test.arr.push("Jack");
    console.log(test.arr);
    console.log(test.run());//Andy,只共享了方法
    
    var test2 = new Child("Bill", 21);
    console.log(test2.arr);//引用问题解决
    

