<template>
  <!-- Main modal -->
  <div class="modal-backdrop" :class="'hidden'">
    <div class="custom-modal w-3/5">
      <header id="modal-header" class="flex items-start">
        <div>
          <h1 class="text-3xl font-bold">{{ headerText }}</h1>
          <p class="text-gray-700 my-3">{{ description }}</p>
          <p class="my-3 font-semibold">Problem Type: {{ problemType }}</p>
          <p class="my-3 font-semibold">
            No Records: {{ heartData.rows.length }}
          </p>
        </div>

        <button class="text-3xl" @click="close">x</button>
      </header>
      <section id="modal-body" class="rounded">
        <data-table
          :headings="heartData.headings"
          :rows="heartData.rows"
        ></data-table>
      </section>
    </div>
  </div>
</template>
<script>
import DataTable from "@/components/elements/DataTable.vue";

export default {
  props: {
    headerText: String,
    description: String,
    heartData: {
      headings: Array,
      rows: [],
    },
    problemType: String,
  },

  components: {
    "data-table": DataTable,
  },
};
</script>
<script setup></script>

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
.custom-modal {
  background: #ffffff;
  border-radius: 5px;
  overflow-x: auto;
  display: flex;
  padding: 35px 60px;
  flex-direction: column;
}

.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  position: relative;
  border-bottom: 1px solid #eeeeee;
  color: #4aae9b;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  flex-direction: column;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  position: absolute;
  top: 0;
  right: 0;
  border: none;
  font-size: 20px;
  padding: 10px;
  cursor: pointer;
  font-weight: bold;
  color: #4aae9b;
  background: transparent;
}

.btn-green {
  color: white;
  background: #4aae9b;
  border: 1px solid #4aae9b;
  border-radius: 2px;
}

.hidden {
}
</style>
