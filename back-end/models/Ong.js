// models/Ong.js
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ProjetoSchema = new Schema({
  nome: String,
  descricao: String,
  responsavel: String,
  status: String
});

const OngSchema = new Schema({
  nome: String,
  projetos: [ProjetoSchema]
});

module.exports = mongoose.model('Ong', OngSchema);
