<!-- <template>
  <v-app>
    <v-container>
    <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to dashboard User!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
        <v-btn color="primary" @click="goBack">Cancel</v-btn>
      </v-app-bar>
    </v-container>
    <v-container>
      <v-card class="pa-5 mt-3 mx-auto" max-width="800">
        <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
          Stage 1 Form
        </v-card-title>
  
        <v-card-text>
          <v-form @submit.prevent="submitStage1">
            <v-row>    
              <v-col cols="6">
                <v-text-field v-model="organisationName" label="Organisation Name" disabled></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="scope" label="Scope" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-file-input label="Stage 1 Plan Upload *" v-model="stage1Plan" required></v-file-input>
              </v-col>

              <v-col cols="6">
                <v-file-input label="Additional Data *" v-model="additionaldata"></v-file-input>
              </v-col> -->
  
              <!-- <v-col cols="6"> -->
                <!-- <v-text-field v-model="mailFrom" label="Mail From" required></v-text-field> -->
                <!-- <v-text-field v-model="mailTo" label="Mail To" required></v-text-field> -->
                <!-- <v-select
                  v-model="mailFrom"
                  label="Mail From"
                  :items="['abc@kvqaindia.com', 'training@kvqaindia.com', 'tech@kvqaindia.com']"
                  required
                ></v-select> -->
              <!-- </v-col> -->
              <!-- <v-col cols="6">
                <v-text-field v-model="mailTo" label="Mail To" required></v-text-field>
              </v-col>

              <v-col cols="6">
                <v-menu 
                    v-model="menu" 
                    :close-on-content-click="false" 
                    transition="scale-transition"
                    >
                    <template v-slot:activator="{ props }">
                        <v-text-field
                            v-model="formattedSelectedDate"
                            label="Select Date"
                            readonly
                            v-bind="props"
                        ></v-text-field>
                    </template> -->
                
                <!-- <v-date-picker 
                    v-model="selectedDate"
                    @update:modelValue="updateDate"
                ></v-date-picker> -->
                    <!-- <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeRoleDate" hide-actions @click.native.stop elevation="24" :show-adjacent-months="true" :view-mode="'year'" :min="'2022-01-01'" :max="'2030-12-31'">
                        </v-date-picker>
                        </v-row>
                    </v-container>
                </v-menu>
            </v-col>
              <v-col cols="12"> -->
                <!-- <v-btn v-model="sendmail" >Send Mail</v-btn> -->
                <!-- <v-btn color="primary" @click="sendEmail">Send Email</v-btn>
              </v-col> -->

              <!-- <v-col cols="6"> -->
                <!-- <v-text-field v-model="mailFrom" label="Mail From" required></v-text-field>
                <v-text-field v-model="mailTo" label="Mail To" required></v-text-field> -->
                <!-- <v-select
                  v-model="mailTo"
                  label="Mail To"
                  :items="['xyz@company.com', 'zxc@company.com', 'qwerty@company.com']"
                  required
                ></v-select>
              </v-col> -->
  
              <!-- <v-col cols="6">
                <v-menu v-model="menu" :close-on-content-click="false" transition="scale-transition">
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="selectedDate"
                      label="Select Date"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="selectedDate" @input="menu = false"></v-date-picker>
                </v-menu>
              </v-col> -->
            <!-- </v-row>
            <v-conatiner>
            <h4>Stage 1 report</h4>
            <v-row>   
              <v-col cols="6">
                <v-text-field v-model="comment" label="Comment" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-menu 
                    v-model="menucomment" 
                    :close-on-content-click="false" 
                    transition="scale-transition"
                    >
                    <template v-slot:activator="{ props }">
                        <v-text-field
                            v-model="formattedSelectedCommentDate"
                            label="Select Date"
                            readonly
                            v-bind="props"
                        ></v-text-field>
                    </template> -->
                
                <!-- <v-date-picker 
                    v-model="selectedDate"
                    @update:modelValue="updateDate"
                ></v-date-picker> -->
                    <!-- <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeCommentDate" hide-actions @click.native.stop elevation="24">
                        </v-date-picker>
                        </v-row>
                    </v-container> -->
                    <!-- <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeCommentDate" hide-actions @click.native.stop elevation="24" :show-adjacent-months="true" :view-mode="'year'" :min="'2022-01-01'" :max="'2030-12-31'">
                        </v-date-picker>
                        </v-row>
                    </v-container>
                </v-menu>
            </v-col>
            <v-col cols="6">
                <v-file-input label="Stage 1 Report Upload *" v-model="stage1Report" required></v-file-input>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="mailToReport" label="Mail To" required></v-text-field>
              </v-col>
              <v-col cols="12"> -->
                <!-- <v-btn v-model="sendmail" >Send Mail</v-btn> -->
                <!-- <v-btn color="primary" @click="sendEmailReport">Send Email</v-btn>
              </v-col>
            </v-row>
        </v-conatiner>
        <v-col cols="12">
                <v-btn type="submit" color="primary">Submit</v-btn>
                <v-btn type="submit" @click="proceedToStage2">
                  Proceed to Stage 2
                </v-btn>
        </v-col>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
  </template>
  
  <script>
  import axios from "axios";
  export default {
    props: {
        format: String
    },
    data() {
      return {
        organisationName: this.$route.query.org_name || "", // Get org name from query params
        auditNumber: this.$route.query.audit_number || "",
        scope: "",
        stage1Plan: null,
        mailFrom: "tech@kvqaindia.com",
        mailTo: "",
        // selectedDate: "",
        menu: false,
        selectedDate: null,
        selectedCommentDate: null,
        menucomment: false,
        stage1Report: null,
        comment: "",
        additionaldata: null,
        mailToReport: ""
      };
    },

  //   computed: {
  //   selectedDate() {
  //     if (!this.selectedDate) return "";
  //     return new Intl.DateTimeFormat("en-GB", {
  //       day: "2-digit",
  //       month: "short",
  //       year: "numeric",
  //     }).format(new Date(this.selectedDate));
  //   },

  //   selectedCommentDate() {
  //     if (!this.selectedCommentDate) return "";
  //     return new Intl.DateTimeFormat("en-GB", {
  //       day: "2-digit",
  //       month: "short",
  //       year: "numeric",
  //     }).format(new Date(this.selectedCommentDate));
  //   },
  // },

  computed: {
  formattedSelectedDate() {
    if (!this.selectedDate) return "";
    return new Intl.DateTimeFormat("en-GB", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    }).format(new Date(this.selectedDate));
  },

  formattedSelectedCommentDate() {
    if (!this.selectedCommentDate) return "";
    return new Intl.DateTimeFormat("en-GB", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    }).format(new Date(this.selectedCommentDate));
  }
},

  mounted() {
    this.fetchStage1Data();
  },
    methods: {
    //   submitStage1() {
    //     console.log("Stage 1 Data Submitted:", {
    //       organisationName: this.organisationName,
    //       scope: this.scope,
    //       stage1Plan: this.stage1Plan,
    //       mailFrom: this.mailFrom,
    //       mailTo: this.mailTo,
    //       selectedDate: this.selectedDate,
    //       selectedCommentDate: this.selectedCommentDate,
    //       stage1Report: this.stage1Report,
    //       comment: this.comment
    //     });
    //     this.$router.push({
    //       path: "/stage2form",
    //       query: {
    //         orgName: this.organisationName
    //       }
    //     });
  
    //     // Navigate to Stage 2 form (extend this later)
    //     alert("Stage 1 submitted! Redirecting to Stage 2...");
    //   },


    // async submitStage1() {
    //     if (!this.scope || !this.stage1Plan || !this.mailFrom || !this.mailTo || !this.selectedDate) {
    //         alert("Please fill in all required fields!");
    //         return;
    //     }

    //     let formData = new FormData();
    //     formData.append("organisationName", this.organisationName);
    //     formData.append("scope", this.scope);
    //     formData.append("stage1Plan", this.stage1Plan);
    //     formData.append("mailFrom", this.mailFrom);
    //     formData.append("mailTo", this.mailTo);
    //     formData.append("selectedDate", this.selectedDate);
    //     formData.append("selectedCommentDate", this.selectedCommentDate);
    //     formData.append("stage1Report", this.stage1Report);
    //     formData.append("comment", this.comment);

    //     try {
    //         const response = await axios.post("http://127.0.0.1:5000/stage1", formData, {
    //             headers: { "Content-Type": "multipart/form-data" },
    //     });

    //     alert(response.data.message);
    //     this.$router.push({
    //         path: "/stage2form",
    //         query: { orgName: this.organisationName }
    //     });

    //     } catch (error) {
    //         console.error("Error submitting Stage 1:", error.response ? error.response.data : error.message);
    //         alert("Failed to submit Stage 1 form.");
    //     }
    // },

    async submitStage1() {
    if (!this.scope || !this.stage1Plan || !this.mailTo || !this.selectedDate) {
        alert("Please fill in all required fields!");
        return;
    }

    let formData = new FormData();
    formData.append("auditNumber", this.auditNumber);
    formData.append("organisationName", this.organisationName);
    formData.append("scope", this.scope);
    formData.append("stage1Plan", this.stage1Plan);
    formData.append("mailFrom", this.mailFrom);
    formData.append("mailTo", this.mailTo);
    formData.append("selectedDate", this.selectedDate);
    formData.append("selectedCommentDate", this.selectedCommentDate);
    formData.append("stage1Report", this.stage1Report);
    formData.append("comment", this.comment);

    // Get the JWT token from local storage or Vuex store
    const token = localStorage.getItem("token"); // Adjust if using Vuex

    try {
        const response = await axios.post("http://127.0.0.1:5000/stage1", formData, {
        // const response = await axios.post("http://127.0.0.1:5000/stage1", formData, {
            headers: { 
                "Content-Type": "multipart/form-data",
                "Authorization": `Bearer ${token}` // Attach JWT token
            },
        });

        alert(response.data.message);
        return true;
        // this.$router.push({
        //     path: "/application",
        // });

    } catch (error) {
        console.error("Error submitting Stage 1:", error.response ? error.response.data : error.message);
        alert("Failed to submit Stage 1 form.");
    }
},


      updateDate() {
        this.selectedDate = date
        
      },

      changeRoleDate(date) {
            this.selectedDate = date
            this.menu = false
        },

        changeCommentDate(date) {
            this.selectedCommentDate = date
            this.menucomment = false
        },

        async sendEmail() {
            if (!this.mailTo || !this.stage1Plan || !this.additionaldata) {
                alert("Please fill in all required fields and upload the necessary files!");
                return;
            }

            console.log("Mail Button is clicked!")

            let emailData = new FormData();
            emailData.append("mailTo", this.mailTo);
            emailData.append("subject", "Stage 1 Plan Submission");
            emailData.append("body", "Please find attached the Stage 1 Plan and Additional Data.");
            emailData.append("attachments", this.stage1Plan);
            emailData.append("attachments", this.additionaldata);

            try {
                // const response = await axios.post("http://127.0.0.1:5000/send-email", emailData, {
                const response = await axios.post("http://127.0.0.1:5000/send-email", emailData, {
                    headers: { "Content-Type": "multipart/form-data" },
                });

                alert(response.data.message);
            } catch (error) {
                console.error("Error sending email:", error.response ? error.response.data : error.message);
                alert("Failed to send email.");
            }
        },

        async sendEmailReport() {
    if (!this.mailToReport || !this.stage1Report) {
        alert("Please enter the recipient email and upload the Stage 1 Report!");
        return;
    }

    console.log("Send Report Email button clicked!");

    let reportEmailData = new FormData();
    reportEmailData.append("mailTo", this.mailToReport);
    reportEmailData.append("subject", "Stage 1 Report Submission");
    reportEmailData.append("body", "Please find attached the Stage 1 Report.");
    reportEmailData.append("attachments", this.stage1Report);

    try {
        // const response = await axios.post("http://127.0.0.1:5000/send-email", reportEmailData, {
        const response = await axios.post("http://127.0.0.1:5000/send-email", reportEmailData, {
            headers: { "Content-Type": "multipart/form-data" },
        });

        alert(response.data.message);
    } catch (error) {
        console.error("Error sending report email:", error.response ? error.response.data : error.message);
        alert("Failed to send report email.");
    }
},

async fetchStage1Data() {
    const orgName = this.$route.query.org_name;
    if (!orgName) {
        // No org_name provided, treat as new entry
        return;
    }

    const token = localStorage.getItem("token"); // Assuming token is stored in localStorage
    if (!token) {
        console.error("No authentication token found.");
        alert("You must be logged in to fetch data.");
        return;
    }

    try {
        // const response = await axios.get(`http://127.0.0.1:5000/stage1-data?org_name=${orgName}`, {
        const response = await axios.get(`http://127.0.0.1:5000/stage1-data?org_name=${orgName}`, {
            headers: {
                Authorization: `Bearer ${token}`
            },
            validateStatus: () => true // Avoid treating 404 as an error
        });

        if (response.status === 401) {
            console.error("Unauthorized: Invalid or expired token.");
            alert("Session expired. Please log in again.");
            return;
        }

        if (response.status === 404) {
            console.log("No existing data found. Displaying empty form.");
            this.organisationName = orgName;
            this.scope = "";
            this.selectedDate = "";
            this.comment = "";
            this.mailTo = "";
            this.mailToReport = "";
            return;
        }

        // Populate form with received data
        this.organisationName = response.data.organisationName || orgName;
        this.scope = response.data.scope || "";
        this.selectedDate = response.data.selectedDate || "";
        this.comment = response.data.comment || "";
        this.mailTo = response.data.mailTo || "";
        this.mailToReport = response.data.mailToReport || "";
    } catch (error) {
        console.error("Error fetching Stage 1 data:", error);
        alert("An error occurred while fetching data.");
    }
},


goBack() {
    this.$router.push('/application');
  },

  async proceedToStage2() {
    const isSubmitted = await this.submitStage1(); // First, save the form
    if (isSubmitted) {
    this.$router.push({
            path: "/stage2form",
            query: { orgName: this.organisationName }
        });
      }
    }

    // selectedDate() {
    //     if (!this.date) return null;
    //         let format = this.format || "%Y-%m-%d";
    //         format = format.replace('%Y', this.date.getYear() + 1900)
    //             .replace('%m', (this.date.getMonth() + 1 + "").padStart(2, "0"))
    //             .replace('%d', (this.date.getDate() + "").padStart(2, "0"));
    //         return format;
    //     }
    }
  };
  </script>
   -->


<template>
  <v-app>
    <v-container>
      <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to dashboard User!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
        <v-btn color="primary" @click="goBack">Cancel</v-btn>
      </v-app-bar>
    </v-container>

    <v-container>
      <v-card class="pa-5 mt-3 mx-auto" max-width="800">
        <v-card-title
          class="white--text"
          style="background-color:#A00;padding:10px;"
        >
          Stage 1 Form
        </v-card-title>

        <v-card-text>
          <v-form @submit.prevent="submitStage1">
            <v-row>
              <v-col cols="6">
                <v-text-field
                  v-model="organisationName"
                  label="Organisation Name"
                  disabled
                />
              </v-col>

              <v-col cols="6">
                <v-text-field
                  v-model="auditNumber"
                  label="Audit Number"
                  disabled
                />
              </v-col>

              <v-col cols="6">
                <v-text-field v-model="scope" label="Scope" />
              </v-col>

              <!-- EXISTING FILE -->
              <v-col cols="6">
                <div v-if="stage1PlanFile" class="text-caption mb-1">
                  Uploaded: <strong>{{ stage1PlanFile }}</strong>
                </div>
                <v-file-input
                  label="Stage 1 Plan Upload"
                  v-model="stage1Plan"
                />
              </v-col>

              <v-col cols="6">
                <v-text-field v-model="mailTo" label="Mail To" />
              </v-col>

              <!-- DATE PICKER -->
              <v-col cols="6">
                <v-menu v-model="menu" :close-on-content-click="false">
                  <template v-slot:activator="{ props }">
                    <v-text-field
                      v-bind="props"
                      label="Select Date"
                      v-model="formattedSelectedDate"
                      readonly
                    />
                  </template>

                  <v-date-picker
                    v-model="selectedDate"
                    view-mode="year"
                    scrollable
                    @update:model-value="menu = false"
                  />
                </v-menu>
              </v-col>

              <v-col cols="12">
                <v-btn color="primary" @click="sendStage1Mail">
                  Save Stage 1 Plan
                </v-btn>
              </v-col>
            </v-row>

            <v-divider class="my-4"></v-divider>

            <h4>Stage 1 Report</h4>

            <v-row>
              <v-col cols="6">
                <v-text-field v-model="comment" label="Comment" />
              </v-col>

              <v-col cols="6">
                <v-menu v-model="menucomment" :close-on-content-click="false">
                  <template v-slot:activator="{ props }">
                    <v-text-field
                      v-bind="props"
                      label="Comment Date"
                      v-model="formattedSelectedCommentDate"
                      readonly
                    />
                  </template>

                  <v-date-picker
                    v-model="selectedCommentDate"
                    view-mode="year"
                    scrollable
                    @update:model-value="menucomment = false"
                  />
                </v-menu>
              </v-col>


              <v-col cols="6">
                <div v-if="stage1ReportFile" class="text-caption mb-1">
                  Uploaded: <strong>{{ stage1ReportFile }}</strong>
                </div>
                <v-file-input
                  label="Stage 1 Report Upload"
                  v-model="stage1Report"
                />
              </v-col>

              <v-col cols="6">
                <v-text-field v-model="mailToReport" label="Mail To" />
              </v-col>

              <v-col cols="12">
                <v-btn color="primary" @click="sendStage1Mail">
                  Save Stage 1 Report
                </v-btn>
              </v-col>
            </v-row>

            <v-col cols="12" class="mt-4">
              <!-- <v-btn type="submit" color="primary">Submit</v-btn> -->
              <v-btn class="ml-3" @click="proceedToStage2">
                Proceed to Stage 2
              </v-btn>
            </v-col>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      auditNumber: "",
      organisationName: "",
      scope: "",
      stage1Plan: null,
      stage1Report: null,
      stage1PlanFile: null,
      stage1ReportFile: null,
      mailFrom: "tech@kvqaindia.com",
      mailTo: "",
      mailToReport: "",
      selectedDate: null,
      selectedCommentDate: null,
      comment: "",
      menu: false,
      menucomment: false,
    };
  },

  computed: {
    formattedSelectedDate() {
      return this.selectedDate
        ? new Date(this.selectedDate).toLocaleDateString("en-GB")
        : "";
    },
    formattedSelectedCommentDate() {
      return this.selectedCommentDate
        ? new Date(this.selectedCommentDate).toLocaleDateString("en-GB")
        : "";
    },
  },


  mounted() {
    this.auditNumber =
      this.$route.query.audit_number ||
      localStorage.getItem("audit_number");

    if (!this.auditNumber) {
      alert("Audit number missing!");
      return;
    }

    localStorage.setItem("audit_number", this.auditNumber);
    this.organisationName = this.$route.query.org_name || "";
    this.fetchStage1Data();
  },

  methods: {
    buildFormData() {
      const fd = new FormData();
      fd.append("audit_number", this.auditNumber);
      fd.append("organisation_name", this.organisationName);
      fd.append("scope", this.scope);
      fd.append("mail_from", this.mailFrom);
      fd.append("mail_to", this.mailTo);
      fd.append("mail_to_report", this.mailToReport);
      fd.append("selected_date", this.selectedDate || "");
      fd.append("selected_comment_date", this.selectedCommentDate || "");
      fd.append("comment", this.comment || "");

      if (this.stage1Plan) fd.append("stage1_plan", this.stage1Plan);
      if (this.stage1Report) fd.append("stage1_report", this.stage1Report);

      return fd;
    },

    async sendStage1Mail() {
      const token = localStorage.getItem("token");
      await axios.post(
        "http://127.0.0.1:5000/stage1",
        this.buildFormData(),
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert("Stage 1 data saved");
    },

    async submitStage1() {
      await this.sendStage1Mail();
      alert("Stage 1 submitted");
    },

    // async fetchStage1Data() {
    //   const token = localStorage.getItem("token");
    //   const res = await axios
    //     .get(
    //       `http://127.0.0.1:5000/stage1-data?audit_number=${this.auditNumber}`,
    //       { headers: { Authorization: `Bearer ${token}` } }
    //     )
    //     .catch(() => null);

    //   if (!res || !res.data) return;

    //   this.scope = res.data.scope || "";
    //   this.mailTo = res.data.mailTo || "";
    //   this.mailToReport = res.data.mailToReport || "";
    //   this.comment = res.data.comment || "";
    //   this.selectedDate = res.data.selectedDate || null;
    //   this.selectedCommentDate = res.data.selectedCommentDate || null;
    //   this.stage1PlanFile = res.data.stage1PlanFile || null;
    //   this.stage1ReportFile = res.data.stage1ReportFile || null;
    // },

    async fetchStage1Data() {
      const token = localStorage.getItem("token");
      const res = await axios
        .get(
          `http://127.0.0.1:5000/stage1-data?audit_number=${this.auditNumber}`,
          { headers: { Authorization: `Bearer ${token}` } }
        )
        .catch(() => null);

      if (!res || !res.data) return;

      this.scope = res.data.scope || "";
      this.mailTo = res.data.mailTo || "";
      this.mailToReport = res.data.mailToReport || "";
      this.comment = res.data.comment || "";

      // Convert backend date strings to Date objects
      this.selectedDate = res.data.selectedDate
        ? new Date(res.data.selectedDate)
        : null;
      this.selectedCommentDate = res.data.selectedCommentDate
        ? new Date(res.data.selectedCommentDate)
        : null;

      this.stage1PlanFile = res.data.stage1PlanFile || null;
      this.stage1ReportFile = res.data.stage1ReportFile || null;
    },

    goBack() {
      this.$router.push("/application");
    },

    proceedToStage2() {
      this.$router.push({
        path: "/stage2form",
        query: { audit_number: this.auditNumber },
      });
    },

    logout() {
      localStorage.clear();
      this.$router.push("/");
    },
  },
};
</script>
