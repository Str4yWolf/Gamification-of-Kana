<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 800px; height: 540px; padding: 30px;">
      <!-- header -->
      <!-- back button -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideMultipleChoiceQuiz')" />
      &nbsp;
      <strong style="font-size: 120%;">Multiple Choice</strong>
      &nbsp;
      &nbsp;
      <!-- manyougana highlight toggle -->
      <q-toggle
        v-if="showHighlightManyougana"
        v-model="highlightManyougana"
        color="red"
        label="Highlight Manyougana"
        @input="updateHighlight()"
      />
      <!-- customization panel  -->
      <q-expansion-item
        style="position: absolute; top: 30px; right: 150px;"
        expand-separator
        icon="settings"
        label="Customize"
        v-model="showOptions"
        >
        <!-- script selection -->
        <span style="position: absolute; top: 0px; right: 110px;">
          <q-select v-model="script1" :options="[userObj.currentMapping[0], userObj.currentMapping[1]]" label="Script1" style="width:200px;" @input="updateScriptSelection1()" />
        </span>
        <span style="position: absolute; top: 0px; right: -100px;">
          <q-select v-model="script2" :options="[userObj.currentMapping[0], userObj.currentMapping[1]]" label="Script2" style="width:200px;" @input="updateScriptSelection2()" />
        </span>
    </q-expansion-item>
      <!-- context dependent buttons -->
      <span style="padding-left:10px; position: absolute; top: 40px; right: 50px;">
        <q-btn v-if="!quizHasStarted" color="green" label="Start" @click="startQuiz()" />
        <q-btn v-if="quizHasStarted" color="green" label="Enter" @click="$refs.InterfaceMCQ.continueQuiz()" :disabled="!validationInProgress" />
      </span>
      <br/>
      <br/>
      <br/>
      <multiple-choice-quiz :userObj="userObj" :script1="script1" :script2="script2" :highlightManyougana="highlightManyougana" :quizLength="1000000" :singleQuestion="true" ref="InterfaceMCQ" />
      <q-dialog v-model="viewTutorial">
        <q-card style="padding: 10px;">
          <strong>Tip: </strong>Use keyboard shortcuts <strong style="color: blue;">1 - 4 </strong> for Options and <strong style="color: blue;">Enter </strong> for ENTER.
        </q-card>
      </q-dialog>
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
      script1: this.userObj.currentMapping[0],
      script2: this.userObj.currentMapping[1],
      // quiz controllers
      quizLength: 3,
      numberQuestionsAnswered: 0,
      questionsAnsweredCorrectly: 0,
      //
      viewTutorial: false
    }
  },
  props: {
    userObj: Object
  },
  computed: {
    showHighlightManyougana () {
      var s1 = this.userObj.currentMapping[0].split('-')[0]
      var s2 = this.userObj.currentMapping[1].split('-')[0]
      if (s1 === 'manyougana' || s2 === 'manyougana') {
        return true
      } else {
        return false
      }
    }
  },
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('setNumberQuestionsAnswered', this.setNumberQuestionsAnswered)
    this.$root.$on('setQuizHasStarted', this.setQuizHasStarted)
    this.$root.$on('setValidationInProgress', this.setValidationInProgress)
  },
  mounted () {
    this.$refs.modal.$el.focus()
    if (this.userObj.viewedTutorial[2] === false) {
      this.userObj.viewedTutorial[2] = true
      this.viewTutorial = true
      this.$root.$emit('updateDatabase')
    }
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
      if (this.script1 === this.script2) {
        this.$q.notify('Cannot use the same script twice.')
      } else {
        this.numberQuestionsAnswered = 0
        this.$refs.InterfaceMCQ.continueQuiz()
      }
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
    },
    updateHighlight () {
      setTimeout(this.$refs.InterfaceMCQ.updateHighlight, 1)
    },
    // make sure scripts are never the same
    updateScriptSelection1 () {
      if (this.script1 === this.userObj.currentMapping[0]) {
        this.script2 = this.userObj.currentMapping[1]
      } else {
        this.script2 = this.userObj.currentMapping[0]
      }
    },
    updateScriptSelection2 () {
      if (this.script2 === this.userObj.currentMapping[0]) {
        this.script1 = this.userObj.currentMapping[1]
      } else {
        this.script1 = this.userObj.currentMapping[0]
      }
    }
  }
}
/**
<q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
<q-dialog v-model="viewTutorial">
  <q-card style="width: 600px;">
    <q-card-section>
      <div class="text-h6">Tutorial (Multiple Choice Quiz)</div>
    </q-card-section>
    <q-card-section>
    Use <strong>Multiple Choice Quiz</strong> to practice recognizing a Japanese letter in a target script.
    <br/>
    <br/>
    Start your game by choosing a source script <strong>Script1</strong> for your question image and a target script <strong>Script2</strong> for your (4) answer images. Adjust the number of questions of your game using the <strong>Slider</strong>. HIt the <strong>Start</strong> button to begin.
    <br/><br/>
    A random letter of Script1 will be displayed. Choose the corresponding equivalent of Script2 by selecting from the <strong>Option</strong> buttons below or type in one of <strong>1, 2, 3, 4</strong> on your keyboard (not the keys of a NumPad).
    <br/><br/>
    When your answer is correct, the next question will be shown. Otherwise, you will be given corrective feedback and shown the <strong><abbr title="One Latin Romanization of Japanese">Romaji</abbr></strong> of each character. Press the <strong>ENTER</strong> button or <strong>Enter</strong> on your keyboard to proceed.
    <br/><br/>
    Once all questions have been answered, your results will be displayed. You may also play another game.
    <br/><br/>
    <strong>Tip:</strong> To highlight the parts of manyougana katakana were derived from, you can toggle <strong>Highlight Manyougana</strong> at any time.
    <br/><br/>
    <strong>Remarks:</strong> Your <strong>Skill Level</strong> determines how many of the 48 Japanese letters will be quizzed. Also, <strong>Spaced Repetition</strong> is implemented to target your learning experience on more difficult questions. See more on the <strong>About Page</strong>.
    <br/>
    </q-card-section>
  </q-card>
</q-dialog>
**/
</script>

<style>
</style>
