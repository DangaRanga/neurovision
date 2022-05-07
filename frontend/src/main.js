import * as Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/tailwind.css";
import "../node_modules/shepherd.js/dist/css/shepherd.css";
import VueShepherd from "vue-shepherd";
import Popper from "popper.js";

const app = Vue.createApp(App);
app.popper = Popper;
app.use(router, VueShepherd);
app.mount("#app");
