<template>
  <v-app>
    <v-card width="450" class="mx-auto mt-5">
      <v-card-title>
        <h2 class="display-1">Inicio de Sesión</h2>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="login" id="login-form">
          <v-text-field 
            v-model="username"
            label="Usuario" 
            name="username" 
            id="username" 
            prepend-icon="mdi-account-circle" />
          <v-text-field 
            v-model="password"
            :type="showPassword ? 'text' : 'password'" 
            label="Contraseña" 
            name="password" 
            id="password" 
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword" />
            <v-btn type="submit" class="mx-auto mt-5 mb-3" color="success" form="login-form">Iniciar Sesión</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      showPassword: false
    }
  },
  methods: {
    login() {
      this.$store.dispatch('obtainToken', {
        username: this.username,
        password: this.password,
      })
        .then(res => {
          this.$store.dispatch('getReports')
            .then(res => {
              this.$router.push({name: 'main'})
            })
        })
    }
  }
}
</script>