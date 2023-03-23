<template>
    <div>
        <br>
        <v-layout wrap justify-space-around align-center>
            <v-flex xs12 sm7> 
                <!-- canvas single -->
                <Canvas :canvas-id="'canvas-one'" ref="childCanvas"/>
            </v-flex>
            <v-flex xs12 sm4>
                <v-layout wrap justify-start>
                    <v-flex xs12><WebCam/></v-flex>
                    <br><v-divider inset></v-divider><br>                    
                    <v-flex xs12>
                        <v-layout wrap justify-space-around align-center >
                            <v-flex xs10 text-center>
                                <OwlCarousel
                                :loop="false"
                                :nav="false"
                                :dots="true"
                                :responsive="owlResponsive"
                                >
                                    <template>
                                        <div v-for=" (col,ide) in swatches" :key="ide">
                                            <v-layout wrap >
                                                <v-flex xs4 text-center pa-2 >
                                                    <v-btn fab small :style = "{backgroundColor : col[0]}" @click="selectColor(col[0])"></v-btn>
                                                </v-flex>
                                            </v-layout>
                                        </div>
                                    </template>
                            </OwlCarousel>
                            </v-flex>
                            <v-flex text-center xs2>
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
                    </v-flex>
                </v-layout>
            </v-flex>            
        </v-layout> 
    </div>
</template>

<script>
    import Canvas from "../components/CanvaS";
    import WebCam from "@/components/WebCam";
    import store from "@/store";

    export default {
        name: "MasteR",
        data: () => ({
            swatches: [
                ['#FF0000'],
                ['#FFFF00'],
                ['#00FF00'],
                ['#00FFFF'],
                ['#0000FF'],
                ['#FFFFFF'],
                ['#000000']
            ],
            color: '#FFFFFF',
            owlResponsive: {
                0: { items: 2, nav: false },
                600: { items: 3, nav: false },
                960: { items: 5, nav: false },
                1264: { items: 7, nav: false },
                2560: { items: 10, nav: false },
            },
        }),
        computed:{
            cam() {
            // We will see what `params` is shortly
                return this.$route.path.cam
            },
        },
        methods: {
            reset() {
                this.$refs.childCanvas.reset();
            },
            selectColor(color) {
                this.color = color;
                store.commit("myColor",this.color);
                localStorage.setItem("color",this.color)
                console.log("ha",this.color);

            }
        
        },
        components: {
            Canvas,
            WebCam
        }
    }
</script>

<style scoped>
</style>