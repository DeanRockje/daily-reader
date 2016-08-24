/**
 * Created by creepy on 24/08/16.
 */

import React from 'react';

class FeedItems extends React.Component{
    constructor(props){
        super(props);
        this.state={
          feed_items:[]
        };
    }

    loadData(URL){
        var component = this;
        $.ajax({
            type:"GET",
            dataTypes:"json",
            url:URL,
            success(data){
                this.setState({feed_items:data})
            }
        })
    }

    componentDidMount(){
        this.loadData("http://localhost:8000/api/feeds/");
    }

    componentWillUnmount(){
        this.serverRequest.abort();
    }

    render(){
        return(

            <div className="wrapper">
                <FeedItems feeds = {this.state.feed_items}/>
            </div>
        )
    }
}


class FeedItem extends React.Component{
    constructor(props){
        super(props);
        var feeds = props;
    }

    render(){

        {this.props.feeds.map((feed, index)=>
            <div className="feed">
                <p className="feed__title" key = {index}>{feed.title}</p>
                <p className="feed__pubDate">{JSON.parse(feed.publication_date)}</p>
                <strong>Articles:{feed.entries.length}</strong>
            </div>
        )}
    }
}