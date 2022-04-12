<template>
  <nav>
    <navbar />
    <router-view />
    <!-- <dataset-selection /> -->
    <!-- <create-model /> -->
    <!-- <customize-dataset /> -->
  </nav>
</template>
<script>
import NavBar from "@/components/elements/NavBar.vue";
import MyInfographic from "@/components/elements/Infographic.vue";
import DatasetSelection from "@/views/DatasetSelection.vue";
import CustomizeDataset from "@/views/CustomizeDataset.vue";
import CreateModel from "@/views/CreateModel.vue";

export default {
  components: {
    navbar: NavBar,
    MyInfographic: MyInfographic,
    "dataset-selection": DatasetSelection,
    // eslint-disable-next-line vue/no-unused-components
    "customize-dataset": CustomizeDataset,
    // eslint-disable-next-line vue/no-unused-components
    "create-model": CreateModel,
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
