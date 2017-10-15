<template>
  <div class="container">
		<router-link :to="'/'+record.id" v-for="record in results">
			<div class="box">
				{{record.title}}
			</div>
		</router-link>
  </div>
</template>

<style scoped>
.container{
		display: flex;
		flex-wrap: wrap
}
.box{
		width: 300px;
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
				console.log('aaaa')
				axios.get("/article")
						.then(response => {
								this.results = response.data
								console.log(this.results)
						})
		}
}
</script>
