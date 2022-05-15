<template>
  <div class="h-20 flex items-center justify-between shadow-md">
    <div class="flex flex-row justify-between items-center">
      <img
        :src="neurovision_logo"
        alt="info"
        class="w-8 h-8 ml-4"
      />
      <span class="font-medium text-lg ml-2">NeuroVision</span>
    </div>
    <div class="flex flex-row justify-around items-center">
      <router-link
        class="w-1/3 text-center text-base font-medium m-5"
        :to="{
          name: 'landing',
        }"
      >
        Home
      </router-link>
      <router-link
        class="w-1/3 text-center text-base font-medium m-5"
        :to="{
          name: 'landing',
        }"
      >
        About
      </router-link>
    </div>
  </div>
</template>

<script>
import neurovision_logo from "@/assets/neurovision_logo.svg";

export default {
    name: "NavBar",
    data: function(){
      return {
        neurovision_logo,
      }
    }
}
</script>