<template>
    <div>
       <problemMenu />
    </div>

    <div class="problem-description">
      <h1 style="text-align: center;">{{ problem.title }}</h1>
      <h2>题目内容</h2>
      <p>{{ problem.content }}</p>
  
      <h2>输入格式</h2>
      <p>{{ problem.inputFormat }}</p>
  
      <h2>输出格式</h2>
      <p>{{ problem.outputFormat }}</p>
  
      <h2>样例一</h2>
      <h3>Input</h3>
      <pre class="code-box">{{ problem.example.input }}</pre>
      <h3>Output</h3>
      <pre class="code-box">{{ problem.example.output }}</pre>  
      <h2>限制与约定</h2>
      <p>时间限制：{{ problem.timeLimit }} ms</p>
      <p>空间限制：{{ problem.spaceLimit }} MB</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import problemMenu from '@/components/problem/problemMenu'
  export default {
    name:"problemDescription",
    components:{
        problemMenu
    },
    data() {
      return {
        problem: {
          title: "",
          content: "",
          inputFormat: "",
          outputFormat: "",
          example: {
            input: "",
            output: ""
          },
          timeLimit: "",
          spaceLimit: ""
        }
      };
    },
    mounted() {
      // Simulated API call to fetch problem data
      this.pid = this.$route.params.pid;
      this.fetchProblemData();
    },
    methods: {
      fetchProblemData() {
        // Simulated problem data
        axios.get('http://127.0.0.1:8000/problem/' + this.pid).then(res => {
        this.problem = {
          title : res.data.title,
          content: res.data.desc,
          inputFormat: res.data.in_desc,
          outputFormat: res.data.out_desc,
          example: {
            input: res.data.in_sample,
            output: res.data.out_sample
          },
          timeLimit: res.data.time_limit,
          spaceLimit: res.data.mem_limit
        };
      });
        
      }
    }
  };
  </script>
  
  <style>
  .problem-description {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .problem-description {
  text-align: left;
  max-width: 800px;
  margin: 0 auto;
}

.code-box {
  background-color: #E8F0FE;
}

  </style>
  