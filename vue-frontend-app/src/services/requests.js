import axios from 'axios';
import authHeader from './auth-header';

class Requests{

    get(url, params) {
        let request = axios.get(url, { params: params, headers: authHeader() })
        .catch((error) => {
            // Handle network error
            if (error.response) {
            // The request was made, but the server responded with a status code outside the range of 2xx
            console.error('Server Error:', error.response.data);
            } else if (error.request) {
            // The request was made, but no response was received (e.g., no internet connection)
            console.error('No Response from Server');
            } else {
            // Something happened in setting up the request that triggered the error
            console.error('Request Error:', error.message);
            }
        });

        return request
    }

    post (url, data) {
        let request = axios
        .post(url, data, { headers: authHeader() })
        .then(response => {
            return response.data;
        }).catch((error) => {
            // Handle network error
            if (error.response) {
            // The request was made, but the server responded with a status code outside the range of 2xx
            console.error('Server Error:', error.response.data);
            } else if (error.request) {
            // The request was made, but no response was received (e.g., no internet connection)
            console.error('No Response from Server');
            } else {
            // Something happened in setting up the request that triggered the error
            console.error('Request Error:', error);
            }
        });
        
        return request
    }

    patch (url, data) {
        let request = axios
        .patch(url, data, { headers: authHeader() })
        .then(response => {
            return response.data;
        }).catch((error) => {
            // Handle network error
            if (error.response) {
            // The request was made, but the server responded with a status code outside the range of 2xx
            console.error('Server Error:', error.response.data);
            } else if (error.request) {
            // The request was made, but no response was received (e.g., no internet connection)
            console.error('No Response from Server');
            } else {
            // Something happened in setting up the request that triggered the error
            console.error('Request Error:', error);
            }
        });
        
        return request
    }
}

export default new Requests();