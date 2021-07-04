/* jshint esversion: 8 */

// Implementation of Materialize(https://materializecss.com/) functionality => Mcss
$(document).ready(function () {
  // Mcss
  $(".dropdown-button").dropdown();
  
  // button to close flash messages
  $("#close-flash").click(function() {
    $("#flash-messages").remove();
  });
});
