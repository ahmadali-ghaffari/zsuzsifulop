var express = require('express');
var mysql = require('mysql');
var app = express();
app.use(express.json());
app.use('/assets', express.static('./assets'));


var conn = mysql.createConnection({
    host: "localhost",
    user: "'root'",
    password: "1234",
    database: 'bookstore'
  });
  
conn.connect(function(err){
    if(err){
      console.log("Error connecting to Db");
      return;
    }
console.log("Connection established");
  });


  
app.get('/', function(req, res){
    res.sendFile(__dirname + '/bookstore_index.html');
})

// app.get('/', function(req, res){
//     conn.query("SELECT * FROM table_name;",function(err,rows){
//         if (err){
//             console.log(err)
//         } else {
//             console.log("Data received from Db:\n");
//             console.log(rows);
//             res.json(row);
//         }
//         });
app.get('/list', function(req, res){
    conn.query("SELECT book_name from book_mast;", function(err, rows){
        if(err){
            console.log('error');
        } 
        console.log("Data recived from Db\n");
        let htmlString = '<ul>'
        rows.forEach(function(row){
            htmlString = htmlString + '<li>' + row.book_name + '</li>';
        });
        htmlString += '</ul>';
        res.send(htmlString);
    })

});
app.get('/all', function(req, res){

});

app.listen(3000);