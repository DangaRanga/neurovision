<template>
  <section>
    <div class="flex justify-center items-center mb-5">
      <img @click="addLayer()" :src="add" alt="add" class="mr-1" />
      <img @click="subLayer()" :src="minus" alt="sub" class="mr-1" />
      <h2>{{ num }}</h2>
      <h2>Hidden Layers</h2>
    </div>
    <div class="flex justify-center items-center mb-5">
      <img @click="addNode(1)" :src="add" alt="add" class="mr-1" />
      <img @click="subNode(1)" :src="minus" alt="sub" class="mr-1" />
    </div>
    <div class="border-t-1 border-gray-light h-full"></div>
    <div id="chart5"></div>
  </section>
</template>

<script>
import * as d3 from "d3";
import add from "@/assets/icons/add.svg";
import minus from "@/assets/icons/minus.svg";

export default {
  name: "CModel",
  data() {
    return {
      width: 900,
      height: 500,
      margin: {
        left: 15,
        right: 15,
        top: 50,
        bottom: 50,
      },
      num: 1,
      add,
      minus,
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
            { id: 1, layer: 1 },
          ],
        },
        {
          id: 2,
          name: "output",
          nodes: [{ id: 0, layer: 2 }],
        },
      ],
    };
  },
  computed: {
    boundedWidth: function () {
      return this.width - this.margin.left - this.margin.right;
    },
    boundedHeight: function () {
      return this.height - this.margin.top - this.margin.bottom;
    },
  },
  methods: {
    addLayer() {
      if (this.num < 3) {
        this.num = this.num + 1;
      } else {
        return;
      }

      const input = this.layers[0];
      const output = this.layers[this.layers.length - 1];
      
      this.layers.splice(-1, 1);
      this.layers = [...this.layers, {
        id: this.layers.length,
        name: `hidden-${this.layers.length}`,
        nodes: [{ id: 0, layer: this.layers.length }],
      }];

      output.id = this.layers.length;
      for (var i = 0; i < output.nodes.length; i++)
        output.nodes[i].layer = this.layers.length;

      this.layers.push(output);
    },
    subLayer() {
      if (this.num > 1) {
        this.num = this.num - 1;
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
      if(layer.nodes.length < 5){
        layer.nodes.push({
          id: layer.nodes.length,
          layer: layer.id
        });
        this.createModel();
      }else{
        return ;
      }
    },
    subNode(index) {
      const layer = this.layers[index];
      if(layer.nodes.length > 1){
        layer.nodes.splice(-1, 1);
        this.createModel();
      }else{
        return ;
      }
    },
    createModel() {

      d3.select("#chart5").select("svg").remove();
      const svg = d3
        .select("#chart5")
        .append("svg")
        .attr("width", this.width) //TODO: responsive width
        .attr("height", this.height);

      const id = (d) => d.id;

      const l_scale = d3
        .scaleBand()
        .domain(this.layers.map(id))
        .range([0, this.width]);

      const c_scale = d3
        .scaleLinear()
        .domain([this.layers[0].id, this.layers[this.layers.length - 1].id])
        .range(["purple", "orange"]);

      const layers = svg
        .selectAll(".layer")
        .data(this.layers)
        .enter()
        .append("g")
        .attr("width", l_scale.bandwidth())
        .attr("height", this.height)
        .attr("fill", (d) => c_scale(d.id))
        .attr("x", (d) => l_scale(d.id));

      var y = d3.scaleLinear().rangeRound([0, this.height / 5]);
      var color = d3.scaleOrdinal(d3.schemeCategory10);
      
      const nodes = layers
        .selectAll("rect")
        .data((d) => d.nodes)
        .enter()
        .append("circle")
        .attr("id", (d) => d.id)
        .style("fill", function (d) {
          return color(d.id + 1);
        })
        .attr("r", 20)
        .attr("cy", function (d) {
          return y(d.id) + 50;
        })
        .attr("cx", (d) => l_scale(d.layer) + 50);

    },
  },
  mounted() {
    this.createModel();
  },
  updated() {
    this.createModel();
    console.log("updated");
  },
};
</script>

<style scoped>
.icon {
  width: 30px;
  margin-right: 5px;
}

h2 {
  margin: 0;
  margin-right: 10px;
}
</style>
