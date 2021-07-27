/* jshint esversion: 8 */

$(document).ready(function() {
    // Add eventslistener on buttons
    // triger the modal depending on the button clicked
    $(":button").on("click", function() {
        // triger cancel event modal
        if ($(this).attr("id") === "try-cancel-event") {
            $("#see-event-overlay").addClass("overlay-active");
            $("#cancel-event-modal").addClass("modal-active");
            
        // triger leave event modal
        } else if ($(this).attr("id") === "try-leave-event") {
            $("#see-event-overlay").addClass("overlay-active");
            $("#leave-event-modal").addClass("modal-active");
        }
    })
})