var footer = `
<div class="pie_pag-col1">
      <!-- Redes sociales -->
      <div class="redes_sub">
          <h4>Redes sociales</h4>
        </div>
      <div class="redes_container">
        
        <div class="redes_item">
          <a href="https://www.instagram.com/hospitalonativia/" target="_blank"><i
              class="fa-brands fa-instagram fa-bounce fa-2xl" style="color: #ffffff;"></i></a>
        </div>
        <div class="redes_item">
        <a href="https://www.facebook.com/hospi.onativia/" target="_blank"><i
            class="fa-brands fa-square-facebook fa-bounce fa-2xl" style="color: #f8f5f5;"></i></a>
      </div>
        
      </div>
      <!-- Cierra Redes sociales -->
      <div class="contacto">
        <div>
          <h4>Contáctanos:</h4>
        </div>
        <div>
          <p>Telf: 1126 5894 5677</p>
        </div>
        <div>
          <p>Email: contacto@email.com</p>
        </div>
      </div>
      </div>
      <!-- Columna 2-->
      <div class="pie_pag-col2"> 
      <div class="navegacion">
        <h4>Navegación</h4>
        <ul>
          <a href="index.html"><li>Inicio</a></li>
          <a href="institucional.html"><li>Institucional</a></li>
          <a href="index.html#noticias"><li>Noticias</a></li>
          <a href="contacto.html"><li>Contacto</a></li>
          <li><a href="servicios.html">Servicios</a></li>
          <a href="http://pacientes.pythonanywhere.com/accounts/login/?next=/pacientes"><li>Intranet</a></li>
        </ul>
      </div>        
      </div>
      <!-- Columna 3-->
      <div class="pie_pag-col3">        
      <div>
        <h4>Podría interesarte:</h4>
      </div>
      <div>
        <ul>
          <li>
            <a href="servicios.html">
              <h5>¿Cómo sacar turno?</h5>
            </a>
          </li>
          <li>
            <a href="">
              <h5>Historia del hospital</h5>
            </a>
          </li>
          <li><a href="https://www.instagram.com/p/Cn7Eg5pOVLe/" target="_blank">
              <h5>Donar sangre</h5>
            </a>
          </li>
          <li>
            <a href="./contacto.html#ubicacion">
              <h5>Ubicación del hospital</h5>
            </a>
          </li>
        </ul>
      </div>
      </div>
      <!-- Columna 4 -->
      <div class="pie_pag-col4">
      <div>
        <a class="irarriba" href="#nav">
          <h4>Ir arriba</h4>
        </a>
      </div>
      <div class="registrarse">
        <div>
          <h4>Suscribite:</h4>
        </div>
        <div><input class="suscripcion" id="suscripcion" type="text" placeholder="Escribe tu email" /></div>
        <div><button type="submit" value="Registrarse">
        <span>Enviar</span>
        </button></div>
      </div>
      </div>
      </div>
`
document.querySelector('footer').innerHTML= footer