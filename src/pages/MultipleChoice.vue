<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 800px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="goUp()" />
      &nbsp;
      <strong style="font-size: 120%;">Multiple Choice ({{questionsAnswered}}/{{questions}})</strong>
      <!-- parameters panel -->
      <span class="row">
        <span>
          <q-select v-model="script1" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana']" label="Script1" style="width:200px;" />
        </span>
        <span>
          <q-select v-model="script2" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana']" label="Script2" style="width:200px;" />
        </span>
        <span style="padding:10px;">
          <strong>Questions: </strong>
        </span>
        <span>
          <q-slider
            v-model="questions"
            :min="3"
            :max="20"
            :step="1"
            label-always
            color="light-green"
            style="width: 120px;"
          />
        </span>
        <span style="padding-left:10px;">
          <q-btn v-if="!started" color="green" label="Start" @click="continueQuiz()" />
          <q-btn v-if="continued" color="green" label="Continue" @click="continueQuiz()" />
        </span>
      </span>
      <!-- question -->
      <span class="row" style="padding: 20px 0px 20px 50px;">
        <character-flashcard id="multiple-choice-question" :imgSrc="questionImage" />
        <span v-if="!answered" style="position:relative; top:68px; left:30px;">What is this {{script1}}'s equivalent in {{script2}}?</span>
        <span v-if="answered" style="padding:30px;"><strong>Feedback: {{feedbackMessage}}</strong></span>
      </span>
      <!-- answers (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;">
        <span>
          <character-flashcard :imgSrc="option1Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-1" label="Option 1" style="top:5px; width:148px;" @click="validateOption" />
        </span>
        <span>
          <character-flashcard :imgSrc="option2Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-2" label="Option 2" style="top:5px; width:148px;" @click="validateOption" />
        </span>
        <span>
          <character-flashcard :imgSrc="option3Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-3" label="Option 3" style="top:5px; width:148px;" @click="validateOption" />
        </span>
        <span>
          <character-flashcard :imgSrc="option4Image" />
          <q-btn color="primary" id="multiple-choice-option-btn-4" label="Option 4" style="top:5px; width:148px;" @click="validateOption" />
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
      started: false,
      script1: 'katakana',
      script2: 'manyougana-katakana',
      scriptIndex: { 'hentaigana': '1',
        'hiragana': '2',
        'katakana': '3',
        'manyougana-katakana': '5' },
      currentKey: '',
      questions: 3,
      questionsAnswered: 0,
      questionsAnsweredCorrectly: 0,
      correctAnswer: -1,
      answered: false,
      continued: false,
      feedbackMessage: '',
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
          console.log('called validateKeyInput with 1-4')
          this.validateOption(event.keyCode - 48)
          break
        case 13:
          console.log('pressed enter in validateKeyInput')
          if (this.answered) {
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
      while (sameKey) {
        var keys = Object.keys(dataset)
        var randomIndex = Math.floor(Math.random() * keys.length)
        key = keys[randomIndex]
        sameKey = (key === letter)
      }
      return this.getLetters(key, script)
    },
    continueQuiz () {
      if (this.questionsAnswered === this.questions) {
        return this.endQuiz()
      }
      this.started = true
      this.answered = false
      this.continued = false
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
      var keys = Object.keys(dataset)
      var randomIndex = Math.floor(Math.random() * keys.length)
      var key = keys[randomIndex]
      console.log(userTracking)
      // var d = Date.now()
      // // need to use userTracking filtered by keys with suffix _s1s2
      // dataset.forEach(function(el)) {
      //   var diff = d - el[3]
      //   var priority = diff / (el[2] ** 2)
      // }
      // need to sort by priorty, assign probability accordingly, and sample according to probabilities
      this.questionImage = this.getLetters(key, this.script1)[0]
      this.currentKey = key
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
      this.answered = true
      this.continued = true
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
      this.started = false
      this.continued = false
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
