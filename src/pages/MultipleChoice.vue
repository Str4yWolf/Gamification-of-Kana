<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 800px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="goUp()" />
      &nbsp;
      <strong style="font-size: 120%;">Multiple Choice ({{questionsAnswered}}/{{quizLength}})</strong>
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
import userTracking from '../statics/svg/user_tracking.json'

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
      questionsAnswered: 0,
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
  mounted () {
    this.$refs.modal.$el.focus()
  },
  methods: {
    validateKeyInput (event) {
      switch (event.keyCode) {
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
        case 13:
          console.log('pressed enter in validateKeyInput')
          if (this.hasAnsweredQuestion) {
            this.continueQuiz()
          }
          break
        default:
          console.log('called validateKeyInput with key')
          console.log(event.key)
          console.log('and keyCode')
          console.log(event.keyCode)
      }
    },
    getLetters (letter, script) {
      console.log('called getLetters(' + letter + ', ' + script + ') from MultipleChoice')
      var suffixes = []
      if (script === 'hentaigana') {
        suffixes = hentaigana[letter]
      } else if (script === 'hiragana') {
        suffixes = hiragana[letter]
      } else if (script === 'katakana') {
        suffixes = katakana[letter]
      } else if (script === 'manyougana-katakana') {
        suffixes = manyouganaKatakana[letter]
      } else {
        alert('invalid script input')
        return undefined
      }
      var paths = []
      suffixes.forEach(suffix => paths.push('../statics/svg/' + script + '/' + script + '_letter_' + letter + suffix + '.svg'))
      return paths
    },
    generateOption (letter, script) {
      console.log('called generateOption(' + letter + ', ' + script + ') from MultipleChoice')
      var dataset = {}
      if (script === 'hentaigana') {
        dataset = hentaigana
      } else if (script === 'hiragana') {
        dataset = hiragana
      } else if (script === 'katakana') {
        dataset = katakana
      } else if (script === 'manyougana-katakana') {
        dataset = manyouganaKatakana
      } else {
        alert('invalid script input')
        return undefined
      }
      var key = ''
      var sameKey = true
      // loop until key != letter; never gets key which is letter
      while (sameKey) {
        var keys = Object.keys(dataset)
        var randomIndex = Math.floor(Math.random() * keys.length)
        key = keys[randomIndex]
        sameKey = (key === letter)
      }
      return this.getLetters(key, script)
    },
    continueQuiz () {
      if (this.questionsAnswered === this.quizLength) {
        return this.endQuiz()
      }
      this.quizHasStarted = true
      this.hasAnsweredQuestion = false
      this.validationInProgress = false
      /**
      var dataset = {}
      if (this.script1 === 'hentaigana') {
        dataset = hentaigana
      } else if (this.script1 === 'hiragana') {
        dataset = hiragana
      } else if (this.script1 === 'katakana') {
        dataset = katakana
      } else if (this.script1 === 'manyougana-katakana') {
        dataset = manyouganaKatakana
      } else {
        alert('invalid script input')
        return undefined
      }
      **/
      // var keys = Object.keys(dataset)
      // var randomIndex = Math.floor(Math.random() * keys.length)
      // var key = keys[randomIndex]
      var d = Date.now()
      var regex = new RegExp('_' + this.scriptIndex[this.script1] + this.scriptIndex[this.script2] + '$')
      var keys = Object.keys(userTracking).filter(akey => regex.test(akey))
      console.log('logging filtered keys in MultipleChoice: ' + keys + ', length: ' + keys.length)
      var priorities = {}
      // need to use userTracking filtered by keys with suffix _s1s2
      var sumPriorities = 0
      keys.forEach(function (el) {
        var entry = userTracking[el]
        var diff = d - entry[3] // how long ago it is a letter of mapping s1s2 has been asked
        var priority = diff / (entry[2] ** 2)
        priorities[el] = priority
        sumPriorities += priority
      })
      // keys.forEach(function (el) {
      //   priorities[el] /= sumPriorities
      // })
      var randomThreshold = Math.floor(Math.random() * sumPriorities)
      var key = ''
      var counter = 0
      for (var el in priorities) {
        counter += priorities[el]
        if (counter >= randomThreshold) {
          key = el
          break
        }
      }
      console.log('sumPriorities: ' + sumPriorities)
      console.log('randomThreshold: ' + randomThreshold)
      console.log('counter: ' + counter)
      key = key.substring(0, key.length - 3)
      console.log('key: ' + key)
      Object.keys(priorities).forEach(function (p) {
        console.log('priority of ' + p + ': ' + priorities[p])
      })
      // need to sort by priorty, assign probability accordingly, and sample according to probabilities
      this.questionImage = this.getLetters(key, this.script1)[0]
      this.currentKey = key
      // generate an option of script2 which is NOT equal to the letter passed as argument key
      this.option1Image = this.generateOption(key, this.script2)[0]
      this.option2Image = this.generateOption(key, this.script2)[0]
      this.option3Image = this.generateOption(key, this.script2)[0]
      this.option4Image = this.generateOption(key, this.script2)[0]
      this.correctAnswer = Math.floor(Math.random() * 4)
      switch (this.correctAnswer) {
        case 0:
          this.option1Image = this.getLetters(key, this.script2)[0]
          break
        case 1:
          this.option2Image = this.getLetters(key, this.script2)[0]
          break
        case 2:
          this.option3Image = this.getLetters(key, this.script2)[0]
          break
        case 3:
          this.option4Image = this.getLetters(key, this.script2)[0]
          break
      }
    },
    validateOption (event) {
      console.log('called validateOption from MultipleChoice')
      this.hasAnsweredQuestion = true
      this.validationInProgress = true
      var userAnswer
      if (event.target !== undefined) {
        userAnswer = parseInt(event.target.id.split('-')[4]) - 1
      } else {
        userAnswer = parseInt(event) - 1
      }
      console.log('userAnswer: ' + userAnswer)
      console.log('correctAnswer: ' + this.correctAnswer)
      if (userAnswer === this.correctAnswer) {
        this.feedbackMessage = 'Your answer (Option ' + (userAnswer + 1) + ') was correct. Great job!'
        this.questionsAnsweredCorrectly += 1
        this.$root.$emit('addExp', 1)
        this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 1)
      } else {
        this.feedbackMessage = 'Your answer (Option ' + (userAnswer + 1) + ') was incorrect. Correct answer: Option ' + (this.correctAnswer + 1) + '.'
        this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 0)
      }
      this.questionsAnswered += 1
    },
    endQuiz () {
      console.log('called endQuiz from MultipleChoice')
      this.quizHasStarted = false
      this.validationInProgress = false
      this.feedbackMessage = 'Congratulations. You have scored ' + this.questionsAnsweredCorrectly + ' out of ' + this.questionsAnswered + ' in this quiz!'
      this.questionsAnswered = 0
      this.questionsAnsweredCorrectly = 0
    },
    goUp () {
      console.log('called goUp() from Settings')
      this.$router.push('../')
    }
  }
}
</script>

<style>
</style>
