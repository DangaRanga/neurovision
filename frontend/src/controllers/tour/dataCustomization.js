export const customizationTour = [
  {
    target: "#v-step-0", // We're using document.querySelector() under the hood
    content: ` <strong>Let's get to customizing our Dataset</strong>!
      Dataset customization involves 
      Dataset customization is important because..`,
    params: {
      placement: "left",
    },
  },
  {
    target: "#v-step-1",
    content: `There are several different types of problems that can be modeled using neural networks.
      These include: <strong>Binary Classification, Multivariate Classification, Prediction and Regression.<\strong>`,
    params: {
      placement: "left",
    },
  },
  {
    target: "#v-step-2",
    content: `<strong>Let us get some information on the Type of Analysis that the dataset is performing</strong>!`,
    params: {
      placement: "top",
    },
  },
  {
    target: "#v-step-3",
    content: `<strong>Let us get some information on the Training Data Percentage needed for this dataset</strong>!`,
    params: {
      placement: "top",
    },
  },
  {
    target: "#v-step-4",
    content: `<strong>Let us get some information on what Normalization is </strong>.`,
    params: {
      placement: "top",
    },
  },
  {
    target: "#v-step-5",
    content: `<strong>Hooray!, now that you've customized the dataset let's continue </strong>.`,
    params: {
      placement: "top",
    },
  },
];
