import React, { Component } from 'react';
import { Tabs, Icon, Button, Menu, Dropdown, Card } from 'antd';
import './Home.css';

class Home extends Component {
  render() {
    const menu = (
      <Menu className="theme">
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="http://www.alipay.com/">
            Profile
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="http://www.taobao.com/">
            Settings
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="http://www.tmall.com/">
            Help
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="http://www.tmall.com/">
            Sign Out
          </a>
        </Menu.Item>
      </Menu>
    );
    const profileButton = (<Dropdown overlay = {menu}>
      <Button>
        <Icon type = "user"/>
      </Button>
      </Dropdown>);
    const { TabPane } = Tabs;
    

    return (
      <div>
        <Tabs tabBarExtraContent={profileButton} defaultActiveKey="2" type="card">
            <TabPane
              tab={
                <span>
                  <Icon type="car" />
                  Drivers
                </span>
              }
              key="1"
            >
              Driver page
            </TabPane>
            <TabPane
              tab={
                <span>
                  <Icon type="team" />
                  Riders
                </span>
              }
              key="2"
            >
              <span>
              <Card title="San Francisco to SLO" extra={<Icon type="user"/>} style={{ width: 1650 }}>
                    <p>Friday 3/3 @ 4:00PM</p>
                    <p>$20</p>
                    <p> 4 spots left <Icon type="user"/>
                    <Icon type="user"/>
                    <Icon type="user"/>
                    <Icon type="user"/></p>
                </Card>
              </span>
            </TabPane>
          </Tabs>
      </div>
    );
  }
}

export default Home;