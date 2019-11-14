import React, { Component } from 'react';
import { Tabs, Icon, Button, Menu, Dropdown } from 'antd';
import './Home.css';

class Home extends Component {
  render() {
    const menu = (
      <Menu>
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
      <Button
      ><Icon type = "user"/>
      </Button>
      </Dropdown>);
    const { TabPane } = Tabs;
    

    return (
      <div>
        <Tabs tabBarExtraContent={profileButton} defaultActiveKey="2">
            <TabPane
              tab={
                <span>
                  <Icon type="car" />
                  Drivers
                </span>
              }
              key="1"
            >
              yayayyaya
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
              Tab 2
            </TabPane>
          </Tabs>
      </div>
    );
  }
}

export default Home;