<template>
  <div class="profile-update">
    <h2>Update Profile</h2>
    <form @submit.prevent="handleUpdateProfile">
      <!-- First Name -->
      <div class="form-group">
        <label for="first-name">First Name:</label>
        <input
          v-model="firstName"
          type="text"
          id="first-name"
          placeholder="Enter First Name"
          required
        />
      </div>

      <!-- Last Name -->
      <div class="form-group">
        <label for="last-name">Last Name:</label>
        <input
          v-model="lastName"
          type="text"
          id="last-name"
          placeholder="Enter Last Name"
          required
        />
      </div>

      <!-- Email -->
      <div class="form-group">
        <label for="email">Email:</label>
        <input
          v-model="email"
          type="email"
          id="email"
          placeholder="Enter Email"
          required
        />
      </div>

      <!-- Phone Number -->
      <div class="form-group">
        <label for="phone-number">Phone Number:</label>
        <input
          v-model="phoneNumber"
          type="text"
          id="phone-number"
          placeholder="Enter Phone Number"
          required
        />
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">Update Profile</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import config from "../config/config"; // Import config for base_url

export default {
  name: "ProfileUpdate",
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      phoneNumber: "",
    };
  },
  created() {
    // Fetch current profile details to prefill the form
    this.fetchProfile();
  },
  methods: {
    async fetchProfile() {
      const accessToken = localStorage.getItem("access_token");

      if (!accessToken) {
        await this.$router.push("/login");
        return;
      }

      try {
        const response = await axios.get(`${config.base_url}/users/profile/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        // Prefill the form with current profile data
        this.firstName = response.data.first_name || "";
        this.lastName = response.data.last_name || "";
        this.email = response.data.email || "";
        this.phoneNumber = response.data.phone_number || "";
      } catch (error) {
        console.error("Error fetching profile:", error.response?.data || error.message);
        this.$router.push("/login");
      }
    },
    async handleUpdateProfile() {
      const accessToken = localStorage.getItem("access_token");

      if (!accessToken) {
        this.$router.push("/login");
        return;
      }

      const payload = {
        first_name: this.firstName,
        last_name: this.lastName,
        email: this.email,
        phone_number: this.phoneNumber,
      };

      try {
        const response = await axios.put(
          `${config.base_url}/users/profile/update/`,
          payload,
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );

        console.log("Profile updated successfully:", response.data);
        alert("Profile updated successfully!");
        await this.$router.push("/profile");
      } catch (error) {
        console.error("Error updating profile:", error.response?.data || error.message);
        alert("Failed to update profile. Please try again.");
      }
    },
  },
};
</script>

<style scoped>
.profile-update {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

input:focus {
  outline: none;
  border-color: #e74c3c;
  box-shadow: 0 0 5px rgba(231, 76, 60, 0.5);
}

button {
  width: 100%;
  padding: 10px;
  background-color: #e74c3c;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #c0392b;
}
</style>
