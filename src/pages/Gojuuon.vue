<template>
  <q-page class="flex flex-center">
    <q-card style="width: 810px; padding: 30px 30px 180px 30px;">
      <span class="row">
        <!-- header -->
        <span>
          <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
          &nbsp;
          <strong style="font-size: 120%;">Reference</strong>
          <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
        </span>
        <!-- script selection -->
        <span style="padding: 0px 0px 0px 40px; top: -10px; position: relative;">
          <q-select v-model="script" :options="['katakana', 'manyougana-katakana']" label="Script" style="width:200px;" />
        </span>
        <!-- manyougana highlight toggle -->
        <span style="padding: 0px 0px 0px 10px;">
          <q-toggle
            v-model="highlight"
            color="red"
            label="Highlight Manyougana"
          />
        </span>
        <!-- show rows toggle -->
        <span style="padding: 0px 0px 0px 30px;">
          <q-toggle
            v-model="showRows"
            color="red"
            label="By Level"
          />
        </span>
      </span>
      <!-- content sorted by level -->
      <q-list v-if="showRows" bordered class="rounded-borders">
        <!-- All gojuon columns -->
        <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 1 (a gyо̄)"
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
          label="Skill Level 2 (ka gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ka'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ki'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ku'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ke'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ko'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 3 (sa gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'sa'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'shi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'su'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'se'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'so'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 4 (ta gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ta'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'chi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'tsu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'te'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'to'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 5 (na gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'na'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ni'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'nu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ne'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'no'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 6 (ha gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ha'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'hi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'fu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'he'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ho'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 7 (ma gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ma'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'me'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mo'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 8 (ra gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ra'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ri'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ru'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'re'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ro'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 9 (ya & wa gyо̄)"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ya'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'yu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'yo'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'wa'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'wo'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="Skill Level 10 (n & wa gyо̄ (pre-modern))"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'n'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'we'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'wi'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      </q-list>
    <!-- content without rows -->
      <span v-if="!showRows">
        <!-- All gojuon columns -->
        <span class="row">
          <character-info :letter="'a'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'i'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'u'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'e'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'o'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'ka'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ki'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ku'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ke'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ko'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'sa'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'shi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'su'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'se'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'so'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'ta'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'chi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'tsu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'te'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'to'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'na'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ni'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'nu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ne'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'no'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'ha'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'hi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'fu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'he'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ho'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'ma'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'me'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mo'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'ya'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="''" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'yu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="''" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'yo'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'ra'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ri'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ru'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'re'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ro'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'wa'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'wi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="''" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'we'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'wo'" :highlight="highlight" :sourceScript="script" />
        </span>
        <span class="row">
          <character-info :letter="'n'" :highlight="highlight" :sourceScript="script" />
        </span>
      </span>
      <!-- content with rows (outdated) -->
      <!-- <q-list v-if="showRows" bordered class="rounded-borders"> -->
        <!-- All gojuon columns -->
        <!-- <q-expansion-item
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
      >
        <span class="row">
          <character-info :letter="'ka'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ki'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ku'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ke'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ko'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="sa gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'sa'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'shi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'su'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'se'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'so'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="ta gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ta'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'chi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'tsu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'te'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'to'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="na gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'na'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ni'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'nu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ne'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'no'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="ha gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ha'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'hi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'fu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'he'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ho'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="ma gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ma'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'me'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'mo'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="ya gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ya'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="''" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'yu'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="''" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'yo'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="ra gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'ra'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ri'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ru'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'re'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'ro'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="wa gyо̄"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'wa'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'wi'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="''" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'we'" :highlight="highlight" :sourceScript="script" />
          <character-info :letter="'wo'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="translate"
          label="n"
          group="gyou"
      >
        <span class="row">
          <character-info :letter="'n'" :highlight="highlight" :sourceScript="script" />
        </span>
      </q-expansion-item>
      </q-list> -->
    <q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Character Reference)</div>
        </q-card-section>
        <q-card-section>
        Use <strong>Character Reference</strong> to view all Japanese letters in different scripts. You will see the <strong><abbr title="One Latin Romanization of Japanese">Romaji</abbr></strong> of the word in <strong><abbr title="shi chi tsu fu, rather than si ti tu hu">Hepburn</abbr></strong> below each character.
        <br/>
        <br/>
        You can choose a <strong>Script</strong> all letters should be displayed in. Hover over the letters to see their katakana and manyougana characters alongside.
        <br/>
        <br/>
        Toggle <strong>Highlight Manyougana</strong> to highlight the parts of manyougana katakana were derived from.
        <br/>
        <br/>
        The default display of letters is in the so-called <strong><abbr title="Japanese ordering for letters">Gojuuon</abbr></strong> table.
        <br/><br/>
        Toggle <strong>By Level</strong> to display the letters according to <strong>Skill Levels</strong> as used in this app. You can now expand <strong><abbr title="literally: colums; implemented as rows here">Gyou</abbr></strong> which correspond to the Gojuuon table's visual rows in most cases.
        <br/>
        </q-card-section>
      </q-card>
    </q-dialog>
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
      script: 'katakana',
      showRows: false,
      viewTutorial: false
    }
  },
  computed: {
  }
}
</script>

<style>
</style>
