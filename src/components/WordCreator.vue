<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 820px; padding: 30px;">
      <span class="row">
        <span>
          <!-- header -->
          <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideWordCreator')" />
          &nbsp;
          <strong style="font-size: 120%;">Word Creator</strong>
        </span>
        <!-- script selection -->
        <span style="padding: 0px 20px 0px 40px;">
          <q-select v-model="script" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script" style="width:200px;" />
        </span>
        <!-- Control buttons -->
        <span style="padding: 15px;">
          <q-btn color="green" label="New Word" title="Get a new word (n)" @click="setNewCreation()" />
          <q-btn color="green" label="Enter" title="Enter answers (Enter)" @click="endCreation()" :disabled="showFeedbackMessage" />
          <q-btn color="green" label="Show Japanese" title="Show Japanese word (j)" @click="showJapanese()" :disabled="showFeedbackMessage" />
        </span>
      </span>
      <br />
      <!-- Text display -->
      <span v-if="!showFeedbackMessage"> Please spell {{currentWordEng}} in Japanese {{japaneseTip}}using {{script}}. </span>
      <span v-if="showFeedbackMessage"><strong>Feedback: {{feedbackMessage}}</strong></span>
      <br />
      <!-- slots (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;">
        <span>
          <character-flashcard :imgSrc="slot1Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot2Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot3Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot4Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot5Image" :showTitle="showFeedbackMessage" />
        </span>
      </span>
      <!-- actual answer slots (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;" v-if="showFeedbackMessage">
        <span>
          <character-flashcard :imgSrc="answer1Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="answer2Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="answer3Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="answer4Image" :showTitle="showFeedbackMessage" />
        </span>
        <span>
          <character-flashcard :imgSrc="answer5Image" :showTitle="showFeedbackMessage" />
        </span>
      </span>
      <!-- answers (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;" v-if="!showFeedbackMessage">
        <span>
          <character-flashcard :imgSrc="option1Image" :showTitle="showFeedbackMessage" />
          <q-btn color="primary" id="multiple-choice-option-btn-1" label="Option 1" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
        <span>
          <character-flashcard :imgSrc="option2Image" :showTitle="showFeedbackMessage" />
          <q-btn color="primary" id="multiple-choice-option-btn-2" label="Option 2" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
        <span>
          <character-flashcard :imgSrc="option3Image" :showTitle="showFeedbackMessage" />
          <q-btn color="primary" id="multiple-choice-option-btn-3" label="Option 3" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
        <span>
          <character-flashcard :imgSrc="option4Image" :showTitle="showFeedbackMessage" />
          <q-btn color="primary" id="multiple-choice-option-btn-4" label="Option 4" style="top:5px; width:148px;" @click="validateOption" :disabled="disableOptions" />
        </span>
      </span>
    </q-card>
    <letter-operations :highlight="false" :skillLevel="userObj['skillLvl']" ref="WCOps" />
  </q-page>
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
      script: 'katakana',
      currentWordEng: 'wolf',
      // control params
      currentIndex: 0,
      correctAnswer: 0,
      userAnswer: 0,
      // history log
      correctWordIndices: {},
      userAnswerIndices: {},
      // feedback message
      showFeedbackMessage: false,
      feedbackMessage: '',
      japaneseTip: '',
      // slot images
      slot1Image: '',
      slot2Image: '',
      slot3Image: '',
      slot4Image: '',
      slot5Image: '',
      // answer images
      answer1Image: '',
      answer2Image: '',
      answer3Image: '',
      answer4Image: '',
      answer5Image: '',
      // option images
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
  },
  mounted () {
    this.$refs.modal.$el.focus()
  },
  computed: {
    currentWordJap () {
      return words[this.currentWordEng]
    },
    currentLetter () {
      if (this.currentIndex >= this.currentWordLength) {
        return this.$refs.WCOps.getRandomLetter(this.script, 0)
      } else {
        return this.currentWordJap[this.currentIndex]
      }
    },
    currentWordLength () {
      return this.currentWordJap.length
    },
    disableOptions () {
      return this.showFeedbackMessage
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
          if (!this.showFeedbackMessage) {
            this.endCreation()
          }
          break
        // show tip
        case 74:
          console.log('pressed j in validateKeyInput')
          if (!this.showFeedbackMessage) {
            this.showJapanese()
          }
          break
        // new word
        case 78:
          console.log('pressed n in validateKeyInput')
          this.setNewCreation()
          break
        // log all other keys
        default:
          console.log('called validateKeyInput with key')
          console.log(event.key)
          console.log('and keyCode')
          console.log(event.keyCode)
      }
    },
    isEqualLetters (obj1, obj2) {
      console.log('called isEqualLetters from WordCreator')
      var keys1 = Object.keys(obj1)
      var keys2 = Object.keys(obj2)
      console.log('keys1: ' + keys1)
      console.log('keys2: ' + keys2)
      console.log('keys1.length :' + keys1.length)
      console.log('keys2.length :' + keys2.length)
      if (keys1.length !== keys2.length) {
        return false
      }
      // all keys count from 0 upward, so the keys should be equal if they are of the same length
      for (var i = 0; i < keys1.length; i++) {
        console.log('i: ' + i)
        console.log('obj1[i]: ' + obj1[i])
        console.log('obj2[i]: ' + obj2[i])
        if (obj1[i] !== obj2[i]) {
          return false
        }
      }
      return true
    },
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
    },
    assembleWord (wordObject) {
      var output = ''
      for (var i = 0; i < this.currentWordLength; i++) {
        output = output += wordObject[i]
      }
      return output
    },
    showJapanese () {
      this.japaneseTip = '(' + this.assembleWord(this.currentWordJap) + ') '
    },
    setSlotImage () {
      var slotImage = ''
      switch (this.userAnswer) {
        case 0:
          slotImage = this.option1Image
          break
        case 1:
          slotImage = this.option2Image
          break
        case 2:
          slotImage = this.option3Image
          break
        case 3:
          slotImage = this.option4Image
          break
      }
      switch (this.currentIndex) {
        case 0:
          this.slot1Image = slotImage
          break
        case 1:
          this.slot2Image = slotImage
          break
        case 2:
          this.slot3Image = slotImage
          break
        case 3:
          this.slot4Image = slotImage
          break
        case 4:
          this.slot5Image = slotImage
          break
      }
    },
    setAnswerImages () {
      var tempImage = ''
      var tempLetter = ''
      for (var i = 0; i < this.currentWordLength; i++) {
        tempLetter = this.currentWordJap[i]
        tempImage = this.$refs.WCOps.getLetters(tempLetter, this.script)[0]
        switch (i) {
          case 0:
            this.answer1Image = tempImage
            break
          case 1:
            this.answer2Image = tempImage
            break
          case 2:
            this.answer3Image = tempImage
            break
          case 3:
            this.answer4Image = tempImage
            break
          case 4:
            this.answer5Image = tempImage
            break
        }
      }
    },
    resetImageSlots () {
      this.slot1Image = ''
      this.slot2Image = ''
      this.slot3Image = ''
      this.slot4Image = ''
      this.slot5Image = ''
      this.answer1Image = ''
      this.answer2Image = ''
      this.answer3Image = ''
      this.answer4I4mage = ''
      this.answer5Image = ''
    },
    setNewCreation () {
      this.currentIndex = 0
      this.correctWordIndices = {}
      this.userAnswerIndices = {}
      this.showFeedbackMessage = false
      this.japaneseTip = ''
      this.resetImageSlots()
      this.setRandomWord()
      this.continueCreation()
    },
    continueCreation () {
      this.option1Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true)[0]
      this.option2Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true)[0]
      this.option3Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true)[0]
      this.option4Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true)[0]
      this.correctAnswer = Math.floor(Math.random() * 4) // let correct answer be one of 0,1,2,3
      if (this.currentIndex < this.currentWordLength) {
        this.correctWordIndices[this.currentIndex] = this.correctAnswer
      }
      // replace one of the options (all incorrect) with correct answer
      switch (this.correctAnswer) {
        case 0:
          this.option1Image = this.$refs.WCOps.getLetters(this.currentLetter, this.script)[0]
          break
        case 1:
          this.option2Image = this.$refs.WCOps.getLetters(this.currentLetter, this.script)[0]
          break
        case 2:
          this.option3Image = this.$refs.WCOps.getLetters(this.currentLetter, this.script)[0]
          break
        case 3:
          this.option4Image = this.$refs.WCOps.getLetters(this.currentLetter, this.script)[0]
          break
      }
    },
    /**
    validate option event triggered by user input
    **/
    validateOption (event) {
      console.log('called validateOption from WordCreator')
      // get user answer
      if (event.target !== undefined) {
        this.userAnswer = parseInt(event.target.id.split('-')[4]) - 1 // from button
      } else {
        this.userAnswer = parseInt(event) - 1 // from keyboard
      }
      this.userAnswerIndices[this.currentIndex] = this.userAnswer
      console.log('userAnswer: ' + this.userAnswer)
      console.log('correctAnswer: ' + this.correctWordIndices[this.currentIndex])
      this.setSlotImage()
      this.currentIndex += 1
      this.continueCreation()
    },
    endCreation () {
      this.showFeedbackMessage = true
      this.setAnswerImages()
      console.log('this.userAnswerIndices: ' + Object.values(this.userAnswerIndices))
      console.log('this.correctWordIndices: ' + Object.values(this.correctWordIndices))
      if (this.isEqualLetters(this.userAnswerIndices, this.correctWordIndices)) {
        this.feedbackMessage = 'Your answer (' + this.assembleWord(this.currentWordJap) + ') was correct. Great job!'
        this.$root.$emit('addExp', this.currentWordLength)
      } else {
        this.feedbackMessage = 'Your answer was incorrect. Correct answer: ' + this.assembleWord(this.currentWordJap) + '.'
      }
    }
  }
}
</script>

<style>
</style>
