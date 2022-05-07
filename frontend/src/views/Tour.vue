<template>
  <div>Testing</div>
</template>

<style>
@import "../0///55850../node_modules/shepherd.js/dist/css/shepherd.css";
</style>
;

<script>
export default {
  name: "ShepherdExample",
  mounted() {
    this.$nextTick(() => {
      console.log("Hello");
      const tour = this.$shepherd({
        useModalOverlay: true,
      });

      tour.addStep({
        attachTo: { element: this.$el, on: "top" },
        text: "Test",
      });

      tour.start();
    });
  },
};
</script>
