import React from "react";
import { shallow } from "enzyme";
import LoginIcon from "./LoginIcon";

describe("LoginIcon", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<LoginIcon />);
    expect(wrapper).toMatchSnapshot();
  });
});
