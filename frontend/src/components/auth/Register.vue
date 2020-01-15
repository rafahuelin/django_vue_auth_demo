<template>

  <v-app>
    <v-card width="450" class="mx-auto mt-5">
      <v-card-title>
        <h2 class="display-1">Registro</h2>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="registration">
          <v-text-field 
            v-model="username"
            label="Usuario" 
            name="username" 
            id="username" 
            prepend-icon="mdi-account-circle" />
          <v-text-field 
            v-model="email"
            label="Correo electrónico" 
            name="email" 
            id="email" 
            prepend-icon="mdi-email-outline" />
          <v-text-field 
            v-model="password"
            :type="showPassword ? 'text' : 'password'" 
            label="Contraseña" 
            name="username" 
            id="password" 
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword" />
            <v-btn type="submit" class="mx-auto mt-5 mb-3" color="success">Registrar</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-app>
</template> 

<script>
export default {
  name: 'Register',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      showPassword: false
    }
  },
  methods: {
    registration() {
      this.$store.dispatch('registration', {
        username: this.username,
        email: this.email,
        password: this.password,
      })
        .then(res => {
          this.$router.push({name: 'login'})
        })
    }
  }
}
</script>