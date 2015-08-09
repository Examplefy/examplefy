// Topic selection
$('li.topic_list_element').on('click', function(e) {
  // Change appearance of topic button
  var topic_button = $('#topic_button')
  topic_button.text("Topic: " + this.id)
  topic_button.attr('disabled', true)

  // Make concept selection available
  var concept_group = $('#concept_group')
  var concept_button = $('<button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" id="topic_button">Chose a Topic</button>')
  var concept_list = $('<ul class="dropdown-menu" role="menu"></ul>')
  concept_list.append('<li class="concept_list_element" id="DUMMY"><a>DUMMY</a></li>')
  //concept_button.hide()
  concept_group.append(concept_button)
  concept_group.append(concept_list)
  //concept_button.delay(1000).fadeIn(2000)
})

/*
<button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" id="topic_button">
  Chose a Topic
</button>
<ul class="dropdown-menu" role="menu">
  {% for topic in data.topics %}
    <li class="topic_list_element" id="{{ topic }}"><a>{{ topic }}</a></li>
  {% endfor %}
</ul>
*/
