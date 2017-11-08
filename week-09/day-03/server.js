var express = require('express');
var app = express();
app.use('/assets', express.static('./assets'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
})
app.get('/zsuzsi', function(req, res){
    
    var id = req.query.name
    console.log(req.query.name);
    res.send('Response send to client::'+req.query.name);
});
//DOUBLING //http://localhost:8080/doubling?input=15
app.get('/doubling', function(req, res) {
    if (req.query.input) {
        res.json({
            "received": req.query.input,
            "result": req.query.input * 2
        })
    }
    else {
        res.json({
            "error": "Please provide an input!"
        })
    }   
 });


//GREETER
app.get('/greeter', function(req, res) {
    if (req.query.title && req.query.name) {
        res.json({
            "welcome_message":"Oh, hi dear " + req.query.name + ", my dearest " + req.query.title + "!"
        });
    }
    else {
        res.json({
            "error": "Please provide a name!"
        })
    }   
 });

 //APPEND-A http://localhost:8080/appenda/kuty
 app.get('/appenda/:animal', function(request, response) {
    if (request.params.animal !== undefined) {
        response.json({"appended": request.params.animal + "a"});
    } else {
        response.json({"error": "404"})
   }
});

//DO UNTIL
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended : false}));
app.use(bodyParser.json());
app.post('/dountil/:type', function(req, res) {

    //console.log(req.params.type)
    //console.log(req.body.until)
    
    if (req.params.type ==="sum"){
        var sumNumber = req.body.until
        var sum = 0
        while (sumNumber >= 0){
            sum += sumNumber
            sumNumber -= 1
        }
        res.json({"result": sum})

    } else if (req.params.type === "factor"){
        var multiNumber = req.body.until
        var multi = 1
        while (multiNumber > 0){
            multi *= multiNumber
            multiNumber -= 1
        }
        res.json({"result": multi})
    }
});

app.listen(8080);
