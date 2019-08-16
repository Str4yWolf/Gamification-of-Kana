<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 820px; padding: 30px;">
      <!-- header -->
      <!-- back button -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideGeneralLearning')" />
      &nbsp;
      <strong style="font-size: 120%;">Learn</strong>
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
        <!-- context dependent buttons -->
        <span style="padding-left:10px; position: absolute; left: 640px; top: 33px;">
          <q-btn color="green" label="Continue" @click="randomizeNextQuestion()" :disabled="!validationInProgress" />
        </span>
      </span>
      <multiple-choice-quiz v-if="showMCQ" :userObj="userObj" :script1="script1" :script2="script2" :highlightManyougana="highlightManyougana" :quizLength="quizLength" ref="GeneralLearningMCQ" />
      <word-creator v-if="showWC" :userObj="userObj" :script="script1" ref="GeneralLearningWC" />
    </q-card>
  </q-page>
</template>

<script>
import MultipleChoiceQuiz from '../components/MultipleChoiceQuiz.vue'
import WordCreator from '../components/WordCreator.vue'

export default {
  // name: 'PageName',
  components: {
    MultipleChoiceQuiz,
    WordCreator
  },
  data () {
    return {
      // Boolean process and button display controllors
      hasAnsweredQuestion: false,
      validationInProgress: true,
      highlightManyougana: false,
      // script-related
      script1: 'katakana',
      scripts: ['katakana', 'manyougana-katakana'],
      // quiz controllers
      mode: 0,
      disableOptions: false
    }
  },
  computed: {
    script2 () {
      if (this.script1 === 'katakana') {
        return 'manyougana-katakana'
      } else {
        return 'katakana'
      }
    },
    showMCQ () {
      return this.mode === 0
    },
    showWC () {
      return this.mode === 1
    }
  },
  props: {
    userObj: Object
  },
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('MultipleChoiceQuestion answered', this.randomizeNextQuestion())
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
    setValidationInProgress (x) {
      this.validationInProgress = x
    },
    randomizeNextQuestion () {
      this.mode = Math.floor(Math.random() * 2)
      this.script1 = this.scripts[Math.floor(Math.random() * 2)]
      switch (this.mode) {
        // Multiple choice
        case 0:
          this.$refs.GeneralLearningMCQ.continueQuiz()
          break
        case 1:
        // Word creator
          this.disableOptions = false
          this.$refs.GeneralLearningWC.setNewCreation()
          break
      }
    }
  }
}
</script>

<style>
</style>
