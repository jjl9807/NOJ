<template>
    <div>
        <myAnnouncement />
    </div>
    <div>
        <problemList />
    </div>
</template>

<script>

import myAnnouncement from '@/components/views/announcement'
import problemList from '@/components/problem/problemList'
    export default{
        name:"myHome",
        components:{
            myAnnouncement,
            problemList
        }
    }
</script>

<style>

</style>