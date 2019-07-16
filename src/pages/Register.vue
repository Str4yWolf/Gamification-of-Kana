<template>
  <q-page class="flex flex-center">
    <!-- entire registration card -->
    <q-card class="register">
      <!-- label -->
      <strong style="font-size: 100%;">Registration</strong>
      <p>
        <!-- username register panel -->
        <q-input v-model="username" label="Your Name" v-on:keyup.enter="validateRegistration()" >
          <!-- containing field -->
          <template v-slot:append>
            <q-icon name="info" color="red">
              <q-tooltip style="font-size: 200%;">
                Upon registration, you will be able to save and track your progress. <br />
                You can change your name or delete your account at any time.
              </q-tooltip>
            </q-icon>
          </template>
        </q-input>
        <br />
        <!-- confirm registration -->
        <q-btn id="signup-enter" color="primary" label="Enter" @click="validateRegistration()"/>
        &nbsp;
        <!-- cancel registration -->
        <q-btn color="white" text-color="black" label="Cancel" @click="cancelRegistration()"/>
      </p>
    </q-card>
  </q-page>
</template>

<style>
.register {
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
    validateRegistration () {
      console.log('Called validateRegistration from Register with name ' + this.username)
      if (this.username === '') {
        alert('Please enter a name or click "Cancel" to proceed without registration.')
      } else {
        alert('Registration successful')
        this.$root.$emit('registerSignIn', this.username)
        this.$router.push('../')
      }
    },
    cancelRegistration () {
      console.log('Called cancelRegistration from Register')
      this.username = ''
      this.$router.push('../')
    }
  }
}
</script>
