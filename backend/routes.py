from flask import Blueprint, request, jsonify
from models import Post, Comment
from extensions import db

bp = Blueprint('api', __name__)

@bp.route('/posts', methods=['GET'])
def get_posts():
    """获取所有文章列表"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/posts', methods=['POST'])
def create_post():
    """创建新文章"""
    data = request.json
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': '标题和内容不能为空'}), 400
    
    post = Post(title=data['title'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

@bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """获取单篇文章详情"""
    post = Post.query.get_or_404(post_id)
    post_dict = post.to_dict()
    post_dict['comments'] = [comment.to_dict() for comment in post.comments]
    return jsonify(post_dict)

@bp.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """更新文章"""
    post = Post.query.get_or_404(post_id)
    data = request.json
    
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']
    
    db.session.commit()
    return jsonify(post.to_dict())

@bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """删除文章"""
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return '', 204

@bp.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    """为文章添加评论"""
    post = Post.query.get_or_404(post_id)
    data = request.json
    
    if not data or 'content' not in data or 'author' not in data:
        return jsonify({'error': '评论内容和作者不能为空'}), 400
    
    comment = Comment(
        content=data['content'],
        author=data['author'],
        post_id=post_id
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201

@bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """删除评论"""
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return '', 204 