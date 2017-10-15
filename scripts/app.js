import Vue from 'vue';
import VueRouter from 'vue-router'
import App from './components/app.vue'
import Index from './components/index.vue'
import Article from './components/article.vue'
Vue.use(VueRouter)

var paths = location.href.split('/')
var path  = '/'+paths.slice(3, paths.length-1).join('/')

// アドレスは全部ルート(/)に向けて
// 画面切替は全部Vueに任せる
const router = new VueRouter({
		mode : 'history',
		base: path,
		routes: [
				{ path: '/', component: Index },
				{ path: '/:aid', component: Article }
		],
})

var vm = new Vue({
		router,
		el: '#app',
		render: h => h(App)
})
