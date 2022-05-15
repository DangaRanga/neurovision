<template>
  <div>
    <div
      class="flex flex-row-reverse bg-grey_dark h-18 py-4 px-2 drop-shadow-lg"
    >
      <button
        class="text-white bg-primary hover:bg-blue-500 rounded-md py-2 px-4 mx-3 transition-colors duration-200"
      >
        Preview Dataset
      </button>
    </div>
  </div>
</template>

<script>
import HeaderDisplayItem from "@/components/elements/HeaderDisplayItem.vue";

export default {
  components: {
    "header-display-item": HeaderDisplayItem,
  },
  data() {
    return {
    };
  },
};
</script>
