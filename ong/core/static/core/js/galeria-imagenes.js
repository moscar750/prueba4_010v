function el_pulento_combo(url) {
  var $select = $('#combo_pulento');
  $.get(url, function(response) {
    $.each(response, function(index, element) {
      $select.append('<option value=' + element.id + '>' + element.name + '</option>');
    });
  });
}
function limpiar(selectorTablaHTML){
  $(selectorTablaHTML).html("");
}

function generar_galeria_imagenes(selectorTablaHTML, numeroTotalImagenes, numeroColumnasPorFila, url, textoBoton, urlData, id, tipo) {
  limpiar(selectorTablaHTML);

  var spinerPrincipalHTML = "";
  spinerPrincipalHTML += "<thead>";
  spinerPrincipalHTML += "    <tr>";
  spinerPrincipalHTML += "        <th colspan=\""+numeroColumnasPorFila+"\">";
  spinerPrincipalHTML += "            <div class=\"progress\" style=\"height:32px;\">"
  spinerPrincipalHTML += "                <div id=\"barra-progreso\" class=\"progress-bar\" style=\"width:0%; height:32px;\">0%</div>"
  spinerPrincipalHTML += "            </div>"
  spinerPrincipalHTML += "        </th>";
  spinerPrincipalHTML += "    </tr>";
  spinerPrincipalHTML += "</thead> ";


  $(selectorTablaHTML).append(spinerPrincipalHTML);
  $(selectorTablaHTML).append("<tbody></tbody>");

  var incrementoBarraProgreso = Math.floor(100/(numeroTotalImagenes));
  var avanceBarraProgreso = 0;

  $.get(url, function(response) {

    contadorImagenesCargadas = 0;
    indiceFilaActual = 0;
    filas = new Array();
    filas[indiceFilaActual] = $("<tr></tr>");
    $(selectorTablaHTML +" tbody").append(filas[indiceFilaActual]);

    $.each(response, function(index, element) {

      if (((index+1)%numeroColumnasPorFila) == 0) {
        indiceFilaActual++;
        filas[indiceFilaActual] = $("<tr></tr>");
        $(selectorTablaHTML +" tbody").append(filas[indiceFilaActual]);
      }

      var img = new Image();
      img.src = element.url;

      img.onload = function() {

        registroHTML = "<td class=\"text-center\">";
        registroHTML += "    <img id=\"imagen-"+element.id+"\" src=\""+element.url+"\" class=\"img-thumbnail\" style=\"width:200px;height:150px;\" /><br/>";
        if(tipo === true){
          registroHTML += "    <button class=\"btn btn-info\" onclick=\"javascript:btnData('"+id+"','"+selectorTablaHTML+"', '"+urlData+"', '"+element.url+"', "+tipo+");\"  >";
        }else{
          registroHTML += "    <button class=\"btn btn-info\" onclick=\"javascript:btnData('"+id+"','"+selectorTablaHTML+"', '"+urlData+"', '"+element.url+"', "+tipo+");\"  >";
        }
        registroHTML += "       <span id=\"ajax-loader-img-"+element.id+"\" class=\"spinner-border spinner-border-sm\"></span>";
        registroHTML += "       "+textoBoton;
        registroHTML += "    </button>";
        registroHTML += "</td>";

        var registro = $(registroHTML).hide();

        $(filas[Math.floor(index/numeroColumnasPorFila)]).append(registro);
        $("#ajax-loader-img-"+element.id).hide();

        if (contadorImagenesCargadas == (numeroTotalImagenes -1)) {
          $(selectorTablaHTML + " td").fadeIn(2000);
          console.log("Galería de imagenes completada")
          actualizarBarraProgreso(100);
        } else {
          contadorImagenesCargadas++;
          avanceBarraProgreso += incrementoBarraProgreso;
          actualizarBarraProgreso(avanceBarraProgreso);
        }
      }
    });

  });
}



function btnData(id, selectorTablaHTML, url, urlimg, tipo) {
  limpiar(selectorTablaHTML);

  console.log("url:::::"+url+id);
  var urldata = url+id;
  $.get(urldata, function(response) {
    $.each(response, function(index, element) {

      registroHTML = '<tr><td class="text-center">';
      registroHTML += '    <img id="imagen-'+element.id+'" src="'+urlimg+'" class="img-thumbnail"  />'
      registroHTML += '</td></tr>';
      registroHTML += '<tr><td>';
      registroHTML += '<p>Peso promedio: '+element.breeds[0].weight.metric+'</p>';
      if(tipo === true){
        registroHTML += '<p>Estatura promedio: '+element.breeds[0].height.metric+'</p>';
      }
      registroHTML += '<p>Nombre: '+element.breeds[0].name+'</p>';
      registroHTML += '<p>Esperanza de vida: '+element.breeds[0].life_span+'</p>';
      registroHTML += '</td></tr>';

      var registro = $(registroHTML).hide();
      $(selectorTablaHTML).html(registro);
      $(selectorTablaHTML + " tr").fadeIn(2000);

    });
  });
}


function btnAction(identificadorImagen) {

  console.log("mostrar spiner para reflejar la ejecución de la llamada ajax de fondo");
  $("#ajax-loader-img-"+identificadorImagen).show();

  $.get(getBtnActionURL(), function(response){

    //iterar por el único elemento que debería devolver la respuesta
    $.each(response, function(index, element){
      //crear imagen para precargar antes de reemplazar por la existente
      var newImagen = new Image();
      newImagen.src = element.url;

      //cuando la imagen ya se encuentra descargada
      newImagen.onload = function() {

        $("#imagen-"+identificadorImagen).fadeOut(1000, function(){
          // se reemplaza la seleccionada, una vez que ya se ha desvanecido, por la nueva ya descargada
          $("#imagen-"+identificadorImagen).attr("src",element.url);

          // se oculta el spiner
          $("#ajax-loader-img-"+identificadorImagen).hide();

          // se vuelve a mostrar, pero con la nueva imagen
          $("#imagen-"+identificadorImagen).fadeIn(2000);
        });

      };
    });
  });
}

function actualizarBarraProgreso(porcentaje) {
  $("#barra-progreso").css("width", porcentaje+"%");
  $("#barra-progreso").html(porcentaje+"%");

  if (porcentaje == 100) {
    $("#barra-progreso").parent().fadeOut(2000);
  }
}
