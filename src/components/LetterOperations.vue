<template>
  <span />
</template>

<script>
import hentaigana from '../statics/svg/hentaigana_hep.json'
import hiragana from '../statics/svg/hiragana_hep.json'
import katakana from '../statics/svg/katakana_hep.json'
import manyouganaKatakana from '../statics/svg/manyougana-katakana_hep.json'
import manyouganaKatakanaC from '../statics/svg/manyougana-katakana-c_hep.json'
import skillLevelDatabaseKeys from '../statics/svg/skill_level_database_keys.json'

export default {
  // name: 'CharacterFlashcard',
  data () {
    return {
      skillLevelKeys: skillLevelDatabaseKeys,
      cache: [] // store keys for duplicate check
    }
  },
  props: {
    highlightManyougana: Boolean,
    skillLevel: Number
  },
  methods: {
    /**
    Return the correct database given a script
    **/
    scriptToData (script) {
      var database = {}
      console.log('highlightManyougana: ' + this.highlightManyougana)
      if (script === 'hentaigana') {
        database = hentaigana
      } else if (script === 'hiragana') {
        database = hiragana
      } else if (script === 'katakana') {
        database = katakana
      } else if (script === 'manyougana-katakana') {
        if (this.highlightManyougana) {
          console.log('database: manyouganaKatakanaC')
          database = manyouganaKatakanaC
        } else {
          console.log('database: manyouganaKatakana')
          database = manyouganaKatakana
        }
      } else if (script === 'manyougana-katakana-c') {
        database = manyouganaKatakanaC
      } else {
        alert('invalid script input')
        database = undefined
      }
      return database
    },
    toggleHighlight () {
      this.highlightManyougana = !this.highlightManyougana
    },
    /**
    Get the letter of an image path
    **/
    getLetterFromPath (path) {
      console.log('called getLetterFromPath(' + path + ')')
      var temp = path.split('/').reverse()[0].split('_letter_')[1].split('.')[0]
      console.log('temp: ' + temp)
      if (temp === undefined) {
        return '' // grey or empty image
      } else if (temp.length === 1) {
        return temp // vowel
      } else {
        return temp.substring(0, 2) // crop numeral suffix if it exists
      }
    },
    /**
    Get an array of svg image paths of given letter and script
    **/
    getLetters (letter, scriptIn) {
      if (letter === '') {
        return ['../statics/grey.png']
      }
      var script = (this.highlightManyougana && scriptIn === 'manyougana-katakana') ? (scriptIn + '-c') : scriptIn
      console.log('called getLetters(' + letter + ', ' + script + ') from LetterOperations')
      var suffixes = this.scriptToData(scriptIn)[letter] // get suffixes of given letter and script
      var paths = []
      // construct an svg image path from each suffix
      suffixes.forEach(suffix => paths.push('../statics/svg/' + script + '/' + script + '_letter_' + letter + suffix + '.svg'))
      return paths
    },
    /**
    Randomly generate an option (get image letter paths) which must not be forbiddenLetter but of given script.
    restricted parameter reduces available options according to current skill level.
    **/
    generateOption (forbiddenLetter, script, restricted, avoidDuplicates) {
      console.log('called generateOption(' + forbiddenLetter + ', ' + script + ') from LetterOperations')
      var datasetKeys = []
      if (restricted) {
        // restricted keys of dataset
        datasetKeys = this.skillLevelKeys[this.skillLevel.toString()]
      } else {
        // dataset and its keys
        var dataset = this.scriptToData(script)
        datasetKeys = Object.keys(dataset)
      }
      // initialize loop
      var randomKey = ''
      var isSameKey = true
      // loop until randomKey != forbiddenLetter; never gets randomKey which is forbiddenLetter
      while (isSameKey) {
        var randomIndex = Math.floor(Math.random() * datasetKeys.length)
        randomKey = datasetKeys[randomIndex]
        isSameKey = (randomKey === forbiddenLetter) // is the randomKey we get the forbiddenLetter
        if (avoidDuplicates) {
          if (this.cache.includes(randomKey)) {
            isSameKey = true
          }
        }
      }
      if (avoidDuplicates) {
        this.cache.push(randomKey)
      }
      return this.getLetters(randomKey, script) // get an option not the forbiddenLetter above but of given script
    },
    /**
    Returns (a path array of) a random letter of the desired script
    **/
    getRandomLetter (script, getPath) {
      console.log('called getRandomLetter(' + script + ', ' + getPath + ') from LetterOperations')
      // dataset and its keys
      var dataset = this.scriptToData(script)
      var datasetKeys = Object.keys(dataset)
      // randomly get a key
      var randomIndex = Math.floor(Math.random() * datasetKeys.length)
      var randomKey = datasetKeys[randomIndex]
      if (getPath) {
        return this.getLetters(randomKey, script) // ultimately get a random letter of given script
      } else {
        return randomKey
      }
    },
    clearCache () {
      this.cache = []
    }
  }
}
</script>

<style>
</style>
