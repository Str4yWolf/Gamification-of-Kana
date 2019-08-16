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
        <!-- script selection -->
        <span style="padding: 0px 20px 0px 40px;">
          <q-select v-model="script" :options="['hentaigana', 'hiragana', 'katakana', 'manyougana-katakana', 'manyougana-katakana-c']" label="Script" style="width:200px;" />
        </span>
        <!-- Control buttons -->
        <span style="padding: 15px;">
          <q-btn color="green" label="New Word" title="Get a new word (n)" @click="newWord()" />
          <q-btn color="green" label="Enter" title="Enter answers (Enter)" @click="enter()" :disabled="disableOptions" />
          <q-btn color="green" label="Show Japanese" title="Show Japanese word (j)" @click="$refs.InterfaceWC.showJapanese()" :disable="disableOptions" />
        </span>
      </span>
      <br />
    <letter-operations :highlight="false" :skillLevel="userObj['skillLvl']" ref="WCOps" />
  <word-creator :userObj="userObj" :script="script" ref="InterfaceWC" />
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
      disableOptions: true
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
        // show tip
        case 74:
          console.log('pressed j in validateKeyInput')
          if (!this.disableOptions) {
            this.$refs.InterfaceWC.showJapanese()
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
