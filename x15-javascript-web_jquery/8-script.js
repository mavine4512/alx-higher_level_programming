$(document).ready(function () {
        $.getJSON(
                "https://swapi-api.alx-tools.com/api/people/5/?format=json",
                function (data) {
                        data.results.forEach(function (film) {
				$("<li>").text(film.title).appendTo("ul#list_movies");
			});
                }
        );
});
