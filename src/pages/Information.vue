<template>
  <q-page class="flex flex-center">
    <q-card style="width: 750px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
      &nbsp;
      <strong style="font-size: 120%;">Information</strong>
      <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
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
              As of 8/2/2019, you can use a simple flashcard function and a multiple choice quiz.<br />
              There is also a WordCreator game to help you practice writing with Japanese scripts. <br />
              Spaced repitition works, although parameters need some trial-and-error tuning.
              User database interaction works. You can gain experience points and hit levels.<br />
              Progress tracking of character in question and target scripts included.<br />
              Inkblots serve as prospective in-game currency to help beat the prospective final game (exam) <br />
              Reference as to what characters are in Romaji is given as tooltips by hovering over images (only when answer to question has been revealed in relevant cases). <br />
              <br />
              <strong>Scripts (48 glyphs)</strong><br />
              [Hentaigana, Hiragana,] Katakana, Man'yougana-Katakana (also with katakana component highlighting)<br />
              <br />
              <strong>Text input</strong><br />
              Latin alphabet (Romaji) in Hepburn script
              <br />
              colour highlighting
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
            <strong>Want to to</strong>
            Achievements and its popup<br/>
            Design<br/>
            Separate modes<br/>
            Add full tutorial and information in about page<br/>
            Debugging<br/>
            <strong>Details / Debugging</strong><br />
            WordCreator remaining answer images bug.<br/>
            Multiple Choice script delay (as in Word Creator)?<br/>
            Multiple Choice same scripts in question and answer<br/>
            WordReader highlight manyougana not updating<br/>
            WordCreator highlight manyougana only updating in one case<br/>
            Redesign question text colour scheme (word bold blue; script bold black)<br/>
            Revise finalExamWords (no skipping questions or so)<br />
            outsource highlight manyougana??<br />
            skill level up popup (use popupedit or so) <br />
            make grey frame bigger on the background<br />
            make SVG greyscale?<br />
            (crop SVGs for faster loading)<br /><br />
            <strong>Requirements (9/10/2019)</strong><br />
            (2) teach mapping at once <br />
            (8) reduce mapping teaching to one script at a time (spread out)<br/>
            (8) increase visual affordances and shorten tutorials / outsource to title<br />
            (8) walk through design and redesign<br />
            (16) clean up code<br />
            (8) vue-fy/quasar-fy<br/>
            (6) user study questionnaire/planning<br/>
            (16) user study<br/>
            (2) bugs <br/>
            (80) <br />
            (50 / 100) BA text<br/>
            130/16 -> 8.125 h / day
            (4) achievements
            scalable SVGs<br />
            design<br />
            improve user flow<br />
            write description of app<br />
            separate different learning options<br />
            spaced repetition on characters of words<br />
            still fewer options<br />
            BA task<br /><br />
            <strong>Core tasks</strong><br />
              (0.5) about page
              (1) immersive/attractive feedback whatsoever<br />
              (3) animations<br />
              (0:15) manyougana button<br />
              (2) badges (bronze,silver,gold,platinum) without design<br />
              (3) add inkblot design to badges
              (0:40) Custom words in word creator<br />
              (1:30) colour design<br />
              (6) app design <br />
              (3) fancy tutorials - transfer to layout; add high z-index arrow overlays<br />
              (4) Practical tests / midterms <br />
              (3) getting rewards<br />
              (10) wrap learning page in a nice context<br />
              (5) Additional gamification elements (e.g., timer)<br />
              ((100+) Story mode)<br />
              (Varying Hentaigana)<br />
              (3) make DBs generic with script1 / script2 to improve adaptability<br/>
              (3) add latin script<br/>
              ((5) add commercial edge -> $0.05 / inklblot)
              (0:20) encourage use of learning page
              <br />
              (4) refactor code -- mixin<br />
              <br />
              <br />
              <strong>FINAL</strong><br/>
              MCQ measurement 1.6 / word -> 0.8 / word<br />
              WC kat measurement 5 / word -> 2.5<br />
              WC man measurement 5.5 / word -> 2.5<br />
              WR measurement 3 / word -> 1.5 / word<br />
              <br/>
              153.6s(96): MCQ(32) -> 25.6s; WR(32) -> 48s; WC(32) -> 80s<br />
              315.6s(+162s) MCQ: 53.6s(+28s); -> WR: 89s(+41s); WC: 173s(+93s)
              <br/>
              <strong>inkblots</strong><br/>
              <b>get permanently: lvl up (lvl),</b> badge (1-4), daily login (1), week (2), month (4); (lucky wheel; daily guess); single midterm with first 25 chars (5); sell exam ticket(1)<br/>
              <b>consume permanently: exam ticket(2)</b><br/>
              <b>get temporarily: no Japanese hints (10), no Manyougana highlight (5),</b><br/>
              <b>consume temporarily: additional second (1)</b><br/>
              <strong>Allocation: allocate points to tasks</strong><br/>
              <br/>
              <strong>exam ticket</strong><br/>
              get 1: pay 2 inkblots; lucky wheel; single midterm<br/>
              consume 1: to get to final with 1.35 exp boost<br/>
              <br/>
            <!-- <strong>Scripts (48 glyphs)</strong><br />
              (Man'yougana-Hiragana), (kanbun)<br />
              <br />
            <strong>Text input</strong><br />
              (Japanese/Chinese input) -->
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-list>
    <q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Information)</div>
        </q-card-section>
        <q-card-section>
        Click on the menus to browse through this <strong>Information</strong> page and to view general, pedagogic, and technical details.
        <br/><br/>
        <strong>ToDo</strong> describes future extensions of this project which will likely be developed privately.
        </q-card-section>
      </q-card>
    </q-dialog>
    </q-card>
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
  data () {
    return {
      viewTutorial: false
    }
  }
}
</script>

<style>
</style>
