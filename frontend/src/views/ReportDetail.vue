<template>
  <div id="app">
    <h1 class="mt-5 mb-3">Detalle Informe</h1>
    <p>Id: {{$route.params.id}}</p>
    <p>Título: {{report.title}}</p>
    <p>Contenido: {{report.content}}</p>
    <p>Mínimo Status Requerido: {{report.minimum_access_level}}</p>
    <v-btn text :to="{name: 'main'}">Volver</v-btn>
  </div>
</template>

<script>

export default {
  name: 'ReportDetail',
  data() {
    return {
      reports: this.$store.state.reports
    }
  },
  computed: {
    report() {
      const report = this.reports.filter(obj => obj.id == this.$route.params.id)[0]
      return report
    }
  }
}
</script>
