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
    <letter-operations :highlightManyougana="false" :skillLevel="9" ref="a" />
  </span>
</template>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import LetterOperations from '../components/LetterOperations.vue'

export default {
  // name: 'PageName',
  components: {
    CharacterFlashcard,
    LetterOperations
  },
  data () {
    return {
      background: 'background-color: #ffffff;',
      backgroundSelected1: 'background-color: #d8f8f2;',
      backgroundSelected2: 'background-color: #ebfbf4;',
      script1: 'manyougana-katakana',
      script2: 'katakana',
      selected: false
    }
  },
  props: {
    letter: String,
    highlight: Boolean,
    sourceScript: String,
    scripts: Array
  },
  mounted () {
  },
  computed: {
    imageSrc () {
      if (this.letter === '') {
        return '../statics/grey.png'
      } else if (this.sourceScript === 'manyougana-katakana' && this.highlight) {
        return ('../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg')
      } else {
        var fileFormat = ((this.sourceScript === 'romaji') ? '.png' : '.svg')
        return ('../statics/svg/' + this.sourceScript + '/' + this.sourceScript + '_letter_' + this.letter + fileFormat)
      }
    },
    image1 () {
      if (this.letter === '') {
        return '../statics/grey.png'
      } else if (this.scripts[0] === 'manyougana-katakana' && this.highlight) {
        return ('../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg')
      } else {
        var fileFormat = ((this.scripts[0] === 'romaji') ? '.png' : '.svg')
        return ('../statics/svg/' + this.scripts[0] + '/' + this.scripts[0] + '_letter_' + this.letter + fileFormat)
      }
    },
    image2 () {
      if (this.letter === '') {
        return '../statics/grey.png'
      } else if (this.scripts[1] === 'manyougana-katakana' && this.highlight) {
        return ('../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg')
      } else {
        var fileFormat = ((this.scripts[1] === 'romaji') ? '.png' : '.svg')
        return ('../statics/svg/' + this.scripts[1] + '/' + this.scripts[1] + '_letter_' + this.letter + fileFormat)
      }
    },
    /**
    component hasn't been rendered yet
    imageSrc () {
      return this.$refs.a.getLetters(this.letter, this.sourceScript)[0]
    },
    image1 () {
      return this.$refs.a.getLetters(this.letter, this.scripts[0])[0]
    },
    image2 () {
      return this.$refs.a.getLetters(this.letter, this.scripts[1])[0]
    },
    **/
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
