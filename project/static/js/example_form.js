// Topic selection
$('li.topic_list_element').on('click', function(e) {
  // record selection
  record("topic", this.id)

  // Change appearance of topic button
  var topic_button = $('#topic_button')
  topic_button.text("Topic: " + this.id)
  topic_button.attr('disabled', true)

  // Make concept selection available
  var concept_group = $('#concept_group')
  var concept_button = $('<button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" id="concept_button">Chose a Concept</button>')
  var concept_list = $('<ul class="dropdown-menu" role="menu"></ul>')
  for (i = 0; i < window.DATA["concepts"][this.id].length; i++) {
    var concept = window.DATA["concepts"][this.id][i]
    concept_list.append('<li class="concept_list_element" id="' + concept + '"><a>' + concept + '</a></li>')
  }
  concept_group.append(concept_button)
  concept_group.append(concept_list)
  bind_concept()
})



function bind_concept() {
  $('li.concept_list_element').on('click', function(e) {
    // record selection
    record("concept", this.id)
    // Change appearance of concept button
    var concept_button = $('#concept_button')
    concept_button.text("Concept: " + this.id)
    concept_button.attr('disabled', true)

    // Make the text box available
    var text_div = $('#text_div')
    var text_area = $('<textarea rows="14" cols="50"></textarea>')
    var submit_button = $('<button type="button" class="btn btn-primary" id="Submit" onclick="submit()">Submit your question</button>')

    text_div.append("<br><br>")
    text_div.append(text_area)
    text_div.append("<br><br>")
    text_div.append(submit_button)
  })
}

function submit(topic, concept) {
  record("text", $('textarea')[0].value)
  var data = window.DATA.js_store
  $.get("/add_example/", data)
}

window.DATA["js_store"] = {}
function record(key, value) {
  window.DATA["js_store"][key] = value
}
function retrieve(key) {
  return window.DATA["js_store"][key]
}
