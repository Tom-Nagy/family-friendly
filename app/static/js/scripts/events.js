/* jshint esversion: 8 */

$(document).ready(function(){
    // Materialize form select initialization
    $('select').material_select();

    // Materialize carousel initialization
    $('.carousel').carousel(
        {indicators: true},
    );

    // Trigger try-see-event modal
    $(":button").on("click", function() {
        if ($(this).attr("id") === "try-see-event" ) {
            $("#try-see-event-modal").addClass("modal-active");
            $("#event-overlay").addClass("overlay-active");
        }
    });
  });