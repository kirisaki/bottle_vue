// ただの枠。ナビゲーションとか共通部分入れてもよし
<template>
	<div class="container">
		<transition name="fade">
			<router-view></router-view>
		</transition>
	</div>
</template>

<style scoped>
.container{
		position: relative;
		top: 0;
		left: 0;
		width: 100%;
}
.fade-enter-active{
		opacity: 1;
		z-index: 0;
}
.fade-leave-active {
		opacity: 0;
		transition: opacity 0.7s;
		z-index: 10;
}

.fade-enter, .fade-leave-to {
		opacity: 0;
}
</style>

<script>
</script>
