<template>
  <div class="flex justify-around">
    <selector-item :src="''" :alt="'Cat Images'"></selector-item>
    <selector-item :src="''" :alt="'Cat Images'"></selector-item>
    <selector-item :src="''" :alt="'Cat Images'"></selector-item>
  </div>
</template>
<script>
import SelectorItem from "@/components/elements/SelectorItem.vue";
export default {
  components: {
    "selector-item": SelectorItem,
  },
};
</script>
