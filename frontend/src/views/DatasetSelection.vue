<template>
  <div class="flex">
    <selector-item></selector-item>
    <selector-item></selector-item>
    <selector-item></selector-item>
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
