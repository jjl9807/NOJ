<template>
  <el-container style="min-width: 992px;">
    <el-header>
      <NavMenu />
    </el-header>
    <el-main>
    <router-view></router-view>  
    </el-main>
  </el-container>
</template>

<script>

import NavMenu from '@/components/views/Menu.vue'

export default {
  name: 'App',
  components:{
    NavMenu
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>@/components/views/Menu.vue
