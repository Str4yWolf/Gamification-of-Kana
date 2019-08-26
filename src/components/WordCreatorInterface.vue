<template>
  <q-page class="flex flex-center" ref="modal" tabindex="0" @keyup="validateKeyInput">
    <q-card style="width: 820px; padding: 30px;">
      <span class="row">
        <span>
          <!-- header -->
          <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideWordCreator')" />
          &nbsp;
          <strong style="font-size: 120%;">Word Creator</strong>
        </span>
        <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
        <!-- script selection -->
        <span style="padding: 0px 20px 0px 40px;">
          <q-select v-model="script" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script" style="width:200px;" />
        </span>
        <!-- Control buttons -->
        <span style="padding: 15px;">
          <q-btn color="green" label="New Word" title="Get a new word (n)" @click="newWord()" />
          <q-btn color="green" label="Enter" title="Enter answers (Enter)" @click="enter()" :disabled="disableOptions" />
        </span>
        <span class="row" style="position: absolute; top: 100px; left: 440px;">
          <!-- manyougana highlight toggle -->
          <q-toggle
            v-model="highlightManyougana"
            color="red"
            label="Highlight Manyougana"
          />
          <!-- show Japanese toggle -->
          <q-toggle
            v-model="showJapanese"
            color="red"
            label="Japanese Hint"
          />
        </span>
      </span>
      <br />
  <word-creator :userObj="userObj" :script="script" :showJapanese="showJapanese" ref="InterfaceWC" />
  <q-dialog v-model="viewTutorial">
    <q-card style="width: 600px;">
      <q-card-section>
        <div class="text-h6">Tutorial (Word Creator)</div>
      </q-card-section>
      <q-card-section>
      Use <strong>Word Creator</strong> to get comfortable spelling Japanese words using Japanese letters of a given script.
      <br/>
      <br/>
      First of all, choose a <strong>Script</strong> you want to use. Press the <strong>NEW WORD</strong> button or <strong>N</strong> on your keyboard to generate a question.
      <br/><br/>
      You will be given the <strong>English</strong> word which you have to spell in <strong>Japanese</strong>. You may always toggle <strong>Japanese Hint</strong> to show the Japanese word in <strong><abbr title="shi chi tsu fu, rather than si ti tu hu">Hepburn</abbr></strong> spelling.
      <br/><br/>
      Spell the Japanese word successively by selecting from the <strong>Option</strong> buttons below or type in one of <strong>1, 2, 3, 4</strong> on your keyboard (not the keys of a NumPad). Hit the <strong>ENTER</strong> button or <strong>Enter</strong> on your keyboard to submit your solution.
      <br/><br/>
      You will be given corrective feedback and shown the <strong><abbr title="One Latin Romanization of Japanese">Romaji</abbr></strong> of each character. The correct solution will be displayed alongside your solution. You may proceed with generating new questions from now on.
      <br/><br/>
      <strong>Tip:</strong> To highlight the parts of manyougana katakana were derived from, you can toggle <strong>Highlight Manyougana</strong> at any time.
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
import WordCreator from '../components/WordCreator.vue'

export default {
  // name: 'PageName',
  components: {
    WordCreator
  },
  data () {
    return {
      // current params
      script: 'katakana',
      disableOptions: true,
      showJapanese: false,
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
  },
  methods: {
    /**
    Validate user keyboard input
    **/
    validateKeyInput (event) {
      switch (event.keyCode) {
        // keyboard numbers 1 - 4
        case 49:
        case 50:
        case 51:
        case 52:
          if (!this.disableOptions) {
            console.log('called validateKeyInput with 1-4')
            this.$refs.InterfaceWC.validateOption(event.keyCode - 48)
          } else {
            console.log('Validation is in progress. Options unusable.')
          }
          break
        // keyboard Enter key
        case 13:
          console.log('pressed enter in validateKeyInput')
          if (!this.disableOptions) {
            this.enter()
          }
          break
        // new word
        case 78:
          console.log('pressed n in validateKeyInput')
          this.newWord()
          break
        // log all other keys
        default:
          console.log('called validateKeyInput with key')
          console.log(event.key)
          console.log('and keyCode')
          console.log(event.keyCode)
      }
    },
    newWord () {
      this.disableOptions = false
      this.$refs.InterfaceWC.setNewCreation()
    },
    enter () {
      this.disableOptions = true
      this.$refs.InterfaceWC.endCreation()
    }
  }
}
</script>

<style>
</style>
