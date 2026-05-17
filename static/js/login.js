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

