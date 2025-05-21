from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# 初始化数据库
db = SQLAlchemy()

# 初始化CORS
cors = CORS() 