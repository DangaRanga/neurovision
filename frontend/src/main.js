import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/tailwind.css";
import VModal from "vue-js-modal";

createApp(App).use(router, VModal).mount("#app");
