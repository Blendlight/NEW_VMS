var path = require('path')
const ipc = require('electron').ipcRenderer;

var pyshell = require('python-shell');

let options = {
  pythonPath: '/usr/bin/python3.6',

};

var sys = require('sys');

var exc = require('child_process').exec;
var child;

function bacaid(evt){
  if (evt.srcElement.id == "capture"){
    var nodeControl = require('console');
    var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
    myConsole.log('\x1b[34m%s\x1b[0m','PRINT BEFORE PYTHON EXEC OCR from SATU.PY');

    pyshell.run('satu.py', options, function(err, results)(
      myConsole.log();

    ))


  }
}
