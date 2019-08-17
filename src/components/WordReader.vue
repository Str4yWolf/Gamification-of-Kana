<template>
  <span>
      <!-- Text display -->
      <span v-if="!showFeedbackMessage"> Please type in the letters you see using Latin letters (Romaji). </span>
      <span v-if="showFeedbackMessage"><strong>Feedback: {{feedbackMessage}}</strong></span>
      <br />
      <!-- slots (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;">
        <span>
          <character-flashcard :imgSrc="slot1Image" :showTitle="showFeedbackMessage" :background="bg1" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot2Image" :showTitle="showFeedbackMessage" :background="bg2" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot3Image" :showTitle="showFeedbackMessage" :background="bg3" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot4Image" :showTitle="showFeedbackMessage" :background="bg4" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot5Image" :showTitle="showFeedbackMessage" :background="bg5" />
        </span>
      </span>
      <q-input v-model="userSolution" label="Enter solution" v-on:keyup.enter="validateSolution()" style="margin: 2px;">
        <template v-slot:append>
          <q-btn round dense flat icon="send" @click="validateSolution()" />
        </template>
      </q-input>
    <letter-operations :highlight="false" :skillLevel="userObj['skillLvl']" ref="WROps" />
  </span>
</template>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import words from '../statics/wordCreatorWords.json'
import LetterOperations from '../components/LetterOperations.vue'

export default {
  // name: 'PageName',
  components: {
    CharacterFlashcard,
    LetterOperations
  },
  data () {
    return {
      // current params
      currentWordEng: 'wolf',
      userSolution: '',
      // feedback message
      showFeedbackMessage: false,
      feedbackMessage: '',
      // slot images
      slot1Image: '',
      slot2Image: '',
      slot3Image: '',
      slot4Image: '',
      slot5Image: '',
      // backgrounds
      bg1: 'background: #ffffff;',
      bg2: 'background: #ffffff;',
      bg3: 'background: #ffffff;',
      bg4: 'background: #ffffff;',
      bg5: 'background: #ffffff;'
    }
  },
  props: {
    userObj: Object,
    script: String
  },
  created () {
  },
  computed: {
    currentWordJap () {
      return words[this.currentWordEng]
    },
    currentWordLength () {
      return this.currentWordJap.length
    },
    currentSolution () {
      return this.assembleWord(this.currentWordJap)
    },
    disableOptions () {
      return this.showFeedbackMessage
    }
  },
  methods: {
    getRandomWord (getKey) {
      var wordsKeys = Object.keys(words)
      var randomIndex = Math.floor(Math.random() * wordsKeys.length)
      var randomKey = wordsKeys[randomIndex]
      if (getKey) {
        return randomKey
      } else {
        return words[randomKey]
      }
    },
    setRandomWord () {
      this.currentWordEng = this.getRandomWord(true)
      while (this.currentWordLength > 5) {
        this.currentWordEng = this.getRandomWord(true)
      }
    },
    assembleWord (wordObject) {
      var output = ''
      for (var i = 0; i < this.currentWordLength; i++) {
        output = output += wordObject[i]
      }
      return output
    },
    setBackgrounds (color) {
      this.bg1 = 'background-color: ' + color + ';'
      this.bg2 = 'background-color: ' + color + ';'
      this.bg3 = 'background-color: ' + color + ';'
      this.bg4 = 'background-color: ' + color + ';'
      this.bg5 = 'background-color: ' + color + ';'
    },
    generateQuestion () {
      this.feedbackMessage = ''
      this.showFeedbackMessage = false
      this.userSolution = ''
      this.setBackgrounds('#ffffff')
      this.setRandomWord()
      if (this.currentWordLength > 0) {
        this.slot1Image = this.$refs.WROps.getLetters(this.currentWordJap[0], this.script)[0]
      } else {
        this.slot1Image = '../statics/grey.png'
      }
      if (this.currentWordLength > 1) {
        this.slot2Image = this.$refs.WROps.getLetters(this.currentWordJap[1], this.script)[0]
      } else {
        this.slot2Image = '../statics/grey.png'
      }
      if (this.currentWordLength > 2) {
        this.slot3Image = this.$refs.WROps.getLetters(this.currentWordJap[2], this.script)[0]
      } else {
        this.slot3Image = '../statics/grey.png'
      }
      if (this.currentWordLength > 3) {
        this.slot4Image = this.$refs.WROps.getLetters(this.currentWordJap[3], this.script)[0]
      } else {
        this.slot4Image = '../statics/grey.png'
      }
      if (this.currentWordLength > 4) {
        this.slot5Image = this.$refs.WROps.getLetters(this.currentWordJap[4], this.script)[0]
      } else {
        this.slot5Image = '../statics/grey.png'
      }
    },
    /**
    validate option event triggered by user input
    **/
    validateSolution () {
      console.log('called validateOption from WordReader')
      if (this.showFeedbackMessage) {
        return
      }
      if (this.userSolution === this.currentSolution) {
        this.feedbackMessage = 'Your answer (' + this.userSolution + ') was correct.'
        this.setBackgrounds('#d1fb9c')
        this.$root.$emit('addExp', this.currentWordLength)
      } else {
        this.feedbackMessage = 'Your answer (' + this.userSolution + ') was incorrect. Correct answer: ' + this.currentSolution
        this.setBackgrounds('#fbad9c')
      }
      this.showFeedbackMessage = true
    }
  }
}
</script>

<style>
</style>