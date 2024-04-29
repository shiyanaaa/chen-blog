---
date: 2022-01-01
category:
  - SpringBoot
tag:
  - SpringBoot
  - Access
---

# SpringBoot 自定义权限管理注解
在SpringBoot中如果要想实现接口的权限控制是一件很麻烦的时间，于是可以使用自定义注解来进行权限控制。
## 1.注解的设计
  需要实现的效果为
  ```java
    @PostMapping("/auth/{code}")
    @Access(level = AccessLevel.LOGIN)
    public Result setAuth(HttpServletRequest request, @PathVariable("code") String code){
        User user = (User) request.getAttribute("user");
        String auth=request.getHeader("auth");
        return weixinService.setAuth(auth,user,code);
    }
  ```
  通过自定义的@Access注解，传入level表明当前接口访问的的权限  
  通过拦截器将非法访问的记录拦截  
  通过 request.getAttribute("user") 获取当前访问的用户信息  
## 2.拦截器的实现

Here is the content.
