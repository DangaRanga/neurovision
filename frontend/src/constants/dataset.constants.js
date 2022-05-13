import {
  getHeartPredictionData,
  getHousePredictionData,
  getIrisPredictionData,
} from "@/controllers/dataControllers/dataset.controller";

import Heart from "@/assets/icons/heart.svg";
import Flower from "@/assets/icons/flower.svg";

const housePredictionData = {
  title: "House Price Prediction",
  description: ` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
      eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
      ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
      aliquip ex ea commodo consequat. Duis aute irure dolor in
      reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
      pariatur.`,
  summary: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
      eiusmod tempor incididunt ut labore`,
  problemType: "Prediction",
  image: "",
  name: "house_price",
};

const heartDiseaseData = {
  title: "Heart Disease",
  description: ` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
        ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur.`,
  summary: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore`,
  problemType: "Binary Classification",
  image: Heart,
  name: "heart_disease",
};

const irisPredictionData = {
  title: "Iris Prediction",
  description: ` Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
          ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur.`,
  summary: `Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore`,
  problemType: "Multivariate Classification",
  image: Flower,
  name: "iris",
  data: getIrisPredictionData(),
};

export { housePredictionData, irisPredictionData, heartDiseaseData };
