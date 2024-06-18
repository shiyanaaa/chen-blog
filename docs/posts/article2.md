---
date: 2024-5-14
category:
  - Vue
tag:
  - 技巧
---

# 右击菜单的封装

## 需求来源

在开发中，需要开发一个右击菜单，经过多次设想，需要考虑因素很多，如边界右击菜单会超出屏幕，以及需求中有二级菜单甚至三级菜单的设计。

## 解决设想

快速简单的实现一个右击菜单，经过思考，想到了ElementPlus中的`Cascader`级联选择器组件
![Cascader组件](/images/article2/Cascader.png)

如果把顶部输入框与箭头隐藏，在右击时使用组件函数`togglePopperVisible`来调出下拉组件，不仅有下拉动画，而且还有边界判定防遮挡，并且二三级菜单也可以同时完成，且还有失焦自动收回，完美符合需求。

## 代码展示

```javascript
<template>
  <div class="context-menu" :style="styles">
    <el-cascader
      popper-class="menu-popper"
      ref="cascaderRef"
      class="menu"
      v-model="value"
      :options="props.menuList"
      @change="handleChange"
      :popper-append-to-body="false"
    >
      <template v-slot="{ node, data }" >
        <el-icon style="vertical-align: middle;margin-right: 8px;"  v-if="data.icon" >
          <component :is="data.icon"></component>
        </el-icon>
        <span :class="{chose:choseMenu.includes(data.value)}">
          {{ data.label }}
        </span>
      </template>
    </el-cascader>
  </div>
</template>

<script setup>
import { computed,inject } from 'vue';
const cascaderRef = ref();
const emit = defineEmits(['change']);
const choseMenu=inject('chose-menu')
const props = defineProps({
  menuList: {
    type: Array,
    default: () => [],
  },
  position: {
    type: Object,
    default: () => {},
  },
});
const value = computed({
  get() {
    return '';
  },
  set(val) {
    emit('change', val);
  },
});
const styles = computed(() => {
  const res = {};
  if (props.position) {
    res['left'] = `${props.position.x}px`;
    res['top'] = `${props.position.y}px`;
  }
  return res;
});
const show = () => {
  cascaderRef.value.cascaderPanelRef.clearCheckedNodes();
  cascaderRef.value.togglePopperVisible(true);
};
defineExpose({ show });
</script>

<style lang="scss" scoped>
.context-menu {
  position: absolute;
  top: 0;
  left: 0;
  width: 0;
  height: 0;
  :deep(.el-cascader) {
    transform: translateY(-20px) translateX(-10px);
    width: 0;
    height: 0;
    overflow: hidden;
    display: block;
  }
}
</style>
```

使用中

```javascript
<ContextMenu
  ref="menuRef"
  v-show="showMenu"
  :position="menuPosition"
  :menuList="menuList"
  @change="FileEdit"
/>
```

## 效果展示

![Cascader组件](/images/article2/demo1.png)

![Cascader组件](/images/article2/demo2.png)

![Cascader组件](/images/article2/demo3.png)
