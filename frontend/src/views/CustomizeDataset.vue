<template>
  <div
    class="pl-12 flex flex-col flex-wrap h-full md:items-center lg:items-start md:flex-row md:flex-nowrap"
  >
    <div
      class="flex-shrink-0 w-full md:w-2/3 mx-auto text-left md:mx-8 md:text-left pt-28"
    >
      <data-table
        class="w-full mr-8"
        :headings="heartDataset.headings"
        :rows="heartDataset.rows"
      ></data-table>
    </div>
    <dataset-sidebar class="w-1/3" :analysis="analysisType" />
  </div>
</template>
<script>
import DatasetSideBar from "@/components/elements/DatasetSideBar.vue";
import DataTable from "@/components/elements/DataTable.vue";
export default {
  components: {
    "dataset-sidebar": DatasetSideBar,
    "data-table": DataTable,
  },
  data() {
    return {
      analysisType: "None",
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
  created() {
    this.analysisType = this.$route.params.analysisType;
  },
};
</script>
