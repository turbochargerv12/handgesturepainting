<template>
    <div>
        <v-layout wrap justify-center mt-16 style="height: 50px;" >
            <v-flex text-center xs11>
                <WebCam
                    ref="webcam"
                    :deviceId="deviceId"
                    width="auto"
                    :isFrontCam="frontCam"     
                      
                    >
                </WebCam>
            </v-flex>
        </v-layout>
        <!-- https://www.npmjs.com/package/vue-2-cam -->
        <v-layout wrap justify-space-around align-center >
                            <v-flex xs8 text-center>
                                <v-color-picker 
                                v-model = "picker"       
                                hide-canvas
                                hide-sliders
                                show-swatches  
                                :swatches="swatches"  
                                elevation="6"
                                @click = " console.log(picker) " 
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
import { WebCam } from 'vue-cam-vision'
export default {
    data () {
    return {
      captures: [],
      imgReport: [],
      frontCam: false,
      webcam: null,
      img: null,
      camera: null,
      deviceId: null,
      devices: [],
    //   googleKey: config.googleVisionKey
    picker: {},
           
            swatches: [
                ['#FF0000', '#AA0000', '#550000'],
                ['#FFFF00', '#AAAA00', '#555500'],
                ['#00FF00', '#00AA00', '#005500'],
                ['#00FFFF', '#00AAAA', '#005555'],
                ['#0000FF', '#0000AA', '#000055'],
            ],
            color: '#FF0000',
    }
  },
  components: {
    WebCam
  }
}
</script>