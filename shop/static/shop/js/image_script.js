/**
 * Displays filename before admin adds or replaces an image.
 */
$("#new-image").on("change", function () {
    var file = $("#new-image")[0].files[0];
    $("#filename").text(`Image will be set to: ${file.name}`);
});
