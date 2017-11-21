ingredientesViewModel = new IngredientesViewModel()

function Ingrediente() {
	var self = this;
	self.nomeIngrediente = ko.observable();
  self.qtdeIngrediente = ko.observable();
  self.unidadeIngrediente = ko.observable();
}

function IngredientesViewModel() {
  var self = this;
  self.ingredientes = ko.observableArray([new Ingrediente()]);
  
  self.novoIngrediente = function () {
  	self.ingredientes.push(new Ingrediente());
  }

  self.removeIngrediente = function () {
  	if(self.ingredientes().length > 1){
  		self.ingredientes.pop();
  	}
  }
}

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
	  'ingredientes': [],
	  'imagens': [],
	};

	var innerArray = ingredientesViewModel.ingredientes();
  $(innerArray).each(function(index, el) {
  	body['ingredientes'].push({
  		'nome_ingrediente': el.nomeIngrediente(),
  		'quantidade': el.qtdeIngrediente(),
  		'unidade': el.unidadeIngrediente()
  	});
  });

	//console.log(JSON.stringify(body));

	var imagens = document.getElementById('imagens').files[0];
	var reader = new FileReader();
   reader.readAsDataURL(imagens);
   reader.onload = function () {
     //console.log(reader.result);
     //var base = reader.result.substring(reader.result.indexOf(",") + 1);
     body['imagens'] = [{'imagem':reader.result}];
     	
     //console.log(JSON.stringify(body));
     	var teste = {
      'json_data': JSON.stringify(body),
      "type": 'clone',
      "csrfmiddlewaretoken": Cookies.get('csrftoken')
    	}

			$.post('http://127.0.0.1:8000/home/cadastroReceitaJson/?format=json', teste, function(data, textStatus, xhr) {
				console.log(data)
				console.log("http://127.0.0.1:8000/home/xml/"+data['id']);
				window.location.replace("http://127.0.0.1:8000/home/"+data['id']);
			}).fail(function (data, textStatus, xhr) {
				console.log(data)
			});
  };
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
	ko.applyBindings(ingredientesViewModel, $('#main')[0]);
	sendForm();
});