
<template>
  <div>
    <v-app>
      <v-main>
        <!-- <ServerError v-if="ServerError" /> -->
        <!-- <Master/> -->
        <v-layout wrap>
          <v-flex xs12><HeaderBar/></v-flex>
        </v-layout>        
        <v-divider></v-divider>
        <v-layout wrap>
          <v-flex xs12><router-view></router-view></v-flex>
        </v-layout>
        <v-layout wrap>
          <v-flex xs12><FooterBar/></v-flex>
        </v-layout> 
      </v-main>
    </v-app>
  </div>
</template>

<script>
  // import Master from "./pages/MasteR";
  import HeaderBar from "./components/HeaderBar";
  import FooterBar from "./components/FooterBar";
  
export default {
  name: 'App',
  components: {
    // Master
    HeaderBar,
    FooterBar
  }
}
</script>