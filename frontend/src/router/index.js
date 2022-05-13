import { createRouter, createWebHistory } from "vue-router";
import DatasetSelection from "../views/DatasetSelection.vue";
import CustomizeDataset from "../views/CustomizeDataset.vue";
import CreateModel from "../views/CreateModel.vue";
import RunModel from "../views/RunModel.vue";
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
    path: "/create",
    name: "create",
    component: CreateModel,
  },
  {
    path: "/run",
    name: "run",
    component: RunModel,
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
