/* jshint esversion: 8 */

$(document).ready(function() {
    // Trigger about modal
    $("#about-us-btn").on("click", function() {
        $("#about-modal").addClass("modal-active");
        $("#about-overlay").addClass("overlay-active");
    });

    // Hide about modal
    $("#about-modal, #about-overlay").on("click", function() {
        $("#about-modal").removeClass("modal-active");
        $("#about-overlay").removeClass("overlay-active");
    });

    // Trigger try-create modal
    $("#try-create").on("click", function() {
        $("#try-create-modal").addClass("modal-active");
        $("#home-overlay").addClass("overlay-active");
    });
});