var path = require('path');
var express = require('express');


var app = express();

app.set('view engine', 'pug');
app.set('views', path.join(__dirname, '/templates'));
app.use('/',express.static(__dirname));

app.locals.basedir = path.join(__dirname, 'templates');

console.log(path.join(__dirname, '/static'))
console.log(path.join(__dirname, '/templates'))

app.use(express.static('public'));

app.get('/:fileName', (req, res) => {
    res.render(req.params.fileName);
});



app.listen(5000, () => console.log('listening on port 5000!'));