import { createApp } from "vue";
import App from "./App.vue";
import { router } from "./router";
import "vfonts/Lato.css"

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getStorage } from"firebase/storage";
import mitt from 'mitt';

// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBUCWyfUdd_K2cUqpMsKgiADQJmJsfufBE",
  authDomain: "sixdegreestest2-f5666.firebaseapp.com",
  databaseURL: "https://sixdegreestest2-f5666.firebaseio.com",
  projectId: "sixdegreestest2-f5666",
  storageBucket: "sixdegreestest2-f5666.appspot.com",
  messagingSenderId: "586073468667",
  appId: "1:586073468667:web:17d01f8792783c94a9ca5e",
  measurementId: "G-BPNJC56MDK"
};

// Initialize Firebase
const app = createApp(App);

const firebase_app = initializeApp(firebaseConfig);
const analytics = getAnalytics(firebase_app);
const storage = getStorage(firebase_app);

app.use(router);

app.mount("#app");
