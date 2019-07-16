<template>
  <q-page class="flex flex-center">
    <q-card style="width: 750px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="goUp()" />
      &nbsp;
      <strong style="font-size: 120%;">Information</strong>
      <!-- content -->
      <q-list bordered class="rounded-borders">
        <q-expansion-item
          expand-separator
          icon="book"
          label="General"
          group="information"
      >
        <q-expansion-item
          :header-inset-level="0.5"
          :content-inset-level="1"
          icon="receipt"
          label="How to use this app"
          group="general"
        >
          <q-card>
            <q-card-section>
              Learn how to read Japanese scripts with this app's different learning options.
               Move through the tabs to find the learning modes that suit you best.
               Try using the embedded game elements to gain experience points, hit new levels, and unlock achievements.
            </q-card-section>
          </q-card>
        </q-expansion-item>
        <q-expansion-item
          :header-inset-level="0.5"
          :content-inset-level="1"
          icon="receipt"
          label="Progress and learning"
          group="general"
        >
          <q-card>
            <q-card-section>
              This app aims to maximize your learning benefit by giving corrective feedback and
               motivate you to practice by honouring your success with rewards.
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-expansion-item>
      <q-expansion-item
          expand-separator
          icon="book"
          label="Details"
          group="information"
      >
        <q-expansion-item
          :header-inset-level="0.5"
          :content-inset-level="1"
          icon="receipt"
          label="Supported actions"
          group="details"
        >
          <q-card>
            <q-card-section>
              <strong>Functions</strong><br />
              As of 7/17/2018, you can use a simple flashcard function and a multiple choice quiz.<br />
              <br />
              <strong>Scripts (48 glyphs)</strong><br />
              Hentaigana, Katakana, Man'yougana-Katakana<br />
              <br />
              <strong>Text input</strong><br />
              Latin alphabet (Romaji) only, in linguistic script (not Hepburn)
            </q-card-section>
          </q-card>
        </q-expansion-item>
        <q-expansion-item
          :header-inset-level="0.5"
          :content-inset-level="1"
          icon="receipt"
          label="Technical"
          group="details"
        >
          <q-card>
            <q-card-section>
              <strong>User account</strong><br />
              For each user account, a database entry will be created in your computer's local storage. The name serves as the key (identification); hence a name can be taken only once.
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-expansion-item>
      <q-expansion-item
          :content-inset-level="1"
          expand-separator
          icon="book"
          label="ToDo"
          group="information"
      >
        <q-card>
          <q-card-section>
            <strong>Functions</strong><br />
              Progress tracking/User-DB entry<br />
              Varying Hentaigana<br />
              Learning theory/Spaced Repetition<br />
              Practical tests (e.g., reading hentaigana)<br />
              Gaining XP, levelling up, and getting rewards<br />
              (Story mode)<br />
              <br />
            <strong>Scripts (48 glyphs)</strong><br />
              Hiragana, Man'yougana-Hiragana, (kanbun)<br />
              <br />
            <strong>Text input</strong><br />
              Hepburn, (Japanese/Chinese input)
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-list>
    </q-card>
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
  data () {
    return {
    }
  },
  methods: {
    goUp () {
      console.log('called goUp() from Settings')
      this.$router.push('../')
    }
  }
}
</script>

<style>
</style>
