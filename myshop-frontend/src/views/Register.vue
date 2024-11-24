<template>
  <div class="register-page">
    <h1>Register</h1>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Username</label>
        <input v-model="username" type="text" id="username" placeholder="Enter your username" required />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" placeholder="Enter your email" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" placeholder="Enter your password" required />
      </div>
      <div class="form-group">
        <label for="phone_number">Phone Number</label>
        <input v-model="phone_number" type="text" id="phone_number" placeholder="Enter your phone number" required />
      </div>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import config from '../config/config';  // Import config
export default {
  name: "Register",
  data() {
    return {
      username: '',
      email: '',
      password: '',
      phone_number: ''
    };
  },
  methods: {
    async handleRegister() {
      const payload = {
        username: this.username,
        email: this.email,
        password: this.password,
        phone_number: this.phone_number
      };
      try {
        const response = await axios.post(`${config.base_url}/users/register/`, payload);
        alert('Registration successful');
        this.$router.push('/login');
      } catch (error) {
        console.error(error);
        alert('Registration failed');
      }
    }
  }
};
</script>


<style scoped>
.register-page {
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
