<template>
  <q-page class="flex flex-center">
    <!-- script display data -->
    <q-select v-model="script1" @input="updateFlashcard()" :options="['hentaigana', 'katakana', 'manyougana-katakana']" label="Script1" />
    <q-select v-model="script2" @input="updateFlashcard()" :options="['hentaigana', 'katakana', 'manyougana-katakana']" label="Script2" />
    <q-input v-model="letter" @input="updateFlashcard()" label="Current Letter" />
    <q-btn class="top-left" id="flip" color="primary" label="Flip" @click="flipCard()" />
    <!-- script display graphics -->
    <character-flashcard path="this.currentLetters1[0]">
    </character-flashcard>
    <!-- logging some information -->
    <q-card>
      Showing Script {{ this.flipped + 1 }}
      <q-tab-panel>
      </q-tab-panel>
    </q-card>
  </q-page>
</template>

<style>
.signup {
  padding: 10px;
}
</style>

<script>
import hentaigana from '../statics/svg/hentaigana.json'
import katakana from '../statics/svg/katakana.json'
import manyouganaKatakana from '../statics/svg/manyougana-katakana.json'
import CharacterFlashcard from '../components/CharacterFlashcard.vue'

export default {
  name: 'PageIndex',
  components: {
    CharacterFlashcard
  },
  data () {
    return {
      letter: '',
      currentLetters1: ['../statics/svg/manyougana-katakana/manyougana-katakana_letter_a.svg'],
      currentLetters2: ['../statics/svg/katakana/katakana_letter_a.svg'],
      script1: 'manyougana-katakana',
      script2: 'katakana',
      flipped: false
    }
  },
  methods: {
    getLetters (letter, script) {
      var suffixes = []
      if (script === 'hentaigana') {
        suffixes = hentaigana[letter]
      } else if (script === 'katakana') {
        suffixes = katakana[letter]
      } else if (script === 'manyougana-katakana') {
        suffixes = manyouganaKatakana[letter]
      } else {
        alert('invalid script input')
        return undefined
      }
      var paths = []
      suffixes.forEach(suffix => paths.push('../statics/svg/' + script + '/' + script + '_letter_' + letter + suffix + '.svg'))
      return paths
    },
    updateFlashcard () {
      this.currentLetters1 = this.getLetters(this.letter, this.script1)
      this.currentLetters2 = this.getLetters(this.letter, this.script2)
      if (this.flipped) {
        this.emit('updateView', this.currentLetters2[0])
      } else {
        this.emit('updateView', this.currentLetters1[0])
      }
    },
    flipCard () {
      if (this.flipped) {
        this.emit('updateView', this.currentLetters1[0])
      } else {
        this.emit('updateView', this.currentLetters2[0])
      }
      this.flipped = !this.flipped
    },
    /**
    openPage (url) {
      this.$router.push(url)
    },
    **/
    emit (arg1, arg2) {
      console.log('called emit(' + arg1 + ', ' + arg2 + ')')
      this.$root.$emit(arg1, arg2)
    }
  }
}
</script>
