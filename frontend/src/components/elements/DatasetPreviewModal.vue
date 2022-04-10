<template>
  <!-- Main modal -->
  <div class="modal-backdrop">
    <div class="modal">
      <header id="modal-header">
        <h1 class="text-3xl font-bold">Modal Title</h1>
        <button type="button" class="btn-close" @click="close">x</button>
      </header>
      <section id="modal-body">
        <data-table
          :headings="heartData.headings"
          :rows="heartData.rows"
        ></data-table>
      </section>
    </div>
  </div>
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
<script>
export default {
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>
<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal {
  background: #ffffff;
  border-radius: 5px;
  overflow-x: auto;
  display: flex;
  padding: 50px 60px;
  flex-direction: column;
}
</style>
