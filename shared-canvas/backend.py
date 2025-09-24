from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# 添加CORS支持
CORS(app, resources={r"/*": {"origins": "*"}})

# 初始化SocketIO时也配置CORS
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# 存储当前的画布状态
current_canvas = []
clients = set()

@app.route('/')
def index():
    return render_template('index.html')

# 添加一个简单的API端点测试CORS
@app.route('/test', methods=['GET'])
def test_cors():
    return {"message": "CORS is working!"}

@socketio.on('connect')
def handle_connect():
    clients.add(request.sid)
    print(f'客户端已连接: {request.sid}, 当前客户端数: {len(clients)}')
    # 发送当前画布状态给新连接的客户端
    if current_canvas:
        emit('canvasData', {'imageData': current_canvas}, room=request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    clients.discard(request.sid)
    print(f'客户端已断开: {request.sid}, 剩余客户端数: {len(clients)}')

@socketio.on('requestCanvas')
def handle_request_canvas():
    # if current_canvas:
    emit('canvasData', {'imageData': current_canvas}, room=request.sid)

@socketio.on('drawLine')
def handle_draw_line(data):
    # 广播绘制指令给所有客户端
    emit('drawLine', data, broadcast=True, include_self=False)
    current_canvas.append(json.loads(data))
    
    # 更新服务器端的画布状态（简单实现，实际应用中可能需要更复杂的同步机制）
    update_canvas_state()

@socketio.on('clearCanvas')
def handle_clear_canvas(data):
    # 广播清空指令给所有客户端
    print('clear request received!')
    emit('clearCanvas', broadcast=True)
    
    # 清空服务器端的画布状态
    global current_canvas
    current_canvas = []

def update_canvas_state():
    """定期更新服务器端的画布状态"""
    # 在实际应用中，这里应该从某个客户端获取最新的画布状态
    # 这里只是简单示例，实际需要更复杂的同步机制
    pass

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9850, debug=True)