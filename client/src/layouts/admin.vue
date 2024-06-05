<script>
  import TheHeader from "@/components/TheHeader.vue";
  export default {
    components: {
      TheHeader
    }
  }
</script>

<template>
  <TheHeader/>

  <div class="container-fluid">
    <div class="row">
<!--      <div class="col-sm-3 d-none d-sm-flex">-->
<!--        Sider Bar-->
<!--      </div>-->
      <div class="col-12">
          <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>