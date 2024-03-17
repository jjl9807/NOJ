<template>
    <el-card class="oj-submissions-card" shadow="hover">
      <div class="oj-submissions">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-input v-model="filterText" placeholder="请输入用户名或题目ID进行筛选"></el-input>
          </el-col>
          <el-col :span="8" class="text-right">
            <el-button type="primary" @click="filter">筛选</el-button>
            <el-button type="info" @click="mySubmissions">我的提交</el-button>
          </el-col>
        </el-row>
        <el-table :data="submissions" style="width: 100%" stripe>
          <el-table-column prop="id" label="ID" width="70"></el-table-column>
          <el-table-column prop="problem" label="题目"></el-table-column>
          <el-table-column prop="username" label="提交者"></el-table-column>
          <el-table-column prop="result" label="结果"></el-table-column>
          <el-table-column prop="time" label="用时"></el-table-column>
          <el-table-column prop="memory" label="内存"></el-table-column>
          <el-table-column prop="language" label="语言"></el-table-column>
          <el-table-column prop="fileSize" label="文件大小"></el-table-column>
          <el-table-column prop="submitTime" label="提交时间"></el-table-column>
        </el-table>
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[10, 20, 50, 100]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </div>
    </el-card>
  </template>
  
  <script>
  export default {
    data() {
      return {
        submissions: [], // 存放提交记录的数组
        filterText: '', // 筛选文本框的值
        currentPage: 1, // 当前页码
        pageSize: 10, // 每页显示的记录数
        total: 100 // 总记录数，这里假设为100条
      };
    },
    methods: {
      // 模拟获取提交记录的方法
      fetchSubmissions() {
        // 模拟数据
        const submissions = [
          // 示例提交记录数据
          { id: 1, problem: '问题1', username: '用户A', result: '通过', time: '1s', memory: '100KB', language: 'C++', fileSize: '10KB', submitTime: '2024-03-17 10:00:00' },
          { id: 2, problem: '问题2', username: '用户B', result: '未通过', time: '-', memory: '-', language: 'Java', fileSize: '20KB', submitTime: '2024-03-17 10:05:00' },
          // 更多提交记录数据...
        ];
        this.submissions = submissions;
      },
      // 筛选提交记录
      filter() {
        // 根据筛选条件过滤提交记录，这里只是简单示例，实际需要根据需求实现
        // 示例：根据用户名或题目ID进行筛选
        // 筛选条件为 this.filterText
      },
      // 我的提交
      mySubmissions() {
        // 根据当前登录用户获取该用户的提交记录，这里只是简单示例，实际需要根据登录状态获取当前用户信息并查询
      },
      // 切换每页显示记录数
      handleSizeChange(size) {
        this.pageSize = size;
        this.fetchSubmissions(); // 根据每页显示的记录数重新获取提交记录
      },
      // 切换页码
      handleCurrentChange(page) {
        this.currentPage = page;
        this.fetchSubmissions(); // 根据页码重新获取提交记录
      }
    },
    mounted() {
      this.fetchSubmissions(); // 组件挂载时获取提交记录
    }
  };
  </script>
  
  <style scoped>
  .oj-submissions-card {
    width: 100%;
    max-width: 1400px; /* 自定义最大宽度 */
    margin: 20px auto; /* 居中并添加上下外边距 */
  }
  
  .text-right {
    text-align: right;
  }
  </style>
  