const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  const rslt = data.results;
  for (let i = 0; i < rslt.length; i++) {
    $('UL#list_movies').append('<li>' + rslt[i].title + '</li>');
  }
});
