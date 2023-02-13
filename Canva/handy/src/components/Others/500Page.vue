<template>
  <v-app>
    <v-main class="ServerError">
      <v-layout wrap justify-center fill-height pt-15>
        <v-flex lg3 md4 xs12 class="text-center" pt-15>
          <v-layout wrap justify-center>
            <v-flex xs12 lg12>
              <h1 class="error500 text-center">500!</h1>
            </v-flex>
            <v-flex lg11 md11 xs12>
              <h3 class="grey--text">Oops! Something went wrong</h3>
              <span class="grey--text">The Server is not responding</span>
              <v-img
                src="./../../assets/serverError.png"
                height="150px"
                contain
              ></v-img>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-main>
  </v-app>
</template>
<style scoped>
.ServerError {
  min-height: 100vh;
  min-width: 100vw;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1;
  background-color: white;
  overflow-x: hidden;
}
.error500 {
  padding: 0;
  font-weight: 80;
}
</style>