// Manages events in /search/

window.DATA["js_store"] = {}
function record(key, value) {
  window.DATA["js_store"][key] = value
}
function retrieve(key) {
  return window.DATA["js_store"][key]
}

$('li.topic_list_element_search').on('click', function(e) {
  record("topic", this.id)

  var topic_button = $('#topic_button_search')
  topic_button.text("Topic: " + this.id)

  var concept_dropdown = $('#concept_dropdown_search')
  concept_dropdown.html("")
  record("concept", null)
  for (i = 0; i < window.DATA["concepts"][this.id].length; i++) {
    var concept = window.DATA["concepts"][this.id][i]
    concept_dropdown.append('<li class="concept_list_element_search" id="' + concept + '"><a>' + concept + '</a></li>')
  }
  bind_concept_search()
  search()
})


function bind_concept_search() {
  var concept_button = $('#concept_button_search')
  concept_button.text("Choose a Concept")

  $('li.concept_list_element_search').on('click', function(e) {
    record("concept", this.id)
    concept_button.text("Concept: " + this.id)
  })
}

function search() {
  var topic = retrieve("topic")
  var concept = retrieve("concept")
  $.get("/get_examples/", {topic: topic, concept: concept}, function(data) {
    var ids = data.split(",")
    display_examples(ids)
  });
}

function make_div_from_id() {

}

function display_examples(ids) {
  for (var i = 0; i < ids.length; i++) {
    var div = make_div_from_id(ids[i])
    $('#example_list').append(div)
  }
}
