var header = `
<nav class="nav" id="nav">
<a class="logo" href="#">
  <img src="img/Logo/logo ajustado.png" alt="Logo hospital">
</a>
<div class="mobile-menu-button">
  <svg class="h-8 w-8" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
    <title>Mobile menu</title>
    <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"></path>
  </svg>
</div>
<ul>
  <li><a href="index.html">Inicio</a></li>
  <li><a href="institucional.html">Institucional</a></li>
  <li><a href="index.html#noticias">Noticias</a></li>
  <li><a href="servicios.html">Servicios</a></li>
  <li><a href="contacto.html">Contacto</a></li>
  <li><a class="intranet" href="http://pacientes.pythonanywhere.com/accounts/login/?next=/pacientes/" target="_blank">Intranet</a>
  </li>

</ul>
</nav>
<div class="dropdown">
<div class="close-button">
  <svg class="h-8 w-8" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
  </svg>
</div>
<hr>
<hr>
<ul>
  <li><a href="index.html">Inicio</a></li>
  <li><a href="institucional.html">Institucional</a></li>
  <li><a href="index.html#noticias">Noticias</a></li>
  <li><a href="servicios.html">Servicios</a></li>
  <li><a href="contacto.html">Contacto</a></li>
  <li><a href="http://pacientes.pythonanywhere.com/accounts/login/?next=/pacientes/" target="_blank">Intranet</a>
  </li>
</ul>
<hr>
<div class="button-container">

</div>
<p class="copyright-text">Copyright © 2023</p>
</div>
<div class="dropdown-backdrop"></div>
<div class="titulo">
<a class="titulo-pag">
  <h1>HOSPITAL D. ARTURO OÑATIVA</h1>
</a>
</div>
<div class="contenedor-imagenhospi">
<img class="imagenhospi" src="img/img_index/hospital4.jpg" alt="" />
</div>
`
document.querySelector('header').innerHTML = header