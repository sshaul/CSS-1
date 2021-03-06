function setDeleteFormItem(string, resourceType){

  $('#' + resourceType).val(string);

}
function setEditFormFields(name, resourceType){

  var table = $("#table")[0];
  for (var i = 0, row; row = table.rows[i]; i++) {

    if(row.cells[1].innerHTML == name)
    {
      if(resourceType == 'room')
      {
        $("#edit_room_name").val(name);
        $("#edit_room_description").val(row.cells[2].innerHTML);
        $("#edit_room_capacity").val(row.cells[3].innerHTML);
        $("#edit_room_notes").val(row.cells[4].innerHTML);
        $("#edit_room_equipment").val(row.cells[5].innerHTML);
      }
      else if(resourceType == 'course')
      {
        $("#edit_course_course_name").val(name);
        $("#edit_course_equipment_req").val(row.cells[2].innerHTML);
        $("#edit_course_description").val(row.cells[3].innerHTML);
      }
    }
  }
}

/*-----------------------------------Resources Page----------------------------------------------*/
var currentCourse;
var csrf;

  function addSectionType() {
    $('#add-section-type-area').show();
    $('#save-section-type-button').show();
    $('#add-section-type-button').hide()
  }
  function submitSectionType() {
    var checkBoxes = $("input[name='name']");

    for (var i = 0; i < checkBoxes.length; i++)
    {
      if(checkBoxes[i].checked)
      {
        var selectedSectionType = checkBoxes[i].value;
        break;
      }

    }

    $.post("/resources/courses/",
          {
              "csrfmiddlewaretoken": csrf,
              "request-name":'save-section-request',
              "course": currentCourse,
              "id_name": selectedSectionType,
              "id_work_units": $('#id_work_units').val(),
              "id_work_hours": $('#id_work_hours').val()
          },

          updateSectionTypesView
    );

    $('#add-section-type-area').hide();
    $('#save-section-type-button').hide();
    $('#add-section-type-button').show()
  }

  function getCourseInfo(course) {
    currentCourse = course;
    csrf = $('#csrf-token').html();

    $.post("/resources/courses/",
          {
              "csrfmiddlewaretoken": csrf,
              "request-name": "course-section-request",
              "course": course
          },

          updateSectionTypesView
    );
  }

  function deleteSectionType(sectionTypeName, courseName) {
    $.post("/resources/courses/",
          {
              "csrfmiddlewaretoken": csrf,
              "request-name": "delete-section-type-request",
              "course": courseName,
              "section_type_name": sectionTypeName
          },

          updateSectionTypesView
    );
  }
  function updateSectionTypesView(data, status){
     var sectionTypes = JSON.parse(data);
      $('#ajax-area').empty();

     for(var sectionType in sectionTypes) {
       $('#ajax-area').append("<p><button onclick=\"deleteSectionType('" + sectionTypes[sectionType].section_type_name + "', '" + sectionTypes[sectionType].course_name + "')\"style=\"font-size: .7em;\" type=\"button\" class=\"btn btn-info btn-xs\" data-toggle=\"modal\" data-target=\"#add-section-type\"><span class=\"glyphicon glyphicon-minus\"></button> " + sectionTypes[sectionType].section_type_name + " Work Units: " + sectionTypes[sectionType].work_units + " Work Hours: " + sectionTypes[sectionType].work_hours + "</p>");
    }
  }
