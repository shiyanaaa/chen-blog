---
date: 2023-03-26
category:
    - 前端
tag:
    - 前端
    - react.js
    - react-native
    - android
    - ios
---
 # 使用React Native构建App
> 原文地址： [ 使用React Native构建App ]()
>
> 最近因为项目需要，深入研究 ` React ` 和 ` React Native ` ， ` React ` 已经掌握得差不多了，现在集中精力在 `
> ReactNative ` 的项目开发。这里需要记录在学习过程中的技术细节，好记性真的不如烂笔头，多写文档总会有好处的。[坑太多，一个个填]
>
> 本文重点记录使用 ` React Native ` 构建双平台 ` App ` 的过程，同时进一步掌握构建过程中运用的技术。【持续更新，坚持不懈...】

##  搭建开发环境

**安装` react-native-cli ` ** ： ` npm i -g react-native-cli `

###  Android SDK

安装Android SDK并启动进行配置：

**配置环境变量**

    
    
    export ANDROID_HOME=~/Library/Android/sdk
    export PATH=${PATH}:${ANDROID_HOME}/tools
    export PATH=${PATH}:${ANDROID_HOME}/platform-tools

###  Android 虚拟机

设定 [ Genymotion ]() 的Android SDK 位置（Android SDK 的路径可以在 SDK Manager 上找到）。

###  模拟器

有多款模拟器可供选择，Android Studio自带，Genymotion和夜神模拟器，推荐选择夜神模拟器。

**配置方法：**

  1. 在 ` Nox/bin ` 目录运行 ` nox_adb.exe connect 127.0.0.1:62001 ` ，如果失败，使用 ` adb devices ` 查询，出现版本不一致的情况，可以把 ` Android/sdk ` 目录下的 ` adb.exe ` 拷贝到 ` Nox/bin ` 下，并改名为 ` nox_adb.exe ` ，反过来操作也是可以的。 
  2. 分别打开Android Studio和夜神模拟器，此时运行命令 ` nox_adb.exe connect 127.0.0.1:62001 ` 基本上都会成功。 

##  新建React Native项目

  1. 运行 ` react-native init project-name ` ，进入 ` project-name ` 文件夹安装依赖 ` npm i ` 并运行 ` react-native run-android ` 或 ` react-native run-ios ` 构建 ` App ` 。 
  2. 以Android App为例，在Android Studio打开 ` Android ` 文件夹（ **注意：此处是` Android ` 文件夹，不是 ` project-name ` 项目文件夹 ** ）。 
  3. 在 ` C:\Users\user\.gradle\wrapper\dists ` 目录下放入对应文件，文件下载地址 [ Gradle ]()

  
  

##  运行项目

  1. **这一步很关键** ，配置java的环境变量，首先是 **JAVA_HOME** 和 **ANDROID_HOME** ： 

    1. **JAVA_HOME** ，变量值为 ` D:\Android\sdk ` ； 
    2. **ANDROID_HOME** ，变量值为 ` D:\Android\sdk ` ； 
    3. 然后在 ` Path ` 项中添加 ` jdk ` 和 ` jre ` 下的 ` bin ` 目录； 
    4. 以上是用户变量配置，下面进行系统变量配置： 

       * 在 ` Path ` 项中添加下图中变量： 

  1. 同时打开Android Studio、Nox并在AS中打开项目中的 ` Android ` 文件夹。 
  2. 运行 ` nox_adb.exe connect 127.0.0.1:62001 ` 连接AS和Nox，然后再运行 ` react-native run-android ` ，此时就会构建Android App， 

> 关闭端口冲突： ` lsof -n -i4TCP:8081 ` ， ` kill -9 <PID> `

