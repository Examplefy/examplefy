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
  validate_form()

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
    $("#error").html("<h3>" + error + "</h3>")
  }
  if (!retrieve("topic")){
      show_error("You must choose a Topic")
  }
}
