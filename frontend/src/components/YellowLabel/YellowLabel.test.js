import React from "react";
import { shallow } from "enzyme";
import YellowLabel from "./YellowLabel";

describe("YellowLabel", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<YellowLabel />);
    expect(wrapper).toMatchSnapshot();
  });
});
