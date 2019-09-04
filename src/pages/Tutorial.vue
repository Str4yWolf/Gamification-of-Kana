<template>
  <q-page class="flex flex-center">
    <img class="background-logo" :src="displayImg" alt="Main Menu Temple" />
    <q-card style="position: absolute; top: 480px; width: 600px; height: 65px; padding: 15px; z-index: 3;">
      <span v-html="displayText" style="display: block; width: 450px;"></span>
      <br />
      <q-btn :disabled="currentIndex < 1" icon="arrow_back" color="green" @click="currentIndex -= 1" style="top: 15px; left: 465px; position: absolute;" />
      <q-btn v-if="!reachedEnd" :disabled="currentIndex === 20" icon="arrow_forward" color="green" @click="currentIndex += 1" style="top: 15px; left: 523px; position: absolute;"  />
      <q-btn v-if="reachedEnd" icon="done" color="green" @click="hidePage()" style="top: 15px; left: 523px; position: absolute;"  />
    </q-card>
  </q-page>
</template>

<style>
</style>

<script>
import tutorialText from '../statics/TutorialText.json'

export default {
  name: 'PageIndex',
  components: {
  },
  data () {
    return {
      currentIndex: 0
    }
  },
  computed: {
    displayText () {
      return tutorialText[this.currentIndex][1]
    },
    displayImg () {
      return tutorialText[this.currentIndex][0]
    },
    reachedEnd () {
      return this.currentIndex === 20
    }
  },
  methods: {
    hidePage () {
      this.$router.push('../')
      setTimeout(this.setShowMenuTrue, 1)
    },
    setShowMenuTrue () {
      this.$root.$emit('setShowMenu', true)
    }
  }
}
</script>

<style>
.background-logo {
  position: absolute;
  top: 0px;
  left: 384px;
  width: 40%;
  z-index: 1;
}
</style>
