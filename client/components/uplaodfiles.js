const axios = require('axios')
const {drawmap} = require('./drawmap')
const {drawmap2} = require('./drawmap')
const {validate} =require('./forms')

  document.getElementById('myDefForm').addEventListener('submit', function(e) {
  var errorM = document.getElementById("error-message")
  e.preventDefault();
  const res = document.getElementById("checkbox").checked;
  if(!validate(res)){
    setTimeout(function(){ 
    errorM.classList.remove("error-m")
    errorM.innerHTML="&nbsp;"
    },3000)
    errorM.classList.add("error-m")
    errorM.innerText="* Some files are required"
    return false;
  }
  if(res){
    uploadOneHeatMap();
  }
  else{
    upload2HeatMaps()
    // upload2();
  }
},false);


function uploadOneHeatMap(){

  let formData = new FormData();
  let cluster = document.getElementById('cluster-select').value
  let linkage = document.getElementById('linkage-select').value

  formData.append("files", document.getElementById('mirNA').files[0]);
  formData.append("files",cluster);
  formData.append("files",linkage);


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
  let cluster_detailes_1 = document.getElementById('miRNA-clust-select').value
  let cluster_detailes_2 = document.getElementById('target-clust-select').value

  formData.append("files", document.getElementById('mirNA').files[0]);
  formData.append("files", document.getElementById('target').files[0]);
  formData.append("files", document.getElementById('connection').files[0]);
  formData.append("files", document.getElementById('mirNA-metadata').files[0]);
  formData.append("files",cluster);
  formData.append("files",linkage);
  formData.append("files",cluster_detailes_1);
  formData.append("files", document.getElementById('target-metadata').files[0]);
  formData.append("files",cluster_detailes_2);


  axios.post('http://127.0.0.1:8000/actions/upload', formData, {
    headers: {
      'content-Type': 'multipart/form-data',
      "Access-Control-Allow-Origin": "*"
    }
    }).then((response) => {
      console.log(response.data)
      drawmap(response.data.first,"inchlib1");
      drawmap2(response.data.second,"inchlib2")
  }, (error) => {
    console.log(error);
  });
}




      // var dict_1to2= response.data.dict_1to2;
      // var dict_1to2_content = JSON.stringify(dict_1to2);

      // var fs = require('fs');
      // fs.writeFile("/resources/dict_1to2.json", dict_1to2_content, function(err, result) {
      //     if(err) console.log('error', err);
      // });

