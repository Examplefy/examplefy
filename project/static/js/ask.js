// Manages events in /ask/

window.DATA["js_store"] = {}
function record(key, value) {
  window.DATA["js_store"][key] = value
}
function retrieve(key) {
  return window.DATA["js_store"][key]
}

$('li.topic_list_element').on('click', function(e) {
    alert("hello!")
})
