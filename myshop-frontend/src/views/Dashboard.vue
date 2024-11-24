<template>
  <div class="dashboard">
    <div class="header">
      <h2>Welcome to Your Dashboard</h2>
      <div class="actions">
        <!-- Cart Icon -->
        <span class="cart-icon">🛒</span>

        <!-- Profile Button -->
        <button class="profile-btn" @click="goToProfile">
          <img src="../../src/assets/profile-icon.svg" alt="Profile" />
        </button>

        <!-- Logout Button -->
        <button @click="handleLogout" class="btn btn-danger">Logout</button>
      </div>
    </div>

    <!-- Random Dashboard Content -->
    <section class="random-content">
      <h3>Latest Updates</h3>
      <p>Here are some random updates or offers that we want to show to the user.</p>
      <div class="offer">
        <p>Offer 1: 10% off on your next purchase!</p>
      </div>
      <div class="offer">
        <p>Offer 2: Free shipping on orders above $50!</p>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import config from '../config/config';  // Import config

export default {
  name: "Dashboard",
  data() {
    return {
      // Add any data properties related to the dashboard here
    };
  },
  created() {
    // Validate if the user is authenticated on component creation
    this.validateUser();
  },
  methods: {
    // Method to check if the user is logged in (i.e., has a valid access token)
    validateUser() {
      const accessToken = localStorage.getItem('access_token');  // Get access token

      if (!accessToken) {
        // If there's no access token, redirect to login
        this.$router.push('/login');
      } else {
        // Validate the token on the backend (e.g., by making an API call)
        this.checkTokenValidity(accessToken);
      }
    },
    // Method to check if the access token is valid
    async checkTokenValidity(token) {
      try {
        const response = await axios.get(`${config.base_url}/users/profile/`, {
          headers: {
            Authorization: `Bearer ${token}`,  // Pass the access token in the header
          }
        });
        console.log('Token is valid:', response.data);
      } catch (error) {
        // If token is invalid, redirect to login
        console.error('Invalid token or unauthorized access:', error.response?.data);
        this.$router.push('/login');
      }
    },

    // Method to navigate to the Profile page
    goToProfile() {
      this.$router.push('/profile');
    },

    // Method to handle logout
    async handleLogout() {
      const accessToken = localStorage.getItem('access_token');  // Get access token
      const refreshToken = localStorage.getItem('refresh_token'); // Get refresh token

      if (!accessToken || !refreshToken) {
        console.error("No tokens found for logout");
        return;
      }

      try {
        // Send the refresh token in the payload and the access token in the Authorization header
        const response = await axios.post(
            `${config.base_url}/users/logout/`,
            { refresh: refreshToken },  // Refresh token in the payload
            {
              headers: {
                'Authorization': `Bearer ${accessToken}`  // Bearer token in the header
              }
            }
        );

        // Clear tokens from localStorage after logout
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');

        // Redirect to login page after successful logout
        this.$router.push('/login');
        console.log("Logged out successfully");
      } catch (error) {
        // Log the error response if the request fails
        console.error("Logout failed:", error.response?.data || error.message);
      }
    }
  }
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
  color: #fff;
  background-color: #333;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cart-icon {
  font-size: 1.5rem;
  margin-right: 15px;
}

.actions {
  display: flex;
  align-items: center;
}

/* Profile button style */
/* Profile button with icon */
.profile-btn {
  background: linear-gradient(45deg, #e74c3c, #333); /* Red-Black gradient background */
  border: none;
  padding: 10px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease, transform 0.2s ease;
  margin-right: 15px; /* Space between profile and logout button */
}

.profile-btn:hover {
  background: linear-gradient(45deg, #c0392b, #222); /* Darker red-black on hover */
  transform: scale(1.1); /* Slight zoom effect on hover */
}

.profile-btn img {
  width: 20px;  /* Adjust size of the profile icon */
  height: 20px;
  object-fit: contain;
}

/* Action buttons container */
.actions {
  display: flex;
  align-items: center;
  justify-content: flex-end; /* Align buttons to the right */
}

button {
  background-color: #e74c3c;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 10px; /* Space between logout and profile button */
}

button:hover {
  background-color: #c0392b;
}

.random-content {
  margin-top: 20px;
}

.offer {
  background-color: #444;
  padding: 10px;
  margin: 10px 0;
  border-radius: 5px;
}
</style>
