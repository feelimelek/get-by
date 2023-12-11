import React from "react";
import { shallow } from "enzyme";
import YellowButton from "./YellowButton";

describe("YellowButton", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<YellowButton />);
    expect(wrapper).toMatchSnapshot();
  });
});
