<template>
<div>
  <v-app-bar color="blue">
    <v-toolbar-title fixed class="white--text">Reto Técnico</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-toolbar-items>
      <v-btn text :to="{name: 'main'}" class="white--text" exact>Informes</v-btn>
      <v-btn text :to="{name: 'about'}" class="white--text" exact>Ayuda</v-btn>
      <v-btn text v-if="!loggedIn" :to="{name: 'login'}" class="white--text" exact>Iniciar sesión</v-btn>
      <v-btn text v-if="!loggedIn" :to="{name: 'register'}" class="white--text" exact>Registrarse</v-btn>
      <v-btn icon v-if="loggedIn" :to="{name: 'profile'}">
        <v-icon class="white--text">mdi-account-circle</v-icon>
      </v-btn>
      <v-btn text v-if="loggedIn" :to="{name: 'logout'}" class="white--text" exact>Finalizar sesión</v-btn>
    </v-toolbar-items>
  </v-app-bar>
</div>
</template>

<script>
export default {
  name: "Navbar",
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn
    }
  },
  watch: {
    $route(to, from) {
      window.console.log('Clicked Navigation')
      this.$store.dispatch('checkToken')
    }
  }
}
</script>