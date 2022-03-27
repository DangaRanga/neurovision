import { createRouter, createWebHashHistory, createWebHistory } from "vue-router";
import DatasetSelection from "../views/DatasetSelection.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: DatasetSelection,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
