<template>
  <div class="box">
    <div class="top">
      <div class="top-center">Account Login</div>
    </div>
    <div>
      <p class="error" v-if="error">Account or Password Wrong!</p>
    </div>
    <div class="content">
      <input type="tel" class="tel-input" autofocus="autofocus" placeholder="Enter Account" v-model="id">
      <input class="scode-input" placeholder="Enter Password" type="password" v-model="password">
    </div>
    <div class="footer">
      <el-button @click.native="log">Login</el-button>
    </div>
  </div>
</template>
<script>
export default {
  data: function() {
    return {
      id: '',
      password: '',
      error: false
    }
  },
  methods: {
    log: function () {
      let serverPath = 'http://127.0.0.1:8000/app/login/'
      let that = this
      this.$axios({
        method: 'post',
        url: serverPath,
        data: {
          id: this.id,
          password: this.password
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
        transformRequest: function (obj) {
          let str = []
          for (let p in obj) {
            str.push(encodeURIComponent(p) + '=' + encodeURIComponent(obj[p]))
          }
          return str.join('&')
        }
      }).then(function (response) {
        if (response.data['level'] === 1) {
          that.$router.push({name: 'content'})
        } else if (response.data['level'] === 2) {
          that.$router.push({name: 'host', query: {userID: response.data['id']}})
        } else if (response.data['level'] === 3) {
          //TODO: Direct to Government Page
          console.log('3')
        } else {
          that.error = true
          setTimeout(that.change, 1000)
        }
      }).catch(function (e) {
        console.log(e.response)
        that.error = true
      })
    },
    change: function () {
      this.error = false
    }
  }
};
</script>
<style lang="stylus" scoped>
.box {
  padding: 40px 32px 30px 32px;

  .top {
    overflow: hidden;

    .top-center {
      color: #424242;
      font-size: 20px;
      text-align: center;
      font-weight: bold;
    }

    .top-right {
      float: right;

      &:hover {
        cursor: pointer;
      }

      img:first-child {
        height: 32px;
        width: 80px;
        margin-right: 12px;
      }

      img:nth-of-type(2) {
        height: 32px;
        width: 32px;
      }
    }
  }

  .error {
    border: #ff525c 1px solid;
    border-radius: 6px;
    background: #ffe8e9;
    height: 40px;
    line-height: 40px;
    margin-top: 10px;

    >img {
      width: 20px;
      height: 20px;
      margin: 0 10px;
      display: inline-block;
      vertical-align: middle;
    }

    >span {
      font-size: 16px;
      color: #424242;
    }
  }

  .content {
    font-size: 15px;
    color: #424242;
    margin-top: 16px;

    input:focus {
      outline: none;
    }

    >input {
      line-height: 64px;
      height: 64px;
      border: 1px solid #c0bebe;
      display: block;
      width: 100%;
      margin-bottom: 24px;
      border-radius: 5px;
      text-indent: 20px;
    }

    .scode-lable {
      line-height: 64px;
      height: 64px;
      border: 1px solid #c0bebe;
      border-radius: 5px;
      text-indent: 20px;
      color: #797979;

      input {
        border: none;
        color: #424242;
        height: 90%;
      }

      .timer {
        color: #ffdc00;
        font-size: 18px;
        display: inline-block;

        &:hover {
          cursor: pointer;
        }
      }
    }
  }

  .footer {
    margin-top: 24px;

    button {
      border: none;
      border-radius: 6px;
      background: #ffdc00;
      padding: 20px 144px;
      outline: none;
      margin-left: 20px;

      &:hover {
        cursor: pointer;
      }
    }
  }
}
</style>
