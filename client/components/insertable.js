


var idSet = new Set()

export function addMir(id){
    var table = document.getElementById("table")
    var length = document.getElementById("table").rows.length;
    id.forEach(element => {
        if(!idSet.has(element)){
        idSet.add(element)
        var newRow = table.insertRow(length)
        newRow.insertCell(0).innerText=element
        newRow.insertCell(1).innerHTML="<a href='www.dsfds.com'>Click here</a>";
        newRow.insertCell(2).innerHTML=`<button id=${element} class="del">Delete</button>`;
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
