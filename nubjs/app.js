var express = require('express');
var app = express();

app.get('/', function(req, res) {
    res.send('NUBBIN');
});


var server = app.listen(3000, function() {
    console.log('Express is listening to http://localhost:3000'); 
});
