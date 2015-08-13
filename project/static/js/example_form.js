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
    var text_area = $('<textarea id="example_question" rows="14" cols="50"></textarea>')
    var submit_button = $('<button type="button" class="btn btn-primary" id="Submit">Submit your question</button>')

    text_div.append("<br><br>")
    text_div.append(text_area)
    text_div.append("<br><br>")
    text_div.append(submit_button)
    bind_confirm()
  })
}

function bind_confirm() {
  $('#Submit').on('click', function(e) {
    record("text", $('textarea.example_question').value)
    $('#ask_form').fadeOut(1000)
    var confirm_div = $('#confirm_div')
    var inner_text = $('<div class="header-content-inner"></div>')
    var topic_text = $('<h3 style="color:white">Topic: ' + retrieve("topic") + '</h3>')
    var concept_text = $('<h3 style="color:white">Concept: ' + retrieve("concept") + '</h3>')

    var confirm_form = $('#confirm_form')
    confirm_form.append($('<input type="submit" value="Submit Example" class="btn">'))
    confirm_form.append($('<input type="hidden" name="topic" value="' + retrieve("topic") + '">'))

    // dramatic entracne
    topic_text.hide()
    concept_text.hide()
    confirm_form.hide()
    inner_text.append(topic_text)
    inner_text.append("<br>")
    inner_text.append(concept_text)
    inner_text.append("<br>")
    inner_text.append(confirm_form)
    confirm_div.prepend(inner_text)

    topic_text.delay(1000).fadeIn(1000)
    concept_text.delay(1500).fadeIn(1000)
    confirm_form.delay(2000).fadeIn(1000)
  })
}

window.DATA["js_store"] = {}
function record(key, value) {
  window.DATA["js_store"][key] = value
}
function retrieve(key) {
  return window.DATA["js_store"][key]
}
