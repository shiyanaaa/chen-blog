---
date: 2024-05-05
category:
    - react.js
tag:
    - react.js
    - jsx
    - ecmascript-6
    - webpack
---
 # Webpack 配置 React 开发环境
##  Webpack 配置 React 开发环境

> 先完成基本的配置项，后面在根据项目的复杂度加入更多的配置内容和技巧

` Webpack ` 是一个前端资源加载/打包工具，只需要相对简单的配置就可以提供前端工程化需要的各种功能，并且如果有需要它还可以被整合到其他比如 `
Grunt / Gulp ` 的工作流。

安装 **Webpack** ： ` npm install -g webpack `

` Webpack ` 使用一个名为 ` webpack.config.js ` 的配置文件，要编译 ` JSX ` ，先安装对应的 **loader**
: ` npm install babel-loader --save-dev `

假设我们在当前工程目录有一个入口文件 ` entry.js ` ， **React** 组件放置在一个 ` components/ ` 目录下，组件被 `
entry.js ` 引用，要使用 ` entry.js ` ，我们把这个文件指定输出到 ` dist/bundle.js ` ， **Webpack**
配置如下：

    
    
    var path = require('path');
    
    module.exports = {
        entry: './entry.js',
        output: {
            path: path.join(__dirname, '/dist'),
            filename: 'bundle.js'
        },
        resolve: {
            extensions: ['', '.js', '.jsx']
        },
        module: {
            loaders: [
                { test: /\.js|jsx$/, loaders: ['babel'] }
            ]
        }
    }
    

` resolve ` 指定可以被 ` import ` 的文件后缀。比如 ` Hello.jsx ` 这样的文件就可以直接用 ` import Hello
from 'Hello' ` 引用。

` loaders ` 指定 ` babel-loader ` 编译后缀名为 ` .js ` 或者 ` .jsx `
的文件，这样你就可以在这两种类型的文件中自由使用 ` JSX ` 和 ` ES6 ` 了。

监听编译: ` webpack -d --watch `

> 代码分片，把代码按照特定的形式进行拆分，使应用不必一次全部加载，实现按需加载 [ SplitChunksPlugin ]()
    
    
    module.exports = {
      optimization: {
        spliteChunks: {
          cacheGroups: {
            vendors: {
              name: "vendors",
              chunks: "all"
            }
          }
        }
      }
    };
    
    
    const HtmlWebpackPlugin = require("html-webpack-plugin");
    
    module.exports = {
      plugins: [
        new HtmlWebpackPlugin()
      ]
    };
    
    
    module.exports = {
      devServer: {
        contentBase: path.join(__dirname + "dist"),
        compress: true,
        port: 8000
      }
    };

> 浏览器缓存，解决打包后依旧使用缓存，使用 ` Hash ` 值作为版本标识添加在文件名中
    
    
    module.exports = {
      output: {
        filename: "[name].bundle.[chunkhash].js",
        path: path.resolve(__dirname, "dist")
      }
    };

> 资源压缩， ` webpack ` 在生产环境下会自动开启压缩
    
    
    module.exports = {
      optimization: {
        minmize: true
      }
    };

> 为了提升打包性能， ` webpack ` 引入了 ` HappyPack `
> ，它的作用是将文件解析任务分解成多个子进程并发执行，子进程处理完任务后再将结果发送给主进程。 ` HappyPack ` 只是作用在 ` loader
> ` 加载器上，使用多个进程同时对文件进行编译
    
    
    module.exports = {
      module: {
        rules: [
          {
            test: /\.css$/,
            use: "happypack/loader?id=styles"
          }
        ]
      },
      plugin: [
        new HtmlWebpackPlugin(),
        new HappyPack({
          id: "styles",
          loaders: ["style-loader", "css-loader"]
        })
      ]
    };

> 动态链接库 ` DllPlugin ` ，将第三方和不常修改的模块预先编译和打包，然后在项目打包时直接使用提前打包的模块库即可  
>  动态链接库配置文件 ` webpack.dll.config.js `
    
    
    const path = require("path");
    const webpack = require("webpack");
    const dllAssetPath = path.join(__dirname, "dll");
    const dllLibraryName = "dllExample";
    
    module.exports = {
      entry: ['lodash'],
      output: {
        path: dllAssetPath,
        filename: "vendor.js",
        library: dllLibraryName
      },
      plugin: [
        new webpack.DllPlugin({
          name: dllLibraryName,
          path: path.join(dllAssetPath, "manifest.json")
        })
      ]
    };
    
    
      "scripts": {
        "dll": "webpack --config=webpack.dll.config.js"
      },
    
    
    const path = require("path");
    const HtmlWebpackPlugin = require("html-webpack-plugin");
    const HappyPack = require("happypack");
    const webpack = require("webpack");
    const AddAssetHtmlPlugin = require("add-asset-html-plugin");
    
    module.exports = {
      plugin: [
        new HtmlWebpackPlugin(),
        new AddAssetHtmlPlugin([{
          filePath: path.resolve(__dirname, "./dll/vendor.js")
        }]),
        new HappyPack({
          id: "styles",
          loaders: ["style-loader", "css-loader"]
        }),
        new webpack.DllReferencePlugin({
          manifest: require(path.join(__dirname, "./dll/manifest.json"))
        })
      ]
    };

> 打包完成后，还需要对打包输出的结果进行检查和分析。使用 ` webpack-bundle-analyzer ` 依赖库查看项目各模块的大小，以按需优化
    
    
    module.exports = {
      plugin: [
        new HtmlWebpackPlugin(),
        new BundleAnalyzerPlugin({
          analyzerPort: 9000
        })
      ]
    };
    
    
      "scripts": {
        "analyze": "webpack --config webpacl-dev.config.js --progress"
      },

