<template>
  <div class="flex flex-col items-center justify-center border h-screen">
    <div class="grid grid-cols-3 mt-48">
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
      >
        Preview Selected Dataset
      </button>

      <router-link
        class="text-white bg-primary hover:bg-blue-500 rounded-md py-3 px-4 mx-3 transition-colors duration-200"
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
      :data="heartDataset"
      :description="datasets[selectedDataset].description"
      :problem-type="datasets[selectedDataset].problemType"
    />
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
      heartDataset: {
        headings: [
          "PatientId",
          "Species",
          "ChestPainType",
          "RestingBP",
          "Cholesterol",
          "MaxHR",
          "ST_Slope",
          "ST_Slope",
          "ST_Slope",
        ],
        rows: [
          [0, "Homo sapiens", "ATA", "150", "214", "168", "Up", "Up", "Up"],
          [0, "Homo sapiens", "ATA", "150", "214", "168", "Up", "Up", "Up"],
          [0, "Homo sapiens", "ATA", "150", "214", "168", "Up", "Up", "Up"],
          [0, "Homo sapiens", "ATA", "150", "214", "168", "Up", "Up", "Up"],
        ],
      },
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
      console.log(this.selectedDataset);
    },
  },
  components: {
    "selector-item": SelectorItem,
    "dataset-preview-modal": DatasetPreviewModal,
  },
};
</script>
SelectorItem
