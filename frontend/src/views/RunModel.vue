<template>
  <div>
    <model-header />
    <div class="grid grid-cols-3 min-h-screen">
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
      <model-sidebar />
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
      layers: [
        {
          id: 0,
          name: "input",
          nodes: [
            { id: 0, layer: 0 },
            { id: 1, layer: 0 },
            { id: 2, layer: 0 },
          ],
        },
        {
          id: 1,
          name: "hidden-1",
          nodes: [
            { id: 0, layer: 1 },
            { id: 1, layer: 1 },
            { id: 2, layer: 1 },
            { id: 3, layer: 1 },
          ],
        },
        {
          id: 2,
          name: "hidden-2",
          nodes: [
            { id: 0, layer: 2 },
            { id: 1, layer: 2 },
            { id: 2, layer: 2 },
          ],
        },
        {
          id: 3,
          name: "output",
          nodes: [
            { id: 0, layer: 3 , output: true},
            { id: 1, layer: 3 , output: true},
            { id: 2, layer: 3 , output: true},
          ],
        },
      ],
      mappings: [],
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
  },
  mounted(){
    this.createmapping();
  },
};
</script>
