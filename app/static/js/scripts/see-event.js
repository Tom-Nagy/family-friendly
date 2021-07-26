/* jshint esversion: 8 */

$(document).ready(function() {
    // Add eventslistener on buttons
    $(":button").on("click", function() {
        // triger the modal depending on the button clicked
        if ($(this).attr("id") === "try-cancel-event") {
            $("#see-event-overlay").addClass("overlay-active");
            $("#cancel-event-modal").addClass("modal-active");
        }
    })
})