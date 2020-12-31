<template>
  <baidu-map :center="center" :zoom="zoom" @ready="handler" class="map">
    <bm-marker :position="center" :dragging="true" animation="BMAP_ANIMATION_BOUNCE">
    </bm-marker>
  </baidu-map>
</template>

<script>
export default {
  data () {
    return {
      center: {lng: 0, lat: 0},
      zoom: 3
    }
  },
  methods: {
    handler ({BMap, map}) {
      this.center.lng = this.$route.params.lon
      this.center.lat = this.$route.params.lat
      this.zoom = 17
    }
  },
}
</script>

<style scoped>
.map {
  width: 100%;
  height: 770px;
}
</style>
