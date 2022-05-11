<template>
  <aside id="v-step-0">
    <div
      v-if="!isRunning"
      class="bg-primary_light py-8 px-10 w-full h-full flex flex-col justify-between"
    >
      <div class="mb-8">
        <div class="mb-10">
          <h3 class="text-2xl font-bold m-0">Activation Functions</h3>
          <p class="text-sm font-regular mt-4">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Dictum enim
            pellentesque auctor ipsum integer feugiat risus nulla sed
          </p>
        </div>
        <div>
          <sidebar-input type="select" :title="title" :options="options" />
        </div>
      </div>
      <div class="flex flex-col justify-center">
        <div class="flex justify-center m-0 mb-4">
          <button
            className="w-2/5 bg-grey_dark text-white font-bold py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-2"
            type="button"
          >
            Previous Step
          </button>
          <button
            className="w-1/3 bg-primary text-white font-semibold py-3 rounded shadow hover:shadow-md outline outline-1"
            type="button"
            @click="changeState"
          >
            Next Step
          </button>
        </div>
        <p class="px-4 mx-auto font-thin text-sm">Step 2 of 5</p>
      </div>
    </div>
    <div
      v-if="isRunning"
      class="bg-primary_light py-8 px-10 w-full h-full flex flex-col justify-between"
    >
      <div class="mb-8">
        <div class="mb-10">
          <tabbed-menu :selected="selected" :changeSelected="changeSelected" />
        </div>
        <div>
          <div v-if="selected == 1">
            <sidebar-input
              v-for="(header, i) in headers"
              :key="i"
              type="input"
              :title="header"
            />
          </div>
          <div v-if="selected == 2">
            <div
              v-for="(graph, i) in graphs"
              :key="i"
              class="w-2/3 h-56 bg-grey_dark mb-10 mx-auto"
            ></div>
          </div>
        </div>
      </div>
      <div class="flex flex-col justify-center">
        <div class="flex justify-center m-0 mb-4">
          <button
            className="w-3/5 bg-primary text-white font-bold py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-2"
            type="button"
            @click="changeState"
          >
            Restart Simulation
          </button>
        </div>
      </div>
    </div>
  </aside>
  <v-tour name="myTour" :steps="steps"></v-tour>
</template>

<script>
import SidebarInput from "@/components/elements/SidebarInput.vue";
import TabbedMenu from "@/components/elements/TabbedMenu.vue";

export default {
  props: ["isRunning", "changeState"],
  components: {
    "sidebar-input": SidebarInput,
    "tabbed-menu": TabbedMenu,
  },
  data() {
    return {
      steps: [
        {
          target: "#v-step-0",
          content: ` <strong>Let's customize the parameters for the Neural Network</strong>!`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `There are several different types of problems that can be modeled using neural networks.
          These include: <strong>Binary Classification, Multivariate Classification, Prediction and Regression.<\strong>`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Let us get some information on the Type of Analysis that the dataset is performing</strong>!`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Let us get some information on the Training Data Percentage needed for this dataset</strong>!`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Let us get some information on what Normalization is </strong>.`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Hooray!, now that you've customized the dataset let's continue </strong>.`,
          params: {
            placement: "left",
          },
        },
      ],
      selected: 1,
      graphs: [1, 2, 3],
      options: [
        { title: "ReLu", value: "relu" },
        { title: "Sigmoid", value: "sigm" },
        { title: "Softmax", value: "smax" },
      ],
      title: "Activation Function",
      headers: [
        "Batch Size",
        "Epochs",
        "Learning Rate",
        "Loss Function",
        "Optimization Algorithm",
      ],
    };
  },
  mounted: function () {
    this.$tours["myTour"].start();
  },
  methods: {
    changeSelected(option) {
      this.selected = option;
    },
  },
};
</script>
