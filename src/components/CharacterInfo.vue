<template>
  <span>
    <character-flashcard :imgSrc="imageSrc" :showTitle="true" :background="selectableBackground" :showScript="false" @mouseover.native="selected = true" @mouseleave.native="selected = false"/>
    <span v-if="unhideMenu" :style="menuStyle">
      <span>
        <character-flashcard :imgSrc="image1" :showTitle="true" :background="backgroundSelected2" :showScript="true" />
      </span>
      <span style="position: absolute; left: 150px; top: 0px;">
        <character-flashcard :imgSrc="image2" :showTitle="true" :background="backgroundSelected2" :showScript="true" />
      </span>
    </span>
  </span>
</template>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'

export default {
  // name: 'PageName',
  components: {
    CharacterFlashcard
  },
  data () {
    return {
      background: 'background-color: #ffffff;',
      backgroundSelected1: 'background-color: #d8f8f2;',
      backgroundSelected2: 'background-color: #ebfbf4;',
      script1: 'katakana',
      script2: 'manyougana-katakana',
      selected: false
    }
  },
  props: {
    letter: String,
    highlight: Boolean,
    sourceScript: String
  },
  mounted () {
  },
  computed: {
    imageSrc () {
      if (this.letter === '') {
        return '../statics/grey.png'
      } else {
        if (this.sourceScript === 'manyougana-katakana' && this.highlight) {
          return '../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg'
        } else {
          return '../statics/svg/' + this.sourceScript + '/' + this.sourceScript + '_letter_' + this.letter + '.svg'
        }
      }
    },
    image1 () {
      if (this.letter === '') {
        return '../statics/grey.png'
      } else {
        if (this.script1 === 'manyougana-katakana' && this.highlight) {
          return '../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg'
        } else {
          return '../statics/svg/' + this.script1 + '/' + this.script1 + '_letter_' + this.letter + '.svg'
        }
      }
    },
    image2 () {
      if (this.letter === '') {
        return '../statics/grey.png'
      } else {
        if (this.script2 === 'manyougana-katakana' && this.highlight) {
          return '../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg'
        } else {
          return '../statics/svg/' + this.script2 + '/' + this.script2 + '_letter_' + this.letter + '.svg'
        }
      }
    },
    letterIsEmpty () {
      return this.letter === ''
    },
    selectableBackground () {
      if (this.selected) {
        return this.backgroundSelected1
      } else {
        return this.background
      }
    },
    unhideMenu () {
      return !this.letterIsEmpty && this.selected
    },
    menuStyle () {
      if (this.selected) {
        return 'position: absolute; z-index: 1'
      } else {
        return ''
      }
    }
  },
  methods: {
  }
}
</script>

<style>
</style>
