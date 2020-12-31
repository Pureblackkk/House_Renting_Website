<template>
 <div>
   <el-card class="box-card" shadow="always">
     <!-- Change Info Button-->
     <el-button type="primary" icon="el-icon-edit" size="small" circle class="edit" @click="inputForm=!inputForm"
                ></el-button>
     <!-- Img Part -->
     <el-avatar :size="60" :src="hostInfo.img"></el-avatar>
     <span class="superHost"><i  style="font-size:20px"
                                 :class="hostInfo.superhost==='t'? 'el-icon-star-on' : 'el-icon-star-off'"></i></span>
     <el-divider></el-divider>
     <!-- Info Part-->
     <!-- Basic Information-->
     <ul>
       <li>
         <span class="host-title">Name: </span>
         <span class="host-content">{{hostInfo.name}}</span>
       </li>
       <li>
         <span class="host-title">Since: </span>
         <span class="host-content">{{hostInfo.since}}</span>
       </li>
       <li>
         <span class="host-title">Loaction: </span>
         <span class="host-content">{{hostInfo.location}}</span>
       </li>
       <li>
         <span class="host-title">Introduction:</span>
         <span class="host-content">
           <el-button type="text" @click="dialogVisible = true">Check Introduction</el-button>
           <el-dialog
             title="Introduction"
             :visible.sync="dialogVisible"
             width="30%"
             >
             <span>
               <span class="host-intro">{{hostInfo.about}}</span>
             </span>
           </el-dialog>
         </span>
       </li>
     </ul>
     <el-divider></el-divider>
     <!-- Host's self Information-->
     <ul>
       <li v-show="hostInfo.repTime">
         <span class="host-self-title">Response Time: </span>
         <span class="host-self-content">{{hostInfo.repTime}}</span>
       </li>
       <li v-show="hostInfo.repRate">
         <span class="host-self-title">Response Rate: </span>
         <span class="host-self-content">{{hostInfo.repRate}}</span>
       </li>
       <li v-show="hostInfo.acpRate">
         <span class="host-self-title">Acceptance Rate: </span>
         <span class="host-self-content">{{hostInfo.acpRate}}</span>
       </li>
     </ul>
   </el-card>
   <!-- Input New Information -->
   <el-card class="input" shadow="always" v-show="inputForm">
     <!-- Upload Name and Introduction -->
     <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign" size="medium ">
       <el-form-item label="Name" class="input-name">
         <el-input v-model="update.name" :placeholder="hostInfo.name"></el-input>
       </el-form-item>
       <el-form-item label="Introduction" class="input-intro">
         <el-input type="textarea" :rows="10" v-model="update.introduction" :placeholder="hostInfo.about"></el-input>
       </el-form-item>
     </el-form>
     <!-- Save or Cancel -->
     <el-button type="primary" class="save" @click="sendUpdate">Update</el-button>
     <el-button class="cancel" @click="inputForm=!inputForm">Cancel</el-button>
   </el-card>
 </div>
</template>

<script>
import Update from './update'
import update from './update'
export default {
  components: {Update},
  name: 'owner',
  data () {
    return {
      dialogVisible: false,
      inputForm: false,
      hostInfo: null,
      labelPosition: 'left',
      update: {
        id: null,
        name: '',
        introduction: ''
      }
    }
  },
  methods: {
    checkEmpty: function (update) {
      if (update.name.length !== 0 && update.introduction.length !== 0) {
        return true
      } else {
        return false
      }
    },
    sendUpdate: function () {
      let serverPath = 'http://127.0.0.1:8000/app/hostUpdate/'
      let that = this
      this.update['id'] = this.hostInfo['id']
      if (!this.checkEmpty(this.update)) {
        that.$message({
          type: 'error',
          message: 'Please Enter Content!'
        })
        return null
      }
      this.$axios({
        method: 'post',
        url: serverPath,
        data: this.update,
        headers: {'Content-Type': 'application/json; charset=UTF-8'}
      }).then(function (response) {
        console.log(response)
        if (response.data === 'Ok') {
          that.$message({
            type: 'success',
            message: 'Success!'
          })
          that.inputForm = !that.inputForm
          location.reload(false)
        } else {
          that.$message({
            type: 'error',
            message: 'Something Wrong Happened!'
          })
        }
      }).catch(function (e) {
        console.log(e.response)
        that.$message({
          type: 'error',
          message: 'Something Wrong Happened!'
        })
        that.inputForm = !that.inputForm
      })
    },
    getData: function (userID) {
      let serverPath = 'http://127.0.0.1:8000/app/hostSearch/'
      let that = this
      this.$axios({
        method: 'get',
        url: serverPath,
        params: {'id': userID},
        headers: {'Content-Type': 'application/json; charset=UTF-8'}
      }).then(function (response) {
        console.log(response.data)
        that.hostInfo = response.data[0]
      }).catch(function (e) {
        console.log(e.response)
        that.$message({
          type: 'error',
          message: 'Something Wrong Happened!'
        })
      })
    }
  },
  mounted () {
    let userID = this.$route.query.userID
    this.getData(userID)
  }
}
</script>

<style scoped>
.edit{
  position: relative;
  left: 15px;
  top: 20px;
  float: left;
}
.box-card {
  position: relative;
  top: 110px;
  left: 30%;
  width: 600px;
  height: 500px;
}
.superHost {
  position: relative;
  left: 25%
}
.host-title {
  position: relative;
  left: 10%;
  font-weight: bold;
  font-size: 16px;
  line-height: 300%;
  width: 100px;

}
.host-content {
  position: relative;
  left: 20%;
  font-weight: bold;
  font-size: 16px;
  line-height: 300%;
  flex: 1;
}
.host-intro{
  position: relative;
}
.host-self-title{
  position: relative;
  left: 8%;
  font-size: 14px;
  line-height: 200%;
  width: 110px;
}
.host-self-content{
  position: relative;
  left: 20%;
  font-size: 14px;
  line-height: 200%;
  flex: 1;
}
li {
  list-style-type:none;
  display: flex;
}
.input{
  position: absolute;
  left: 26%;
  top: 14%;
  width: 700px;
  height: 550px;
}
.input-name{
  position: relative;
  top:60px
}
.input-intro{
  position: relative;
  top:100px;
  overflow-y: auto;
}
.save{
  position: relative;
  left: -50px;
  top:150px
}
.cancel{
  position: relative;
  left: 100px;
  top:150px
}
</style>
