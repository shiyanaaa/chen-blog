---
date: 2024-07-09
category:
  - JavaScript
tag:
  - 技巧
  - Vue3
---

# 大量数据插入解决卡顿

## 函数介绍

这是一个用于处理数据的函数，主要用途是在空闲时间内逐步处理数据的插入操作，防止页面渲染大量数据卡顿。

## 函数定义

```javascript
const setDataHandle=(data, value, index: number, resolve, reject)=> {
  requestIdleCallback((idle) => {
    if (index !== data.value.length) {
      reject(null);
      return;
    }
    if (value.length > index) {
      if (idle.timeRemaining() > 0) {
        data.value.push(value[index]);
        setDataHandle(data, value, index + 1, resolve, reject);
      } else {
        setDataHandle(data, value, index, resolve, reject);
      }
    } else {
      resolve(null);
      return;
    }
  });
}
export const setData=(data, value)=> {
  return new Promise((resolve,reject)=>{
    data.value = []
    setDataHandle(data,value,0,resolve,reject)
  })
}
```

## 函数使用

```javascript

const data=ref([])
const getData=(list)=>{
  setData(data,list).then(res=>{
    console.log("添加完成")
  })
}
```
