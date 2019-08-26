<template>
  <q-page class="flex flex-center">
    <!-- entire registration card -->
    <q-card class="register">
      <!-- label -->
      <strong style="font-size: 100%;">Registration</strong>
      <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
      <p>
        <!-- username register panel -->
        <q-input v-model="username" label="Your Name" v-on:keyup.enter="validateRegistration()" >
        </q-input>
        <br />
        <!-- confirm registration -->
        <q-btn id="signup-enter" color="primary" label="Enter" @click="validateRegistration()"/>
        &nbsp;
        <!-- cancel registration -->
        <q-btn color="white" text-color="black" label="Cancel" @click="cancelRegistration()"/>
      </p>
      <q-dialog v-model="viewTutorial">
        <q-card style="width: 600px;">
          <q-card-section>
            <div class="text-h6">Tutorial (Register)</div>
          </q-card-section>
          <q-card-section>
          Register to save and track your progress.
          <br/><br/>
          Type in your name in the <strong>Text Input</strong> field. Click the <strong>ENTER</strong> button or hit <strong>Enter</strong> on your keyboard to proceed, or click the <strong>Cancel</strong> button to return.
          <br/><br/>
          Your name will be unique and cannot be registered by another user on the same device.
          <br/><br/>
          You can change your name or delete your account at any time under <strong>Settings</strong>, thereby making your account name free to register again.
          </q-card-section>
        </q-card>
      </q-dialog>
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
      username: '',
      viewTutorial: false
    }
  },
  methods: {
    validateRegistration () {
      console.log('Called validateRegistration from Register with name ' + this.username)
      if (this.username === '') {
        alert('Please enter a name or click "Cancel" to proceed without registration.')
      } else {
        this.$root.$emit('registerSignIn', this.username)
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
