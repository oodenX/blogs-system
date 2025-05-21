.PHONY: install build start stop clean help

# 默认目标
.DEFAULT_GOAL := help

# 变量定义
DOCKER_COMPOSE = docker-compose

# 帮助信息
help:
	@echo "可用的命令："
	@echo "  make install    - 安装所有依赖（前端和后端）"
	@echo "  make build      - 构建Docker镜像"
	@echo "  make start      - 启动所有服务"
	@echo "  make stop       - 停止所有服务"
	@echo "  make clean      - 清理所有生成的文件和容器"
	@echo "  make logs       - 查看服务日志"
	@echo "  make restart    - 重启所有服务"

# 安装依赖
install:
	@echo "正在安装后端依赖..."
	cd backend && pip install -r requirements.txt
	@echo "正在安装前端依赖..."
	cd frontend && npm install

# 构建Docker镜像
build:
	@echo "正在构建Docker镜像..."
	$(DOCKER_COMPOSE) build

# 启动服务
start:
	@echo "正在启动服务..."
	$(DOCKER_COMPOSE) up -d

# 停止服务
stop:
	@echo "正在停止服务..."
	$(DOCKER_COMPOSE) down

# 清理
clean:
	@echo "正在清理..."
	$(DOCKER_COMPOSE) down -v
	rm -rf frontend/node_modules
	rm -rf backend/__pycache__
	rm -rf backend/*.pyc

# 查看日志
logs:
	$(DOCKER_COMPOSE) logs -f

# 重启服务
restart: stop start 