const { defineConfig } = require('@vue/cli-service')
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const MonacoWebpackPlugin = require('monaco-editor-webpack-plugin')
module.exports = defineConfig({
  transpileDependencies: true,
  productionSourceMap: false,
  devServer: {
    proxy: {
      '/api': {
        "target": "localhost:3000",
        ws: true,
        changeOrigin: true
        //pathRewrite:{
       //     '^/api':''
       // }
      }
    }
  },
  chainWebpack(config) {
    if (process.env.NODE_ENV === 'production') {
      config.optimization.splitChunks({
        cacheGroups: {
          monacoEditor: {
            test: /[\\/]node_modules[\\/]monaco-editor[\\/]/,
            name: 'monaco-editor',
            chunks: 'all',
            priority: 20,
          },
          common: {
            name: 'ty',
            chunks: 'all',
          },
        }
      })
    }
  },
  configureWebpack: {
    plugins: [
      // new BundleAnalyzerPlugin(),
      new MonacoWebpackPlugin({ languages: ['cpp'] })
    ]
  }
});