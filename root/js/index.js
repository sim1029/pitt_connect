var buttons = document.getElementsByClassName("remove-btn");
var editBtn = document.getElementById("edit-btn");

editBtn.onclick = function() {
  if (buttons[0].style.display === "none") {
    for(var i = 0; i<buttons.length; i++){
      buttons[i].style.display = "block";
    }
    editBtn.innerText = "End Editing";
  } else {
    for(var i = 0; i<buttons.length; i++){
      buttons[i].style.display = "none";
    }
    editBtn.innerText = "Edit Courses";
  }
}
