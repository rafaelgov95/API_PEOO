const express = require('express');
const router = express.Router();
const Ong = require('../models/Ong'); 
const auth = require('../middleware/auth');

const getOng = async (req, res, next) => {
  try {
    const ong = await Ong.findById(req.params.id);
    if (!ong) {
      return res.status(404).json({ message: 'ONG não encontrada' });
    }
    res.ong = ong;
    next();
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

router.get('/', async (req, res) => {
  try {
    const ongs = await Ong.find();
    res.json(ongs);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});


// Rota para adicionar uma nova ONG
router.post('/',auth, async (req, res) => {
  const ong = new Ong({
    nome: req.body.nome,
    projetos: req.body.projetos // Se seu modelo Ong tem um array de projetos
  });

  try {
    const novoOng = await ong.save();
    res.status(201).json(novoOng);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

router.put('/:id',auth, async (req, res) => {
  const updates = {
    nome: req.body.nome,
    projetos: req.body.projetos
  };
  try {
    const ong = await Ong.findById(req.params.id);
    if (!ong) {
      return res.status(404).json({ message: 'ONG não encontrada' });
    }
    ong.nome = updates.nome;
    ong.projetos = updates.projetos;

    const updatedOng = await ong.save();
    res.json(updatedOng);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Rota para deletar uma ONG
router.delete('/:id', auth,getOng, async (req, res) => {
  try {
    await res.ong.deleteOne(); // Usa deleteOne() para remover a ONG do banco de dados
    res.json({ message: 'ONG deletada' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
