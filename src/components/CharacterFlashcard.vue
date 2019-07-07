<template>
  <q-card>
  <div class="character-flashcard">
    <!-- <object class="character-flashcard-character" type="image/svg+xml" v-bind:data="this.path"></object> -->
      <img id="character-flashcard-image" v-bind:src="this.currentImage" class="center"/>
      <q-btn id="test" color="primary" label="Test" @click="status" class="character-flashcard-btn" />
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
  props: { 'path': String },
  created () {
    // listen to event calls from elsewhere
    this.$root.$on('updateView', this.updateView)
  },
  methods: {
    status: function () {
      alert('hi')
    },
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
  left: 5px;
}
.character-flashcard-btn {
  position: relative;
  top: 80px;
}
</style>
