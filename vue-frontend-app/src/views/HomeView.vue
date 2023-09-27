<template>
    <div id="home">
        <h5>Home</h5>
    </div>
</template>
<script>
import UserService from "../services/user.service"
import axios from 'axios';

export default {
  name: "Login_Page",
  data() {
    return {
    };
  },
  computed: {
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
    // Define the URL of the API you want to fetch data from
    const apiUrl = 'http://127.0.0.1:8000/api/auth/user/profile/';

    // Make the GET request using Axios
    axios.get(apiUrl)
      .then(response => {
        // Handle the successful response here
        console.log('Data:', response.data);
      })
      .catch(error => {
        // Handle any errors here
        console.error('Error:', error);
      });
  }
  },
};
</script>
