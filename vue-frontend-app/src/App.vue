<template>
  <component :is="layout" />
  <span class="loader" v-if="loading">Loading...</span>
</template>
<script>
import AuthLayout from "@/layouts/AuthLayout";
import DashboardLayout from "@/layouts/DashboardLayout";
import FreeSpaceLayout from "@/layouts/FreeSpaceLayout";
import axios from "axios";
export default {
  components: {
    AuthLayout,
    DashboardLayout,
    FreeSpaceLayout,
  },
  data() {
    return {
      layout: null,
      loading: false,
    };
  },
  watch: {
    $route(to) {
      // set layout by route meta
      if (to.meta.layout !== undefined) {
        this.layout = to.meta.layout;
      } else {
        this.layout = "DashboardLayout"; // this is default layout if route meta is not set
      }
    },
  },
  created() {
    // Set up Axios interceptor
    axios.interceptors.request.use(
      (config) => {
        this.loading = true
        return config;
      },
      (error) => {
        // Hide the loader on error (optional)
        this.loading = false
        return Promise.reject(error);
      },
    );

    axios.interceptors.response.use(
      (response) => {
        // Hide the loader when the response is received
        this.loading = false
        return response;
      },
      (error) => {
        // Hide the loader on error (optional)
        this.loading = false
        return Promise.reject(error);
      },
    );
  },
};
</script>
<style lang="scss">
  @import'~bootstrap/dist/css/bootstrap.css'
</style>
