var express = require('express');
var flick = require('flick');
var shell = require('shelljs');
var app = express();
var handler = flick();

handler.use(function(req, res, next) {
    console.log('Got a WebHook!');
    res.send('NUBBIN');
    next();
});
 
app.use('/', flick.secret(process.env.GITHUB_SECRET));
app.use('/', handler);
app.listen(3000);
