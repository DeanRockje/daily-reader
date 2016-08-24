"use strict";

Object.defineProperty(exports, "__esModule", {
    value: true
});

var _react = require("react");

var _react2 = _interopRequireDefault(_react);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var CategoryItem = _react2.default.createClass({
    displayName: "CategoryItem",

    render: function render() {
        var data = this.props.data;
        {

            return _react2.default.createElement(
                "div",
                { className: "item" },
                _react2.default.createElement(
                    "p",
                    { className: "title" },
                    item.category_title
                ),
                _react2.default.createElement(
                    "p",
                    { className: "feeds" },
                    item.feeds
                )
            );
        }
    }

}); /**
     * Created by creepy on 22/08/16.
     */

exports.default = CategoryItem;

//# sourceMappingURL=Item-compiled.js.map