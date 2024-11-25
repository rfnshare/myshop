<template>
  <div class="register-page">
    <h1>Register</h1>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="first-name">First Name:</label>
        <input v-model="firstName" type="text" id="first-name" placeholder="Enter first name" required />
      </div>
      <div class="form-group">
        <label for="last-name">Last Name:</label>
        <input v-model="lastName" type="text" id="last-name" placeholder="Enter last name" required />
      </div>
      <div class="form-group">
        <label for="username">Username</label>
        <input v-model="userName" type="text" id="username" placeholder="Enter your username" required />
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
      <div class="form-group">
        <label for="profile-pic">Profile Picture:</label>
        <input @change="handleFileUpload" type="file" id="profile-pic" accept="image/*" />
      </div>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import config from "../config/config"; // Import config for base_url

export default {
  name: "Register",
  data() {
    return {
      userName: "",
      firstName: "",  // First name for registration
      lastName: "",   // Last name for registration
      email: "",      // Email for registration
      phone_number: "",
      password: "",   // Password for registration
      profilePic: null, // Profile picture file
    };
  },
  methods: {
    handleFileUpload(event) {
      this.profilePic = event.target.files[0]; // Save the uploaded file to data
    },
    async handleRegister() {
      const formData = new FormData(); // Create FormData for file upload
      formData.append("username", this.userName);
      formData.append("first_name", this.firstName);
      formData.append("last_name", this.lastName);
      formData.append("last_name", this.phone_number);
      formData.append("email", this.email);
      formData.append("password", this.password);
      if (this.profilePic) {
        formData.append("profile_pic", this.profilePic);
      }

      try {
        const response = await axios.post(`${config.base_url}/users/register/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data", // Ensure correct content type for file upload
          },
        });
        console.log("Registration successful:", response.data);

        // Redirect to login page on successful registration
        this.$router.push("/login");
      } catch (error) {
        console.error("Registration failed:", error.response?.data || error.message);
      }
    },
  },
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
