const express = require('express');
const _ = require('lodash');
const app = express();
const port = 3000;

// Intentional security vulnerability for demonstration
app.get('/user/:id', (req, res) => {
    const userId = req.params.id;
    // SQL injection vulnerability (simulated)
    const query = "SELECT * FROM users WHERE id = " + userId;
    res.json({ message: 'User data retrieved', query: query });
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});
