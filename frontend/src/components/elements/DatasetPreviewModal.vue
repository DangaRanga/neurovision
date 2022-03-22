<template>
  <!-- Main modal -->

  <data-table></data-table>
</template>
<script>
import DataTable from "@/components/elements/DataTable.vue";

export default {
  components: {
    "data-table": DataTable,
  },

  props: {
    isVisible: Boolean,
  },
};
</script>
