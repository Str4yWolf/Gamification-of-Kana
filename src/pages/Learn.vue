<template>
  <q-page class="flex flex-center">
    <q-card style="width: 810px; padding: 30px;">
      <span class="row">
        <!-- header -->
        <span>
          <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
          &nbsp;
          <strong style="font-size: 120%;">Learn</strong>
        </span>
        <!-- script selection -->
        <span style="padding: 0px 0px 0px 200px; top: -10px; position: relative;">
          <q-select v-model="script" :options="['katakana', 'manyougana-katakana']" label="Script" style="width:200px;" />
        </span>
        <!-- manyougana highlight toggle -->
        <span style="padding: 0px 30px 0px 30px;">
          <q-toggle
            v-model="highlight"
            color="red"
            label="Highlight Manyougana"
          />
        </span>
      </span>
      <!-- content -->
      <q-list bordered class="rounded-borders">
        <!-- All gojuon columns -->
        <q-expansion-item
          expand-separator
          icon="translate"
          label="a gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'a'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'i'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'u'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'e'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'o'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="ka gyо̄"
          group="gyou"
      > Bello
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="sa gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="ta gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="na gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="ha gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="ma gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="ya gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="ra gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="wa gyо̄"
          group="gyou"
      >
        </q-expansion-item>
        <q-expansion-item
          expand-separator
          icon="translate"
          label="n"
          group="gyou"
      >
        </q-expansion-item>
      </q-list>
    </q-card>
  </q-page>
</template>

<script>
import CharacterInfo from '../components/CharacterInfo.vue'

export default {
  // name: 'PageName',
  components: {
    CharacterInfo
  },
  data () {
    return {
      highlight: false,
      script: 'katakana'
    }
  }
}
</script>

<style>
</style>
