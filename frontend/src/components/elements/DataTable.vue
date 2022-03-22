<template>
  <div class="shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left">
      <thead class="text-xs text-gray-700 uppercase bg-gray-100">
        <tr>
          <th
            v-for="(heading, index) in headings"
            class="px-6 py-3"
            :key="index"
          >
            {{ heading }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b odd:bg-white even:bg-gray-50">
          <th
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
          >
            Apple MacBook Pro 17"
          </th>
          <td class="px-6 py-4">Sliver</td>
          <td class="px-6 py-4">Laptop</td>
          <td class="px-6 py-4">$2999</td>
        </tr>
        <tr class="border-b odd:bg-white even:bg-gray-50">
          <th
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
          >
            Apple MacBook Pro 17"
          </th>
          <td class="px-6 py-4">Sliver</td>
          <td class="px-6 py-4">Laptop</td>
          <td class="px-6 py-4">$2999</td>
        </tr>
        <tr class="border-b odd:bg-white even:bg-gray-50">
          <th
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
          >
            Apple MacBook Pro 17"
          </th>
          <td class="px-6 py-4">Sliver</td>
          <td class="px-6 py-4">Laptop</td>
          <td class="px-6 py-4">$2999</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import { toRefs } from "vue";

export default {
  props: {
    rows: [Object],
    headings: [String],
  },

  setup(props) {
    const { headings, rows } = toRefs(props);
  },
};
</script>
