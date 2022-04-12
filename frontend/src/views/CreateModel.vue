<template>
  <div>
    <model-header :isRunning=true />
    <div class="grid grid-cols-3 min-h-screen">
      <div class="bg-primary col-span-2"></div>
      <model-sidebar :isRunning=true />
    </div>
    <!-- <model-build /> -->
  </div>
</template>

<script>
import ModelHeader from "@/components/elements/ModelHeader.vue";
import ModelSidebar from "@/components/elements/ModelSidebar.vue";
import ModelBuild from "@/components/elements/ModelBuild.vue";

export default {
  components: {
    "model-header": ModelHeader,
    "model-sidebar": ModelSidebar,
    "model-build": ModelBuild,
  },
};
</script>
