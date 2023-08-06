// script that fetches and prints how to say “Hello” depending on the language
const url = 'https://hellosalut.stefanbohacek.dev/';
$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    let cnt = $('#language_code').val();
    if (cnt === '') {
      cnt = 'en';
    }
    const urlMod = url + '?lang=' + cnt;
    $.get(urlMod, function (data) {
      const msg = data.hello;
      $('#hello').text(msg);
    });
  });
});
