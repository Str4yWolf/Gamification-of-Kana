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
        <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
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
    <q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Word Reader)</div>
        </q-card-section>
        <q-card-section>
        Use <strong>Word Reader</strong> to become more fluent in reading Japanese letters of a given script.
        <br/>
        <br/>
        First of all, choose a <strong>Script</strong> you want to use. Press the <strong>NEW WORD</strong> button or <strong>N</strong> on your keyboard to generate a question.
        <br/><br/>
        You will be shown a word spelled with Japanese letters of your desired script. in the <strong>Text Field (Enter solution)</strong>, type in the <strong><abbr title="One Latin Romanization of Japanese">Romaji</abbr></strong> of the word in <strong><abbr title="shi chi tsu fu, rather than si ti tu hu">Hepburn</abbr></strong>. Don't use any delimiters such as spaces ' ' or commas ','.
        <br/><br/>
        Hit the <strong>ENTER</strong> button or <strong>Enter</strong> on your keyboard to submit your solution.
        <br/><br/>
        You will be given corrective feedback and shown the <strong><abbr title="One Latin Romanization of Japanese">Romaji</abbr></strong> of each character. The correct solution will be displayed alongside your solution on the Feedback. You may proceed with generating new questions from now on.
        <br/><br/>
        <strong>Remarks:</strong> Your <strong>Skill Level</strong> determines how many of the 48 Japanese letters will be quizzed, which in turn determines the words and word length you will be asked.
        <br/>
        </q-card-section>
      </q-card>
    </q-dialog>
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
      questionInProgress: false,
      //
      viewTutorial: false
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
    if (this.userObj.viewedTutorial[4] === false) {
      this.userObj.viewedTutorial[4] = true
      this.viewTutorial = true
      this.$root.$emit('updateDatabase')
    }
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
