<template>
  <div>
    <el-row align="middle">
      <!-- Single Room -->
      <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0" :push="3">
        <el-card :body-style="{ padding: '0px' }">
          <!-- Img -->
          <div class="image">
            <a :href="info[index].basic_web"><img :src="info[index].basic_img" class="house-image" ></a>
            <div class="inner-image">
              <el-avatar :src="info[index].host_img" class="host-image" :size="50" @click.native="dialogClick(index)"></el-avatar>
              <!-- Turn to Map -->
              <el-button circle class="el-icon-s-promotion" @click.native="tomap(index)"></el-button>
            </div>
          </div>
          <!-- Host Info -->
          <el-dialog
            title="房东信息"
            :visible.sync="dialogVisible"
            width="40%"
            class="host-info"
            top="35vh"
          >
            <div>
              <span class="host-title">Name: </span>
              <span class="host-content">{{info[clickNow].host_name}}</span>
            </div>
            <div>
              <span class="host-title">Since: </span>
              <span class="host-content">{{info[clickNow].host_since}}</span>
            </div>
            <div>
              <span class="host-title">Loaction: </span>
              <span class="host-content">{{info[clickNow].host_local}}</span>
            </div>
            <div>
              <span class="host-title">Introduction:</span>
              <span class="host-content">{{info[clickNow].host_about}}</span>
            </div>
          </el-dialog>
          <!-- Info Below the Imgae -->
          <div style="padding: 20px;">
            <span class="house-name">{{info[index].basic_name}}</span>
            <!-- Basic Info  -->
            <el-collapse>
              <el-collapse-item title="Summary" :name="name1">
                <div class="house-sumary">{{info[index].basic_summary}}</div>
              </el-collapse-item>
              <el-collapse-item title="Space" :name="name2">
                <div class="house-space">{{info[index].basic_space}}</div>
              </el-collapse-item>
              <el-collapse-item title="Price" :name="name3">
                <div class="house-space">{{info[index].basic_price}}</div>
              </el-collapse-item>
            </el-collapse>
            <!-- Other Info -->
            <div class="bottom clearfix">
              <el-button type="text" class="button-left" @click="drawer1Click(index)">Room Info</el-button>
              <el-button type="text" class="button-right" @click="drawer2Click(index)">Review Info</el-button>
              <!-- Room Info-->
              <el-drawer
                title="我是标题"
                :visible.sync="drawer1"
                :direction="direction1"
                :with-header="false"
              >
                <div class="room-info">
                  <div class="room-item">
                    <span class="room-title">Property: </span>
                    <span class="room-content">{{info[clickNow].room_property}}</span>
                  </div>
                  <div class="room-item">
                    <span class="room-title">Room: </span>
                    <span class="room-content">{{info[clickNow].room_room}}</span>
                  </div>
                  <div class="room-item">
                    <span class="room-title">Accommodates: </span>
                    <span class="room-content">{{info[clickNow].room_accommodates}}</span>
                  </div>
                  <div class="room-item">
                    <span class="room-title">Bathrooms: </span>
                    <span class="room-content">{{info[clickNow].room_bathrooms}}</span>
                  </div>
                  <div class="room-item">
                    <span class="room-title">Bedrooms: </span>
                    <span class="room-content">{{info[clickNow].room_bedrooms}}</span>
                  </div>
                  <div class="room-item">
                    <span class="room-title">Beds: </span>
                    <span class="room-content">{{info[clickNow].room_beds}}</span>
                  </div>
                </div>
              </el-drawer>
              <!-- Review Info-->
              <el-drawer
                title="我是标题"
                :visible.sync="drawer2"
                :direction="direction2"
                :with-header="false"
              >
                <div class="review-info">
                  <div class="review-item">
                    <span class="review-title">Mark: </span>
                    <span class="review-content">{{info[clickNow].review_rating}}</span>
                  </div>
                  <div class="review-item">
                    <span class="review-title">Accuracy: </span>
                    <span class="review-content">{{info[clickNow].review_accuracy}}</span>
                  </div>
                  <div class="review-item">
                    <span class="review-title">Cleanliness: </span>
                    <span class="review-content">{{info[clickNow].review_clean}}</span>
                  </div>
                  <div class="review-item">
                    <span class="review-title">Checkin: </span>
                    <span class="review-content">{{info[clickNow].review_checkin}}</span>
                  </div>
                  <div class="review-item">
                    <span class="review-title">Communication: </span>
                    <span class="review-content">{{info[clickNow].review_communication}}</span>
                  </div>
                  <div class="review-item">
                    <span class="review-title">Locations: </span>
                    <span class="review-content">{{info[clickNow].review_locations}}</span>
                  </div>
                  <div class="review-item">
                    <span class="review-title">Value: </span>
                    <span class="review-content">{{info[clickNow].review_value}}</span>
                  </div>
                </div>
              </el-drawer>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'house',
  data () {
    return {
      drawer1: false,
      direction1: 'ltr',
      drawer2: false,
      direction2: 'rtl',
      name1: '1',
      name2: '2',
      name3: '3',
      dialogVisible: false,
      clickNow: 0
    }
  },
  props: {
    info: {
      type: Array,
      required: true
    }
  },
  methods: {
    tomap (index) {
      this.$router.push({ name: 'map', params: { lon: this.info[index].loc_lon, lat: this.info[index].loc_lat}})
    },
    dialogClick (index) {
      this.clickNow = index
      this.dialogVisible = true
    },
    drawer1Click (index) {
      this.clickNow = index
      this.drawer1 = true
    },
    drawer2Click (index) {
      this.clickNow = index
      this.drawer2 = true
    }
  }
}
</script>

<style scoped>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button-left {
  padding: 0;
  float: left;
}

.button-right {
  padding: 0;
  float: right;
}
.image{
  position: relative;
}
.inner-image{
  position: relative;
  z-index: 99;
}
.house-image {
  height: 100%;
  width: 100%;
  display: block;
}
.host-image{
  position: absolute;
  left: 15px;
  top: -60px;
}
.el-icon-s-promotion{
  position: relative;
  left: 40%;
  top: -50px;
  z-index: 98;
}
.host-info{
  font-weight: bold;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}
.host-title{
  position: relative;
  float: left;
  font-weight: bold;

}
.room-info{
  position: relative;
  top: 30%;
  font-weight: bold;
}
.room-item{
  line-height: 50px;
}
.review-item{
  line-height: 50px;
}
.review-info{
  position: relative;
  top: 30%;
  font-weight: bold;
}
</style>
