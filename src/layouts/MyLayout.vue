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
        </q-item>
        <q-item v-if="!showAvatar">
          <q-btn color="green" label="Sign In" @click="showSignIn()" />
        </q-item>
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
      username: ''
    }
  },
  methods: {
    signIn: function (name) {
      console.log('Called signIn')
      this.showAvatar = true
      this.username = name
    },
    showSignIn: function () {
      console.log('Called showSignIn from Layout')
      this.$root.$emit('showSignIn')
    }
  }
}
</script>

<style>
</style>
