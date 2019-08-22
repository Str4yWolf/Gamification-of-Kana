<template>
  <q-page class="flex flex-center">
    <q-card style="width: 300px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
      &nbsp;
      <strong style="font-size: 120%;">Shop</strong>
      <!-- content -->
      <q-item-section>
      <!-- purchase exam tickets -->
      <span class="row">
        <span style="top: 20px; position: relative;"><strong>Exam Tickets: </strong></span>
        &nbsp; &nbsp; &nbsp;
        <q-input
          v-model.number="number"
          type="number"
          max-length="3"
          style="max-width: 50px;"
        />
        &nbsp; &nbsp; &nbsp;
        <q-btn color="green" label="Get" @click="getExamTickets" style="height: 20px; top: 10px; position: relative;" />
      </span>
        <br/>
        <br/>
        <p>Get 1 exam ticket for 2 inkblots. Purchase cannot be undone.</p>
      </q-item-section>
    </q-card>
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
  data () {
    return {
      number: 0
    }
  },
  methods: {
    getExamTickets () {
      this.$root.$emit('getExamTickets', this.number, true)
    }
  }
}
</script>

<style>
</style>
