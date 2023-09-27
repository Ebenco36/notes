import axios from 'axios';
import authHeader from './auth-header';

const API_URL = process.env.VUE_APP_APP_URL + "api/auth/";

class UserService {

  getUser() {
    return axios.get(API_URL + 'user/profile/', { headers: authHeader() });
  }

}

export default new UserService();