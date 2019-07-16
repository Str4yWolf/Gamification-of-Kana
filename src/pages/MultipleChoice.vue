<template>
  <q-page class="flex flex-center">
    <q-card style="width: 800px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="goUp()" />
      &nbsp;
      <strong style="font-size: 120%;">Multiple Choice ({{questionsAnswered}}/{{questions}})</strong>
      <!-- parameters panel -->
      <span class="row">
        <span>
          <q-select v-model="script1" :options="['hentaigana', 'katakana', 'manyougana-katakana']" label="Script1" style="width:200px;" />
        </span>
        <span>
          <q-select v-model="script2" :options="['hentaigana', 'katakana', 'manyougana-katakana']" label="Script2" style="width:200px;" />
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
      <span class="row" style="padding: 20px 0px 20px 50px;" v-on:keyup.49="validateOption(1)"  v-on:keyup.50="validateOption(2)" v-on:keyup.51="validateOption(3)" v-on:keyup.52="validateOption(4)">
        <character-flashcard id="multiple-choice-question" />
        <span v-if="!answered" style="position:relative; top:68px; left:30px;">What is this {{script1}}'s equivalent in {{script2}}?</span>
        <span v-if="answered" style="padding:30px;"><strong>Feedback: {{feedbackMessage}}</strong></span>
      </span>
      <!-- answers (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;">
        <span>
          <character-flashcard id="multiple-choice-option-1" />
          <q-btn color="primary" id="multiple-choice-option-btn-1" label="Option 1" style="top:5px; width:148px;" @click="validateOption" />
        </span>
        <span>
          <character-flashcard id="multiple-choice-option-2" />
          <q-btn color="primary" id="multiple-choice-option-btn-2" label="Option 2" style="top:5px; width:148px;" @click="validateOption" />
        </span>
        <span>
          <character-flashcard id="multiple-choice-option-3" />
          <q-btn color="primary" id="multiple-choice-option-btn-3" label="Option 3" style="top:5px; width:148px;" @click="validateOption" />
        </span>
        <span>
          <character-flashcard id="multiple-choice-option-4" />
          <q-btn color="primary" id="multiple-choice-option-btn-4" label="Option 4" style="top:5px; width:148px;" @click="validateOption" />
        </span>
      </span>
    </q-card>
  </q-page>
</template>

<script>
import hentaigana from '../statics/svg/hentaigana.json'
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
      started: false,
      script1: 'katakana',
      script2: 'manyougana-katakana',
      questions: 3,
      questionsAnswered: 0,
      questionsAnsweredCorrectly: 0,
      correctAnswer: -1,
      answered: false,
      continued: false,
      feedbackMessage: ''
    }
  },
  methods: {
    getLetters (letter, script) {
      console.log('called getLetters(' + letter + ', ' + script + ') from MultipleChoice')
      var suffixes = []
      if (script === 'hentaigana') {
        suffixes = hentaigana[letter]
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
      var question = this.getLetters(key, this.script1)[0]
      var option1 = this.generateOption(key, this.script2)[0]
      var option2 = this.generateOption(key, this.script2)[0]
      var option3 = this.generateOption(key, this.script2)[0]
      var option4 = this.generateOption(key, this.script2)[0]
      this.correctAnswer = Math.floor(Math.random() * 4)
      switch (this.correctAnswer) {
        case 0:
          option1 = this.getLetters(key, this.script2)[0]
          break
        case 1:
          option2 = this.getLetters(key, this.script2)[0]
          break
        case 2:
          option3 = this.getLetters(key, this.script2)[0]
          break
        case 3:
          option4 = this.getLetters(key, this.script2)[0]
          break
      }
      this.$root.$emit('updateView2', question, 'multiple-choice-question')
      this.$root.$emit('updateView2', option1, 'multiple-choice-option-1')
      this.$root.$emit('updateView2', option2, 'multiple-choice-option-2')
      this.$root.$emit('updateView2', option3, 'multiple-choice-option-3')
      this.$root.$emit('updateView2', option4, 'multiple-choice-option-4')
      console.log(option1)
      console.log(option2)
      console.log(option3)
      console.log(option4)
    },
    validateOption (event) {
      console.log('called validateOption from MultipleChoice')
      this.answered = true
      this.continued = true
      var userAnswer = parseInt(event.target.id.split('-')[4]) - 1
      console.log('userAnswer: ' + userAnswer)
      console.log('correctAnswer: ' + this.correctAnswer)
      if (userAnswer === this.correctAnswer) {
        this.feedbackMessage = 'Your answer (Option ' + (userAnswer + 1) + ') was correct. Great job!'
        this.questionsAnsweredCorrectly += 1
      } else {
        this.feedbackMessage = 'Your answer (Option ' + (userAnswer + 1) + ') was incorrect. Correct answer: Option ' + (this.correctAnswer + 1) + '.'
      }
      this.questionsAnswered += 1
    },
    endQuiz () {
      console.log('called endQuiz from MultipleChoice')
      this.started = false
      this.continued = false
      this.feedbackMessage = 'Congratulations. You have scored ' + this.questionsAnsweredCorrectly + ' out of ' + this.questionsAnswered + ' in this quiz!'
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
