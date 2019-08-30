<template>
  <q-page class="flex flex-center">
    <q-card style="width: 300px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
      &nbsp;
      <strong style="font-size: 120%;">Settings</strong>
      <!-- content -->
      <q-item-section>
        <!-- change name -->
        <q-input v-model="username" label="Change name" v-on:keyup.enter="changeName()" style="margin: 2px;">
          <template v-slot:append>
            <q-btn round dense flat icon="send" @click="changeName()" />
          </template>
        </q-input>
        <!-- reset account -->
        <q-btn color="primary" label="Reset Account" @click="resetAccount" style="margin: 2px;" />
        <!-- delete account -->
        <q-btn color="primary" label="Delete Account" @click="deleteAccount" style="margin: 2px;" />
      </q-item-section>
    </q-card>
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
    changeName () {
      console.log('Emitted changeName() from Settings')
      this.$root.$emit('changeName', this.username)
    },
    resetAccount () {
      console.log('Called resetAccount() from Settings')
      var confirmation = confirm('Are you sure you want to reset your account? It cannot be undone!')
      if (confirmation) {
        console.log('resetAccount confirmed')
        this.$root.$emit('resetAccount')
      }
    },
    deleteAccount () {
      console.log('Called deleteAccount() from Settings')
      var confirmation = confirm('Are you sure you want to delete your account? It cannot be undone!')
      if (confirmation) {
        // localStorage.removeItem(username)
        console.log('deleteAccount confirmed')
        this.$root.$emit('deleteAccount')
      }
    }
  }
}
/**
<q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
<q-dialog v-model="viewTutorial">
  <q-card style="width: 600px;">
    <q-card-section>
      <div class="text-h6">Tutorial (Settings)</div>
    </q-card-section>
    <q-card-section>
    You can simply reset your name by typing a new name into the <strong>Text Input Field</strong> and hitting <strong>Enter</strong> on your keyboard or pressing the <strong>Send (<q-icon name="send"/>)</strong> button.
    <br/>
    <br/>
    Your new name must not already be registered on your device.
    <br/>
    <br/>
    Note that upon successful name change, your old name will become available for registration again and may thus be "claimed" by another account.
    <br/>
    <br/>
    By clicking <strong>RESET ACCOUNT</strong>, you will reset your level, achievements, progress tracking, and preferences.
    <br/>
    <br/>
    By clicking <strong>DELETE ACCOUNT</strong>, you will permanently remove your account and associated data from the database. Your username will become available for registration again.
    </q-card-section>
  </q-card>
</q-dialog>
**/
</script>

<style>
</style>
