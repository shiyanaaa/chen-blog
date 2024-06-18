---
date: 2023-10-01
category:
  - SpringBoot
tag:
  - SpringBoot
  - Access
---

# SpringBoot 自定义权限管理注解

## 需求来源

在 SpringBoot 中如果要想实现接口的权限控制是一件很麻烦的时间，尝试使用自定义注解来进行权限控制。
<!-- more -->
## 解决设想


## 代码展示

```java
  @PostMapping("/auth/{code}")
  @Access(level = AccessLevel.LOGIN)
  public Result setAuth(HttpServletRequest request, @PathVariable("code") String code){
      User user = (User) request.getAttribute("user");
      String auth=request.getHeader("auth");
      return weixinService.setAuth(auth,user,code);
  }
```

通过自定义的@Access 注解，传入 level 表明当前接口访问的的权限  

通过拦截器将非法访问的记录拦截  

通过 request.getAttribute("user") 获取当前访问的用户信息

## 效果展示

