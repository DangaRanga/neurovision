<template>
  <div>
    <model-header />
    <div class="grid grid-cols-3 min-h-screen">
      <div class="col-span-2 grid items-center">
        <model-build />
      </div>
      <model-sidebar 
        output="ReLu" 
        :layers="1"
      />
    </div>
  </div>
</template>

<script>
import CMHeader from "@/components/elements/CMHeader.vue";
import CMSidebar from "@/components/elements/CMSidebar.vue";
import CModel from "@/components/elements/CModel.vue";

export default {
  components: {
    "model-header": CMHeader,
    "model-sidebar": CMSidebar,
    "model-build": CModel,
  },
  data() {
    return {
      isRunning: false,
    };
  },
  methods: {
  },
  created() {
    this.isRunning = this.$route.params.isRunning == "true" ? true : false;
  },
};
</script>
