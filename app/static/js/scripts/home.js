/* jshint esversion: 8 */

$(document).ready(function() {
    $("#about-us-btn").on("click", function() {
        $("#about-modal").addClass("modal-active");
        $("#about-overlay").addClass("overlay-active");
    });
    $("#about-modal, #about-overlay").on("click", function() {
        $("#about-modal").removeClass("modal-active");
        $("#about-overlay").removeClass("overlay-active");
    });
});