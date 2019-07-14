<template>
  <q-page padding>
    <div>
      Information
      <q-input v-model="username" label="Change name" @click="emit" />
      <q-btn color="primary" label="Reset Account" @click="resetAccount"/>
      <q-btn color="primary" label="Delete Account" @click="deleteAccount" />
    </div>
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
  data () {
    return {
      username: ''
    }
  },
  methods: {
    resetAccount () {
      // confirm thingy
      var confirmation = 0
      if (confirmation) {
        // code to reset your progress
      }
    },
    delecteAccount () {
      // confirm thingy
      var confirmation = 0
      if (confirmation) {
        // code to reset your progress
      }
    }
  }
}
</script>

<style>
</style>
