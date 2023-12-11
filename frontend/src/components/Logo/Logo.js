import React from "react";
import {StyleSheet, Image } from 'react-native';

const Logo = () => {
  return <Image source={require('../../assets/img/Logo.jpg')} style={styles.Logo}/> 
};

export default Logo;

const styles = StyleSheet.create({
  Logo: {
    width: 188,
    height: 101,
  },
})
