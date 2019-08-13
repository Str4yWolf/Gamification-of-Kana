<template>
  <q-page class="flex flex-center">
    <q-card style="padding: 15px;">
      <!-- logging some information -->
      <q-item-label>
        Showing Script{{ this.flipped + 1 }}
      </q-item-label>
      <!-- script display graphics -->
      <character-flashcard :img-src="currentImage" :showTitle="true" style="left:15px;" />
      <!-- script display data -->
      <!-- flow simplification -->
      <!-- enabled: scripts: katakana, manyougana-katakana disabled scripts: hentaigana, hiragana -->
      <q-item-section v-on:keyup.enter="flipCard()">
        <q-select v-model="script1" @input="updateFlashcard()" :options="['katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script1" />
        <q-select v-model="script2" @input="updateFlashcard()" :options="['katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script2" />
      </q-item-section>
      <q-item-section>
        <q-input v-model="letter" @input="updateFlashcard()" v-on:keyup.enter="flipCard()" label="Current Letter" />
        <q-btn class="top-left" id="flip" style="margin: 5px 0px 5px 0px;" color="primary" label="Flip" @click="flipCard()" />
      </q-item-section>
    </q-card>
    <letter-operations ref="IndexOps" />
  </q-page>
</template>

<style>
</style>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import LetterOperations from '../components/LetterOperations.vue'

export default {
  name: 'PageIndex',
  components: {
    CharacterFlashcard,
    LetterOperations
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
    updateFlashcard () {
      this.currentLetters1 = this.$refs.IndexOps.getLetters(this.letter, this.script1)
      this.currentLetters2 = this.$refs.IndexOps.getLetters(this.letter, this.script2)
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
    }
  }
}
</script>
