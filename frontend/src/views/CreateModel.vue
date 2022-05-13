<template>
  <div>
    <model-header />
    <div class="grid grid-cols-3 min-h-screen">
      <div class="col-span-2 grid items-center">
          <div>
            <div class="flex flex-col justify-center items-center mt-20 mb-20">
              <h1 class="mx-auto font-extrabold text-4xl">Build Your Neural Network</h1>
              <h1 class="mx-auto mt-2 font-semibold text-lg text-grey">Build the structure of your neural network</h1>
            </div>
            <model-build 
              :num_hidden="num_hidden"
              :layers="layers"
              :addNode="addNode"
              :subNode="subNode"
              :subLayer="subLayer"
              :addLayer="addLayer"
              :width="width"
              :height="height"
            /> 
          </div>
      </div>
      <model-sidebar 
        output="ReLu" 
        :layers="num_hidden"
      />
    </div>
  </div>
</template>

<script>
import CMHeader from "@/components/elements/CMHeader.vue";
import CMSidebar from "@/components/elements/CMSidebar.vue";
import CModel from "@/components/elements/CModel.vue";

export default {
  components: {
    "model-header": CMHeader,
    "model-sidebar": CMSidebar,
    "model-build": CModel,
  },
  data() {
    return {
      width: 800,
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
          nodes: [{ id: 0, layer: 2, output: true }],
        },
      ],
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
    },
    subLayer() {
      if (this.num_hidden > 1) {
        this.num_hidden = this.num_hidden - 1;
      } else {
        return;
      }

      const output = this.layers[this.layers.length - 1];

      this.layers.splice(-2, 2);
      output.id = this.layers.length;
      for (var i = 0; i < output.nodes.length; i++)
        output.nodes[i].layer = this.layers.length;
      this.layers.push(output);
    },
    addNode(index) {
      const layer = this.layers[index];
      if (layer.nodes.length < 4) {
        layer.nodes.push({
          id: layer.nodes.length,
          layer: layer.id,
        });
      } else {
        return;
      }
    },
    subNode(index) {
      const layer = this.layers[index];
      if (layer.nodes.length > 1) {
        layer.nodes.splice(-1, 1);
      } else {
        return;
      }
    },
  },
};
</script>
