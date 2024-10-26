const express = require('express');
const jwt = require('jsonwebtoken');
const jf = require('jsonfile')
const mongoose = require('mongoose');
const { ObjectId } = require('mongodb');

const ValidationusersRepo = require('../repositories/useresValidationRepo');
const usersRepo = require('../repositories/usersRepo');

const SECRET_KEY = 'some_key';
const FILE = '../Data/System_Users_Actions.json'


const Validate = async (filters) => {
  const { data } = await ValidationusersRepo.GetUSersPlaceholder();
  const { username, email } = filters.body;


  const userV = data.filter((user) => user.email === email && user.username === username)
  if (userV.length > 0) {
    let usr = await usersRepo.getAllusers({ "FullName": userV[0].name })
    let usrid = usr[0]._id
    maxactions = usr[0].Num_Of_actions

    const data = await jf.readFile(FILE);
    const now = new Date();
    let today = new Date(now.getTime() - now.getTimezoneOffset() * 60000).toISOString().slice(0, -1);


    let actionAllowed = data.actions.filter(act => {
      // Convert act.id to ObjectId and compare with userId
      const actId = new mongoose.Types.ObjectId(act.id); // Assuming act.id is a valid ObjectId string
      return actId.equals(usrid) && today.slice(0, 10) === act.date.slice(0, 10);
    });


    const token =
    {
      "Token":
        jwt.sign({ username, email, usrid, maxactions }, SECRET_KEY, { expiresIn: '2h' })
      ,
      "Fullname": userV[0].name
      ,
      "Num_Of_actions": maxactions - actionAllowed.length
      ,
      "Status": "Success"
    }

    return token
  }

  return 0

};

const getAllusers = () => {
  return ValidationusersRepo.GetUSersPlaceholder();
};


const ServerRequest = async (token) => {

  const jt = jwt.verify(token, SECRET_KEY)

  const { data } = await ValidationusersRepo.GetUSersPlaceholder();
  const { username, email, usrid, maxactions } = jt;
  const userV = data.filter((user) => user.email === email && user.username === username)
  if (userV.length > 0) {

    const data = await jf.readFile(FILE);
    const now = new Date();
    let today = new Date(now.getTime() - now.getTimezoneOffset() * 60000).toISOString().slice(0, -1);


    let actionAllowd = data.actions.filter(act => act.id === usrid && today.slice(0, 10) === act.date.slice(0, 10))

    if (maxactions - actionAllowd.length === 0)
      return 0;


    data.actions.push({
      "id": new ObjectId(usrid),
      "maxActions": maxactions,
      "date": new Date(),
      "actionAllowd": maxactions - actionAllowd.length

    });
    await jf.writeFile(FILE, data);

  }

  return 1

};



module.exports = {
  getAllusers,
  ServerRequest,
  Validate
};
