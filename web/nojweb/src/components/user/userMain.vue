<template>
    <div style="margin: auto;max-width: 1000px;min-width: 800px;">
      <el-row>
        <el-col :span="7">
          <div style="margin: 0 20px;">
            <el-avatar shape="square" :size="250" :src="require('@/assets/R-C.png')" />
          </div>
          <div id="name">
            {{ info.name }}
          </div>
          <el-button v-if="this.$store.state.uid === parseInt(this.uid)" type="info" plain
            @click="this.$router.push('/user/edit/');" id="modify">修改资料</el-button>
          <div v-if="info.email" class="infos">
            <span class="subtitle">邮箱</span>
            <span style="float: right;">{{ info.email }}</span>
          </div>
          <div class="infos">
            <span class="subtitle">用户类型</span>
            <span style="float: right;">{{ group[info.gid] }}</span>
          </div>
          <div class="infos">
            <span class="subtitle">注册时间</span>
            <span style="float: right;">{{ info.reg_time }}</span>
          </div>
          <div v-if="info.login_time" class="infos">
            <span class="subtitle">登录时间</span>
            <span style="float: right;">{{ info.login_time }}</span>
          </div>
        </el-col>
        <el-col :span="17">
          <el-card id="main" shadow="never">
            <v-md-preview :text="info.motto" />
          </el-card>
        </el-col>
      </el-row>
    </div>
  </template>
  
  <script>
  
  export default {
    name: "userMain",
    data() {
      return {
        uid: 0,
        info: {},
        newMotto: '/',
        avatarAddress: '@/assets/R-C.png',
        group: ['', '普通用户', '管理员', '超级管理员'],
      }
    },
    methods: {
      all() {
       
      },
      getAvatarAddress() {
      
      },
    },
    async mounted() {
      this.uid = this.$route.params.uid;
      await this.all();
    }
  }
  </script>
  
  <style scoped>
  #name {
    font-size: 25px;
    font-weight: 600;
    margin: 10px 20px 15px;
  }
  
  #modify {
    width: 250px;
    height: 35px;
    margin: 0 20px 15px;
    font-size: 15px;
    font-weight: 600;
    color: #3f3f3f;
  }
  
  .infos {
    width: 250px;
    height: 30px;
    margin: 5px 20px;
    font-size: 15px;
    font-weight: 500;
    color: #656565;
  }
  
  .subtitle {
    float: left;
    color: #3f3f3f;
    font-weight: 600;
  }
  
  #main {
    min-height: 400px;
    overflow-y: scroll;
  }
  </style>