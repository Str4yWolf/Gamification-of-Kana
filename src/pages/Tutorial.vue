<template>
  <q-page class="flex flex-center">
    <q-card style="width: 600px; height: 400px; padding: 15px; font-weight: bold;">
      <span v-html="displayText"></span>
      <br />
      <q-btn :disabled="currentIndex < 1" icon="arrow_back" color="green" @click="currentIndex -= 1" style="top: 350px; position: absolute;" />
      <q-btn :disabled="currentIndex > 3" icon="arrow_forward" color="green" @click="currentIndex += 1" style="top: 350px; left: 73px; position: absolute;"  />
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
      username: 'Legosi',
      goalScript: 'manyougana-katakana',
      currentIndex: 0
    }
  },
  computed: {
    displayText () {
      return tutorialText[this.currentIndex]
    }
  },
  methods: {
  }
}
</script>
