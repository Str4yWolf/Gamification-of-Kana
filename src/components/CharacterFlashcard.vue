<template>
  <q-card>
  <div class="character-flashcard">
      <img id="character-flashcard-image" v-bind:src="this.currentImage" class="center"/>
  </div>
  </q-card>
</template>

<script>
export default {
  // name: 'CharacterFlashcard',
  data () {
    return {
      currentImage: ''
    }
  },
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('updateView', this.updateView)
  },
  methods: {
    updateView: function (image) {
      document.getElementById('character-flashcard-image').src = image
    }
  }
}
</script>

<style>
div .character-flashcard {
  height: 150px;
  width: 150px;
}
.center {
  display: block;
  margin: auto;
  width: 50%;
  height: 50%;
  position: relative;
  top: 42px;
  left: 17px;
}
.character-flashcard-btn {
  position: relative;
  top: 80px;
}
</style>
