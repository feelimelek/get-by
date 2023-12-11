import React from "react"
import { StyleSheet, Text, View, TouchableHighlight } from "react-native"

export default function YellowButton({handlePressButton}) {

  return (
    <TouchableHighlight
      activeOpacity={0.6}
      underlayColor="#rgba(194,139,23,0.3)"
      onPress={handlePressButton}
      style={styles.YellowButtonTouchable}>
        <View style={styles.YellowButtonView}>
          <Text style={styles.YellowButtonText}>Dar dica</Text>
      </View>
    </TouchableHighlight>
  )
}

const styles = StyleSheet.create({
  YellowButtonTouchable: {
    width: "fit-content",
    borderRadius: 50,
  },
  YellowButtonView: {
    display: "flex",
    width: "fit-content",
    height: "10vh",
    paddingLeft: 16,
    paddingRight: 17,
    paddingTop: 13,
    paddingBottom: 14,
    borderWidth: 1,
    borderColor: "rgba(194,139,23,1)",
    borderRadius: 50,
    boxSizing: "border-box",
    backgroundColor: "rgba(255, 255, 255, 0)",
  },
  YellowButtonText: {
    display: "flex",
    justifyContent: "center",
    color: "rgba(194,139,23,1)",
    fontSize: "19px",
    lineHeight: "20px",
    fontFamily: "K2D, sans-serif",
    fontWeight: "800",
    textAlign: "center",
    width: "fit-content"
  },
})
