<script setup>
import { ref } from 'vue';
const open = ref(false);
const afterOpenChange = bool => {
  console.log('open', bool);
};
const showDrawer = () => {
  open.value = true;
};
</script>

<template>
  <div class="container-fluid">
    <div class="row text-white" style="background-color: #0c713d; padding: 1rem">

      <div class="col-9 d-flex align-items-center justify-content-start">
        <img src="@/assets/logo.svg" alt="logo" height="32" width="34" class="ms-3 me-3">
        <span class="d-flex">ADMIN</span>
      </div>

      <div class="col-3 d-flex align-items-center justify-content-end">
        <a>
          <router-link :to="{name: 'login'}">
            <span>Đăng xuất</span>
          </router-link>
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>