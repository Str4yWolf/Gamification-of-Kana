<template>
  <span />
</template>

<script>
import hentaigana from '../statics/svg/hentaigana.json'
import hiragana from '../statics/svg/hiragana.json'
import katakana from '../statics/svg/katakana.json'
import manyouganaKatakana from '../statics/svg/manyougana-katakana.json'

export default {
  // name: 'CharacterFlashcard',
  data () {
    return {}
  },
  methods: {
    /**
    Return the correct database given a script
    **/
    scriptToData (script) {
      var database = {}
      if (script === 'hentaigana') {
        database = hentaigana
      } else if (script === 'hiragana') {
        database = hiragana
      } else if (script === 'katakana') {
        database = katakana
      } else if (script === 'manyougana-katakana') {
        database = manyouganaKatakana
      } else {
        alert('invalid script input')
        database = undefined
      }
      return database
    },
    /**
    Get an array of svg image paths of given letter and script
    **/
    getLetters (letter, script) {
      console.log('called getLetters(' + letter + ', ' + script + ') from MultipleChoice')
      var suffixes = this.scriptToData(script)[letter] // get suffixes of given letter and script
      var paths = []
      // construct an svg image path from each suffix
      suffixes.forEach(suffix => paths.push('../statics/svg/' + script + '/' + script + '_letter_' + letter + suffix + '.svg'))
      return paths
    },
    /**
    Randomly generate an option (get image letter paths) which must not be forbiddenLetter but of given script
    **/
    generateOption (forbiddenLetter, script) {
      console.log('called generateOption(' + forbiddenLetter + ', ' + script + ') from MultipleChoice')
      // dataset and its keys
      var dataset = this.scriptToData(script)
      var datasetKeys = Object.keys(dataset)
      // initialize loop
      var randomKey = ''
      var isSameKey = true
      // loop until randomKey != forbiddenLetter; never gets randomKey which is forbiddenLetter
      while (isSameKey) {
        var randomIndex = Math.floor(Math.random() * datasetKeys.length)
        randomKey = datasetKeys[randomIndex]
        isSameKey = (randomKey === forbiddenLetter) // is the randomKey we get the forbiddenLetter
      }
      return this.getLetters(randomKey, script) // get an option not the forbiddenLetter above but of given script
    }
  }
}
</script>

<style>
</style>
