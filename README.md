# bitnp-icebreaker 网络开拓者协会破冰会工具箱
------------------------------------------------

## 1. 项目内容
1. 抽卡动画 (./introduction)
2. 共享画布 (./shared-canvas)

------------------------------------------------
## 2. 安装
### 2.1 抽卡动画安装
``` sh
cd ./introduction
npm install
```

### 2.2 共享画布安装
``` sh
cd ./shared-canvas
pip install flask flask-socketio flask-cors eventlet
```

------------------------------------------------

## 3. 运行
### 3.1 运行抽卡动画
``` sh
cd ./introduction
npm run serve
```
然后在浏览器打开`localhost:8080`

提供以下页面：
- `localhost:8080/#/directors`: 部长介绍页；
- `localhost:8080/#/lottery-random`: 抽奖页；
- `localhost:8080/#/lottery-ordered`: 伪抽奖页。


使用下箭头键/上箭头键来播放动画 (类似PPT)
_如果觉得动画视频或音频太长，可以再按一次下箭头键，来跳过动画_

**快捷键列表**
| 快捷键 | 功能 |
| --- | --- |
| ⬇️ | 播放动画（类似 PPT），再次按下可跳过动画 |
| ⬆️ | 播放动画（类似 PPT） |
| 空格 | 跳过动画视频或音频 （BanG Dream 抽卡音乐有点长，建议名字出来之后使用空格键跳过） |
| F | 进入/退出全屏 |
| U | 上传抽奖名单文件 (.json 或 .txt) |

_**关于抽奖名单文件格式**_
接受`.json`或`.txt`两种格式。
- `.json`文件格式示例：
``` json
[
  {"name": "林子煊", "avatarUrl": "/avatar/azusa.jpeg", "theme": "GenshinImpact", "shumeiniangImage": "guitar2"},
  {"name": "张家诚", "avatarUrl": "/avatar/mugi.jpeg", "theme": "Arknights", "shumeiniangImage": "keyboard"},
  {"name": "袁靖", "avatarUrl": "/avatar/mio.jpeg", "theme": "WutheringWaves", "shumeiniangImage": "bass"},
  {"name": "杨浩天", "avatarUrl": "/avatar/ritsu.jpeg", "theme": "PJSK", "shumeiniangImage": "drum"},
  {"name": "郭逸戈", "avatarUrl": "/avatar/yui.jpeg", "theme": "BanGDream", "shumeiniangImage": "guitar1"}
]
```
其中， `avatarUrl`、`theme` 以及 `shumeiniangImage` 字段可以省略。

- `.txt`文件格式示例：(仅描述name列表，用换行符`\n`分隔)
```
林子煊
张家诚
袁靖
杨浩天
郭逸戈
```


### 3.2 运行共享画布
#### 3.2.1 后端
``` sh
cd ./shared-canvas
python backend.py
```
#### 3.2.2 前端
``` sh
cd ./shared-canvas/frontend
python -m http.server 8000
```

_注意：共享画布需要公网 IP 才能使用户正常访问，最好部署在服务器上，或使用允许 http 服务费的内网穿透工具_


------------------------------------------------
作者：`25网协技术部`

如有问题，请通过邮箱`indexguo@163.com`随时联系
