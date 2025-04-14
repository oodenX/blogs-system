from flask import Flask, request, render_template, url_for, abort, escape

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>菜单</h1>'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return '这是一个 POST 请求'
    else:
        return '这是一个 GET 请求（或者其他方法）'

# 访问 /search?q=flask&page=2
@app.route('/search')
def search():
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)    # 默认值为 1，类型转换为 int
    return f'<h1>搜索词：{query}, 页数：{page}</h1>'

@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'POST':
        # 如果是 POST 请求，说明用户提交了表当
        # 这里可以获取表当数据并进行处理（使用request对象）
        username = request.form.get('username')
        password = request.form.get('password')
        return f'<h1>用户名：{username}, 密码：{password}</h1>'
    else:
        return '''
            <form method="post">
                <p><input type="text" name="username" placeholder="用户名"></p>
                <p><input type="password" name="password" placeholder="密码"></p>
                <p><input type="submit" value="登陆"></p>
            </form>
        '''

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()   # 获取 JSON 数据
    if data:
        item_name = data.get('name')
        item_value = data.get('value')
        return f'<h1>接收到数据：{item_name} = {item_value}</h1>'
    else:
        return '<h1>没有接收到数据</h1>', 400


if __name__ == '__main__':
    app.run(debug=True)