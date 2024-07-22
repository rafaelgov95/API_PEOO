// routes/ong.js
const express = require('express');
const router = express.Router();
const Ong = require('../models/Ong');

// Rota para obter todas as ONGs
router.get('/', async (req, res) => {
  try {
    const ongs = await Ong.find();
    res.json(ongs);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Rota para adicionar uma nova ONG
router.post('/', async (req, res) => {
  const ong = new Ong({
    nome: req.body.nome,
    projetos: req.body.projetos
  });

  try {
    const novoOng = await ong.save();
    res.status(201).json(novoOng);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

module.exports = router;
