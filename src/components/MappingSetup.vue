<template>
  <q-page class="flex flex-center">
    <!-- entire registration card -->
    <q-card style="padding: 30px; width: 200px; height: 210px;">
      <!-- label -->
      <!-- <strong style="font-size: 100%;">Mapping Setup ({{step + 1}})</strong><br/>
      <span style="position: relative; padding: 30px;"/> -->
      <span v-if="!step">
        <strong><p>I want to learn </p></strong>
        <q-select v-model="script1" :options="['romaji', 'katakana', 'manyougana-katakana', 'hiragana', 'hentaigana']" label="Target Script" />
      </span>
      <span v-if="step">
        <strong><p>I already know </p></strong>
        <q-select v-model="script2" :options="['romaji', 'katakana', 'manyougana-katakana', 'hiragana', 'hentaigana']" label="Source Script" @input="checkAlreadyLearned()" />
      </span>
      <!-- buttons -->
      <q-btn v-if="!step" style="position: absolute; top: 150px; left: 100px;" color="green" label="Next" @click="step = true"/>
      <q-btn v-if="step" style="position: absolute; top: 150px; left: 26px;" color="green" label="Back" @click="step = false"/>
      <q-btn v-if="step" style="position: absolute; top: 150px; left: 96px;" color="purple" label="Setup" @click="validateMapping()"/>
    </q-card>
  </q-page>
</template>

<script>

export default {
  name: 'MappingSetup',
  data () {
    return {
      script1: 'katakana',
      script2: 'romaji',
      step: 0
    }
  },
  props: {
    userObj: String
  },
  methods: {
    checkAlreadyLearned () {
      var learnedMappings = this.userObj.learnedMappings
      for (var i = 0; i < learnedMappings.length; i++) {
        var currentMapping = learnedMappings[i].split('_')
        if ((this.script1 === currentMapping[0] && this.script2 === currentMapping[1]) || (this.script1 === currentMapping[1] && this.script2 === currentMapping[0])) {
          this.$q.notify('You have already learned this mapping. Please choose another one.')
          this.step = 0
          return true
        }
      }
      return false
    },
    validateMapping () {
      if (this.script1 === this.script2) {
        this.$q.notify('You cannot enter the same script twice. Please change your setup.')
        this.step = 0
        return
      }
      if (!this.checkAlreadyLearned()) {
        this.userObj.currentMapping = [this.script1, this.script2]
        this.$root.$emit('setNewMapping')
      }
    }
  }
}
</script>
