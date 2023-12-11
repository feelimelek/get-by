import React from "react";
import { StyleSheet, View } from "react-native"
import Logo from "../../components/Logo/Logo";
import YellowLabel from "../../components/YellowLabel/YellowLabel";
import PurpleButton from "../../components/PurpleButton/PurpleButton";
import YellowButton from "../../components/YellowButton/YellowButton"
import LoginIcon from "../../components/LoginIcon/LoginIcon"; 

 const MainScreen = (navigation) => {

  const handlePressPurpleButton = () => {
    alert('Purple Button Pressed!')
  }
  const handlePressYellowButton = () => {
    alert('Yellow Button Pressed!')
  }

  return (
    <>
      <View style={styles.view}>
        <LoginIcon/>
        <Logo/>
        <YellowLabel/>
        <PurpleButton handlePressButton={handlePressPurpleButton}/>
        <YellowButton handlePressButton={handlePressYellowButton}/>
      </View>
    </>
  );
};

export default MainScreen;

const styles = StyleSheet.create({
  view: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
  },
})
