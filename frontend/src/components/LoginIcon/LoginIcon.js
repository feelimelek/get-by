import React from "react";
import { TouchableOpacity, StyleSheet } from "react-native"
import Icon from '@mdi/react';
import { mdiLogin } from '@mdi/js';
import "./LoginIcon.css"

const LoginIcon = () => {
  const handleLoginIconPress = () => {
    alert("login!")
  }

  return (
    <TouchableOpacity
    activeOpacity={0.6}
    underlayColor="rgba(75,0,130,0.3)"
    onPress={handleLoginIconPress}
    style={styles.iconButton}>  
      <Icon
        path={mdiLogin}
        title="Login"
        className="icon"
      />
    </TouchableOpacity>
  )
}

export default LoginIcon;

const styles = StyleSheet.create({
  iconButton: {
    backgroundColor: "#ffffff",
    height: '18%',
    width: '9%',
    cursor: 'pointer'
  },
})