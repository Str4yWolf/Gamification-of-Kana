<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card :style="pageStyle">
      <!-- header -->
      <!-- back button -->
      <q-btn round dense flat icon="keyboard_backspace" @click="leavePageConfirm()" />
      &nbsp;
      <strong style="font-size: 120%;">Final Exam</strong>
      <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
      <span v-if="activateResults">
        <strong style="font-size: 120%;"> (Results)</strong>
        <br/>
        <br/>
        <span style="padding: 0px 107px 0px 57px;">
          Points:
        </span>
        <strong>{{examPoints}}</strong>
        <br/>
        <span style="padding: 0px 109px 0px 57px;">
          Errors:
        </span>
        <strong>{{96 - examPoints}}</strong>
        <br/>
        <!--<span style="padding: 0px 79px 0px 57px;">
          Free Errors:
        </span>
        <strong>{{(96 - examPoints) + freeErrors}}</strong>
        <br/>-->
        <span style="padding: 0px 28px 0px 57px;">
          Reward:
        </span>
        <strong>{{examPoints}}</strong> x 1.35
        <br/>
        <span style="padding: 0px 143px 0px 57px;">
        </span>
        <strong>= {{Math.ceil(examPoints * 1.35)}}</strong>
        <br>
        <br>
        <span style="font-size: 150%; font-weight: bold;">
          <span v-if="!hasFailedExam" style="color: green;">Pass!</span>
          <span v-if="hasFailedExam" style="color: red;">Fail</span>
          <span v-if="hasFailedExamErrors"><br/> &nbsp; ... due to errors.</span>
          <span v-if="hasFailedExamTime"><br/> &nbsp; ... due to time limitation.</span>
        </span>
        <br/>
        <br/>
        <span v-if="!hasFailedExam">
          Congratulations on finishing this Final Exam. Check out your achievements and try to unlock if you like.
        </span>
        <span v-if="hasFailedExam">
          You have done a great job. Continue learning and try again.
        </span>
        <br/>
        <br/>
        <br/>
        <span>
          <q-btn color="green" label="Retry" @click="retakeExam()" />
          &nbsp;
          <q-btn color="purple" label="Done" @click="leavePageConfirm()" />
        </span>
      </span>
      <span v-if="setupInProgress">
        <strong style="font-size: 120%;"> (Setup)</strong>
        <br/>
        &nbsp;
        &nbsp;
        <q-list>
        <strong style="font-size: 120%;" title="Configure your available inkblots">Available Inkblots</strong>
        <br/><br/>
        <q-expansion-item
          expand-separator
          icon="bubble_chart"
          label="Available Inkblots"
          title="Configure your available inkblots"
        >
        <!-- base inkblots -->
        <span style="padding: 0px 109px 0px 57px;" title="Inkblots you have collected"><strong>Your Inkblots</strong></span>
        <strong><q-icon name="whatshot" /> {{userObj.inkblots}}</strong>
        <br/>
        <br/>
        <!-- manyougana highlight toggle -->
        <span title="Highlight Manyougana during Exam">
          <q-toggle
            v-if="!showHighlightManyougana"
            v-model="highlightManyougana"
            color="red"
            label="Highlight Manyougana"
            style="width: 250px; color: red; text-decoration: line-through;"
            disable
          />
          <q-toggle
            v-if="showHighlightManyougana"
            v-model="highlightManyougana"
            color="red"
            label="Highlight Manyougana"
            style="width: 250px;"
          />
          <strong><q-icon name="whatshot" /> +{{extraInkblots1}}</strong>
        </span>
        <br/>
        <!-- Japanese Tip -->
        <span title="Show Japanese word translation during Exam">
          <q-toggle
            v-model="showJapanese"
            color="blue"
            label="Show Japanese Hints"
            style="width: 250px;"
          />
          <strong><q-icon name="whatshot" /> +{{extraInkblots2}}</strong>
        </span>
        <br/>
        <hr/>
        </q-expansion-item>
        <!-- total number of inkblots -->
        <span title="Your available inkblots">
          <span style="padding: 0px 162px 0px 57px;"><strong>Total</strong></span>
          <strong><q-icon name="whatshot" /> {{totalInkblots}}</strong>
        </span>
        <br/>
        <br/>
        <br/>
        <!-- inkblot allocation -->
        <strong style="font-size: 120%;" title="Allocate your inkblots for bonuses">Allocate Inkblots</strong>
        <br/><br/>
        <!-- total number of inkblots spent -->
        <q-expansion-item
          expand-separator
          icon="poll"
          label="Allocate Inkblots"
          title="Allocate your inkblots for bonuses"
        >
        <!-- error tolerance -->
        <span class="row" title="How many errors you can make during the exam">
          <span style="top: 20px; padding: 0px 0px 0px 18px; position: relative;"><strong>Free Errors (<q-icon name="done_all"/>)</strong> (<strong>5 <q-icon name="whatshot" /> each</strong>)</span>
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
        <span>
          <span style="top: 0px; padding: 0px 104px 0px 18px; position: relative;" title="How many additional seconds you can get for each question catogory"><strong>Bonus Seconds (1 <q-icon name="whatshot" /> each)</strong></span>
          <strong><q-icon name="whatshot" /> -{{modeInkblots}}</strong>
          <span class="row">
          &nbsp; &nbsp; &nbsp; &nbsp;
          <q-input
            v-model.number="mode1Inkblots"
            label="38.4s"
            type="number"
            max-length="2"
            style="max-width: 120px;"
            title="38.4s + your bonus for 48 questions"
            :rules="
              [val => !(val < 0) || 'invalid input']">
            <template v-slot:hint>
              Multiple Choice
            </template>
          </q-input>
          &nbsp; &nbsp;
          <q-input
            v-model.number="mode2Inkblots"
            label="36s"
            type="number"
            max-length="2"
            style="max-width: 120px;"
            title="36s + your bonus for 24 questions"
            :rules="
              [val => !(val < 0) || 'invalid input']">
            <template v-slot:hint>
              Word Reader
            </template>
          </q-input>
          &nbsp; &nbsp;
          <q-input
            v-model.number="mode3Inkblots"
            label="60s"
            type="number"
            max-length="2"
            style="max-width: 120px;"
            title="60s + your bonus for 24 questions"
            :rules="
              [val => !(val < 0) || 'invalid input']">
            <template v-slot:hint>
              Word Creator
            </template>
          </q-input>
        </span>
      </span>
      <br/>
      <hr/>
      </q-expansion-item>
      <span :style="markedOutOfInkblot" title="Your allocated inkblots">
        <span style="padding: 0px 204px 0px 57px;"><strong>Total</strong></span>
        <strong><q-icon name="whatshot" /> -{{allocatedInkblots}}</strong>
      </span>
      </q-list>
      <br/>
      <br/>
      <q-checkbox v-if="userObj.inkblots" v-model="paidExamFee" label="Pay 2 inkblots" title="2 inkblots will be consumed" />
      <!-- disabled version -->
      <q-checkbox v-if="!userObj.inkblots" v-model="paidExamFee" label="Pay 2 inkblots" title="2 inkblots will be consumed" disable />
      <br/>
      <br/>
      <br/>
      <span>
        <q-btn color="green" label="Start Exam" @click="startExam()" title="Start exam with current configuration" :disabled="disableExamStart" />
        &nbsp;
        <q-btn color="purple" label="Reset" @click="resetSetup()" title="Reset configuration" />
      </span>
      </span>
      <!-- parameters panel -->
      <span v-if="!setupInProgress" class="row">
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
      <word-reader :style="styleWR" :userObj="userObj" :script="script1" :highlightManyougana="highlightManyougana" :isFinalExam="true" :currentWordFinal="currentWord" ref="FinalExamWR"/>
      <word-creator :style="styleWC" :userObj="userObj" :script="script1" :isFinalExam="true" :currentWordFinal="currentWord" ref="FinalExamWC" :showJapanese="showJapanese" :highlightManyougana="highlightManyougana" />
    <q-dialog v-model="unlockNewMappingInfo">
      <q-card>
        <q-card-section>
          <div class="text-h6">Unlocked New Mapping</div>
        </q-card-section>
        <q-card-section>
          You can now learn <strong>one</strong> new mapping (<strong>Menu -> Learn New Mapping</strong>).
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog v-model="viewTutorial">
      <q-card>
        <q-card-section>
        Allocate your available inkblots to help you pass this Final Exam. <strong style="color: blue;">Hover over elements </strong>for more info.
        <br/>
        <br/>
        <strong>Exp boost: 1.35x</strong>
        <span v-if="!userObj.unlockNewMapping">
          <br/>
          <br/>
          <strong>Reward (Pass): Unlock new script mapping</strong>
        </span>
        </q-card-section>
      </q-card>
    </q-dialog>
    </q-card>
  </q-page>
</template>

<script>
import MultipleChoiceQuiz from '../components/MultipleChoiceQuiz.vue'
import WordCreator from '../components/WordCreator.vue'
import WordReader from '../components/WordReader.vue'
import finalExamKeys from '../statics/finalExamKeys.json'
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
      originalFreeErrors: 0,
      mode1Inkblots: 0,
      mode2Inkblots: 0,
      mode3Inkblots: 0,
      paidExamFee: false,
      // exam controllers
      remainingTime: 0,
      // Boolean process and button display controllors
      quizHasStarted: false,
      hasAnsweredQuestion: false,
      validationInProgress: false,
      highlightManyougana: false,
      // script-related
      script1: this.userObj.currentMapping[0],
      scripts: this.userObj.currentMapping,
      // quiz controllers
      mode: 0,
      disableOptions: true,
      questionInProgress: false,
      showJapanese: false,
      // final exam controller
      wordKeysPool: Object.keys(finalExamKeys),
      currentKey: 'a',
      currentWord: 'wolf',
      examPoints: 0,
      hasFailedExamErrors: false,
      hasFailedExamTime: false,
      numberQuestionsAnswered: 0,
      questionsPerCategory: 32,
      //
      viewTutorial: false,
      unlockNewMappingInfo: false
    }
  },
  computed: {
    showHighlightManyougana () {
      var s1 = this.scripts[0].split('-')[0]
      var s2 = this.scripts[1].split('-')[0]
      if (s1 === 'manyougana' || s2 === 'manyougana') {
        return true
      } else {
        return false
      }
    },
    script2 () {
      if (this.script1 === this.scripts[0]) {
        return this.scripts[1]
      } else {
        return this.scripts[0]
      }
    },
    hasFailedExam () {
      return (this.hasFailedExamErrors || this.hasFailedExamTime)
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
    activateResults () {
      return !this.setupInProgress && this.mode === 3
    },
    pageStyle () {
      var constant = 'width: 840px; padding: 30px;'
      if (this.setupInProgress) {
        return constant + ' height: 895px;'
      } else {
        return constant + ' height: 540px;'
      }
    },
    styleMCQ () {
      var constant = 'position: absolute; top: 100px;'
      if (this.activateMCQ) {
        return constant + ' z-index: 2;'
      } else {
        return constant + ' z-index: -1;'
      }
    },
    styleWC () {
      var constant = 'position: absolute; top: 100px;'
      if (this.activateWC) {
        return constant + ' z-index: 2;'
      } else {
        return constant + ' z-index: -1;'
      }
    },
    styleWR () {
      var constant = 'position: absolute; top: 100px;'
      if (this.activateWR) {
        return constant + ' z-index: 2;'
      } else {
        return constant + ' z-index: -1;'
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
      return (this.mode1Inkblots + this.mode2Inkblots + this.mode3Inkblots)
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
      return !this.paidExamFee || this.outOfInkblots || (this.freeErrors < 0) || (this.freeErrors > 10) || (this.mode1Inkblots < 0) || (this.mode2Inkblots < 0) || (this.mode3Inkblots < 0)
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
    this.$root.$on('leavePageFinalExam', this.leavePage)
    this.$root.$on('timeElapsed', this.timeElapsed)
    if (this.userObj.viewedTutorial[5] === false) {
      this.userObj.viewedTutorial[5] = true
      this.viewTutorial = true
      this.$root.$emit('updateDatabase')
    }
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
      // setup controllers
      this.setJapaneseHint = true
      this.setManyouganaHighlight = true
      this.freeErrors = 0
      this.originalFreeErrors = 0
      this.mode1Inkblots = 0
      this.mode2Inkblots = 0
      this.mode3Inkblots = 0
      this.paidExamFee = false
      // exam controllers
      this.remainingTime = 0
      // Boolean process and button display controllors
      this.quizHasStarted = false
      this.hasAnsweredQuestion = false
      this.validationInProgress = false
      this.highlightManyougana = false
      // script-related
      this.script1 = this.userObj.currentMapping[0]
      this.scripts = this.userObj.currentMapping
      // quiz controllers
      this.disableOptions = true
      this.questionInProgress = false
      this.showJapanese = false
      // final exam controller
      this.wordKeysPool = Object.keys(finalExamKeys)
      this.currentKey = 'a'
      this.currentWord = 'wolf'
      this.$root.$emit('stopTimer')
      this.$root.$emit('setShowTimer', false)
      this.wordKeysPool = Object.keys(finalExamKeys)
    },
    startExam () {
      this.setupInProgress = false
      this.userObj.inkblots -= 2
      this.originalFreeErrors = this.freeErrors
      this.$root.$emit('updateDatabase')
      this.$root.$emit('setIsFinalExam', true)
      this.$root.$emit('updateNumberFreeErrors', this.freeErrors)
      this.$root.$emit('setShowTimer', true)
      this.$root.$emit('setTimer', 38.4 + this.mode1Inkblots)
      this.nextQuestion()
    },
    endExam () {
      var reward = Math.ceil(this.examPoints * 1.35)
      this.$root.$emit('addExp', reward)
      this.$q.notify('Finished. You have been awarded ' + reward.toString() + ' experience points.')
      this.resetSetup()
      this.mode = 3
      if (this.hasFailedExam) {
        this.userObj.timesExamFailed += 1
      } else {
        this.userObj.timesExamPassed += 1
        // check all achievements
        if (this.showHighlightManyougana && !this.highlightManyougana) {
          this.$root.$emit('checkAchievements', 17)
        }
        if (!this.showJapanese) {
          this.$root.$emit('checkAchievements', 18)
        }
        if (this.modeInkblots <= 150) {
          this.$root.$emit('checkAchievements', 19)
        }
        if (this.modeInkblots <= 100) {
          this.$root.$emit('checkAchievements', 20)
        }
        if (this.modeInkblots <= 60) {
          this.$root.$emit('checkAchievements', 21)
        }
        if (this.modeInkblots <= 30) {
          this.$root.$emit('checkAchievements', 22)
        }
        if (this.originalFreeErrors === 0) {
          this.$root.$emit('checkAchievements', 23)
        }
        if (this.showHighlightManyougana && !this.highlightManyougana && !this.showJapanese) {
          this.$root.$emit('checkAchievements', 24)
        }
        if (!this.highlightManyougana && !this.showJapanese && this.originalFreeErrors === 0 && this.modeInkblots === 0) {
          this.$root.$emit('checkAchievements', 25)
        }
      }
      if (!this.hasFailedExam && this.userObj.unlockNewMapping === false) {
        this.checkMappingAchievements()
        this.userObj.learnedMappings.push(this.scripts[0] + '_' + this.scripts[1])
        if (this.userObj.learnedMappings.length === 10) {
          this.$root.$emit('checkAchievements', 36)
        }
        this.userObj.unlockNewMapping = true
        this.unlockNewMappingInfo = true
      }
      this.$root.$emit('checkAchievements', 9)
      this.$root.$emit('checkAchievements', 10)
      this.$root.$emit('checkAchievements', 11)
      this.$root.$emit('checkAchievements', 12)
      this.$root.$emit('updateDatabase')
    },
    /**
    systematically check whether any of the mapping achievements have been unlocked
    **/
    checkMappingAchievements () {
      var s1 = this.scripts[0]
      var s2 = this.scripts[1]
      var xs = ['romaji', 'katakana', 'manyougana-katakana', 'hiragana', 'hentaigana']

      if ((s1 === xs[1] & s2 === xs[0]) || (s1 === xs[0] & s2 === xs[1])) {
        this.$root.$emit('checkAchievements', 26)
      } else if ((s1 === xs[2] & s2 === xs[0]) || (s1 === xs[0] & s2 === xs[2])) {
        this.$root.$emit('checkAchievements', 27)
      } else if ((s1 === xs[3] & s2 === xs[0]) || (s1 === xs[0] & s2 === xs[3])) {
        this.$root.$emit('checkAchievements', 28)
      } else if ((s1 === xs[4] & s2 === xs[0]) || (s1 === xs[0] & s2 === xs[4])) {
        this.$root.$emit('checkAchievements', 29)
      } else if ((s1 === xs[2] & s2 === xs[1]) || (s1 === xs[1] & s2 === xs[2])) {
        this.$root.$emit('checkAchievements', 30)
      } else if ((s1 === xs[3] & s2 === xs[1]) || (s1 === xs[1] & s2 === xs[3])) {
        this.$root.$emit('checkAchievements', 31)
      } else if ((s1 === xs[4] & s2 === xs[1]) || (s1 === xs[1] & s2 === xs[4])) {
        this.$root.$emit('checkAchievements', 32)
      } else if ((s1 === xs[3] & s2 === xs[2]) || (s1 === xs[2] & s2 === xs[3])) {
        this.$root.$emit('checkAchievements', 33)
      } else if ((s1 === xs[4] & s2 === xs[2]) || (s1 === xs[2] & s2 === xs[4])) {
        this.$root.$emit('checkAchievements', 34)
      } else if ((s1 === xs[4] & s2 === xs[3]) || (s1 === xs[3] & s2 === xs[4])) {
        this.$root.$emit('checkAchievements', 35)
      }
    },
    retakeExam () {
      this.setupInProgress = true
      this.examPoints = 0
      this.hasFailedExamErrors = false
      this.hasFailedExamTime = false
      this.numberQuestionsAnswered = 0
      this.$root.$emit('updateNumberQuestions', [this.numberQuestionsAnswered, 96])
      this.mode = 0
      this.$root.$emit('setIsFinalExam', false)
    },
    startQuiz () {
      this.$refs.FinalExamMCQ.continueQuiz()
    },
    leavePageConfirm () {
      console.log('called leavePageConfirm() in FinalExam')
      if (!this.setupInProgress && !(this.mode === 3)) { // ask only when taking exam
        if (confirm('Are you sure you want to leave this page? All exam progress will be lost!')) {
          this.leavePage()
        }
      } else {
        this.leavePage()
      }
    },
    leavePage () {
      console.log('called leavePage() in FinalExam')
      this.resetSetup()
      this.setupInProgress = true
      this.examPoints = 0
      this.hasFailedExamErrors = false
      this.hasFailedExamTime = false
      this.numberQuestionsAnswered = 0
      this.$root.$emit('updateNumberQuestions', [this.numberQuestionsAnswered, 96])
      this.mode = 0
      this.$root.$emit('setIsFinalExam', false)
      this.$root.$emit('hideFinalExam')
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
      if (this.numberQuestionsAnswered === 96) {
        return this.endExam()
      }
      // TBD start
      // workaround for preemptive unintended drainout of word pool
      // fix finalExamWords keys / try 1 word per key
      if (this.wordKeysPool.length === 0) {
        this.wordKeysPool = Object.keys(finalExamKeys)
      }
      // TBD end
      // sample randomly from 96 word keys
      var ri1 = Math.floor(Math.random() * this.wordKeysPool.length)
      var nextCharacter = this.wordKeysPool[ri1].split('_')
      this.wordKeysPool.splice(ri1, 1)
      this.currentKey = nextCharacter[0]
      this.script1 = ((this.numberQuestionsAnswered < 47) ? this.scripts[parseInt(nextCharacter[1])] : this.scripts[0])
      // this.$q.notify('Script1 in nextQuestion(): ' + this.script1)

      // sample random word with current key
      var finalWordPool = finalExamWords[this.currentKey]
      var ri2 = Math.floor(Math.random() * finalWordPool.length)
      this.currentWord = finalWordPool[ri2]
      if (this.numberQuestionsAnswered === 48) {
        this.mode = 2
        this.$root.$emit('stopTimer')
        this.$root.$emit('setTimer', 36 + this.mode2Inkblots)
      } else if (this.numberQuestionsAnswered === 72) {
        this.mode = 1
        this.$root.$emit('stopTimer')
        this.$root.$emit('setTimer', 60 + this.mode3Inkblots)
      }
      console.log('CurrentKeyScript: ' + this.currentKey + ' ' + this.script1)
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
    },
    addExamPoints (n, correctAnswer) {
      console.log('called addExamPoints in FinalExam')
      if (!correctAnswer) {
        this.freeErrors -= 1
        this.$root.$emit('updateNumberFreeErrors', this.freeErrors)
        if (this.freeErrors === -1) {
          if (!this.hasFailedExam) {
            this.$q.notify('Exam failed due to error in answer. You may continue to practice.')
          }
          this.hasFailedExamErrors = true
        }
      } else {
        this.examPoints += n
      }
    },
    timeElapsed () {
      if (!this.setupInProgress) {
        if (!this.hasFailedExam) {
          this.$q.notify('Exam failed due to time limit. You may continue to practice.')
        }
        this.hasFailedExamTime = true
      }
    },
    incrementNumberQuestionsAnswered (n) {
      this.numberQuestionsAnswered += n
      this.$root.$emit('updateNumberQuestions', [this.numberQuestionsAnswered, 96])
    },
    enterSolutionWR () {
      this.questionInProgress = false
      setTimeout(this.$refs.FinalExamWR.validateSolution, 1)
    },
    enterSolutionWC () {
      this.disableOptions = true
      this.$refs.FinalExamWC.endCreation()
    }
  }
}
/**
<q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Final Exam)</div>
        </q-card-section>
        <q-card-section>
        Passing the <strong>Final Exam</strong> is proof of your knowledge of Manyougana and all the time and work you have chosen to invest into your studies. It is a <strong>milestone</strong> along your journey to master Manyougana.
        <br/>
        <br/>
        In the final exam, you will face the challenge of applying your knowledge of Manyougana in a race against time. You will generally be asked all 48 Japanese letters with Manyougana as source and target script, with a low probability of receiving a random letter.
        <br/>
        <br/>
        <br/>
        <br/>
        <strong style="font-size: 120%; ">Setup</strong>
        <br/>
        <br/>
        In addition to acquiring proficiency through practice, you can make use of your <strong>Available Inkblots.</strong> They are the sum of your <strong>Base Inkblots</strong> (the Inkblots displayed on the top left menu) and additional <strong>bonuses</strong>.
        <br/>
        <br/>
        The bonuses apply when you choose <strong>not to use </strong> <strong>Highlight Manyougana</strong>, <strong>Show Japanese Hints</strong>, or <strong>both</strong>. Adjust the toggles to (de)activate the bonuses.
        <br/>
        <br/>
        You use your Available Inkblots in <strong>Allocate Inkblots</strong> to get helpful means to help you pass your exam. <strong>Free Errors</strong> allow you to fail questions (you can get at most 10 Free Errors). <strong>Bonus Seconds</strong> can be allocated to each of the three question types (<strong>Multiple Choice</strong>, <strong>Word Reader</strong>, <strong>Word Creator</strong>). The base time for each question type is displayed above its input field. Adjust the input fields to your preferences.
        <br/>
        <br/>
        You can allocate at most the number of Available Inkblots, but you don't need to.
        <br/>
        <br/>
        Finally, you need to provide an <strong>Exam Ticket</strong> you can purchase at the <strong>Shop</strong>. Check the respective checkbox.
        <br/>
        <br/>
        If all of your input is sound, the <strong>START EXAM</strong> button will be enabled and you can choose to start, or click <strong>RESET</strong> to reset the settings.
        <br/>
        <br/>
        While none of your <strong>"Base" Inkblots</strong> will actually be consumed, you will permanently lose one <strong>Exam Ticket</strong> once you start the exam, regardless of whether you are going to finish the exam or its outcome.
        <br/>
        <br/>
        None of the Setup can be changed anymore once you have started the exam.
        <br/>
        <br/>
        <br/>
        <br/>
        <strong style="font-size: 120%; ">Taking the Exam</strong>
        <br/>
        <br/>
        The exam comprises 96 Questions split into three distinct categories. Questions 1-32 are Multiple Choice, Questions 33-64 are Word Reader, and Questions 65-96 are Word Creator.
        <br/>
        <br/>
        You will have a limited amount of time to answer question for <strong>each</strong> category. Remaining time cannot be carried over. The timer will be set at the <strong>base time + your respective bonus seconds</strong> for each category.
        <br/>
        <br/>
        The timer will only run when you have been shown a question. Once you have answered the question, the timer will stop and you will be given immediate feedback as to whether you were right or wrong. Wrong answers will be counted as errors and subsequently subtracted from your <strong>Free Errors</strong>.
        <br/>
        <br/>
        Once the timer runs out of time in <strong>any</strong> of the three Question categories, you will fail the exam and notified thereof. The same applies once your Free Errors count drops below 0. However, you may want to proceed with the exam to the end to claim experience points.
        <br/>
        <br/>
        As soon as you have answered all 96 questions, your results will be shown.
        <br/>
        <br/>
        <br/>
        <br/>
        <strong style="font-size: 120%; ">Results</strong>
        <br/>
        <br/>
        Your results summarize how many answers you have answered correctly (<strong>"Points"</strong>), how many <strong>Errors</strong> you have made, and whether you have <strong color="green">Passed</strong> or <strong color="red">Failed</strong>. You will also be told why you have failed the exam.
        <br/>
        <br/>
        You will receive <strong>boosted experience points (x1.35) after</strong> you have finished the exam. Only correct answers will receive one point each; i.e., <strong>Free Errors</strong> will not count as points when they have "saved" an incorrect answer.
        <br/>
        <br/>
        You may choose to retake the exam (go to the Final Exam Setup) by clicking <strong>RETRY</strong> or leave the page by clicking <strong>DONE</strong>.
        <br/>
        <br/>
        <br/>
        <br/>
        <strong>Keyboard Shortcuts </strong>
        <br/>
        You can comfortably dash through the exam by using keyboard only. Keyboard shortcuts will work immediately in both <strong>Multiple Choice</strong> (Questions 1-32) and <strong>Word Creator</strong> (Questions 65-96). For <strong>Word Reader</strong> (Questions 33-64), you need to click on the text field once for keyboard shortcuts to work to the end (or until you use a mouse click again).
        <br/>
        </q-card-section>
      </q-card>
    </q-dialog>
**/
</script>

<style>
</style>
