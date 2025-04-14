# 1. 引入 Flask 类
from flask import Flask, request, escape

# 2. 创建 Flask 应用实例
# Flask 类需要一个参数 __name__它告诉 Flask 应用的根路径在哪里，
# 这样 Flask 就可以找到资源文件和模板文件
app = Flask(__name__)

# 3. 定义路由
# @app.route('/') 是一个修饰器，他告诉 Flask 哪一个 URL 应该调用下面的函数
# '/' 是根 URL (比如https://localhost:5000/)
@app.route('/hello')
def hello_world():
    return 'hello world!'

@app.route('/goodbye')
def goodbye():
    return 'goodbye'

# 这里的 <username> 是一个变量部分，它会被 Flask 解析为 URL 的一部分
@app.route('/user/<username>')
def show_user_profile(username):
    # 这里的 username 是 URL 中的变量部分
    # 使用 escape 函数来防止 XSS 攻击
    return f'<h1>用户 {escape(username)}</h1>'

@app.route('/')
def menu():
    return '''
    <h1>菜单</h1>
    <ul>
        <li><a href="/hello">hello world</a></li>
        <li><a href="/goodbye">goodbye world</a></li>
    </ul>
    '''

# 这里的 <int:num1> 和 <int:num2> 是 URL 中的变量部分
@app.route('/cal/<int:num1>/<int:num2>')
def cal(num1, num2):
    return f'<h1>计算结果：{num1} + {num2} = {num1 + num2}</h1>'


@app.route('/multi/<int:num1>/<int:num2>')
def multi(num1, num2):
    num3 = num1 * num2
    return f'<h1>计算结果：{num1} * {num2} = {num3}</h1>'

@app.route('/file/<path:filename>')
def show_file(filename):
    # 这里的 filename 是 URL 中的变量部分
    # 使用 escape 函数来防止 XSS 攻击
    return f'<h1>文件名：{escape(filename)} 类型为 {type(filename).__name__}</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 如果是 POST 请求，说明用户提交了表当
        # 这里可以获取表当数据并进行处理（使用request对象）
        username = request.form.get('username')
        password = request.form.get('password')
        # 这里可以进行用户名和密码的验证
        if username == 'admin' and password == 'password':
            return f'<h1>欢迎 {escape(username)}!</h1>'
        else:
            return '<h1>用户名或密码错误</h1>'
    else:
        # 如果是 GET 请求，返回登录表单
        return '''
        <form method="POST">
            用户名：<input type="text" name="username"><br>
            密码：<input type="password" name="password"><br>
            <button type="submit">登录</button>
        </form>
        '''


# 4. 启动 Flask 应用
# 这段代码确保只有当这个脚本被直接运行时（而不是被导入到其他脚本时）
# 才会执行 app.run() 函数
if __name__ == '__main__':
    # app.run() 启动 Flask 应用
    # debug=True 使得 Flask 在代码更改时自动重启，并在发生错误时提供调试信息
    app.run(debug=True)