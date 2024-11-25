<template>
  <div v-if="dashboardStats" class="dashboard-stats">
    <p>Total Customers: {{ dashboardStats.total_customers }}</p>
    <p>Total Admins: {{ dashboardStats.total_admins }}</p>
    <p>Active Customers: {{ dashboardStats.active_customers }}</p>
  </div>

  <div class="admin-dashboard">
    <div class="header">
      <h1 v-if="isAdmin">Admin Dashboard</h1>
      <h1 v-else>Access Denied</h1>
      <button v-if="isAdmin" @click="handleLogout" class="logout-btn">Logout</button>
      <button @click="goToProductManagement" class="btn btn-primary">Product Management</button>
    </div>

    <div v-if="isAdmin" class="dashboard-content">
      <p>Welcome, Admin! This is your dashboard.</p>
    </div>
    <div v-else class="error-content">
      <p>You are not authorized to view this page. Please log in as an admin.</p>
    </div>
    <div v-if="customers.length" class="customer-list">
      <h3>Customer List</h3>
      <ul>
        <li v-for="customer in customers" :key="customer.id">
          <strong>◉ {{ customer.username }}</strong> - {{ customer.email }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No customers found.</p>
    </div>



  </div>
</template>

<script>
import axios from "axios";
import config from "../config/config";

export default {
  name: "AdminDashboard",
  data() {
    return {
      isAdmin: false, // Determine if the user is an admin,
      dashboardStats: null,
      customers: []
    };
  },
  created() {
    this.validateUser();
    this.fetchDashboardStats();
    this.fetchCustomers();
  },

  methods: {
    goToProductManagement() {
      // Navigate to the product management page
      this.$router.push('/admin/product-management');
    },
    async fetchCustomers() {
      const accessToken = localStorage.getItem("access_token"); // Get the access token

      if (!accessToken) return;

      try {
        // Fetch customer list
        const response = await axios.get(`${config.base_url}/users/admin/customers/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        // Save the customer list in the component's data
        this.customers = response.data;
      } catch (error) {
        console.error("Error fetching customers:", error.response?.data || error.message);
      }
    },
    async validateUser() {
      const accessToken = localStorage.getItem("access_token"); // Get the access token

      if (!accessToken) {
        // If no token is available, redirect to the admin login page
        this.$router.push("/admin/login");
        return;
      }

      try {
        // Fetch profile details to validate user role
        const response = await axios.get(`${config.base_url}/users/profile/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        // Check if the user is an admin (is_staff: true)
        this.isAdmin = response.data.is_staff;

        if (!this.isAdmin) {
          console.error("Access denied: User is not an admin");
          // this.$router.push("/login"); // Redirect to user login if not an admin
        }
      } catch (error) {
        console.error(
            "Error validating user role:",
            error.response?.data || error.message
        );
        this.$router.push("/admin/login"); // Redirect to admin login on error
      }
    },
    async fetchDashboardStats() {
      const accessToken = localStorage.getItem("access_token"); // Get the access token

      if (!accessToken) return;

      try {
        // Fetch admin dashboard stats
        const response = await axios.get(`${config.base_url}/users/admin/dashboard/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        // Save stats in the component's data
        this.dashboardStats = response.data;
      } catch (error) {
        console.error("Error fetching admin dashboard stats:", error.response?.data || error.message);
      }
    },

    async handleLogout() {
      const accessToken = localStorage.getItem("access_token");
      const refreshToken = localStorage.getItem("refresh_token");

      if (!accessToken || !refreshToken) {
        console.error("No tokens found for logout");
        return;
      }

      try {
        // Call the logout API
        await axios.post(
            `${config.base_url}/users/logout/`,
            {refresh: refreshToken},
            {
              headers: {
                Authorization: `Bearer ${accessToken}`,
              },
            }
        );

        // Clear tokens from localStorage after successful logout
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");

        // Redirect to admin login page
        this.$router.push("/admin/login");
        console.log("Admin logged out successfully");
      } catch (error) {
        console.error("Admin logout failed:", error.response?.data || error.message);
      }
    },
  },
};
</script>

<style scoped>
.admin-dashboard {
  padding: 20px;
  color: #333;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logout-btn {
  background-color: red;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}

.logout-btn:hover {
  background-color: darkred;
}

.dashboard-content {
  margin-top: 20px;
}

.error-content {
  margin-top: 20px;
  color: red;
  font-weight: bold;
  text-align: center;
}

.dashboard-stats {
  margin-top: 10px;
  background-color: #f7f7f7;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  color: #333;
}

.dashboard-stats p {
  margin: 5px 0;
  font-size: 14px;
}

.customer-list {
  margin-top: 20px;
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 5px;
}

.customer-list h3 {
  margin-bottom: 10px;
  color: #333;
}

.customer-list ul {
  list-style-type: none;
  padding: 0;
}

.customer-list li {
  margin: 5px 0;
  padding: 5px;
  border-bottom: 1px solid #ddd;
  font-size: 14px;
}

.customer-list li:last-child {
  border-bottom: none;
}

</style>
