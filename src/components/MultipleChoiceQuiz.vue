<template>
  <span>
      <!-- question -->
      <span class="row" style="padding: 20px 0px 20px 50px;">
        <character-flashcard id="multiple-choice-question" :imgSrc="questionImage" :showTitle="validationInProgress" />
        <span v-if="!hasAnsweredQuestion" style="position:relative; top:68px; left:30px;">What is this <strong>{{script1}}</strong>'s equivalent in <strong>{{script2}}</strong>?</span>
        <span v-if="hasAnsweredQuestion" style="padding:30px;">
          <span v-if="hasAnsweredCorrectly">
            <strong>Feedback: </strong> Your answer (<strong style="color: blue">Option {{this.userAnswer + 1}}</strong>) was <strong style="color: green;">correct</strong>. Great job!
          </span>
          <span v-if="!hasAnsweredCorrectly">
            Your answer (<strong style="color: blue">Option {{this.userAnswer + 1}}</strong>) was <strong style="color: red;">incorrect</strong>.
            <br/>
            <br/>
            <strong>
              <span style="color: green">Correct answer: </span>
              <span style="color: blue;">Option {{this.correctAnswer + 1}}</span>
            </strong>
          </span>
        </span>
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
    <letter-operations :highlightManyougana="highlightManyougana" :skillLevel="userObj['skillLvl']" ref="MCQOps" />
  </span>
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
      // script-related
      currentKey: '',
      // convert script to its number code as used in script-to-script maps
      scriptIndex: {
        'romaji': '0',
        'katakana': '1',
        'manyougana-katakana': '2',
        'manyougana-katakana-c': '2',
        'hiragana': '3',
        'hentaigana': '4'
      },
      // quiz controllers
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
    userObj: Object,
    script1: String,
    script2: String,
    highlightManyougana: Boolean,
    quizLength: Number,
    singleQuestion: Boolean,
    isFinalExam: Boolean,
    currentKeyFinal: String
  },
  mounted () {
    // this.$refs.modal.$el.focus()
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
    },
    hasAnsweredCorrectly () {
      return this.userAnswer === this.correctAnswer
    }
  },
  methods: {
    /**
    Highlight or unhighlight the image according to the highlightManyougana state
    **/
    updateHighlight () {
      console.log('called updateHighlight() from MultipleChoiceQuiz')
      // this.$refs.MCQOps.toggleHighlight()
      if (this.script1 === 'manyougana-katakana') {
        this.questionImage = this.$refs.MCQOps.getLetters(this.currentKey, 'manyougana-katakana')[0]
      } else {
        console.log(this.option1Image)
        console.log(this.$refs.MCQOps.getLetterFromPath(this.option1Image))
        this.option1Image = this.$refs.MCQOps.getLetters(this.$refs.MCQOps.getLetterFromPath(this.option1Image), 'manyougana-katakana')[0]
        console.log(this.option1Image)
        this.option2Image = this.$refs.MCQOps.getLetters(this.$refs.MCQOps.getLetterFromPath(this.option2Image), 'manyougana-katakana')[0]
        this.option3Image = this.$refs.MCQOps.getLetters(this.$refs.MCQOps.getLetterFromPath(this.option3Image), 'manyougana-katakana')[0]
        this.option4Image = this.$refs.MCQOps.getLetters(this.$refs.MCQOps.getLetterFromPath(this.option4Image), 'manyougana-katakana')[0]
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
      this.$root.$emit('setQuizHasStarted', true)
      this.hasAnsweredQuestion = false
      this.validationInProgress = false
      this.$root.$emit('setValidationInProgress', false)
      // set a random new currentKey which yet employs spaced repetition and emphasis on less mastered questions
      this.randomizeCurrentKey()
      // get question image
      this.questionImage = this.$refs.MCQOps.getLetters(this.currentKey, this.script1)[0]
      // generate options of target script2 which is NOT equal to the letter passed as randomKey
      this.option1Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true, true)[0]
      this.option2Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true, true)[0]
      this.option3Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true, true)[0]
      this.option4Image = this.$refs.MCQOps.generateOption(this.currentKey, this.script2, true, true)[0]
      this.$refs.MCQOps.clearCache()
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
    Generate next options and display them accordingly
    **/
    continueExam () {
      console.log('called continueExam in MultipleChoice')
      // adjust display controls
      this.quizHasStarted = true
      this.$root.$emit('setQuizHasStarted', true)
      this.hasAnsweredQuestion = false
      this.validationInProgress = false
      this.$root.$emit('setValidationInProgress', false)
      // get question image
      this.questionImage = this.$refs.MCQOps.getLetters(this.currentKeyFinal, this.script1)[0]
      // generate options of target script2 which is NOT equal to the letter passed as randomKey
      this.option1Image = this.$refs.MCQOps.generateOption(this.currentKeyFinal, this.script2, true, true)[0]
      this.option2Image = this.$refs.MCQOps.generateOption(this.currentKeyFinal, this.script2, true, true)[0]
      this.option3Image = this.$refs.MCQOps.generateOption(this.currentKeyFinal, this.script2, true, true)[0]
      this.option4Image = this.$refs.MCQOps.generateOption(this.currentKeyFinal, this.script2, true, true)[0]
      this.$refs.MCQOps.clearCache()
      this.correctAnswer = Math.floor(Math.random() * 4) // let correct answer be one of 0,1,2,3
      // replace one of the options (all incorrect) with correct answer
      switch (this.correctAnswer) {
        case 0:
          this.option1Image = this.$refs.MCQOps.getLetters(this.currentKeyFinal, this.script2)[0]
          break
        case 1:
          this.option2Image = this.$refs.MCQOps.getLetters(this.currentKeyFinal, this.script2)[0]
          break
        case 2:
          this.option3Image = this.$refs.MCQOps.getLetters(this.currentKeyFinal, this.script2)[0]
          break
        case 3:
          this.option4Image = this.$refs.MCQOps.getLetters(this.currentKeyFinal, this.script2)[0]
          break
      }
      this.$root.$emit('startTimer')
    },
    /**
    validate option event triggered by user input
    **/
    validateOption (event) {
      console.log('called validateOption from MultipleChoice')
      this.$root.$emit('stopTimer')
      this.userObj.timesMCQ += 1
      this.$root.$emit('checkAchievements', 13)
      // adjust controls
      this.hasAnsweredQuestion = true
      this.validationInProgress = true
      this.$root.$emit('setValidationInProgress', true)
      // get user answer
      if (event.target !== undefined) {
        this.userAnswer = parseInt(event.target.id.split('-')[4]) - 1 // from button
      } else {
        this.userAnswer = parseInt(event) - 1 // from keyboard
      }
      console.log('userAnswer: ' + this.userAnswer)
      console.log('correctAnswer: ' + this.correctAnswer)
      this.numberQuestionsAnswered += 1
      this.$root.$emit('setNumberQuestionsAnswered', this.numberQuestionsAnswered)
      if (!this.isFinalExam) {
        this.$root.$emit('MultipleChoiceQuestion answered')
      } else {
        this.$root.$emit('incrementNumberQuestionsAnswered', 1)
      }
      // display feedback,
      // adjust quiz controls, and
      // log progress in user tracking (to affect future questions in spaced repetition)
      // depending on answer
      if (this.hasAnsweredCorrectly) {
        this.questionsAnsweredCorrectly += 1
        // reward with exp (perhaps level-ups)
        if (!this.isFinalExam) {
          this.$root.$emit('addExp', 1)
          this.$root.$emit('addSkillExp', 1)
          this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 1)
        } else {
          this.$root.$emit('addExamPoints', 1, true)
        }
        if (!this.singleQuestion) {
          if (!this.isFinalExam) {
            this.continueQuiz()
          } else {
            this.continueExam()
          }
        }
      } else {
        if (!this.isFinalExam) {
          this.$root.$emit('incrementTracking', this.currentKey, this.scriptIndex[this.script1], this.scriptIndex[this.script2], 0)
        } else {
          this.$root.$emit('addExamPoints', 1, false)
        }
      }
    },
    /**
    End quiz by intializing quiz controls and displaying feedback to user
    **/
    endQuiz () {
      console.log('called endQuiz from MultipleChoice')
      this.quizHasStarted = false
      this.$root.$emit('setQuizHasStarted', false)
      this.validationInProgress = false
      this.$root.$emit('setValidationInProgress', false)
      this.feedbackMessage = 'Congratulations. You have scored ' + this.questionsAnsweredCorrectly + ' out of ' + this.numberQuestionsAnswered + ' in this quiz!'
      this.questionsAnsweredCorrectly = 0
      this.numberQuestionsAnswered = 0
    }
  }
}
</script>

<style>
</style>
