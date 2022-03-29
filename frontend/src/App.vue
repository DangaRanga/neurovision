<template>
  <nav>
    <navbar />
    <dataset-selection />
    <!-- <page2 /> -->
  </nav>
</template>
<script>
import Nav from "@/components/elements/Nav.vue";
import DatasetSelection from "@/views/DatasetSelection.vue";
import Page2 from "@/views/Page2.vue";

export default {
  components: {
    navbar: Nav,
    "dataset-selection": DatasetSelection,
    page2: Page2,
  },
};
</script>

<style>
@import "./assets/styles/variables.css";
@import "./assets/styles/animations.css";
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;400;500;600;700&display=swap");
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
