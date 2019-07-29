<template>
  <q-page class="flex flex-center">
    <q-card style="padding: 15px;">
      <!-- logging some information -->
      <q-item-label>
        Showing Script{{ this.flipped + 1 }}
      </q-item-label>
      <!-- script display graphics -->
      <character-flashcard :img-src="currentImage" style="left:15px;" />
      <!-- script display data -->
      <q-item-section v-on:keyup.enter="flipCard()">
        <q-select v-model="script1" @input="updateFlashcard()" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana']" label="Script1" />
        <q-select v-model="script2" @input="updateFlashcard()" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana']" label="Script2" />
      </q-item-section>
      <q-item-section>
        <q-input v-model="letter" @input="updateFlashcard()" v-on:keyup.enter="flipCard()" label="Current Letter" />
        <q-btn class="top-left" id="flip" style="margin: 5px 0px 5px 0px;" color="primary" label="Flip" @click="flipCard()" />
      </q-item-section>
    </q-card>
  </q-page>
</template>

<style>
</style>

<script>
// allow for hepburn input as well
import hentaigana from '../statics/svg/hentaigana_hep.json'
import hiragana from '../statics/svg/hiragana_hep.json'
import katakana from '../statics/svg/katakana_hep.json'
import manyouganaKatakana from '../statics/svg/manyougana-katakana_hep.json'
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
      currentImage: 'asf',
      flipped: false
    }
  },
  methods: {
    getLetters (letter, script) {
      var suffixes = []
      if (script === 'hentaigana') {
        suffixes = hentaigana[letter]
      } else if (script === 'hiragana') {
        suffixes = hiragana[letter]
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
        this.currentImage = this.currentLetters2[0]
      } else {
        this.currentImage = this.currentLetters1[0]
      }
    },
    flipCard () {
      if (this.flipped) {
        this.currentImage = this.currentLetters1[0]
      } else {
        this.currentImage = this.currentLetters2[0]
      }
      this.flipped = !this.flipped
    },
    emit (arg1, arg2) {
      console.log('called emit(' + arg1 + ', ' + arg2 + ')')
      this.$root.$emit(arg1, arg2)
    }
  }
}
</script>
