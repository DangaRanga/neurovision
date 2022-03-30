<template>
  <div
    class="pl-12 flex flex-col flex-wrap h-full md:items-center lg:items-start md:flex-row md:flex-nowrap"
  >
    <div
      class="flex-shrink-0 w-full md:w-2/3 mx-auto text-left md:mx-0 md:text-left pt-28"
    >
      <div
        class="bg-white rounded-sm outline outline-1 outline-grey_dark w-5/6 h-96 mx-auto"
      >
        Insert Dataset Info
      </div>
    </div>
    <sidebar class="w-1/3" />
  </div>
</template>
<script>
import DatasetSideBar from "@/components/elements/DatasetSideBar.vue";
export default {
  components: {
    "dataset-sidebar": DatasetSideBar,
  },
};
</script>
