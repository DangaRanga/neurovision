<template>
  <aside>
    <div
      class="bg-primary_light py-8 px-10 w-full h-full flex flex-col justify-between"
      id="v-step-0"
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
              :type="header.type"
              :title="header.title"
              :value="header.value"
              :options="header.options"
              :change="header.change"
              :id="'v-step-' + (i + 1)"
              :index="i"
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
            @click="update"
            className="w-3/5 bg-primary text-white font-bold py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-2"
            type="button"
            id="v-step-6"
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
import { modelTour } from "@/controllers/tour/animationCustomization.js";

export default {
  props: ["batch", "epoch", "lrate", "loss"],
  components: {
    "sidebar-input": SidebarInput,
    "tabbed-menu": TabbedMenu,
  },
  data() {
    return {
      batch_size: 1,
      epochs: 100,
      l_rate: 0.01,
      loss_f: "MSE",
      steps: modelTour,
      selected: 1,
      graphs: [1, 2, 3],
      isTourVisible: localStorage.getItem("isTourVisible") === "true",
      headers: [
        {
          title: "Batch Size",
          type: "input-n",
          value: "",
          options: [],
          change: this.changeParam,
        },
        {
          title: "Epochs",
          type: "input-n",
          value: "",
          options: [],
          change: this.changeParam,
        },
        {
          title: "Learning Rate",
          type: "input-n",
          value: "",
          options: [],
          change: this.changeParam,
        },
        {
          title: "Loss Function",
          type: "select",
          value: "",
          options: [
            { title: "Mean Squared Error", value: "mse" },
            { title: "Binary Cross-Entropy", value: "bce" },
          ],
          change: this.changeLoss,
        },
        {
          title: "Optimization Algorithm",
          type: "input-d",
          value: "Stochastic Gradient Descent",
          options: [],
          change: "",
        },
      ],
    };
  },
  created(){
    this.batch_size = this.batch || 1;
    this.epochs = this.epoch || 100;
    this.l_rate = this.lrate || 0.01;
    this.loss_f = this.loss || "MSE";
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
    changeParam(data) {
      switch (data.index) {
        case 0:
          this.batch_size = data.value;
          break;
        case 1:
          this.epochs = data.value;
          break;
        case 2:
          this.l_rate = data.value;
          break;
      }
    },
    changeLoss(data) {
      switch (data.value) {
        case "mse":
          this.loss_f = "MSE";
          break;
        case "bce":
          this.loss_f = "Binary Cross Entropy";
          break;
        default:
          this.loss_f = "MSE";
          break;
      }
    },
    update() {
      // validation before sending data

      this.$emit("restart", [
        { title: "Batch Size", value: this.batch_size },
        { title: "Epoch No.", value: this.epochs },
        { title: "Learning Rate", value: this.l_rate },
        { title: "Loss Function", value: this.loss_f },
      ]);
    },
  },
};
</script>
<style scoped>
.v-tour__target--highlighted {
  box-shadow: 0 0 0 9999px rgba(0, 0, 0, 0.5);
}
</style>
