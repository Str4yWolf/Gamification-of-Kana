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
          <q-item-section>
            <q-item-label><strong>{{ username }}</strong> &nbsp; &nbsp; &nbsp; &nbsp;
             Exp: {{userObj.exp}}/{{lvlThreshold[userObj.lvl]}}</q-item-label>
            <q-item-label caption>
              <q-linear-progress stripe rounded style="height: 20px" :value="lvlProgress" color="secondary" />
            </q-item-label>
          </q-item-section>
          <q-menu auto-close>
            <q-list style="min-width: 100px">
              <q-item @click="$router.push('/Information/')" clickable>
                <q-item-section>Info</q-item-section>
              </q-item>
              <q-item @click="$router.push('/Settings/')" clickable>
                <q-item-section>Settings</q-item-section>
              </q-item>
              <q-item @click="$router.push('/MultipleChoice/')" clickable>
                <q-item-section>Multiple Choice</q-item-section>
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
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import userTracking from '../statics/svg/user_tracking.json'

export default {
  name: 'MyLayout',
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('registerSignIn', this.registerSignIn)
    this.$root.$on('changeName', this.changeName)
    this.$root.$on('resetAccount', this.resetAccount)
    this.$root.$on('deleteAccount', this.deleteAccount)
    this.$root.$on('logOut', this.logOut)
    this.$root.$on('addExp', this.addExp)
    this.$root.$on('incrementTracking', this.incrementTracking)
  },
  data () {
    return {
      showAvatar: false,
      showSignInBtn: true,
      showRegisterBtn: true,
      showSignInField: false,
      lvlThreshold: { 0: 5, 1: 13, 2: 21, 3: 34, 4: 65, 5: 89, 6: 154, 7: 243, 8: 397, 9: 640, 10: 1037, 11: 1000000 },
      username: '',
      userObj: { lvl: 0, exp: 0, tracking: 0 }
    }
  },
  computed: {
    lvlProgress () {
      var value = 0
      if (this.userObj.lvl !== 0) {
        value = (this.userObj.exp - this.lvlThreshold[this.userObj.lvl - 1]) / (this.lvlThreshold[this.userObj.lvl] - this.lvlThreshold[this.userObj.lvl - 1])
      } else {
        value = this.userObj.exp / 5
      }
      return value
    }
  },
  methods: {
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
    registerSignIn (name) {
      console.log('Called registerSignIn from Layout')
      if (localStorage.getItem(name) !== null) {
        alert('The name ' + name + ' has already been registered. Please try a different name.')
      } else {
        alert('Registration successful.')
        localStorage.setItem(name, JSON.stringify({ lvl: 0, exp: 0, tracking: userTracking }))
        this.showAvatar = true
        this.showSignInBtn = false
        this.showSignInField = false
        this.showRegisterBtn = false
        this.username = name
        this.$router.push('../')
      }
    },
    logOut () {
      console.log('Called logOut')
      this.showAvatar = false
      this.showSignInBtn = true
      this.showRegisterBtn = true
      this.username = ''
      this.$router.push('/')
    },
    changeName (name) {
      console.log('Called changeName(' + name + ') from Layout')
      if (localStorage.getItem(name) !== null) {
        alert('The name ' + name + ' already exists. Please try a different name.')
      } else {
        var userData = localStorage.getItem(this.username)
        localStorage.removeItem(this.username)
        localStorage.setItem(name, userData)
        this.username = name
        alert('Successfully changed name to ' + name + '.')
      }
    },
    resetAccount () {
      localStorage.setItem(this.username, JSON.stringify({ lvl: 0, exp: 0, tracking: userTracking }))
      this.userObj = JSON.parse(localStorage.getItem(this.username))
    },
    deleteAccount () {
      localStorage.removeItem(this.username)
      this.userObj = { lvl: 0, exp: 0, tracking: userTracking }
      this.logOut()
    },
    addExp (n) {
      this.userObj.exp += n
      this.updateLvl()
      this.updateDatabase()
    },
    updateLvl () {
      if (this.userObj.lvl === 12) {
        return
      }
      var threshold = this.lvlThreshold[this.userObj.lvl]
      if (this.userObj.exp >= threshold) {
        this.userObj.lvl += 1
        alert('Congratulations. You have reached level ' + this.userObj.lvl + '!')
        this.updateLvl()
      }
    },
    /**
    @params
    prefix: letter in question
    s1: source script (question)
    s2: target script (answer)
    correct: whether user has answered correctly
    **/
    incrementTracking (prefix, s1, s2, correct) {
      console.log('updateTracking with prefix: ' + prefix + ', scripts ' + s1 + ' ' + s2 + ' and increment of correct words count of ' + correct + '.')
      var key = prefix + '_' + s1 + s2
      // val := [s1, s2, mastery, time_last_seen]
      var val = this.userObj['tracking'][key]
      val[3] = Date.now()
      if (correct) {
        val[0] += 1
        val[2] += 1
      } else {
        // penalty for answering wrong
        val[2] = Math.ceil(val[2] / 5)
      }
      val[1] += 1
      this.userObj['tracking'].prefix = val
      this.updateDatabase()
    },
    updateDatabase () {
      localStorage.setItem(this.username, JSON.stringify(this.userObj))
    }
  }
}
</script>

<style>
</style>
