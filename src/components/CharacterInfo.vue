<template>
  <span>
    <character-flashcard :imgSrc="imageSrc" :showTitle="true" :background="background" :showScript="false" />
    <q-menu auto-close>
    <span style="position: relative;" class="row">
      <span>
        <character-flashcard :imgSrc="image1" :showTitle="true" :background="background" :showScript="true" />
      </span>
      <span>
        <character-flashcard :imgSrc="image2" :showTitle="true" :background="background" :showScript="true" />
      </span>
    </span>
    </q-menu>
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
      script1: 'katakana',
      script2: 'manyougana-katakana'
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
      if (this.sourceScript === 'manyougana-katakana' && this.highlight) {
        return '../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg'
      } else {
        return '../statics/svg/' + this.sourceScript + '/' + this.sourceScript + '_letter_' + this.letter + '.svg'
      }
    },
    image1 () {
      if (this.script1 === 'manyougana-katakana' && this.highlight) {
        return '../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg'
      } else {
        return '../statics/svg/' + this.script1 + '/' + this.script1 + '_letter_' + this.letter + '.svg'
      }
    },
    image2 () {
      if (this.script2 === 'manyougana-katakana' && this.highlight) {
        return '../statics/svg/manyougana-katakana-c/manyougana-katakana-c_letter_' + this.letter + '.svg'
      } else {
        return '../statics/svg/' + this.script2 + '/' + this.script2 + '_letter_' + this.letter + '.svg'
      }
    }
  },
  methods: {
  }
}
</script>

<style>
</style>
