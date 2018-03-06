function activateSearch(){
    var searchWord = document.getElementById('homeSearch').value;
    window.location.href = "/search/?query=" + searchWord
}
function sendToRegistration(){
    window.location.href = "/signup/"
}

function sendToAdminPanel() {
    window.location.href = "/admin/"
}

function sendToCart() {
    window.location.href = "/cart/"
}

function sendToSearch() {
    window.location.href = "/search/"
}

function addItemToCart(id) {
    window.location.href = "/add_item/" + id
}