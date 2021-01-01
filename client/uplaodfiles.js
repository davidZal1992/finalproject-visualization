
document.getElementById('buttonid').addEventListener('click', generate);

async function generate() {

  const res = await axios.get('http://127.0.0.1:8000/actions/upload2')
  console.log(res);

  let formData = new FormData();

  formData.append("files", document.getElementById('mirNA').files[0]);
  formData.append("files", document.getElementById('target').files[0]);
  formData.append("files", document.getElementById('connection').files[0]);
  
  axios.post('http://127.0.0.1:8000/actions/upload', formData, {
    headers: {
      'content-Type': 'multipart/form-data'
    }
    }).then((response) => {
    console.log(response);
  }, (error) => {
    console.log(error);
  });
}