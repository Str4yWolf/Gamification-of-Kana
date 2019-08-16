<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 800px; padding: 30px;">
      <!-- header -->
      <!-- back button -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideMultipleChoiceQuiz')" />
      &nbsp;
      <strong style="font-size: 120%;">Multiple Choice ({{numberQuestionsAnswered}}/{{quizLength}})</strong>
      &nbsp;
      &nbsp;
      &nbsp;
      &nbsp;
      <!-- manyougana highlight toggle -->
      <q-toggle
        v-model="highlightManyougana"
        color="red"
        label="Highlight Manyougana"
        @input="$refs.InterfaceMCQ.updateHighlight()"
      />
      <!-- parameters panel -->
      <span class="row">
        <!-- script selection -->
        <span>
          <q-select v-model="script1" :options="['katakana', 'manyougana-katakana']" label="Script1" style="width:200px;" />
        </span>
        <span>
          <q-select v-model="script2" :options="['katakana', 'manyougana-katakana']" label="Script2" style="width:200px;" />
        </span>
        <!-- number of questions slider -->
        <span style="padding:10px;" v-if="!quizHasStarted">
          <strong>Questions: </strong>
        </span>
        <span v-if="!quizHasStarted">
          <q-slider
            v-model="quizLength"
            :min="3"
            :max="20"
            :step="1"
            label-always
            color="light-green"
            style="width: 120px;"
          />
        </span>
        <!-- context dependent buttons -->
        <span style="padding-left:10px; position: absolute; left: 640px;">
          <q-btn v-if="!quizHasStarted" color="green" label="Start" @click="startQuiz()" />
          <q-btn v-if="quizHasStarted" color="green" label="Enter" @click="$refs.InterfaceMCQ.continueQuiz()" :disabled="!validationInProgress" />
        </span>
      </span>
      <multiple-choice-quiz :userObj="userObj" :script1="script1" :script2="script2" :highlightManyougana="highlightManyougana" :quizLength="quizLength" ref="InterfaceMCQ" />
    </q-card>
  </q-page>
</template>

<script>
import MultipleChoiceQuiz from '../components/MultipleChoiceQuiz.vue'

export default {
  // name: 'PageName',
  components: {
    MultipleChoiceQuiz
  },
  data () {
    return {
      // Boolean process and button display controllors
      quizHasStarted: false,
      hasAnsweredQuestion: false,
      validationInProgress: false,
      highlightManyougana: false,
      // script-related
      script1: 'katakana',
      script2: 'manyougana-katakana',
      // quiz controllers
      quizLength: 3,
      numberQuestionsAnswered: 0,
      questionsAnsweredCorrectly: 0
    }
  },
  props: {
    userObj: Object
  },
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('setNumberQuestionsAnswered', this.setNumberQuestionsAnswered)
    this.$root.$on('setQuizHasStarted', this.setQuizHasStarted)
    this.$root.$on('setValidationInProgress', this.setValidationInProgress)
  },
  mounted () {
    this.$refs.modal.$el.focus()
  },
  methods: {
    /**
    Validate user keyboard input
    **/
    validateKeyInput (event) {
      switch (event.keyCode) {
        // keyboard numbers 1 - 4
        case 49:
        case 50:
        case 51:
        case 52:
          if (!this.validationInProgress && this.quizHasStarted) {
            console.log('called validateKeyInput with 1-4')
            this.$refs.InterfaceMCQ.validateOption(event.keyCode - 48)
          } else {
            console.log('Validation is in progress. Options unusable.')
          }
          break
        // keyboard Enter key
        case 13:
          console.log('pressed enter in validateKeyInput')
          if (this.validationInProgress) {
            this.$refs.InterfaceMCQ.continueQuiz()
          }
          break
        // log all other keys
        default:
          console.log('called validateKeyInput with key')
          console.log(event.key)
          console.log('and keyCode')
          console.log(event.keyCode)
      }
    },
    startQuiz () {
      this.numberQuestionsAnswered = 0
      this.$refs.InterfaceMCQ.continueQuiz()
    },
    /**
    End quiz by intializing quiz controls and displaying feedback to user
    **/
    endQuiz () {
      console.log('called endQuiz from MultipleChoice')
      this.quizHasStarted = false
      this.validationInProgress = false
      this.feedbackMessage = 'Congratulations. You have scored ' + this.questionsAnsweredCorrectly + ' out of ' + this.numberQuestionsAnswered + ' in this quiz!'
      this.questionsAnsweredCorrectly = 0
      this.numberQuestionsAnswered = 0
    },
    setNumberQuestionsAnswered (x) {
      this.numberQuestionsAnswered = x
    },
    setQuizHasStarted (x) {
      this.quizHasStarted = x
    },
    setValidationInProgress (x) {
      this.validationInProgress = x
    }
  }
}
</script>

<style>
</style>
