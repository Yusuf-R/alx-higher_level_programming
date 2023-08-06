// Fetches character name from given URL
url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$.get(url, function (data) {
  const msg = data.name;
  $('#character').text(msg)
});
