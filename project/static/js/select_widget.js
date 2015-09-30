$('li.topic_list_element').on('click', function(e) {
  // set topic
  $('#topic_button').text("Topic: " + this.id)
  $('#topic_field').attr("value", this.id)
  // reset concept
  $('#concept_button').text("Choose a Concept")
  $('#concept_field').attr("value", "")
  $('#concept_dropdown').html("")
  // restrict concept options
  $.get("/get_concepts_by_topic/", {topic: this.id}, function(data){
    for (i = 0; i < data.concepts.length; i++) {
      var concept = data.concepts[i]
      $("#concept_dropdown").append('<li class="concept_list_element" id="' + concept + '"><a>' + concept + '</a></li>')
    }
    bind_concept()
  })
})

function bind_concept() {
  $('li.concept_list_element').on('click', function(e) {
    $('#concept_button').text("Concept: " + this.id)
    $('#concept_field').attr("value", this.id)
  })
}
