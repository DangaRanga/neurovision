<template>
  <aside id="v-step-0">
    <div
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
          >
            Restart Simulation
          </button>
        </div>
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
    this.$tours["myTour"].start();
  },
  methods: {
    changeSelected(option) {
      this.selected = option;
    },
  },
};
</script>
