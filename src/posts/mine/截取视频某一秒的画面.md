---
date: 2024-01-13
category:
  - JavaScript
tag:
  - 技巧
---

# 截取视频某一秒的画面

## 需求来源

在开发中，有个需求是在视频下方需要展示视频的进度，鼠标移入需要展示这个时间点的缩略图。
<!-- more -->
## 解决设想

视频获取其中图片，通过将视频绘制在`canvas`上进行，通过调整视频播放时间来进行获取图片。

## 代码展示

tools.js内代码

```javascript
const handleGetVideoThumb =  (url, options = {})=> {
  if (typeof url != 'string'&&!url instanceof File) {
    return;
  }

  const defaults = {
    seekTime :1,
    onLoading: () => {},
    onLoaded: () => {},
    onFinish: () => {},
  };

  const params ={
      ...defaults,
      ...options
  };

  const video = document.createElement('video');

  video.muted = true;

  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d', {
    willReadFrequently: true,
  });

  let isTimeUpdated = false;

  video.addEventListener('loadedmetadata', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    draw();
  });
  video.addEventListener('timeupdate', () => {
    isTimeUpdated = true;
  });

  params.onLoading();

  if(url instanceof File){
      const videoUrl = URL.createObjectURL(url);
      video.src = videoUrl;
  }
  else if (/^blob:|base64,/i.test(url)) {
    video.src = url;
  } else {
    fetch(url)
      .then((res) => res.blob())
      .then((blob) => {
        params.onLoaded();
        video.src = URL.createObjectURL(blob);
      });
  }
  const draw = () => {
    const duration = video.duration;
    video.currentTime = params.seekTime;
    const onSeeked = () => {
      context.clearRect(0, 0, canvas.width, canvas.height);
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      canvas.toBlob((blob) => {
        params.onFinish(URL.createObjectURL(blob),duration);
      }, 'image/jpeg');
    };

    video.addEventListener('seeked', onSeeked);
  };
};
```

使用中

```javascript
handleGetVideoThumb(fileDom.files[0], {
  seekTime: 10, 
  onFinish: (data) => {
    console.log(data)
  },
});
```

## 方法拓展

可以拓展为promise方法，传入的seekTime也可以拓展为数组，同时截取视频内多张图片
