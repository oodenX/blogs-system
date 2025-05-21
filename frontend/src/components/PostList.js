import React, { useState, useEffect } from 'react';
import { 
    List, 
    ListItem, 
    ListItemText, 
    Typography, 
    Button,
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    TextField
} from '@mui/material';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const PostList = () => {
    const [posts, setPosts] = useState([]);
    const [open, setOpen] = useState(false);
    const [newPost, setNewPost] = useState({ title: '', content: '' });

    useEffect(() => {
        fetchPosts();
    }, []);

    const fetchPosts = async () => {
        try {
            const response = await axios.get(`${API_URL}/posts`);
            setPosts(response.data);
        } catch (error) {
            console.error('Error fetching posts:', error);
        }
    };

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
        setNewPost({ title: '', content: '' });
    };

    const handleSubmit = async () => {
        try {
            await axios.post(`${API_URL}/posts`, newPost);
            handleClose();
            fetchPosts();
        } catch (error) {
            console.error('Error creating post:', error);
        }
    };

    const handleDelete = async (postId) => {
        try {
            await axios.delete(`${API_URL}/posts/${postId}`);
            fetchPosts();
        } catch (error) {
            console.error('Error deleting post:', error);
        }
    };

    return (
        <div>
            <Typography variant="h4" gutterBottom>
                博客文章列表
            </Typography>
            <Button variant="contained" color="primary" onClick={handleClickOpen} style={{ marginBottom: 20 }}>
                发布新文章
            </Button>
            <List>
                {posts.map((post) => (
                    <ListItem key={post.id} divider>
                        <ListItemText
                            primary={post.title}
                            secondary={
                                <>
                                    <Typography component="span" variant="body2" color="textPrimary">
                                        {post.content.substring(0, 100)}...
                                    </Typography>
                                    <br />
                                    <Typography component="span" variant="caption" color="textSecondary">
                                        发布时间: {new Date(post.created_at).toLocaleString()}
                                    </Typography>
                                </>
                            }
                        />
                        <Button 
                            variant="outlined" 
                            color="secondary" 
                            onClick={() => handleDelete(post.id)}
                        >
                            删除
                        </Button>
                    </ListItem>
                ))}
            </List>

            <Dialog open={open} onClose={handleClose}>
                <DialogTitle>发布新文章</DialogTitle>
                <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        label="标题"
                        fullWidth
                        value={newPost.title}
                        onChange={(e) => setNewPost({ ...newPost, title: e.target.value })}
                    />
                    <TextField
                        margin="dense"
                        label="内容"
                        fullWidth
                        multiline
                        rows={4}
                        value={newPost.content}
                        onChange={(e) => setNewPost({ ...newPost, content: e.target.value })}
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        取消
                    </Button>
                    <Button onClick={handleSubmit} color="primary">
                        发布
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    );
};

export default PostList; 