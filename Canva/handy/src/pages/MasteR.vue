<template>
    <div>
        <br>
        <v-layout wrap justify-space-around align-center>
            <v-flex xs8> 
                <!-- canvas single -->
                <div><Canvas :canvas-id="'canvas-one'" ref="childCanvas"/></div>
            </v-flex>
        </v-layout>
        <br><v-divider inset></v-divider><br>
        <v-layout wrap justify-space-around align-center >
                    <v-flex xs4 >
                        <v-color-picker 
                        v-model = "picker" 
                        onclick = "changeColor(event)"                  
                        
                        hide-canvas
                        hide-sliders
                        show-swatches  
                        :swatches="swatches"  
                        elevation="6"
                        ></v-color-picker> 
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
    import store from "@/store";

    export default {
        name: "MasteR",
        data: () => ({
            picker: {},
            p:null,
            swatches: [
                ['#FF0000', '#AA0000', '#550000'],
                ['#FFFF00', '#AAAA00', '#555500'],
                ['#00FF00', '#00AA00', '#005500'],
                ['#00FFFF', '#00AAAA', '#005555'],
                ['#0000FF', '#0000AA', '#000055'],
            ],
            color: '#FF0000',
        }),
        computed:{
            PColor() {
            return store.state.p;
        },
        },
        methods: {
            reset() {
                this.$refs.childCanvas.reset();
            },
            changeColor(){
                store.commit("picker",this.picker)
                console.log(this.picker)
            }
        },
        components: {
            Canvas
        }
    }
</script>

<style scoped>
</style>