function submitForm(){

    let pass = document.getElementById("password").value;
    let confirm = document.getElementById("confirm").value;
    
    if(pass !== confirm){
        alert("Passwords do not match");
        return;
    }
    
    if(!document.getElementById("terms").checked){
        alert("Please accept terms");
        return;
    }
    
    window.location.href = "success.html";
    }
    