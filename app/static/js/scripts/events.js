/* jshint esversion: 8 */

$(document).ready(function(){
    // Materialize form select initialization
    $('select').material_select();

    // Materialize collapsible initialization
    $('.collapsible').collapsible();

    // Trigger try-see-event modal
    $(":button").on("click touchend", function() {
        if ($(this).attr("id") === "try-see-event" ) {
            $("#try-see-event-modal").addClass("modal-active");
            $("#event-overlay").addClass("overlay-active");
        }
    });
  });