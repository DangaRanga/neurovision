<template>
  <aside>
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
              <p class="w-4/5 text-s font-semibold py-2">Type of Analysis</p>
              <img
                :src="infographics_icon"
                alt="train_info"
                class="object-cover pt-2 mr-6 pr-10 items-center justify-center"
                @click="showAnalysisType()"
              />
            </div>
            <select
              name="datasettype"
              id="datasettype"
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
              <img
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
              <img
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
            <button
              className="w-1/3 bg-grey_dark text-white text-xs font-bold px-4 py-3 rounded shadow hover:shadow-md outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3"
              type="button"
            >
              Pervious Step
            </button>
            <button
              className="w-1/3 bg-primary text-white text-xs font-semibold px-4 py-3 rounded shadow hover:shadow-md outline outline-1 lg:mr-1 lg:mb-0 ml-3 mb-3"
              type="button"
            >
              Next Step
            </button>
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
      infographics_icon: infographics_icon,
      trainTitle: "Training Data Pecentage",
      trainInfo: "This is zxy, abc.",
      isModalVisible: false,
      message: "Helloo",
      title: "My Title",
      analysisType: this.analysis,
    };
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
      this.message =
        "This is the train Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare facilisis pellentesque vitae eget. Felis etiam elit tincidunt dis habitasse metus elementum enim.";
      this.showModal();
    },
    showNormalization() {
      this.title = "Normalization";
      this.message =
        "Normalization is Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare facilisis pellentesque vitae eget. Felis etiam elit tincidunt dis habitasse metus elementum enim. Id auctor enim vulputate sed in fusce non massa. ";
      this.showModal();
    },
    showAnalysisType() {
      switch (this.analysisType) {
        case "binaryClassification":
          this.title = "Binary Classification";
          this.message =
            "Binary Classification is Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare facilisis pellentesque vitae eget. Felis etiam elit tincidunt dis habitasse metus elementum enim. Id auctor enim vulputate sed in fusce non massa. Vulputate etiam nunc, vitae elit sem faucibus pulvinar.";
          break;
        case "multivariateClassification":
          this.title = "Multivariate Classification";
          this.message =
            "Multivariable Classification is Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare facilisis pellentesque vitae eget. Felis etiam elit tincidunt dis habitasse metus elementum enim. Id auctor enim vulputate sed in fusce non massa. Vulputate etiam nunc, vitae elit sem faucibus pulvinar.";
          break;
        case "prediction":
          this.title = "Prediction";
          this.message =
            "Prediction is Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare facilisis pellentesque vitae eget. Felis etiam elit tincidunt dis habitasse metus elementum enim. Id auctor enim vulputate sed in fusce non massa. Vulputate etiam nunc, vitae elit sem faucibus pulvinar.";
          break;
        default:
          this.title = "Type of Analysis";
          this.message =
            "There are several different types of problems that can be modeled using neural networks. These include: Binary Classification, Multivariate Classification, Prediction and Regression.";
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