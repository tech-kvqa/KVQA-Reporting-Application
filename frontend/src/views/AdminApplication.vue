<template>
    <v-app>
      <!-- Admin Side Navigation Drawer -->
      <v-navigation-drawer app>
        <v-list>
          <v-list-item link to="/admin/dashboard">
            <v-list-item-content>
              <v-list-item-title>Admin Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/admin/users">
            <v-list-item-content>
              <v-list-item-title>Manage Users</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/admin/application">
            <v-list-item-content>
              <v-list-item-title>Manage Applications</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <container>
        <!-- Admin Top Navigation Bar -->
        <v-app-bar color="black" dark>
          <v-spacer></v-spacer>
          <span class="white--text text-h6">Admin - Manage Applications</span>
          <v-spacer></v-spacer>
          <v-btn text color="red" @click="logout">Logout</v-btn>
        </v-app-bar>
      </container>
  
      <!-- Main Content -->
      <v-main>
        <v-container>
          <v-btn color="primary" class="mb-4" @click="navigateToApplicationForm">
            Create new application
          </v-btn>
          <!-- Search Fields -->
          <v-row>
            <v-col cols="5">
              <v-text-field v-model="organisationName" label="Organisation Name"></v-text-field>
            </v-col>
            <v-col cols="5">
              <v-text-field v-model="auditNumber" label="Audit Number"></v-text-field>
            </v-col>
            <v-col cols="2">
              <v-btn color="primary" @click="searchApplications">Search</v-btn>
            </v-col>
          </v-row>
  
          <!-- Applications Table -->
          <v-card>
            <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
              User Applications:
            </v-card-title>
  
            <v-data-table :headers="headers" :items="applications" class="elevation-1">
              <!-- <template #[`item.approve`]="{ item }">
                <v-btn color="green" text @click="approveApplication(item.id)">Approve</v-btn>
              </template>
              <template #[`item.reject`]="{ item }">
                <v-btn color="red" text @click="rejectApplication(item.id)">Reject</v-btn>
              </template> -->
              <template #[`item.delete`]="{ item }">
                <v-btn color="red" text @click="deleteApplication(item.id)">Delete</v-btn>
              </template>
              <template #[`item.view`]="{ item }">
                <v-btn color="blue" text @click="viewApplication(item.org_name, item.audit_number)">View</v-btn>
              </template>
            </v-data-table>
          </v-card>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        organisationName: "",
        auditNumber: "",
        applications: [],
        headers: [
          { title: "S.NO", key: "id" },
          { title: "Organisation Name", key: "org_name" },
          { title: "Audit Number", key: "audit_number" },
          { title: "Application Status", key: "status" },
          { title: "Auditor", key: "auditor" },
          { title: "Decision Maker", key: "decision_maker" },
          // { title: "Approve", key: "approve", sortable: false },
          // { title: "Reject", key: "reject", sortable: false },
          { title: "Delete", key: "delete", sortable: false },
          { title: "View", key: "view", sortable: false }
        ]
      };
    },
    methods: {
      async fetchApplications() {
        try {
          const token = localStorage.getItem("token");
          if (!token) {
            throw new Error("No authentication token found. Please log in again.");
          }
  
          // const response = await axios.get("http://127.0.0.1:5000/admin/applications", {
          const response = await axios.get("http://127.0.0.1:5000/admin/applications", {
            headers: { Authorization: `Bearer ${token}` },
          });
  
          this.applications = response.data;
        } catch (error) {
          console.error("Error fetching applications:", error);
          alert("Failed to fetch applications. Please log in again.");
          this.$router.push("/admin/login");
        }
      },
  
      async approveApplication(id) {
        try {
          const token = localStorage.getItem("token");
          // await axios.put(`http://127.0.0.1:5000/admin/applications/${id}/approve`, {}, {
          await axios.put(`http://127.0.0.1:5000/admin/applications/${id}/approve`, {}, {
            headers: { Authorization: `Bearer ${token}` },
          });
  
          alert("Application approved successfully!");
          this.fetchApplications();
        } catch (error) {
          console.error("Error approving application:", error);
          alert("Failed to approve application.");
        }
      },
  
      async rejectApplication(id) {
        try {
          const token = localStorage.getItem("token");
          // await axios.put(`http://127.0.0.1:5000/admin/applications/${id}/reject`, {}, {
          await axios.put(`http://127.0.0.1:5000/admin/applications/${id}/reject`, {}, {
            headers: { Authorization: `Bearer ${token}` },
          });
  
          alert("Application rejected successfully!");
          this.fetchApplications();
        } catch (error) {
          console.error("Error rejecting application:", error);
          alert("Failed to reject application.");
        }
      },
  
      async deleteApplication(id) {
        try {
          const token = localStorage.getItem("token");
          // await axios.delete(`http://127.0.0.1:5000/admin/applications/${id}`, {
          await axios.delete(`http://127.0.0.1:5000/admin/applications/${id}`, {
            headers: { Authorization: `Bearer ${token}` },
          });
  
          this.applications = this.applications.filter(app => app.id !== id);
          alert("Application deleted successfully!");
        } catch (error) {
          console.error("Error deleting application:", error);
          alert("Failed to delete application.");
        }
      },
  
      async searchApplications() {
        try {
          const token = localStorage.getItem("token");
  
          const response = await axios.get("http://127.0.0.1:5000/admin/search", {
          // const response = await axios.get("https://kvqa-auditor-data-management.onrender.com/admin/search", {
            headers: { Authorization: `Bearer ${token}` },
            params: {
              org_name: this.organisationName.trim(),
              audit_number: this.auditNumber.trim(),
            },
          });
  
          this.applications = response.data;
        } catch (error) {
          console.error("Error searching applications:", error);
          alert("Failed to fetch filtered applications.");
        }
      },
  
      viewApplication(organisationName, auditNumber) {
        this.$router.push({
          name: "AdminApplicationDetails",
          params: { organisation_name: organisationName, audit_number: auditNumber }
        });
      },
  
      logout() {
        localStorage.removeItem("token");
        this.$router.push("/admin/login");
      },

      navigateToApplicationForm() {
        this.$router.push("/applicationform");
      },
    },
    created() {
      this.fetchApplications();
    }
  };
  </script>
  
  