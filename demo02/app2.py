from flask import Flask, request, escape, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # 生成 '/about' 的路径的 URL
    about_url = url_for('about')
    # 生成 '/user/test_user/ 路径对应的 URL
    user_url = url_for('show_user_profile', username='test_user')   # 注意这里传入了动态路由需要的参数
    return f'''
        <h1>菜单</h1>
        <p><a href="{about_url}">关于</a></p>
        <p><a href="{user_url}">用户</a></p>
        <p><a href="{url_for('show_post', post_id=42)}">查看文章 42</a></p>
        <p><a href="{url_for('login')}">登陆界面</a></p>
        <p><a href="{url_for('redict_example')}">菜单</a></p>
        '''

@app.route('/about')
def about():
    return '<h2>关于界面</h2>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'<h1>用户 {escape(username)}</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<h1>文章 {post_id}</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 如果是 POST 请求，说明用户提交了表当
        # 这里可以获取表当数据并进行处理（使用request对象）
        username = request.form.get('username')
        password = request.form.get('password')
        # 这里可以进行用户名和密码的验证
        return f'<h1>用户名：{escape(username)} 密码：{escape(password)}</h1>'
    else:
        # 如果是 GET 请求，返回登陆表单
        return '''
            <form method="post">
                <p><input type="text" name="username" placeholder="用户名"></p>
                <p><input type="password" name="password" placeholder="密码"></p>
                <p><input type="submit" value="登陆"></p>
            </form>
        '''

@app.route('/redict-me')
def redict_example():
    # 重定向到 index 视图函数对应的 URL ('/)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)