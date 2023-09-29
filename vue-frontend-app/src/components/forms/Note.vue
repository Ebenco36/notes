<template>
  <div class="post-form-container" style="margin-top: 100px">
    <h2>Create a Note</h2>
    <form @submit.prevent="createOrEditNote" class="post-form">
      <div class="form-group">
        <label for="postContent">Note title:</label>
        <input
          type="text"
          v-model="title"
          class="form-control mt-2"
          placeholder="note title"
        />
      </div>
      <div class="form-group">
        <label for="postContent">Note Body:</label>
        <textarea
          id="postContent"
          v-model="body"
          class="form-control"
          rows="4"
          required
        ></textarea>
      </div>
      <div class="form-group">
        <label for="newTag" title="add new tag if tag does not exist"
          >Add Tags:</label
        >
        <input
          type="text"
          id="newTag"
          v-model="newTag"
          @keydown.prevent.enter="addTag"
        />
        <br />
        <select
          style="width: 100%"
          id="tagList"
          v-model="selectedTags"
          multiple
        >
          <option v-for="tag in tagList" :key="tag.id" :value="tag.name">
            {{ tag.name }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label>Do you wish to add more ?</label>
        <div>
          <input
            type="radio"
            id="yes"
            name="addMore"
            value="yes"
            v-model="addMore"
          />
          <label for="yes">Yes</label><br />
          <input
            type="radio"
            id="no"
            name="addMore"
            value="no"
            v-model="addMore"
          />
          <label for="css">No</label><br />
        </div>
      </div>
      <span class="alert alert-info" v-if="message.length > 0">{{
        message
      }}</span>
      <br />
      <button type="submit" class="btn btn-primary">Create Note</button>
    </form>
  </div>
</template>

<script>
import userService from "@/services/user.service";

export default {
  name: "NoteForm",
  data() {
    return {
      title: "",
      body: "",
      tagList: [], // Replace with your tag list data
      selectedTags: [],
      newTag: "",
      addMore: "no",
      message: "",
    };
  },
  created() {
    this.getTags();
    // check if we are updating or creating.
    if (this.$route.params && this.$route.params.key) {
      this.fetchNote(this.$route.params.key);
    }
  },
  methods: {
    addTag() {
      if (this.newTag.trim() !== "") {
        this.tagList.push({
          id: this.tagList.length + 1,
          name: this.newTag.trim(),
        });
        this.newTag = "";
      }
    },
    fetchNote(noteId) {
      userService.fetchNote(noteId).then((res) => {
        console.log(res);
        if (res && res.data) {
          let data = res.data;
          this.title = data.title;
          this.body = data.body;
          this.selectedTags = data.tags;
        }
      });
    },
    getTags() {
      userService.getTags().then((res) => {
        console.log(res);
        this.tagList = res.data.data;
      });
    },
    createOrEditNote() {
      const note = {
        title: this.title,
        body: this.body,
        tags: this.selectedTags,
      };
      let connect = null;
      if (this.$route.params && this.$route.params.key) {
        connect = userService.editNote(note, this.$route.params.key);
      } else {
        connect = userService.createNote(note);
      }
      connect
        .then((response) => {
          if (this.addMore === "no") {
            this.$router.push("/");
          }
          this.message = "Note added successfully.";
        })
        .catch((error) => {
          // Check if it's a 401 Unauthorized error
          if (error.response && error.response.status === 401) {
            // Handle the 401 error here
            console.error(
              "Authentication failed. Redirect to login page or show an error message."
            );
          } else {
            // Handle other types of errors
            console.error("An error occurred:", error.message);
          }
        });
      // Send the post object to your backend or perform other actions
      if (!this.$route.params && !this.$route.params.key) {
        // Clear the form fields on create
        this.title = "";
        this.body = "";
        this.newTag = "";
      }
    },
  },
};
</script>

<style scoped>
.post-form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.post-form {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

/* Use Bootstrap classes for styling */
.btn-primary {
  background-color: #007bff;
  color: #fff;
}

/* Add more Bootstrap classes as needed */
</style>
