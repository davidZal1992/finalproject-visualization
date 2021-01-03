const axios = require('axios')
const {drawmap} = require('./drawmap')
const {drawmap2} = require('./drawmap')
const Papa = require('papaparse');

document.getElementById('buttonid').addEventListener('click', generate);

function generate() {
  
  const res = document.getElementById("checkbox").checked;
  if(res){
    uploadOneHeatMap();
  }
  else{
    // upload2HeatMaps()
    upload2();
  }
}

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
      drawmap(response.data)
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
      drawmap(response.data.first)
      drawmap2(response.data.second)
      var connection_file= document.getElementById('connection').files[0];
      var newArray=[];
      parseMe(connection_file, newArray = doStuff);
      console.log('(Log no.2) After parse call but before complete fired, newArray:', newArray, new Date());
      console.log('(Log no.3) ',newArray);
  }, (error) => {
    console.log(error);
  });
}

function parseMe(url, callBack){
  Papa.parse(url, {
      complete: function(results) {
      callBack(results.data[0]);
      }
  });
}

function doStuff(data){
  var newArray=data;
  console.log('(Log no.1) In OnComplete callback, Array is:', new Date(), newArray); //log no. 1
  return newArray;
}



