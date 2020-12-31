// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import BaiduMap from 'vue-baidu-map'

Vue.prototype.$axios = axios
Vue.use(BaiduMap, {
  // ak 是在百度地图开发者平台申请的密钥 详见 http://lbsyun.baidu.com/apiconsole/key */
  ak: 'zMXzBkKIs9weKTo5kCz278MIG8UW9ACP'
})
Vue.use(ViewUI);
Vue.use(ElementUI);
Vue.config.productionTip = true;
Vue.prototype.axios = axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
