FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# 使用清华镜像源安装依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip && \
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"] 