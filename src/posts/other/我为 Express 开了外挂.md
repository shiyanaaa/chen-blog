---
date: 2024-05-14
category:
    - 前端
tag:
    - 前端
    - javascript
    - typescript
    - node.js
---
 # 我为 Express 开了外挂
> 本项目源码地址：  
>  [ https://github.com/pingan8787/Leo-JavaScript/blob/master/Cute-
> Gist/LearnSource/OvernightDemo/ ]()

随着 Nodejs 在前端涉及领域越来越广，也越来越成熟，相信很多朋友已经尝试或使用过 Nodejs 开发服务端项目了。  
本文我将和大家一起回顾 Express，然后介绍一个超级外挂—— **OvernightJS** ，它强大的地方在于，它将为 Express 路由提供
TypeScript 装饰器支持，使得我们开发路由更加简单，代码复用性更好。  
这里也希望帮助大家对 TypeScript 的装饰器有更深了解。

接下来跟本文主角 Leo 一起来看看这个外挂吧~

##  一、背景介绍

最近 Leo 打算使用 [ Express ]() 来开始重构自己博客的服务端项目，经过认真研究和设计，并确定完方案，Leo 开始下手啦：

    
    
    // app.ts
    
    import express, { Application, Request, Response } from 'express';
    
    const app: Application = express();
    
    app.get('/', (req: Request, res: Response) => {
      res.send('Hello World!');
    });
    
    app.listen(3000, ()=> {
      console.log('Example app listening on port 3000!');
    });

其中 tsconfig.json 配置如下：

    
    
    {
      "compilerOptions": {
        "target": "es6",
        "module": "commonjs",
        "strict": true,
            "esModuleInterop": true,
        "experimentalDecorators": true, // 开启装饰器
        "emitDecoratorMetadata": true,  // 开启元编程
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      }
    }

基本代码写完，测试能不能跑起来。  
Leo 在命令行使用 ` ts-node ` 命令行执行。（ [ ts-node ]() 用来直接运行 ts 文件，详细介绍请查看文档，这里不细讲咯）：

    
    
    $ ts-node app.ts

看到命令行输出：

    
    
    Example app listening on port 3000!

服务跑起来了，心情愉快。  
接下来 Leo 使用 Express 的路由方法写了其他接口：

    
    
    // app.ts
    
    app.get('/article', (req: Request, res: Response) => {res.send('Hello get!')});
    app.post('/article', (req: Request, res: Response) => {res.send('Hello post!')});
    app.put('/article', (req: Request, res: Response) => {res.send('Hello put!')});
    app.delete('/article', (req: Request, res: Response) => {res.send('Hello delete!')});
    app.get('/article/list', (req: Request, res: Response) => {res.send('Hello article/list!')});
    // ... 等等其他接口

> Express 路由方法派生自 HTTP 方法之一，附加到 express 类的实例。 支持对应于 HTTP
> 方法的以下路由方法：get、post、put、head、delete、options等等。

同事 Robin 看了看代码，问到：  

随着接口越写越多，代码不免出现复杂和冗余的情况，为了解决这个问题，Leo 引入 Express 的 ` Router() ` ，来创建
**可安装的模块化路由处理程序** 。Router 实例是 **完整的中间件** 和 **路由系统** 。因此，常常将其称为“ **微型应用程序** ”。

Leo 新建文件 ` app.router.ts ` ，重新实现上面接口：

    
    
    // app.router.ts
    
    import express, { Router, Request, Response } from 'express';
    const router: Router = express.Router();
    
    router.get('/', (req: Request, res: Response) => {res.send('Hello get!')});
    router.post('/', (req: Request, res: Response) => {res.send('Hello post!')});
    router.put('/', (req: Request, res: Response) => {res.send('Hello put!')});
    router.delete('/', (req: Request, res: Response) => {res.send('Hello delete!')});
    router.get('/user', (req: Request, res: Response) => {res.send('Hello api/user!')});
    
    export default router;

接着在 app.ts 中使用，由于 [ ` express.Router() ` ]() 是个中间件，因此可以使用 ` app.use() ` 来使用：

    
    
    // app.ts
    
    // 删除原来路由声明
    import router from "../controller/app.router";
    app.use('/api', router);

这里 ` app.use ` 第一个参数 ` /api ` 表示这一组路由对象的根路径，第二个参数 ` router ` 表示一组路由对象。

于是就实现了下面 API 接口：

  * ` /api `
  * ` /api/user `

确定所有接口正常运行后，Leo 琢磨着，既然 Express 每个路由都是由 **路由名称** 和 **路由处理方法** 组成，那为什么不能给
Express 加个外挂？为每个路由添加装饰器来装饰。  
幸运的是，已经有大佬实现这个外挂了，它就是今天主角—— [ OvernightJS ]() 。  
下面一起看看这个很棒的 OvernightJS 吧。

##  二、基础知识介绍

  
在开始介绍 Overnight 之前，我们先回顾下“装饰器”和“Reflect”：

###  1\. 装饰器

####  1.1 什么是装饰器？

TypeScript 中，装饰器（Decorators）是一种特殊类型的声明，它能够被附加到类声明、方法、访问符、属性或参数上， **本质上还是个函数**
。  
装饰器为我们在类的声明及成员上通过 **元编程语法** 添加标注提供了一种方式。

需要记住这几点：

  * 装饰器是一个声明（表达式）； 
  * 该表达式被执行后， **返回一个函数** ； 
  * 函数的入参分别为 ` target ` 、 ` name ` 和 ` descriptor ` ； 
  * 执行该函数后，可能返回 ` descriptor ` 对象，用于配置 ` target ` 对象； 

更多装饰器详细介绍，请阅读文档 [ 《TypeScript 装饰器》 ]() 。

####  1.2 装饰器分类

装饰器一般包括：

  * 类装饰器（Class decorators）； 
  * 属性装饰器（Property decorators）； 
  * 方法装饰器（Method decorators）； 
  * 参数装饰器（Parameter decorators）； 

####  1.3 示例代码

这里以类装饰器（Class decorators）为例，介绍如何使用装饰器：

    
    
    function MyDecorators(target: Function): void {
      target.prototype.say = function (): void {
        console.log("Hello 前端自习课!");
      };
    }
    
    @MyDecorators
    class LeoClass {
      constructor() {}
      say(){console.log("Hello Leo")}
    }
    
    let leo = new LeoClass();
    leo.say(); 
    // 'Hello Leo!';

####  1.4 编译结果

装饰器实际上非常简单，编译出来以后，只是个函数，我们接着看。  
这里以《1.3 示例代码》为例，看看它的编译结果：

    
    
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    function MyDecorators(target) {
        target.prototype.say = function () {
            console.log("Hello 前端自习课!");
        };
    }
    let LeoClass = class LeoClass {
        constructor() { }
        say() { console.log("Hello Leo"); }
    };
    LeoClass = __decorate([
        MyDecorators,
        __metadata("design:paramtypes", [])
    ], LeoClass);
    let leo = new LeoClass();
    leo.say();
    // 'Hello Leo!';

其实就是 ` __decorate ` 函数啦，具体大家可以自行细看咯~  
从编译后 JS 代码中可以看出， **装饰器是在模块导入时便执行的** 。如下：

    
    
    LeoClass = __decorate([
        MyDecorators,
        __metadata("design:paramtypes", [])
    ], LeoClass);

####  1.5 小结

接下来通过下图来回顾装饰器的知识。  

###  2\. Reflect Metadata API

####  2.1 什么是 Reflect ？

Reflect（即反射）是 ES6 新增的一个 **内置对象** ，它提供用来 **拦截和操作** JavaScript 对象的 API。并且
**Reflect 的所有属性和方法都是静态的** ，就像 Math 对象（ ` Math.random() ` 等）。

更多 Reflect 详细介绍，请阅读文档 [ 《MDN Reflect》 ]() 。

####  2.2 为什么出现 Reflect？

其核心目的，是为了保持 JS 的简单，让我们可以不用写很多代码，这里举个栗子🌰，看看有使用 Reflect 和没使用有什么区别：  
当对象里有 ` Symbol ` 时，如何遍历对象的 ` keys ` ？

    
    
    const s = Symbol('foo');
    const k = 'bar';
    const o = { [s]: 1, [k]: 1 };
    
    // 没有使用 Reflect
    const keys = Object.getOwnPropertyNames(o).concat(Object.getOwnPropertySymbols(o));
    
    // 使用 Reflect
    Reflect.ownKeys(o);

这看起来是不是简单多了？

更多 ` Reflect ` 详细介绍，请阅读文档 [ 《MDN Reflect》 ]() 。

####  2.3 什么是 Reflect Metadata

Reflect Metadata 是 ES7 的一个提案，它主要用来 **在声明的时添加和读取元数据** 。TypeScript 在 1.5+
的版本已经支持它，你只需要：

  * ` npm i reflect-metadata --save ` 。 
  * 在 ` tsconfig.json ` 里配置 ` emitDecoratorMetadata ` 选项。 

Reflect Metadata 可以当做装饰器使用，有两个 API：

  * 使用 ` Reflect.metadata() ` API **添加元数据** ； 
  * 使用 ` Reflect.getMetadata() ` API **读取元数据** 。 

    
    
    @Reflect.metadata('inClass', 'A')
    class LearnReflect {
      @Reflect.metadata('inMethod', 'B')
      public hello(): string {
        return 'hello world';
      }
    }
    
    console.log(Reflect.getMetadata('inClass', LearnReflect)); // 'A'
    console.log(Reflect.getMetadata('inMethod', new LearnReflect(), 'hello')); // 'B'

当然 ` Reflect ` 提供很多其他 API：

    
    
    import 'reflect-metadata';
    
    // 定义对象或属性的元数据
    Reflect.defineMetadata(metadataKey, metadataValue, target);
    Reflect.defineMetadata(metadataKey, metadataValue, target, propertyKey);
    
    // 检查对象或属性的原型链上是否存在元数据键
    let result = Reflect.hasMetadata(metadataKey, target);
    let result = Reflect.hasMetadata(metadataKey, target, propertyKey);
    
    // 检查对象或属性是否存在自己的元数据键
    let result = Reflect.hasMetadata(metadataKey, target);
    let result = Reflect.hasMetadata(metadataKey, target, propertyKey);
    
    // 获取对象或属性原型链上元数据键的元数据值
    let result = Reflect.getMetadata(metadataKey, target);
    let result = Reflect.getMetadata(metadataKey, target, propertyKey);
    
    // 获取对象或属性的自己的元数据键的元数据值
    let result = Reflect.getOwnMetadata(metadataKey, target);
    let result = Reflect.getOwnMetadata(metadataKey, target, propertyKey);
    
    // 获取对象或属性原型链上的所有元数据键
    let result = Reflect.getMetadataKeys(target);
    let result = Reflect.getMetadataKeys(target, propertyKey);
    
    // 获取对象或属性的所有自己的元数据键
    let result = Reflect.getOwnMetadataKeys(target);
    let result = Reflect.getOwnMetadataKeys(target, propertyKey);
    
    // 从对象或属性中删除元数据
    let result = Reflect.deleteMetadata(metadataKey, target);
    let result = Reflect.deleteMetadata(metadataKey, target, propertyKey);
    
    // 通过装饰器将元数据应用于构造函数
    @Reflect.metadata(metadataKey, metadataValue)
    class C {
      // 通过装饰器将元数据应用于方法(属性)
      @Reflect.metadata(metadataKey, metadataValue)
      method() {
      }
    }

需要记得配置 tsconfig.json：

    
    
    {
      "compilerOptions": {
        "target": "es5",
        "lib": ["es6", "dom"],
        "types": ["reflect-metadata"],
        "module": "commonjs",
        "moduleResolution": "node",
        "experimentalDecorators": true,
        "emitDecoratorMetadata": true
      }
    }

在 Overnight 中主要使用有两个 API：

  * 使用 ` Reflect.defineMetadata() ` API **添加元数据** ； 
  * 使用 ` Reflect.getOwnMetadata() ` API **读取元数据** 。 

下面以 Overnight 中类装饰器（Common Class）来介绍这两个 API 使用过程：  

####  2.4 小结

这里回顾下 Relect Metadata 的知识：  
  
理解清楚前面两个知识点后，我们接下来开始看看 Overnight。

##  三、Overnight 详解

###  1\. 概念介绍

[ **OvernightJS** ]() **主要是为 Express 路由提供 TypeScript 装饰器支持，通过装饰器来管理路由** 。  
是不是抽象了点？那看看下面这段代码吧：

    
    
    @Controller('api/posts')
    export class PostController {
        @Get(':id')
        private get(req: Request, res: Response) {
            // do something
        }
    }

如上面代码所示，OvernightJS 就是这样使用，简单，明了。  
另外 OvernightJS 共提供了三个库：

  * OvernightJS/core：核心库； 
  * OvernightJS/logger：日志记录工具库； 
  * OvernightJS/jwt： [ JWT ]() 库； 

接下来主要介绍 OvernightJS/core 核心库，其他两个有兴趣可以自己看哈，举一反三，其实核心一样的。

###  2\. OvernightJS/core 快速上手

####  2.1 安装 OvernightJS/core

    
    
    $ npm install --save @overnightjs/core express 
    $ npm install --save-dev @types/express

####  2.2 OvernightJS/core 示例代码

首先介绍下我们示例代码需要实现的功能：

  1. ` UserController ` 类，负责管理 **业务逻辑** 的控制器； 
  2. ` ServerController ` 类，负责管理 **服务逻辑** 的控制器； 
  3. 执行服务启动； 

**第一步** ，导入需要的依赖：

    
    
    import { Controller, Get, Server } from '@overnightjs/core';
    import { Request, Response } from 'express';
    import * as bodyParser from 'body-parser';
    const port = 3000;

**第二步** ，实现 ` UserController ` 类：

    
    
    @Controller('/users')
    class UserController {
        @Get('/:id')
        private get(req: Request, res: Response) {
            return res.send(`hello, your id is:${req.params.id}`)
        }
        @Get('/list')
        private getList(req: Request, res: Response) {
            return res.send([
              {name: "leo", age: 17},
              {name: "robin", age: 19}
            ])
        }
    }

在声明 ` UserController ` 类时，使用 OvernightJS/core 的 ` @Controller ` 装饰器，使用 `
"/users" `
路径作为参数，作用是为当前路由控制器指定一个路由地址，可以理解为这组路由的“根路径”，该类中实现的所有接口路径，都会以该“根路径”为基础。  
然后在 ` UserController ` 类中，通过 OvernightJS/core 提供 ` @Get ` 装饰器，分别使用 ` "/:id" `
和 ` "/list" ` 路径作为参数，绑定路由。

最终 ` UserController ` 类实现的路由地址包括：

  * ` /user/:id `
  * ` /users/list `

**第三步** ，实现 ` ServerController ` 类：

    
    
    class ServerController extends Server {
        constructor() {
            super();
            this.app.use(bodyParser.json());
            super.addControllers(new UserController());
        }
        public start(port?: number): void {
            this.app.listen(port, () => {console.log('启动成功，端口号：',port)});
        }
    }

` ServerController ` 类继承 OvernightJS/core 提供的 ` Server ` 类，通过在构造函数中调用 `
super.addControllers(new UserController()) `
来实现将前面声明好的路由控制器类，添加到OvernightJS/core 统一管理的控制器数组中。  
另外在该类中，我们还声明 ` start ` 方法，用来启动服务器。

**第四步** ，实现启动服务器逻辑：

    
    
    const server = new ServerController();
    server.start(port);

这里启动服务器就相当简单咯~~

整个实现示例代码的流程如下：  
声明了两个类： ` UserController ` 和 ` ServerController ` ，分别为 **业务逻辑的控制器** 和
**服务逻辑的控制器** ，最后在主入口中去实例化，并执行实例化结果的 ` start ` 方法启动服务。  
  
最后完整代码如下：

    
    
    import { Controller, Get, Server } from '@overnightjs/core';
    import { Request, Response } from 'express';
    import * as bodyParser from 'body-parser';
    const port = 3000;
    
    @Controller('users')
    class UserController {
        @Get(':id')
        private get(req: Request, res: Response) {
            return res.send(`hello, your id is:${req.params.id}`)
        }
        @Get('list')
        private get(req: Request, res: Response) {
            return res.send([
              {name: "leo", age: 17},
              {name: "robin", age: 19}
            ])
        }
    }
    
    class ServerController extends Server {
        constructor() {
            super();
            this.app.use(bodyParser.json());
            super.addControllers(new UserController());
        }
        public start(port?: number): void {
            this.app.listen(port, () => {console.log('启动成功，端口号：',port)});
        }
    }
    
    const server = new ServerController();
    server.start(port);

###  3\. OvernightJS/core 装饰器分析

在阅读源码过程中，我将 OvernightJS/core 中所有的装饰器按照 **源码目录结构维度** 做了分类，结果如下：  
  
通过上图可以清晰看出，OvernightJS/core 为我们提供了四个大类的装饰器，具体的使用方式，还请看看官网文档啦~

###  4\. OvernightJS/core 架构分析

OvernightJS/core 结构设计上还是比较简单，大致如下架构：  
  
在 OvernightJS/core 中，主要提供两个大类： ` Server ` 类和 ` Decorators ` 相关方法。  
其中 ` Server ` 类中的 ` addConterllers ` 方法是关键，下一节将详细介绍。哈哈

###  5\. OvernightJS/core 与 Express 关联

回顾下 Express ，我们经常通过 ` app.use(path, route) ` 来定义一个接口：

    
    
    app.use(path, route);

那么在 OvernightJS 中呢？？  
前一小节提到的 ` addConterllers ` 方法是什么呢？？

其实 OvernightJS 本质上是通过调用 ` addConterllers() ` 方法来和 Express 做关联。  
可以理解为 **OvernightJS 与 Express 之间的桥梁** ，它将 OvernightJS/core 定义好的路由控制器作为参数，通过
Express 的 ` use ` 方法，将路由添加的 Express 中，实现 Express 路由注册。

我们看下源码中 ` addControllers ` 方法做了什么事情：

    
    
    // core/lib/Server.ts
    
    public addControllers(
        controllers: Controller | Controller[],
        routerLib?: RouterLib,
        globalMiddleware?: RequestHandler,
    ): void {
        controllers = (controllers instanceof Array) ? controllers : [controllers];
        const routerLibrary: RouterLib = routerLib || Router;
        controllers.forEach((controller: Controller) => {
            if (controller) {
                const routerAndPath: IRouterAndPath | null = this.getRouter(routerLibrary, controller);
                if (routerAndPath) {
                    if (globalMiddleware) {
                        this.app.use(routerAndPath.basePath, globalMiddleware, routerAndPath.router);
                    } else {
                        this.app.use(routerAndPath.basePath, routerAndPath.router);
                    }
                }
            }
        });
    }

我们简化下上面代码，保留核心功能的源码：

    
    
    public addControllers(
        controllers: Controller | Controller[],
        routerLib?: RouterLib,
        globalMiddleware?: RequestHandler,
    ): void {
      // ... 省略其他代码
        controllers = (controllers instanceof Array) ? controllers : [controllers];
        controllers.forEach((controller: Controller) => {
            this.app.use(routerAndPath.basePath, routerAndPath.router);
        });
    }

从上面代码可以看出， ` addControllers ` 方法支持传入单个 controller 或一个数组的 controller，方法内通过 `
forEach ` 遍历每个控制器，并将 ` path ` 和 ` router ` 作为参数传入 ` app.use ` 方法中，实现 Express
的路由注册。

##  四、Overnight VS Express

从前面概念介绍中，我们知道：OvernightJS 主要是为 Express 路由提供 TypeScript 装饰器支持，通过装饰器来管理路由。

那么 **使用 OvernightJS 跟没有使用有什么区别呢？**  
下面我们分别通过 OvernightJS 和 Express 实现相同功能，功能包括：本地启动 4000 端口，支持 ` api/users/:id `
接口。

###  1\. OvernightJS 实现

首先实现入口文件，其中通过实例化 ` ServerController ` 类，并执行实例化结构的 ` start ` 方法来启动服务：

    
    
    // customApp.ts
    
    import ServerController from "../controller/custom.server.controller";
    const port = 4000;
    
    const server = new ServerController();
    server.start(port);

其中 tsconfig.json 配置如下：

    
    
    {
      "compilerOptions": {
        "target": "es6",
        "module": "commonjs",
        "strict": true,
        "esModuleInterop": true,
        "experimentalDecorators": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true
      }
    }

大致过程如上面代码，接下来要开始实现具体的 ` ServerController ` 类：

    
    
    // controller/custom.server.controller.ts
    
    import { Server } from "@overnightjs/core";
    import RouterController from "./custom.router.controller";
    
    class ServerController extends Server {
        constructor() {
            super();
            super.addControllers(new RouterController());
        }
        public start(port?: number): void {
            this.app.listen(port, () => {
                console.log('启动成功，端口号：',port)});
        }
    }
    
    export default ServerController;

  
最后实现 ` RouterController ` 类，该 API 下的路由方法，都定义在这个类中：

    
    
    // controller/custom.router.controller.ts
    import { Request, Response } from 'express';
    import { Controller, Get, Put } from '@overnightjs/core';
    
    @Controller("api/users")
    class RouterController {
        @Get(":id")
        private get(req:Request, res:Response): any{
            res.send("hello leo!")
        }
    }
    
    export default RouterController;

###  2\. Express 实现

跟前面一下，这里也是先实现入口文件：

    
    
    // app.ts
    
    import ServerController from "../controller/server.controller";
    const port = 4000;
    
    const server = new ServerController();
    server.start(port);

然后实现具体的 ` ServerController ` 类：

    
    
    // controller/server.controller/.ts
    
    import express, { Application } from 'express';
    import RouterController from "./router.controller";
    
    class ServerController {
        app: Application = express();
        constructor(){this.addControllers()};
        public addControllers(){
            const Router = new RouterController().getController();
            this.app.use('/api/users', Router);
        }
        public start(port?: number): void {
            this.app.listen(port, () => {console.log('启动成功，端口号：',port)});
        }
    }
    
    export default ServerController;

  
最后实现 ` RouterController ` 类：

    
    
    // controller/router.controller.ts
    
    import express, { Router, Application, Request, Response, NextFunction } from "express";
    
    class RouterController {
        router: Router = express.Router();
        constructor() { this.addControllers()};
        public getController = (): Router => this.router;
        public addControllers(): void {
            this.router.get("/:id", this.get);
        }
        public get (req: Request, res: Response, next: NextFunction){
            res.send("hello leo!")
            next();
        }
    }
    
    export default RouterController;

###  3\. 两者比较

相信看到这里的朋友，对前面两种实现方法大致了解了，接下来通过一张图，来看看总结两者实现的区别吧。  

##  五、总结

本文主要介绍 OvernightJS 与 Express 路由功能的基本使用，然后分别用两者实现相同的路由功能，对比得出 OvernightJS
的优点，推荐使用 Express + TypeScript 的朋友可以尝试使用 OvernightJS 咯~

