<template>
  <main class="flex flex-col items-center my-5">
    <h1 class="text-3xl font-bold my-3 text-grey">Feature Engineering</h1>
    <p class="text-grey">{{ rationale }}</p>
    <div class="w-4/5 my-5">
      <data-table
        class="w-full mr-8"
        :headings="dataset.headings"
        :rows="dataset.rows"
        :height="'h-96'"
        :index_highlighted="featureIndex"
      ></data-table>
    </div>
    <button @click="performFeatureEngineering()">test</button>
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
      engineeringStep: 1,
      featureIndex: -1,
      rationale: `Here we will make the necessary changes to our dataset to prepare it for
      predictions!`,
    };
  },
  components: {
    "data-table": DataTable,
  },

  methods: {
    highlightFeature() {
      // Feature to be extracted will always be the first
      const feature = this.removeableFeatures[0];

      // Update description of action being performed
      this.rationale = feature.reason;

      // Highlight the feature
      const datasetColumn = this.dataset.headings.indexOf(feature.name);
      if (datasetColumn !== -1) {
        this.featureIndex = datasetColumn;
      }

      this.engineeringStep = 2;
    },

    removeFeature() {
      // Remove feature from dataset
      const feature = this.removeableFeatures.pop();
      console.log(`Feature is ${feature.name}`);

      // Remove the feature and refresh dataset
      this.featureEngineeringQuery("/data/rfeature", feature.name);

      // Unhighlight next feature
      this.featureIndex = -1;

      // Restart steps until all features are extracted
      if (this.removeableFeatures.length > 0) {
        this.engineeringStep = 1;
      } else {
        this.engineeringStep = 3;
      }
    },

    removeInvalid() {
      // Remove the feature and refresh dataset
      this.featureEngineeringQuery("/data/rinvalid");

      // Update engineering steps to step 3
      this.engineeringStep = 4;
    },

    translateData() {
      // Translate dataset data
      this.featureEngineeringQuery("/data/translate");

      // Move to next step
      this.engineeringStep = 5;
    },

    normalizeData() {
      // Perform dataset normalization
      this.featureEngineeringQuery("/data/normalize");

      // Mark Feature engineering as completed
      this.engineeringStep = 6;
    },

    featureEngineeringQuery(endpoint, featureName) {
      // Develop query object
      let query = {
        data: {
          headings: this.dataset.headings,
          rows: this.dataset.rows,
          index: this.dataset.index,
        },
      };

      if (featureName) {
        query["featureName"] = featureName;
      }

      // Perform feature engineering query
      this.$http
        .post(`${process.env.VUE_APP_API_URL}${endpoint}`, query)
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

          // Cache the data for reuse
          this.dataset = data;
          localStorage.setItem("base-dataset", JSON.stringify(data));
        });
    },

    performFeatureEngineering() {
      if (this.engineeringStep === 1) {
        this.highlightFeature();
      } else if (this.engineeringStep === 2) {
        this.removeFeature();
      } else if (this.engineeringStep === 3) {
        this.removeInvalid();
      } else if (this.engineeringStep === 4) {
        this.translateData();
      } else if (this.engineeringStep === 5) {
        this.normalizeData();
      } else {
        // Navigate to next page
      }
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
