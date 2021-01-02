const axios = require('axios')
const {drawmap} = require('./drawmap')
document.getElementById('buttonid').addEventListener('click', generate);

function generate() {
  
  let formData = new FormData();

  formData.append("files", document.getElementById('mirNA').files[0]);
  formData.append("files", document.getElementById('target').files[0]);
  formData.append("files", document.getElementById('connection').files[0]);
  console.log('check')
  axios.post('http://127.0.0.1:8000/actions/upload', formData, {
    headers: {
      'content-Type': 'multipart/form-data',
      "Access-Control-Allow-Origin": "*"
    }
    }).then((response) => {
      console.log(response.data)
      drawmap(response.data)
  }, (error) => {
    console.log(error);
  });
}

