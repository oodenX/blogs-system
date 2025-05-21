import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import {
    Typography,
    Paper,
    TextField,
    Button,
    List,
    ListItem,
    ListItemText,
    Divider
} from '@mui/material';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const PostDetail = () => {
    const { id } = useParams();
    const [post, setPost] = useState(null);
    const [newComment, setNewComment] = useState({ content: '', author: '' });

    useEffect(() => {
        fetchPost();
    }, [id]);

    const fetchPost = async () => {
        try {
            const response = await axios.get(`${API_URL}/posts/${id}`);
            setPost(response.data);
        } catch (error) {
            console.error('Error fetching post:', error);
        }
    };

    const handleSubmitComment = async (e) => {
        e.preventDefault();
        try {
            await axios.post(`${API_URL}/posts/${id}/comments`, newComment);
            setNewComment({ content: '', author: '' });
            fetchPost();
        } catch (error) {
            console.error('Error posting comment:', error);
        }
    };

    const handleDeleteComment = async (commentId) => {
        try {
            await axios.delete(`${API_URL}/comments/${commentId}`);
            fetchPost();
        } catch (error) {
            console.error('Error deleting comment:', error);
        }
    };

    if (!post) {
        return <Typography>加载中...</Typography>;
    }

    return (
        <div>
            <Paper elevation={3} style={{ padding: 20, marginBottom: 20 }}>
                <Typography variant="h4" gutterBottom>
                    {post.title}
                </Typography>
                <Typography variant="body1" paragraph>
                    {post.content}
                </Typography>
                <Typography variant="caption" color="textSecondary">
                    发布时间: {new Date(post.created_at).toLocaleString()}
                </Typography>
            </Paper>

            <Typography variant="h5" gutterBottom>
                评论 ({post.comments.length})
            </Typography>

            <Paper elevation={2} style={{ padding: 20, marginBottom: 20 }}>
                <form onSubmit={handleSubmitComment}>
                    <TextField
                        fullWidth
                        label="你的名字"
                        value={newComment.author}
                        onChange={(e) => setNewComment({ ...newComment, author: e.target.value })}
                        margin="normal"
                        required
                    />
                    <TextField
                        fullWidth
                        label="评论内容"
                        multiline
                        rows={3}
                        value={newComment.content}
                        onChange={(e) => setNewComment({ ...newComment, content: e.target.value })}
                        margin="normal"
                        required
                    />
                    <Button type="submit" variant="contained" color="primary" style={{ marginTop: 10 }}>
                        发表评论
                    </Button>
                </form>
            </Paper>

            <List>
                {post.comments.map((comment) => (
                    <React.Fragment key={comment.id}>
                        <ListItem>
                            <ListItemText
                                primary={comment.content}
                                secondary={
                                    <>
                                        <Typography component="span" variant="body2" color="textPrimary">
                                            {comment.author}
                                        </Typography>
                                        {' — '}
                                        {new Date(comment.created_at).toLocaleString()}
                                    </>
                                }
                            />
                            <Button
                                variant="outlined"
                                color="secondary"
                                size="small"
                                onClick={() => handleDeleteComment(comment.id)}
                            >
                                删除
                            </Button>
                        </ListItem>
                        <Divider />
                    </React.Fragment>
                ))}
            </List>
        </div>
    );
};

export default PostDetail; 