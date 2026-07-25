const express = require('express');
const app = express();
const port = 3001;

app.get('/', (req, res) => {
  res.json({
    message: 'DevSecOps Sample Application',
    version: '1.0.0',
    timestamp: new Date().toISOString()
  });
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    uptime: process.uptime()
  });
});

app.listen(port, () => {
  console.log(`Sample app listening at http://localhost:${port}`);
});
