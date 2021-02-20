

$(document).ready(function() {
    var max_fields = 10;
    var wrapper = $(".container1");
    var add_button = $(".add_form_field");

    var x = 1;
    $(add_button).click(function(e) {
        e.preventDefault();
        if (x < max_fields) {
            x++;
            $(wrapper).append('<div class="input-group mb-3" id="add"><button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><input type="text" class="form-control" aria-label="Text input with dropdown button"></div><a href="#" class="delete">Delete</a></div>'); //add input box
} else {
            alert('You Reached the limits')
        }
    });

    $(wrapper).on("click", ".delete", function(e) {
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});

$("#zoomLectureLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><span class="input-group-text" id="basic-addon3">Zoom Lecture Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3"><span class="input-group-text" id="basic-addon3">Meeting Time</span><input type="text" aria-label="Time" class="form-control">')
})

$("#zoomRecitationLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><span class="input-group-text" id="basic-addon3">Zoom Lecture Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3"><span class="input-group-text" id="basic-addon3">Meeting Time</span><input type="text" aria-label="Time" class="form-control">')
})

$("#zoomOfficeLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><span class="input-group-text" id="basic-addon3">Zoom Lecture Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3"><span class="input-group-text" id="basic-addon3">Meeting Time</span><input type="text" aria-label="Time" class="form-control">')
})

$("#discordLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li><li><a class="dropdown-item" href="#" id="zoomRecitationLink">Zoom Recitation</a></li><li><a class="dropdown-item" href="#" id="zoomOfficeLink">Zoom Office Hours</a></li><li><a class="dropdown-item" href="#" id="discordLink">Discord</a></li><li><a class="dropdown-item" href="#" id="groupMeLink">Group Me</a></li><li><a class="dropdown-item" href="#" id="slackLink">Slack</a></li><li><a class="dropdown-item" href="#" id="topHatLink">TopHat</a></li><li><a class="dropdown-item" href="#" id="canvasLink">Canvas</a></li><li><a class="dropdown-item" href="#" id="gradescopeLink">Gradescope</a></li></ul><span class="input-group-text" id="basic-addon3">Discord Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">')
  console.log($("#add"));
})

$("#groupMeLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Group</a></li></ul><span class="input-group-text" id="basic-addon3">Groupme Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">')
})

$("#slackLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><span class="input-group-text" id="basic-addon3">Slack Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">')
})

$("#tophatLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><span class="input-group-text" id="basic-addon3">Top Hat Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">')
})

$("#canvasLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><span class="input-group-text" id="basic-addon3">Canvas Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">')
})

$("#gradescopeLink").click(function() {
  $("#add").html('<button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button><ul class="dropdown-menu" id="breakpoint"><li><a class="dropdown-item" href="#" id="zoomLectureLink">Zoom Lecture</a></li></ul><span class="input-group-text" id="basic-addon3">Gradescope Link</span><input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">')
})


function zoomField() {
  var zoom = document.getElementById("zoomLi");

}
