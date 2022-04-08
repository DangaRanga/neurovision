<template>
  <div>
    <model-header :isRunning=false />
    <div class="grid grid-cols-3 min-h-screen">
      <div class="bg-primary col-span-2"></div>
      <model-sidebar />
    </div>
  </div>
</template>

<script>
import ModelHeader from "@/components/elements/ModelHeader.vue";
import ModelSidebar from "@/components/elements/ModelSidebar.vue";

export default {
  components: {
    "model-header": ModelHeader,
    "model-sidebar": ModelSidebar
  },
};
</script>