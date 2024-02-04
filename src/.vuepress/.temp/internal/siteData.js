export const siteData = JSON.parse("{\"base\":\"/chen-blog/\",\"lang\":\"zh_CN\",\"title\":\"阿晨的技术博客\",\"description\":\"记录开发中的技术与解决方案\",\"head\":[],\"locales\":{}}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updateSiteData) {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ siteData }) => {
    __VUE_HMR_RUNTIME__.updateSiteData(siteData)
  })
}
