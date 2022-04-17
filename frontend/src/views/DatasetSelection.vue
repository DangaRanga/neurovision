<template>
  <div class="flex flex-col items-center justify-center border h-screen">
    <div class="grid grid-cols-3 mt-48">
      <selector-item
        image=""
        title="Heart Predict Dataset"
        summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
      ></selector-item>
      <selector-item
        image=""
        title="Iris Dataset"
        summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
      ></selector-item>
      <selector-item
        image=""
        title="House Price Dataset"
        summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
      ></selector-item>
    </div>
    <div class="mx-auto">
      <button
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
      :header-text="'Test Modal'"
      :heart-data="heartData"
      :description="description"
    />
  </div>
</template>
<script>
import SelectorItem from "@/components/elements/SelectorItem.vue";
import DatasetPreviewModal from "@/components/elements/DatasetPreviewModal.vue";
import { ref } from "vue";
export default {
  setup() {
    // eslint-disable-next-line no-unused-vars
    const selected = ref(null);

    // eslint-disable-next-line no-unused-vars
    function toggleDatasetPreview() {}
  },
  data() {
    return {
      description: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur.`,
      heartData: {
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
  components: {
    "selector-item": SelectorItem,
    "dataset-preview-modal": DatasetPreviewModal,
  },
};
</script>
