<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 800px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
      &nbsp;
      <strong style="font-size: 120%;">Multiple Choice ({{numberQuestionsAnswered}}/{{quizLength}})</strong>
      <!-- parameters panel -->
      <span class="row">
        <!-- script selection -->
        <span>
          <q-select v-model="script1" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana']" label="Script1" style="width:200px;" />
        </span>
        <span>
          <q-select v-model="script2" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana']" label="Script2" style="width:200px;" />
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
        <character-flashcard id="multiple-choice-question" :imgSrc="questionImage" />
        <span v-if="!hasAnsweredQuestion" style="position:relative; top:68px; left:30px;">What is this {{script1}}'s equivalent in {{script2}}?</span>
        <span v-if="hasAnsweredQuestion" style="padding:30px;"><strong>Feedback: {{feedbackMessage}}</strong></span>
      </span>
      <!-- answers (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;">
        <span>
          <character-flashcard :imgSrc="option1Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-1" label="Option 1" style="top:5px; width:148px;" @click="validateOption" :disabled="validationInProgress" />
        </span>
        <span>
          <character-flashcard :imgSrc="option2Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-2" label="Option 2" style="top:5px; width:148px;" @click="validateOption" :disabled="validationInProgress" />
        </span>
        <span>
          <character-flashcard :imgSrc="option3Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-3" label="Option 3" style="top:5px; width:148px;" @click="validateOption" :disabled="validationInProgress" />
        </span>
        <span>
          <character-flashcard :imgSrc="option4Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-4" label="Option 4" style="top:5px; width:148px;" @click="validateOption" :disabled="validationInProgress" />
        </span>
      </span>
    </q-card>
  </q-page>
</template>

<script>
import hentaigana from '../statics/svg/hentaigana.json'
import hiragana from '../statics/svg/hiragana.json'
import katakana from '../statics/svg/katakana.json'
import manyouganaKatakana from '../statics/svg/manyougana-katakana.json'
import CharacterFlashcard from '../components/CharacterFlashcard.vue'

export default {
  // name: 'PageName',
  components: {
    CharacterFlashcard
  },
  data () {
    return {
      // Boolean process and button display controllors
      quizHasStarted: false,
      hasAnsweredQuestion: false,
      validationInProgress: false,
      // script-related
      script1: 'katakana',
      script2: 'manyougana-katakana',
      currentKey: '',
      // convert script to its number code as used in script-to-script maps
      scriptIndex: { 'hentaigana': '1',
        'hiragana': '2',
        'katakana': '3',
        'manyougana-katakana': '5' },
      // quiz controllers
      quizLength: 3,
      numberQuestionsAnswered: 0,
      questionsAnsweredCorrectly: 0,
      correctAnswer: -1,
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
  created () {
    this.$root.$on('receiveUserObj', this.receiveUserObj)
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
          if (!this.validationInProgress) {
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
    Return the correct database given a script
    **/
    scriptToData (script) {
      var database = {}
      if (script === 'hentaigana') {
        database = hentaigana
      } else if (script === 'hiragana') {
        database = hiragana
      } else if (script === 'katakana') {
        database = katakana
      } else if (script === 'manyougana-katakana') {
        database = manyouganaKatakana
      } else {
        alert('invalid script input')
        database = undefined
      }
      return database
    },
    /**
    Get an array of svg image paths of given letter and script
    **/
    getLetters (letter, script) {
      console.log('called getLetters(' + letter + ', ' + script + ') from MultipleChoice')
      var suffixes = this.scriptToData(script)[letter] // get suffixes of given letter and script
      var paths = []
      // construct an svg image path from each suffix
      suffixes.forEach(suffix => paths.push('../statics/svg/' + script + '/' + script + '_letter_' + letter + suffix + '.svg'))
      return paths
    },
    /**
    Randomly generate an option (get image letter paths) which must not be forbiddenLetter but of given script
    **/
    generateOption (forbiddenLetter, script) {
      console.log('called generateOption(' + forbiddenLetter + ', ' + script + ') from MultipleChoice')
      // dataset and its keys
      var dataset = this.scriptToData(script)
      var datasetKeys = Object.keys(dataset)
      // initialize loop
      var randomKey = ''
      var isSameKey = true
      // loop until randomKey != forbiddenLetter; never gets randomKey which is forbiddenLetter
      while (isSameKey) {
        var randomIndex = Math.floor(Math.random() * datasetKeys.length)
        randomKey = datasetKeys[randomIndex]
        isSameKey = (randomKey === forbiddenLetter) // is the randomKey we get the forbiddenLetter
      }
      return this.getLetters(randomKey, script) // get an option not the forbiddenLetter above but of given script
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
      var databaseKeys = Object.keys(database).filter(key1 => regex.test(key1))
      console.log('logging filtered keys in MultipleChoice: ' + databaseKeys + ', length: ' + databaseKeys.length)
      // initialize key selection loop (1)
      var priorities = {}
      var sumPriorities = 0
      // calculate priority for each key
      databaseKeys.forEach(function (key2) {
        var entry = database[key2] // entry := [_,_,mastery,time_last_seen]
        var diff = d - entry[3] // how long ago it is a question with given letter of mapping s1s2 has been asked
        var priority = diff / (entry[2] ** 2) // priority as diff scaled by quadratically significant mastery
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
      this.questionImage = this.getLetters(this.currentKey, this.script1)[0]
      // generate options of target script2 which is NOT equal to the letter passed as randomKey
      this.option1Image = this.generateOption(this.currentKey, this.script2)[0]
      this.option2Image = this.generateOption(this.currentKey, this.script2)[0]
      this.option3Image = this.generateOption(this.currentKey, this.script2)[0]
      this.option4Image = this.generateOption(this.currentKey, this.script2)[0]
      this.correctAnswer = Math.floor(Math.random() * 4) // let correct answer be one of 0,1,2,3
      // replace one of the options (all incorrect) with correct answer
      switch (this.correctAnswer) {
        case 0:
          this.option1Image = this.getLetters(this.currentKey, this.script2)[0]
          break
        case 1:
          this.option2Image = this.getLetters(this.currentKey, this.script2)[0]
          break
        case 2:
          this.option3Image = this.getLetters(this.currentKey, this.script2)[0]
          break
        case 3:
          this.option4Image = this.getLetters(this.currentKey, this.script2)[0]
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
      var userAnswer
      if (event.target !== undefined) {
        userAnswer = parseInt(event.target.id.split('-')[4]) - 1 // from button
      } else {
        userAnswer = parseInt(event) - 1 // from keyboard
      }
      console.log('userAnswer: ' + userAnswer)
      console.log('correctAnswer: ' + this.correctAnswer)
      // display feedback,
      // adjust quiz controls, and
      // log progress in user tracking (to affect future questions in spaced repetition)
      // depending on answer
      if (userAnswer === this.correctAnswer) {
        this.feedbackMessage = 'Your answer (Option ' + (userAnswer + 1) + ') was correct. Great job!'
        this.questionsAnsweredCorrectly += 1
        // reward with exp (perhaps level-ups)
        this.$root.$emit('addExp', 1)
        this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 1)
      } else {
        this.feedbackMessage = 'Your answer (Option ' + (userAnswer + 1) + ') was incorrect. Correct answer: Option ' + (this.correctAnswer + 1) + '.'
        this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 0)
      }
      this.numberQuestionsAnswered += 1
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
