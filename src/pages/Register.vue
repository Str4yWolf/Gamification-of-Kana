<template>
  <q-page class="flex flex-center">
    <q-card class="signup">
      <p>
      <q-input v-model="username" label="Your Name" />
      <br />
      <q-btn id="signup-enter" color="primary" label="Enter" @click="validateSignup()"/> &nbsp;
      <q-btn color="white" text-color="black" label="Cancel" @click="cancelSignup()"/>
      </p>
    </q-card>
  </q-page>
</template>

<style>
.signup {
  padding: 10px;
}
</style>

<script>

export default {
  name: 'Register',
  data () {
    return {
      username: ''
    }
  },
  methods: {
    validateSignup () {
      console.log('Logging validated signup: \'' + this.username + '\'')
      if (this.username === '') {
        alert('Please enter a name or click "Cancel" to continue without tracking your progress.')
      } else {
        alert('Registration successful')
        this.signupVisible = false
        this.$root.$emit('signIn', this.username)
        this.$router.push('../')
      }
    },
    cancelSignup () {
      console.log('Cancelling signup')
      alert('Registration cancelled. Progress will not be tracked.')
      this.signupVisible = false
      this.$router.push('../')
    }
  }
}
</script>
