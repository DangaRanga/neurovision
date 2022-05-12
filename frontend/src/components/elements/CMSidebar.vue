<template>
  <aside id="v-step-0">
    <div
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
          <sidebar-input type="input-d" title="Output Layer Activation Function" value="ReLu" />
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
          >
            Next Step
          </button>
        </div>
        <p class="px-4 mx-auto font-thin text-sm">Step 4 of 5</p>
      </div>
    </div>
    <v-tour name="myTour" :steps="steps"></v-tour>
  </aside>
</template>

<script>
import SidebarInput from "@/components/elements/SidebarInput.vue";
import TabbedMenu from "@/components/elements/TabbedMenu.vue";

export default {
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
          content: `<strong>Click to view information on Batch Size parameters<\strong>`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Click to view information on Epochs parameter</strong>!`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Click to view information on the Learning Rate of a Neural Network </strong>!`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Find out what is meant by the Loss Function of a Neural Network </strong>.`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Let's look at what is the purpose of an Optimization Algorithm </strong>.`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-0",
          content: `<strong>Hooray!, now that you've learnt how to customize the parameters, here comes the fun part ! 
          <br /> <br /> Let's start the simulation and observe the changes in the Neural Network</strong> !`,
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
    // this.$tours["myTour"].start();
  },
  methods: {
    changeSelected(option) {
      this.selected = option;
    },
  },
};
</script>
