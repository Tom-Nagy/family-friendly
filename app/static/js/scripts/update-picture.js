/* jshint esversion: 8 */
$(document).ready(function () {

    // Credit to https://www.geeksforgeeks.org/validation-of-file-size-while-uploading-using-javascript-jquery/ 
    // for file size validation adapted to website needs.
    $('#profile_picture').on('change', function () {
    
        let size =
            (this.files[0].size / 1024 / 1024);
    
        if (size > 6 || size < 0.002) {
            alert("File size must be between 1 KB and 6 MB ");
            // empty the input field if the size is not correct
            $('#profile_picture').val("")
        }
    });

});