import axios from 'axios';

const API_URL = process.env.VUE_APP_APP_URL + "api/auth/";

class AuthService {
  login(user) {
    let request = axios
      .post(API_URL + 'login/', {
        email: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data) {
          localStorage.setItem('user', JSON.stringify(response.data.data));
        }

        return response.data;
      });
      
    return request
  }

  logout() {
    localStorage.removeItem('user');
    return axios.post(API_URL + 'logout/', {});
  }

  register(user) {
    return axios.post(API_URL + 'register/', user);
  }
}

export default new AuthService();