<template>
  <div id="app">
    <h1 class="mt-5 mb-3">Perfil</h1>
    <img :src="avatar_url" alt="Profile Picture">
    <!-- <input type="file" @change="onFileSelected"> -->
    <!-- <v-container fluid class="mx-auto" style="max-width: 300px; cursor: pointer"> -->
      <br>
      <input type="file" ref="upload" style="display: none" @change="uploadImage">
      <button 
        class="v-btn v-btn--flat v-btn--outlined theme--light elevation-1 v-size--default blue--text text--accent-4 mb-5" 
        @click="$refs.upload.click()"
        >reemplazar imagen
      </button>
    
    <p>Nombre de Usuario: {{profile.username}}</p>
    <p>Groups: {{groups}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Profile',
  computed: {
    profile() {
      return this.$store.state.profile
    },
    groups() {
      let groups = this.$store.state.profile.groups
      if(!groups) {
        groups = ''
      } else if(groups.length > 1) {
        groups = groups.join(", ")
      } else if(groups.length == 1) {
        groups = groups[0]
      } else {
        groups = 'Todavía no está en ningún grupo'
      }
      return groups
    },
    avatar_url() {
      const avatar_url = `http://localhost:8000${this.$store.state.profile.avatar}`
      return avatar_url
    }
  },
  created() {
    this.$store.dispatch('getProfile')
  },
  methods: {
    uploadImage(event) {
      this.selectedFile = event.target.files[0]
      window.console.log(this.selectedFile)
      const fd = new FormData()
      fd.append('avatar',this.selectedFile, this.selectedFile.name)
      const headers = {headers: {'Authorization': `JWT ${this.$store.state.token}`}}
      axios.put('http://localhost:8000/api/v1/user/update-avatar/', fd, headers)
        .then(res => {
          window.console.log(res)
          this.$store.dispatch('getProfile')
        })
        .catch(err => {
          this.$store.dispatch('clearProfile')
          this.$store.dispatch('deleteToken')
            .then(res => {
              this.$router.push({name: 'login'})
        })
        })
    }
  }
}
</script>

<style scoped>
  img {
    border-radius: 50%;
    width: 200px;
    margin-bottom: 15px;
  }

  .input-300 {
    max-width: 300px;
    padding-right: 32px;
  }
</style>
