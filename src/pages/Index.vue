<template>
  <q-page class="flex flex-center">
    <transition
      appear
      enter-active-class="animated bounceInRight"
      leave-active-class="animated fadeOut"
    >
    <!--
    <img class="clickable-main-menu" style="position: absolute; top: 0px; left: 0px;" @click="$root.$emit('unhideGeneralLearning')" src="../statics/Quest area map.png" alt="Area Map" width="40%" />
    <img class="clickable-main-menu" style="position: absolute; top: 0px; left: 0px;" @click="$root.$emit('unhideFinalExam')" src="../statics/Final area map.png" alt="Area Map" width="40%" />
    <img class="clickable-main-menu" style="position: absolute; top: 0px; left: 0px;" @click="$root.$emit('unhideCharacterReference')" src="../statics/Reference area map.png" alt="Area Map" width="40%" />
    <img class="clickable-main-menu" style="position: absolute; top: 0px; left: 0px;" @click="$root.$emit('unhideFlipCard')" src="../statics/SmartFlashcard area map.png" alt="Area Map" width="40%" />
    <img class="clickable-main-menu" style="position: absolute; top: 0px; left: 0px;" @click="$root.$emit('unhideMultipleChoiceQuiz')" src="../statics/MultipleChoice area map.png" alt="Area Map" width="40%" />
    <img class="clickable-main-menu" style="position: absolute; top: 0px; left: 0px;" @click="$root.$emit('unhideWordReader')" src="../statics/WordReader area map.png" alt="Area Map" width="40%" />
    <img class="clickable-main-menu" style="position: absolute; top: 0px; left: 0px;" @click="$root.$emit('unhideWordCreator')" src="../statics/WordCreator area map.png" alt="Area Map" width="40%" />
  -->
    <img class="background-logo" @click="showMessage()" src="../statics/MainMenuTemple.png" alt="Main Menu Temple" width="40%" />
    </transition>
  </q-page>
</template>

<style>
</style>

<script>
export default {
  name: 'PageIndex',
  components: {
  },
  data () {
    return {
    }
  },
  methods: {
    showMessage () {
      alert('Click on you avatar to view the menu')
    }
  }
}
</script>
<style>
img .background-logo :hover {
  background-color: #888888;
  opacity: 50%;
  z-index: 0;
}
.clickable-main-menu :hover {
  backgrond-color: powderblue;
  opacity: 20%;
  z-index: 1;
}
</style>
