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
@import "./assets/styles/animations.css";
#selectable {
  cursor: pointer;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
