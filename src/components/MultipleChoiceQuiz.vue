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
        @input="updateHighlight()"
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
        <!-- context dependent button -->
        <span style="padding-left:10px;">
          <q-btn v-if="!quizHasStarted" color="green" label="Start" @click="continueQuiz()" />
          <q-btn v-if="validationInProgress" color="green" label="Continue" @click="continueQuiz()" />
        </span>
      </span>
      <!-- question -->
      <span class="row" style="padding: 20px 0px 20px 50px;">
        <character-flashcard id="multiple-choice-question" :imgSrc="questionImage" :showTitle="validationInProgress" />
        <span v-if="!hasAnsweredQuestion" style="position:relative; top:68px; left:30px;">What is this {{script1}}'s equivalent in {{script2}}?</span>
        <span v-if="hasAnsweredQuestion" style="padding:30px;"><strong>Feedback: {{feedbackMessage}}</strong></span>
      </span>
      <!-- answers (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;">
        <span>
          <character-flashcard :imgSrc="option1Image" :showTitle="validationInProgress" :background="option1ImageBackground" />
          <q-btn color="primary" id="multiple-choice-option-btn-1" label="Option 1" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
        <span>
          <character-flashcard :imgSrc="option2Image" :showTitle="validationInProgress" :background="option2ImageBackground" />
          <q-btn color="primary" id="multiple-choice-option-btn-2" label="Option 2" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
        <span>
          <character-flashcard :imgSrc="option3Image" :showTitle="validationInProgress" :background="option3ImageBackground" />
          <q-btn color="primary" id="multiple-choice-option-btn-3" label="Option 3" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
        <span>
          <character-flashcard :imgSrc="option4Image" :showTitle="validationInProgress" :background="option4ImageBackground" />
          <q-btn color="primary" id="multiple-choice-option-btn-4" label="Option 4" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
      </span>
    <letter-operations :highlight="highlightManyougana" :skillLevel="userObj['skillLvl']" ref="MCQOps" />
    </q-card>
  </q-page>
</template>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import LetterOperations from '../components/LetterOperations.vue'
import skillLevelDatabaseKeys from '../statics/svg/skill_level_database_keys.json'

export default {
  // name: 'PageName',
  components: {
    CharacterFlashcard,
    LetterOperations
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
      currentKey: '',
      // convert script to its number code as used in script-to-script maps
      scriptIndex: { 'hentaigana': '1',
        'hiragana': '2',
        'katakana': '3',
        'manyougana-katakana': '5',
        'manyougana-katakana-c': '5' },
      // quiz controllers
      quizLength: 3,
      numberQuestionsAnswered: 0,
      questionsAnsweredCorrectly: 0,
      correctAnswer: -1,
      userAnswer: -1,
      // user feedback after each time answered
      feedbackMessage: '',
      // image paths
      questionImage: '',
      option1Image: '',
      option2Image: '',
      option3Image: '',
      option4Image: ''
    }
  },
  props: {
    userObj: Object
  },
  mounted () {
    this.$refs.modal.$el.focus()
  },
  computed: {
    disableOptions () {
      return (!this.quizHasStarted || this.validationInProgress)
    },
    option1ImageBackground () {
      if (this.correctAnswer === 0 && this.disableOptions) {
        return 'background-color: #d1fb9c;'
      } else if (this.userAnswer === 0 && this.disableOptions) {
        return 'background-color: #fbad9c;'
      } else {
        return 'background-color: #ffffff'
      }
    },
    option2ImageBackground () {
      if (this.correctAnswer === 1 && this.disableOptions) {
        return 'background-color: #d1fb9c;'
      } else if (this.userAnswer === 1 && this.disableOptions) {
        return 'background-color: #fbad9c;'
      } else {
        return 'background-color: #ffffff'
      }
    },
    option3ImageBackground () {
      if (this.correctAnswer === 2 && this.disableOptions) {
        return 'background-color: #d1fb9c;'
      } else if (this.userAnswer === 2 && this.disableOptions) {
        return 'background-color: #fbad9c;'
      } else {
        return 'background-color: #ffffff'
      }
    },
    option4ImageBackground () {
      if (this.correctAnswer === 3 && this.disableOptions) {
        return 'background-color: #d1fb9c;'
      } else if (this.userAnswer === 3 && this.disableOptions) {
        return 'background-color: #fbad9c;'
      } else {
        return 'background-color: #ffffff'
      }
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
          if (!this.disableOptions) {
            console.log('called validateKeyInput with 1-4')
            this.validateOption(event.keyCode - 48)
          } else {
            console.log('Validation is in progress. Options unusable.')
          }
          break
        // keyboard Enter key
        case 13:
          console.log('pressed enter in validateKeyInput')
          if (this.hasAnsweredQuestion) {
            this.continueQuiz()
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
    /**
    Get the letter of an image path
    **/
    getLetterFromPath (path) {
      console.log('called getLetterFromPath(' + path + ')')
      var temp = path.split('/').reverse()[0].split('_letter_')[1].split('.')[0]
      console.log('temp: ' + temp)
      if (temp.length === 1) {
        return temp
      } else {
        return temp.substring(0, 2) // crop numeral suffix if it exists
      }
    },
    /**
    Highlight or unhighlight the image according to the highlightManyougana state
    **/
    updateHighlight () {
      console.log('called updateHighlight() from MultipleChoiceQuiz')
      this.$refs.MCQOps.toggleHighlight()
      if (this.script1 === 'manyougana-katakana') {
        this.questionImage = this.$refs.MCQOps.getLetters(this.currentKey, 'manyougana-katakana')[0]
      } else {
        console.log(this.option1Image)
        console.log(this.getLetterFromPath(this.option1Image))
        this.option1Image = this.$refs.MCQOps.getLetters(this.getLetterFromPath(this.option1Image), 'manyougana-katakana')[0]
        console.log(this.option1Image)
        this.option2Image = this.$refs.MCQOps.getLetters(this.getLetterFromPath(this.option2Image), 'manyougana-katakana')[0]
        this.option3Image = this.$refs.MCQOps.getLetters(this.getLetterFromPath(this.option3Image), 'manyougana-katakana')[0]
        this.option4Image = this.$refs.MCQOps.getLetters(this.getLetterFromPath(this.option4Image), 'manyougana-katakana')[0]
      }
    },
    /**
      sets a random new currentKey while taking the past user progress into account
       (spaced repetition with emphasis on less mastered questions)
    **/
    randomizeCurrentKey () {
      console.log('called randomizeCurrentKey() in MultipleChoice')
      var d = Date.now() // current time stamp
      // generate regular expression to filter letters of correct script mapping (ending on _s1s2)
      var regex = new RegExp('_' + this.scriptIndex[this.script1] + this.scriptIndex[this.script2] + '$')
      // filter keys by given script mapping
      var database = this.userObj.tracking
      var databaseKeysRaw = Object.keys(database).filter(key1 => regex.test(key1))
      // filter according to skill level
      var skillLvlKeys = skillLevelDatabaseKeys[this.userObj.skillLvl]
      var databaseKeys = []
      databaseKeysRaw.forEach(function (k) {
        if (skillLvlKeys.includes(k.split('_')[0])) {
          databaseKeys.push(k)
        }
      })
      console.log('logging filtered keys in MultipleChoice: ' + databaseKeys + ', length: ' + databaseKeys.length)
      // initialize key selection loop (1)
      var priorities = {}
      var sumPriorities = 0
      // calculate priority for each key
      databaseKeys.forEach(function (key2) {
        var entry = database[key2] // entry := [_,_,mastery,time_last_seen]
        var diff = d - entry[3] // how long ago it is a question with given letter of mapping s1s2 has been asked
        // try to optimize power term somehow
        var priority = diff / (entry[2] ** 1.7) // priority as diff scaled by power-fold significant mastery
        priorities[key2] = priority // key: priority map
        sumPriorities += priority
      })
      // initialize key selection loop (2)
      var randomThreshold = Math.floor(Math.random() * sumPriorities)
      var randomKey = ''
      var currentSum = 0
      // loop until threshold has been reached; randomly select key proportional to the priorities (unnormalized distribution)
      for (var key3 in priorities) {
        currentSum += priorities[key3]
        if (currentSum >= randomThreshold) {
          randomKey = key3.substring(0, key3.length - 3) // select key and remove script mapping suffix
          break
        }
      }
      this.currentKey = randomKey // make current key visible outside method
      // temporary logs
      console.log('sumPriorities: ' + sumPriorities)
      console.log('randomThreshold: ' + randomThreshold)
      console.log('counter: ' + currentSum)
      console.log('randomKey: ' + randomKey)
      Object.keys(priorities).forEach(function (key4) {
        console.log('priority of ' + key4 + ': ' + priorities[key4])
      })
    },
    /**
    Generate next options and display them accordingly
    **/
    continueQuiz () {
      console.log('called continueQuiz in MultipleChoice')
      console.log('current userObj: ' + JSON.stringify(this.userObj))
      // end quiz when given number of questions have been answered
      if (this.numberQuestionsAnswered === this.quizLength) {
        return this.endQuiz()
      }
      // adjust display controls
      this.quizHasStarted = true
      this.hasAnsweredQuestion = false
      this.validationInProgress = false
      // set a random new currentKey which yet employs spaced repetition and emphasis on less mastered questions
      this.randomizeCurrentKey()
      // get question image
      this.questionImage = this.$refs.MCQOps.getLetters(this.currentKey, this.script1)[0]
      // generate options of target script2 which is NOT equal to the letter passed as randomKey
      this.option1Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true)[0]
      this.option2Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true)[0]
      this.option3Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true)[0]
      this.option4Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true)[0]
      this.correctAnswer = Math.floor(Math.random() * 4) // let correct answer be one of 0,1,2,3
      // replace one of the options (all incorrect) with correct answer
      switch (this.correctAnswer) {
        case 0:
          this.option1Image = this.$refs.MCQOps.getLetters(this.currentKey, this.script2)[0]
          break
        case 1:
          this.option2Image = this.$refs.MCQOps.getLetters(this.currentKey, this.script2)[0]
          break
        case 2:
          this.option3Image = this.$refs.MCQOps.getLetters(this.currentKey, this.script2)[0]
          break
        case 3:
          this.option4Image = this.$refs.MCQOps.getLetters(this.currentKey, this.script2)[0]
          break
      }
    },
    /**
    validate option event triggered by user input
    **/
    validateOption (event) {
      console.log('called validateOption from MultipleChoice')
      // adjust controls
      this.hasAnsweredQuestion = true
      this.validationInProgress = true
      // get user answer
      if (event.target !== undefined) {
        this.userAnswer = parseInt(event.target.id.split('-')[4]) - 1 // from button
      } else {
        this.userAnswer = parseInt(event) - 1 // from keyboard
      }
      console.log('userAnswer: ' + this.userAnswer)
      console.log('correctAnswer: ' + this.correctAnswer)
      this.numberQuestionsAnswered += 1
      // display feedback,
      // adjust quiz controls, and
      // log progress in user tracking (to affect future questions in spaced repetition)
      // depending on answer
      if (this.userAnswer === this.correctAnswer) {
        this.feedbackMessage = 'Your answer (Option ' + (this.userAnswer + 1) + ') was correct. Great job!'
        this.questionsAnsweredCorrectly += 1
        // reward with exp (perhaps level-ups)
        this.$root.$emit('addExp', 1)
        this.$root.$emit('addSkillExp', 1)
        this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 1)
        this.continueQuiz()
      } else {
        this.feedbackMessage = 'Your answer (Option ' + (this.userAnswer + 1) + ') was incorrect. Correct answer: Option ' + (this.correctAnswer + 1) + '.'
        this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 0)
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
    }
  }
}
</script>

<style>
</style>
