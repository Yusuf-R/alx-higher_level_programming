// Adds a <li> element to a list when the user clicks on tag `DIV#add_item`
$('document').ready(function () {
  $('#add_item').on('click', function () {
    const item = '<li>Item</li>';
    $('.my_list').append(item);
  });
});
