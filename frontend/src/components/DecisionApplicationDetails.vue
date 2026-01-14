<template>
    <v-container fluid class="full-screen-container">
      <v-card class="pa-4 full-screen-card">
        <v-card-title class="text-h5 font-weight-bold">Application Details</v-card-title>
        <v-divider class="mb-4"></v-divider>
  
        <!-- Organisation & Audit Details -->
        <v-row>
          <v-col cols="12" md="6">
            <v-card outlined class="pa-3">
              <v-card-subtitle class="text-h6 font-weight-bold">Organisation Name</v-card-subtitle>
              <v-card-text class="text-body-1">{{ organisation_name }}</v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" md="6">
            <v-card outlined class="pa-3">
              <v-card-subtitle class="text-h6 font-weight-bold">Audit Number</v-card-subtitle>
              <v-card-text class="text-body-1">{{ audit_number }}</v-card-text>
            </v-card>
          </v-col>
        </v-row>
        <!-- Zip File Download -->
        <v-row class="mt-3">
          <v-col cols="12">
            <v-btn v-if="adminapplicationDetails?.zip_file_name"
                  color="primary"
                  class="elevation-1"
                  @click="downloadFile(adminapplicationDetails?.zip_file_name)">
              Download Zip File
            </v-btn>
          </v-col>
        </v-row>
  
        <!-- Stage 1 Details -->
        <v-card v-if="adminapplicationDetails && adminapplicationDetails.stage1" class="mt-4 pa-4 elevation-2 details-card">
  <v-card-title class="text-h6 font-weight-bold">Stage 1 Details</v-card-title>
  <v-divider class="mb-3"></v-divider>

  <v-row>
    <v-col cols="12" md="4">
      <v-card-subtitle class="text-body-1 font-weight-medium">Date of Audit</v-card-subtitle>
      <v-card-text>{{ formatDate(adminapplicationDetails.stage1.selected_date) }}</v-card-text>
    </v-col>
    <v-col cols="12" md="4">
      <v-card-subtitle class="text-body-1 font-weight-medium">Mail To</v-card-subtitle>
      <v-card-text>{{ adminapplicationDetails.stage1.mail_to }}</v-card-text>
    </v-col>
    <v-col cols="12" md="4">
      <v-card-subtitle class="text-body-1 font-weight-medium">Mail From</v-card-subtitle>
      <v-card-text>{{ adminapplicationDetails.stage1.mail_from }}</v-card-text>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="6">
      <v-card-subtitle class="text-body-1 font-weight-medium">Date of Comment</v-card-subtitle>
      <v-card-text>{{ formatDate(adminapplicationDetails.stage1.selected_comment_date) }}</v-card-text>
    </v-col>
    <v-col cols="6">
      <v-card-subtitle class="text-body-1 font-weight-medium mt-3">Scope</v-card-subtitle>
      <v-card-text>{{ adminapplicationDetails.stage1.scope }}</v-card-text>
    </v-col>
  </v-row>

  <v-row class="mt-3">
    <v-col cols="12" md="6">
      <v-btn v-if="adminapplicationDetails.stage1.stage1_plan"
             color="primary"
             class="elevation-1"
             @click="downloadFile(adminapplicationDetails.stage1.stage1_plan)">
        Download Stage 1 Plan
      </v-btn>
    </v-col>
    <v-col cols="12" md="6">
      <v-btn v-if="adminapplicationDetails.stage1.stage1_report"
             color="primary"
             class="elevation-1"
             @click="downloadFile(adminapplicationDetails.stage1.stage1_report)">
        Download Stage 1 Report
      </v-btn>
    </v-col>
  </v-row>
</v-card>
  
        <!-- Stage 2 Details -->
        <v-card v-if="adminapplicationDetails && adminapplicationDetails.stage2" class="mt-4 pa-4 elevation-2 details-card">
  <v-card-title class="text-h6 font-weight-bold">Stage 2 Details</v-card-title>
  <v-divider class="mb-3"></v-divider>

  <v-row>
    <v-col cols="12" md="4">
      <v-card-subtitle class="text-body-1 font-weight-medium">Date of Audit</v-card-subtitle>
      <v-card-text>{{ formatDate(adminapplicationDetails.stage2.selected_date) }}</v-card-text>
    </v-col>
    <v-col cols="12" md="4">
      <v-card-subtitle class="text-body-1 font-weight-medium">Mail To</v-card-subtitle>
      <v-card-text>{{ adminapplicationDetails.stage2.mail_to }}</v-card-text>
    </v-col>
    <v-col cols="12" md="4">
      <v-card-subtitle class="text-body-1 font-weight-medium">Mail From</v-card-subtitle>
      <v-card-text>{{ adminapplicationDetails.stage2.mail_from }}</v-card-text>
    </v-col>
  </v-row>

  <v-row>
    <v-col cols="6">
      <v-card-subtitle class="text-body-1 font-weight-medium">Date of Comment</v-card-subtitle>
      <v-card-text>{{ formatDate(adminapplicationDetails.stage2.selected_comment_date) }}</v-card-text>
    </v-col>
    <v-col cols="6">
      <v-card-subtitle class="text-body-1 font-weight-medium mt-3">Scope</v-card-subtitle>
      <v-card-text>{{ adminapplicationDetails.stage2.scope }}</v-card-text>
    </v-col>
  </v-row>

  <v-row class="mt-3">
    <v-col cols="12" md="6">
      <v-btn v-if="adminapplicationDetails.stage2.stage2_plan"
             color="primary"
             class="elevation-1"
             @click="downloadFile(adminapplicationDetails.stage2.stage2_plan)">
        Download Stage 2 Plan
      </v-btn>
    </v-col>
    <v-col cols="12" md="6">
      <v-btn v-if="adminapplicationDetails.stage2.stage2_report"
             color="primary"
             class="elevation-1"
             @click="downloadFile(adminapplicationDetails.stage2.stage2_report)">
        Download Stage 2 Report
      </v-btn>
    </v-col>
  </v-row>
</v-card>
  
        <!-- Back Button -->
        <v-card-actions class="justify-center">
          <v-btn color="blue-darken-3" class="mt-4" @click="$router.push('/decisionmaker')">
            Back
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
    
    <script>
    import axios from "axios";
    
    export default {
      props: ["organisation_name"],
      data() {
        return {
          // organisation_name: this.$route.params.organisation_name || "",
          audit_number: this.$route.params.audit_number || "",
          // adminapplicationDetails: { stage1: {}, stage2: {} },
          // adminapplicationDetails: { applications: [] },
          // adminapplicationDetails: {
          //   stage1: {}, // Ensure these objects exist initially
          //   stage2: {}
          // },
          // // adminapplicationDetails: {}
          // isLoading: true,
          adminapplicationDetails: null,
        };
      },

      computed: {
        organisationName() {
          return this.organisation_name || this.$route.params.organisation_name || "";
        }
      },
      methods: {
      //   async fetchAdminApplication() {
      //   try {
      //     const token = localStorage.getItem("token");
      //     if (!token) {
      //       throw new Error("No authentication token found. Please log in again.");
      //     }
  
      //     const response = await axios.get(`http://127.0.0.1:5000/admin/application/${this.organisation_name}`, {
      //     // const response = await axios.get(`https://kvqa-data-management-application.onrender.com/application/${this.organisation_name}`, {
      //       headers: {
      //         Authorization: `Bearer ${token}`,
      //       },
      //     });

      //     console.log(response.data)
  
      //     this.adminapplicationDetails = await response.data;
      //     console.log(this.adminapplicationDetails)
      //   } catch (error) {
      //     console.error("Error fetching application details:", error);
      //     alert("Failed to fetch details. Please log in again.");
      //     this.$router.push("/admin/application");
      //   }
      // },

      async fetchAdminApplication() {
  try {
    // const response = await axios.get(`http://127.0.0.1:5000/decision/application/${this.organisation_name}`);
    const response = await axios.get(`https://kvqa-reporting-application.onrender.com/decision/application/${this.organisation_name}`);
    console.log(response.data);

    if (response.data?.applications?.length > 0) {
      this.adminapplicationDetails = response.data.applications[0]; // Ensure the correct structure
      console.log(this.adminapplicationDetails.stage1.selected_date)
    } else {
      console.error("No application data found.");
      this.applicationDetails = {}; // Prevent undefined errors
    }
  } catch (error) {
    console.error("Error fetching application details:", error);
    this.applicationDetails = {}; // Prevent undefined errors
  }
},


    
        async downloadFile(filename) {
          try {
            const token = localStorage.getItem("token");
            if (!token) {
              throw new Error("No authentication token found. Please log in again.");
            }
    
            const cleanFilename = filename.replace(/^uploads\//, "");
            // const response = await axios.get(`http://127.0.0.1:5000/admin/download/${encodeURIComponent(cleanFilename)}`, {
            const response = await axios.get(`https://kvqa-reporting-application.onrender.com/admin/download/${encodeURIComponent(cleanFilename)}`, {
              headers: { Authorization: `Bearer ${token}` },
              responseType: "blob",
            });
    
            const blob = new Blob([response.data], { type: response.headers["content-type"] });
            const link = document.createElement("a");
            link.href = window.URL.createObjectURL(blob);
            link.setAttribute("download", cleanFilename);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
          } catch (error) {
            console.error("Error downloading file:", error);
            alert("Failed to download the file.");
          }
        },
  
        formatDate(dateString) {
      if (!dateString) return "Invalid Date"; // Handle null/undefined cases
  
      const date = new Date(dateString);
      if (isNaN(date)) return "Invalid Date"; // Handle incorrect date formats
  
      return date.toDateString(); // Outputs: "Thu Feb 27 2025"
    }
      },
      created() {
        this.fetchAdminApplication();
      },
    };

// import { onMounted, ref } from "vue";
// import axios from "axios";

// export default {
//   props: ["organisation_name"],
//   setup(props) {
//     const adminapplicationDetails = ref(null);

//     const fetchAdminApplication = async () => {
//       try {
//         const response = await axios.get(
//           `http://127.0.0.1:5000/admin/application/${props.organisation_name}`
//         );
//         console.log(response.data)
//         // adminapplicationDetails.value = response.data?.applications?.[0] || {};
//         adminapplicationDetails = response.data.applications[0]
//         console.log(response.data)
//         console.log('appluication details: ', adminapplicationDetails.stage1)
//       } catch (error) {
//         console.error("Error fetching application details:", error);
//       }
//     };

//     onMounted(fetchAdminApplication);

//     return { adminapplicationDetails };
//   },
// };

    </script>
    
    
    