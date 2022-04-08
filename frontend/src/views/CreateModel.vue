<template>
  <div>
    <model-header />
    <div class="grid grid-cols-3">
      <div class="bg-primary col-span-2"></div>
      <dataset-sidebar />
    </div>
  </div>
</template>

<script>
import ModelHeader from "@/components/elements/ModelHeader.vue";
import DatasetSideBar from "@/components/elements/DatasetSideBar.vue";

export default {
  components: {
    "model-header": ModelHeader,
    "dataset-sidebar": DatasetSideBar
  },
};
</script>