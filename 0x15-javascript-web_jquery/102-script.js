// script that fetches and prints how to say “Hello” depending on the language
$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
