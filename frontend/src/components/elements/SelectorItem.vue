<template>
  <article
    class="shadow-lg w-52 h-52 rounded-full flex items-center justify-center transition-colors duration-200"
    :class="selected ? 'border-2 border-cyan-600' : ''"
    id="selectable"
    @click="toggleSelected"
  >
    Selection item
  </article>
</template>
<script>
export default {
  name: "selection-item",
  props: ["img", "selected"],
  data() {
    return {
      selected: false,
    };
  },

  methods: {
    toggleSelected() {
      console.log(this.selected);
      this.selected = !this.selected;
    },
  },
};
</script>
