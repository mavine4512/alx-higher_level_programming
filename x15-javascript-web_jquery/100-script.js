document.addEventListener("DOMContentLoaded", function() {
	var headerElement = document.querySelector("header");

	if (headerElement) {
		headerElement.style.color = "#FF0000";
	} else {
		console.error("Header element not found.");
	}
});
