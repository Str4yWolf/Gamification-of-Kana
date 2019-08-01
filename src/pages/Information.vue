<template>
  <q-page class="flex flex-center">
    <q-card style="width: 750px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
      &nbsp;
      <strong style="font-size: 120%;">Information</strong>
      <!-- content -->
      <q-list bordered class="rounded-borders">
        <!-- General (Index 1) -->
        <q-expansion-item
          expand-separator
          icon="book"
          label="General"
          group="information"
      >
        <!-- How to use (Index 1-1) -->
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
        <!-- Progress and learning (Index 1-2) -->
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
      <!-- Details (Index 2) -->
      <q-expansion-item
          expand-separator
          icon="book"
          label="Details"
          group="information"
      >
        <!-- supported actions (Index 2-1) -->
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
              As of 7/31/2019, you can use a simple flashcard function and a multiple choice quiz.<br />
              Spaced repitition works, although parameters need some trial-and-error tuning.
              User database interaction works. You can gain experience points and hit levels.<br />
              Progress tracking of character in question and target scripts included.<br />
              <br />
              <strong>Scripts (48 glyphs)</strong><br />
              Hentaigana, Hiragana, Katakana, Man'yougana-Katakana (also with katakana component highlighting)<br />
              <br />
              <strong>Text input</strong><br />
              Latin alphabet (Romaji) only, in both linguistic and Hepburn script
            </q-card-section>
          </q-card>
        </q-expansion-item>
        <!-- Technical (Index 2-2) -->
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
              For each user account, a database entry will be created in your computer's local storage. The name serves as the key (identification); hence a name can be taken only once. This app counts the number of times you see a question on a letter and with a script map between two scripts. It will also count how successful you are in answering questions, assigning mastery gradings to each such map. Time stamps help with spaced repetition.
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-expansion-item>
      <!-- ToDo (Index 3) -->
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
              Reference as to what characters are in Romaji<br />
              Practical tests (e.g., reading hentaigana)<br />
              getting rewards<br />
              Additional gamification elements (e.g., timer)<br />
              Final (exam)<br />
              (Story mode)<br />
              (Varying Hentaigana)<br />
              <br />
            <strong>Scripts (48 glyphs)</strong><br />
              Man'yougana-Hiragana, (kanbun)<br />
              <br />
            <strong>Text input</strong><br />
              (Japanese/Chinese input)
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
  }
}
</script>

<style>
</style>
