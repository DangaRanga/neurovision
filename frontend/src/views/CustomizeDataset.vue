<template>
  <div
    class="pl-12 flex flex-col flex-wrap h-full md:items-center lg:items-start md:flex-row md:flex-nowrap"
  >
    <div
      class="flex-shrink-0 w-full md:w-2/3 mx-auto text-left md:mx-8 md:text-left pt-28"
    >
      <data-table
        class="w-full mr-8"
        :headings="dataset.headings"
        :rows="dataset.rows"
        :height="'h-96'"
      ></data-table>
    </div>
    <dataset-sidebar
      class="w-1/3"
      :analysisType="analysisType"
      :datasettitle="title"
      :description="description"
    />
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
      analysisType: "",
      title: "",
      description: "",
    };
  },
  computed: {
    dataset() {
      return JSON.parse(localStorage.getItem("base-dataset"));
    },
  },

  mounted() {
    this.analysisType = this.$route.params.analysisType;
    this.title = this.$route.params.title;
    this.description = this.$route.params.description;
    console.log(this.analysisType);
  },
  update() {
    this.analysisType = this.$route.params.analysisType;
    this.title = this.$route.params.title;
    this.description = this.$route.params.description;
    console.log(this.dataset);
  },
};
</script>
