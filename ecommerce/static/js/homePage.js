function activateSearch(){
    var searchWord = document.getElementById('homeSearch').value;
    window.location.href = "/search/?query=" + searchWord
}
function sendToRegistration(){
    window.location.href = "/register/"
}

function sendToAdminPanel() {
    window.location.href = "/admin/"
}

function sendToCart() {
    window.location.href = "/cart/"
}