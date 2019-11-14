import React, { Component } from 'react';
import { Card, Icon } from 'antd';

class Rider extends Component {

    render() {
        return (
            <div>
                <Card title="San Francisco to SLO" extra={<Icon type="user"/>} style={{ width: 1500 }}>
                    <p>Date: 3/3</p>
                    <p>Card content</p>
                    <p>Card content</p>
                </Card>
            </div>
        );
    }

}

export default Rider;