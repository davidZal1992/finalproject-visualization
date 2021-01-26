
var idSet = new Set()

export function addMir(id, idMap){
    if(idMap==='inchlib1'){// add mir only if the mir map was clicked
        var table = document.getElementById("table-connect-1to2")
        var length = document.getElementById("table-connect-1to2").rows.length;
        var connection_kind= "connect_1to2";
    }
    else{
        var table = document.getElementById("table-connect-2to1")
        var length = document.getElementById("table-connect-2to1").rows.length;
        var connection_kind= "connect_2to1";

    }
        id.forEach(element => {
            if(!idSet.has(element)){
            idSet.add(element)
            var newRow = table.insertRow(length)
            newRow.insertCell(0).innerText=element
            var element_getDetailes= element+"-getDetailes-"+connection_kind;
            console.log(element_getDetailes);
            newRow.insertCell(1).innerHTML=`<button id=${element_getDetailes}  type='button' >Click here</button>`;
            newRow.insertCell(2).innerHTML=`<i id=${element} style="color:red;"class="fas fa-trash-alt"></i>`;
            document.getElementById(element).addEventListener('click', deleteId);
            document.getElementById(element_getDetailes).addEventListener('click', targetConnection);
            length++;

            }
        });  
}

function deleteId(event){
    var td = event.target.parentNode; 
    var tr = td.parentNode; // the row to be removed
    tr.parentNode.removeChild(tr);
}

function targetConnection(event){
    var td = event.target.parentNode; 
    var Left_element = td.children[0].id;
    var Left_element_array = Left_element.split('-');
    var Left_element_deatils=Left_element_array[0];
    var connection_kind=Left_element_array[2];

    console.log(Left_element_deatils);
    console.log(connection_kind);
    console.log("here");

    var connection_list = document.getElementById("connection_list");
    //get just once the connection from the server as two dictionary

    if(connection_kind==="connect_1to2"){
        connection_list.textContent="target1, target2, target3"; //dict_1to2 content
    }
    else{
        connection_list.textContent="miRna1, miRna2, miRna3"; //dict_1to2 content

    }

    $('#connection-dialog').modal('show');
    
    
}

