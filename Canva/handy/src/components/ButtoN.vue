<template>
    <div>
    <v-layout wrap justify-center style="height: 92vh">
      <v-flex text-center pt-11 mt-4>
        <v-img src="../assets/hello.png" style="height: 90vh">
          <v-layout wrap justify-center fill-height style="height: 100vh;">
            <v-flex
              text-center
              align-self-center
              lg4
              sm5
              md4
              my-lg-5
              mx-lg-7
              pa-lg-4
            >
              <v-card
                outlined
                style="
                  background-color: lightgray;
                  border: 2px solid black;
                  padding-left: 40%;
                "
                rounded-pill
                class="pa-4 ma-2"
              >
                <v-layout wrap justify-center>
                  <v-flex xs3 text-center align-self-center>
                    <v-card-actions class="align-self-center">
                              <v-btn
                                color="black darken-2"
                                text
                                @click="created"
                                outlined
                              >
                              <v-icon>mdi-palette</v-icon>
                              </v-btn>
                              <v-snackbar v-model="snackbar">
                                {{ text }}
                                <template v-slot:action="{ attrs }">
                                  <v-btn
                                    color="red"
                                    text
                                    v-bind="attrs"
                                    @click="snackbar = false"
                                  >
                                    Close
                                  </v-btn>
                                </template>
                              </v-snackbar>
                            </v-card-actions>
                  </v-flex>
                </v-layout>
              </v-card>
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
            snackbar: false,
            text:'unsucessful'
        }
    },
    methods:{
      created() {
          axios.get('/button')
              .then(response => {
                this.snackbar = true
                this.text = 'Loading please wait'
                this.data = response.data
              })
              .catch(error => {
                  console.log(error)
                  this.snackbar = true
                this.text = error
              })
      }
    }
}

</script>