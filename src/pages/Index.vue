<template>
  <q-page class="flex flex-center">
    <span v-if="showMenu">
      <img class="clickable-main-menu" style="position: absolute; top: 309px; left: 473px;"  @click="$root.$emit('unhideGeneralLearning')" src="../statics/QuestAreaMap.png" alt="Area Map" />
      <img class="clickable-main-menu" style="position: absolute; top: 397px; left: 473px;" @click="$root.$emit('unhideFinalExam')" src="../statics/Final area map.png" alt="Area Map" />
      <img class="clickable-main-menu" style="position: absolute; top: 264px; left: 473px;" @click="$root.$emit('unhideCharacterReference')" src="../statics/Reference area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 62px; left: 578px;" @click="$root.$emit('unhideFlipCard')" src="../statics/SmartFlashcard area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 109px; left: 452px;" @click="$root.$emit('unhideMultipleChoiceQuiz')" src="../statics/MultipleChoice area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 135px; left: 578px;" @click="$root.$emit('unhideWordReader')" src="../statics/WordReader area map.png" alt="Area Map" />
      <img class="clickable-individual-tools" style="position: absolute; top: 107px; left: 703px;" @click="$root.$emit('unhideWordCreator')" src="../statics/WordCreator area map.png" alt="Area Map" />
      <img class="background-logo" src="../statics/MainMenuTemple.png" alt="Main Menu Temple" />
    </span>
    <span v-if="!showMenu">
      <q-card class="flash" style="padding: 10px; color: white; background-color: orange; position: absolute; top: 10px; left: 515px; z-index: 3;">
        Click Sign In or Register to get started!
      </q-card>
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
      console.log('called setShowMenu(' + x + ') in Index')
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
.flash {
  animation: flasher 3s linear infinite;
}
@keyframes flasher {
  25% { opacity: 1; }
  50% { opacity: 0; }
  75% { opacity: 1; }
}
</style>
