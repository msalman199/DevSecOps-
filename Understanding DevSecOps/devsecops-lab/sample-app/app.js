// Sample application with security issues for demonstration
const express = require('express');
const app = express();

// Security issue: Missing input validation
app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;
    
    // Security issue: SQL injection vulnerability
    const query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
    
    // Security issue: Hardcoded credentials
    if (username === 'admin' && password === 'password123') {
        res.send('Login successful');
    } else {
        res.send('Login failed');
    }
});

app.listen(3000, () => {
    console.log('App running on port 3000');
});
