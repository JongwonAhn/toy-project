const express = require('express');

const PORT = 8080;

//APP
const app = express();
app.get('/', (req,res) =>{
    res.send("hello world")
});

app.listen(PORT);