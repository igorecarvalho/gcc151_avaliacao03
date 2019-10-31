'use strict';

const express = require('express');
const validarCpf = require('validar-cpf');
const name = process.env.name || "World";

// Constants
const PORT = 5000;

// App
const app = express();
app.get('/', (req, res) => {
    res.send('Hello from ' + name + '.\n' + 'Acessado de: '+ req.connection.localAddress + ' ' + req.connection.localPort + '.\n');
});

app.get('/validar/:cpf', (req, res) => {
    var cpf = req.params.cpf;
    res.send('CPF validado por ' + name + '!' + '.\nCPF ' + validarCpf(cpf)+'\n');
});
  
app.listen(PORT);
	console.log(`Running listening on port ${PORT}`);
