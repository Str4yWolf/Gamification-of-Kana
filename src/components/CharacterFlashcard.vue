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
      <span v-if="isNormal">
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
      </span>
      <span v-if="isHighlightedManyougana">
        <span v-if="showTitle"
          style="
            width: 100px;
            top: 35px;
            position: relative;
            display: inline-block;
            ">
          <strong>{{imgLetter.split('\.')[0]}}</strong>
        </span>
        <span v-if="showScript"
          style="
            width: 100px;
            top: -99px;
            position: relative;
            display: inline-block;
          ">
          <strong>{{imgScript}}</strong>
        </span>
        <span v-if="isRomaji">
          <span v-if="showTitle"
            style="
              width: 100px;
              top: 35px;
              position: relative;
              display: inline-block;
              ">
            <strong>{{imgLetter.split('\.')[0]}}</strong>
          </span>
          <span v-if="showScript"
            style="
              width: 100px;
              top: -99px;
              position: relative;
              display: inline-block;
            ">
            <strong>{{imgScript}}</strong>
          </span>
        </span>
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
        if (this.imgSrc === '../statics/grey.png' || this.imgSrc === '') { // no letter input
          return ''
        } else if (this.isRomaji) { // PNG images contain romaji only at the moment
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
    isHighlightedManyougana () {
      if (this.imgSrc.split('/')[3] === undefined) {
        return ''
      } else {
        return this.imgSrc.split('/')[3].split('-')[2] === 'c'
      }
    },
    isRomaji () {
      console.log('imgSrc in CharacterFlashcard: ' + this.imgSrc)
      if (this.imgSrc !== '' && this.imgSrc !== '../statics/grey.png') {
        return this.imgSrc.split('/')[3].split('-')[0] === 'romaji'
      } else {
        return false
      }
    },
    isNormal () {
      return !this.isHighlightedManyougana && !this.isRomaji
    },
    imgSrcComp () {
      if (this.imgSrc === '') {
        return '../statics/grey.png'
      } else {
        return this.imgSrc
      }
    },
    imgSrcSVG () {
      return this.imgSrcComp + '#svgView(viewbox(0 0 100 100))"'
    }
  }
}
</script>

<style>
</style>
