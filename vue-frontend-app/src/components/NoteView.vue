<template>
  <div style="margin-top: 100px">
    <h3>{{ title }}</h3>
    <p>{{ body }}</p>
    Tags:
    <span
      class="badge badge-primary"
      style="background-color: gray"
      v-for="tag in tags"
      :key="tag"
      >{{ tag }}</span
    >
  </div>
</template>
<script>
import userService from "@/services/user.service";

export default {
  name: "NoteView",
  data() {
    return {
      title: "",
      body: "",
      tags: [],
    };
  },
  created() {
    if (this.$route.params && this.$route.params.key) {
      this.fetchNote(this.$route.params.key);
    }
  },
  methods: {
    fetchNote(noteId) {
      userService.fetchNote(noteId).then((res) => {
        console.log(res);
        if (res && res.data) {
          let data = res.data;
          this.title = data.title;
          this.body = data.body;
          this.tags = data.tags;
        }
      });
    },
  },
};
</script>
