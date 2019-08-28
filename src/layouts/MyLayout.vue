<template>
  <q-layout view="lHh Lpr lFf">
    <q-header :style="layoutColor" elevated>
      <!-- info display at top -->
      <q-toolbar>
        <!-- avatar -->
        <q-item v-if="showAvatar">
          <q-item-section side>
            <q-avatar square color="red" text-color="white" >
              {{ username[0] }}
              <q-badge floating color="teal">LV {{userObj.lvl}}</q-badge>
            </q-avatar>
          </q-item-section>
          <!-- User progress display -->
          <q-item-section>
            <q-item-label><strong>{{ username }}</strong> &nbsp; &nbsp; &nbsp; &nbsp;
             Exp: {{userObj.exp}}/{{lvlThreshold[userObj.lvl]}}</q-item-label>
            <q-item-label caption>
              <q-linear-progress stripe rounded style="height: 20px" :value="lvlProgress" color="secondary" />
            </q-item-label>
          </q-item-section>
          &nbsp; &nbsp; &nbsp;
          <!-- normal display -->
          <span v-if="!isFinalExam">
            <span class="row">
              <span title="Skill Level" style="width: 80px;"><q-icon name="school"/> {{userObj.skillLvl}}</span>
              <span title="Inkblots"><q-icon name="whatshot"/> {{userObj.inkblots}}</span>
            </span>
            <span class="row">
              <span title="Achievements" style="width: 80px;"><q-icon name="star"/> {{achievementsFraction}}%</span>
              <span title="Exam Tickets"><q-icon name="note"/> {{userObj.examTickets}}</span>
            </span>
          </span>
          <!-- final exam display -->
          <span v-if="isFinalExam">
            <span title="Questions"><q-icon name="casino"/> {{numberQuestions[0]}}/{{numberQuestions[1]}}</span> <br />
            <span title="Free Errors"><q-icon name="done_all"/> {{freeErrors}}</span>
          </span>
          &nbsp; &nbsp; &nbsp;
          &nbsp; &nbsp; &nbsp;
          <!-- Timer display -->
          <span v-if="showTimer">
            <q-item-label><strong>Time</strong> &nbsp; &nbsp; &nbsp; &nbsp;
             <strong></strong>{{timeActualFormatted}}s/{{timeMax}}s</q-item-label>
            <q-item-label caption>
              <q-linear-progress stripe rounded :style="timerStyle" :value="timeFraction" color="secondary" />
            </q-item-label>
          </span>
          <!-- menu (pages) -->
          <q-menu transition-show="jump-down" transition-hide="jump-up">
            <q-list style="min-width: 100px">
              <q-item @click="unhideGeneralLearning()" clickable>
                <q-item-section>Quest</q-item-section>
              </q-item>
              <q-item clickable>
                <q-item-section>Individual Tools</q-item-section>
                <q-item-section side>
                  <q-icon name="keyboard_arrow_right" />
                </q-item-section>
                <!-- submenu start -->
                <q-menu transition-show="jump-right" transition-hide="jump-left" anchor="top right" auto-close>
                  <q-list>
                    <q-item @click="unhideFlipCard()" clickable>
                      <q-item-section>Smart Flashcard</q-item-section>
                    </q-item>
                    <q-item @click="unhideMultipleChoiceQuiz()" clickable>
                      <q-item-section>Multiple Choice</q-item-section>
                    </q-item>
                    <q-item @click="unhideWordCreator()" clickable>
                      <q-item-section>Word Creator</q-item-section>
                    </q-item>
                    <q-item @click="unhideWordReader()" clickable>
                      <q-item-section>Word Reader</q-item-section>
                    </q-item>
                  </q-list>
                </q-menu>
                <!-- submenu end -->
              </q-item>
              <q-item @click="showGojuuon()" clickable>
                <q-item-section>Character Reference</q-item-section>
              </q-item>
              <q-item @click="showShop()" clickable>
                <q-item-section>Shop</q-item-section>
              </q-item>
              <q-item @click="unhideFinalExam()" clickable>
                <q-item-section>Take Final Exam</q-item-section>
              </q-item>
              <q-item @click="showInformation()" clickable>
                <q-item-section>App Info</q-item-section>
              </q-item>
              <q-item @click="showSettings()" clickable>
                <q-item-section>Settings</q-item-section>
              </q-item>
              <q-item @click="logOut()" clickable>
                <q-item-section>Log Out</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-item>
        <!-- sign in button -->
        <q-btn v-if="showSignInBtn" color="green" label="Sign In" @click="unhideSignInField()" />
        <!-- sign in field -->
        <q-input v-if="showSignInField" v-model="username" color="white" @blur="hideSignInField()" v-on:keyup.enter="signIn()" filled>
          <template v-slot:append>
            <q-btn round dense flat icon="send" @click="signIn()" />
          </template>
        </q-input>
        &nbsp;
        <!-- register button -->
        <q-btn v-if="showRegisterBtn" color="purple" label="Register" @click="$router.push('/Register/')" />
        <!-- <q-toolbar-title>
          Kana Sensei
        </q-toolbar-title> -->
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view v-if="showRouterPage" />
      <multiple-choice-quiz-interface :userObj="userObj" v-if="showMultipleChoiceQuizPage" />
      <word-creator-interface :userObj="userObj" v-if="showWordCreatorPage" />
      <word-reader-interface :userObj="userObj" v-if="showWordReaderPage" />
      <general-learning :userObj="userObj" v-if="showGeneralLearningPage" />
      <final-exam :userObj="userObj" v-if="showFinalExamPage" />
      <flip-card v-if="showFlipCardPage" :userObj="userObj" :isTutorial="false" />
      <q-dialog v-model="hitSkillLvlUp">
      <q-card>
        <q-card-section>
          <div class="text-h6">New Skill Level ({{userObj.skillLvl}})</div>
        </q-card-section>
        <q-card-section>
          Congratulations! You have unlocked new characters.
          <span v-if="!showGeneralLearning"> &nbsp; Go to <strong>Quest</strong> to see which ones.</span>
          <br />
          <br />
          <strong>{{skillWordsCounts[userObj.skillLvl][0]}}</strong> new words available! &nbsp; Total word count: <strong>{{skillWordsCounts[userObj.skillLvl][1]}}</strong>
          <br />
          <span v-if="skillLvl2"> Also, the maximum word length has increased to 3!</span>
          <span v-if="skillLvl4"> Also, the maximum word length has increased to 4!</span>
          <span v-if="skillLvl6"> Also, the maximum word length has increased to 5!</span>
        </q-card-section>
      </q-card>
    </q-dialog>
    </q-page-container>
  </q-layout>
</template>

<script>
import userTracking from '../statics/svg/user_tracking.json'
import FlipCard from '../components/FlipCard.vue'
import MultipleChoiceQuizInterface from '../components/MultipleChoiceQuizInterface.vue'
import WordCreatorInterface from '../components/WordCreatorInterface.vue'
import WordReaderInterface from '../components/WordReaderInterface.vue'
import GeneralLearning from '../components/GeneralLearning.vue'
import FinalExam from '../components/FinalExam.vue'

export default {
  name: 'MyLayout',
  components: {
    FlipCard,
    MultipleChoiceQuizInterface,
    WordCreatorInterface,
    WordReaderInterface,
    GeneralLearning,
    FinalExam
  },
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('updateDatabase', this.updateDatabase)
    this.$root.$on('registerSignIn', this.registerSignIn)
    this.$root.$on('changeName', this.changeName)
    this.$root.$on('resetAccount', this.resetAccount)
    this.$root.$on('deleteAccount', this.deleteAccount)
    this.$root.$on('logOut', this.logOut)
    this.$root.$on('addExp', this.addExp)
    this.$root.$on('addSkillExp', this.addSkillExp)
    this.$root.$on('incrementTracking', this.incrementTracking)
    this.$root.$on('hideFlipCard', this.hideFlipCard)
    this.$root.$on('hideMultipleChoiceQuiz', this.hideMultipleChoiceQuiz)
    this.$root.$on('hideWordCreator', this.hideWordCreator)
    this.$root.$on('hideWordReader', this.hideWordReader)
    this.$root.$on('hideGeneralLearning', this.hideGeneralLearning)
    this.$root.$on('hideFinalExam', this.hideFinalExam)
    this.$root.$on('getExamTickets', this.getExamTickets)
    this.$root.$on('updateNumberQuestions', this.updateNumberQuestions)
    this.$root.$on('updateNumberFreeErrors', this.updateNumberFreeErrors)
    this.$root.$on('setTimer', this.setTimer)
    this.$root.$on('startTimer', this.startTimer)
    this.$root.$on('stopTimer', this.stopTimer)
    this.$root.$on('setShowTimer', this.setShowTimer)
    this.$root.$on('setIsFinalExam', this.setIsFinalExam)
  },
  data () {
    return {
      // display control
      showFlipCard: false,
      showMultipleChoiceQuiz: false,
      showWordCreator: false,
      showWordReader: false,
      showGeneralLearning: false,
      showFinalExam: false,
      showAvatar: false,
      showSignInBtn: true,
      showRegisterBtn: true,
      showSignInField: false,
      // level control
      lvlThreshold: { 0: 5, 1: 13, 2: 21, 3: 34, 4: 65, 5: 89, 6: 154, 7: 243, 8: 397, 9: 640, 10: 1037, 11: 1677, 12: 2714, 13: 4591, 14: 7305, 15: 11896, 16: 1000000 },
      skillLvlThreshold: { 0: 80, 1: 168, 2: 264, 3: 368, 4: 480, 5: 600, 6: 728, 7: 864, 8: 1008, 9: 1160, 10: 1500000 },
      // user data
      username: '',
      userObj: { lvl: 0, exp: 0, skillLvl: 0, skillExp: 0, inkblots: 0, tracking: 0 },
      hitSkillLvlUp: false,
      skillWordsCounts: { 0: [11, 11], 1: [19, 30], 2: [23, 53], 3: [20, 73], 4: [20, 93], 5: [20, 113], 6: [21, 134], 7: [20, 154], 8: [20, 174], 9: [20, 194], 10: [20, 194], 11: [20, 194] },
      script: 'katakana',
      achievements: [],
      // controls for timer
      showTimer: false,
      timeActual: 0,
      timeMax: 0,
      runTimer: false,
      highlight: false,
      currentTime: 0,
      // final exam controller
      isFinalExam: false,
      numberQuestions: [0, 96],
      freeErrors: 0
    }
  },
  computed: {
    /**
    lvlProgress is fraction of how many experience points a user has within the current level,
     bounded by the threshold for the next level.
     Once the user hits a new level, the lvlProgress will be set to 0 again.
    **/
    lvlProgress () {
      var value = 0
      if (this.userObj.lvl !== 0) {
        value = (this.userObj.exp - this.lvlThreshold[this.userObj.lvl - 1]) / (this.lvlThreshold[this.userObj.lvl] - this.lvlThreshold[this.userObj.lvl - 1])
      } else {
        value = this.userObj.exp / 5
      }
      return value
    },
    achievementsFraction () {
      var temp = (this.achievements.length / 29) * 10000
      return Math.floor(temp) / 100
    },
    timeFraction () {
      return this.timeActual / this.timeMax
    },
    timeActualFormatted () {
      if (this.timeActual === Math.floor(this.timeActual)) { // decimal will always be shown
        return this.timeActual.toString() + '.0'
      } else {
        return this.timeActual.toString()
      }
    },
    showFlipCardPage () {
      return (this.$route.path === '/' && this.showFlipCard)
    },
    showMultipleChoiceQuizPage () {
      return (this.$route.path === '/' && this.showMultipleChoiceQuiz)
    },
    showWordCreatorPage () {
      return (this.$route.path === '/' && this.showWordCreator)
    },
    showWordReaderPage () {
      return (this.$route.path === '/' && this.showWordReader)
    },
    showGeneralLearningPage () {
      return (this.$route.path === '/' && this.showGeneralLearning)
    },
    showFinalExamPage () {
      return (this.$route.path === '/' && this.showFinalExam)
    },
    showRouterPage () {
      return !(this.showFlipCardPage || this.showMultipleChoiceQuizPage || this.showWordCreatorPage || this.showWordReaderPage || this.showGeneralLearningPage || this.showFinalExamPage)
    },
    skillLvl0 () {
      return this.userObj.skillLvl === 0
    },
    skillLvl1 () {
      return this.userObj.skillLvl === 1
    },
    skillLvl2 () {
      return this.userObj.skillLvl === 2
    },
    skillLvl3 () {
      return this.userObj.skillLvl === 3
    },
    skillLvl4 () {
      return this.userObj.skillLvl === 4
    },
    skillLvl5 () {
      return this.userObj.skillLvl === 5
    },
    skillLvl6 () {
      return this.userObj.skillLvl === 6
    },
    skillLvl7 () {
      return this.userObj.skillLvl === 7
    },
    skillLvl8 () {
      return this.userObj.skillLvl === 8
    },
    skillLvl9 () {
      return this.userObj.skillLvl === 9
    },
    layoutColor () {
      if (this.showFinalExamPage && this.isFinalExam) {
        return 'background-color: #a65d58;' // when having Final Exam
      } else if (this.showFinalExamPage) {
        return 'background-color: #027be3;' // when on Final Exam page (think about intermediate colour)
      } else {
        return 'background-color: #027be3;' // default
      }
    },
    timerStyle () {
      var constant = 'height: 20px; width: 200px;'
      if (this.timeFraction >= 0.5) {
        return constant + ' color: green;'
      } else if (this.timeFraction >= 0.25) {
        return constant + ' color: yellow;'
      } else if (this.timeFraction >= 0.1) {
        return constant + ' color: orange;'
      } else {
        return constant + ' color: red;'
      }
    }
  },
  methods: {
    unhideFlipCard () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.hideAllComponents()
      this.showFlipCard = true
    },
    hideFlipCard () {
      this.showFlipCard = false
    },
    unhideMultipleChoiceQuiz () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.hideAllComponents()
      this.showMultipleChoiceQuiz = true
    },
    hideMultipleChoiceQuiz () {
      this.showMultipleChoiceQuiz = false
    },
    unhideWordCreator () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.hideAllComponents()
      this.showWordCreator = true
    },
    hideWordCreator () {
      this.showWordCreator = false
    },
    unhideWordReader () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.hideAllComponents()
      this.showWordReader = true
    },
    hideWordReader () {
      this.showWordReader = false
    },
    unhideGeneralLearning () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.hideAllComponents()
      this.showGeneralLearning = true
    },
    hideGeneralLearning () {
      console.log('called hideGeneralLearning')
      this.showGeneralLearning = false
    },
    unhideFinalExam () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.hideAllComponents()
      this.showFinalExam = true
    },
    hideFinalExam () {
      this.showFinalExam = false
    },
    hideAllComponents () {
      this.showFlipCard = false
      this.showMultipleChoiceQuiz = false
      this.showWordCreator = false
      this.showWordReader = false
      this.showGeneralLearning = false
      this.showFinalExam = false
      this.$router.push('/')
    },
    unhideSignInField () {
      console.log('Called unhideSignInField from Layout')
      this.showSignInBtn = false
      this.showSignInField = true
    },
    hideSignInField () {
      console.log('Called hideSignInField from Layout')
      this.showSignInBtn = true
      this.showSignInField = false
    },
    /**
    pages
    **/
    showGojuuon () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.$router.push('/Gojuuon/')
    },
    showShop () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.$router.push('/Shop/')
    },
    showInformation () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.$router.push('/Information/')
    },
    showSettings () {
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.$router.push('/Settings/')
    },
    /**
    Signs in a registered user by loading user data and setting display elements.
     Unregistered names will be prompted to the user.
    **/
    signIn () {
      console.log('Called signIn from Layout')
      if (localStorage.getItem(this.username) !== null) {
        this.userObj = JSON.parse(localStorage.getItem(this.username))
        console.log(this.userObj)
        this.showAvatar = true
        this.showSignInField = false
        this.showRegisterBtn = false
        this.$router.push('/')
      } else {
        alert('The username ' + this.username + ' doesn\'t exist. Please try registering it.')
      }
    },
    /**
    Returns an initialized userObj with current time stamp
    **/
    initializeUserObj () {
      var tmpObj = { lvl: 0, exp: 0, skillLvl: 0, skillExp: 0, inkblots: 0, examTickets: 0, tracking: userTracking, learningMode: 0, learningExp: 0, viewedTutorial: [false, false, false, false, false, false, false, false, false, false] }
      var trackingKeys = Object.keys(tmpObj.tracking)
      var currentDate = Date.now()
      // initialize time stamp to current time for all user tracking maps
      trackingKeys.forEach(function (trackingKey) {
        tmpObj.tracking[trackingKey] = [0, 0, 1, currentDate]
      })
      return tmpObj
    },
    /**
    Registers a username (creates a new database entry) and adjusts display if the username is not already given.
     Else prompts the user to try a different name.
    **/
    registerSignIn (name) {
      console.log('Called registerSignIn from Layout')
      if (localStorage.getItem(name) !== null) {
        alert('The name ' + name + ' has already been registered. Please try a different name.')
      } else {
        alert('Registration successful.')
        this.showAvatar = true
        this.showSignInBtn = false
        this.showSignInField = false
        this.showRegisterBtn = false
        this.username = name
        this.userObj = this.initializeUserObj()
        this.$router.push('../')
        this.updateDatabase()
      }
    },
    /**
    Logs out a user by adjusting display and resetting currently loaded user data.
    **/
    logOut () {
      console.log('Called logOut')
      if (this.isFinalExam) {
        if (confirm('Are you sure you want to leave this page? Unless you have finished the all questions, your progress will be lost!')) {
          this.$root.$emit('leavePageFinalExam')
        } else {
          return
        }
      }
      this.showAvatar = false
      this.showSignInBtn = true
      this.showRegisterBtn = true
      this.username = ''
      this.hideAllComponents()
      this.userObj = { lvl: 0, exp: 0, skillLvl: 0, skillExp: 0, inkblots: 0, examTickets: 0, tracking: userTracking, learningMode: 0, learningExp: 0, viewedTutorial: [false, false, false, false, false, false, false, false, false, false] }
    },
    /**
    Changes username to a new name if the new name doesn't already exists.
     Technically, the user data will be bound to a new key (new username).
    **/
    changeName (name) {
      console.log('Called changeName(' + name + ') from Layout')
      if (localStorage.getItem(name) !== null) {
        alert('The name ' + name + ' already exists. Please try a different name.')
      } else {
        var userData = localStorage.getItem(this.username) // old data backup
        localStorage.removeItem(this.username) // remove database entry of old name
        localStorage.setItem(name, userData) // create database entry with new name and data backup
        this.username = name
        alert('Successfully changed name to ' + name + '.')
      }
    },
    /**
    Resets user data and reloads that data to current display.
    **/
    resetAccount () {
      localStorage.setItem(this.username, JSON.stringify(this.initializeUserObj()))
      this.userObj = JSON.parse(localStorage.getItem(this.username))
    },
    /**
    Permanently removes the username and data associated with it and proceeds with the logout procedure.
    **/
    deleteAccount () {
      localStorage.removeItem(this.username)
      this.logOut()
    },
    // TIMER
    setShowTimer (x) {
      console.log('called setShowTimer(' + x + ') in MyLayout')
      this.showTimer = x
    },
    /**
    set the timer to max (in seconds.f1)
    **/
    setTimer (max) {
      this.timeMax = max
      this.timeActual = max
    },
    startTimer () {
      this.runTimer = true
      // this.currentTime = Date.now()
      setTimeout(this.reduceTime, 91)
    },
    reduceTime () {
      // console.log('called reduceTime() in MyLayout; timeActual: ' + this.timeActual)
      // console.log('timeActual: ' + this.timeActual)
      // console.log('this.runTimer: ' + this.runTimer)
      if ((this.timeActual > 0) && this.runTimer) {
        var temp = (this.timeActual * 10) - 1 // avoid float imprecision
        this.timeActual = (temp / 10)
        clearTimeout()
        setTimeout(this.reduceTime, 91)
        // console.log((Date.now() - this.currentTime) / 1000)
      } else if (this.timeActual === 0) {
        this.$root.$emit('timeElapsed')
        clearTimeout()
      }
    },
    /**
    startTimer () {
      this.runTimer = true
      // this.currentTime = Date.now()
      setInterval(this.reduceTime, 91)
    },
    reduceTime () {
      // console.log('called reduceTime() in MyLayout; timeActual: ' + this.timeActual)
      // console.log('timeActual: ' + this.timeActual)
      // console.log('this.runTimer: ' + this.runTimer)
      if ((this.timeActual > 0) && this.runTimer) {
        var temp = (this.timeActual * 10) - 1 // avoid float imprecision
        this.timeActual = (temp / 10)
        // console.log((Date.now() - this.currentTime) / 1000)
      } else if (this.timeActual === 0) {
        this.$root.$emit('timeElapsed')
        clearInterval()
      }
    },
    **/
    stopTimer () {
      this.runTimer = false
      clearTimeout()
    },
    /**
    Calculate an additional experience boost dependent on time taken
    @ params
    n: base experience
    t: time passed
    decay: how fast the boost will decay (exponential factor)
    **/
    getTimeBoost (n, t, decay) {
      if (t === 0) {
        return n
      } else {
        return Math.round(n * ((1 / t) ** decay))
      }
    },
    /**
    Add one exam ticket to current user object.
    @params
    n: number of tickets
    consumeInkblots: Boolean; will consume 2 inkblots if true
    **/
    getExamTickets (n, consumeInkblots) {
      if ((n * 2) > this.userObj.inkblots) {
        alert('Purchase failed. You need ' + (n * 2) + ' inkblots but only have ' + this.userObj.inkblots + '.')
        return
      } else if (n < 0) {
        alert('Purchase failed. You cannot enter a negative number.')
        return
      }
      console.log('getExamTickets logging')
      console.log(typeof n)
      console.log(typeof this.userObj.examTickets)
      this.userObj.examTickets += n
      if (consumeInkblots) {
        this.userObj.inkblots -= (n * 2)
      }
      this.updateDatabase()
      if (consumeInkblots) {
        this.$q.notify('You have purchased ' + n + ' Exam Tickets for ' + (n * 2) + ' Inkblots.')
      } else {
        this.$q.notify('You have received ' + n + ' Exam Tickets.')
      }
    },
    /**
    Adds user experience and calls relevant functions to make changes effective.
    **/
    addExp (n) {
      this.userObj.exp += n
      this.userObj.learningExp += n
      this.updateLvl()
      this.updateLearningMode()
      this.updateDatabase()
    },
    /**
    similar to addExp(n)
    **/
    addSkillExp (n) {
      this.userObj.skillExp += n
      this.updateSkillLvl()
      this.updateDatabase()
    },
    /**
    Recursive function to check for level-ups which are governed by lvlThreshold object.
     Maximum reachable level is 16.
    **/
    updateLvl () {
      if (this.userObj.lvl === 16) {
        return
      }
      var threshold = this.lvlThreshold[this.userObj.lvl] // get threshold associated with current user level
      if (this.userObj.exp >= threshold) {
        this.userObj.lvl += 1 // increment level upon hitting threshold
        this.userObj.inkblots += this.userObj.lvl // get inkblots as rewards
        this.$q.notify('Congratulations. You have reached level ' + this.userObj.lvl + '!')
        this.updateLvl() // check whether more levels have been hit
      }
    },
    /**
    Updates skillLvl similarly to updateLevel()
    **/
    updateSkillLvl () {
      if (this.userObj.skillLvl === 10) {
        return
      }
      var threshold = this.skillLvlThreshold[this.userObj.skillLvl]
      if (this.userObj.skillExp >= threshold) {
        this.userObj.skillLvl += 1
        this.$q.notify('Congratulations. You have reached skill level ' + this.userObj.skillLvl + '!')
        this.userObj.learningMode = 0
        this.userObj.learningExp = 0
        if (this.userObj.skillLvl !== 9) {
          this.hitSkillLvlUp = true
        }
        this.updateSkillLvl()
      }
    },
    /**
    Change learning mode (how many different games will be included in Quest)
    learning mode depends on how many experience points a user has gained within a skill level
    **/
    updateLearningMode () {
      if (this.userObj.learningExp >= (20 + (this.userObj.skillLvl * 4)) && this.userObj.learningMode === 1) {
        this.$q.notify('You have unlocked Word Creator for learning Skill Level ' + (this.userObj.skillLvl + 1) + '.')
        this.userObj.learningMode = 2
      }
      if (this.userObj.learningExp >= (50 + (this.userObj.skillLvl * 6)) && this.userObj.learningMode === 2) {
        this.$q.notify('You have unlocked Word Reader for learning Skill Level ' + (this.userObj.skillLvl + 1) + '.')
        this.userObj.learningMode = 3
      }
    },
    /**
    Increment user tracking by adjusting counters, mastery, and time_last_seen
    ---
    @params
    prefix: letter in question
    s1: source script (question)
    s2: target script (answer)
    correctlyAnswered: whether user has answered correctly
    **/
    incrementTracking (prefix, s1, s2, correctlyAnswered) {
      console.log('updateTracking with prefix: ' + prefix + ', scripts ' + s1 + ' ' + s2 + ' and increment of correct words count of ' + correctlyAnswered + '.')
      var key = prefix + '_' + s1 + s2 // format used in user tracking
      var val = this.userObj['tracking'][key] // val := [times_correctly_answered, times_seen, mastery, time_last_seen]
      val[3] = Date.now() // update time_last_seen
      if (correctlyAnswered) {
        val[0] += 1 // increase correct answer count
        val[2] += 1 // increase mastery
      } else {
        val[2] = Math.ceil(val[2] / 5) // penalty on mastery for answering wrong
      }
      val[1] += 1 // increase total times seen count
      this.userObj['tracking'][key] = val // update map
      this.updateDatabase()
    },
    setIsFinalExam (x) {
      console.log('called setIsFinalExam(' + x + ') in MyLayout')
      this.isFinalExam = x
    },
    updateNumberQuestions (xs) {
      this.numberQuestions = xs
    },
    updateNumberFreeErrors (n) {
      this.freeErrors = n
    },
    /**
    Writes current userObj of user onto database
    **/
    updateDatabase () {
      localStorage.setItem(this.username, JSON.stringify(this.userObj))
    }
  }
}
</script>

<style>
</style>
