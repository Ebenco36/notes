<template>
    <div id="register">
        <section class="vh-100" style="background-color: #9A616D;">
            <div class="container py-5 h-100">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col col-xl-6">
                        <div class="card">
                            <div class="card-body col-md-12 p-4 p-lg-5 text-black">
                                <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign Up</h5>
                                <Form @submit="handleRegister" :validation-schema="schema">
                                    <div class="col-md-12 col-lg-12">
                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="first_name">First Name</label>
                                            <Field type="text" id="first_name" name="first_name" class="form-control form-control-lg" />
                                            <ErrorMessage name="first_name" class="error-feedback" />
                                        </div>

                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="last_name">Last Name</label>
                                            <Field type="text" id="last_name" name="last_name" class="form-control form-control-lg" />
                                            <ErrorMessage name="last_name" class="error-feedback" />
                                        </div>

                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="username">Username</label>
                                            <Field type="text" id="username" name="username" class="form-control form-control-lg" />
                                            <ErrorMessage name="username" class="error-feedback" />
                                        </div>
                                    </div>
                                    <div class="col-md-12 col-lg-12 align-items-center">
                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="email">Email address</label>
                                            <Field type="email" id="email" name="email" class="form-control form-control-lg" />
                                            <ErrorMessage name="email" class="error-feedback" />
                                        </div>

                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="password">Password</label>
                                            <Field type="password" name="password" id="password" class="form-control form-control-lg" />
                                            <ErrorMessage name="password" class="error-feedback" />
                                        </div>

                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="confirm_password">Confirm Password</label>
                                            <Field type="password" name="confirm_password" id="confirm_password" class="form-control form-control-lg" />
                                            <ErrorMessage name="confirm_password" class="error-feedback" />
                                        </div>
                                    </div>

                                    <div class="col-md-12 mb-4 align-items-center">
                                        <button class="btn btn-dark btn-lg btn-block" type="submit">Register</button>
                                        <br />
                                        <a class="small text-muted" href="#!">Forgot password?</a>
                                        <p class="mb-5 pb-lg-2" style="color: #393f81;">I have an account?
                                            <router-link to="/login">
                                                Login here
                                            </router-link>
                                        </p>
                                        <a href="#!" class="small text-muted">Terms of use.</a>
                                        <a href="#!" class="small text-muted">Privacy policy</a>
                                    </div>
                                </Form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";

export default {
  name: "Login_Page",
  components: {
    Form,
    Field,
    ErrorMessage,
  },
  data() {
    const schema = yup.object().shape({
        first_name: yup.string().required("First name is required!"),
        last_name: yup.string().required("Last name is required!"),
        username: yup.string().required("username is required!"),
        email: yup.string().email().required("Email is required!"),
        password: yup.string().min(8).required("Password is required!"),
        confirm_password: yup.string().min(8).required("Password is required!")
        .oneOf([yup.ref('password')], 'Passwords do not match'),
    });

    return {
      loading: false,
      message: "",
      schema,
    };
  },
  computed: {
  },
  created() {
  },
  methods: {
    handleRegister(user) {
      this.loading = true;
      this.$store.dispatch("auth/register", user).then(
        () => {
          this.$router.push("/login");
        },
        (error) => {
          this.loading = false;
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        },
      );
    },
  },
};
</script>
