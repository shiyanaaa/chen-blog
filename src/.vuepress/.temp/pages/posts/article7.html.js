export const data = JSON.parse("{\"key\":\"v-7881aaa3\",\"path\":\"/posts/article7.html\",\"title\":\"Article 7\",\"lang\":\"zh_CN\",\"frontmatter\":{\"date\":\"2022-01-07T00:00:00.000Z\",\"category\":[\"CategoryA\",\"CategoryB\"],\"tag\":[\"tag C\",\"tag D\"]},\"headers\":[{\"level\":2,\"title\":\"Heading 2\",\"slug\":\"heading-2\",\"link\":\"#heading-2\",\"children\":[{\"level\":3,\"title\":\"Heading 3\",\"slug\":\"heading-3\",\"link\":\"#heading-3\",\"children\":[]}]}],\"git\":{\"updatedTime\":1706842947000,\"contributors\":[{\"name\":\"梁晨\",\"email\":\"1161480992@qq.com\",\"commits\":1}]},\"filePathRelative\":\"posts/article7.md\"}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
