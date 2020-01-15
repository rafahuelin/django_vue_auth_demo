<template>
    <v-card
      color="#f5f5f5"
      width="450"
      dark
      class="mb-5 mx-auto mt-5"
      elevation="1"
      shaped
    >
      <v-card-title class="headline">{{report.title}}</v-card-title>

      <v-card-subtitle class="text-left">{{report.content}}</v-card-subtitle>

      <v-card-actions>
        <v-btn text :to="{name: 'report', params: {id: report.id}}">detalles</v-btn>
      </v-card-actions>
    </v-card>

</template>

<script>
export default {
  name: "ReportItem",
  props: ["report"]
}
</script>

<style scoped>
* {
  color: #555 !important;
}


</style>