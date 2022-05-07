<template>
  <div
    class="flex flex-col items-center justify-center border h-screen"
    id="v-step-0"
  >
    <div class="grid grid-cols-3 mt-48" id="v-step-1">
      <article v-for="(dataset, index) in datasets" :key="index">
        <selector-item
          :image="dataset.image"
          :title="dataset.title"
          :summary="dataset.summary"
          :dataset-index="index"
          @select="selectDataset"
          v-bind="index"
        ></selector-item>
      </article>
    </div>
    <div class="mx-auto">
      <button
        @click="showDatasetPreviewModal()"
        class="text-white bg-gray-500 font-semibold rounded-md py-3 px-4 hover:bg-gray-600 transition-colors duration-200"
        id="v-step-2"
      >
        Preview Selected Dataset
      </button>

      <router-link
        class="text-white bg-primary hover:bg-blue-500 rounded-md py-3 px-4 mx-3 transition-colors duration-200"
        id="v-step-3"
        :to="{
          name: 'dataset',
          params: { analysisType: 'prediction' },
        }"
      >
        Next Step
      </router-link>
    </div>
    <div class="my-3">
      <p class="text-center font-medium text-primary_dark">
        Not sure which to select? Preview each dataset to learn more!
      </p>
    </div>

    <dataset-preview-modal
      v-if="isModalVisible && selectDataset"
      @close="closeModal"
      :title="datasets[selectedDataset].title"
      :data="dataset"
      :problem-type="datasets[selectedDataset].problemType"
    />
    <v-tour name="myTour" :steps="steps"></v-tour>
  </div>
</template>
<script>
import SelectorItem from "@/components/elements/SelectorItem.vue";
import DatasetPreviewModal from "@/components/elements/DatasetPreviewModal.vue";
import {
  heartDiseaseData,
  irisPredictionData,
  housePredictionData,
} from "@/constants/dataset.constants";

export default {
  data() {
    return {
      datasets: [heartDiseaseData, irisPredictionData, housePredictionData],
      selectedDataset: undefined,
      isModalVisible: false,
      data: null,
      dataset: {
        headings: [],
        rows: [],
      },
      steps: [
        {
          target: "#v-step-0", // We're using document.querySelector() under the hood
          content: `Welcome to <strong>Neurovision.</strong> Where we learn all the basis of neural networks! `,
        },
        {
          target: "#v-step-1",
          content:
            "<strong>Let's Get Started!!</strong> First select a dataset for building the neural network model!",
          params: {
            placement: "top",
          },
        },
        {
          target: "#v-step-2",
          content:
            "<strong>Great!!</strong> Next preview the contents of the dataset selected.",
          params: {
            placement: "top",
          },
        },
        {
          target: "#v-step-3",
          content: "Now that you have previewed the dateset let's move on!!!",
          params: {
            placement: "top",
          },
        },
      ],
    };
  },
  methods: {
    showDatasetPreviewModal() {
      if (this.selectedDataset === undefined) {
        console.log("No Dataset selected");
      } else {
        this.isModalVisible = true;
      }
    },
    isSelected(title) {
      if (title == this.selectDataset) {
        console.log("This works");
        return true;
      } else {
        return false;
      }
    },
    closeModal() {
      this.isModalVisible = false;
    },

    selectDataset(dataset) {
      this.selectedDataset = dataset;
      console.log(this.datasets[dataset]);
      this.$http
        .get(
          `http://localhost:9090/api/data?dataset=${this.datasets[dataset].name}`,
          {}
        )
        .then((response) => {
          const newData = response.data.dataset;
          this.dataset = {
            headings: newData.columns,
            rows: newData.data,
          };
        });
    },
  },
  components: {
    "selector-item": SelectorItem,
    "dataset-preview-modal": DatasetPreviewModal,
  },

  watch: {
    data: {
      handler(newValue, oldValue) {
        console.log(newValue);
        // Note: `newValue` will be equal to `oldValue` here
        // on nested mutations as long as the object itself
        // hasn't been replaced.
      },
      deep: true,
    },
  },
  mounted: function () {
    this.$tours["myTour"].start();
  },
};
</script>
