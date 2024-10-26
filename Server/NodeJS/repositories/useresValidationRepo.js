const axios = require('axios');

const RestApi = require('../configs/RestApi');
const USERS_URL = RestApi.Get_URL()

const GetUSersPlaceholder = () => {
  return axios.get(USERS_URL);
};


module.exports = {
  GetUSersPlaceholder
};