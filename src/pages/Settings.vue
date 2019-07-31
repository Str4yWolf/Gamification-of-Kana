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
        <span class="row">
          <span>
            <q-btn color="primary" label="Reset Account" @click="resetAccount" style="margin: 2px; width:200px;" />
          </span>
          <span>
            <q-icon name="info" color="red" style="left:9px; top:7px;">
              <q-tooltip style="font-size: 200%;">
                Resets your level, achievements, progress tracking, and preferences.
              </q-tooltip>
            </q-icon>
          </span>
        </span>
        <!-- delete account -->
        <span class="row">
          <span>
            <q-btn color="primary" label="Delete Account" @click="deleteAccount" style="margin: 2px; width:200px;" />
          </span>
          <span>
            <q-icon name="info" color="red" style="left:9px; top:7px;">
              <q-tooltip style="font-size: 200%;">
                Permanently removes your account and associated data from the database. <br />
                Your username will become available for registration again.
              </q-tooltip>
            </q-icon>
          </span>
        </span>
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
</script>

<style>
</style>
