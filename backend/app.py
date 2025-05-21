from flask import Flask
from extensions import db, cors
from config import Config
from routes import bp as api_bp

def create_app():
    """创建并配置Flask应用"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    cors.init_app(app)

    # 注册蓝图
    app.register_blueprint(api_bp, url_prefix='/api')

    # 创建数据库表
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True) 