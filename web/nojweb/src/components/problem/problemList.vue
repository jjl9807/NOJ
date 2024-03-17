<template>
    <div style="text-align: center; margin: 0 auto; max-width: 1200px">
      <el-card class="box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            题目列表
            <el-pagination @current-change="handleCurrentChange" :current-page="currentPage" :page-size="20"
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

  
  export default {
    name: 'problemList',
    data() {
      return {
        problemList: [],
        total: 0,
        gid: 1,
        currentPage: 1,
        finished: false
      }
    },
    methods: {
        all() {
      // 模拟数据请求延迟效果
      this.finished = false;
      setTimeout(() => {
        // 模拟从后端获取的数据
        const mockData = [
          { pid: 1, title: '题目1', acCnt: 10, submitCnt: 20, time: '2024-03-17', publisher: '出题人1', publisherUid: 1 },
          { pid: 2, title: '题目2', acCnt: 5, submitCnt: 15, time: '2024-03-16', publisher: '出题人2', publisherUid: 2 },
          // 其他题目数据...
        ];
        this.problemList = mockData;
        this.total = mockData.length;
        this.finished = true;
      }, 1000); // 模拟延迟1秒
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.all();
    }
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