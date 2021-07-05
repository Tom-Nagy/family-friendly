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
});