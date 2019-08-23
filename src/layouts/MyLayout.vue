<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
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
          <span>
            <span title="Skill Level"><q-icon name="school"/> {{userObj.skillLvl}}</span> <br />
            <span title="Inkblots"><q-icon name="whatshot"/> {{userObj.inkblots}}</span>
          </span>
          &nbsp; &nbsp; &nbsp;
          <span>
            <span title="Exam Tickets"><q-icon name="note"/> {{userObj.examTickets}}</span>
          </span>
          <!-- Timer display -->
          <q-item-section v-if="showTimer">
            <q-item-label><strong>Time Boost</strong> &nbsp; &nbsp; &nbsp; &nbsp;
             <strong>Boost: </strong>{{timeBoostActual}}/ {{timeBoostMax}}</q-item-label>
            <q-item-label caption>
              <q-linear-progress stripe rounded style="height: 20px" :value="timeBoostActual" color="secondary" />
            </q-item-label>
          </q-item-section>
          <!-- menu (pages) -->
          <q-menu transition-show="jump-down" transition-hide="jump-up">
            <q-list style="min-width: 100px">
              <q-item @click="unhideGeneralLearning()" clickable>
                <q-item-section>Learn</q-item-section>
              </q-item>
              <q-item clickable>
                <q-item-section>Learning Tools</q-item-section>
                <q-item-section side>
                  <q-icon name="keyboard_arrow_right" />
                </q-item-section>
                <!-- submenu start -->
                <q-menu transition-show="jump-right" transition-hide="jump-left" anchor="top right" auto-close>
                  <q-list>
                    <q-item @click="unhideFlipCard()" clickable>
                      <q-item-section>Simple Flashcard</q-item-section>
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
              <q-item @click="$router.push('/Gojuuon/')" clickable>
                <q-item-section>Character Reference</q-item-section>
              </q-item>
              <q-item @click="$router.push('/Shop/')" clickable>
                <q-item-section>Shop</q-item-section>
              </q-item>
              <q-item @click="unhideFinalExam()" clickable>
                <q-item-section>Take Final Exam</q-item-section>
              </q-item>
              <q-item @click="$router.push('/Information/')" clickable>
                <q-item-section>App Info</q-item-section>
              </q-item>
              <q-item @click="$router.push('/Settings/')" clickable>
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
      <flip-card v-if="showFlipCardPage" />
      <q-dialog v-model="hitSkillLvlUp" style="width: 800px;">
      <q-card style="width: 800px; height: 500px;">
        <q-card-section>
          <div class="text-h6">New Skill Level ({{userObj.skillLvl}})</div>
        </q-card-section>
        <q-card-section style="width: 800px;">
          Congratulations! You have unlocked the following characters. Hover over them to see katakana. Also visible under <strong>Menu -> "Character Reference"</strong>.
          <br />
          <br />
          <span v-if="skillLvl0" class="row">
            <character-info :letter="'a'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'i'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'u'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'e'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'o'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl1" class="row">
            <character-info :letter="'ka'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ki'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ku'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ke'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ko'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl2" class="row">
            <character-info :letter="'sa'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'shi'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'su'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'se'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'so'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl3" class="row">
            <character-info :letter="'ta'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'chi'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'tsu'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'te'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'to'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl4" class="row">
            <character-info :letter="'na'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ni'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'nu'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ne'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'no'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl5" class="row">
            <character-info :letter="'ha'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'hi'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'fu'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'he'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ho'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl6" class="row">
            <character-info :letter="'ma'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'mi'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'mu'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'me'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'mo'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl7" class="row">
            <character-info :letter="'ra'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ri'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ru'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'re'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'ro'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl8" class="row">
            <character-info :letter="'ya'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'yu'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'yo'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'wa'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'wo'" :highlight="highlight" :sourceScript="script" />
          </span>
          <span v-if="skillLvl9" class="row">
            <character-info :letter="'n'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'we'" :highlight="highlight" :sourceScript="script" />
            <character-info :letter="'wi'" :highlight="highlight" :sourceScript="script" />
          </span>
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <br />
          <strong>{{skillWordsCounts[userObj.skillLvl][0]}}</strong> new words available! &nbsp; Total word count: <strong>{{skillWordsCounts[userObj.skillLvl][1]}}</strong>
          <br />
          <span v-if="skillLvl2"> Also, the maximum word length has improved to 3!</span>
          <span v-if="skillLvl4"> Also, the maximum word length has improved to 4!</span>
          <span v-if="skillLvl6"> Also, the maximum word length has improved to 5!</span>
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
import CharacterInfo from '../components/CharacterInfo.vue'

export default {
  name: 'MyLayout',
  components: {
    FlipCard,
    MultipleChoiceQuizInterface,
    WordCreatorInterface,
    WordReaderInterface,
    GeneralLearning,
    FinalExam,
    CharacterInfo
  },
  created () {
    // listen to event calls from elsewhere
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
      skillLvlThreshold: { 0: 50, 1: 110, 2: 180, 3: 260, 4: 350, 5: 450, 6: 560, 7: 680, 8: 810, 9: 950, 10: 1500000 },
      // user data
      username: '',
      userObj: { lvl: 0, exp: 0, skillLvl: 0, skillExp: 0, inkblots: 0, tracking: 0 },
      hitSkillLvlUp: false,
      skillWordsCounts: { 0: [11, 11], 1: [19, 30], 2: [23, 53], 3: [20, 73], 4: [20, 93], 5: [20, 113], 6: [21, 134], 7: [20, 154], 8: [20, 174], 9: [20, 194], 10: [20, 194], 11: [20, 194] },
      script: 'katakana',
      // controls for time boost
      timeStamp: 0,
      showTimer: false,
      timeBoostMax: 0,
      highlight: false
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
    timeBoostActual () {
      var currentTime = Date.now()
      var secondsPassed = (currentTime - this.timeStamp()) / 1000
      return this.getTimeBoost(this.timeBoostMax, secondsPassed, 1) / this.timeBoostMax
    },
    boostValue () {
      return this.timeBoostActual / this.timeBoostMax
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
    }
  },
  methods: {
    unhideFlipCard () {
      this.hideAllComponents()
      this.showFlipCard = true
    },
    hideFlipCard () {
      this.showFlipCard = false
    },
    unhideMultipleChoiceQuiz () {
      this.hideAllComponents()
      this.showMultipleChoiceQuiz = true
    },
    hideMultipleChoiceQuiz () {
      this.showMultipleChoiceQuiz = false
    },
    unhideWordCreator () {
      this.hideAllComponents()
      this.showWordCreator = true
    },
    hideWordCreator () {
      this.showWordCreator = false
    },
    unhideWordReader () {
      this.hideAllComponents()
      this.showWordReader = true
    },
    hideWordReader () {
      this.showWordReader = false
    },
    unhideGeneralLearning () {
      this.hideAllComponents()
      this.showGeneralLearning = true
    },
    hideGeneralLearning () {
      console.log('called hideGeneralLearning')
      this.showGeneralLearning = false
    },
    unhideFinalExam () {
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
      var tmpObj = { lvl: 0, exp: 0, skillLvl: 0, skillExp: 0, inkblots: 0, examTickets: 0, tracking: userTracking }
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
      this.showAvatar = false
      this.showSignInBtn = true
      this.showRegisterBtn = true
      this.username = ''
      this.hideAllComponents()
      this.userObj = { lvl: 0, exp: 0, skillLvl: 0, skillExp: 0, inkblots: 0, examTickets: 0, tracking: userTracking }
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
      this.userObj.examTickets += n
      if (consumeInkblots) {
        this.userObj.inkblots -= (n * 2)
      }
      this.updateDatabase()
    },
    /**
    Adds user experience and calls relevant functions to make changes effective.
    **/
    addExp (n) {
      this.userObj.exp += n
      this.updateLvl()
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
     Maximum reachable level is 12.
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
        if (this.userObj.skillLvl !== 9) {
          this.hitSkillLvlUp = true
        }
        this.updateSkillLvl()
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
