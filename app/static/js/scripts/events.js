/* jshint esversion: 8 */

$(document).ready(function(){
    // Materialize carousel initialization
    $('.carousel').carousel(
        {indicators: true},
    );

    // Trigger try-see-event modal
    $("#try-see-event").on("click", function() {
        $("#try-see-event-modal").addClass("modal-active");
        $("#event-overlay").addClass("overlay-active");
    });
  });