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
          <!-- menu (pages) -->
          <q-menu auto-close>
            <q-list style="min-width: 100px">
              <q-item @click="$router.push('/Information/')" clickable>
                <q-item-section>Info</q-item-section>
              </q-item>
              <q-item @click="$router.push('/Settings/')" clickable>
                <q-item-section>Settings</q-item-section>
              </q-item>
              <q-item @click="unhideMultipleChoiceQuiz()" clickable>
                <q-item-section>Multiple Choice</q-item-section>
              </q-item>
              <q-item @click="unhideWordCreator()" clickable>
                <q-item-section>Word Creator</q-item-section>
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
      <multiple-choice-quiz :userObj="userObj" v-if="showMultipleChoiceQuizPage" />
      <word-creator v-if="showWordCreatorPage" />
    </q-page-container>
  </q-layout>
</template>

<script>
import userTracking from '../statics/svg/user_tracking.json'
import MultipleChoiceQuiz from '../components/MultipleChoiceQuiz.vue'
import WordCreator from '../components/WordCreator.vue'

export default {
  name: 'MyLayout',
  components: {
    MultipleChoiceQuiz,
    WordCreator
  },
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('registerSignIn', this.registerSignIn)
    this.$root.$on('changeName', this.changeName)
    this.$root.$on('resetAccount', this.resetAccount)
    this.$root.$on('deleteAccount', this.deleteAccount)
    this.$root.$on('logOut', this.logOut)
    this.$root.$on('addExp', this.addExp)
    this.$root.$on('incrementTracking', this.incrementTracking)
    this.$root.$on('hideMultipleChoiceQuiz', this.hideMultipleChoiceQuiz)
    this.$root.$on('hideWordCreator', this.hideWordCreator)
  },
  data () {
    return {
      // display control
      showMultipleChoiceQuiz: false,
      showWordCreator: false,
      showAvatar: false,
      showSignInBtn: true,
      showRegisterBtn: true,
      showSignInField: false,
      // level control
      lvlThreshold: { 0: 5, 1: 13, 2: 21, 3: 34, 4: 65, 5: 89, 6: 154, 7: 243, 8: 397, 9: 640, 10: 1037, 11: 1000000 },
      // user data
      username: '',
      userObj: { lvl: 0, exp: 0, tracking: 0 }
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
    showMultipleChoiceQuizPage () {
      return (this.$route.path === '/' && this.showMultipleChoiceQuiz)
    },
    showWordCreatorPage () {
      return (this.$route.path === '/' && this.showWordCreator)
    },
    showRouterPage () {
      return !(this.showMultipleChoiceQuizPage || this.showWordCreatorPage)
    }
  },
  methods: {
    unhideMultipleChoiceQuiz () {
      this.showMultipleChoiceQuiz = true
      this.$router.push('/')
    },
    hideMultipleChoiceQuiz () {
      this.showMultipleChoiceQuiz = false
    },
    unhideWordCreator () {
      this.showWordCreator = true
      this.$router.push('/')
    },
    hideWordCreator () {
      this.showWordCreator = false
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
      var tmpObj = { lvl: 0, exp: 0, tracking: userTracking }
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
      this.$router.push('/')
      this.userObj = { lvl: 0, exp: 0, tracking: userTracking }
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
    Adds user experience and calls relevant functions to make changes effective.
    **/
    addExp (n) {
      this.userObj.exp += n
      this.updateLvl()
      this.updateDatabase()
    },
    /**
    Recursive function to check for level-ups which are governed by lvlThreshold object.
     Maximum reachable level is 12.
    **/
    updateLvl () {
      if (this.userObj.lvl === 12) {
        return
      }
      var threshold = this.lvlThreshold[this.userObj.lvl] // get threshold associated with current user level
      if (this.userObj.exp >= threshold) {
        this.userObj.lvl += 1 // increment level upon hitting threshold
        alert('Congratulations. You have reached level ' + this.userObj.lvl + '!')
        this.updateLvl() // check whether more levels have been hit
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
