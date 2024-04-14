<template>
    <div style="text-align: center; margin: 0 auto; max-width: 1200px">
      <el-card class="box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            题目列表
            <el-pagination @current-change="handleCurrentChange" :current-page="currentPage" :page-size="page_size"
              layout="total, prev, pager, next" :total="total"></el-pagination>
            <el-button-group>
              <el-button type="primary" @click="all">
                <el-icon class="el-icon--left">
                  <Refresh />
                </el-icon>
                刷新
              </el-button>
            </el-button-group>
          </div>
        </template>
        <el-table :data="problemList" height="600px" :header-cell-style="{ textAlign: 'center' }"
          :cell-style="{ textAlign: 'center' }" v-loading="!finished">
          <el-table-column prop="pid" label="#" width="100px" />
          <el-table-column prop="title" label="标题" width="auto">
            <template #default="scope">
              <span class="rlink" @click="this.$router.push('/problem/' + scope.row.pid)">
                {{ scope.row.title }}
              </span>
              <el-icon id="hidden" v-if="!scope.row.isPublic">
                <Hide />
              </el-icon>
            </template>
          </el-table-column>
          <el-table-column prop="status" label="AC/提交" width="150px">
            <template #default="scope">
              <span> {{ scope.row.acCnt }} / {{ scope.row.submitCnt }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="time" label="发布时间" width="200px" />
          <el-table-column prop="publisher" label="出题人" width="120px">
            <template #default="scope">
              <span class="rlink" @click="this.$router.push('/user/' + scope.row.publisherUid)">
                {{ scope.row.publisher }}
              </span>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </div>
  </template>
  
  <script>
import axios from 'axios';


  
  export default {
    name: 'problemList',
    data() {
      return {
        problemList: [],
        total: 0,
        gid: 1,
        page_size: 10,
        currentPage: 1,
        finished: false
      }
    },
    methods: {
        all() {
          this.problemList = [];
      // 请求数据
      axios.get('http://127.0.0.1:8000/problem/', {
        params: {
          limit: this.page_size,
          offset: (this.currentPage - 1) * this.page_size,
        }
      }).then(res => {
        // this.problemList = res.data.data;
        this.total = res.data.count;
        for (let i = 0; i < res.data.results.length; i++) {
          // 时间格式化
          const date = new Date(res.data.results[i]['time']);
          const year = date.getFullYear();
          const month = (date.getMonth() + 1).toString().padStart(2, '0');
          const day = date.getDate().toString().padStart(2, '0');
          const hours = date.getHours().toString().padStart(2, '0');
          const minutes = date.getMinutes().toString().padStart(2, '0');
          const seconds = date.getSeconds().toString().padStart(2, '0');
          // 数据对接
          const problem_entry = res.data.results[i];
          const rec = {
            pid: problem_entry['pid'],
            title: problem_entry['title'],
            acCnt: 10,
            submitCnt: 20,
            time: `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`,
            publisher: problem_entry['author'],
            publisherUid: -1
          };
          this.problemList.push(rec);
        }
        this.finished = true;
      }).catch(err => {
        console.error(err);
      });
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.all();
    }
  },
  mounted() {
      this.gid = this.$store.state.gid;
      this.all();
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .box-card {
    height: 700px;
    margin: 10px;
  }
  
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 20px;
  }
  </style>