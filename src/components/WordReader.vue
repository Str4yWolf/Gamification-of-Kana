<template>
  <span>
      <!-- Text display -->
      <span v-if="!showFeedbackMessage">
        <br/>
        <br/>
        Please type the letters you see in <strong>Romaji</strong> (Latin script).
        <br/>
      </span>
      <span v-if="showFeedbackMessage">
        <span v-if="hasAnsweredCorrectly">
          <br/>
          <br/>
          Your answer (<strong style="color: blue;">{{userSolution}}</strong>) was <strong style="color: green">correct</strong>. Great Job!
          <br/>
        </span>
        <span v-if="!hasAnsweredCorrectly">
          Your answer (<strong style="color: blue;">{{userSolution}}</strong>) was <strong style="color: red">incorrect</strong>.
          <br/>
          <br/>
          <strong>
            <span style="color: green">Correct answer: </span>
            <span style="color: blue;">{{currentSolution}}</span>
          </strong>
          <br/>
        </span>
        </span>
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
    <letter-operations :highlightManyougana="highlightManyougana" :skillLevel="userObj['skillLvl']" ref="WROps" />
  </span>
</template>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import words from '../statics/wordsBySkillAll.json'
import wordsFinal from '../statics/wordsAll.json'
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
    script: String,
    highlightManyougana: Boolean,
    isFinalExam: Boolean,
    currentWordFinal: String
  },
  created () {
  },
  computed: {
    currentWordJap () {
      if (!this.isFinalExam) {
        return words[this.userObj.skillLvl][this.currentWordEng]
      } else {
        return wordsFinal[this.currentWordEng]
      }
    },
    currentWordLength () {
      return this.currentWordJap.length
    },
    currentSolution () {
      return this.assembleWord(this.currentWordJap)
    },
    disableOptions () {
      return this.showFeedbackMessage
    },
    hasAnsweredCorrectly () {
      return this.userSolution === this.currentSolution
    }
  },
  methods: {
    getRandomWord (getKey) {
      var wordsKeys = Object.keys(words[this.userObj.skillLvl])
      var randomIndex = Math.floor(Math.random() * wordsKeys.length)
      var randomKey = wordsKeys[randomIndex]
      if (getKey) {
        return randomKey
      } else {
        return words[this.userObj.skillLvl][randomKey]
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
    /**
    Highlight or unhighlight the image according to the highlightManyougana state
    **/
    updateHighlight () {
      console.log('called updateHighlight() from WordCreator')
      // this.$refs.WROps.toggleHighlight()
      if (this.script === 'manyougana-katakana') {
        this.slot1Image = this.$refs.WROps.getLetters(this.$refs.WROps.getLetterFromPath(this.slot1Image), 'manyougana-katakana')[0]
        this.slot2Image = this.$refs.WROps.getLetters(this.$refs.WROps.getLetterFromPath(this.slot2Image), 'manyougana-katakana')[0]
        this.slot3Image = this.$refs.WROps.getLetters(this.$refs.WROps.getLetterFromPath(this.slot3Image), 'manyougana-katakana')[0]
        this.slot4Image = this.$refs.WROps.getLetters(this.$refs.WROps.getLetterFromPath(this.slot4Image), 'manyougana-katakana')[0]
        this.slot5Image = this.$refs.WROps.getLetters(this.$refs.WROps.getLetterFromPath(this.slot5Image), 'manyougana-katakana')[0]
      }
    },
    generateQuestion () {
      this.feedbackMessage = ''
      this.showFeedbackMessage = false
      this.userSolution = ''
      this.setBackgrounds('#ffffff')
      if (!this.isFinalExam) {
        this.setRandomWord()
      } else {
        this.currentWordEng = this.currentWordFinal
      }
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
      this.$root.$emit('startTimer')
    },
    /**
    validate option event triggered by user input
    **/
    validateSolution () {
      console.log('called validateOption from WordReader')
      this.$root.$emit('stopTimer')
      if (this.showFeedbackMessage) {
        return
      }
      if (this.hasAnsweredCorrectly) {
        this.setBackgrounds('#d1fb9c')
        if (!this.isFinalExam) {
          this.$root.$emit('addExp', this.currentWordLength)
          this.$root.$emit('addSkillExp', Math.ceil(this.currentWordLength / 2))
        } else {
          this.$root.$emit('addExamPoints', 1, true)
        }
      } else {
        this.setBackgrounds('#fbad9c')
        if (this.isFinalExam) {
          this.$root.$emit('addExamPoints', 1, false)
        }
      }
      this.$root.$emit('incrementNumberQuestionsAnswered', 1)
      this.showFeedbackMessage = true
    }
  }
}
</script>

<style>
</style>
