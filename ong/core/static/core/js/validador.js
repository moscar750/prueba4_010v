
$(document).ready(function(){

    $("#formulario-login span.alert").hide();


});

function validar(){
	usuario=$('#usuario').val();
  pass=$('#pass').val();

  console.log(countDigits(pass));
  console.log(countLetra(pass));

  if (usuario.length<=8 || /\s/.test(usuario)) {
      $("#usuario").addClass("error-campo-formulario");
      $("label[for='usuario'] span.alert").html("El campo no puede tener menos de 8 caracteres o espacios en blanco");
      $("label[for='usuario'] span.alert").show();
      $("label[for='usuario'] span.alert").fadeOut( 5000 )

      if (countDigits( pass ) < 2) {
          $("#pass").addClass("error-campo-formulario");
          $("label[for='pass'] span.alert").html("La clave debe tener al menos 2 números y 2 letras.");
          $("label[for='pass'] span.alert").show();
          $("label[for='pass'] span.alert").fadeOut( 5000 );
      }
      return false;
  } else {
      $("#usuario").removeClass("error-campo-formulario");
      $("label[for='usuario'] span.alert").hide();

      if (countDigits( pass ) < 2 || countLetra(pass) < 2) {
          $("#pass").addClass("error-campo-formulario");
          $("label[for='pass'] span.alert").html("La clave debe tener al menos 2 números y 2 letras.");
          $("label[for='pass'] span.alert").show();
          $("label[for='pass'] span.alert").fadeOut( 5000 )

          return false;
      } else {
          $("#pass").removeClass("error-campo-formulario");
          $("label[for='pass'] span.alert").hide();

          return true;
      }
  }


  function countDigits( str ) {
    var acu = 0;
    Array.prototype.forEach.call( str, function( val ) {
      acu += ( val.charCodeAt( 0 ) > 47 ) && ( val.charCodeAt( 0 ) < 58 ) ? 1 : 0;
    });
    return acu;
  }

  function countLetra( str ) {
    var acu = 0;
    Array.prototype.forEach.call( str, function( val ) {
      acu += ( val.charCodeAt( 0 ) > 64 ) && ( val.charCodeAt( 0 ) < 91 ) ? 1 : 0;
      acu += ( val.charCodeAt( 0 ) > 96 ) && ( val.charCodeAt( 0 ) < 123 ) ? 1 : 0;
    });
    return acu;
  }
}
