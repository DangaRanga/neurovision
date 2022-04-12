<template>
  <div>
    <model-header :isRunning="isRunning" />
    <div class="grid grid-cols-3 min-h-screen">
      <div class="bg-primary col-span-2">{{ isRunning }}</div>
      <model-sidebar :isRunning="isRunning" :changeState="changeState" />
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
  data() {
    return {
      isRunning: false,
    };
  },
  methods: {
    changeState() {
      this.isRunning = !this.isRunning;
    },
  },
  mounted() {
    this.isRunning = Boolean(this.$route.params.isRunning);
    console.log(this.$route.params.isRunning);
  },
  created() {
    this.isRunning = this.$route.params.isRunning == "true" ? true : false;
  },
};
</script>
