<template>
  <div class="admin-login">
    <h1>Admin Login</h1>
    <form @submit.prevent="handleAdminLogin">
      <div class="form-group">
        <label for="username">Username:</label>
        <input v-model="username" type="text" id="username" placeholder="Enter username" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input v-model="password" type="password" id="password" placeholder="Enter password" required />
      </div>
      <button type="submit" class="btn">Login</button>
    </form>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "axios";
import config from "../config/config";

export default {
  name: "AdminLogin",
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
    };
  },
  methods: {
    async handleAdminLogin() {
      try {
        const payload = {
          username: this.username,
          password: this.password,
        };

        const response = await axios.post(`${config.base_url}/users/login/`, payload);
        console.log("Admin logged in:", response.data);

        // Store tokens locally
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);

        // Redirect to admin dashboard
        this.$router.push("/admin/dashboard");
      } catch (error) {
        console.error("Admin login failed:", error.response?.data || error.message);
        this.errorMessage = error.response?.data?.message || "Login failed. Please try again.";
      }
    },
  },
};
</script>

<style scoped>
.admin-login {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  background-color: #333;
  color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 95%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: red;
  color: white;
  width: 100%;
  padding: 10px;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: darkred;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}
</style>
