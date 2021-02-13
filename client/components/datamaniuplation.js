const axios = require('axios')


var wichTableWorkOn;
var clusterManipluate;
document.getElementById('preprocess1').addEventListener('click',(e) =>{
    wichTableWorkOn="first_second"
},false)


document.getElementById('preprocess2').addEventListener('click',(e) =>{
    wichTableWorkOn="second_first"
},false)


document.getElementById('mainuplate-data').addEventListener('click',(e) =>{
    dataManipulate();
},false)


document.getElementById('target-clust-select-manipul').addEventListener('change',changeSelectClusterManipulate)




function dataManipulate(){

    let properties = {}
    let checkIfBoth = document.getElementById('target-clust-select-manipul').value
    let action = document.getElementById('action').value
    let linkage1 = document.getElementById('linkage-select-manipulate').value
    let distance1 = document.getElementById('distance-select2-manipulate').value
    let values = getAllValues(wichTableWorkOn ==="first_second" ? "table-connect-1to2" :"table-connect-2to1" )
    properties['data_work_on'] = wichTableWorkOn;
    properties['action'] = (action+"").toLowerCase()
    properties['cluster'] = checkIfBoth
    properties['linakge1'] = linkage1
    properties['distance1'] = linkage1
    

    if(checkIfBoth==='Both'){
        properties['linakge2'] = document.getElementById('linkage-select-column-manipulate').value
        properties['distance2'] = document.getElementById('distance-select-column2-manipulate').value
    }

    properties['values'] = values

    sendToServer(properties)

}



function sendToServer(properties){

    axios.post('http://127.0.0.1:8000/actions/'+properties['action'], properties, {
      headers: {
        'content-Type': 'application/json',
        "Access-Control-Allow-Origin": "*"
      }
      }).then((response) => {
        console.log(response)
    }, (error) => {
      console.log(error);
    });

}


function changeSelectClusterManipulate(event){

    if(event.target.value === 'Both'){
        document.getElementById('mir-linkage-column-manipulate').style.display='block'
        document.getElementById('tgt-distance-column-manipulate').style.display='block'
    }
    else{
        document.getElementById('mir-linkage-column-manipulate').style.display='none'
        document.getElementById('distance-select-column2-manipulate').style.display='none'
    }   


}


function getAllValues(tableName){
    let array = []
    $('#'+tableName+' tbody tr td:nth-child(1)').each( function(){
        //add item to array
        array.push( $(this).text() );       
     });
     return array;
}