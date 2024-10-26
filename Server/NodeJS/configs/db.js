const mongoose = require('mongoose');

const connectDB = () => {
  // Connect to MongoDB database
  mongoose
    .connect(`mongodb://localhost:27017/MyDB`)
    .then(() => console.log('Connected to MyDB'))
    .catch((error) => console.log(error));
};

module.exports = connectDB;
