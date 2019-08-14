<template>
  <q-card :style="background">
  <div class="character-flashcard">
    <img id="character-flashcard-image" v-bind:src="imgSrc" :title="imgLetter" class="center" />
    <span v-if="showTitle" style="width: 100px; top: 44px; display: inline-block; position: relative;"><strong>{{imgLetter.split('\.')[0]}}</strong></span>
    <span v-if="showScript" style="width: 100px; top: -86px; display: inline-block; position: relative;"><strong>{{imgScript}}</strong></span>
  </div>
  </q-card>
</template>

<script>
export default {
  // name: 'CharacterFlashcard',
  props: {
    imgSrc: String,
    showTitle: Boolean,
    background: String,
    showScript: Boolean
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
    },
    imgScript () {
      if (this.showScript) {
        return this.imgSrc.split('/')[3].split('-')[0]
      } else {
        return ''
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
  text-align: center;
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
