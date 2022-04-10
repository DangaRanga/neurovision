import { createRouter, createWebHistory } from "vue-router";
import DatasetSelection from "../views/DatasetSelection.vue";
import CustomizeDataset from "../views/CustomizeDataset.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: DatasetSelection,
  },
  {
    path: "/dataset",
    name: "dataset",
    component: CustomizeDataset,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
