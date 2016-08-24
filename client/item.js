/**
 * Created by creepy on 23/08/16.
 */

import React from 'react';



var FeedsByCategory = React.createClass({
   render:function () {
       var feeds = this.props.feeds;
       return(
        <ul>
            {this.props.feeds.map((feed, index)=>
                <li key = {index}>{feed}</li>
            )}

        </ul>
       )
   }
});



var CategoryItem = React.createClass({


    getInitialState:function () {
       return {
           visible:false
    };
    },

    onClick:function () {
      this.setState({visible:!this.state.visible});
    },

    render:function () {
        var data = this.props.data;
        {
        return (
            <div id="categories">
            <p onClick={this.onClick}>{this.props.data.category_title}</p>
                {this.state.visible ? <FeedsByCategory feeds = {this.props.data['feeds']}/>:null}
            </div>


        )
    }
    }

});

export default CategoryItem;