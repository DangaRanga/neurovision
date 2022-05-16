<template>
  <div>
    <model-header 
      :isHidden=isHidden 
      :close=close 
      :headers="headers"
    />
    <div v-if="!isHidden" class="grid grid-cols-3 min-h-screen">
      <div class="col-span-2 grid items-center">
        <div>
          <div class="flex flex-col justify-center items-center mb-20">
            <h1 class="mx-auto font-extrabold text-4xl">Playground</h1>
            <h1 class="mx-auto mt-2 font-semibold text-lg text-grey">Test the structure of your neural network</h1>
          </div>
          <model-build 
            :num_hidden="num_hidden"
            :layers="layers"
            :mappings="mappings"
            :width="width"
            :height="height"
          />
        </div>
      </div>
      <model-sidebar 
        @restart="updateParams"
        :batch="headers[0].value"
        :epoch="headers[1].value"
        :lrate="headers[2].value"
        :loss="headers[3].value"
      />
    </div>
    <div v-if="isHidden" class="grid items-center min-h-screen">
      <div class="flex flex-col justify-center items-center mt-20 mb-20">
        <h1 class="mx-auto font-extrabold text-4xl">Playground</h1>
        <h1 class="mx-auto mt-2 font-medium text-lg text-grey">Test the structure of your neural network</h1>
      </div>
      <model-build 
        :num_hidden="num_hidden"
        :layers="layers"
        :mappings="mappings"
        :width="width"
        :height="height"
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
      ]
    };
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
    close(){
      this.isHidden = !this.isHidden;
    },
    updateParams(data){
      for(var obj in data){
        this.headers = this.headers.map( d => {
          if(d.header == data[obj].title){
            return  { header: d.header , value: data[obj].value }
          }else{
            return d;
          }
        })
      }
    },
    updateModel(){
      //HTTP Request to Build and Run Model
      // {
      //    "data": Dataset
      //    "prob":"HRT", 
      //    "layers":[5,5], 
      //    "activations":["relu","relu"], 
      //    "lr":0.5, 
      //    "batch_size":10, 
      //    "epochs":10
      //    "train": 80
      // }

      //get modified-dataset from the localstorage
      // const JSON.parse(localStorage.getItem("base-dataset"));
      this.$http
      .post(
        `http://127.0.0.1:9090/api/model/run`,
        {
          "data": Dataset,
          "prob":"HRT", 
          "layers":[5,5], 
          "activations":["relu","relu"], 
          "lr":0.5, 
          "batch_size":10, 
          "epochs":10,
          "train": 80
        }
      )
      .then((response) => {
        const newData = response.data.dataset;
        const data = {
          headings: newData.columns,
          rows: newData.data,
          analysisType: this.analysisType,
          title: this.title,
          description: this.summary,
        };
        this.dataset = data;
        localStorage.setItem("base-dataset", JSON.stringify(data));
      });
    },
  },
  created(){
    this.num_hidden = this.$route.params.hidden || 1;
    this.layers = this.$route.params.struct ? JSON.parse(this.$route.params.struct) : [
        {
          id: 0,
          name: "input",
          nodes: [
            { id: 0, layer: 0 },
            { id: 1, layer: 0 },
          ],
        },
        {
          id: 1,
          name: "hidden-1",
          nodes: [
            { id: 0, layer: 1 },
          ],
        },
        {
          id: 2,
          name: "output",
          nodes: [{ id: 0, layer: 2, output: true }],
        },
      ];
    this.activation = this.$route.params.activation || ["ReLu"];
    this.headers = this.headers.map(d => {
      if(d.header == "Problem Type"){
        return {header: d.header, value: this.$route.params.problem || "Regression"};
      }else{
        return d;
      }
    });  
    this.createmapping();
  },
  mounted(){
    // this.buildModel();
    // this.runModel();
  }
};
</script>
