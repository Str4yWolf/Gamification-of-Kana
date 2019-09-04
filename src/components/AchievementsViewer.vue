<template>
  <q-page class="flex flex-center">
    <q-card style="width: 810px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$root.$emit('hideAchievementsViewer')" />
      &nbsp;
      <strong style="font-size: 120%;">Achievements</strong>
      <achievement-object v-for="a in achievementsMax" :key="'achievement-object_' + a" :index="a" :achievement="achievementsDatabase[a.toString()]" :userAchievements="userObj.achievements" />
    </q-card>
  </q-page>
</template>

<script>
import AchievementObject from '../components/AchievementObject.vue'

export default {
  // name: 'PageName',
  components: {
    AchievementObject
  },
  data () {
    return {
    }
  },
  props: {
    userObj: Object,
    achievementsDatabase: Object,
    achievementsMax: Number
  },
  computed: {
  }
}
</script>

<style>
</style>
