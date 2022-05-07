import * as Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/tailwind.css";
import VueAxios from "vue-axios";
import axios from "axios";

// import "../node_modules/shepherd.js/dist/css/shepherd.css";
// import VueShepherd from "vue-shepherd";
// import Popper from "popper.js";

const neuroVisionApp = createApp(App);

// Set up Vue Axios
axios.defaults.baseURL = process.env.NEUROVISION_API_URL;
neuroVisionApp.use(VueAxios, axios);

// Set up other plugins
neuroVisionApp.use(router);
//require("vue-tour/dist/vue-tour.css");
//neuroVisionApp.use(VueTour);

neuroVisionApp.mount("#app");
