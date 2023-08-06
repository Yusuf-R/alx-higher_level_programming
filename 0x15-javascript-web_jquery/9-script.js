// Fetch from an api and translate
// get to say hello
const api_route = "https://hellosalut.stefanbohacek.dev/?lang=fr"
$.get(api_route, function (data) {
  $('#hello').text(data.hello);
});
