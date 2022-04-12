<template>
  <div
    className="w-1/3 bg-grey_dark text-white text-xs font-bold px-4 py-3 rounded shadow hover:shadow-md outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3"
  >
    Update
  </div>
</template>

<script>
export default {
  name: "ShepherdExample",
  mounted() {
    this.$nextTick(() => {
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
