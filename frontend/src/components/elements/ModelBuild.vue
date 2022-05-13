<template>
  <section>
    <div class="controls">
      <img @click="addLayer()" :src="add" alt="add" class="icon" />
      <img @click="subLayer()" :src="minus" alt="sub" class="icon" />
      <h2>{{ num }}</h2>
      <h2>Hidden Layers</h2>
    </div>
    <div id="chart5"></div>
    <div id="node" class="bg-primary"></div>
  </section>
</template>

<script>
import * as d3 from "d3";
import add from "@/assets/icons/add.svg";
import minus from "@/assets/icons/minus.svg";
//hi
export default {
  name: "ModelBuild",
  data() {
    return {
      width: 900,
      height: 500,
      margin: {
        left: 15,
        right: 15,
        top: 15,
        bottom: 15,
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
            { id: 2, layer: 0 },
            { id: 3, layer: 0 },
            { id: 4, layer: 0 },
          ],
        },
        {
          id: 1,
          name: "hidden-1",
          nodes: [{ id: 0, layer: 1 }],
        },
        {
          id: 2,
          name: "output",
          nodes: [{ id: 0, layer: 2 }],
        },
      ],
      nodes: [
        {
          id: 0,
          name: "ServiceGroup",
          description: "Port : 80",
          connection_count: 3,
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
      if (this.num < 5) {
        this.num = this.num + 1;
      } else {
        return;
      }

      const input = this.layers[0];
      const output = this.layers[this.layers.length - 1];

      this.layers = [];
      this.layers.push(input);
      for (var i = 0; i < this.num; i++)
        this.layers.push({
          id: i + 1,
          name: `hidden-${i + 1}`,
          nodes: [{ id: 0, layer: i + 1 }],
        });
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
    addNode() {
      return 0;
    },
    subNode() {
      return 0;
    },
    createModel() {
      d3.select("#chart5").select("svg").remove();
      const svg = d3
        .select("#chart5")
        .append("svg")
        .attr("width", this.width)
        .attr("height", this.height);

      const id = (d) => d.id;

      const l_scale = d3
        .scaleBand()
        .domain(this.layers.map(id))
        .range([0, this.width]);

      const nodes_scale = d3
        .scaleBand()
        .domain(this.layers.map(id))
        .range([0, this.height / 2]);

      const c_scale = d3
        .scaleLinear()
        .domain([this.layers[0].id, this.layers[this.layers.length - 1].id])
        .range(["purple", "orange"]);

      svg
        .selectAll(".text")
        .data(this.layers)
        .enter()
        .append("text")
        .attr("text-anchor", "middle")
        .attr("text-color", "#535353")
        .attr("class", "text-center font-medium text-primary_dark")
        .style("font-size", "28px")
        .style("color", "#535353")
        .text((d) => d.name)
        .attr("x", (d) => l_scale(d.id) + 100);

      const layers = svg
        .selectAll(".layer")
        .data(this.layers)
        .enter()
        .append("g")
        // .append("rect")
        .attr("width", l_scale.bandwidth())
        .attr("height", this.height)
        .attr("fill", (d) => c_scale(d.id))
        .attr("x", (d) => l_scale(d.id));

      var x = d3.scaleBand().rangeRound([0, this.width]).padding(0.3);
      var y = d3.scaleLinear().rangeRound([0, this.height / 5]);
      var colorRange = d3.schemeCategory10;
      var color = d3.scaleOrdinal(colorRange);
      const nodes = layers
        .selectAll("g")
        .data((d) => d.nodes)
        .enter()
        .append("circle")
        .attr("id", (d) => d.id)
        .style("fill", function (d) {
          return color(d.id + 1);
        })
        .attr("width", 50)
        .attr("height", 50)
        .attr("class", "bg-grey_light")
        .attr("r", 30)
        .attr("cy", function (d) {
          return y(d.id) + 50;
        })
        .attr("cx", (d) => l_scale(d.layer) + 50);

      const links = nodes
        .selectAll("circle")
        .data((d) => d.nodes)
        .enter()
        .append("line")
        .attr("class", "link")
        .attr("style", "stroke:black")
        .attr("x1", function (d) {
          return 50;
        }) //... (x coordinate source node)
        .attr("y1", function (d) {
          return y(d.id) + 50;
        }) //... (y coordinate source node)
        .attr("x2", function (d) {
          return 200;
        }) //... (x coordinate target node)
        .attr("y2", function (d) {
          return y(d.id + 1) + 50;
        }); //... (y coordinate target node)

      d3.select("#node").select("svg").remove();
      const svg2 = d3
        .select("#node")
        .append("svg")
        .attr("width", this.width)
        .attr("height", this.height);

      const circle = svg2
        .selectAll(".circle")
        .data(this.layers[1].nodes)
        .enter()
        .append("circle")
        .attr("id", (d) => d.id)
        .attr("width", 50)
        .attr("height", 50)
        .attr("class", "bg-grey")
        .attr("fill", "green")
        .attr("r", 30)
        .attr("cx", 70)
        .attr("cy", 90);

      const links = circle
        .selectAll("circle")
        .data(this.layers[1].nodes)
        .enter()
        .append("line")
        .attr("class", "link")
        .attr("style", "stroke:black");

      // svg2.merge(circle);
    },
  },
  mounted() {
    this.createModel();
  },
  updated() {
    this.createModel();
  },
};
</script>

<style scoped>
.controls {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.icon {
  width: 30px;
  margin-right: 5px;
}

h2 {
  margin: 0;
  margin-right: 10px;
}
</style>
