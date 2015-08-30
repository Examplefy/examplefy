// Manages events in /search/

window.DATA["js_store"] = {}
window.DATA["js_store"]["topic"] = null
window.DATA["js_store"]["concept"] = null
function record(key, value) {
  window.DATA["js_store"][key] = value
}
function retrieve(key) {
  return window.DATA["js_store"][key]
}

function search() {
  $("#search_input").trigger("searched.fu.search")
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
    search()
  })
}


function dynamicDataSource(options, callback) {

  // define the columns for the grid
  var columns = [
    {
      'label': 'Title',      // column header label
      'property': 'title',   // the JSON property you are binding to
      'sortable': true      // is the column sortable?
    },
    {
      'label': 'Topic',
      'property': 'topic',
      'sortable': true
    },
    {
      'label': 'Concept',
      'property': 'concept',
      'sortable': true
    },
    {
      'label': 'Date Added',
      'property': 'date',
      'sortable': true
    }
  ];

  // set options
  var pageIndex = options.pageIndex;
  var pageSize = options.pageSize;
  var options = {
    'pageIndex': pageIndex,
    'pageSize': pageSize,
    'sortDirection': options.sortDirection,
    'sortBy': options.sortProperty,
    'filterBy': options.filter.value || '',
    'searchBy': options.search || ''
  };

  var topic = retrieve("topic")
  var concept = retrieve("concept")
  $.get("/get_examples_json/", {topic: topic, concept: concept}, function(data) {
    items = data.items

    // transform array
    var pageIndex = options.pageIndex;
    var pageSize = options.pageSize;
    var totalItems = data.total;
    var totalPages = Math.ceil(totalItems / pageSize);
    var startIndex = (pageIndex * pageSize) + 1;
    var endIndex = (startIndex + pageSize) - 1;
    if (endIndex > items.length) {
      endIndex = items.length;
    }
    var rows = items.slice(startIndex - 1, endIndex);
    var dataSource = {
      'page':    pageIndex,
      'pages':   totalPages,
      'count':   totalItems,
      'start':   startIndex,
      'end':     endIndex,
      'columns': columns,
      'items':   items
    };
    // pass the datasource back to the repeater
    callback(dataSource);
  });
}

function customColumnRenderer(helpers, callback) {
        // Determine what column is being rendered and review
        // http://getfuelux.com/extensions.html#bundled-extensions-list-options
        // for more information on the helpers object.
        var column = helpers.columnAttr;

        // get all the data for the entire row
        var rowData = helpers.rowData;
        var customMarkup = '';

        // Only override the output for specific columns.
        // This will default to output the text value of the row item
        switch(column) {
          case 'title':
            customMarkup = '<a href="/example?id=' + rowData.id + '">' + rowData.title + '</a>';
            break;

          case 'topic':
            customMarkup = '<h4 style="color: white">' + rowData.topic + '</h4>';
            break;

          case 'concept':
            customMarkup = '<h4 style="color: white">' + rowData.concept + '</h4>';
            break;

          case 'date':
            customMarkup = '<h4 style="color: white">' + rowData.date + '</h4>';
            break;


          default:
            // otherwise, just use the existing text value
            customMarkup = helpers.item.text();
            break;
        }

        helpers.item.html(customMarkup);

        callback();
      }


$(function() {
  // initialize the repeater
  var repeater = $('#myRepeater');
  repeater.repeater({
    // setup your custom datasource to handle data retrieval;
    // responsible for any paging, sorting, filtering, searching logic
    dataSource: dynamicDataSource,
    // setup custom column renderer for the list view
    list_columnRendered: customColumnRenderer
  });
});
