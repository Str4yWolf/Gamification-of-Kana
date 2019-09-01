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
          <q-card>
            <q-card-section>
              <strong>Goal</strong><br/>
              Use this app to learn Japanese scripts and become more fluent in using them.
              <br/><br/>
              <strong>How to use this app</strong><br/>
              Start out with <strong>Menu -> Quest </strong> to walk through the incremental learning experience.
               Play around with all menu items and all usable elements to learn, gain experience, and unlock new learning material. <br/>
               Take the Final Exam to prove your knowledge.
              <br/><br/>
              <strong>Progress and learning</strong><br/>
              This app aims to maximize your learning benefit by giving corrective feedback and
               motivate you to practice by honouring your success with rewards.
            </q-card-section>
          </q-card>
        </q-expansion-item>
        <!-- supported actions (Index 2) -->
        <q-expansion-item
          icon="book"
          label="Supported actions"
          group="information"
          >
          <q-card>
            <q-card-section>
              <strong>Functionality: </strong>Smart Flashcard, Multiple Choice Quiz, Word Reader, Word Creator, Quest (guide), Final Exam (proof of knowledge), Character Reference, Settings
              <br /><br/>
              <strong>Elements: </strong>Level, Experience Points, Skill Level, Skill Level Points, Inkblots (in-game currency), Timer, Score
              <br /><br/>
              <strong>Scripts: </strong>Romaji, Katakana, Manyougana-Katakana, Hiragana, Hentaigana
              <br /><br/>
              <strong>Database: </strong>User object, progress tracking; Japanese letters, Japanese words
              <br /><br/>
              <strong>Design (Pragmatics): </strong>Spaced Repetition System, Gamification, Motivation; Manyougana highlight showcasing Katakana component, Info (Dialog, Tooltip); Flow (keyboard shortcuts, limited options)
              <br /><br/>
            </q-card-section>
          </q-card>
        </q-expansion-item>
        <!-- ToDo (Index 3) -->
        <q-expansion-item
            expand-separator
            icon="book"
            label="ToDo"
            group="information"
        >
          <q-card>
            <q-card-section>
              <strong>Want to to</strong><br/>
              Achievements and its popup<br/>
              Design<br/>
              Debugging<br/>
              <strong>Details / Debugging</strong><br />
              Revise finalExamWords (no skipping questions or so)<br />
              make grey frame bigger on the background<br />
              make SVG greyscale?<br />
              (crop SVGs for faster loading)<br /><br />
              <strong>Requirements (9/10/2019)</strong><br />
              (4) walk through design and redesign<br />
              (15) clean up code<br />
              (8) vue-fy/quasar-fy<br/>
              (27)
              (6) user study questionnaire/planning<br/>
              (16) user study<br/>
              (49) <br />
              (50 / 100) BA text<br/>
              130/16 -> 8.125 h / day
              (4) achievements
              scalable SVGs<br />
              spaced repetition on characters of words<br />
              BA task<br /><br />
              <strong>Core tasks</strong><br />
                (1) immersive/attractive feedback whatsoever<br />
                (3) animations<br />
                (2) badges (bronze,silver,gold,platinum) without design<br />
                (3) add inkblot design to badges
                (0:40) Custom words in word creator<br />
                (1:30) colour design<br />
                (6) app design <br />
                (6) wrap learning page in a nice context<br />
                ((100+) Story mode)<br />
                (Varying Hentaigana)<br />
                ((5) add commercial edge -> $0.05 / inklblot)<br/>
                (0:20) encourage use of learning page<br/>
                conflate script databases with only one image per letter<br/>
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
                153.6s(96): MCQ(48) -> 38.4?s; WR(24) -> 36s; WC(24) -> 60s<br />
                315.6s(+162s) MCQ: 53.6s(+28s); -> WR: 89s(+41s); WC: 173s(+93s)
                <br/>
                <strong>inkblots</strong><br/>
                <b>get permanently: lvl up (lvl),</b> badge (1-4), daily login (1), week (2), month (4); (lucky wheel; daily guess);<br/>
                <b>consume permanently: inkblots(2)</b><br/>
                <b>get temporarily: no Japanese hints (10), no Manyougana highlight (5),</b><br/>
                <b>consume temporarily: additional second (1)</b><br/>
                <strong>Allocation: allocate points to tasks</strong><br/>
                <br/>
              <!-- <strong>Scripts (48 glyphs)</strong><br />
                (Man'yougana-Hiragana), (kanbun)<br />
                <br />
              <strong>Text input</strong><br />
                (Japanese/Chinese input) -->
              </q-card-section>
            </q-card>
          </q-expansion-item>
          <!-- About devs (Index 4) -->
          <q-expansion-item
              expand-separator
              icon="book"
              label="About us"
              group="information"
          >
            <q-card>
              <q-card-section>
                <strong>Project: </strong>Gamification of Japanese Scripts (Former Working Title: "Gamification of the Historical Development of Kana")
                <br /><br/>
                <strong>Context: </strong>Bachelor Thesis Computer Science (University of Hamburg)
                <br /><br/>
                <strong>Developer: </strong>Michael W K Huang; contributions by Vinodh Rajan Sampath
                <br /><br/>
                <strong>Contact Email: </strong>michaelhuang@hotmail.de (add custom email soon)
                <br /><br/>
              </q-card-section>
            </q-card>
          </q-expansion-item>
          <!-- Terms of use (Index 5) -->
          <q-expansion-item
              expand-separator
              icon="book"
              label="Terms of Use"
              group="information"
          >
            <q-card>
              <q-card-section>
                <strong>$1</strong> This app, in this phase, is intended for experimental purposes only. Any other use requires express knowledge and approval of the Developer. <br/>
                <strong>$2</strong> Although the Developer tries to maximze the learning experience and minimize errors, complete functionality and correctness of learning resources is not guaranteed. <br/>
                <strong>$3</strong> Data collected and stored by this app will use the Local Storage of your browser. Collected data will not be transmitted elsewhere. <br/>
                <strong>$4</strong> The Developer cannot be held responsible for any damages or losses incurred by the use of this app.
                <strong>$5</strong> By using this app, the user automatically agrees to these Terms of Use. <br/>
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
      viewTutorial: false
    }
  }
}
/**
<q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
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
**/
</script>

<style>
</style>
