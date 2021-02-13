const axios = require('axios')
const {drawmap} = require('./drawmap')
const {drawmap2} = require('./drawmap')
const {validate} =require('./forms')
const {cleanConnectionTables} = require('./drawmap')

  document.getElementById('myDefForm').addEventListener('submit', function(e) {
  var errorM = document.getElementById("error-message")
  e.preventDefault();
  const res = document.getElementById("checkbox-maps-choose").checked;
  if(!validate(res)){
    setTimeout(function(){ 
    errorM.classList.remove("error-m")
    errorM.innerHTML="&nbsp;"
    },3000)
    errorM.classList.add("error-m")
    errorM.innerText="* Some files are required"
    return false;
  }

  document.getElementById("spinner").style.display="block";
  if(res){
    uploadOneHeatMap();
  }
  else{
    upload2HeatMaps()

  }
},false);


function uploadOneHeatMap(){

  let formData = new FormData();
  let properties = {}
  
  formData.append("files", document.getElementById('mirNA').files[0]);

  properties = propertiesFilePrepare('mirNA',"mirNA-metadata",'checkbox-meta-data1')

  if(properties['metadata'] == 1) 
    formData.append("files", document.getElementById('mirNA-metadata').files[0])

  properties['raw_distance'] = document.getElementById('distance-select').value
  properties['raw_linkage'] = document.getElementById('linkage-select').value
  properties['both1']=0
  if(document.getElementById("miRNA-clust-select").value == "Both"){
    properties['both1']=1
    properties['column_distance'] = document.getElementById('distance-select-column').value
    properties['column_linkage'] = document.getElementById('linkage-select-column').value
  }

  formData.append("files", JSON.stringify(properties));

    axios.post('http://127.0.0.1:8000/actions/uploadone', formData, {
      headers: {
        'content-Type': 'multipart/form-data',
        "Access-Control-Allow-Origin": "*"
      }
      }).then((response) => {
        cleanConnectionTables();
        drawmap(response.data,"inchlib")
    }, (error) => {
      console.log(error);
    });
}

function upload2HeatMaps(){
  let formData = new FormData();

  let properties = {}
  let propertiesSecond = {}

  formData.append("files", document.getElementById('mirNA').files[0]);
 
  properties = propertiesFilePrepare('mirNA',"mirNA-metadata",'checkbox-meta-data1')

  if(properties['metadata'] == 1) 
    formData.append("files", document.getElementById('mirNA-metadata').files[0])


  // Second Map

  formData.append("files", document.getElementById('target').files[0]);

  propertiesSecond = propertiesFilePrepare('target','target-metadata','checkbox-meta-data2')

  if(propertiesSecond['metadata'] == 1) 
    formData.append("files", document.getElementById('target-metadata').files[0])


  //Connections
  formData.append("files", document.getElementById('connection').files[0])

  properties['file2'] = propertiesSecond['file1']
  properties['metadata2'] = propertiesSecond['metadata']

  // Clustering

  properties['raw_distance'] = document.getElementById('distance-select').value
  properties['raw_linkage'] = document.getElementById('linkage-select').value
  properties['both1'] = 0
  if(document.getElementById("miRNA-clust-select").value == "Both"){
    properties['both1']=1
    properties['column_distance'] = document.getElementById('distance-select-column').value
    properties['column_linkage'] = document.getElementById('linkage-select-column').value
  }

  properties['raw_distance2'] = document.getElementById('distance-select').value
  properties['raw_linkage2'] = document.getElementById('linkage-select').value
  properties['both2'] = 0
  if(document.getElementById("target-clust-select").value == "Both"){
    properties['both2'] = 1
    properties['column_distance2'] = document.getElementById('distance-select-column2').value
    properties['column_linkage2'] = document.getElementById('linkage-select-column2').value
  }


  formData.append("files", JSON.stringify(properties));

  axios.post('http://127.0.0.1:8000/actions/upload', formData, {
    headers: {
      'content-Type': 'multipart/form-data',
      "Access-Control-Allow-Origin": "*"
    }
    }).then((response) => {
      localStorage.setItem('uuid',response.headers.uuid)
      cleanConnectionTables();
      drawmap(response.data.first,"inchlib1");
      drawmap2(response.data.second,"inchlib2");

      var first_second_connections= response.data.first_second_connections;
      localStorage.setItem('first_second_connections',JSON.stringify(first_second_connections))

      var second_first_connections= response.data.second_first_connections;
      localStorage.setItem('second_first_connections',JSON.stringify(second_first_connections))

      }, (error) => {
        console.log(error);
      });
}



function propertiesFilePrepare(id1,id2,id3){
  if(document.getElementById(id1).files[0] && document.getElementById(id2).files[0] && document.getElementById(id3).checked){
    properties ={
      file1:'1',
      metadata:'1',
    }
  }
else{
  properties ={
      file1:'1',
      metadata:'0',
  }
}
return properties
}