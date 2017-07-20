function $(element) {
     return document.getElementById(element);
}

var blSubmit = $('save');
var blName = $('bl_title');
var blDescription = $('bl_description');
var blList = $('list_bucketlists');
var blArray = [];
var bltitle = $('a');

blSubmit.addEventListener('click', function(e) {
    e.preventDefault();
    var title = blName.value.trim();
    var description = blDescription.value.trim();

    var newLI = document.createElement('li');
    newLI.appendChild(document.createTextNode(title+": "+description));
    
    blArray.push(title+":"+description);
    blList.appendChild(newLI);
    
    blName.value = '';
    blDescription.value = '';
    bltitle.innerHTML = "Added bucketlists";


}, false);