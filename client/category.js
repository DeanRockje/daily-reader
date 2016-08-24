/**
 * Created by creepy on 21/08/16.
 */


import React from 'react';
import CategoryItem from './item';
import $ from 'jquery';

var Category = React.createClass({

    getInitialState:function () {
        return {
            categories: []

        };
    },

    loadData:function (URL) {
        var component = this;
        $.ajax({
            type:"GET",
            dataTypes:'json',
            url:URL,
            success:function (data) {
                component.setState({categories:data}).bind(this,'json');
            },
        })
    },

    componentDidMount:function () {
        this.loadData("http://localhost:8000/api/category");
    },

    componentWillUnmount:function () {
        this.request.abort();
    },

    render:function(){
      return(
        <div className="Category">
            <p className="category_list">Categories</p>
            <ul>
                {this.state.categories.map((category, index) =>
                <li className="category__item" key = {index}>
                    <CategoryItem data = {category}/>
                </li>
                )}
            </ul>

        </div>
      );
    }
});

export default Category;