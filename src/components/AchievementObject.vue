<template>
  <q-card :style="objectStyle">
    <span>
      <strong>no. {{index}}: </strong>
      <span style="position: absolute; left: 100px;">
        <strong>{{achievement[0]}}</strong>
      </span>
      <span style="position: absolute; left: 620px;">
        <strong>Reward: <q-icon name="whatshot" title="inkblots"/>{{achievement[1]}}</strong>
      </span>
    </span>
  </q-card>
</template>

<script>
export default {
  // name: 'PageName',
  data () {
    return {
    }
  },
  props: {
    index: Number,
    achievement: Array,
    userAchievements: Array
  },
  computed: {
    achieved () {
      return this.userAchievements.includes(this.index)
    },
    isEven () {
      return (this.index % 2) === 0
    },
    objectStyle () {
      var temp = 'width: 750px; padding: 30px;'
      temp += (this.achieved ? ' color: black;' : ' color: #cacaca;')
      return temp + (!this.isEven ? ' background-color: white;' : 'background-color: #efefef;')
    }
  }
}
</script>

<style>
</style>
