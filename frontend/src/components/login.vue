<template>
  <div id="app">
    <div id="logo"></div>
    <div class="items">
      <div class="itembox">
        <tel></tel>
      </div>
      <div class="bottom">&copy;朱姝慧、罗云中、胡婧璇、胡乐箫、陶鼎</div>
    </div>
  </div>
</template>

<script>
import tel from "./tel.vue";
export default {
  components: {
    tel
  },
  data() {
    return {
    };
  },
};
</script>

<style lang="stylus" scoped>
ul, li {
  list-style: none;
  margin: 0;
  padding: 0;
}

#app {
  height: 100%;
  width: 100%;
  min-height: 1000px;
  min-width: 800px;
  position: relative;
  background: url('../assets/imgs/back.jpg') left top / cover no-repeat;
}

#logo {
  color: #fff;
  position: relative;
  left: 70px;
  top: 0px;
  background: url('../assets/imgs/qutego_03.png') left center / 110% 110% no-repeat;
  width: 344px;
  height: 190px;
}

.items {
  position: absolute;
  left: 60%;
  top: 20%;

  .itembox {
    background: #ffffff;
    width: 420px;
    height: 420px;
    border-radius: 6px;
  }

  .bottom {
    text-align: center;
    color: slategray;
    font-size: 18px;
    margin-top: 30px;
    font-weight: 380

  }
}
</style>
