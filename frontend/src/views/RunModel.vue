<template>
  <div>
    <model-header />
    <div class="grid grid-cols-3 min-h-screen">
      <div class="bg-white col-span-2"><model-build /></div>
      <model-sidebar />
    </div>
  </div>
</template>

<script>
import RMHeader from "@/components/elements/RMHeader.vue";
import RMSidebar from "@/components/elements/RMSidebar.vue";
import RModel from "@/components/elements/RModel.vue";

export default {
  components: {
    "model-header": RMHeader,
    "model-sidebar": RMSidebar,
    "model-build": RModel,
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
  created() {
    this.isRunning = this.$route.params.isRunning == "true" ? true : false;
  },
};
</script>
