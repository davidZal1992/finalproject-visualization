const axios = require('axios')

document.getElementById('buttonid').addEventListener('click', generate);

function generate() {

  axios.get('http://127.0.0.1:8000/actions/upload2')
  .then((response) => {
    console.log(response);
  }, (error) => {
    console.log(error);
  });

}

