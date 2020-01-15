<template>
  <v-app id="app">
    <Navbar class="mb-10" />
    <router-view />
  </v-app>
</template>

<script>
import Navbar from './components/layout/Navbar'

export default {
  name: "app",
  components: {
    Navbar
  },
  created() {
    this.removeUser()
    window.addEventListener('beforeunload', e => {
      e.preventDefault()
      this.removeUser()
    })
  },
  methods: {
    removeUser() {
      this.$store.dispatch('clearProfile')
      this.$store.dispatch('deleteToken')
        .then(res => {
          this.$router.push({name: 'login'})
        })
    },
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  line-height: 2;
}

body {
    margin: 0;
    padding: 0;
}

.container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.titlebar {
  background-color: blue;
  height: 35px;
  flex-shrink: 0;
}

.content {
  flex-grow: 1;
  overflow-x: auto;
}

</style>