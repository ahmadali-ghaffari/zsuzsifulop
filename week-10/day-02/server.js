'use strict';

var express = require('express');
var app = express();
app.use(express.json());
app.use('/', express.static('./assets'));
var mysql = require('mysql');
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '1234',
    database: 'audioplayer'
});

connection.connect(function (err) {
    if (err) {
        console.log("Error connecting to Db");
        return;
    }
    console.log("Connection established");
});

var get_playlist = function () {
    var playlist = [];
    connection.query('SELECT * FROM playlists', function (err, result, fields) {
        playlist = [].concat(result);
    });
    return playlist;
};

app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/playlist', function (req, res) {
    connection.query('SELECT * FROM playlists', function (err, result, fields) {
        if (err) {
            console.log('error in the connecion querry');
        }
        console.log("Data recived from Db\n");
        res.send(result);
    });
});

app.get('/playlist/:playlist_id', function (req, res) {
    connection.query('SELECT * FROM tracks WHERE playlist_id =' + req.params.playlist_id, function (err, result, fields) {
        if (err) {
            console.log('error in the connecion querry');
        }
        console.log("Data recived from Db\n");
        res.send(result);
    });

});

app.post('/add/:string', function (req, res) {

    var q = "INSERT INTO playlists (playlist) values (\"" + req.params.string + "\");";
    console.log(q);
    connection.query(q);
    res.send({'status': 'ok'});
});

app.delete('/delete/:id', function (req, res) {
    console.log(req.params);
    connection.query('DELETE FROM playlists WHERE id = ' + req.params.id + ' AND system = 0;');
    res.send({'status': 'ok'});
});

app.post('/playlist', function (req, res) {
    console.log(req.body);
    connection.query("INSERT INTO playlists (playlist) VALUES (" + req.body.playlist + ")", function (err, result, fields) {
        if (err) {
            console.log('error in the connecion querry');
        } else {
            console.log("New line recived from Db\n");
            console.log({"result": result});
        }
        console.log(get_playlist());
        res.send(JSON.stringify(get_playlist()));
    });
});

app.get('/favourite', function (req, res) {
    connection.query('SELECT * FROM playlists WHERE system = 0 ', function (err, result, fields) {
        if (err) {
            console.log('error in the connecion querry');
        }
        console.log("Data recived from Db\n");
        res.send(result);
    });
});

app.listen(8080, function () {
    console.log("Hey, I am working on localhost:8080");
});