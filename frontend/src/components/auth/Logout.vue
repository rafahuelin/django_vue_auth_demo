<template>
  <div v-if="hideEmptyDiv"></div>
</template>

<script>
export default {
  name: 'Logout',
  created() {
    this.$store.dispatch('clearProfile')
    this.$store.dispatch('deleteToken')
      .then(res => {
          this.$router.push({name: 'login'})
        })
  },
  computed: {
    hideEmptyDiv() {
      return false
    }
  }
}
</script>