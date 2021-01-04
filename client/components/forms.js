
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

export function validate(res){
    var input1 = document.getElementById("mirNA")
    var input2 = document.getElementById("target")
    var input3 = document.getElementById("connection")

    if(!input1.value){
        input1.classList.add("input-error");
        return false;
    }
    else{
        input1.classList.remove("input-error");
    }
    if(!res){
        if(!input2.value){
            input2.classList.add("input-error");
            return false;
        }
        else{
            input2.classList.remove("input-error");
        }

        if(!input3.value){
            input3.classList.add("input-error");
            return false;
        }
        else{
            input3.classList.remove("input-error");
        }
    }
    return true;

}