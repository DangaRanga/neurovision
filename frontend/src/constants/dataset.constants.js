import {
  getHeartPredictionData,
  getHousePredictionData,
  getIrisPredictionData,
} from "@/controllers/dataControllers/dataset.controller";

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
  problemType: "Regression",
  image: "",
  data: getHousePredictionData(),
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
  image: "",
  data: getHeartPredictionData(),
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
  problemType: "Multi Classification",
  image: "",
  data: getIrisPredictionData(),
};

export { housePredictionData, irisPredictionData, heartDiseaseData };
