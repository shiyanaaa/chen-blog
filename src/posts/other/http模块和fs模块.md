---
date: 2023-06-27
category:
    - node.js
tag:
    - node.js
    - http
    - fs
    - javascript
---
 # http模块和fs模块
> 文章链接： [ http模块和fs模块 ]()

##  ` http ` 模块

` response ` 对象常用方法：

  1. ` response.writeHead(200,{'Content-Type':'text/plain:charset=UTF-8'}); `

此方法只能在消息上调用一次，并且必须在调用 ` response.end() ` 之前调用。

  1. ` response.write() ` 发送一块相应主体，用来给客户端发送相应数据。 ` write ` 可以使用多次，但是最后一定要使用 ` end ` 来结束响应，否则客户端会一直等待。 
  2. ` response.end() ` 此方法向服务器发出信号，表示已发送所有响应头和主体，该服务器应该视为此消息完成。必须在每个响应上调用方法 ` response.end() ` 。 

    
    
    const http = require('http');
    http.createServer(function(req, res) {
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write('hello world');
      res.write('<h1>hello node.js</h1>');
      res.end();
    }).listen(8080);
    console.log('Server running at http://127.0.0.1:8080');

**` request ` 对象 **

  1. ` request.url ` 获取请求路径，获取到的是端口号之后的那一部分路径，也就是说所有的 ` url ` 都是以 ` / ` 开头的，判断路径处理响应。 
  2. ` request.socket.localAddress ` 获取 ` ip ` 地址。 
  3. ` request.socket.remotePort ` 获取源端口。 

    
    
    const http = require('http');
    
    let server = http.createServer();
    server.on('request', function(req, res) {
      console.log('收到请求，请求路径是：' + req.url);
      console.log('请求我的客户端的地址是：', req.socket.remoteAddress, req.socket.remotePort);
      let url = req.url;
      res.writeHead(200, {'Content-Type': 'text/html;charset=UTF-8'});
      switch (url) {
        case '/':
          res.end('<h1>Index page</h1>');
          break;
        case '/login':
          res.end('<h1>Login page</h1>');
          break;
        default:
          res.end('404 Not Found.');
          break;
      }
    });
    server.listen(8080, function() {
      console.log('服务器启动成功，可以访问了。。。');
    });

##  ` fs ` 模块

所有文件系统操作都具有同步和异步的形式。异步方法中回调的第一个参数总是留给异常参数，如果方法成功完成，那么这个参数为 ` null ` 或 `
undefined ` 。

因为Node.js是单线程的，所以在Node.js中绝大部分需要在服务器运行期反复执行业务逻辑的代码，必须使用异步代码，否则，同步代码在执行期，服务器将停止响应。

服务器启动时如果需要读取配置文件，或结束时需要写入到状态文件时，可以使用同步代码，因为这些代码只在启动和结束时执行一次，不影响服务器正常运行时的异步执行。

**打开文件**

异步打开文件语法格式： ` fs.open(path,flags[mode],callback); `

参数说明：

  * ` path ` ：文件路径。 
  * ` flags ` ：文件打开的行为。 
  * ` mode ` ：设置文件模式（权限），文件创建默认权限为 ` 0o666 ` （可读写）。 
  * ` callback ` ：回调函数，带有两个参数： ` callback(err,fd) ` 。 

` flags ` 参数：

  * ` a ` \- 打开文件用于追加。如果文件不存在，则创建该文件。 
  * ` ax ` \- 与 ` a ` 相似，但如果路径存在则失败。 
  * ` a+ ` \- 打开文件用于读取和追加。如果文件不存在，则创建该文件。 
  * ` ax+ ` \- 与 ` a+ ` 相似，但如果路径存在则失败。 
  * ` as ` \- 以同步模式打开文件用于追加。如果文件不存在，则创建该文件。 
  * ` as+ ` \- 以同步模式打开文件用于读取和追加。如果文件不存在，则创建该文件。 
  * ` r ` \- 打开文件用于读取。如果文件不存在，则会发生异常。 
  * ` r+ ` \- 打开文件用于读取和写入。如果文件不存在，则会发生异常。 
  * ` rs+ ` \- 以同步模式打开文件用于读取和写入。指示操作系统绕开本地文件系统缓存。这对于在 ` NFS ` 挂载上打开文件非常有用，因为它允许跳过可能过时的本地缓存。 它对 ` I/O ` 性能有非常实际的影响，因此除非需要，否则不建议使用此标志。这不会将 ` fs.open() ` 或 ` fsPromises.open() ` 转换为同步的阻塞调用。 如果需要同步操作，则应使用 ` fs.openSync() ` 之类的操作。 
  * ` w ` \- 打开文件用于写入。创建文件（如果它不存在）或截断文件（如果存在）。 
  * ` wx ` \- 与 ` w ` 相似，但如果路径存在则失败。 
  * ` w+ ` \- 打开文件用于读取和写入。创建文件（如果它不存在）或截断文件（如果存在）。 
  * ` wx+ ` \- 与 ` w+ ` 相似，但如果路径存在则失败。 

    
    
    const fs = require('fs');
    
    fs.open('file/syl.txt', 'r+', function(err, fd) {
      if (err) {
        return console.error(err);
      }
      console.log('文件打开成功！');
    });

**关闭文件**

异步打开文件语法格式： ` fs.close(fs,callback); `

    
    
    const fs = require('fs');
    
    fs.open('file/syl.txt', 'r+', function(err, fd) {
      if (err) {
        return console.error(err);
      }
      console.log('文件打开成功！');
      fs.close(fd, function(err) {
        if (err) {
          console.log(err);
        }
        console.log('文件关闭成功');
      });
    });
    

###  使用 ` fs.read ` 和 ` fs.write ` 读写文件

使用 ` fs.read ` 和 ` fs.write ` 读写文件需要使用 ` fs.open ` 打开文件和 ` fs.close ` 关闭文件。

**使用` fs.read ` 读取文件 **

异步读取文件的语法格式： ` fs.read(fs,buffer,offset,length,position,callback) `

参数：

  * ` fd ` ：通过 ` fs.open() ` 方法返回的文件描述符。 
  * ` buffer ` ：数据写入的缓冲区。 
  * ` offset ` ：缓冲区中开始写入的偏移量。 
  * ` length ` ：一个整数，指定要读取的字节数。 
  * ` position ` ：指定从文件中开始读取的位置。如果 ` position ` 为 ` null ` ，则从当前文件位置读取数据，并更新文件位置。 
  * ` callback ` ：回调函数，有三个参数 ` err ` 、 ` bytesRead ` 、 ` buffer ` 。 

    
    
    const fs = require('fs');
    
    fs.open('file/syl.txt', 'r+', function(err, fd) {
      if (err) {
        return console.error(err);
      }
      console.log('文件打开成功！');
      console.log('准备读取文件：');
      // 创建一个大小为1024字节的缓存区
      let buf = Buffer.alloc(1024);
      // 异步读取文件
      fs.read(fd, buf, 0, buf.length, 0, function(err, bytes, buf) {
        if (err) {
          console.log(err);
        }
        console.log(bytes + '字节被读取');
        if (bytes > 0) {
          console.log(buf.slice(0, bytes).toString());
        }
        fs.close(fd, function(err) {
          if (err) {
            console.log(err);
          }
          console.log('文件关闭成功');
        });
      });
    });
    // 文件打开成功！
    // 准备读取文件：
    // 5字节被读取
    // Hello
    // 文件关闭成功

**使用` fs.write ` 写入文件 **

异步写入文件的语法格式： ` fs.write(fd,buffer,offset,length,position,callback); `

    
    
    const fs = require('fs');
    
    fs.open('file/syl.txt', 'a', function(err, fd) {
      if (err) {
        return console.error(err);
      }
      console.log('文件打开成功！');
      console.log('准备写入文件：');
      let buf = Buffer.from(new String('Hello World'));
      fs.write(fd, buf, 0, 11, 0, function(err, bytes, buf) {
        if (err) {
          console.log(err);
        }
        console.log('写入成功');
        console.log(bytes + '字节被写入');
        console.log(buf.slice(0, bytes).toString());
        fs.close(fd, function(err) {
          if (err) {
            console.log(err);
          }
          console.log('文件关闭成功');
        });
      });
    });
    // 文件打开成功！
    // 准备写入文件：
    // 写入成功
    // 11字节被写入
    // Hello World
    // 文件关闭成功
    

另外一种语法： ` fs.write(fd,string,position,encoding,callback); `

    
    
    const fs = require('fs');
    
    fs.open('file/syl.txt', 'a', function(err, fd) {
      if (err) {
        return console.error(err);
      }
      console.log('文件打开成功！');
      console.log('准备写入文件：');
      let data = ',Hello Node.js';
      fs.write(fd, data, 0, 'utf-8', function(err, bytes, buffer) {
        if (err) {
          console.log(err);
        }
        console.log(bytes + '字节被写入');
        console.log(buffer);
        fs.close(fd, function(err) {
          if (err) {
            console.log(err);
          }
          console.log('文件关闭成功');
        });
      });
    });
    // 文件打开成功！
    // 准备写入文件：
    // 14字节被写入
    // ,Hello Node.js
    // 文件关闭成功
    

` fs.read ` 和 ` fs.write ` 需要结合 ` fs.open ` 得到文件句柄来使用。

###  ` readFile ` 读取文件

语法格式： ` fs.readFile(path,[options],callback); `

参数：

  * ` path ` ：文件明或文件描述符。 
  * ` options ` ：该参数是一个对象，包含 ` {encoding,flag} ` 。 ` encoding ` 默认值为 ` null ` ， ` flag ` 默认值为 ` r ` 。 

第一种方式：

    
    
    const fs = require('fs');
    
    fs.readFile('file/syl.txt', 'utf-8', function(err, data) {
      if (err) {
        throw  err;
      }
      console.log(data);
    });
    

第二种方式：

    
    
    fs.readFile('file/syl.txt', function(err, data) {
      if (err) {
        throw  err;
      }
      console.log(data.toString());
    });
    

###  ` writeFile ` 写入文件

语法格式： ` fs.writeFile(file,data,[options],callback); `

    
    
    const fs = require('fs');
    
    fs.writeFile('file/syl.txt', '我是新写入的内容', function(err) {
      if (err) {
        throw  err;
      }
      console.log('已保存');
      fs.readFile('file/syl.txt', 'utf-8', function(err, data) {
        if (err) {
          throw err;
        }
        console.log(data);
      });
    });
    // 已保存
    // 我是新写入的内容
    

我们可以通过设置 ` flag ` 的值，来改变默认的写入方式，比如设置为 ` a ` 追加数据到文件中。

    
    
    fs.writeFile('file/syl.txt', '我是新写入的内容', {'flag': 'a'}, function(err) {
      if (err) {
        throw  err;
      }
      console.log('已保存');
      fs.readFile('file/syl.txt', 'utf-8', function(err, data) {
        if (err) {
          throw err;
        }
        console.log(data);
      });
    });
    

###  获取文件信息

语法格式： ` fs.stat(path,callback); `

不建议在调用 ` fs.open() ` 、 ` fs.readFile() ` 或 ` fs.writeFile() ` 之前使用 ` fs.stat()
` 检查文件是否存在。而是应该直接打开、读取或写入文件，并在文件不可用时处理引发的错误。

` fs.stat(path) ` 执行后，会将 ` stats ` 类的实例返回给其回调函数。可以通过 ` stats `
类中的提供方法判断文件的相关属性。

    
    
    const fs = require('fs');
    
    fs.stat('file/syl.txt', function(err, stats) {
      console.log(stats.isFile());
    });
    // true
    

###  截取文件

语法格式： ` fs.ftruncate(fd,len,callback); `

    
    
    const fs = require('fs');
    
    fs.open('file/syl.txt', 'r+', function(err, fd) {
      if (err) {
        return console.error(err);
      }
      console.log('文件打开成功');
      console.log('截取6字节内的文件内容，超出部分将被去除。');
      // 截取文件
      let buf = Buffer.alloc(1024);
      fs.ftruncate(fd, 6, function(err) {
        if (err) {
          console.log(err);
        }
        console.log('文件截取成功。');
        console.log('读取相同的文件');
        fs.read(fd, buf, 0, buf.length, 0, function(err, bytes) {
          if (err) {
            console.log(err);
          }
          if (bytes > 0) {
            console.log(buf.slice(0, bytes).toString());
          }
    
          fs.close(fd, function(err) {
            if (err) {
              console.log(err);
            }
            console.log('文件关闭成功！');
          });
        });
      });
    });
    

###  删除文件

    
    
    fs.unlink('file/syl.txt', function(err) {
      if (err) {
        return console.error(err);
      }
      console.log('文件删除成功！');
    });
    

###  修改文件名

语法格式： ` fs.rename(oldPath,newPath,callback); `

    
    
    fs.rename('file/old.txt', 'file/new.txt', err => {
      if (err) throw err;
      console.log('重命名完成');
    });
    

###  目录操作

**新建目录**

语法格式： ` fs.mkdir(path,callback); `

    
    
    fs.mkdir('./test/', function(err) {
      if (err) {
        return console.error(err);
      }
      console.log('目录创建成功。');
    });
    

**读取目录**

语法格式： ` fs.readdir(path,callback); `

    
    
    fs.readdir('./test', function(err, files) {
      if (err) {
        throw err;
      }
      console.log(files);
    });
    

**删除目录**

语法格式： ` fs.rmdir(path,callback); `

只能删除空目录。

    
    
    fs.rmdir('./test', function(err) {
      if (err) {
        return console.error(err);
      }
    });    

