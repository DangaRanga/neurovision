<template>
  <section>
    <div id="chart5" class="flex justify-center items-center mb-5"></div>
  </section>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "CModel",
  props: [
    "num_hidden",
    "layers",
    "mappings",
    "width",
    "height",
    "epochs",
    "isRunning",
    "toggleRunning"
  ],
  data() {
    return {};
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

      const layers = svg
        .selectAll(".layer")
        .data(this.layers)
        .enter()
        .append("g")
        .style("transform", `translate(${80}px, ${0}px)`);

      var y = d3.scaleLinear().rangeRound([0, this.height / 5]);

      const nodes = layers
        .selectAll("rect")
        .data((d) => d.nodes)
        .enter()
        .append("circle")
        .attr("id", (d) => d.id)
        .style("fill", function (d) {
          if (d.layer == 0) {
            return "#20A4F3";
          } else if (d.output) {
            return "#20A4F3";
          } else {
            return "#5D5FEF";
          }
        })
        .attr("r", 20)
        .attr("cy", function (d) {
          return y(d.id) + 50;
        })
        .attr("cx", (d) => l_scale(d.layer) + 50);

      const len = 3;
      const links = nodes
        .select("circle")
        .data(this.mappings)
        .enter()
        .append("line")
        .style("stroke", "grey")
        .style("stroke-width", 3)
        .attr("x1", (d) => d.sourcex)
        .attr("y1", (d) => d.sourcey)
        .attr("x2", (d) => d.targetx)
        .attr("y2", (d) => d.targety);

      const update = () => {
        this.toggleRunning();
      };

      function forward(epoch) {

        links
          .style("stroke", "green")
          .style("stroke-width", 5)
          .attr("stroke-dasharray", 10 + " " + 10)
          .attr("stroke-dashoffset", 250)
          .interrupt()
          .transition()
          .style("stroke", "green")
          .duration(700)
          .ease(d3.easeQuadIn)
          .attr("stroke-dashoffset", 100)
          .on("end", (event) => {
            if (epoch > 1) {
              // console.log(event);
              backward(epoch);
            }else {
              update();
            }
          });
      }

      function backward(epoch) {
        links
          .transition()
          .style("stroke", "green")
          .duration(100)
          .ease(d3.easeLinear)
          .attr("stroke-dashoffset", 250)
          .style("stroke", "green")
          .on("end", forward(epoch - 1));
      }

      const epochs = this.epochs;
      if (this.isRunning) {
        forward(epochs);
      }
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
.icon {
  width: 30px;
  margin-right: 5px;
}

h2 {
  margin: 0;
  margin-right: 10px;
}
</style>
