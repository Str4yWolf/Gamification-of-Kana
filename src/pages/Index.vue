<template>
  <q-page class="flex flex-center">
    <span v-if="showMenu">
      <img class="clickable-main-menu" style="position: absolute; top: 330px; left: 473px;"  @click="$root.$emit('unhideGeneralLearning')" src="../statics/QuestAreaMap.png" alt="Area Map" />
      <img class="clickable-main-menu" style="position: absolute; top: 418px; left: 473px;" @click="$root.$emit('unhideFinalExam')" src="../statics/Final area map.png" alt="Area Map" />
      <img class="clickable-main-menu" style="position: absolute; top: 285px; left: 473px;" @click="$root.$emit('unhideCharacterReference')" src="../statics/Reference area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 83px; left: 578px;" @click="$root.$emit('unhideFlipCard')" src="../statics/SmartFlashcard area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 130px; left: 452px;" @click="$root.$emit('unhideMultipleChoiceQuiz')" src="../statics/MultipleChoice area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 156px; left: 578px;" @click="$root.$emit('unhideWordReader')" src="../statics/WordReader area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 128px; left: 703px;" @click="$root.$emit('unhideWordCreator')" src="../statics/WordCreator area map.png" alt="Area Map" />
      <img class="background-logo" src="../statics/MainMenuTemple.png" alt="Main Menu Temple" />
    </span>
    <span v-if="!showMenu">
      <img class="background-logo" src="../statics/MainMenuSplash.png" alt="Main Menu Splash" />
    </span>
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
      showMenu: false
    }
  },
  mounted () {
    this.$root.$on('setShowMenu', this.setShowMenu)
  },
  methods: {
    setShowMenu (x) {
      this.showMenu = x
    }
  }
}
</script>
<style>
.background-logo {
  position: absolute;
  top: 0px;
  left: 384px;
  width: 40%;
  z-index: 1;
}
.clickable-main-menu {
  width: 25%;
  background-color: #000000;
  opacity: 0.0;
  z-index: 2;
}
.clickable-individual-tools {
  width: 9.8%;
  background-color: #000000;
  opacity: 0.0;
  z-index: 2;
}
.clickable-main-menu:hover {
  opacity: 0.1;
}
.clickable-individual-tools:hover {
  opacity: 0.1;
}
</style>
