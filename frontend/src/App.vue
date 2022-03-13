<template>
  <nav>
    <navbar />
    <dataset-selection />
  </nav>
</template>
<script>
import Nav from "@/components/elements/Nav.vue";
import DatasetSelection from "@/views/DatasetSelection.vue";

export default {
  components: {
    navbar: Nav,
    "dataset-selection": DatasetSelection,
  },
};
</script>

<style>
@import "./assets/styles/variables.css";
#selectable {
  cursor: pointer;
}
</style>
