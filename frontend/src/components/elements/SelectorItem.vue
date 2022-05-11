<template>
  <div class="flex flex-col items-center">
    <article
      class="shadow-lg w-52 h-52 rounded-full flex items-center justify-center transition-colors duration-200"
      :class="selected ? 'border-2 border-primary parent' : ''"
      id="selectable"
      @click="toggleSelected"
    >
      <div v-if="image">
        <img :src="image" :alt="title" />
      </div>
    </article>

    <div class="text-center w-1/2 my-3">
      <h1 class="text-lg font-bold text-primary_dark">
        {{ title }}
      </h1>
      <p class="text-gray-600">
        {{ summary }}
      </p>
    </div>
    <transition name="fade">
      <div v-if="selected">
        <svg
          class="checkmark"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 52 52"
        >
          <circle
            class="checkmark__circle"
            cx="26"
            cy="26"
            r="25"
            fill="none"
          />
          <path
            class="checkmark__check"
            fill="none"
            d="M14.1 27.2l7.1 7.2 16.7-16.8"
          />
        </svg>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "selection-item",
  props: {
    image: String,
    itemNo: Number,
    title: String,
    summary: String,
    datasetIndex: Number,
    selected: false,
  },

  data() {},

  methods: {
    toggleSelected() {
      console.log(this.selected);

      this.$emit("select", this.datasetIndex);
    },
  },
};
</script>
<style scoped>
.checkmark__circle {
  stroke-dasharray: 166;
  stroke-dashoffset: 166;
  stroke-width: 2;
  stroke-miterlimit: 10;
  stroke: var(--primary);
  fill: none;
  animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
}

.checkmark {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  position: relative;
  top: -18.3em;
  left: 6em;
  stroke-width: 2;
  stroke: #fff;
  stroke-miterlimit: 10;
  box-shadow: inset 0px 0px 0px var(--primary);
  animation: fill 0.4s ease-in-out 0.4s forwards,
    scale 0.3s ease-in-out 0.9s both;
}

.checkmark__check {
  transform-origin: 50% 50%;
  stroke-dasharray: 48;
  stroke-dashoffset: 48;
  animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards;
}
</style>
