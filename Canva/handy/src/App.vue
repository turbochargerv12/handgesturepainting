
<template>
  <div>
    <v-app>
      <v-main>
        <ServerError v-if="ServerError" />
        <!-- <Master/> -->
        <router-view></router-view>
      </v-main>
    </v-app>
  </div>
</template>

<script>
  // import Master from "./pages/MasteR";
export default {
  name: 'App',
  components: {
    // Master
  }
}
</script>