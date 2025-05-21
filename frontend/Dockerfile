FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

# 使用淘宝镜像源安装依赖，并添加网络超时配置
RUN npm config set registry https://registry.npmmirror.com && \
    npm config set fetch-timeout 300000 && \
    npm config set fetch-retry-mintimeout 20000 && \
    npm config set fetch-retry-maxtimeout 120000 && \
    npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"] 