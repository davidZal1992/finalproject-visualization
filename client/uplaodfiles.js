
document.getElementById('buttonid').addEventListener('click', generate);

async function generate() {

  let formData = new FormData();

  formData.append("files", document.getElementById('mirNA').files[0]);
  formData.append("files", document.getElementById('target').files[0]);
  formData.append("files", document.getElementById('connection').files[0]);
  try {
    result = await axios.post('http://127.0.0.1:8000/actions/upload', formData, {
      headers: {
        'content-Type': 'multipart/form-data'
      }
  
  });
  console.log(result)
  } catch (error) {
    console.log(error)
  }

}