// fetches and prints how to say “Hello” depending on the language
// it will capture both the enter key and the submit button
const url = 'https://hellosalut.stefanbohacek.dev/';
$(document).ready(function () {
  function handleEvent () {
    let cnt = $('#language_code').val();
    if (cnt === '') {
      cnt = 'en';
    }
    const urlMod = url + '?lang=' + cnt;
    $.get(urlMod, function (data) {
      const msg = data.hello;
      $('#hello').text(msg);
    });
  }

  $('#btn_translate').on('click', handleEvent);
  $('#language_code').on('keyup', function (event) {
    if (event.key === 'Enter') {
      handleEvent();
    }
  });
});
