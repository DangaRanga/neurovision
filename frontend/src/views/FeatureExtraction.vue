<template>
  <main class="flex flex-col items-center my-5">
    <h1 class="text-3xl font-bold my-3 text-grey">
      Extracting Dataset Features
    </h1>
    <p class="text-grey">
      Selecting inputs from our dataset and highlighting the output
    </p>
    <div class="w-4/5 my-5">
      <data-table
        class="w-full mr-8"
        :headings="dataset.headings"
        :rows="dataset.rows"
        :height="'h-96'"
      ></data-table>
    </div>
    <button @click="removeFeature()">test</button>
  </main>
</template>
<script>
import DataTable from "@/components/elements/DataTable.vue";
import {
  irisFeatures,
  houseFeatures,
  heartFeatures,
} from "../constants/featureExraction.js";

export default {
  data() {
    return {
      removeableFeatures: [],
      dataset: JSON.parse(localStorage.getItem("base-dataset")),
    };
  },
  components: {
    "data-table": DataTable,
  },

  methods: {
    removeFeature() {
      // Remove feature from dataset
      const feature = this.removeableFeatures.pop();
      console.log(`Feature is ${feature.name}`);
      // Fetch the data
      this.$http
        .post(`${process.env.VUE_APP_API_URL}/data/rfeature`, {
          data: {
            headings: this.dataset.headings,
            rows: this.dataset.rows,
            index: this.dataset.index,
          },
          featureName: feature.name,
        })
        .then((response) => {
          const newData = response.data.dataset;
          const data = {
            headings: newData.columns,
            rows: newData.data,
            analysisType: this.dataset.analysisType,
            title: this.dataset.title,
            description: this.dataset.summary,
            index: newData.index,
            name: this.dataset.name,
          };
          this.dataset = data;
          localStorage.setItem("base-dataset", JSON.stringify(data));
        });

      const datasetColumn = this.dataset.headings.indexOf(feature.name);
      console.log(datasetColumn);

      console.log(this.removeableFeatures);
    },
  },

  mounted() {
    const datasetObj = {
      heart_disease: heartFeatures,
      house_price: houseFeatures,
      iris: irisFeatures,
    };

    this.removeableFeatures = datasetObj[this.dataset.name];
  },
};
</script>
