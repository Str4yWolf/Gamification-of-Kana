<template>
  <q-page class="flex flex-center">
    <q-card class="signup">
      <p>
      <q-input v-model="username" @input="name = username" label="Your Name" />
      <br />
      <q-btn id="signup-enter" color="primary" label="Enter" @click="validateSignup"/> &nbsp;
      <q-btn color="white" text-color="black" label="Cancel" @click="getLetters('a', 'katakana')"/>
      </p>
    </q-card>
    <q-card>
      <div>
        <img src="../../../svg/katakana/katakana_letter_a.svg" height="1000px" width="1000px"/>
      </div>
    </q-card>
  </q-page>
</template>

<style>
.signup {
  padding: 10px;
}
</style>

<script>
import data from '../../../svg/kana-maps.json'
export default {
  name: 'PageIndex',
  data () {
    return {
      name: ''
    }
  },
  methods: {
    validateSignup () {
      console.log('Logging validated signup: \'' + this.name + '\'')
      if (this.name === '') {
        alert('Please enter a name')
      } else {
        alert('Name saved')
      }
    },
    getLetters (letter, script) {
      var paths = []
      var d = data.data
      for (var i in d) {
        console.log('i is ' + i)
        if (d[i].script === script) {
          console.log('d[i].script is ' + d[i].script)
          console.log('script is ' + script)

          console.log(paths)
          console.log('path')
          console.log('../../../svg/%s/%s_letter_%s.svg' % (script, script, letter)) // doesn't work?
          console.log('../../../svg/' + script + '/' + script + '_letter_' + letter + '.svg')
          console.log(letter, script, d[i].letters.letter)

          console.log('d[i].letters is ' + d[i].letters)
          console.log('d[i].letters.letter is ' + d[i].letters.letter) // why object and not dict?
          console.log('d[i].letters[letter] is ' + d[i].letters[letter])
          console.log('d[i].letters[0].letter is ' + d[i].letters[0].letter)
          console.log(d)
          return d[i].letters.letter
          /**
          for (var suffix in d[i].letters.letter) {
            // path = ('../../../svg/%s/%s_letter_%s%s.svg' %(script, script, letter, p))
            path = '../../../svg/' + script + '/' + script + '_letter_' + letter + suffix + '.svg'
            paths.push(path)
          }
          **/
        }
      }
    }
  }
}
</script>
