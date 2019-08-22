<template>
  <q-card :style="background">
  <div class="character-flashcard"
    style="
      height: 150px;
      width: 150px;
      position: relative;
      text-align: center;
      ">
    <img id="character-flashcard-image" v-bind:src="imgSrcSVG" :title="imgLetter" width="50%"
      style="
        top: 42px;
        position: relative;
        display: inline-block;
      " />
    <span v-if="showTitle"
      style="
        width: 100px;
        top: -35px;
        position: relative;
        display: inline-block;
        ">
      <strong>{{imgLetter.split('\.')[0]}}</strong>
    </span>
    <span v-if="showScript"
      style="
        width: 100px;
        top: -166px;
        position: relative;
        display: inline-block;
      ">
      <strong>{{imgScript}}</strong>
    </span>
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
    },
    imgSrcSVG () {
      return this.imgSrc + '#svgView(viewbox(0 0 100 100))"'
    }
  }
}
</script>

<style>
</style>
