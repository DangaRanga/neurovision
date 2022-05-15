<template>
  <aside id="v-step-0">
    <div class="bg-primary_light grid grid-cols-1 py-10 w-full">
      <div class="w-full pl-8 pr-12">
        <h3 class="text-lg font-bold py-2">Dataset - {{ datasettitle }}</h3>
        <p class="text-s font-regular py-2">
          {{ description }}
        </p>
      </div>
      <div class="w-full">
        <form class="pl-10 py-6 flex flex-col justify-center">
          <div class="py-4">
            <sidebar-input
              type="input-d"
              title="Type of Analysis"
              :value="analysisType"
              :id="'v-step-' + 1"
              :functionName="showAnalysisType"
            />
          </div>
          <sidebar-input
            type="select"
            title="Training Data Percentage"
            :options="splitoptions"
            :change="changeActFcn"
            :index="2"
            :id="'v-step-' + 2"
            :functionName="showTrain"
          />
          <sidebar-input
            type="select"
            title="Perform Normalization"
            :options="normalizeoptions"
            :change="changeActFcn"
            :index="2"
            :id="'v-step-' + 3"
            :functionName="showNormalization"
          />
          <div
            class="px-4 pt-12 mt-6 mb-4 flex justify-center m-0 mb-4 sm:flex-row sm:text-left sm:items-baseline"
          >
            <router-link
              className="w-1/3 bg-grey_dark text-white text-xs font-bold px-4 py-3 rounded shadow hover:shadow-md outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3"
              :to="{
                name: 'create',
                params: { isRunning: true },
              }"
            >
              Pervious Step
            </router-link>
            <router-link
              id="v-step-4"
              class="w-1/3 bg-primary text-center text-white text-xs font-semibold px-4 py-3 rounded shadow hover:shadow-md outline outline-1 lg:mr-1 lg:mb-0 ml-3 mb-3"
              :to="{
                name: 'create',
                params: { isRunning: false },
              }"
            >
              Next Step
            </router-link>
            <!-- <button
              className="w-1/3 bg-primary text-white text-xs font-semibold px-4 py-3 rounded shadow hover:shadow-md outline outline-1 lg:mr-1 lg:mb-0 ml-3 mb-3"
              type="button"
            >
              Next Step
            </button> -->
          </div>
          <p class="px-4 mx-auto font-thin text-sm">Step 2 of 5</p>
        </form>
      </div>
    </div>

    <Modal
      :topic="title"
      :message="message"
      v-show="isModalVisible"
      @close="closeModal"
    />
    <v-tour name="myTour" :steps="steps"></v-tour>
  </aside>
</template>
<script>
// import DataTable from "@/components/elements/DataTable.vue";
import infographics_icon from "@/assets/icons/infographics_icon.svg";
import InfograpicModal from "@/components/elements/Infographic.vue";
import SidebarInput from "@/components/elements/SidebarInput.vue";
import { customizationTour } from "@/controllers/tour/dataCustomization.js";

export default {
  components: {
    Modal: InfograpicModal,
    "sidebar-input": SidebarInput,
  },
  props: {
    analysisType: String,
    datasettitle: String,
    description: String,
  },
  data() {
    return {
      splitoptions: [
        { title: "10%", value: "10" },
        { title: "20%", value: "20" },
        { title: "30%", value: "30" },
        { title: "40%", value: "40" },
        { title: "50%", value: "50" },
      ],
      normalizeoptions: [
        { title: "Yes", value: "yes" },
        { title: "No", value: "no" },
      ],
      steps: customizationTour,
      infographics_icon: infographics_icon,
      trainTitle: "Training Data Pecentage",
      trainInfo: "This is zxy, abc.",
      isModalVisible: false,
      message: "Helloo",
      title: "My Title",
      selected: this.analysis,
    };
  },
  mounted: function () {
    console.log(this.analysisType);
    this.$tours["myTour"].start();
  },
  methods: {
    showModal() {
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
    showTrain() {
      this.title = "Training Data Percentage";
      this.message = `Refers to the percentage of data being used to train and teach the model 
      the hidden features or patterns in the data.
      Example: Training data is fed to the neural network continuously, in order for the model to 
      continue to learn the features of the data. `;
      this.showModal();
    },
    showNormalization() {
      this.title = "Normalization";
      this.message = `The process of transforming or changing the columns in a dataset to a common
       scale is referred to as Normalization.
       Example: In the process known as Min-Max scaling, values are rescaled to ensure that the 
       values are within a specified range varying between 0 and 1. The process of scaling these 
       values on a common scale is known as normalization.`;
      this.showModal();
    },
    showAnalysisType() {
      switch (this.analysisType) {
        case "Binary Classification":
          this.title = "Binary Classification";
          this.message = `A type of classification that predicts categorical variables and categorizes
           the output into two classes. This is especially important when predicting a possible outcome
            based on a series of data given.
            Example: A patient displaying multiple symptoms for a particular disease is predicted to be 
            ‘healthy’ or ‘carrying the disease’ based on the two possible outcomes of their diagnosis. 
            This outcome is categorized into two classes known as positive and negative. `;
          break;
        case "Multivariate Classification":
          this.title = "Multivariate Classification";
          this.message = `The term ‘multivariate’ refers to having one or more variables. It is the process
           by which data contains observations with more than one variable or outcome being measured.
           Example: The measurement of a star in terms of different variables such as its color, luminosity 
           and environment`;
          break;
        case "Prediction":
          this.title = "Prediction";
          this.message = `The end result or output of an algorithm that has been trained on a dataset 
          containing  already existing data and new data in an effort to determine a particular outcome.
          Example: Determining or predicting the weather forecast for a particular day based on a historical 
          dataset and new data gathered.`;
          break;
        default:
          this.title = "Type of Analysis";
          this.message = `There are several different types of problems that can be modeled using neural networks. 
          These include: Binary Classification, Multivariate Classification, Prediction and Regression.`;
          break;
      }

      this.showModal();
    },
  },
};
</script>
