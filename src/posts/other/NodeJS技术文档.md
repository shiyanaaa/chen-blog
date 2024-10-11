---
date: 2023-10-02
category:
    - node.js
tag:
    - node.js
    - npm
---
 # NodeJS技术文档
命令  |  说明   
---|---  
` npm init [-y] ` |  初始化一个 ` package.json ` 文件   
` npm install ` 包名  |  安装一个包   
` npm install --save/-S ` 包名  |  将安装的包添加到 ` package.json ` 的依赖中   
` npm install -g ` 包名  |  安装一个命令行工具   
` npm docs ` 包名  |  查看包的文档（非常有用）   
` npm root -g ` |  查看全局包安装路径   
` npm config set prefix ` "路径"  |  修改全局包安装路径   
` npm list ` |  查看当前目录下安装的所有包   
` npm list -g ` |  查看全局包的安装路径下所有的包   
` npm uninstall ` 包名  |  卸载当前目录下某个包   
` npm uninstall -g ` 包名  |  卸载全局安装路径下某个包   
` npm update ` 包名  |  更新当前目录下某个包   
参数  |  说明   
---|---  
` file ` |  文件名或文件描述符   
` data ` |  要写入文件的数据，可以是 ` String ` （字符串）或 ` Buffer ` （流）对象   
` options ` |  该参数是一个对象，包含 ` {encoding,mode,flag} ` 。默认编码为 ` utf8 ` ，模式为 ` 0o666 ` ， ` flag ` 为 ` 'w' `  
` callback ` |  回调函数，只包含错误信息参数 ` (err) ` ，在写入失败是返回   
flag  |  说明   
---|---  
` r ` |  文件名或文件描述符   
` r+ ` |  打开文件进行读取和写入，如果该文件不存在则发生异常   
` rs ` |  打开文件，用于读取在同步方式   
` rs+ ` |  打开文件进行读取和写入，告诉 ` OS ` 同步地打开它   
` w ` |  打开文件进行写入。该文件被创建（如果它不存在）或截断（如果它存在）   
` wx ` |  类似 ` w ` ，如果路径存在则失败   
` w+ ` |  打开文件进行读取和写入。该文件被创建（如果不存在）或截断（如果存在）   
` wx+ ` |  类似 ` w+ ` ，但如果路径存在则失败   
` a ` |  打开文件进行追加。如果它不存在，则创建该文件   
` ax ` |  类似 ` a ` ，但如果路径存在则失败   
` a+ ` |  打开文件进行读取和附加。如果它不存在，则创建该文件   
` ax+ ` |  类似 ` a+ ` ，但如果路径存在则失败   
  
> 在进行文件操作时，如果是同步 ` API ` ，必须使用 ` try...catch ` 来捕获异常，防止程序因为异常退出，导致后续代码无法继续执行。

函数（ ` stats ` ）  |  说明   
---|---  
` stats.isFile() ` |  如果是文件返回 ` true ` ，否则返回 ` false `  
` stats.isDirectory() ` |  如果是目录返回 ` true ` ，否则返回 ` false `  
` stats.isBlockDevice() ` |  如果是块设备返回 ` true ` ，否则返回 ` false `  
` stats.isCharacterDevice() ` |  如果是字符设备返回 ` true ` ，否则返回 ` false `  
` stats.isSymbolicLink() ` |  如果是软链接返回 ` true ` ，否则返回 ` false `  
` stats.isFIFO() ` |  如果是 ` FIFO ` 返回 ` true ` ，否则返回 ` false ` 。 ` FIFO ` 是 ` UNIX ` 中的一种特殊类型的命令管道   
` stats.isSocket() ` |  如果是 ` Socket ` 返回 ` true ` ，否则返回 ` false `  
函数（ ` path ` ）  |  说明   
---|---  
` basename(p[,ext]) ` |  获取文件名   
` dirname(p) ` |  获取文件目录   
` extname(p) ` |  获取文件扩展名   
` isAbsolute(path) ` |  判断是否是绝对路径   
` join([path1][,path2][,...]) ` |  拼接路径字符串   
` normalize(p) ` |  将非标准路径转换为标准路径   
` sep ` |  获取操作系统的文件路径分隔符   
分层  |  说明   
---|---  
应用层  |  协议有 ` HTTP ` 、 ` FTP ` 、 ` SMTP ` 等   
表示层  |  ` ASCII ` 码、 ` JPEG ` 、 ` MPEG ` 和 ` WAV ` 等文件转换   
会话层  |  负责访问次序的安排等   
传输层  |  协议有 ` TCP ` 、 ` UDP ` 等   
网络层  |  三层交换机、路由器灯属于此层，协议有 ` IP ` 、 ` SPX `  
数据链路层  |  二层交换机、网桥和网卡等属于此层   
物理层  |  集线器、中继器和传输线路属于此层   
  
> 无连接：无连接的含义是限制每次连接只处理一个请求。服务器处理外客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间。  
>  无状态： ` HTTP `
> 协议是无状态协议。无状态是指协议处于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息是它的应答就较快。

###  事件循环 ` Event Loop `

