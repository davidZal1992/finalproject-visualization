
var idSet = new Set()

export function addMir(id, idMap){
    if(idMap==='inchlib1'){// add mir only if the mir map was clicked
        var table = document.getElementById("table-connect-1to2")
        var length = document.getElementById("table-connect-1to2").rows.length;
    }
    else{
        var table = document.getElementById("table-connect-2to1")
        var length = document.getElementById("table-connect-2to1").rows.length;
    }
        id.forEach(element => {
            if(!idSet.has(element)){
            idSet.add(element)
            var newRow = table.insertRow(length)
            newRow.insertCell(0).innerText=element
            newRow.insertCell(1).innerHTML="<a href='www.dsfds.com'>Click here</a>";
            newRow.insertCell(2).innerHTML=`<i id=${element} style="color:red;"class="fas fa-trash-alt"></i>`;
            document.getElementById(element).addEventListener('click', deleteId);
            length++;
            }
        });  
}

function deleteId(event){
    var td = event.target.parentNode; 
    var tr = td.parentNode; // the row to be removed
    tr.parentNode.removeChild(tr);
}
