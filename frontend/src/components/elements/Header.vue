<template>
  <div>
    <div v-if="isRunning" class="flex flex-row-reverse bg-grey_dark h-18 py-4 px-2 drop-shadow-lg"> 
      <button
          class="text-white bg-primary hover:bg-blue-500 rounded-md py-2 px-4 mx-3 transition-colors duration-200"
        >
          Preview Dataset
        </button>
    </div>
    <div v-if="!isRunning" class="flex bg-grey_dark h-18 py-4 px-2 drop-shadow-lg"> 
      <div class="text-white bg-primary hover:bg-blue-500 rounded-full h-10 w-10 p-0.5 ml-2 transition-colors duration-200">
        <svg 
          xmlns="http://www.w3.org/2000/svg" 
          height="35px" 
          viewBox="0 0 24 24" 
          width="35px" 
          fill="#FFFFFF"
        >
          <path d="M0 0h24v24H0z" fill="none"/>
          <path d="M8 5v14l11-7z"/>
        </svg>
      </div>
      <div class="text-white rounded-full h-10 w-10 p-2 transition-colors duration-200">
        <svg 
        xmlns="http://www.w3.org/2000/svg" 
        height="24px" 
        viewBox="0 0 24 24" 
        width="24px" 
        fill="#FFFFFF"
        >
          <path d="M0 0h24v24H0z" fill="none"/>
          <path d="M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z"/>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data(){
    return {
      isRunning: false,
    }
  }

}
</script>