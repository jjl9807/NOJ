<template>
    <div>
       <problemMenu />
    </div>

    <div class="problem-description">
      <h1>{{ problem.title }}</h1>
      <h2>题目内容</h2>
      <p>{{ problem.content }}</p>
  
      <h2>输入格式</h2>
      <p>{{ problem.inputFormat }}</p>
  
      <h2>输出格式</h2>
      <p>{{ problem.outputFormat }}</p>
  
      <h2>样例一</h2>
      <h3>Input</h3>
      <pre>{{ problem.example.input }}</pre>
      <h3>Output</h3>
      <pre>{{ problem.example.output }}</pre>
  
      <h2>限制与约定</h2>
      <p>时间限制：{{ problem.timeLimit }}</p>
      <p>空间限制：{{ problem.spaceLimit }}</p>
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
      this.fetchProblemData();
    },
    methods: {
      fetchProblemData() {
        // Simulated problem data
        
        axios.post('http://127.0.0.1:8000/1/problem', {
        pid: this.pid,
      }).then(res => {
        this.problem = {
          title : res.title,
          content: "This is a sample problem description.",
          inputFormat: "The input format is...",
          outputFormat: "The output format is...",
          example: {
            input: "Sample input...",
            output: "Sample output..."
          },
          timeLimit: "1s",
          spaceLimit: "64MB"
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

  </style>
  