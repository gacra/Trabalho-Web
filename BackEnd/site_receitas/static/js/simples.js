function printPage() {
	window.print();
}

$(document).ready(function() {
	console.log('hey')
	$('#id').on('click', function(event) {
		event.preventDefault();
		window.print();
	});
});