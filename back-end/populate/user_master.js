// scripts/populate_db.js
const mongoose = require('mongoose');
const Ong = require('../models/Ong');

// Dados iniciais
const dados = [
    {'nome':'rafael.viana','senha':'ShutDown99*'}
            
      
];

// Conectar ao MongoDB
mongoose.connect('mongodb://127.0.0.1:27017/ong', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(async () => {
  console.log('Conectado ao MongoDB');

  // Limpar a coleção antes de inserir dados
  await Ong.deleteMany({});

  // Inserir os dados
  await Ong.insertMany(dados);
  console.log('Dados inseridos com sucesso');

  // Fechar a conexão
  mongoose.connection.close();
}).catch(err => {
  console.error('Erro ao conectar ao MongoDB:', err);
});
