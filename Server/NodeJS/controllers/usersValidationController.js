const express = require('express');
const ValidationService = require('../services/ValidationService');

const router = express.Router();

router.get('/', async (req, res) => {
  try {
    //const users = await ValidationService.getAllusers()
    res.json("Validation does not support GET requests");
  } catch (error) {
    res.json(error);
  }
});


router.post('/', async (req, res) => {
  try {
    const V = await ValidationService.Validate(req);
    console.log(V)
    if (V.Status === "Success") {
      res.status(200).json(V);
      return;
    }
    res.status(500).json({ "Status": "Failed" });
  } catch (error) {
    res.status(500).json(error.message);
  }
});


module.exports = router;
