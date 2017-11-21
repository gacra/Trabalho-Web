function postREST() {
  var csrfmiddlewaretoken = $("[name='csrfmiddlewaretoken']").val();
  var nome = $("#nome").val();
  var nascimento = $('#nascimento').val();
  var cidade = $('#cidade').val();
  var estado = $('#estado').val();
  var telefone = $('#telefone').val();
  var usuario = $('#nome_usuario').val();
  var password = $('#senha').val();
  var body = {
    'csrfmiddlewaretoken': csrfmiddlewaretoken,
    'nome': nome,
    'nascimento': nascimento,
    'cidade': cidade,
    'estado': estado,
    'telefone': telefone,
    'usuario': usuario,
    'password':password,
  };    
  $.post('http://127.0.0.1:8000/home/cadastroUsuarioJson/?format=json', body, function(data, textStatus, xhr) {
      console.log(data)
    }).fail(function (data, textStatus, xhr) {
    console.log(data)
  });
}

function sendForm(){
  var form = document.getElementById("cadastrarUsuario");
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