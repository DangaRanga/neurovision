<template>
  <div>
      <div v-if="type == 'select'">
          <p class="text-s font-semibold py-2">{{ title }}</p>
          <select
            class="bg-white rounded-sm outline outline-1 outline-white h-8 text-s"
          >
            <option v-for="(item, i ) in options" :key=i :value=item.value > {{ item.header }}</option>
          </select>
      </div>
      <div v-if="type == 'input'">
          <p class="text-s font-semibold py-2">{{ title }}</p>
          <input
            class="bg-white rounded-sm outline outline-1 outline-white h-8 text-s"
            value=""
          />
      </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            type: "select",
            options: [
                { title: "Binary Classification", value: "BC"},
                { title: "Multiple Classification", value: "MC"},
                { title: "Regression", value: "RG"},
            ],
            title: "Type of Analysis"
        }
    }
}
</script>