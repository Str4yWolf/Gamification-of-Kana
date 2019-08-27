<template>
  <q-page class="flex flex-center">
    <transition
      appear
      enter-active-class="animated bounceInRight"
      leave-active-class="animated fadeOut"
    >
    <img class="background-logo" @click="showMessage()" src="../statics/logo.png" alt="Manyougana Logo" width="50%" />
    </transition>
  </q-page>
</template>

<style>
</style>

<script>
export default {
  name: 'PageIndex',
  components: {
  },
  data () {
    return {
    }
  },
  methods: {
    showMessage () {
      alert('Click on you avatar to view the menu')
    }
  }
}
</script>
<style>
img .background-logo :hover {
  background-color: #888888;
  opacity: 50%;
}
</style>
