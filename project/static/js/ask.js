// Manages events in /ask/

window.DATA["js_store"] = {}
function record(key, value) {
  window.DATA["js_store"][key] = value
}
function retrieve(key) {
  return window.DATA["js_store"][key]
}
record("error", false)

$('#submit').on('click', function(e) {
  record("title", $('#Title').val())
  record("email", $('#Email').val())
  record("content", $('#Content').val())

  if (validate_form()) {
    fade_out_form()
    fade_in_confirm()
  }
})

$('li.topic_list_element').on('click', function(e) {
  record("topic", this.id)

  var topic_button = $('#topic_button')
  topic_button.text("Topic: " + this.id)


  var concept_dropdown = $('#concept_dropdown')
  concept_dropdown.html("")
  record("concept", null)
  for (i = 0; i < window.DATA["concepts"][this.id].length; i++) {
    var concept = window.DATA["concepts"][this.id][i]
    concept_dropdown.append('<li class="concept_list_element" id="' + concept + '"><a>' + concept + '</a></li>')
  }
  bind_concept()
})


function bind_concept() {
  var concept_button = $('#concept_button')
  concept_button.text("Choose a Concept")

  $('li.concept_list_element').on('click', function(e) {
    record("concept", this.id)
    concept_button.text("Concept: " + this.id)
  })
}

function validate_form() {
  function show_error(error) {
    $("#error").html('<h3 style="color:white">' + error + '</h3>')
  }
  if (!retrieve("topic")) {
    show_error("Please choose a Topic")
    return false
  }
  else if (!retrieve("concept")) {
    show_error("Please choose a Concept")
    return false
  }
  else if (!retrieve("title")) {
    show_error("Please include a title")
    return false
  }
  else if (!retrieve("content")) {
    show_error("Your question must include content")
    return false
  }
  else if (!retrieve("email")) {
    show_error("You must enter an email address")
    return false
  }
  else return true
}

function fade_out_form() {
  $('.form').fadeOut(1000)
}

function fade_in_confirm() {
  var header = $('#confirm_header')
  var form = $('#confirm_form')
  header.append('<h2 style="color:white">Confirm Question</h2>')
  header.append('<h3 style="color:white">Topic: ' + retrieve("topic") + ', Concept: ' + retrieve("concept") + '</h3>')
  header.append('<br>')
  form.append('<input type="submit" class="form-control"></input>')
  form.append($('<input type="hidden" name="title" value="' + retrieve("title") + '">'))
  form.append($('<input type="hidden" name="content" value="' + retrieve("content") + '">'))
  form.append($('<input type="hidden" name="concept" value="' + retrieve("concept") + '">'))
  form.append($('<input type="hidden" name="topic" value="' + retrieve("topic") + '">'))
  form.append($('<input type="hidden" name="email" value="' + retrieve("email") + '">'))
}
