const usersRepo = require('../repositories/usersRepo');
const jf = require('jsonfile')
const FILE = '../Data/System_Users_Actions.json'
const { ObjectId } = require('mongodb');

const getAllusers = async (filters) => {
  let usrs = await usersRepo.getAllusers(filters);
  const data = await jf.readFile(FILE);
  const now = new Date();
  let today = new Date(now.getTime() - now.getTimezoneOffset() * 60000).toISOString().slice(0, -1);

  let usrsA = []

  let obj = ""

  usrs.forEach(usr => {
    // Filter actions for the current user and today's date
    const actionAllowed = data.actions.filter(act => {
      try {
        const actId = new ObjectId(act.id); // Check if act.id is a valid ObjectId
        const isSameDate = today.slice(0, 10) === act.date.slice(0, 10); // Compare dates
        return actId.equals(usr._id) && isSameDate;
      } catch (error) {
        console.error('Invalid ObjectId:', act.id, 'Error:', error);
        return false; // Skip invalid ObjectId
      }
    });


    usrsA.push({
      "_id": usr._id,
      "FullName": usr.FullName,
      "Num_Of_actions": usr.Num_Of_actions,
      "currentActions": usr.Num_Of_actions - actionAllowed.length
    })

  })

  console.log(usrsA)

  return usrsA

};

const getById = (id) => {
  return usersRepo.getById(id);
};

const adduser = (obj) => {
  return usersRepo.adduser(obj);
};

const updateuser = (id, obj) => {
  return usersRepo.updateuser(id, obj);
};

const deleteuser = (id) => {
  return usersRepo.deleteuser(id);
};

module.exports = {
  getAllusers,
  getById,
  adduser,
  updateuser,
  deleteuser,
};
