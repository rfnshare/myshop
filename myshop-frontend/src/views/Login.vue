<template>
  <div class="login-page">
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username</label>
        <input v-model="username" type="text" id="username" placeholder="Enter your username" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" placeholder="Enter your password" required />
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import config from '../config/config';  // Import config

export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async handleLogin() {
      const payload = {
        username: this.username,
        password: this.password
      };
      try {
        const response = await axios.post(`${config.base_url}/users/login/`, payload);

        // Correct keys based on API response
        localStorage.setItem('access_token', response.data.access);  // Use 'access' key from API response
        localStorage.setItem('refresh_token', response.data.refresh);  // Use 'refresh' key from API response

        // Redirect to the dashboard on successful login
        await this.$router.push('/dashboard');
        console.log("Login successful");
      } catch (error) {
        console.error("Login failed:", error.response?.data || error.message);
      }

    }
  }
};
</script>


<style scoped>
.login-page {
  padding: 20px;
  max-width: 400px;
  margin: auto;
  text-align: left;
  background-color: #222;
  color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

h1 {
  text-align: center;
  color: #e74c3c;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  font-size: 1rem;
  background-color: #333;
  border: 1px solid #444;
  color: #fff;
  border-radius: 5px;
}

button {
  margin-top: 10px;
  background-color: #e74c3c;
  border: none;
  color: white;
  padding: 10px;
  width: 100%;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #c0392b;
}
</style>
