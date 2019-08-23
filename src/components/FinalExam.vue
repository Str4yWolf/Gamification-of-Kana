<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 820px; padding: 30px;">
      <!-- header -->
      <!-- back button -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideFinalExam')" />
      &nbsp;
      <strong style="font-size: 120%;">Final Exam</strong>

      <span v-if="setupInProgress">
        <strong style="font-size: 120%;"> (Setup)</strong>
        <br/>
        &nbsp;
        &nbsp;
        <q-list>
        <strong style="font-size: 120%;">Available Inkblots</strong>
        <br/><br/>
        <q-expansion-item
          expand-separator
          icon="bubble_chart"
          label="Available Inkblots"
        >
        <!-- base inkblots -->
        <span style="padding: 0px 107px 0px 57px;"><strong>Base Inkblots</strong></span>
        <strong><q-icon name="whatshot" /> {{userObj.inkblots}}</strong>
        <br/>
        <br/>
        <!-- manyougana highlight toggle -->
        <q-toggle
          v-model="highlightManyougana"
          color="red"
          label="Highlight Manyougana"
          style="width: 250px;"
        />
        <strong><q-icon name="whatshot" /> +{{extraInkblots1}}</strong>
        <br/>
        <!-- Japanese Tip -->
        <q-toggle
          v-model="showJapanese"
          color="red"
          label="Show Japanese Hints"
          style="width: 250px;"
        />
        <strong><q-icon name="whatshot" /> +{{extraInkblots2}}</strong>
        <br/>
        <hr/>
        </q-expansion-item>
        <!-- total number of inkblots -->
        <span style="padding: 0px 162px 0px 57px;"><strong>Total</strong></span>
        <strong><q-icon name="whatshot" /> {{totalInkblots}}</strong>
        <br/>
        <br/>
        <br/>
        <!-- inkblot allocation -->
        <strong style="font-size: 120%;">Allocate Inkblots</strong>
        <br/><br/>
        <!-- total number of inkblots spent -->
        <q-expansion-item
          expand-separator
          icon="poll"
          label="Allocate Inkblots"
        >
        <!-- error tolerance -->
        <span class="row">
        <span style="top: 20px; padding: 0px 0px 0px 18px; position: relative;">Free Errors (<strong>5 <q-icon name="whatshot" />/ea</strong>)</span>
        &nbsp; &nbsp; &nbsp;
        <q-input
          v-model.number="freeErrors"
          type="number"
          max-length="2"
          style="max-width: 70px;"
          :rules="
            [val => !(val < 0) || 'invalid input',
            val => !(val > 10) || 'limit is 10',
            outOfInkblots || 'not enough inkblots']"
        />
        <span style="top: 20px; padding: 0px 0px 0px 18px; position: relative;"><strong><q-icon name="whatshot" /> -{{errorInkblots}}</strong></span>
        </span>
        <!-- fieldAllocation -->
        <span style="top: 0px; padding: 0px 76px 0px 18px; position: relative;">Bonus Seconds (<strong>1 <q-icon name="whatshot" />/ea</strong>)</span>
        <strong><q-icon name="whatshot" /> -{{modeInkblots}}</strong>
        <span class="row">
        &nbsp; &nbsp; &nbsp; &nbsp;
        <q-input
          v-model.number="mode1Inkblots"
          label="20s"
          type="number"
          max-length="2"
          style="max-width: 120px;"
          :rules="
            [val => !(val < 0) || 'invalid input']">
          <template v-slot:hint>
            Multiple Choice
          </template>
        </q-input>
        &nbsp; &nbsp;
        <q-input
          v-model.number="mode2Inkblots"
          label="37.5s"
          type="number"
          max-length="2"
          style="max-width: 120px;"
          :rules="
            [val => !(val < 0) || 'invalid input']">
          <template v-slot:hint>
            Word Reader
          </template>
        </q-input>
        &nbsp; &nbsp;
        <q-input
          v-model.number="mode3Inkblots"
          label="62.5s"
          type="number"
          max-length="2"
          style="max-width: 120px;"
          :rules="
            [val => !(val < 0) || 'invalid input']">
          <template v-slot:hint>
            Word Creator
          </template>
        </q-input>
        &nbsp; &nbsp;
        <q-input
          v-model.number="mode4Inkblots"
          label="Task4?"
          type="number"
          max-length="2"
          style="max-width: 120px;"
          :rules="
            [val => !(val < 0) || 'invalid input']">
          <template v-slot:hint>
            unknown
          </template>
        </q-input>
      </span>
      <br/>
      <hr/>
      </q-expansion-item>
      <span :style="markedOutOfInkblot">
        <span style="padding: 0px 162px 0px 57px;"><strong>Total</strong></span>
        <strong><q-icon name="whatshot" /> -{{allocatedInkblots}}</strong>
      </span>
      </q-list>
      <br/>
      <br/>
      <q-checkbox v-if="userObj.examTickets" v-model="shownExamTicket" label="Provide Exam Ticket" title="Exam Ticket will be consumed." />
      <!-- disabled version -->
      <q-checkbox v-if="!userObj.examTickets" v-model="shownExamTicket" label="Provide Exam Ticket" title="Exam Ticket will be consumed." disable />
      <br/>
      <br/>
      <br/>
      <span>
        <q-btn color="green" label="Start Exam" @click="startExam()" :disabled="disableExamStart" />
        &nbsp;
        <q-btn color="purple" label="Reset" @click="resetSetup()" />
      </span>
      </span>
      <!-- parameters panel -->
      <span class="row">
        <!-- context dependent buttons -->
        <span v-if="activateMCQ" style="padding-left:10px; position: absolute; left: 640px; top: 33px;">
          <q-btn v-if="validationInProgress" color="green" label="Continue" @click="nextQuestion()" />
          <q-btn v-if="!quizHasStarted" color="green" label="Continue" @click="nextQuestion()" />
        </span>
        <span v-if="activateWC">
          <q-btn v-if="disableOptions" color="green" label="Continue" title="Continue to next question (Enter)" @click="nextQuestion()" style="padding-left:10px; position: absolute; left: 640px; top: 33px;" />
          <q-btn v-if="!disableOptions" color="green" label="Enter" title="Enter answers (Enter)" @click="enterSolutionWC()" style="padding-left:10px; position: absolute; left: 640px; top: 33px;" />
        </span>
        <span v-if="activateWR">
          <q-btn v-if="!questionInProgress" color="green" label="Continue" title="Continue to next question (Enter)" @click="nextQuestion()" style="padding-left:10px; position: absolute; left: 640px; top: 33px;" />
          <q-btn v-if="questionInProgress" color="green" label="Enter" title="Enter answers (Enter)" @click="enterSolutionWR()" style="padding-left:10px; position: absolute; left: 640px; top: 33px;" />
        </span>
      </span>
      <multiple-choice-quiz :style="styleMCQ" :userObj="userObj" :script1="script1" :script2="script2" :highlightManyougana="highlightManyougana" :quizLength="25" :singleQuestion="true" :isFinalExam="true" :currentKeyFinal="currentKey" ref="FinalExamMCQ" />
      <word-creator :style="styleWC" :userObj="userObj" :script="script1" ref="FinalExamWC" :showJapanese="showJapanese" :highlightManyougana="highlightManyougana" />
      <word-reader :style="styleWR" :userObj="userObj" :script="script1" :highlightManyougana="highlightManyougana" ref="FinalExamWR" />
    </q-card>
  </q-page>
</template>

<script>
import MultipleChoiceQuiz from '../components/MultipleChoiceQuiz.vue'
import WordCreator from '../components/WordCreator.vue'
import WordReader from '../components/WordReader.vue'
import finalExamWords from '../statics/finalExamWords.json'

export default {
  // name: 'PageName',
  components: {
    MultipleChoiceQuiz,
    WordCreator,
    WordReader
  },
  data () {
    return {
      // setup controllers
      setupInProgress: true,
      setJapaneseHint: true,
      setManyouganaHighlight: true,
      freeErrors: 0,
      mode1Inkblots: 0,
      mode2Inkblots: 0,
      mode3Inkblots: 0,
      mode4Inkblots: 0,
      shownExamTicket: false,
      // exam controllers
      remainingTime: 0,
      // Boolean process and button display controllors
      quizHasStarted: false,
      hasAnsweredQuestion: false,
      validationInProgress: false,
      highlightManyougana: false,
      // script-related
      script1: 'katakana',
      scripts: ['katakana', 'manyougana-katakana'],
      // quiz controllers
      mode: 0,
      disableOptions: true,
      questionInProgress: false,
      showJapanese: false,
      // final exam controller
      wordKeysPool: Object.keys(finalExamWords),
      currentKey: 'a',
      examPoints: 0,
      hasFailedExam: false,
      numberQuestionsAnswered: 0
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
    activateMCQ () {
      return !this.setupInProgress && this.mode === 0
    },
    activateWC () {
      return !this.setupInProgress && this.mode === 1
    },
    activateWR () {
      return !this.setupInProgress && this.mode === 2
    },
    styleMCQ () {
      if (this.activateMCQ) {
        return 'position: relative; z-index: 2;'
      } else {
        return 'position: relative; z-index: -1;'
      }
    },
    styleWC () {
      if (this.activateWC) {
        return 'position: relative; z-index: 2; top: -400px;'
      } else {
        return 'position: relative; z-index: -1;'
      }
    },
    styleWR () {
      if (this.activateWR) {
        return 'position: relative; z-index: 2; top: -800px;'
      } else {
        return 'position: relative; z-index: -1;'
      }
    },
    extraInkblots1 () {
      if (this.highlightManyougana) {
        return 0
      } else {
        return 5
      }
    },
    extraInkblots2 () {
      if (this.showJapanese) {
        return 0
      } else {
        return 10
      }
    },
    totalInkblots () {
      return this.userObj.inkblots + this.extraInkblots1 + this.extraInkblots2
    },
    errorInkblots () {
      return this.freeErrors * 5
    },
    modeInkblots () {
      return (this.mode1Inkblots + this.mode2Inkblots + this.mode3Inkblots + this.mode4Inkblots)
    },
    allocatedInkblots () {
      return this.errorInkblots + this.modeInkblots
    },
    outOfInkblots () {
      return this.allocatedInkblots > this.totalInkblots
    },
    markedOutOfInkblot () {
      if (this.outOfInkblots) {
        return 'color: red;'
      } else {
        return 'color: black;'
      }
    },
    disableExamStart () {
      return !this.shownExamTicket || this.outOfInkblots || (this.freeErrors < 0) || (this.freeErrors > 10) || (this.mode1Inkblots < 0) || (this.mode2Inkblots < 0) || (this.mode3Inkblots < 0) || (this.mode4Inkblots < 0)
    }
  },
  props: {
    userObj: Object
  },
  created () {
  },
  mounted () {
    this.$refs.modal.$el.focus()
    // listen to event calls from elsewhere
    this.$root.$on('MultipleChoiceQuestion answered', this.nextQuestion())
    this.$root.$on('setValidationInProgress', this.setValidationInProgress)
    this.$root.$on('incrementNumberQuestionsAnswered', this.incrementNumberQuestionsAnswered)
    this.$root.$on('addExamPoints', this.addExamPoints)
  },
  methods: {
    /**
    Validate user keyboard input
    **/
    validateKeyInput (event) {
      if (this.activateMCQ) { // Multiple choice
        switch (event.keyCode) {
          // keyboard numbers 1 - 4
          case 49:
          case 50:
          case 51:
          case 52:
            if (!this.validationInProgress) {
              console.log('called validateKeyInput with 1-4')
              this.$refs.FinalExamMCQ.validateOption(event.keyCode - 48)
            } else {
              console.log('Validation is in progress. Options unusable.')
            }
            break
          case 13:
            console.log('pressed enter in validateKeyInput')
            if (this.validationInProgress) {
              this.nextQuestion()
            }
            break
        }
      } else if (this.activateWC) { // word creator
        switch (event.keyCode) {
          case 49:
          case 50:
          case 51:
          case 52:
            if (!this.disableOptions) {
              console.log('called validateKeyInput with 1-4')
              this.$refs.FinalExamWC.validateOption(event.keyCode - 48)
            } else {
              console.log('Validation is in progress. Options unusable.')
            }
            break
          case 13:
            console.log('pressed enter in validateKeyInput')
            if (!this.disableOptions) {
              this.enterSolutionWC()
            } else {
              this.nextQuestion()
            }
            break
        }
      } else if (this.activateWR) { // word reader
        switch (event.keyCode) {
          case 13:
            console.log('pressed enter in validateKeyInput')
            if (this.questionInProgress) {
              this.enterSolutionWR()
            } else {
              this.nextQuestion()
            }
            break
        }
      } else {
        console.log('called validateKeyInput with key')
        console.log(event.key)
        console.log('and keyCode')
        console.log(event.keyCode)
      }
    },
    resetSetup () {
      this.setJapaneseHint = true
      this.setManyouganaHighlight = true
      this.freeErrors = 0
      this.mode1Inkblots = 0
      this.mode2Inkblots = 0
      this.mode3Inkblots = 0
      this.mode4Inkblots = 0
      this.shownExamTicket = false
    },
    startExam () {
      this.setupInProgress = false
      this.userObj.examTickets -= 1
      this.$root.$emit('updateDatabase')
      this.$root.$emit('toggleIsFinalExam')
      this.$root.$emit('updateNumberFreeErrors', this.freeErrors)
    },
    startQuiz () {
      this.$refs.FinalExamMCQ.continueQuiz()
    },
    /**
    End quiz by intializing quiz controls and displaying feedback to user
    **/
    endQuiz () {
      console.log('called endQuiz from MultipleChoice')
      this.quizHasStarted = false
      this.validationInProgress = false
      this.questionsAnsweredCorrectly = 0
    },
    setQuizHasStarted (x) {
      this.quizHasStarted = x
    },
    setValidationInProgress (x) {
      this.validationInProgress = x
    },
    nextQuestion () {
      console.log('called nextQuestion in Final Exam')
      var randomIndex = Math.floor(Math.random() * this.wordKeysPool.length)
      var nextCharacter = this.wordKeysPool[randomIndex].split('_')
      this.wordKeysPool.splice(randomIndex, 1)
      this.currentKey = nextCharacter[0]
      this.script1 = nextCharacter[1]
      switch (this.mode) {
        case 0:
        // Multiple choice
          this.$refs.FinalExamMCQ.$el.focus()
          this.quizHasStarted = true
          this.$refs.FinalExamMCQ.continueExam()
          break
        case 1:
        // Word creator
          this.$refs.FinalExamWC.$el.focus()
          this.disableOptions = false
          this.$refs.FinalExamWC.setNewCreation()
          break
        case 2:
        // Word reader
          this.$refs.FinalExamWR.$el.focus()
          this.questionInProgress = true
          this.$refs.FinalExamWR.generateQuestion()
          break
      }
      console.log('called randomizeNextQuestion in GL')
    },
    addExamPoints (n, correctAnswer) {
      console.log('called addExamPoints in FinalExam')
      this.examPoints += n
      if (!correctAnswer) {
        this.freeErrors -= 1
        this.$root.$emit('updateNumberFreeErrors', this.freeErrors)
        if (this.freeErrors === -1) {
          this.$q.notify('Exam failed. You may continue to practice')
          this.hasFailedExam = true
        }
      }
    },
    incrementNumberQuestionsAnswered () {
      this.numberQuestionsAnswered += 1
      this.$root.$emit('updateNumberQuestions', [this.numberQuestionsAnswered, 96])
    },
    enterSolutionWR () {
      this.questionInProgress = false
      this.$refs.FinalExamWR.validateSolution()
    },
    enterSolutionWC () {
      this.disableOptions = true
      this.$refs.FinalExamWC.endCreation()
    }
  }
}
</script>

<style>
</style>
