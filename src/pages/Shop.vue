<template>
  <q-page class="flex flex-center">
    <q-card style="width: 300px; height: 230px; padding: 30px;">
      <!-- header -->
      <q-btn round dense flat icon="keyboard_backspace" @click="$router.push('../')" />
      &nbsp;
      <strong style="font-size: 120%;">Shop</strong>
      <q-btn round dense flat icon="help" color="red" @click="viewTutorial=true" />
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
      <strong style="position: relative; top: 20px;">1 <q-icon title="Exam Tickets" name="note"/> = 2 <q-icon title="Inkblots" name="whatshot"/></strong>
      <strong style=" position: relative; top: 40px;">To pay: <span style="position: relative; left: 150px;">{{number * 2}} <q-icon title="Inkblots" name="whatshot"/></span></strong>
      </q-item-section>
    </q-card>
    <q-dialog v-model="viewTutorial">
      <q-card style="width: 600px;">
        <q-card-section>
          <div class="text-h6">Tutorial (Shop)</div>
        </q-card-section>
        <q-card-section>
        Buy <strong>Exam Tickets (<q-icon name="note"/>)</strong> to get access to the Final Exam.
        <br/>
        <br/>
        Choose your desired number of Exam Tickets by entering a positive number or clicking the arrows in the <strong>Input Field</strong>. Click <strong>GET</strong> to purchase.
        <br/>
        <br/>
        Purchased Exam Tickets are non-refundable.
        <br/>
        <br/>
        Current prices are displayed on screen.
        <br/>
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
  data () {
    return {
      number: 0,
      viewTutorial: false
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
