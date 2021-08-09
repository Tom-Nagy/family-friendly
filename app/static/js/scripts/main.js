/* jshint esversion: 8 */

// Implementation of Materialize(https://materializecss.com/) functionality => Mcss
$(document).ready(function () {
  // Mcss
  $(".dropdown-button").dropdown();

  // function to close flash messages
  $(":button").click(function () {
    if ($(this).attr("id") === "close-flash") {
      $("#flash-messages").remove();
    }
  });

  // Trigger try-contact modal
  $("#try-contact").on("click", function () {
    $("#try-contact-modal").addClass("modal-active");
    $("#footer-overlay").addClass("overlay-active");
  });
});