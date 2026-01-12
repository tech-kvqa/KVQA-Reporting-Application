<template>
    <v-app>
      <!-- Top Navigation Bar -->
      <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to Decision Maker Dashboard!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
      </v-app-bar>
  
      <!-- Side Navigation Drawer -->
      <v-navigation-drawer app permanent width="200">
        <v-list>
          <v-list-item link to="/dashboard">
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/application">
            <v-list-item-content>
              <v-list-item-title>Application</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/decisionmaker">
            <v-list-item-content>
              <v-list-item-title>Decision Maker</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
  
      <!-- Main Content -->
      <v-main>
        <v-container fluid>
          <!-- Search Fields -->
          <v-row>
            <v-col cols="5">
              <v-text-field v-model="organisationName" label="Organisation Name"></v-text-field>
            </v-col>
            <v-col cols="5">
              <v-text-field v-model="auditNumber" label="Audit Number"></v-text-field>
            </v-col>
            <v-col cols="2">
              <v-btn color="primary" @click="searchDecisionMakerApps">Search</v-btn>
            </v-col>
          </v-row>
  
          <!-- Applications Table -->
          <v-card>
            <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
              Applications Where You Are a Decision Maker:
            </v-card-title>
  
            <v-data-table :headers="headers" :items="decisionMakerApps" class="elevation-1">
              <template #[`item.approve`]="{ item }">
                <v-btn color="green" text @click="approveApplication(item.id)">Approve</v-btn>
              </template>
              <template #[`item.reject`]="{ item }">
                <v-btn color="red" text @click="rejectApplication(item.id)">Reject</v-btn>
              </template>
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
        decisionMakerApps: [],
        organisationName: "",
        auditNumber: "",
        applications: [],
        headers: [
          { title: "Organisation Name", key: "org_name" },
          { title: "Audit Number", key: "audit_number" },
          { title: "Auditor", key: "auditor" },
          { title: "Status", key: "status" },
          { title: "Approve", key: "approve", sortable: false },
          { title: "Reject", key: "reject", sortable: false },
          { title: "Delete", key: "delete", sortable: false },
          { title: "View", key: "view", sortable: false },
        ]
      };
    },
    methods: {
      async fetchDecisionMakerApps() {
        try {
          const token = localStorage.getItem("token");
          // const response = await axios.get("http://127.0.0.1:5000/decision-maker-applications", {
          const response = await axios.get("https://kvqa-reporting-application.onrender.com/decision-maker-applications", {
            headers: { Authorization: `Bearer ${token}` }
          });
          this.decisionMakerApps = response.data.applications;
        } catch (error) {
          console.error("Error fetching decision maker applications:", error);
        }
      },
      searchDecisionMakerApps() {
        this.decisionMakerApps = this.decisionMakerApps.filter(app => 
          (this.organisationName ? app.org_name.includes(this.organisationName) : true) &&
          (this.auditNumber ? app.audit_number.includes(this.auditNumber) : true)
        );
      },
      viewApplication(organisationName, auditNumber) {
        this.$router.push(`/decision/application/${organisationName}/${auditNumber}`);
    },

    async approveApplication(id) {
        try {
          const token = localStorage.getItem("token");
          // await axios.put(`http://127.0.0.1:5000/admin/applications/${id}/approve`, {}, {
          await axios.put(`https://kvqa-reporting-application.onrender.com/admin/applications/${id}/approve`, {}, {
            headers: { Authorization: `Bearer ${token}` },
          });
  
          alert("Application approved successfully!");
          this.fetchDecisionMakerApps();
        } catch (error) {
          console.error("Error approving application:", error);
          alert("Failed to approve application.");
        }
      },
  
      async rejectApplication(id) {
        try {
          const token = localStorage.getItem("token");
          // await axios.put(`http://127.0.0.1:5000/admin/applications/${id}/reject`, {}, {
          await axios.put(`https://kvqa-reporting-application.onrender.com/admin/applications/${id}/reject`, {}, {
            headers: { Authorization: `Bearer ${token}` },
          });
  
          alert("Application rejected successfully!");
          this.fetchDecisionMakerApps();
        } catch (error) {
          console.error("Error rejecting application:", error);
          alert("Failed to reject application.");
        }
      },
  
      async deleteApplication(id) {
        try {
          const token = localStorage.getItem("token");
          // await axios.delete(`http://127.0.0.1:5000/admin/applications/${id}`, {
          await axios.delete(`https://kvqa-reporting-application.onrender.com/admin/applications/${id}`, {
            headers: { Authorization: `Bearer ${token}` },
          });
  
          this.applications = this.applications.filter(app => app.id !== id);
          alert("Application deleted successfully!");
        } catch (error) {
          console.error("Error deleting application:", error);
          alert("Failed to delete application.");
        }
      },
      logout() {
        localStorage.removeItem("token");
        this.$router.push("/");
      }
    },
    mounted() {
      this.fetchDecisionMakerApps();
    }
  };
  </script>
  