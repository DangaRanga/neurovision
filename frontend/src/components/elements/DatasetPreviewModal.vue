<template>
  <!-- Main modal -->

  <data-table
    :headings="heartData.headings"
    :rows="heartData.rows"
  ></data-table>
</template>
<script setup>
import DataTable from "@/components/elements/DataTable.vue";
import { ref } from "vue";

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
</script>
