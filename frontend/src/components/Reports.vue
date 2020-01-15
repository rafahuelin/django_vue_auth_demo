<template>
  <div>
    <br>
    <div :key="report.id" v-for="report in reports">
      <ReportItem :report="report" />
    </div>
  </div>
</template>

<script>
import ReportItem from './ReportItem'
export default {
  name: "Reports",
  data() {
    return {
      reports: this.$store.state.reports
    }
  },
  components: {
    ReportItem
  },
  created() {
    this.$store.dispatch('getReports')
  }
}
</script>

<style scoped>

</style>