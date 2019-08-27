<template>
  <span>
      <!-- Text display -->
      <span v-if="!showFeedbackMessage"> Please spell <strong>{{currentWordEng}}</strong> in Japanese <strong>{{japaneseTip}}</strong>using {{script}}. </span>
      <span v-if="showFeedbackMessage"><strong>Feedback: {{feedbackMessage}}</strong></span>
      <br />
      <!-- slots (later: implement with v-for through array of flashcards) -->
      <span class="row" style="padding: 20px 0px 20px 0px;">
        <span>
          <character-flashcard :imgSrc="slot1Image" :showTitle="showFeedbackMessage" :background="slot1ImageBackground" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot2Image" :showTitle="showFeedbackMessage" :background="slot2ImageBackground" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot3Image" :showTitle="showFeedbackMessage" :background="slot3ImageBackground" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot4Image" :showTitle="showFeedbackMessage" :background="slot4ImageBackground" />
        </span>
        <span>
          <character-flashcard :imgSrc="slot5Image" :showTitle="showFeedbackMessage" :background="slot5ImageBackground" />
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
    <letter-operations :highlightManyougana="highlightManyougana" :skillLevel="userObj['skillLvl']" ref="WCOps" />
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
    userObj: Object,
    script: String,
    showJapanese: Boolean,
    highlightManyougana: Boolean,
    isFinalExam: Boolean,
    currentWordFinal: String
  },
  created () {
    console.log('words: ' + words[10])
    console.log('skillLvl: ' + this.userObj.skillLvl)
  },
  computed: {
    currentWordJap () {
      if (!this.isFinalExam) {
        return words[this.userObj.skillLvl][this.currentWordEng]
      } else {
        return wordsFinal[this.currentWordEng]
      }
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
    },
    slot1ImageBackground () {
      if (this.showFeedbackMessage) {
        // console.log('s1 showFeedbackMessage: true in WordCreator slot1ImageBackground')
        if (this.currentWordLength < 1) { // overstepped correct word's limit
          // console.log('s2 correctWordIndices undefined in WordCreator slot1ImageBackground')
          if (this.userAnswerIndices[0] === undefined) {
            // console.log('s3 userAnswerIndices undefined in WordCreator slot1ImageBackground (white)')
            return 'background-color: #ffffff;' // user has not entered anything
          } else {
            // console.log('s3 userAnswerIndices not undefined in WordCreator slot1ImageBackground (red)')
            return 'background-color: #fbad9c;' // user has falsely given input
          }
        } else if (this.correctWordIndices[0] === this.userAnswerIndices[0] && this.userAnswerIndices[0] !== undefined) {
          // console.log('s2 answers match up in WordCreator slot1ImageBackground (green)')
          return 'background-color: #d1fb9c;' // user input and correct word match up
        } else {
          // console.log('s2 userAnswer false or undefined WordCreator slot1ImageBackground (red)')
          return 'background-color: #fbad9c;' // user input is false or doesn't exist
        }
      } else {
        // console.log('s1 showFeedbackMessage: false in WordCreator slot1ImageBackground (white)')
        return 'background-color: #ffffff;' // no background highlighting intended
      }
    },
    slot2ImageBackground () {
      if (this.showFeedbackMessage) {
        if (this.currentWordLength < 2) { // overstepped correct word's limit
          if (this.userAnswerIndices[1] === undefined) {
            return 'background-color: #ffffff;' // user has not entered anything
          } else {
            return 'background-color: #fbad9c;' // user has falsely given input
          }
        } else if (this.correctWordIndices[1] === this.userAnswerIndices[1] && this.userAnswerIndices[1] !== undefined) {
          return 'background-color: #d1fb9c;' // user input and correct word match up
        } else {
          return 'background-color: #fbad9c;' // user input is false or doesn't exist
        }
      } else {
        return 'background-color: #ffffff;' // no background highlighting intended
      }
    },
    slot3ImageBackground () {
      if (this.showFeedbackMessage) {
        if (this.currentWordLength < 3) { // overstepped correct word's limit
          if (this.userAnswerIndices[2] === undefined) {
            return 'background-color: #ffffff;' // user has not entered anything
          } else {
            return 'background-color: #fbad9c;' // user has falsely given input
          }
        } else if (this.correctWordIndices[2] === this.userAnswerIndices[2] && this.userAnswerIndices[2] !== undefined) {
          return 'background-color: #d1fb9c;' // user input and correct word match up
        } else {
          return 'background-color: #fbad9c;' // user input is false or doesn't exist
        }
      } else {
        return 'background-color: #ffffff;' // no background highlighting intended
      }
    },
    slot4ImageBackground () {
      if (this.showFeedbackMessage) {
        if (this.currentWordLength < 4) { // overstepped correct word's limit
          if (this.userAnswerIndices[3] === undefined) {
            return 'background-color: #ffffff;' // user has not entered anything
          } else {
            return 'background-color: #fbad9c;' // user has falsely given input
          }
        } else if (this.correctWordIndices[3] === this.userAnswerIndices[3] && this.userAnswerIndices[3] !== undefined) {
          return 'background-color: #d1fb9c;' // user input and correct word match up
        } else {
          return 'background-color: #fbad9c;' // user input is false or doesn't exist
        }
      } else {
        return 'background-color: #ffffff;' // no background highlighting intended
      }
    },
    slot5ImageBackground () {
      if (this.showFeedbackMessage) {
        if (this.currentWordLength < 5) { // overstepped correct word's limit
          if (this.userAnswerIndices[4] === undefined) {
            return 'background-color: #ffffff;' // user has not entered anything
          } else {
            return 'background-color: #fbad9c;' // user has falsely given input
          }
        } else if (this.correctWordIndices[4] === this.userAnswerIndices[4] && this.userAnswerIndices[4] !== undefined) {
          return 'background-color: #d1fb9c;' // user input and correct word match up
        } else {
          return 'background-color: #fbad9c;' // user input is false or doesn't exist
        }
      } else {
        return 'background-color: #ffffff;' // no background highlighting intended
      }
    },
    japaneseTip () {
      if (this.showJapanese) {
        return '(' + this.assembleWord(this.currentWordJap) + ') '
      } else {
        return ''
      }
    }
  },
  methods: {
    isEqualLetters (obj1, obj2) {
      console.log('called isEqualLetters from WordCreator')
      var keys1 = Object.keys(obj1)
      var keys2 = Object.keys(obj2)

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
    },
    assembleWord (wordObject) {
      var output = ''
      for (var i = 0; i < this.currentWordLength; i++) {
        output = output += wordObject[i]
      }
      return output
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
      this.answer4Image = ''
      this.answer5Image = ''
    },
    /**
    Highlight or unhighlight the image according to the highlightManyougana state
    **/
    updateHighlight () {
      console.log('called updateHighlight() from WordCreator')
      this.$refs.WCOps.toggleHighlight()
      if (this.script === 'manyougana-katakana') {
        this.option1Image = this.$refs.WCOps.getLetters(this.$refs.WCOps.getLetterFromPath(this.option1Image), 'manyougana-katakana')[0]
        this.option2Image = this.$refs.WCOps.getLetters(this.$refs.WCOps.getLetterFromPath(this.option2Image), 'manyougana-katakana')[0]
        this.option3Image = this.$refs.WCOps.getLetters(this.$refs.WCOps.getLetterFromPath(this.option3Image), 'manyougana-katakana')[0]
        this.option4Image = this.$refs.WCOps.getLetters(this.$refs.WCOps.getLetterFromPath(this.option4Image), 'manyougana-katakana')[0]
        this.slot1Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.slot1Image), 'manyougana-katakana')[0]
        this.slot2Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.slot2Image), 'manyougana-katakana')[0]
        this.slot3Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.slot3Image), 'manyougana-katakana')[0]
        this.slot4Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.slot4Image), 'manyougana-katakana')[0]
        this.slot5Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.slot5Image), 'manyougana-katakana')[0]
        this.answer1Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.answer1Image), 'manyougana-katakana')[0]
        this.answer2Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.answer2Image), 'manyougana-katakana')[0]
        this.answer3Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.answer3Image), 'manyougana-katakana')[0]
        this.answer4Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.answer4Image), 'manyougana-katakana')[0]
        this.answer5Image = this.$refs.WCOPS.getLetters(this.$refs.WCOps.getLetterFromPath(this.answer5Image), 'manyougana-katakana')[0]
      }
    },
    setNewCreation () {
      console.log('Called setNewCreation() in WordCreator; current script: ' + this.script)
      this.currentIndex = 0
      this.correctWordIndices = {}
      this.userAnswerIndices = {}
      this.showFeedbackMessage = false
      this.resetImageSlots()
      if (!this.isFinalExam) {
        this.setRandomWord()
      } else {
        this.currentWordEng = this.currentWordFinal
      }
      this.$root.$emit('startTimer')
      // this.$q.notify('setNewCreation() with ' + this.script)
      /**
      ...When changing scripts, WordCreator fails to update first letter of a word although prop is passed and relevant update function takes place after that. Change not evident in update function but in HTML's {{script}}.
      This delay works as a patch.
      **/
      setTimeout(this.continueCreation, 1)
    },
    continueCreation () {
      console.log('Called continueCreation() in WordCreator; current script: ' + this.script)
      // this.$q.notify('continueCreation() with ' + this.script)

      this.option1Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true, true)[0]
      this.option2Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true, true)[0]
      this.option3Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true, true)[0]
      this.option4Image = this.$refs.WCOps.generateOption(this.currentLetter, this.script, true, true)[0]

      console.log(this.option1Image)
      console.log(this.option2Image)

      this.$refs.WCOps.clearCache()
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
      this.$root.$emit('stopTimer')
      this.showFeedbackMessage = true
      this.setAnswerImages()
      console.log('this.userAnswerIndices: ' + Object.values(this.userAnswerIndices))
      console.log('this.correctWordIndices: ' + Object.values(this.correctWordIndices))
      if (this.isEqualLetters(this.userAnswerIndices, this.correctWordIndices)) {
        this.feedbackMessage = 'Your answer (' + this.assembleWord(this.currentWordJap) + ') was correct. Great job!'
        if (!this.isFinalExam) {
          this.$root.$emit('addExp', this.currentWordLength)
          this.$root.$emit('addSkillExp', Math.ceil(this.currentWordLength / 2))
        } else {
          this.$root.$emit('addExamPoints', 1, true)
        }
      } else {
        this.feedbackMessage = 'Your answer was incorrect. Correct answer: ' + this.assembleWord(this.currentWordJap) + '.'
        if (this.isFinalExam) {
          this.$root.$emit('addExamPoints', 1, false)
        }
      }
      this.$root.$emit('incrementNumberQuestionsAnswered', 1)
    }
  }
}
</script>

<style>
</style>
