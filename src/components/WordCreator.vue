<template>
  <q-page class="flex flex-center">
    <q-card style="width: 800px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideWordCreator')" />
      &nbsp;
      <strong style="font-size: 120%;">Word Creator</strong>
      <!-- script selection -->
        <span>
          <q-select v-model="script" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana']" label="Script" style="width:200px;" />
        </span>
      <p>Please spell {{currentWordEng}} in Japanese using {{script}}. </p>
      <q-btn color="primary" label="Random" @click="setRandomWord()" />
    </q-card>
  </q-page>
</template>

<script>
// import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import words from '../statics/wordCreatorWords.json'
export default {
  // name: 'PageName',
  components: {
    // CharacterFlashcard
  },
  data () {
    return {
      currentWordEng: 'wolf',
      script: 'katakana'
    }
  },
  props: {
  },
  created () {
  },
  computed: {
    currentWordJap () {
      return words[this.currentWordEng]
    },
    currentWordLength () {
      return this.currentWordJap.length
    }
  },
  methods: {
    getRandomWord (getKey) {
      var wordsKeys = Object.keys(words)
      var randomIndex = Math.floor(Math.random() * wordsKeys.length)
      var randomKey = wordsKeys[randomIndex]
      if (getKey) {
        return randomKey
      } else {
        return words[randomKey]
      }
    },
    setRandomWord () {
      this.currentWordEng = this.getRandomWord(true)
    }
  }
}
</script>

<style>
</style>
