function notifyUserAboutCreatedAccount() {
    window.alert("Congratulations! You have created an account")
}

function goToHomePage(){
    window.location.href = "/home/"
}

function goToLoginPage(){
    window.location.assign("http://127.0.0.1:8000/accounts/login/")
}