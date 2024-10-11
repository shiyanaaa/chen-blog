---
date: 2024-07-02
category:
    - node.js
tag:
    - node.js
    - javascript
---
# Node.js学习备案

> 最近在深入学习并争取尽快掌握 ` Node.js ` 的技术细节，考虑开一篇文章用于记录需要记录下来的 **概念** 、 **方法** 以及
> **代码实例** ，方便在实际项目中进行查找。此篇会持续更新，或另开文章讨论更核心、关键的技术问题。

**这是一个通过` http ` 模块进行客户端和服务器端通信的基础例子，个人觉得很不错，虽然有些地方需要重构一下，先记录下来。 **
```js
    
    
    //Client
    var http = require('http');
    var qs = require('querystring');
    
    function send(theName) {
        http.request({
            host: '127.0.0.1',
            port: 3000,
            url: '/',
            method: 'POST'
        }, function (res) {
            res.setEncoding('utf8');
            res.on('end', function () {
                console.log('\nRequest completed!');
                process.stdout.write('\nyour name:')
            })
        }).end(qs.stringify({name: theName}));
    }
    
    process.stdout.write('\nyour name: ');
    process.stdin.resume();
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', function (name) {
        send(name.replace('\n', ''))
    });
    
    
    //Server
    var http = require('http');
    var qs = require('querystring');
    
    http.createServer(function (req, res) {
        var body = '';
        req.on('data', function (chunk) {
            body += chunk;
        });
        req.on('end', function () {
            res.writeHead(200);
            res.end('Done');
            console.log('\ngot name: ' + qs.parse(body).name + '\n');
        })
    }).listen(3000);
    console.log('Server is running on the port:3000');
    
    
    var http = require('http');
    var qs = require('querystring');
    http.createServer(function (req, res) {
        if ('/' === req.url) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.end([
                `<form method="POST" action="/url">
                <h1>My form</h1>
                <fieldset>
                    <label>Personal information</label>
                    <p>What is your name?</p>
                    <input type="text" name="name" placeholder="input your name">
                    <p><button>Submit</button></p>
                </fieldset>
            </form>`
            ].join(''));
        } else if ('/url' === req.url && 'POST' === req.method) {
            var body = '';
            req.on('data', function (chunk) {
                body += chunk;
            });
            req.on('end', function () {
                res.writeHead(200, {'Content-Type': 'text/html'});
                res.end('<b>Your name is <b>' + qs.parse(body).name + '</b></p>')
            })
        } else {
            res.writeHead(404);
            res.end('Not Found');
        }
    }).listen(3000);
    console.log('Server is running on the port:3000');

```