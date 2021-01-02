
//Choose how much maps display
document.getElementById('checkbox').addEventListener('click', showHide);


function showHide(){
    const res = document.getElementById("checkbox").checked;
    var settings = document.getElementById("checkbox-option");
    if(res){
        settings.style.display="none"; 
    }
    else{
        settings.style.display="block";  
    }
}