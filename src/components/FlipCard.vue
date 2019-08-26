<template>
  <q-page class="flex flex-center">
    <q-card style="width: 252px; height: 475px; padding: 30px;">
      <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideFlipCard')" style="position: absolute; top: 34px; left: 20px;" />
      <strong style="font-size: 120%; display: flex; justify-content: center;">Simple Flashcard</strong>
      <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" style="position: absolute; top: 34px; right: 20px;" />
      <!-- logging some information -->
      <q-item-label style="display: flex; justify-content: center;">
        Script{{ this.flipped + 1 }}
      </q-item-label>
      <!-- script display graphics -->
      <character-flashcard :img-src="currentImage" :showTitle="true" style="left:21px;" />
      <!-- script display data -->
      <!-- flow simplification -->
      <!-- enabled: scripts: katakana, manyougana-katakana disabled scripts: hentaigana, hiragana -->
      <q-item-section v-on:keyup.enter="flipCardOver()">
        <q-select v-model="script1" @input="updateFlashcard()" :options="['katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script1" />
        <q-select v-model="script2" @input="updateFlashcard()" :options="['katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script2" />
      </q-item-section>
      <q-item-section>
        <q-input v-model="letter" @input="updateFlashcard()" v-on:keyup.enter="flipCardOver()" label="Current Letter" />
        <q-btn class="top-left" id="flip" style="margin: 10px 0px 5px 0px;" color="primary" label="Flip" @click="flipCardOver()" />
      </q-item-section>
    </q-card>
    <q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Simple Flashcard)</div>
        </q-card-section>
        <q-card-section>
        Use <strong>Simple Flashcard</strong> to view a Japanese letter in different scripts.
        <br/>
        <br/>
        You can type the <strong><abbr title="shi chi tsu fu, rather than si ti tu hu">Hepburn</abbr></strong> version of your desired letter in the <strong>Current Letter</strong> input field.
        <br/><br/>
        <strong>Script1</strong> is the front and <strong>Script2</strong> is the back side of the flashcard. These sides show whatever script you configure in the respective dropdowns.
        <br/><br/>
        Press the <strong>FLIP</strong> button or <strong>Enter</strong> on your keyboard to "flip" the flashcard. You can see the active script just above the character image. <br/>
        </q-card-section>
      </q-card>
    </q-dialog>
    <letter-operations :highlight="false" :skillLevel="9" ref="IndexOps" />
  </q-page>
</template>

<style>
</style>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import LetterOperations from '../components/LetterOperations.vue'

export default {
  name: 'FlipCard',
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
      currentImage: '../statics/grey.png',
      flipped: false,
      viewTutorial: false
    }
  },
  mounted () {
    if (this.userObj.viewedTutorial[1] === false) {
      this.userObj.viewedTutorial[1] = true
      this.viewTutorial = true
      this.$root.$emit('updateDatabase')
    }
  },
  methods: {
    updateFlashcard () {
      this.currentLetters1 = this.$refs.IndexOps.getLetters(this.letter, this.script1, false)
      this.currentLetters2 = this.$refs.IndexOps.getLetters(this.letter, this.script2, false)
      if (this.flipped) {
        this.currentImage = this.currentLetters2[0]
      } else {
        this.currentImage = this.currentLetters1[0]
      }
    },
    flipCardOver () {
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
