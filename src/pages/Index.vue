<template>
  <q-page class="flex flex-center">
    <q-select v-model="script1" @input="updateFlashcard()" :options="['hentaigana', 'katakana', 'manyougana-katakana']" label="Script1" />
    <q-select v-model="script2" @input="updateFlashcard()" :options="['hentaigana', 'katakana', 'manyougana-katakana']" label="Script2" />
    <q-input v-model="letter" @input="updateFlashcard()" label="Current Letter" />
    <q-btn class="top-left" id="flip" color="primary" label="Flip" @click="flipCard()" />
    <span v-if="signupVisible">
      <q-card class="signup">
        <p>
        <q-input v-model="username" label="Your Name" />
        <br />
        <q-btn id="signup-enter" color="primary" label="Enter" @click="validateSignup()"/> &nbsp;
        <q-btn color="white" text-color="black" label="Cancel" @click="cancelSignup()"/>
        </p>
      </q-card>
    </span>
    <character-flashcard path="this.currentLetters1[0]">
    </character-flashcard>
    <q-card>
      Showing Script {{ this.flipped + 1 }}
    </q-card>
    <!-- <q-card v-for="i in currentLetters1" :key="'currentLetter1' + i">
      <div>
        <img src="currentLetters1[i]" height="auto" width="auto" />
      </div>
    </q-card> -->
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
  created () {
    this.$root.$on('show', this.show)
  },
  data () {
    return {
      username: '',
      signupVisible: false,
      letter: '',
      currentLetters1: ['../statics/svg/manyougana-katakana/manyougana-katakana_letter_a.svg'],
      currentLetters2: ['../statics/svg/katakana/katakana_letter_a.svg'],
      script1: 'manyougana-katakana',
      script2: 'katakana',
      flipped: false
    }
  },
  methods: {
    show (item) {
      console.log('showing ' + item)
      if (item === 'signIn') {
        // this.signupVisible = true
        this.$router.push('/Register/')
      } else if (item === 'register') {
        // this.signupVisible = true
        this.$router.push('/Register/')
      }
    },
    validateSignup () {
      console.log('Logging validated signup: \'' + this.username + '\'')
      if (this.username === '') {
        alert('Please enter a name or click "Cancel" to not track your progress.')
      } else {
        alert('Registration successful')
        this.signupVisible = false
        this.emit('signIn', this.username)
      }
    },
    cancelSignup () {
      console.log('Cancelling signup')
      alert('Progress will not be tracked.')
      this.signupVisible = false
    },
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
      console.log(paths)
      return paths
    },
    flipCard () {
      if (this.flipped) {
        this.emit('updateView', this.currentLetters1[0])
      } else {
        this.emit('updateView', this.currentLetters2[0])
      }
      this.flipped = !this.flipped
    },
    updateFlashcard () {
      console.log('before - this.currentLetters1: ' + this.currentLetters1)
      this.currentLetters1 = this.getLetters(this.letter, this.script1)
      this.currentLetters2 = this.getLetters(this.letter, this.script2)
      console.log('after - this.currentLetters1: ' + this.currentLetters1)
      console.log('this.currentLetters1[0]: ' + this.currentLetters1[0])
      console.log('this.currentLetters1[0]: ' + typeof this.currentLetters1[0])
      if (this.flipped) {
        this.emit('updateView', this.currentLetters2[0])
      } else {
        this.emit('updateView', this.currentLetters1[0])
      }
    },
    emit (arg1, arg2) {
      console.log('called emit(' + arg1 + ', ' + arg2 + ')')
      this.$root.$emit(arg1, arg2)
    }
  }
}
</script>
