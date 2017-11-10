'use strict'

var express = require('express');
var app = express();
app.use(express.json());
app.use('/', express.static('./'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/space.html');
})

app.get('/hello', function(req, res){
    res.send("Hello world!");
})
app.listen(8080);