<template>
  <div class="mb-10">
      <div v-if="type == 'select'">
          <p class="text-s font-semibold my-4">{{ title }}</p>
          <select
            class="bg-white rounded-sm outline outline-1 outline-white focus:outline-primary h-12 pl-2 text-base w-full"
            @change="changeValue($event)"
          >
            <option v-for="(item, i ) in options" :key=i :value=item.value > {{ item.title }}</option>
          </select>
      </div>
      <div v-if="type == 'input'">
          <div
            class="flex flex-row justify-between mb-3"
          >
            <p class="text-base font-semibold">{{ title }}</p>
            <img
              :src="infographics_icon"
              alt="info"
              class="items-center"
            />
          </div>
          <input
            class="bg-white rounded outline outline-1 outline-white focus:outline-primary h-12 text-base w-full p-2"
            value=""
            placeholder="Enter text"
          />
      </div>
      <div v-if="type == 'input-d'">
          <div
            class="flex flex-row justify-between mb-3"
          >
            <p class="text-base font-semibold">{{ title }}</p>
            <img
              :src="infographics_icon"
              alt="info"
              class="items-center"
            />
          </div>
          <input
            class="bg-white rounded outline outline-1 outline-white focus:outline-primary h-12 text-base w-full p-2"
            :value=value
            disabled
          />
      </div>
  </div>
</template>

<script>
import infographics_icon from "@/assets/icons/infographics_icon.svg";

export default {
    props : ["type", "options", "title", "value", "change", "index"],
    data(){
        return {
            infographics_icon: infographics_icon,
        }
    },
    methods: {
      changeValue(event){
        const value = event.target.value;
        if(value == "sigm"){
          this.change(this.index, "Sigmoid");
        }else if(value == "smax"){
          this.change(this.index, "Softmax");
        }else{
          this.change(this.index, "ReLu");
        }
      }
    }
}
</script>