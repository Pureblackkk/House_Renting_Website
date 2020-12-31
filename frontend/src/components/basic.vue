<template>
  <div>
    <div class="search">
    <search @search-event="update"></search>
    </div>
    <div class="infinite-list-wrapper" style="overflow:auto">
      <ul
        class="list"
        v-infinite-scroll="load"
        infinite-scroll-disabled="disabled">
        <li v-for="i in count" class="list-item">
          <house :info="[info[2*i-2], info[2*i-1]]" @click2map="tomap" v-show="info[2*i-1]"></house>
        </li>
      </ul>
      <p v-if="loading">Loading...</p>
      <p v-if="noMore">No More</p>
    </div>
  </div>

</template>

<script>
import House from './house'
import Search from './search'
export default {
  components: {House, Search},
  data () {
    return {
      count: 3,
      loading: false,
      id: [],
      info: []
    }
  },
  computed: {
    noMore () {
      return this.count >= (this.info.length / 2)
    },
    disabled () {
      return this.loading || this.noMore
    }
  },
  methods: {
    getData: function () {
      let serverPath = 'http://127.0.0.1:8000/app/user/'
      let that = this
      this.$axios({
        method: 'get',
        url: serverPath,
        data: {
          id: this.id,
          password: this.password
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
      }).then(function (response) {
        that.info = response.data
      }).catch(function (e) {
        console.log('Something Went Wrong!')
      })
    },
    load () {
      this.loading = true
      setTimeout(() => {
        this.count += 2
        this.loading = false
      }, 2000)
    },
    update: function (data) {
      console.log(data)
      this.info = data
    }
  },
  mounted () {
    this.getData()
  }
}
</script>

<style scoped>
.list-item{
}
.el-icon-star-off{
  position: fixed;
  left: 1350px;
  top: 700px;
  z-index: 99;
}
</style>
