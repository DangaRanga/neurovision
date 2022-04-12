import { createRouter, createWebHistory } from "vue-router";
import DatasetSelection from "../views/DatasetSelection.vue";
import CustomizeDataset from "../views/CustomizeDataset.vue";
import Tour from "@/views/Tour.vue";

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
  {
    path: "/tour",
    name: "tour",
    component: Tour,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
