<template>
  <div class="flex flex-col items-center justify-center border h-screen">
    <div class="grid grid-cols-3 my-10">
      <selector-item
        image=""
        title="Heart Predict Dataset"
        summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
      ></selector-item>
      <selector-item
        image=""
        title="cat image"
        summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
      ></selector-item>
      <selector-item
        image=""
        title="cat image"
        summary="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
      ></selector-item>
    </div>
    <div class="mx-auto">
      <button
        class="text-white bg-gray-500 font-semibold rounded-md py-3 px-4 hover:bg-gray-600 transition-colors duration-200"
      >
        Preview Selected Dataset
      </button>

      <button
        class="text-white bg-primary hover:bg-blue-500 rounded-md py-3 px-4 mx-3 transition-colors duration-200"
      >
        Next Step
      </button>
    </div>
    <div class="my-3">
      <p class="text-center font-medium text-primary_dark">
        Not sure which to select? Preview each dataset to learn more!
      </p>
    </div>
    <dataset-preview-modal />
  </div>
</template>
<script>
import SelectorItem from "@/components/elements/SelectorItem.vue";
import DatasetPreviewModal from "@/components/elements/DatasetPreviewModal.vue";
import { ref } from "vue";
export default {
  setup() {
    const selected = ref(null);

    const heartData = ref({
      headings: [
        "PatientId",
        "Species",
        "ChestPainType",
        "RestingBP",
        "Cholesterol",
        "MaxHR",
        "ST_Slope",
      ],
      rows: [
        [0, "Homo sapiens", "ATA", "150", "214", "168", "Up"],
        [0, "Homo sapiens", "ATA", "150", "214", "168", "Up"],
        [0, "Homo sapiens", "ATA", "150", "214", "168", "Up"],
        [0, "Homo sapiens", "ATA", "150", "214", "168", "Up"],
      ],
    });
    function toggleDatasetPreview() {}
  },

  components: {
    "selector-item": SelectorItem,
    "dataset-preview-modal": DatasetPreviewModal,
  },
};
</script>
