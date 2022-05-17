<template>
  <div>
    <model-header 
      :isHidden="isHidden" 
      :close="toggleHidden" 
      :headers="headers" 
      :toggleRunning="toggleRunning"
      :isRunning="isRunning"
    />
    <div v-if="!isHidden" class="grid grid-cols-3 min-h-screen">
      <div class="col-span-2 grid items-center">
        <div>
          <div class="flex flex-col justify-center items-center mb-20">
            <h1 class="mx-auto font-extrabold text-4xl">Playground</h1>
            <h1 class="mx-auto mt-2 font-semibold text-lg text-grey">
              Test the structure of your neural network
            </h1>
          </div>
          <model-build
            :num_hidden="num_hidden"
            :layers="layers"
            :mappings="mappings"
            :width="width"
            :height="height"
            :isRunning="isRunning"
            :epochs="headers[1].value"
            :toggleRunning="toggleRunning"
            :training="training"
          />
        </div>
      </div>
      <model-sidebar
        @restart="updateParams"
        :batch="headers[0].value"
        :epoch="headers[1].value"
        :lrate="headers[2].value"
        :loss="headers[3].value"
        :numRecords="dataset.rows.length"
        :isRunning="isRunning"
        :graph="[accuracy, loss]"
      />
    </div>
    <div v-if="isHidden" class="grid items-center min-h-screen">
      <div class="flex flex-col justify-center items-center mt-20 mb-20">
        <h1 class="mx-auto font-extrabold text-4xl">Playground</h1>
        <h1 class="mx-auto mt-2 font-medium text-lg text-grey">
          Test the structure of your neural network
        </h1>
      </div>
      <model-build
        :num_hidden="num_hidden"
        :layers="layers"
        :mappings="mappings"
        :width="width"
        :height="height"
        :isRunning="isRunning"
        :epochs="headers[1].value"
        :toggleRunning="toggleRunning"
        :training="training"
      />
    </div>
  </div>
</template>

<script>
import RMHeader from "@/components/elements/RMHeader.vue";
import RMSidebar from "@/components/elements/RMSidebar.vue";
import RModel from "@/components/elements/RModel.vue";
import * as d3 from "d3";

export default {
  components: {
    "model-header": RMHeader,
    "model-sidebar": RMSidebar,
    "model-build": RModel,
  },
  data() {
    return {
      isRunning: false,
      problem: "regression",
      width: 900,
      height: 500,
      num_hidden: 1,
      activation: [],
      layers: [],
      mappings: [],
      isHidden: true,
      headers: [
        { header: "Batch Size", value: 1 },
        { header: "Epoch No.", value: 100 },
        { header: "Learning Rate", value: 0.01 },
        { header: "Loss Function", value: "MSE" },
        { header: "Problem Type", value: "Classification" },
      ],
      evaluation: {},
      training: {},
    };
  },
  computed: {
    dataset(){
      return JSON.parse(localStorage.getItem("base-dataset"));
    },
    accuracy(){
      return {
        epochs: this.training.epochs,
        acc: this.training.acc_hist
      };
    },
    loss(){
      return {
        epochs: this.training.epochs,
        loss: this.training.acc_hist
      };
    }
  },
  methods: {
    createmapping() {
      const id = (d) => d.id;
      let newmappings = [];
      const l_scale = d3
        .scaleBand()
        .domain(this.layers.map(id))
        .range([0, this.width]);

      var y = d3.scaleLinear().rangeRound([0, this.height / 5]);

      for (let layer = 0; layer < this.layers.length - 1; layer++) {
        const sourcelayer = this.layers[layer];
        const targetlayer = this.layers[layer + 1];

        sourcelayer.nodes.forEach((sourcenode) => {
          targetlayer.nodes.forEach((targetnode) => {
            newmappings = [
              ...newmappings,
              {
                sourceid: sourcenode.id,
                sourcelayer: sourcenode.layer,
                sourcex: l_scale(sourcenode.layer) + 68,
                sourcey: y(sourcenode.id) + 50,
                targetid: targetnode.id,
                targetlayer: targetnode.layer,
                targetx: l_scale(targetnode.layer) + 30,
                targety: y(targetnode.id) + 50,
              },
            ];
          });
        });
      }
      this.mappings = newmappings;
    },
    deleteNodeMapping(sourcelayer, sourceid) {
      let removed;
      for (let mapping = 0; mapping < this.mappings.length; mapping++) {
        if (
          this.mappings[mapping].sourcelayer == sourcelayer &&
          this.mappings[mapping].sourceid == sourceid
        ) {
          removed = this.mappings.splice(mapping, 1);
        } else {
          if (
            this.mappings[mapping].targetlayer == sourcelayer &&
            this.mappings[mapping].targetid == sourceid
          ) {
            removed = this.mappings.splice(mapping, 1);
          }
        }
      }
    },
    deleteLayerMapping(sourcelayer) {
      let removed;
      for (let mapping = 0; mapping < this.mappings.length; mapping++) {
        if (this.mappings[mapping].sourcelayer == sourcelayer) {
          removed = this.mappings.splice(mapping, 1);
        } else {
          if (this.mappings[mapping].targetlayer == sourcelayer) {
            removed = this.mappings.splice(mapping, 1);
          }
        }
      }
    },
    toggleHidden() {
      this.isHidden = !this.isHidden;
    },
    toggleRunning(){
      this.isRunning = !this.isRunning;
    },
    updateParams(data) {
      for (var obj in data) {
        this.headers = this.headers.map((d) => {
          if (d.header == data[obj].title) {
            return { header: d.header, value: data[obj].value };
          } else {
            return d;
          }
        });
      }
      this.updateModel();
      this.isRunning = false;
    },
    updateModel() {
      
      const dataSnap = JSON.parse(localStorage.getItem("data-snap"));

      this.problem = dataSnap.problem;
      this.layers = dataSnap.layers;
      this.activation = dataSnap.activation;
      this.num_hidden = dataSnap.num_hidden;

      const dataset = this.dataset;
      const train = Number(localStorage.getItem("train"));
      const hlayer = this.layers
        .filter((d) => d.name.includes("hidden"))
        .map((d) => Number(d.nodes.length));
      const act = this.activation.map((d) => d.toLowerCase());

      localStorage.setItem("data-snap", JSON.stringify({
        num_hidden: this.num_hidden,
        layers: this.layers,
        problem: this.problem,
        activation: this.activation
      }));

      this.$http
        .post(
          `${process.env.VUE_APP_API_URL}/model/run`, 
          {
            data: dataset,
            layers: hlayer || [1],
            activations: act || ["relu"],
            lr: this.headers[2].value || 0.5,
            batch_size: this.headers[0].value || 1,
            epochs: this.headers[1].value || 10,
            prob: this.problem,
            train: train || 80,
          }
        ).then((response) => {
          const newData = response.data;
          this.evaluation = newData.evaluation;
          this.training = newData.training;
        });
    },
  },
  created() {

    const dataSnap = JSON.parse(localStorage.getItem("data-snap"));

    this.num_hidden = this.$route.params.hidden || dataSnap.num_hidden;
    this.layers = this.$route.params.struct
      ? JSON.parse(this.$route.params.struct)
      : JSON.parse(localStorage.getItem("layer-struct"));
    this.activation = this.$route.params.activation || dataSnap.activation;
    this.problem = this.$route.params.name || this.dataset.name;
    this.headers = this.headers.map((d) => {
      if (d.header == "Problem Type") {
        return {
          header: d.header,
          value: this.$route.params.problem || this.dataset.analysisType,
        };
      } else {
        return d;
      }
    });

    console.log(this.activation)
    localStorage.setItem("data-snap", JSON.stringify({
      num_hidden: this.num_hidden,
      layers: this.layers,
      problem: this.problem,
      activation: this.activation
    }));

    this.createmapping();
  },
  mounted() {
    this.updateModel();
  },
};
</script>
