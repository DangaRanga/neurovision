import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/tailwind.css";
import VueShepherd from "vue-shepherd";

createApp(App).use(router, VueShepherd).mount("#app");
