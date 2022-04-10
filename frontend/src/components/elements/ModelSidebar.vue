<template>
  <aside>
    <div v-if="!isRunning" class="bg-primary_light py-8 px-10 w-full h-full flex flex-col justify-between">
      <div class="mb-8">
        <div class="mb-10">
          <h3 class="text-2xl font-bold m-0">Activation Functions</h3>
          <p class="text-sm font-regular mt-4">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Dictum enim
            pellentesque auctor ipsum integer feugiat risus nulla sed
          </p>
        </div>
        <div>
          <sidebar-input 
            type="select"
            :title=title
            :options=options 
          />
        </div>
      </div>
      <div class="flex flex-col justify-center">
        <div
            class="flex justify-center m-0 mb-4"
          >
            <button
              className="w-2/5 bg-grey_dark text-white font-bold py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-2"
              type="button"
            >
              Previous Step
            </button>
            <button
              className="w-1/3 bg-primary text-white font-semibold py-3 rounded shadow hover:shadow-md outline outline-1"
              type="button"
            >
              Next Step
            </button>
            
          </div>
        <p class="px-4 mx-auto font-thin text-sm">Step 2 of 5</p>
      </div>  
    </div>
    <div v-if="isRunning" class="bg-primary_light py-8 px-10 w-full h-full flex flex-col justify-between">
      <div class="mb-8">
        <div class="mb-10">
          Tabbed Menu
        </div>
        <div>
          <sidebar-input 
            v-for="(header, i) in headers"
            :key=i
            type="input"
            :title=header 
          />
        </div>
      </div>
      <div class="flex flex-col justify-center">
        <div
            class="flex justify-center m-0 mb-4"
          >
            <button
              className="w-3/5 bg-primary text-white font-bold py-3 rounded shadow hover:shadow-md outline-none focus:outline-none mr-2"
              type="button"
            >
              Restart Simulation
            </button>            
          </div>
      </div>  
    </div>
  </aside>
</template>

<script>
import SidebarInput from "@/components/elements/SidebarInput.vue";

export default {
  props: ['isRunning'],
  components: {
    "sidebar-input": SidebarInput,
  },
  data(){
    return {
      options: [
        { title: "ReLu", value: "relu"},
        { title: "Sigmoid", value: "sigm"},
        { title: "Softmax", value: "smax"},
      ],
      title: "Activation Function",
      headers: ["Batch Size", "Epochs", "Learning Rate", "Loss Function", "Optimization Algorithm"]
    }
  }
};
</script>
