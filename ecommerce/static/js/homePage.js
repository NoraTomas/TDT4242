function activateSearch(){
    var searchWord = document.getElementById('homeSearch').value;
    alert(searchWord)
    window.location.href = "/search/?query=" + searchWord
}