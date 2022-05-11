<template>
  <aside id="v-step-0">
    <div class="bg-primary_light grid grid-cols-1 py-10 w-full">
      <div class="w-full pl-8 pr-12">
        <h3 class="text-lg font-bold py-2">
          Dataset - Heart Disease Prediction
        </h3>
        <p class="text-s font-regular py-2">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Dictum enim
          pellentesque auctor ipsum integer feugiat risus nulla sed
        </p>
      </div>
      <div class="w-full">
        <form class="pl-10 py-6">
          <div class="py-4">
            <div
              class="flex flex-row flex-nowrap md:items-center lg:items-start md:flex-row md:flex-nowrap"
            >
              <p id="v-step-1" class="w-4/5 text-s font-semibold py-2">Type of Analysis</p>
              <img
                :src="infographics_icon"
                alt="train_info"
              id="v-step-2" class="object-cover pt-2 mr-6 pr-10 items-center justify-center"
                @click="showAnalysisType()"
              />
            </div>
            <select
              name="datasettype"
              id="datasettype"
              v-model="selected"
              class="bg-white rounded-sm outline outline-1 outline-white w-2/3 md:w-5/6 h-8 text-s"
              @change="onChange($event)"
            >
              <option value="binaryClassification">
                Binary Classification
              </option>
              <option value="multivariateClassification">
                Multiple Classification
              </option>
              <option value="prediction">Prediction</option>
            </select>
          </div>
          <div class="py-4">
            <div
              class="flex flex-row flex-nowrap md:items-center lg:items-start md:flex-row md:flex-nowrap"
            >
              <p class="w-4/5 text-s font-semibold py-2">
                Training Data Percentage
              </p>
              <img id="v-step-3"
                :src="infographics_icon"
                alt="train_info"
                class="object-cover pt-2 mr-6 pr-10 items-center justify-center"
                @click="showTrain()"
              />
            </div>
            <select
              name="datasplit"
              id="datasplit"
              class="bg-white rounded-sm outline outline-1 outline-white w-2/3 md:w-5/6 h-8 text-s"
            >
              <option value="10">10%</option>
              <option value="20">20%</option>
              <option value="30">30%</option>
              <option value="40">40%</option>
              <option value="50">50%</option>
            </select>
          </div>
          <div class="py-4">
            <div
              class="flex flex-row flex-nowrap md:items-center lg:items-start md:flex-row md:flex-nowrap"
            >
              <p class="w-4/5 text-s font-semibold py-2">
                Perform Normalization?
              </p>
              <img id="v-step-4"
                :src="infographics_icon"
                alt="normalization_info"
                class="object-cover pt-2 mr-6 pr-10 items-center justify-center"
                @click="showNormalization()"
              />
            </div>
            <select
              name="normalize"
              id="normalize"
              class="bg-white rounded-sm outline outline-1 outline-white w-2/3 md:w-5/6 h-8 text-s"
            >
              <option value="yes">Yes</option>
              <option value="no">No</option>
            </select>
          </div>

          <div
            class="px-4 pt-12 mt-6 mb-4 flex flex-col text-center sm:flex-row sm:text-left sm:items-baseline"
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
            <router-link id="v-step-5"
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
          <p class="px-4 mx-auto">Step 2 of 5</p>
        </form>
      </div>
    </div>

    <Modal
      :topic="title"
      :message="message"
      v-show="isModalVisible"
      @close="closeModal"
    />
  </aside>
<v-tour name="myTour" :steps="steps"></v-tour>
</template>
<script>
// import DataTable from "@/components/elements/DataTable.vue";
import infographics_icon from "@/assets/icons/infographics_icon.svg";
import InfograpicModal from "@/components/elements/Infographic.vue";

export default {
  components: {
    Modal: InfograpicModal,
  },
  props: {
    analysis: String,
  },
  data() {
    return {
      steps: [
        {
          target: "#v-step-0", // We're using document.querySelector() under the hood
          content: ` <strong>Let's get to customizing our Dataset</strong>!
          Dataset customization involves 
          Dataset customization is important because..`,
          params: {
            placement: "left",
          },
        },
        {
          target: "#v-step-1",
          content: `There are several different types of problems that can be modeled using neural networks.
          These include: <strong>Binary Classification, Multivariate Classification, Prediction and Regression.<\strong>`,
          params: {
          placement: "left",
          },
        },
        {
          target: "#v-step-2",
          content:
            `<strong>Let us get some information on the Type of Analysis that the dataset is performing</strong>!`,
          params: {
            placement: "top",
          },
        },
        {
          target: "#v-step-3",
          content:
            `<strong>Let us get some information on the Training Data Percentage needed for this dataset</strong>!`,
          params: {
            placement: "top",
          },
        },
         {
          target: "#v-step-4",
          content:
            `<strong>Let us get some information on what Normalization is </strong>.`,
          params: {
            placement: "top",
          },
        },
        {
          target: "#v-step-5",
          content:
            `<strong>Hooray!, now that you've customized the dataset let's continue </strong>.`,
          params: {
            placement: "top",
          },
        },
      ],
      infographics_icon: infographics_icon,
      trainTitle: "Training Data Pecentage",
      trainInfo: "This is zxy, abc.",
      isModalVisible: false,
      message: "Helloo",
      title: "My Title",
      analysisType: this.analysis,
      selected: this.analysis,
    };
  },
   mounted: function () {
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
        case "binaryClassification":
          this.title = "Binary Classification";
          this.message = `A type of classification that predicts categorical variables and categorizes
           the output into two classes. This is especially important when predicting a possible outcome
            based on a series of data given.
            Example: A patient displaying multiple symptoms for a particular disease is predicted to be 
            ‘healthy’ or ‘carrying the disease’ based on the two possible outcomes of their diagnosis. 
            This outcome is categorized into two classes known as positive and negative. `;
          break;
        case "multivariateClassification":
          this.title = "Multivariate Classification";
          this.message = `The term ‘multivariate’ refers to having one or more variables. It is the process
           by which data contains observations with more than one variable or outcome being measured.
           Example: The measurement of a star in terms of different variables such as its color, luminosity 
           and environment`;
          break;
        case "prediction":
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
    onChange(event) {
      let analysisOption = event.target.value;
      this.analysisType = analysisOption;
      var optionText =
        event.target.options[event.target.options.selectedIndex].text;

      console.log(optionText);
    },
  },
};
</script>
