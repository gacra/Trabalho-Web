function postREST() {
	var autor = $('#autor').val();
	var nome = $('#nome').val();
	var descricao = $('#descricao').val();
	var categoria = $('#categoria').val();
	var porcoes = $('#porcoes').val();
	var nutri = $('#nutri').val();
	var tempo = $('#tempo').val();
	var instrucoes = $('#instrucoes').val();
	var cozimento = $('#cozimento').val();
	var body = {
	  'autor': autor,
	  'nome_receita': nome,
	  'descricao': descricao,
	  'categoria': categoria,
	  'procoes': porcoes,
	  'val_nutricional': nutri,
	  'tempo_preparo': tempo,
	  'instrucoes_preparo': instrucoes,
	  'metodo_cozimento': cozimento,
	  'rating': 0,
	  'num_votos' : 0,
	  'ingredientes': [{'nome_ingrediente': 'Banana', 'quantidade': 2, 'unidade': 'unidades'},{'nome_ingrediente': 'Banana2', 'quantidade': 22, 'unidade': 'unidades2'}],
	  'imagens': [],
	};
	console.log(JSON.stringify(body));

	var teste =     {
      'json_data': JSON.stringify(body),
      "type": 'clone',
      "csrfmiddlewaretoken": Cookies.get('csrftoken')
    }

	$.post('http://127.0.0.1:8000/home/cadastroReceita/?format=json', teste, function(data, textStatus, xhr) {
	}).fail(function (data, textStatus, xhr) {
		console.log(data)
	});
}

function sendForm(){
	var form = document.getElementById("cadastroReceita");
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
});