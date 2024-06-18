---
date: 2024-05-11
category:
  - Vue
  - Vue3
tag:
  - 技巧
---

# 封装Vue3中自动loading响应式

## 需求来源

在开发中，在一个现成的项目中需要把每个页面表单的添加与修改按钮加上loading，防止多次点击多次提交表单，如果每个都写一个loading，并且在接口事件处理中进行loading状态的控制，将会很麻烦，所以寻求一个通用解决方案。

## 解决设想

接口的本质是一个promise，可不可以通过劫持promise来进行loading状态的更改，添加一个通用的辅助函数，从其中结构出一个loading响应式，一个函数，把每个接口函数包裹达到自动更新loading状态值。

## 代码展示

tools.js内代码

```javascript
import { ref } from 'vue'
export function usePromiseWithLoading() {
  const loading = ref(false)
  const useLoading = (promise) => {
    loading.value = true
    promise.finally(() => {
      loading.value = false;
    })
    return promise
  }
  return [
    loading,
    useLoading
  ]
}
```

使用中

```javascript
<template>
    <el-button @click="getList" :loading="loading">
        提交
    </el-button>
</template>
<script>
import { getListApi } from '@/api/user'
import {usePromiseWithLoading} from '@/utils/tools'
const [ loading ,useLoading ]=usePromiseWithLoading()

const getList=()=>{
    //使用useLoading对接口进行包裹
    useLoading(getListApi()).then(res=>{
        console.log(res)
    })
}
</script>
```

## 问题解释

为何usePromiseWithLoading返回数组而不是对象，如果使用对象返回,在一个组件内有多个loading效果的时候略嫌麻烦

```javascript
//对象方式
const { loading,useLoading }=usePromiseWithLoading()
const { loading as loading1,useLoading as useLoading1 }=usePromiseWithLoading()
//数组方式
const [ loading,useLoading ]=usePromiseWithLoading()
const [ loading1,useLoading1 ]=usePromiseWithLoading()
```
