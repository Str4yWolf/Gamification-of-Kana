<template>
  <q-card :style="background">
  <div class="character-flashcard">
      <img id="character-flashcard-image" v-bind:src="imgSrc" :title="imgLetter" class="center" />
      <span v-if="showTitle" style="position: relative; top: 50px; left: 64px;"><strong>{{imgLetter.split('\.')[0]}}</strong></span>
  </div>
  </q-card>
</template>

<script>
export default {
  // name: 'CharacterFlashcard',
  props: {
    imgSrc: String,
    showTitle: Boolean,
    background: String
  },
  computed: {
    imgLetter () {
      if (this.showTitle) {
        if (this.imgSrc === '../statics/grey.png') { // no letter input
          return ''
        } else {
          return this.imgSrc.split('/').reverse()[0].split('_letter_')[1]
        }
      } else {
        return 'No cheating allowed'
      }
    }
  }
}
</script>

<style>
div .character-flashcard {
  height: 150px;
  width: 150px;
  position: relative;
}
.center {
  display: block;
  margin: auto;
  width: 50%;
  height: 50%;
  position: relative;
  top: 42px;
}
.character-flashcard-btn {
  position: relative;
  top: 80px;
}
</style>
