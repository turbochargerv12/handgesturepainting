<template>
    <div>
      <v-app-bar elevate-on-scroll>
        <!-- class="v-app-bar--fixed" -->
        <v-avatar style="width: 6em" tile
          ><v-img src="../assets/serverError.png"></v-img
        ></v-avatar>
        <v-toolbar-title
          style="
            font-family: 'Times New Roman', Times, serif;
            font-size: 2em;
            padding-left: 40px;
          "
          >AirPainting.ai</v-toolbar-title
        >
        <v-spacer></v-spacer>
        <!-- <v-menu bottom left>
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon v-bind="attrs" v-on="on" @click="expand = !expand">
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
          <v-expand-transition>        
            <v-layout wrap justify-center style="background-color: white;" class="pa-4">
              <v-flex xs12 text-center><v-icon color="orange darken-3">mdi-account</v-icon></v-flex>
              <v-flex xs12 text-center>
                
              </v-flex>
              <v-flex xs12 text-center>{{ getRole }}</v-flex>
              <v-divider class="mx-4 my-2"></v-divider>
              <v-flex xs12 text-center><v-btn color="red darken-3" outlined>Logout</v-btn></v-flex>
            </v-layout>
          </v-expand-transition>
        </v-menu> -->
      </v-app-bar>
    </div>
</template>
  
<script>
  import store from "@/store";
  export default {
    data() {
      return {
        isLoading: false,
        expand: false,
        picker: {},
            p:null,
            swatches: [
                ['#FF0000', '#AA0000', '#550000'],
                ['#FFFF00', '#AAAA00', '#555500'],
                ['#00FF00', '#00AA00', '#005500'],
                ['#00FFFF', '#00AAAA', '#005555'],
                ['#0000FF', '#0000AA', '#000055'],
            ],
      };
    },
    computed: {
      getName() {
        return "hello";
      },
      getRole() {
        return "mello";
      },
    },
    methods: {
        changeColor(){
                store.commit("picker",this.picker)
                console.log(this.picker)
            }
    },
  };
  </script>
  <style scoped>
  .v-app-bar {
    position: fixed;

  }
  </style>