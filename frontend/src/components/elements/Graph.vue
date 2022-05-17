<template>
  <section class="w-2/3 h-56 bg-grey_dark mb-10 mx-auto">
      Hey
  </section>
</template>

<script>
export default {
    name: "Graph",
    props: ["values", "width", "height"],
    data(){
        return {
            margin: {
                top: 10,
                bottom: 10,
                left: 10,
                right: 10,
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
    methods: {
        createGraph(){
            // const svg = d3.create("svg")
            //     .attr("width", width)
            //     .attr("height", height)
            //     .attr("viewBox", [0, 0, width, height])
            //     .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

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