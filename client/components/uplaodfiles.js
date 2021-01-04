const axios = require('axios')
const {drawmap} = require('./drawmap')
const {drawmap2} = require('./drawmap')
const {validate} =require('./forms')

  document.getElementById('myform').addEventListener('submit', function(e) {
  e.preventDefault();
  const res = document.getElementById("checkbox").checked;
  if(!validate(res)){
    return false;
  }
  if(res){
    uploadOneHeatMap();
  }
  else{
    // upload2HeatMaps()
    upload2();
  }
},false);


function uploadOneHeatMap(){

  let formData = new FormData();
  let cluster = document.getElementById('cluster-select')
  let linkage = document.getElementById('linkage-select')

  formData.append("files", document.getElementById('mirNA').files[0]);
  formData.append("files",cluster);
  formData.append("files",linkage);


  console.log(cluster)
  console.log(linkage)
  
  axios.post('http://127.0.0.1:8000/actions/uploadone', formData, {
    headers: {
      'content-Type': 'multipart/form-data',
      "Access-Control-Allow-Origin": "*"
    }
    }).then((response) => {
      console.log(response.data)
      drawmap(response.data,"inchlib")
  }, (error) => {
    console.log(error);
  });
}

function upload2HeatMaps(){
  let formData = new FormData();
  let cluster = document.getElementById('cluster-select').value
  let linkage = document.getElementById('linkage-select').value

  formData.append("files", document.getElementById('mirNA').files[0]);
  formData.append("files", document.getElementById('target').files[0]);
  formData.append("files", document.getElementById('connection').files[0]);
  formData.append("files",cluster);
  formData.append("files",linkage);


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


function upload2(){
  axios.get('http://127.0.0.1:8000/actions/upload2').then((response) => {
      console.log(response)
      drawmap(response.data.first,"inchlib1")
      drawmap2(response.data.second,"inchlib2")
  })
}


