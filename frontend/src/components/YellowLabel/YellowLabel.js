import React from "react"
import { StyleSheet, Text, View } from "react-native"

export default function YellowLabel() {
  return (
    <View style={styles.YellowLabelView}>
      <Text style={styles.YellowLabelText}>O que você quer fazer?</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  YellowLabelView: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "flex-start",
    alignItems: "flex-start",
    paddingRight: 2,
    paddingTop: 7,
    paddingBottom: 7,
    boxSizing: "border-box",
  },
  YellowLabelText: {
    color: "rgba(194,139,23,1)",
    fontSize: "20px",
    lineHeight: "48px",
    fontFamily: "K2D, sans-serif",
    fontWeight: "800",
  },
})

