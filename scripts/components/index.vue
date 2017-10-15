<!-- 記事を並べてタイトル表示 -->
<template>
  <div class="container">
		<router-link :to="'/'+record.aid" v-for="record in results">
			<div class="box">
				{{record.title}}
			</div>
		</router-link>
  </div>
</template>

<style scoped>
.container{
		width: 100%;
		display: flex;
		flex-wrap: wrap
}
.box{
		width: 32vw;
		height: 300px;
		border: 1px black solid;
}
</style>

<script>
import axios from 'axios'
export default {
		data () {
				return {
						results:[],
				}
		},
		mounted(){
				// v-forするデータを明示的にしないと
				// ちょっと不具合とか出そう
				axios.get("/api/article")
						.then(response => {
								this.results = response.data
						})
		}
}
</script>
