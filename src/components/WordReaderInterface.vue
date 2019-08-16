<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 820px; padding: 30px;">
      <span class="row">
        <span>
          <!-- header -->
          <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideWordReader')" />
          &nbsp;
          <strong style="font-size: 120%;">Word Reader</strong>
        </span>
        <!-- script selection -->
        <span style="padding: 0px 20px 0px 40px;">
          <q-select v-model="script" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script" style="width:200px;" />
        </span>
        <!-- Control buttons -->
        <span style="padding: 15px;">
          <q-btn v-if="!questionInProgress" color="green" label="New Word" title="Get new word (Enter)" @click="newQuestion()" />
          <q-btn v-if="questionInProgress" color="green" label="Enter" title="Enter answers (Enter)" @click="enterSolution()" />
        </span>
      </span>
    <word-reader :userObj="userObj" :script="script" ref="InterfaceWR" />
    </q-card>
  </q-page>
</template>

<script>
import WordReader from '../components/WordReader.vue'

export default {
  // name: 'PageName',
  components: {
    WordReader
  },
  data () {
    return {
      // current params
      script: 'katakana',
      questionInProgress: false
    }
  },
  computed: {
  },
  props: {
    userObj: Object
  },
  created () {
  },
  mounted () {
    this.$refs.modal.$el.focus()
  },
  methods: {
    /**
    Validate user keyboard input
    **/
    validateKeyInput (event) {
      switch (event.keyCode) {
        // keyboard Enter key
        case 13:
          console.log('pressed enter in validateKeyInput')
          if (this.questionInProgress) {
            this.enterSolution()
          } else {
            this.newQuestion()
          }
          break
        // log all other keys
        default:
          console.log('called validateKeyInput with key')
          console.log(event.key)
          console.log('and keyCode')
          console.log(event.keyCode)
      }
    },
    newQuestion () {
      this.questionInProgress = true
      this.$refs.InterfaceWR.generateQuestion()
    },
    enterSolution () {
      this.questionInProgress = false
      this.$refs.InterfaceWR.validateSolution()
    }
  }
}
</script>

<style>
</style>
