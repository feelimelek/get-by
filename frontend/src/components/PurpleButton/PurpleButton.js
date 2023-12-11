import React from "react"
import { StyleSheet, Text, View, TouchableHighlight } from "react-native"

export default function PurpleButton({handlePressButton}) {

  return (
    <TouchableHighlight
      activeOpacity={0.6}
      underlayColor="rgba(75,0,130,0.3)"
      onPress={handlePressButton}
      style={styles.PurpleButtonTouchable}>
        <View style={styles.PurpleButtonView}>
          <Text style={styles.PurpleButtonText}>Procurar dica</Text>
      </View>
    </TouchableHighlight>
  )
}

const styles = StyleSheet.create({
  PurpleButtonTouchable: {
    width: "60vw",
    borderRadius: 50,
  },
  PurpleButtonView: {
    display: "flex",
    width: "60vw",
    height: "10vh",
    paddingLeft: 16,
    paddingRight: 17,
    paddingTop: 13,
    paddingBottom: 14,
    marginTop: 20,
    marginBottom: 20,
    borderWidth: 1,
    borderColor: "rgba(75,0,130,1)",
    borderRadius: 50,
    boxSizing: "border-box",
    backgroundColor: "rgba(255, 255, 255, 0)",
  },
  PurpleButtonText: {
    display: "flex",
    justifyContent: "center",
    color: "rgba(75,0,130,1)",
    fontSize: "19px",
    lineHeight: "20px",
    fontFamily: "K2D, sans-serif",
    fontWeight: "800",
    textAlign: "center",
    width: "fill-container"
  },
})
