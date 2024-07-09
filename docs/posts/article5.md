---
date: 2024-05-06
category:
  - JavaScript
  - Vue
tag:
  - 技巧
---

# Vue中js回显操作

## 需求来源

在开发中，对于后台管理系统，很多表格选项可以配置选择选项，如配置菜系有“川菜”、“徽菜”等，添加菜品的时候可以选择菜系，选择一般储存为菜系id，但列表中显示时需要显示为菜系名称。
<!-- more -->
## 解决设想

菜系列表也为一个接口，菜品列表也为一个接口，大部分做法为在获取到菜品列表后，循环菜品列表与菜系列表，给菜品列表单位添加一个菜系名称字段。但此方法存在问题，菜系接口与菜品接口无法判断何时返回数据以及前后顺序，并且每次获取列表都需要进行双层循环。


所以选择将菜系列表进行循环转变为字典，转变为`typeMap={"id001":"川菜","id002":"徽菜",......}`，在Element Plus的table表格中，使用默认列插槽，`row`为当前行数据，`typeMap[row.typeId]`则为菜系名称。

## 代码展示

```html
<template>
  <el-table :data="data">
    <el-table-column  prop="name"  label="菜品名称">
    </el-table-column>
    <el-table-column  prop="typeId"  label="菜系名称">
      <template v-slot:default="{ row }">
        {{ typeMap[row.typeId] }}
      </template>
    </el-table-column>
  </el-table>
</template>
```

```javascript
<script setup>
const typeList=ref([])
const typeMap=computed(()=>{
  const map={}
  typeList.value.forEach(item=>{
    map[item.id]=item.name
  })
  return map;
})
</script>
```
