function postREST() {
	var csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
	var fk_usuario_comentario = $('#fk_usuario_comentario').val();
	var fk_receita_comentario = $('#fk_receita_comentario').val();
	var texto_comentario = $('#texto_comentario').val();
	var body = {
	  'csrfmiddlewaretoken': csrfmiddlewaretoken,
	  'fk_usuario_comentario': fk_usuario_comentario,
	  'fk_receita_comentario': fk_receita_comentario,
	  'texto_comentario': texto_comentario,
	};  	
	$.post('http://127.0.0.1:8000/home/cadastroComentario/?format=json', body, function(data, textStatus, xhr) {
		console.log(data)
		var $rateYo = $("#rateYo").rateYo();
    var rating = $rateYo.rateYo("rating");
    var body2 = {
    	'csrfmiddlewaretoken': csrfmiddlewaretoken,
    	'nota': rating,
    	'receita': fk_receita_comentario
    }
    $.post('http://127.0.0.1:8000/home/avaliar/?format=json', body2, function(data, textStatus, xhr) {
			console.log(data)
			location.reload();
		}).fail(function (data, textStatus, xhr) {
			console.log(data)
		});
	}).fail(function (data, textStatus, xhr) {
		console.log(data)
	});
}

function sendForm(){
	var form = document.getElementById("cadastroComentario");
	form.addEventListener("submit", function(event) {
		if (form.checkValidity() != false) {
			event.preventDefault();
			event.stopPropagation();
			postREST();
		}
	}, false);
}

$(document).ready(function() {
	sendForm();
	$("#rateYo").rateYo({
    rating: 0,
    fullStar: true
  });
  $("#rateYo").rateYo()
    .on("click", function () {
 		var $rateYo = $("#rateYo").rateYo();
    var rating = $rateYo.rateYo("rating");
   	console.log(rating);
   });
});