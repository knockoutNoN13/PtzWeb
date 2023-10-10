    function addQuestion() {
        var newdiv = document.createElement("div");
        newdiv.innerHTML = "<input type='text'>"
         //newdiv.appendTo('div#quest');
         document.getElementById("headerClass").appendChild(newdiv);
         return false;
  }