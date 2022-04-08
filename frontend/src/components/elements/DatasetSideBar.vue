<template>
  <aside>
    <div class="bg-primary_light grid grid-cols-1 py-10 w-full">
      <div class="w-full pl-8 pr-12">
        <h3 class="text-lg font-bold py-2">Dataset - Heart Disease Prediction</h3>
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
            >
              <option value="binaryClassification">Binary Classification</option>
              <option value="multipleClassification">
                Multiple Classification
              </option>
              <option value="prediction">Pediction</option>
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
              <p class="w-4/5 text-s font-semibold py-2">Normalize Data</p>
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
  data() {
    return {
      infographics_icon: infographics_icon,
      trainTitle: "Training Data Pecentage",
      trainInfo: "This is zxy, abc.",
      isModalVisible: false,
      message: "Helloo",
      title: "My Title",
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
      this.message = "This is the train xyz";
      this.showModal();
    },
    showNormalization() {
      this.title = "Normalize";
      this.message = "Normalization is abc";
      this.showModal();
    },
    showAnalysisType() {
      this.title = "Binary Classification";
      this.message = "Binary Classification id qrs";
      this.showModal();
    },
  },
};
</script>
