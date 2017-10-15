<!-- 個別記事表示 -->
<template>
  <div class="container">
			<div class="box">
				<h1>{{result.title}}</h1>
				<div>{{result.date}}</div>
				<div>{{result.content}}</div>
				<div><router-link to="/">戻る</router-link></div>
			</div>
  </div>
</template>

<style scoped>
.container{
		width: 100%;
}
.box{
}
</style>

<script>
import axios from 'axios'
export default {
		data () {
				return {
						result:{},
				}
		},
		mounted(){
				// $route.paramsでURLのIDを引っ張ってきて
				// 記事のjsonを持ってくる
				axios.get(`/api/article/${this.$route.params.aid}`)
						.then(response => {
								this.result = response.data
						})
		}
}
</script>
