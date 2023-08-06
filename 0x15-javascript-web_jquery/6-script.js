// Update text of <header> when user clicks `DIV#update_header`
$('document').ready(function () {
  $('#update_header').on('click', function () {
    const msg = 'New Header!!!';
    $('header').text(msg);
  })
})
