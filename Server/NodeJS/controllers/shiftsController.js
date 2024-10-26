const express = require('express');
const shiftsService = require('../services/shiftsService');
const ValidationService = require('../services/ValidationService');



const router = express.Router();

// Entry point: http://localhost:3000/shifts

// Get All shifts
router.get('/', async (req, res) => {
  try {
    const filters = req.query;
    const shifts = await shiftsService.getAllshifts(filters);
    res.json(shifts);
  } catch (error) {
    res.json(error);
  }
});

// Get a shift By ID
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const shift = await shiftsService.getById(id);
    res.json(shift);
  } catch (error) {
    res.json(error);
  }
});


// Add a new shift
router.post('/', async (req, res) => {
  const validreq = await ValidationService.ServerRequest(req.body.token);
  console.log(req.body.token)
  if ( validreq === 0 ||  validreq.length === 0)
  {
    res.status(500).json("Can't do another actions today")
    return;
  }

  try {
    const obj = req.body.shift;
    const result = await shiftsService.addshift(obj);
    res.status(201).json(result);

  } catch (error) {
    res.status(500).json(error.message);
  }
});

// Update a shift
router.put('/:id', async (req, res) => {
  const validreq = await ValidationService.ServerRequest(req.body.token);
  console.log(req.body.token)
  if ( validreq === 0 ||  validreq.length === 0)
  {
    res.status(500).json("Can't do another actions today")
    return;
  }

  try {
    const { id } = req.params;
    const obj = req.body.shift;
    const result = await shiftsService.updateshift(id, obj);
    res.json(result);
  } catch (error) {
    res.json(error);
  }
});

// Delete a shift
router.delete('/:id/', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await shiftsService.deleteshift(id);
    res.json(result);
  } catch (error) {
    res.json(error);
  }
});

// Allocate employee to shift
router.put('/:id/allocate', async (req, res) => {
  const validreq = await ValidationService.ServerRequest(req.body.token);
  if ( validreq === 0 ||  validreq.length === 0)
  {
    res.status(500).json("Can't do another actions today")
    return;
  }
  
  try {
    const { id } = req.params;
    const { employeeId } = req.body.shift;
    const result = await shiftsService.allocateEmployee(id, employeeId);
    if (result.message)
      res.json(result);
    else
      res.status(500).json(result);
  } catch (error) {
    res.status(500).json(error.message);
  }
});

module.exports = router;
