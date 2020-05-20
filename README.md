# AdminLTE for PugJS 

This is an [AdminLTE](https://adminlte.io/themes/AdminLTE/index2.html) rewrite for [PugJS](https://pugjs.org/api/getting-started.html) template renderer. 

It also works with [Flask](https://flask.palletsprojects.com/en/1.1.x/) using the [PyPugJS](https://pypi.org/project/pypugjs/).


![AdminLTE](https://raw.githubusercontent.com/kantium/AdminLTE-for-PugJS/master/static/img/site.png)

## Warning

There is a difference between PyPugJS and PugJS on how Pug files in subdirectories are handled.
You need to rename ether ```basepy.pug``` or ```basejs.pug``` to ```base.pug``` before use (located in ```templates/layout/baseXX.pug```) 

## Python3

```
mv templates/layout/basepy.pug templates/layout/base.pug
pip3 install flask
pip3 install pypugjs
python3 app.py
```

## NodeJS

```
mv templates/layout/basejs.pug templates/layout/base.pug
npm install
npm start
```
