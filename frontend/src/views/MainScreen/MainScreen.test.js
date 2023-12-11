import React from "react";
import { shallow } from "enzyme";
import MainScreen from "./MainScreen";

describe("MainScreen", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<MainScreen />);
    expect(wrapper).toMatchSnapshot();
  });
});
