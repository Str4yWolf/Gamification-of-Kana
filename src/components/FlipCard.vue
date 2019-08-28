<template>
  <q-page class="flex flex-center">
    <q-card :style="pageStyle">
      <q-btn v-if="!isTutorial" round dense flat icon="keyboard_backspace" @click="$root.$emit('hideFlipCard')" style="position: absolute; top: 34px; left: 20px;" />
      <strong style="font-size: 120%; display: flex; justify-content: center;">Smart Flashcard</strong>
      <!-- logging some information -->
      <q-item-label style="display: flex; justify-content: center;">
        <strong>{{flashcardSide}}</strong>
      </q-item-label>
      <!-- script display graphics -->
      <!--
      Transition TBD
      <transition name="fade">
        <character-flashcard v-if="!flipped" :img-src="currentLetters1[0]" :showTitle="true" :showScript="true" style="left:21px;" />
      </transition>
      <transition name="fade">
        <character-flashcard v-if="flipped" :img-src="currentLetters2[0]" :showTitle="true" :showScript="true" style="left:21px;" />
      </transition>
      -->
      <character-flashcard v-if="!flipped" :img-src="currentLetters1[0]" :showTitle="true" :showScript="true" style="left:21px;" />
      <character-flashcard v-if="flipped" :img-src="currentLetters2[0]" :showTitle="true" :showScript="true" style="left:21px;" />
      <!--<character-flashcard :img-src="currentImage" :showTitle="true" :showScript="true" style="left:21px;" />-->
      <!-- script display data -->
      <!-- flow simplification -->
      <!-- enabled: scripts: katakana, manyougana-katakana disabled scripts: hentaigana, hiragana -->
      <q-item-section>
        <q-input v-model="letter" @input="updateFlashcard()" v-on:keyup.enter="manualFlip()" label="Current Letter" />
        <q-btn class="top-left" id="flip" style="margin: 10px 0px 5px 0px;" color="primary" label="Flip" @click="manualFlip()" :disabled="autoflip" />
        <q-btn class="top-left" style="margin: 0px 0px 5px 0px;" color="green" label="Next" @click="getNextLetter()" />
      </q-item-section>
      <q-expansion-item
          expand-separator
          icon="settings"
          label="Customize"
          v-model="showOptions"
       >
        <q-item-section>
          <span v-if="!isTutorial">
            <q-select v-model="script1" @input="updateFlashcard()" :options="['katakana', 'manyougana-katakana']" label="Front" />
            <q-select v-model="script2" @input="updateFlashcard()" :options="['katakana', 'manyougana-katakana']" label="Back" />
          </span>
          <span style="position: relative; padding: 10px;"/>
          <q-toggle
            v-model="highlightManyougana"
            color="red"
            label="Highlight Manyougana"
            @input="updateFlashcard()"
          />
          <q-toggle
            v-model="autoflip"
            color="blue"
            label="Auto-Flip"
            @input="timedFlip()"
          />
          <q-toggle
            v-model="randomizedNextLetter"
            color="green"
            label="Randomize NEXT"
          />
        </q-item-section>
      </q-expansion-item>
    </q-card>
    <!--
    Doesn't work for whatever reason
    <letter-operations :highlightManyougana="highlightManyougana" :skillLevel="9" ref="IndexOps" />
    -->
    <letter-operations :highlightManyougana="false" :skillLevel="9" ref="IndexOps" />
  </q-page>
</template>

<style>
</style>

<script>
import CharacterFlashcard from '../components/CharacterFlashcard.vue'
import LetterOperations from '../components/LetterOperations.vue'
import skillLevelDatabaseKeys from '../statics/svg/skill_level_database_keys.json'
import skillLevelDatabaseKeysDisjoint from '../statics/svg/skill_level_database_keys_disjoint.json'

export default {
  name: 'FlipCard',
  components: {
    CharacterFlashcard,
    LetterOperations
  },
  data () {
    return {
      letter: 'a',
      currentLetters1: ['../statics/svg/manyougana-katakana/manyougana-katakana_letter_a.svg'],
      currentLetters2: ['../statics/svg/katakana/katakana_letter_a.svg'],
      script1: 'manyougana-katakana',
      script2: 'katakana',
      flipped: true,
      currentKeyIndex: 0,
      highlightManyougana: false,
      autoflip: false,
      randomizedNextLetter: false,
      showOptions: false
    }
  },
  props: {
    userObj: Object,
    isTutorial: Boolean
  },
  computed: {
    availableKeys () {
      if (this.isTutorial) {
        return skillLevelDatabaseKeysDisjoint[this.userObj.skillLvl]
      } else {
        return skillLevelDatabaseKeys[this.userObj.skillLvl]
      }
    },
    flashcardSide () {
      if (!this.flipped) {
        return 'front side'
      } else {
        return 'back side'
      }
    },
    nextKeyIndex () {
      if ((this.currentKeyIndex + 1) === this.availableKeys.length) {
        return 0
      } else {
        return this.currentKeyIndex + 1
      }
    },
    pageStyle () {
      if (this.showOptions && !this.isTutorial) {
        return 'width: 256px; height: 680px; padding: 30px;'
      } else if (this.showOptions && this.isTutorial) {
        return 'width: 256px; height: 570px; padding: 30px;'
      } else {
        return 'width: 256px; height: 440px; padding: 30px;'
      }
    }
  },
  mounted () {
    if (this.userObj.viewedTutorial[1] === false) {
      this.userObj.viewedTutorial[1] = true
      this.viewTutorial = true
      this.$root.$emit('updateDatabase')
    }
    this.flipCardOver()
  },
  methods: {
    updateFlashcard () {
      console.log('called updateFlashcard in FlipCard')
      if (this.script1 === 'manyougana-katakana' && this.highlightManyougana) {
        this.currentLetters1 = this.$refs.IndexOps.getLetters(this.letter, this.script1 + '-c')
      } else {
        this.currentLetters1 = this.$refs.IndexOps.getLetters(this.letter, this.script1)
      }
      if (this.script2 === 'manyougana-katakana' && this.highlightManyougana) {
        this.currentLetters2 = this.$refs.IndexOps.getLetters(this.letter, this.script2 + '-c')
      } else {
        this.currentLetters2 = this.$refs.IndexOps.getLetters(this.letter, this.script2)
      }
    },
    flipCardOver () {
      if (this.flipped) {
        this.currentImage = this.currentLetters1[0]
      } else {
        this.currentImage = this.currentLetters2[0]
      }
      this.flipped = !this.flipped
      this.timedFlip()
    },
    /**
    Flip card over after 5 seconds
    Active when autoflip is engaged
    **/
    timedFlip () {
      if (this.autoflip) {
        setTimeout(this.flipCardOver, 5000)
      }
    },
    /**
    Manually flip card.
    **/
    manualFlip () {
      clearTimeout()
      this.flipCardOver()
    },
    /**
    Get the desired next letter
    **/
    getNextLetter () {
      if (this.randomizedNextLetter) {
        this.getRandomNextLetter()
      } else {
        this.getSystematicNextLetter()
      }
    },
    /**
    Get a random next letter, restricted to user skill level
    **/
    getRandomNextLetter () {
      var oldLetter = this.letter
      var randomInt = 0
      var sameKey = true
      while (sameKey) {
        randomInt = Math.floor(Math.random() * this.availableKeys.length)
        sameKey = (this.availableKeys[randomInt] === oldLetter)
      }
      this.letter = this.availableKeys[randomInt]
      this.currentKeyIndex = randomInt
      this.updateFlashcard()
    },
    /**
    Get the next letter in skill level database order, restricted to user skill level
    **/
    getSystematicNextLetter () {
      this.letter = this.availableKeys[this.nextKeyIndex]
      this.currentKeyIndex = this.nextKeyIndex
      this.updateFlashcard()
    }
  }
}
/**
<q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" style="position: absolute; top: 34px; right: 20px;" />
<q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Simple Flashcard)</div>
        </q-card-section>
        <q-card-section>
        Use <strong>Simple Flashcard</strong> to view a Japanese letter in different scripts.
        <br/>
        <br/>
        You can type the <strong><abbr title="shi chi tsu fu, rather than si ti tu hu">Hepburn</abbr></strong> version of your desired letter in the <strong>Current Letter</strong> input field.
        <br/><br/>
        <strong>Script1</strong> is the front and <strong>Script2</strong> is the back side of the flashcard. These sides show whatever script you configure in the respective dropdowns.
        <br/><br/>
        Press the <strong>FLIP</strong> button or <strong>Enter</strong> on your keyboard to "flip" the flashcard. You can see the active script just above the character image. <br/>
        </q-card-section>
      </q-card>
    </q-dialog>
**/
</script>
