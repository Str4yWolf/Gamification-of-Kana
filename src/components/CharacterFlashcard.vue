<template>
  <span class="character-flashcard-selector">
  <q-card :style="background">
  <div class="character-flashcard"
    style="
      height: 190px;
      width: 190px;
      position: relative;
      text-align: center;
      ">
    <span>
    <object id="character-flashcard-image" v-bind:data="imgSrc" :title="imgLetter" type="image/svg+xml"
      style="
        top: 47px;
        left: 43px;
        position: relative;
        display: inline-block;
      " />
    </span>
    <span v-if="showTitle"
      style="
        width: 100px;
        top: -2px;
        position: relative;
        display: inline-block;
        font-size: 125%;
        ">
      <strong>{{imgLetter.split('\.')[0]}}</strong>
    </span>
    <span v-if="showScript"
      style="
        width: 100px;
        top: -171px;
        position: relative;
        display: inline-block;
        font-size: 125%;
      ">
      <strong>{{imgScript}}</strong>
    </span>
  </div>
  </q-card>
  </span>
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
span.character-flashcard-selector {
  transform: rotate(20deg);
}
</style>
