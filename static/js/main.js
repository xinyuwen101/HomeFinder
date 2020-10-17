// Upload an images with showing the file name
$(".custom-file-input").on("change", function () {
    let fileName = $(this).val().split("\\").pop();
    $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
});
//
// const date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear();

$(document).on("click", '[data-toggle="lightbox"]', function (event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

$("#message").alert();
window.setTimeout(function () {
    $(".alert-message").alert('close');
}, 2000);