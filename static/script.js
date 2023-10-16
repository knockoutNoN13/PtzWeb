    var i = 1;
    function addQuestion() {
        var newdiv = document.createElement("div");
        newdiv.innerHTML = "<div class='input-container'>\n<input type='text' class='inp1' name='headerName'>\n<input type='text' class='inp2' name='headerValue'>\n</div>"
         //newdiv.appendTo('div#quest');
         document.getElementById("headerClass").appendChild(newdiv);
         i++;
         return false;
  }