import React from "react";
import { shallow } from "enzyme";
import PurpleButton from "./PurpleButton";

describe("PurpleButton", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<PurpleButton />);
    expect(wrapper).toMatchSnapshot();
  });
});
