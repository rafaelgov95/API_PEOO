// server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const ongRoutes = require('./routes/ong');

const app = express();
const port = 3000; // Ou qualquer porta que preferir

// Conectar ao MongoDB
mongoose.connect('mongodb://127.0.0.1:27017/ong', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Conectado ao MongoDB');
}).catch(err => {
  console.error('Erro ao conectar ao MongoDB:', err);
});

// Middleware
app.use(bodyParser.json());

// Usar o roteador
app.use('/ongs', ongRoutes);

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
