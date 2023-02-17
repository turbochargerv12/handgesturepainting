<template>
    <div>
        <br>
        <!-- canvas single -->
        <v-layout wrap  >
            <v-flex xs1></v-flex>
            <v-flex xs8>
                <div><Canvas :canvas-id="'canvas-one'" ref="childCanvas"/></div>
            </v-flex>
            <v-flex xs3>
                <v-layout wrap justify-space-around align-center>
                    <v-flex xs12 >
                        <v-color-picker v-model="picker" dot-size="25"
  swatches-max-height="200" show-swatches  :swatches="swatches" mode="rgba" style="box-shadow: 0 10px 8px -8px black; border: 2px solid black;"> </v-color-picker>
                        <br>
                    </v-flex>
                    <v-flex text-center xs12>
                <v-btn elevation="2" @click.prevent="reset">
                    CLEAR
                </v-btn>
            </v-flex>
                </v-layout> 
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
    import Canvas from "../components/CanvaS";
    export default {
        name: "MasteR",
        data: () => ({
            buttons: ['Simple', 'Separate', 'Replicated'],
            single: true,
            dialog : false,
            picker: null,
            swatches: [
                ['#FF0000', '#AA0000', '#550000'],
                ['#FFFF00', '#AAAA00', '#555500'],
                ['#00FF00', '#00AA00', '#005500'],
                ['#00FFFF', '#00AAAA', '#005555'],
                ['#0000FF', '#0000AA', '#000055'],
            ],
        }),
        methods: {
            reset() {
                this.$refs.childCanvas.reset();
            }
        },
        components: {
            Canvas
        }
    }
</script>

<style scoped>
</style>