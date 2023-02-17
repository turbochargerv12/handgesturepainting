<template>
    <div>
        <br>
        <v-layout wrap justify-space-around align-center>
            
            <v-flex xs8> <!-- canvas single -->
                <div><Canvas :canvas-id="'canvas-one'" ref="childCanvas"/></div>
            </v-flex>
        </v-layout>
        <br><v-divider 3px></v-divider><br>
        <v-layout wrap justify-space-around align-center>
                    <v-flex xs4 >
                        <v-color-picker 
                        v-model="picker" 
                        hide-inputs
                        hide-canvas
                        hide-sliders
                        swatches-max-height="200" 
                        show-swatches  
                        :swatches="swatches"  
                        elevation="6"> </v-color-picker>
                        <br>
                    </v-flex>
                    <v-flex text-center xs4>
                        <v-btn
                            class="ma-2"
                            outlined
                            fab
                            elevation="2"
                            color="indigo darken-4"
                            @click.prevent="reset"
                            >
                            <v-icon>mdi-eraser</v-icon>
                            </v-btn>
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