$(document).ready(function() {
  var url = "https://api.thedogapi.com/v1/breeds";
    el_pulento_combo(url);
});

function buscar(){
  var e = document.getElementById("combo_pulento");
  var valor = e.value;

  var nroTotalImagenes = 10;
  var nroColumnasPorFila = 5;
  var selectorTablaHTML = "#lista-perros";
  var texto = "Ver detalle";
  var url =     "https://api.thedogapi.com/v1/images/search?limit="+nroTotalImagenes;
  var url2 =    "https://api.thedogapi.com/v1/images/search?limit="+nroTotalImagenes+"&include_breed=1&breed_id=" + valor;
  var urlData = "https://api.thedogapi.com/v1/images/search?include_breed=1&breed_id=";
  var urlDataSin = "https://api.thedogapi.com/v1/images/search?include_breed=1";

  if(valor == 'all'){
    generar_galeria_imagenes(selectorTablaHTML, nroTotalImagenes, nroColumnasPorFila, url, texto, urlDataSin, 0, true);
  }else if(valor == 'empty'){
    limpiar(selectorTablaHTML);
  }else{
    generar_galeria_imagenes(selectorTablaHTML, nroTotalImagenes, nroColumnasPorFila, url2, texto, urlData, valor, true);
  }
}

function getBtnActionURL() {
    return "https://api.thedogapi.com/v1/images/search?limit=1";
}
