---
date: 2023-07-04
category:
    - javascript
tag:
    - javascript
    - css
---
 # CSS + JS 送学妹满屏幕小爱心
##  故事开始

午饭时间，暗恋已久的学妹拉着我的衣袖：“学长学长，你能不能让这些爱心变成五颜六色的吗~”。  
  
  
我在旁边笑开了花~~~  

  
  
  
诶呀，口水流出来了。  
  
  
我想最终效果是这样的（猜猜多少个爱心）：

然后开始动手吧~  

[ ]()

##  学啥本领

本文将带大家学习两个好东西：  
1.生成随机色的方法；  
2.Element.animate() 方法。  
  
  
当然，还有撩妹技巧了~  

[ ]()

##  代码走起

[ ]()

###  1\. 画个小爱心

  
爱心怎么画，不是咱们本文重点，so，SVG搞起：

    
    
    <div id="heart">
      <svg t="1587910011145" class="icon" viewBox="0 0 1024 1024" version="1.1" 
           xmlns="http://www.w3.org/2000/svg" p-id="1253" width="32" height="32"
      >
        <path d="M677.51936 192.03072c113.1008 0 204.8 91.6992 204.8 204.77952 0 
                 186.91072-370.3296 435.15904-370.3296 435.15904S141.68064 592.67072 141.68064 
                 396.81024c0-140.78976 91.6992-204.77952 204.77952-204.77952 68.11648 0 
                 128.28672 33.40288 165.5296 84.55168C549.24288 225.4336 609.41312 192.03072 
                 677.51936 192.03072z" p-id="1254"
        ></path>
      </svg>
    </div>

小爱心出来了：  

###  2\. 画一大堆爱心

现在删除到之前的 SVG 标签，换成动态生成咯~~

    
    
    let heartList = '';
    const n = 99;
    for(let i = 0; i <= n; i++){
        heartList += `
          <svg t="1587910011145" class="icon" viewBox="0 0 1024 1024" version="1.1" 
               xmlns="http://www.w3.org/2000/svg" p-id="1253" width="32" height="32">
            <path d="M677.51936 192.03072c113.1008 0 204.8 91.6992 204.8 204.77952 0 
                     186.91072-370.3296 435.15904-370.3296 435.15904S141.68064 592.67072 141.68064 
                     396.81024c0-140.78976 91.6992-204.77952 204.77952-204.77952 68.11648 0 
                     128.28672 33.40288 165.5296 84.55168C549.24288 225.4336 609.41312 192.03072 
                     677.51936 192.03072z" p-id="1254"
            ></path>
          </svg>
        `
    }
    document.getElementById('heart').innerHTML = heartList;

一大堆小爱心出现啦：  
  

[ ]()

###  3\. 打造魔法棒

接下来我们要打造一把魔法棒，能让我们这些小爱心变成各种各样的颜色。  
没错，这把魔法棒，就是用来生成随机颜色。  
  
  
方法很多，我搜集以下几种简单好用的生成随机颜色的方法，基本我们业务随便一个都能用：  

    
    
    function getRandomColor(){
        const r = Math.floor(Math.random()*255);
        const g = Math.floor(Math.random()*255);
        const b = Math.floor(Math.random()*255);
        return 'rgba('+ r +','+ g +','+ b +',0.8)';
    }
    
    function getRandomColor(){
        return '#'+Math.floor(Math.random()*16777215).toString(16);
    }
    
    function getRandomColor(){
        return '#' + (function(color){    
            return (color +=  '0123456789abcdef'[Math.floor(Math.random()*16)])    
            && (color.length == 6) ?  color : arguments.callee(color);    
        })('');
    }
    
    function getRandomColor(){
        return '#'+'0123456789abcdef'.split('').map(
            (v,i,a) => i>5 ? null : a[Math.floor(Math.random()*16)] 
        ).join('');
    }
    
    function getRandomColor(){
        return '#'+('00000'+(Math.random()*0x1000000<<0).toString(16)).slice(-6);
    }
    
    function getRandomColor(){
        const colorAngle = Math.floor(Math.random()*360);
        return 'hsla('+ colorAngle +',100%,50%,1)';
    }
    
    function getRandomColor(){
        return (function(m,s,c){
            return (c ? arguments.callee(m,s,c-1) : '#') +
            s[m.floor(m.random() * 16)]
        })(Math,'0123456789abcdef',5)
    }

随机色真好玩~  

[ ]()

###  4\. 五颜六色！变~

最后，我们修改前面 SVG 的代码片段，加入 ` getRandomColor ` 方法的调用：  

    
    
    for(let i = 0; i <= n; i++){
        heartList += `
          <svg t="1587910011145" class="icon" viewBox="0 0 1024 1024" version="1.1" 
               xmlns="http://www.w3.org/2000/svg" p-id="1253" width="32" height="32"
                         fill="${getRandomColor()}"
                >
            <path d="M677.51936 192.03072c113.1008 0 204.8 91.6992 204.8 204.77952 0 
                     186.91072-370.3296 435.15904-370.3296 435.15904S141.68064 592.67072 141.68064 
                     396.81024c0-140.78976 91.6992-204.77952 204.77952-204.77952 68.11648 0 
                     128.28672 33.40288 165.5296 84.55168C549.24288 225.4336 609.41312 192.03072 
                     677.51936 192.03072z" p-id="1254"
            ></path>
          </svg>
        `
    }

99 个小爱心，水灵灵的！  

###  5\. 动起来吧！

这时候，每个爱心都静静躺着页面，是时候让它们动起来啦，为了学妹~  
  
  
继续改造前面 SVG 代码，为每个 SVG 标签添加连续 ID 值：

    
    
    for(let i = 0; i <= n; i++){
        heartList += `
          <svg id="heart_${i}" t="1587910011145" class="icon" viewBox="0 0 1024 1024" version="1.1" 
               xmlns="http://www.w3.org/2000/svg" p-id="1253" width="32" height="32"
                         fill="${getRandomColor()}"
                >
            <path d="M677.51936 192.03072c113.1008 0 204.8 91.6992 204.8 204.77952 0 
                     186.91072-370.3296 435.15904-370.3296 435.15904S141.68064 592.67072 141.68064 
                     396.81024c0-140.78976 91.6992-204.77952 204.77952-204.77952 68.11648 0 
                     128.28672 33.40288 165.5296 84.55168C549.24288 225.4336 609.41312 192.03072 
                     677.51936 192.03072z" p-id="1254"
            ></path>
          </svg>
        `
    }

生命随机放大倍数，并设置动画效果：

    
    
    let getRandomNum = () => Math.floor(Math.random()*2+1);
    setTimeout(function(){
        for (let i = 0; i <= n; i++) {
            const item = `heart_${i}`;
            document.getElementById(item).animate([
                // keyframes translateY(0px)
                { transform: `scale(${getRandomNum()})` },
                { transform: `scale(${getRandomNum()})` },
                { transform: `scale(${getRandomNum()})` },
                { transform: `scale(${getRandomNum()})` },
                { transform: `scale(${getRandomNum()})` },
                { transform: `scale(${getRandomNum()})` },
            ], {
                // timing options
                duration: 5000,
                iterations: Infinity
            });
        }
    }, 100)

然后，小爱心们动起来啦。  

###  6\. 飞起来吧~

  
接下来，要让这些小爱心飞起来~  

  
  
下面贴代码。

    
    
    html,body{
        overflow: hidden;
        width: 100%;
        height: 100%;
        margin: 0;
    }
    #heart{
        position: relative;
    }
    .item{
        position: absolute;
    }

逻辑修改：

    
    
    let heartList = ''; 
    const n = 666; // 总爱心数
    // 生成随机颜色
    function getRandomColor() {
        return (function (m, s, c) {
            return (c ? arguments.callee(m, s, c - 1) : '#') +
                s[m.floor(m.random() * 16)]
        })(Math, '0123456789abcdef', 5)
    }
    // 生成爱心列表
    for(let i = 0; i <= n; i++){
        heartList += `
          <svg id="heart_${i}" class="item" t="1587910011145" class="icon" viewBox="0 0 1024 1024" version="1.1" 
               xmlns="http://www.w3.org/2000/svg" p-id="1253" width="32" height="32"
                         fill="${getRandomColor()}"
                >
            <path d="M677.51936 192.03072c113.1008 0 204.8 91.6992 204.8 204.77952 0 
                     186.91072-370.3296 435.15904-370.3296 435.15904S141.68064 592.67072 141.68064 
                     396.81024c0-140.78976 91.6992-204.77952 204.77952-204.77952 68.11648 0 
                     128.28672 33.40288 165.5296 84.55168C549.24288 225.4336 609.41312 192.03072 
                     677.51936 192.03072z" p-id="1254"
            ></path>
          </svg>
        `
    }
    // 随机放大倍数
    const getRandomNum = (scale) => Math.floor(Math.random()*scale+1);
    const boxWidth = window.innerWidth;
    const boxHeight = window.innerHeight;
    setTimeout(function(){
        for (let i = 0; i <= n; i++) {
            const item = `heart_${i}`;
            const width = getRandomNum(boxWidth);
            const height = getRandomNum(boxHeight);
            const cWidth = getRandomNum(1000) - width;
            const cHeight = getRandomNum(1000) - height;
            document.getElementById(item).animate([
                { transform: `scale(${getRandomNum(2)})`,left: `0px`, top: `0px` },
                { transform: `scale(${getRandomNum(2)})`,left: `${boxWidth/2}px`, top: `${boxHeight/2}px` },
                { transform: `scale(${getRandomNum(2)})`,left: `${cWidth * 2}px`, top: `${cHeight * 2}px` },
            ], {
                duration: 9000,
                iterations: Infinity,
                easing: 'ease-in-out'
            });
        }
    }, 100)
    document.getElementById('heart').innerHTML = heartList;

聪明的你，再配上BGM，浪漫~  
  
  
还能做更多有意思的小玩意，靠各位发挥啦。  

[ ]()

##  故事结束

继续~  
  
  
对了，送给学妹的代码我放在仓库：  
[ https://github.com/pingan8787/Leo-JavaScript/blob/master/Leo-
Demo/7-WeiteHeartPop.html ]()

