<template>
  <div>
    <model-header />
    <div class="grid grid-cols-3 min-h-screen">
      <div class="col-span-2 grid items-center">
        <div class="mx-auto mt-10 mb-10 flex flex-col align-center">
          <h1 class="font-extrabold text-4xl">Build Your Neural Network</h1>
          <h1 class="mx-auto mt-2 font-semibold text-lg text-grey">Build the structure of your neural network</h1>
        </div>
        <model-build 
          :num_hidden="num_hidden"
          :layers="layers"
          :mappings="mappings"
          :addNode="addNode"
          :subNode="subNode"
          :subLayer="subLayer"
          :addLayer="addLayer"
          :width="width"
          :height="height"
        />
      </div>
      <model-sidebar />
    </div>
  </div>
</template>

<script>
import RMHeader from "@/components/elements/RMHeader.vue";
import RMSidebar from "@/components/elements/RMSidebar.vue";
import RModel from "@/components/elements/RModel.vue";

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
          nodes: [{ id: 0, layer: 2 , output: true}],
        },
      ],
      mappings: [],
    };
  },
  methods: {
    addLayer() {
      if (this.num_hidden < 3) {
        this.num_hidden = this.num_hidden + 1;
      } else {
        return;
      }

      const input = this.layers[0];
      const output = this.layers[this.layers.length - 1];

      this.layers.splice(-1, 1);
      this.layers = [
        ...this.layers,
        {
          id: this.layers.length,
          name: `hidden-${this.layers.length}`,
          nodes: [{ id: 0, layer: this.layers.length }],
        },
      ];

      output.id = this.layers.length;
      for (var i = 0; i < output.nodes.length; i++)
        output.nodes[i].layer = this.layers.length;

      this.layers.push(output);
      this.createmapping();
    },
    subLayer() {
      if (this.num_hidden > 1) {
        this.num_hidden = this.num_hidden - 1;
      } else {
        return;
      }

      const output = this.layers[this.layers.length - 1];
      let deleteLayer = this.layers[this.layers.length - 2];
      console.log(deleteLayer);
      this.deleteLayerMapping(deleteLayer.id);

      this.layers.splice(-2, 2);
      output.id = this.layers.length;
      for (var i = 0; i < output.nodes.length; i++)
        output.nodes[i].layer = this.layers.length;
      this.layers.push(output);
      this.createmapping();
    },
    addNode(index) {
      const layer = this.layers[index];
      if (layer.nodes.length < 5) {
        layer.nodes.push({
          id: layer.nodes.length,
          layer: layer.id,
        });
        this.createmapping();
      } else {
        return;
      }
    },
    subNode(index) {
      const layer = this.layers[index];
      if (layer.nodes.length > 1) {
        let deletenode = layer.nodes[layer.nodes.length - 1];
        this.deleteNodeMapping(deletenode.layer, deletenode.id);

        layer.nodes.splice(-1, 1);
      } else {
        return;
      }
    },
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
      console.log(this.mappings)
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
