---
date: 2023-10-05
category:
    - vue.js
tag:
    - vue.js
    - vue-router
    - vuex
    - javascript
    - 前端
---
 # Vue.js路由与Vuex数据模型设计
###  路由设计

本则路由考虑验证进入登录页面，完成登录操作进入首页。  
**router/router.js**

    
    
    import Vue from "vue";
    import Router from "vue-router";
    Vue.use(Router);
    
    import store from "@/store/store";
    
    // (延迟加载)
    const Login = () => import("@/views/login");
    const Home = () => import("@/views/home");
    
    const HomeRoute = {
      path: "/",
      name: "首页",
      component: Home
    };
    
    export { HomeRoute };
    
    const router = new Router({
      base: process.env.BASE_URL,
      routes: [
        {
          path: "/login",
          name: "登录",
          component: Login
        },
        HomeRoute
      ]
    });
    
    router.beforeEach((to, from, next) => {
      let loginName = store.state.user.loginName;
      if (to.path === "/" && loginName == "") {
        next("/login");
      } else {
        next();
      }
    });
    
    export default router;

**vue.config.js**

    
    
    let path = require("path");
    
    module.exports = {
      chainWebpack: config => {
        config.resolve.alias.set("@", path.join(__dirname, "src"));
        config.resolve.symlinks(true);
      },
      publicPath: "./",
      devServer: {
        proxy: {
          "/api": {
            target: "http://jsonplaceholder.typicode.com/",
            ws: true,
            changeOrigin: true,
            pathRewrite: {
              "^/api": "/"
            }
          }
        }
      }
    };

###  构造请求实例

**utils/cookie.js**

    
    
    import Cookies from "js-cookie";
    
    export function getCookie(key) {
      return Cookies.get(key);
    }
    
    export function setCookie(key, val) {
      return Cookies.set(key, val);
    }
    
    export function removeCookie(key) {
      return Cookies.remove(key);
    }
    
    export function getToken() {
      return Cookies.get("XY_TOKEN");
    }
    
    export function setToken(val) {
      return Cookies.set("XT_TOKEN", val);
    }
    
    export function removeToken() {
      return Cookies.remove("XY_TOKEN");
    }
    
    export function getViewPower() {
      return Cookies.get("XY_VIEWPOWER");
    }
    
    export function setViewPower(val) {
      return Cookies.set("XY_VIEWPOWER", val);
    }

**utils/localStorage.js**

    
    
    export default {
      fetch(name) {
        return JSON.parse(window.localStorage.getItem(name) || "[]");
      },
      save(name, items) {
        window.localStorage.setItem(name, JSON.stringify(items));
      }
    };

**utils/request.js**

    
    
    import axios from "axios";
    import { baseUrl } from "@/api/variable";
    import store from "@/store/store";
    
    // axios请求实例
    const request = axios.create({
      baseURL: baseUrl,
      timeout: 30000,
      headers: {
        "Content-Type": "application/json; charset=UTF-8"
      }
    });
    
    // 请求拦截，进行token传值
    request.interceptors.request.use(
      config => {
        if (store.state.user.token) {
          config.headers["token"] = store.state.user.token;
        }
        return config;
      },
      error => {
        return Promise.reject(error);
      }
    );
    
    // 响应拦截，获取真实数据
    request.interceptors.response.use(
      respone => {
        return respone;
      },
      error => {
        return Promise.reject(error);
      }
    );
    
    export default request;

###  数据模型

**api/variable.js**

    
    
    const baseUrl = "http://jsonplaceholder.typicode.com/";
    const wsUrl = "";
    if (process.env.NODE_ENV == "production") {
      if (process.env.VUE_APP_FLAG == "pro") {
        baseUrl = localStorage.getItem("baseUrl");
        wsUrl = localStorage.getItem("wsUrl");
      }
    }
    
    export { baseUrl, wsUrl };

**api/post.js**

    
    
    import request from "@/utils/request";
    
    export function getAllPosts() {
      return request({
        url: "posts",
        method: "get"
      });
    }

**store/store.js**

    
    
    import Vue from "vue";
    import Vuex from "vuex";
    Vue.use(Vuex);
    
    import app from "./modules/app";
    import user from "./modules/user";
    import post from "./modules/post";
    import getters from "./getters";
    
    const store = new Vuex.Store({
      modules: {
        app,
        user,
        post
      },
      getters
    });
    
    export default store;

**store/modules/user.js**

    
    
    const state = {
      loginName: ""
    };
    const mutations = {
      SET_LOGINNAME(state, loginName) {
        state.loginName = loginName;
      }
    };
    const actions = {
      login({ commit }, userInfo) {
        return new Promise((res, ret) => {
          commit("SET_LOGINNAME", userInfo);
          res();
        });
      },
      logout({ commit }) {
        return new Promise((res, ret) => {
          commit("SET_LOGINNAME", "");
          res();
        });
      }
    };
    export default {
      namespaced: true,
      state,
      mutations,
      actions
    };

**store/modules/post.js**

    
    
    import { getAllPosts } from "@/api/post";
    
    const state = {
      // 所有文章标题title
      titleList: []
    };
    const mutations = {
      // 存储文章标题
      SET_TITLELIST(state, list) {
        state.titleList = list;
      }
    };
    const actions = {
      // 获取文章标题
      getAllPosts({ commit }) {
        return new Promise((res, ret) => {
          getAllPosts()
            .then(data => {
              if (data.status == "200") {
                commit("SET_TITLELIST", data.data);
                res(data.data);
              }
            })
            .catch(err => {
              ret(err);
            });
        });
      }
    };
    
    export default {
      namespaced: true,
      state,
      mutations,
      actions
    };

###  组件

**views/login.vue**

    
    
    <div class="modify">
      <input
        type="text"
        @keydown.enter.prevent="handleKeydown"
        v-model="currentVal"
        placeholder="使用enter键切换频道"
      />
      <button @click="reset" style="margin-left:5px;outline:none;cursor:pointer;">复位</button>
    </div>
    
    
    import { mapState, mapMutations, mapActions } from "vuex";
    export default {
      name: "login",
      data() {
        return {
          currentVal: "",
          list: ["咨询服务", "音悦台", "体育台", "财经频道", "时尚资讯"],
          index: 0
        };
      },
      computed: {
        ...mapState({
          loginName: state => state.user.loginName
        })
      },
      methods: {
        ...mapActions({
          login: "user/login"
        }),
        handleToHome() {
          let userInfo = "user";
          this.login(userInfo);
          this.$router.push({
            path: "/"
          });
        },
        handleKeydown() {
          this.currentVal = this.list[this.index];
          this.index++;
          let len = this.list.length - 1;
          if (this.index > len) {
            this.index = 0;
          }
        },
        reset() {
          this.index = 0;
          this.currentVal = "";
        }
      }
    };

以上即是构建一个Vue+Vuex+VueRouter项目的主体架构，具有一定的通用性。

