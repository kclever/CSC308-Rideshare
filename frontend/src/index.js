import React from 'react';
import ReactDOM from 'react-dom';

class CalPolyRides extends React.Component
{
    constructor()
    {
        super();
        this.state = {
            'items': []
        }
    }
    componentDidMount()
    {
        this.getItems();
    }

    getItems()
    {
        fetch('http://localhost:8000/api/item/')
            .then(results => results.json())
            .then(results => this.setState({'items': results}));
    } 
    render()
    {
        return ( 
            <ul>
                {this.state.items.map(function(item, index)
                    {
                        return (
                            <div>
                                <h1>{item.from_u} -> {item.to_u}</h1>
                                <p>{item.extra_details_u}</p>
                            </div>    
                            )
                    }

                    )}
                
            </ul> 
        );
    }
}

ReactDOM.render(<CalPolyRides />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
