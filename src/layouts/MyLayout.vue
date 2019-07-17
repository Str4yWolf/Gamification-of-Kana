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
              <q-badge floating color="teal">LV 0</q-badge>
            </q-avatar>
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ username }}</q-item-label>
            <q-item-label caption></q-item-label>
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
export default {
  name: 'MyLayout',
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('registerSignIn', this.registerSignIn)
    this.$root.$on('changeName', this.changeName)
    this.$root.$on('logOut', this.logOut)
  },
  data () {
    return {
      showAvatar: false,
      showSignInBtn: true,
      showRegisterBtn: true,
      showSignInField: false,
      username: ''
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
        localStorage.setItem(name, 'Level: 0')
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
    }
  }
}
</script>

<style>
</style>
