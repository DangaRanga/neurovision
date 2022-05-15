<template>
  <main class="bg-white py-8 px-10 w-full flex flex-col items-center h-screen">
    <h1 class="text-3xl font-bold mb-12" v-if="type == 'prequiz'">
      Test Your Existing Knowledge of Neural Networks
    </h1>
    <h1 class="text-3xl font-bold mb-12" v-if="type == 'postquiz'">
      Test Knowledge of Neural Networks Gained
    </h1>

    <section
      class="bg-primary p-4 max-w-2xl w-full flex flex-col rounded outline outline-2 outline-white"
      v-if="!quizCompleted"
    >
      <div class="flex flex-row justify-between mb-6">
        <span class="font-medium text-xl mr-2">{{
          getCurrentQuestion.question
        }}</span>
        <div
          class="bg-violet-400 ml-4 w-44 h-12 rounded outline outline-1 outline-white flex flex-col items-center justify-center text-base"
        >
          <span class="font-medium text-xl"
            >Score {{ score }}/{{ questions.length }}</span
          >
        </div>
      </div>

      <div class="mb-4">
        <label
          v-for="(option, index) in getCurrentQuestion.options"
          :key="index"
          :for="'option' + index"
          id="option"
          :class="`  bg-primary_light p-4 mb-4 block rounded outline outline-1 outline-white focus:outline-grey_light 
                    active:bg-grey_light hover:bg-grey_light h-16 text-base cursor-pointer${
                      getCurrentQuestion.selected == index
                        ? index == getCurrentQuestion.answer
                          ? 'correct'
                          : 'wrong'
                        : ''
                    } ${
            getCurrentQuestion.selected != null &&
            index != getCurrentQuestion.selected
              ? 'disabled'
              : ''
          }`"
        >
          <input
            type="radio"
            class="font-regular text-lg"
            :id="'option' + index"
            :name="getCurrentQuestion.index"
            :value="index"
            v-model="getCurrentQuestion.selected"
            :disabled="getCurrentQuestion.selected"
            @change="SetAnswer($event)"
          />
          <span>{{ option }}</span>
        </label>
      </div>

      <button
        @click="NextQuestion()"
        :disabled="!getCurrentQuestion.selected"
        class="justify-center w-3/5 mx-auto my-4 bg-primary_dark text-white text-lg font-medium uppercase rounded outline outline-1 outline-white appearance-none cursor-pointer p-4"
      >
        {{
          getCurrentQuestion.index == questions.length - 1
            ? "Finish"
            : getCurrentQuestion.selected == null
            ? "Select an option"
            : "Next question"
        }}
      </button>
    </section>

    <section
      v-else
      class="bg-primary p-4 max-w-2xl w-full flex flex-col rounded outline outline-2 outline-white"
    >
      <h2 class="text-2xl font-medium mb-2 justify-center mx-auto">
        You have finished the quiz!
      </h2>
      <p class="text-2xl font-medium mb-4 justify-center mx-auto">
        Your score is {{ score }}/{{ questions.length }}
      </p>
      <div v-if="type == 'prequiz'">
        <div class="mt-4">
          <p class="text-xl mx-auto text-center font-regular text-primary_dark">
            It is recommened that new users start with the tutorial!
          </p>
        </div>
        <div class="flex justify-center my-4">
          <router-link
            class="justify-center mx-2 my-4 bg-primary_dark text-white text-lg text-center font-medium uppercase outline outline-1 outline-white appearance-none cursor-pointer p-4 hover:bg-gray-500 rounded-md py-3 px-4 transition-colors duration-200"
            id="v-step-3"
            @click="showTour(false)"
            :to="{
              name: 'select',
            }"
          >
            Start Without Tutorial
          </router-link>
          <router-link
            class="justify-center mx-2 my-4 bg-primary_dark text-white text-lg text-center font-medium uppercase outline outline-1 outline-white appearance-none cursor-pointer p-4 hover:bg-gray-500 rounded-md py-3 px-4 transition-colors duration-200"
            id="v-step-3"
            @click="showTour(true)"
            :to="{
              name: 'select',
            }"
          >
            Start With Tutorial
          </router-link>
        </div>
      </div>
      <div v-if="type == 'postquiz'">
        <div class="flex justify-center m-0 mb-4">
          <button
            @click="showTour(true)"
            className="justify-center w-4/5 mx-2 my-4 bg-primary_dark text-white text-lg font-medium uppercase rounded outline outline-1 outline-white appearance-none cursor-pointer p-4"
          >
            Give Us Your Feedback
          </button>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
  props: { type: String, quizquestions: Array },
  data() {
    return {
      questions: this.quizquestions,
      quizCompleted: false,
      currentQuestion: 0,
    };
  },
  mounted() {
    this.questions = this.quizquestions;
  },
  computed: {
    score() {
      let value = 0;
      this.questions.map((q) => {
        if (q.selected != null && q.answer == q.selected) {
          console.log("correct");
          value++;
        }
      });
      return value;
    },

    getCurrentQuestion() {
      let question = this.questions[this.currentQuestion];
      question.index = this.currentQuestion;
      return question;
    },
  },
  methods: {
    SetAnswer(event) {
      this.questions[this.currentQuestion].selected = event.target.value;
      event.target.value = null;
    },

    NextQuestion() {
      if (this.currentQuestion < this.questions.length - 1) {
        this.currentQuestion++;
        return;
      }

      this.quizCompleted = true;
    },
    showTour(tour) {
      localStorage.setItem("isTourVisible", JSON.stringify(tour));
    },
  },
};
</script>

<style scoped>
#option.correct {
  background-color: #2cce7d;
}
#option.wrong {
  background-color: #ff5a5f;
}

input[type="radio"]:checked {
  background-color: #2cce7d;
}
</style>
