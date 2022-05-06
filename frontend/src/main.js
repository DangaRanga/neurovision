import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/tailwind.css";
import VueAxios from "vue-axios";
import axios from "axios";

const neuroVisionApp = createApp(App);

// Set up Vue Axios
axios.defaults.baseURL = process.env.NEUROVISION_API_URL;
neuroVisionApp.use(VueAxios, axios);

// Set up other plugins
neuroVisionApp.use(router);
//require("vue-tour/dist/vue-tour.css");
//neuroVisionApp.use(VueTour);

neuroVisionApp.mount("#app");
