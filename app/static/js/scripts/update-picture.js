/* jshint esversion: 8 */
$(document).ready(function () {

    // Credit to https://www.geeksforgeeks.org/validation-of-file-size-while-uploading-using-javascript-jquery/ 
    // for file size validation adapted to website needs.
    $('#profile_picture').on('change', function () {
    
        let size =
            (this.files[0].size / 1024 / 1024);
    
        if (size > 60 || size < 0) {
            alert("File size must be between 2-6 KB ");
            $('#profile_picture').val("")
        } else {
            $("#output").html('<b>' +
                'This file size is: ' + size + " MB" + '</b>');
        }
    });

});