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

## 3. 运行
### 3.1 运行抽卡动画
``` sh
cd ./introduction
npm run serve
```
然后在浏览器打开`localhost:8080`
使用下箭头键/上箭头键来播放动画 (类似PPT) , 鼠标左键点击任意位置跳过动画/终止音频

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


作者：`25网协技术部`

如有问题，请通过邮箱`indexguo@163.com`随时联系
