<template>
  <div>
    <div class="selection">
      <!-- Price Select -->
      <div class="block">
        <p class="price-label">Price</p>
          <el-slider
            v-model="price"
            range
            show-stops
            vertical
            :max="2000"
            height="150px"
            class="price-select">
         </el-slider>
      </div>
      <!-- Mark Select -->
      <div class="block">
        <p class="mark-label">Mark</p>
        <el-slider
          v-model="mark"
          range
          show-stops
          vertical
          :max="100"
          height="150px"
          class="mark-select">
        </el-slider>
      </div>
      <!--  Room Type Select -->
      <div class="room-type">
        <el-select v-model="resRoomType" placeholder="Room" class="room-select">
          <el-option
            v-for="item in roomType"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            >
          </el-option>
        </el-select>
      </div>
      <!-- Proper Type Select -->
      <div class="proper-type">
        <el-select v-model="resPropType" placeholder="Property" class="proper-select">
          <el-option
            v-for="item in properType"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </div>
      <!-- Room Detailed Select -->
      <p class="accom-title">Accommodates</p>
      <el-input-number v-model="accom" @change="handleChange" :min="0" :max="15"
                       label="s" size="mini" class="accom-select">
      </el-input-number>
      <p class="bathroom-title">Bathrooms</p>
      <el-input-number v-model="bathroom" @change="handleChange" :min="0" :max="15" label="s" size="mini" class="bathroom-select"></el-input-number>
      <p class="bedroom-title">Bedrooms</p>
      <el-input-number v-model="bedroom" @change="handleChange" :min="0" :max="15" label="s" size="mini" class="bedroom-select"></el-input-number>
      <p class="bed-title">Beds</p>
      <el-input-number v-model="bed" @change="handleChange" :min="0" :max="15" label="s" size="mini" class="bed-select"></el-input-number>
      <!-- Search Icon -->
      <el-button type="primary" icon="el-icon-search" class="search-icon" @click.native="sendData">Search</el-button>
    </div>
    </div>
</template>

<script>
export default {
  name: 'search',
  data () {
    return {
      price: [0, 2000],
      mark: [0, 100],
      accom: null,
      bathroom: null,
      bedroom: null,
      bed: null,
      resRoomType: null,
      resPropType: null,
      roomType: [{
        value: 1,
        label: 'Entire home'
      }, {
        value: 2,
        label: 'Private room'
      }, {
        value: 3,
        label: 'Shared room'
      }, {
        value: 4,
        label: 'Hotel room'
      }],
      properType: [{
        value: 1,
        label: 'Apartment'
      }, {
        value: 2,
        label: 'Guest suite'
      }, {
        value: 3,
        label: 'Condominium'
      }, {
        value: 4,
        label: 'Hostel'
      }, {
        value: 5,
        label: 'Hotel'
      }, {
        value: 6,
        label: 'House'
      }]
    }
  },
  methods: {
    sendData: function () {
      let serverPath = 'http://127.0.0.1:8000/app/usrSearch/'
      let that = this
      // Make Data Object
      let sdata = {
        price: this.price,
        mark: this.mark,
        accom: this.accom,
        bathroom: this.bathroom,
        bedroom: this.bedroom,
        bed: this.bed,
        roomType: this.resRoomType,
        propType: this.resPropType
      }
      this.$axios({
        method: 'post',
        url: serverPath,
        data: sdata,
        headers: {'Content-Type': 'application/json; charset=UTF-8'}
      }).then(function (response) {
        console.log(response.data)
        that.$emit('search-event', response.data)
      }).catch(function (e) {
        console.log(e.response)
      })
    }
  }
}
</script>

<style scoped>
.selection{
  width: 120px;
  float: left;
}
.price-label{
  position: relative;
  left: 0%;
  top: 26%;
  font-family: "Microsoft YaHei";
  font-size:15px;
  padding: 10px;
}
.price-select{
  position: relative;
  left: 80%;
  width:50px;
}
.block{
  display: block;
  float: left;
  height: 360px;
  width: 60px;
}
.mark-label{
  position: relative;
  left: 140%;
  top: 26%;
  font-family: "Microsoft YaHei";
  font-size:15px;
  padding: 10px;
}
.mark-select{
  position: relative;
  left: 100%;
  width:100px;
}
.room-select{
  position: relative;
  top: -140px;
  left: 39%;
}
.proper-select{
  position: relative;
  top: -130px;
  left: 39%;
}
.accom-select{
  position: relative;
  top: -100px;
  left: 34%;
}
.bed-select{
  position: relative;
  top: -100px;
  left: 34%;
}
.bedroom-select{
  position: relative;
  top: -100px;
  left: 34%;
}
.bathroom-select{
  position: relative;
  top: -100px;
  left: 34%;
}
.accom-title{
  position: relative;
  top: -100px;
  left: 36%;
}
.bed-title{
  position: relative;
  top: -100px;
  left: 36%;
}
.bedroom-title{
  position: relative;
  top: -100px;
  left: 36%;
}
.bathroom-title{
  position: relative;
  top: -100px;
  left: 36%;
}
.search-icon{
  position: relative;
  left: 36%;
  top: -80px;
}
</style>
