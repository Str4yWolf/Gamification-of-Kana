<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-btn style="position: absolute; top: 27px; left: 245px; z-index: 3;" round dense flat icon="keyboard_backspace" @click="$root.$emit('hideGeneralLearning')" />
    <q-card v-if="activateQuiz" style="width: 840px; padding: 30px; height: 540px;">
      <span v-if="a" style="padding: 0px 0px 0px 37px;"/>
      &nbsp;
      <!-- header -->
      <!-- back button -->
      <strong style="font-size: 120%; ">Quest</strong>
      &nbsp;
      &nbsp;
      &nbsp;
      &nbsp;
      <!-- manyougana highlight toggle -->
      <q-toggle
        v-if="showHighlightManyougana"
        v-model="highlightManyougana"
        color="red"
        label="Highlight Manyougana"
        @input="updateHighlights()"
      />
      <!-- Japanese Tip -->
      <q-toggle
        v-if="activateWC"
        v-model="showJapanese"
        color="red"
        label="Japanese Hint"
      />
      <!-- parameters panel -->
      <span class="row">
        <!-- context dependent buttons -->
        <span v-if="activateMCQ" style="padding-left:10px; position: absolute; right: 62px; top: 33px;">
          <q-btn v-if="validationInProgress" color="green" label="Continue" @click="randomizeNextQuestion()" />
        </span>
        <span v-if="activateWC">
          <q-btn v-if="disableOptions" color="green" label="Continue" title="Continue to next question (Enter)" @click="randomizeNextQuestion()" style="padding-left:10px; position: absolute; right: 62px; top: 33px;" />
          <q-btn v-if="!disableOptions" color="green" label="Enter" title="Enter answers (Enter)" @click="enterSolutionWC()" style="padding-left:10px; position: absolute; right: 62px; top: 33px;" />
        </span>
        <span v-if="activateWR">
          <q-btn v-if="!questionInProgress" color="green" label="Continue" title="Continue to next question (Enter)" @click="randomizeNextQuestion()" style="padding-left:10px; position: absolute; right: 62px; top: 33px;" />
          <q-btn v-if="questionInProgress" color="green" label="Enter" title="Enter answers (Enter)" @click="enterSolutionWR()" style="padding-left:10px; position: absolute; right: 62px; top: 33px;" />
        </span>
      </span>
      <multiple-choice-quiz :style="styleMCQ" :userObj="userObj" :script1="script1" :script2="script2" :highlightManyougana="highlightManyougana" :quizLength="1000000" :singleQuestion="true" ref="GeneralLearningMCQ" />
      <word-creator :style="styleWC" :userObj="userObj" :script="userObj.currentMapping[0]" ref="GeneralLearningWC" :showJapanese="showJapanese" :highlightManyougana="highlightManyougana" />
      <word-reader :style="styleWR" :userObj="userObj" :script="userObj.currentMapping[0]" :highlightManyougana="highlightManyougana" ref="GeneralLearningWR" />
      <q-dialog v-model="viewTutorial">
        <q-card style="padding: 10px;">
          <strong>Tip: </strong>Use keyboard shortcuts <strong style="color: blue;">1 - 4 </strong> for Options and <strong style="color: blue;">Enter </strong> for ENTER and CONTINUE.
        </q-card>
      </q-dialog>
    </q-card>
    <q-card v-if="showIntro1" style="width: 840px; padding: 30px; height: 560px;">
      <!-- header -->
      <!-- back button -->
      <span v-if="a" style="padding: 0px 0px 0px 37px;"/>
      &nbsp;
      <strong style="font-size: 120%;">Quest Preparation (1)</strong> &nbsp; &nbsp; &nbsp;
      <!-- manyougana highlight toggle -->
      <q-toggle
        v-if="showHighlightManyougana"
        v-model="highlightManyougana"
        color="red"
        label="Highlight Manyougana"
        @input="updateHighlights()"
      /><br/>
      <!-- next button -->
      <span style="padding-left:10px; position: absolute; left: 700px; top: 33px;">
          <q-btn color="green" label="Next" @click="introFirstPage = false" />
      </span>
      <span v-if="!skillLvl10" style="position: relative; padding: 40px;">
        <p>Here are the characters you will need to know to rise to <strong>Skill Level {{'' + (userObj.skillLvl + 1)}}</strong>.
          <br/>
          <br/>
          <strong><span style="color: blue;">Hover your mouse over the images</span> to familiarize yourself.</strong>
        </p>
      </span>
      <span v-if="skillLvl10" style="position: relative; padding: 40px;">
        <br/>
        <br/>
        <p><strong>Congratulations.</strong> You have learned all characters. Here you can strengthen your knowledge.
        </p>
      </span>
      <span v-if="skillLvl0" class="row">
        <character-info :letter="'a'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'i'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'u'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'e'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'o'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl1" class="row">
        <character-info :letter="'ka'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ki'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ku'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ke'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ko'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl2" class="row">
        <character-info :letter="'sa'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'shi'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'su'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'se'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'so'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl3" class="row">
        <character-info :letter="'ta'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'chi'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'tsu'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'te'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'to'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl4" class="row">
        <character-info :letter="'na'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ni'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'nu'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ne'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'no'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl5" class="row">
        <character-info :letter="'ha'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'hi'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'fu'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'he'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ho'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl6" class="row">
        <character-info :letter="'ma'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'mi'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'mu'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'me'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'mo'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl7" class="row">
        <character-info :letter="'ra'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ri'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ru'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'re'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'ro'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl8" class="row">
        <character-info :letter="'ya'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'yu'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'yo'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'wa'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'wo'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
      <span v-if="skillLvl9" class="row">
        <character-info :letter="'n'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'we'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
        <character-info :letter="'wi'" :highlight="highlightManyougana" :sourceScript="userObj.currentMapping[0]" :scripts="userObj.currentMapping" />
      </span>
    </q-card>
    <q-card v-if="showIntro2" style="width: 840px; padding: 30px; height: 560px;">
      <!-- header -->
      <!-- back button -->
      <span v-if="a" style="padding: 0px 0px 0px 37px;"/>
      &nbsp;
      <strong style="font-size: 120%;">Quest Preparation (2)</strong><br/>
      <!-- back button -->
      <span style="padding-left:10px; position: absolute; left: 630px; top: 33px;">
          <q-btn color="green" label="Back" @click="introFirstPage = true" />
      </span>
      <!-- next button -->
      <span style="padding-left:10px; position: absolute; left: 700px; top: 33px;">
          <q-btn color="purple" label="Start" @click="startQuest()" />
      </span>
      <span style="position: relative; padding: 40px;"/>
      <p>Please make good use of the <br/><strong>Smart Flashcard</strong><br/> before starting your <strong>Quest</strong>!</p>
      <br/>
      <br/>
      <br/>
      <br/>
      <br/>
      <br/>
      <p style="color: blue;"><strong>Tip: </strong>You can always review all <br/>characters in <strong>Character Reference</strong> or <br/><strong>Individual Tools -> Smart Flashcard</strong><br/> in the menu.</p>
      <flip-card style="position: absolute; top: -20px; left: 292px;" :userObj="userObj" :isTutorial="true" />
    </q-card>
  </q-page>
</template>

<script>
import CharacterInfo from '../components/CharacterInfo.vue'
import FlipCard from '../components/FlipCard.vue'
import MultipleChoiceQuiz from '../components/MultipleChoiceQuiz.vue'
import WordCreator from '../components/WordCreator.vue'
import WordReader from '../components/WordReader.vue'

export default {
  // name: 'PageName',
  components: {
    CharacterInfo,
    FlipCard,
    MultipleChoiceQuiz,
    WordCreator,
    WordReader
  },
  data () {
    return {
      // Boolean process and button display controllors
      quizHasStarted: false,
      hasAnsweredQuestion: false,
      validationInProgress: false,
      highlightManyougana: false,
      highlight: false,
      // script-related
      script1: this.userObj.currentMapping[0],
      script2: this.userObj.currentMapping[1],
      // quiz controllers
      mode: 0,
      disableOptions: true,
      questionInProgress: false,
      showJapanese: false,
      //
      viewTutorial: false,
      introFirstPage: true,
      a: true
    }
  },
  computed: {
    activateMCQ () {
      return this.mode === 0 && this.userObj.learningMode !== 0
    },
    activateWR () {
      return this.mode === 1 && this.userObj.learningMode !== 0
    },
    activateWC () {
      return this.mode === 2 && this.userObj.learningMode !== 0
    },
    activateQuiz () {
      return this.userObj.learningMode > 0
    },
    showIntro1 () {
      return this.userObj.learningMode === 0 && this.introFirstPage
    },
    showIntro2 () {
      return this.userObj.learningMode === 0 && !this.introFirstPage
    },
    showHighlightManyougana () {
      var s1 = this.userObj.currentMapping[0].split('-')[0]
      var s2 = this.userObj.currentMapping[1].split('-')[0]
      if (this.showIntro1 && (s1 === 'manyougana' || s2 === 'manyougana')) {
        return true
      } else if (this.activateMCQ && (s1 === 'manyougana' || s2 === 'manyougana')) {
        return true
      } else if (this.activateWR && s1 === 'manyougana') {
        return true
      } else if (this.activateWC && s1 === 'manyougana') {
        return true
      } else {
        return false
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
    skillLvl0 () {
      return this.userObj.skillLvl === 0
    },
    skillLvl1 () {
      return this.userObj.skillLvl === 1
    },
    skillLvl2 () {
      return this.userObj.skillLvl === 2
    },
    skillLvl3 () {
      return this.userObj.skillLvl === 3
    },
    skillLvl4 () {
      return this.userObj.skillLvl === 4
    },
    skillLvl5 () {
      return this.userObj.skillLvl === 5
    },
    skillLvl6 () {
      return this.userObj.skillLvl === 6
    },
    skillLvl7 () {
      return this.userObj.skillLvl === 7
    },
    skillLvl8 () {
      return this.userObj.skillLvl === 8
    },
    skillLvl9 () {
      return this.userObj.skillLvl === 9
    },
    skillLvl10 () {
      return this.userObj.skillLvl > 9
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
    this.$root.$on('MultipleChoiceQuestion answered', this.randomizeNextQuestion())
    this.$root.$on('setValidationInProgress', this.setValidationInProgress)
    if (this.userObj.viewedTutorial[0] === false) {
      this.userObj.viewedTutorial[0] = true
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
              this.$refs.GeneralLearningMCQ.validateOption(event.keyCode - 48)
            } else {
              console.log('Validation is in progress. Options unusable.')
            }
            break
          case 13:
            console.log('pressed enter in validateKeyInput')
            if (this.validationInProgress) {
              this.randomizeNextQuestion()
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
              this.$refs.GeneralLearningWC.validateOption(event.keyCode - 48)
            } else {
              console.log('Validation is in progress. Options unusable.')
            }
            break
          case 13:
            console.log('pressed enter in validateKeyInput')
            if (!this.disableOptions) {
              this.enterSolutionWC()
            } else {
              this.randomizeNextQuestion()
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
              this.randomizeNextQuestion()
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
    updateHighlights () {
      /**
      switch (this.mode) {
        case 1:
          this.$refs.GeneralLearningMCQ.updateHighlight()
          break
        case 2:
          this.$refs.GeneralLearningWR.updateHighlight()
          break
        case 3:
          this.$refs.GeneralLearningWC.updateHighlight()
          break
      }
      **/
      setTimeout(this.$refs.GeneralLearningMCQ.updateHighlight, 1)
      setTimeout(this.$refs.GeneralLearningWR.updateHighlight, 1)
      setTimeout(this.$refs.GeneralLearningWC.updateHighlight, 1)
    },
    startQuiz () {
      this.$refs.GeneralLearningMCQ.continueQuiz()
    },
    /**
    End quiz by intializing quiz controls and displaying feedback to user
    **/
    endQuiz () {
      console.log('called endQuiz from MultipleChoice')
      this.quizHasStarted = false
      this.validationInProgress = false
      this.questionsAnsweredCorrectly = 0
      this.numberQuestionsAnswered = 0
    },
    setQuizHasStarted (x) {
      this.quizHasStarted = x
    },
    setValidationInProgress (x) {
      this.validationInProgress = x
    },
    startQuest () {
      console.log('called startQuest')
      this.userObj.learningMode += 1
      this.introFirstPage = true
      this.$q.notify('You have unlocked Multiple Choice Quiz for learning Skill Level ' + (this.userObj.skillLvl + 1) + '.')
      this.$root.$emit('updateDatabase')
      this.$root.$emit('initializeGeneralLearningQuiz')
    },
    randomizeNextQuestion () {
      console.log('called randomizeNextQuestion in GL')
      this.userObj.timesGL += 1
      this.$root.$emit('checkAchievements', 16)
      this.mode = Math.floor(Math.random() * this.userObj.learningMode)
      var script1Index = Math.floor(Math.random() * 2)
      var script2Index = (script1Index ? 0 : 1)
      this.script1 = this.userObj.currentMapping[script1Index]
      this.script2 = this.userObj.currentMapping[script2Index]
      switch (this.mode) {
        case 0:
        // Multiple choice
          this.$refs.GeneralLearningMCQ.$el.focus()
          this.quizHasStarted = true
          setTimeout(this.$refs.GeneralLearningMCQ.continueQuiz, 1)
          break
        case 1:
        // Word reader
          this.$refs.GeneralLearningWR.$el.focus()
          this.questionInProgress = true
          this.$refs.GeneralLearningWR.generateQuestion()
          break
        case 2:
        // Word creator
          this.$refs.GeneralLearningWC.$el.focus()
          this.disableOptions = false
          this.$refs.GeneralLearningWC.setNewCreation()
          break
      }
      console.log('called randomizeNextQuestion in GL')
    },
    enterSolutionWR () {
      this.questionInProgress = false
      this.$refs.GeneralLearningWR.validateSolution()
    },
    enterSolutionWC () {
      this.disableOptions = true
      this.$refs.GeneralLearningWC.endCreation()
    }
  }
}
/**
<q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
<q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Learning)</div>
        </q-card-section>
        <q-card-section>
        Use <strong>Learning</strong> to combine <strong>Multiple Choice Quiz</strong>, <strong>Word Creator</strong>, and <strong>Word Reader</strong> into a single learning page by randomly looping between them. For details on each game, go to their respective pages under <strong>Learning Tools</strong> and view their tutorials.
        <br/>
        <br/>
        <strong>Keyboard Shortcuts: </strong>You can comfortably dash through the games by using keyboard only. Keyboard shortcuts will work once you hit <strong>Enter</strong> on the keyboard after typing a word in <strong>Word Reader</strong> and deactivate once you use the mouse to click any buttons.
        <br/><br/>
        <strong>Tip:</strong> To highlight the parts of manyougana katakana were derived from, you can toggle <strong>Highlight Manyougana</strong> at any time. The changes will be visible on the next question.
        <br/><br/>
        </q-card-section>
      </q-card>
    </q-dialog>
**/
</script>

<style>
</style>
