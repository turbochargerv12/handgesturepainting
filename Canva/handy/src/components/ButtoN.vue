<template>
  <div>
  <v-layout wrap justify-center style="height: 92vh">
    <v-flex text-center pt-12 mt-4>
      <v-img src="../assets/hello.png" style="height: 90vh">
        <v-layout wrap justify-center fill-height style="height: 100vh;">
          <v-flex
            text-center
            align-self-center
            pt-12
            mt-12
          >
            <v-btn
              color="white darken-2"
              text
              @click="created"
              large
              fab
              icon
            >
              <v-icon large>mdi-palette</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-img>
    </v-flex>
  </v-layout>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
      return {
          data: {},
      }
  },
  methods:{
    created() {
        axios.get('/button')
            .then(response => {
              this.data = response.data
            })
            .catch(error => {
                console.log(error)
            })
    }
  }
}

</script>