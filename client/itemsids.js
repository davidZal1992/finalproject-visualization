
var idSet = new Set()

function addMir(id){
    var table = document.getElementById("table")
    var length = document.getElementById("table").rows.length;
    id.forEach(element => {
        if(!idSet.has(element)){
        idSet.add(element)
        var newRow = table.insertRow(length)
        cell = newRow.insertCell(0).innerText=element
        cell = newRow.insertCell(1).innerHTML="<a href='www.dsfds.com'>Click here</a>";
        cell = newRow.insertCell(2).innerHTML=`<button onClick="deleteId(this)" class="del">Delete</button>`;
        length++;
        }
    });   
}

function deleteId(deleteRow){
var parent=deleteRow.parentNode.parentNode;
parent.parentNode.removeChild(parent);
}


function checkIfExists(){
    
}