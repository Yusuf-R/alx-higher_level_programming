// Fetches and list title of all movies from URL
url = 'https://swapi-api.alx-tools.com/api/films/?format=json'
$.get(url, function (data) {
  let i = 0;
  if (data.results.length === 0) {
    $('#list_movies').empty();
    return
  }
  else {
    let msg = data.results;
    while(i < msg.length) {
      $('#list_movies').append(`<li>${msg[i].title}</li>`);
      i++;
      //$('#list_movies').append(msg[i].title + '<br />');
      //console.log(msg[i]);
      //i++;
    }
  }

});
