// Login Page Code Goes Here
function validate(){

var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if (username == "admin" && password == "user") {
    //  alert("login succesfully");
    window.open('./admin/index.html')
    return false;

}
else {
     alert("Login Failed")
  
}
}

function SendMail(){
    var params = {
        from_name : document.getElementById("Name").value,
        email_id : document.getElementById("Email").value,
        message : document.getElementById("Message").value,
        phone : document.getElementById("Phone").value,
        subject : document.getElementById("Subject").value
    }
    emailjs.send("service_88kktfa","template_txfaohc", params).then(function(res){
        alert("Success!" + res.status)
    })
}
