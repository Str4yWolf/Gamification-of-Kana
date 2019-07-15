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
              <q-item @click="pushInformation()" clickable>
                <q-item-section>Info</q-item-section>
              </q-item>
              <q-item @click="pushSettings()" clickable>
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
        <q-input v-if="showSignInField" v-model="username" color="white" filled>
          <template v-slot:append>
            <q-btn round dense flat icon="send" @click="signIn()" />
          </template>
        </q-input>
        &nbsp;
        <!-- register button -->
        <q-btn v-if="showRegisterBtn" color="purple" label="Register" @click="pushRegister()" />
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
      console.log('Called showSignInField from Layout')
      this.showSignInBtn = false
      this.showSignInField = true
    },
    signIn () {
      console.log('Called signIn from Layout')
      this.showAvatar = true
      this.showSignInField = false
      this.showRegisterBtn = false
      this.$router.push('/')
    },
    registerSignIn (name) {
      console.log('Called registerSignIn from Layout')
      this.showAvatar = true
      this.showSignInBtn = false
      this.showSignInField = false
      this.showRegisterBtn = false
      this.username = name
    },
    logOut () {
      console.log('Called logOut')
      this.showAvatar = false
      this.showSignInBtn = true
      this.showRegisterBtn = true
      this.username = ''
    },
    // A bunch of one-liner router pushers because generic method has no reactive router
    pushRegister () {
      console.log('Called pushRegister() from Layout')
      this.$router.push('/Register/')
    },
    pushInformation () {
      console.log('Called pushInformation() from Layout')
      this.$router.push('/Information/')
    },
    pushSettings () {
      console.log('Called pushSettings() from Layout')
      this.$router.push('/Settings/')
    }
    /**
    openPage: function (url) {
      this.$root.$emit('openPage', url)
    }
    **/
  }
}
</script>

<style>
</style>
