<template>
  <div class="about">
    <h1 class="display-1mt-12 underline">Reto Técnico (Django + Vue)</h1>
    <v-container class="body-1 mt-12 justify-content" style="max-width: 900px;">
      <h2 class="headline justify-content mb-7 font-weight-bold">Funcionamiento de la aplicación:</h2>
      <p>Aplicación de autentificación i gestión de usuarios y sus perfiles. Además, muestra sólo contenido a cada usuario dependiendo de su nivel de permisos</p>
      <p>Los usuarios tienen niveles, a mayor status, mayor la información a la que pueden acceder: Gold, Silver y Bronze.</p>
      <p>Los informes tienen un mínimo nivel requerido para poder ser leídos.</p>
      <p>Cuando un usuario se registra, no tiene ningún nivel, el cual, debe ser adjudicado por el administrador.</p>

      <h2 class="headline justify-content mb-7 mt-5 font-weight-bold">Django (Backend):</h2>
      <p>Django es el encargado de subministrar los Endpoints al frontend, administrar registro, autentificación y permisos de los usuarios de la aplicación.</p>
      <p>El proyecto se divide en dos "apps": users y reports.</p>
      <p>La app "users" contiene el modelo "Profile", es un modelo proxy que extiende la funcionalidad del modelo User que trae por defecto Django. Tienen una relacion one-to-one.</p>
      <p>Este modelo se ayuda de "signals" para asegurar que se crea un perfil cada vez que un usuario es creado y se guarda cuando el modelo User se guarda.</p>
      <p>La app "reports", contiene los informes y el permiso mínimo que tiene que tener un usuario para poder leer un informe.</p>
      <p>La vista tiene la funcion "access_level_queryset" que devuelve una consulta con todos los informes que el usuario puede leer. Dicha funcion es aprovechada por ListReportView y DetailReportView.</p>

      <h2 class="headline justify-content mb-7 mt-5 font-weight-bold">Vue & Vuex (Frontend):</h2>
      <p>Utilizamos Vuex como almacén de información y funcionalidad. Los componentes del frontend deberán consultar al "store" necesiten información.</p>
      <p>El router es el encargado de mostrar las vistas que el usuario desee. "About", "Main" y "Profile" son accesibles directamente desde la barra de menu superior. Se podrá visitar cada informe en particular gracias a sus rutas dinámicas.</p>
      <p>Para el formato de la aplicación se ha utilizado "Vuetify", el framework de componentes para Vue basado en "Material Design".</p>

    </v-container>
  </div>
</template>

<style scoped>
  .underline {
    text-decoration: underline;
  }

  body p {
    font-size: 22px;
    line-height: 2;
    text-align: justify;
  }

</style>
