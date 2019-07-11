<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
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
            <q-item clickable>
              <q-item-section>Info</q-item-section>
            </q-item>
            <q-item clickable>
              <q-item-section>Settings</q-item-section>
            </q-item>
            <q-item @click="signOut" clickable>
              <q-item-section>Log Out</q-item-section>
            </q-item>
          </q-list>
        </q-menu>
        </q-item>
        <q-btn v-if="!showAvatar" color="green" label="Sign In" @click="unhideSignIn()" />
        <q-input v-if="showSignIn" v-model="username" color="white" filled />
        <q-btn v-if="showSignIn" @click="signIn()" label="Go" />
        &nbsp;
        <q-btn v-if="!showAvatar" color="purple" label="Register" @click="show('register')" />
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
    this.$root.$on('signIn', this.signIn)
  },
  data () {
    return {
      showAvatar: false,
      showSignIn: false,
      username: ''
    }
  },
  methods: {
    signIn: function () {
      console.log('Called signIn')
      this.showAvatar = true
      this.showSignIn = false
      this.$router.push('../')
    },
    signOut: function (name) {
      console.log('Called signOut')
      this.showAvatar = false
      this.username = ''
    },
    show: function (item) {
      console.log('Called show ' + item + ' from Layout')
      this.$root.$emit('show', item)
    },
    unhideSignIn: function () {
      this.showSignIn = true
    }
  }
}
</script>

<style>
</style>
