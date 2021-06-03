/*
No es tan complicado, solo deben importar el JS con el idioma español y despues le indican al datepicker que usaran ese idioma.
*/
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="/resources/demos/style.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

$('#datepicker').datepicker({
    uiLibrary: 'bootstrap4',
    locale: 'es-es',
  });