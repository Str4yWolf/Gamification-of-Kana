<template>
  <q-card>
  <div class="character-flashcard">
      <img id="character-flashcard-image" v-bind:src="imgSrc" class="center" />
  </div>
  </q-card>
</template>

<script>
export default {
  // name: 'CharacterFlashcard',
  props: {
    imgSrc: String
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
