# Flask + React 博客评论系统

## 项目简介

本项目是一个全栈博客评论系统，后端基于 Flask + SQLAlchemy，前端基于 React + Material-UI，支持文章发布、评论、Docker一键部署。

### 主要功能

- 文章发布与展示
- 文章评论
- RESTful API
- 响应式前端界面
- Docker容器化部署

### 技术栈

- 后端：Flask, SQLAlchemy, Flask-CORS
- 前端：React, Material-UI, Axios, React Router
- 数据库：SQLite
- 部署：Docker, Docker Compose

## 项目结构

```
flask-quick-start/
├── backend/                  # 后端Flask服务
│   ├── app.py               # 主应用入口
│   ├── models.py            # 数据库模型
│   ├── routes.py            # 路由与接口
│   ├── extensions.py        # 扩展初始化
│   ├── config.py            # 配置文件
│   ├── requirements.txt     # 后端依赖
│   └── Dockerfile          # 后端Dockerfile
│
├── frontend/                # 前端React应用
│   ├── src/
│   │   ├── components/     # React组件
│   │   │   ├── PostList.js
│   │   │   └── PostDetail.js
│   │   ├── App.js         # 主应用组件
│   │   └── index.js       # 入口文件
│   ├── public/            # 静态资源
│   ├── package.json       # 前端依赖
│   └── Dockerfile        # 前端Dockerfile
│
├── docker-compose.yml     # Docker编排
└── README.md             # 项目说明
```

## 快速开始

### 1. 本地开发

#### 后端

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

#### 前端

```bash
cd frontend
npm install
npm start
```

- 前端访问：http://localhost:3000
- 后端API：http://localhost:5000/api

### 2. Docker部署

```bash
# 构建并启动容器
docker-compose up --build

# 仅启动容器
docker-compose up

# 停止容器
docker-compose down
```

- 前端：http://localhost:3000
- 后端API：http://localhost:5000/api

## API接口

### 文章接口

- `GET /api/posts` - 获取所有文章
- `POST /api/posts` - 创建新文章
- `GET /api/posts/<id>` - 获取单篇文章
- `PUT /api/posts/<id>` - 更新文章
- `DELETE /api/posts/<id>` - 删除文章

### 评论接口

- `POST /api/posts/<id>/comments` - 添加评论
- `DELETE /api/comments/<id>` - 删除评论

## 开发说明

### 后端开发

1. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行开发服务器：
```bash
python app.py
```

### 前端开发

1. 安装依赖：
```bash
npm install
```

2. 运行开发服务器：
```bash
npm start
```

3. 构建生产版本：
```bash
npm run build
```

## 部署说明

### Docker部署

1. 确保已安装Docker和Docker Compose

2. 在项目根目录运行：
```bash
docker-compose up --build
```

3. 访问：
- 前端：http://localhost:3000
- 后端API：http://localhost:5000/api

### 环境变量

- `FLASK_APP`: Flask应用入口
- `FLASK_ENV`: 运行环境
- `FLASK_DEBUG`: 调试模式
- `REACT_APP_API_URL`: 前端API地址

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Cors==4.0.0
python-dotenv==1.0.0
SQLAlchemy==2.0.23
