<template>
  <aside>
    <div
      class="bg-primary_light py-8 px-10 w-full h-full flex flex-col justify-between"
    >
      <div class="mb-8">
        <div class="mb-10" id="v-step-0">
          <tabbed-menu :selected="selected" :changeSelected="changeSelected" />
        </div>
        <div>
          <div v-if="selected == 1">
            <sidebar-input
              v-for="(header, i) in headers"
              :key="i"
              :type="header.type"
              :title="header.title"
              :value="header.value"
              :options="header.options"
              :id="'v-step-' + (i + 1)"
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
      <div class="flex flex-col justify-center" id="v-step-6">
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
          target: "#v-step-1",
          content: `<strong>Click to view information on Batch Size parameters<\strong>`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-2",
          content: `<strong>Click to view information on Epochs parameter</strong>!`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-3",
          content: `<strong>Click to view information on the Learning Rate of a Neural Network </strong>!`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-4",
          content: `<strong>Find out what is meant by the Loss Function of a Neural Network </strong>.`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-5",
          content: `<strong>Let's look at what is the purpose of an Optimization Algorithm </strong>.`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-6",
          content: `<strong>Hooray!, now that you've learnt how to customize the parameters, here comes the fun part ! 
          <br /> <br /> Let's start the simulation and observe the changes in the Neural Network</strong> !`,
          params: {
            placement: "left",
          },
        },
      ],
      selected: 1,
      graphs: [1, 2, 3],
      isTourVisible: localStorage.getItem("isTourVisible") === "true",
      options: [
        { title: "ReLu", value: "relu" },
        { title: "Sigmoid", value: "sigm" },
        { title: "Softmax", value: "smax" },
      ],
      title: "Activation Function",
      headers: [
        { title: "Batch Size", type: "input", value: "", options: [] },
        { title: "Epochs", type: "input", value: "", options: [] },
        { title: "Learning Rate", type: "input", value: "", options: [] },
        {
          title: "Loss Function",
          type: "select",
          value: "",
          options: [
            { title: "Mean Squared Error", value: "mse" },
            { title: "Binary Cross-Entropy", value: "bce" },
          ],
        },
        {
          title: "Optimization Algorithm",
          type: "input-d",
          value: "Stocrastic Gradient Descent",
          options: [],
        },
      ],
    };
  },
  mounted: function () {
    if (this.isTourVisible) {
      this.showTour();
    }
  },
  methods: {
    showTour() {
      this.$tours["myTour"].start();
    },
    changeSelected(option) {
      this.selected = option;
    },
  },
};
</script>
