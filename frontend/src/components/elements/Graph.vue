<template>
  <section :id="'section-'+ index" class="mb-10 mx-auto flex flex-col">
    <span class="mb-2 text-lg font-bold">{{ values.title }}</span>
  </section>
</template>

<script>
import * as d3 from "d3";

export default {
    name: "Graph",
    props: ["values", "width", "height", "isRunning", "index"],
    data(){
        return {
            margin: {
                top: 20,
                bottom: 40,
                left: 55,
                right: 20,
            }
        }
    },
    computed: {
        boundedHeight: function () {
            return this.height - this.margin.top - this.margin.bottom
        },
        boundedWidth: function () {
            return this.width - this.margin.left - this.margin.right;
        }
    },
    mounted(){
        this.createGraph();
    },
    updated(){
        this.createGraph();
    },
    methods: {
        createGraph(){
            d3.select(`#section-${this.index}`).select("svg").remove();
            const dataset = this.values.data;

            const svg = d3.select(`#section-${this.index}`).append("svg")
                .attr("width", this.width)
                .attr("height", this.height);
            
            svg.append("rect").attr("width", this.width).attr("height", this.height).attr("fill", "white");

            const bound = svg.append("g").style("transform", `translate(${this.margin.left}px, ${this.margin.top}px)`);

            const xAccessor = d => d.epoch;
            const yAccessor = this.index == 0 ? d => d.acc : d => d.loss;

            const xScale = d3.scaleLinear().domain(d3.extent(dataset, xAccessor)).range([0, this.boundedWidth]);
            const yScale = d3.scaleLinear().domain([0, d3.max(dataset, yAccessor)]).range([this.boundedHeight, 0]);

            const lineGenerator = d3.line().x(d => xScale(xAccessor(d))).y(d => yScale(yAccessor(d)));

            const line = bound.append("path")
                .attr("d", lineGenerator(dataset))
                .attr("fill", "none")
                .attr("stroke", "#20A4F3")
                .attr("stroke-width", 2);
            
            const xAxisG = d3.axisBottom().scale(xScale).ticks(5);
            const yAxisG = d3.axisLeft().scale(yScale).ticks(5);

            const xAxis = bound.append("g").call(xAxisG)
                .style("transform", `translateY(${this.boundedHeight}px)`);;
            const yAxis = bound.append("g").call(yAxisG);

            const xAxisLabel = xAxis.append("text")
                                    .attr("x", this.boundedWidth / 2)
                                    .attr("y", this.margin.bottom - 10 )
                                    .attr("fill", "black")
                                    .style("font-size", "1em")
                                    .html("Epochs");

            const label = this.index == 0 ? "Accuracy (%)" : "Loss (%)";
            const yAxisLabel = yAxis.append("text")
                                    .attr("x", -this.boundedHeight / 2)
                                    .attr("y", -this.margin.left + 15 )
                                    .attr("fill", "black")
                                    .style("font-size", "1em")
                                    .style("transform", "rotate(-90deg)")
                                    .style("text-anchor", "middle")
                                    .html(label);

            

            // const xAxis = d3.axisBottom().scale
                // .attr("viewBox", [0, 0, width, height])
                // .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

            // const zx = x.copy(); // x, but with a new domain.

            // const line = d3.line()
            //     .x(d => zx(d.date))
            //     .y(d => y(d.close));

            // const path = svg.append("path")
            //     .attr("fill", "none")
            //     .attr("stroke", "steelblue")
            //     .attr("stroke-width", 1.5)
            //     .attr("stroke-miterlimit", 1)
            //     .attr("d", line(data));

            // const gx = svg.append("g")
            //     .call(xAxis, zx);

            // const gy = svg.append("g")
            //     .call(yAxis, y);

            // return Object.assign(svg.node(), {
            //     update(domain) {
            //     const t = svg.transition().duration(750);
            //     zx.domain(domain);
            //     gx.transition(t).call(xAxis, zx);
            //     path.transition(t).attr("d", line(data));
            //     }
            // });
        }
    }
}
</script>