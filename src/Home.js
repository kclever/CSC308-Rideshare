import React, { Component } from 'react';
import { Tabs, Icon, Button, Menu, Dropdown, Card, Input, Checkbox } from 'antd';
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
      <Button>
        <Icon type = "user"/>
      </Button>
      </Dropdown>);
    const { TabPane } = Tabs;
    const { Search } = Input;
    const { TextArea } = Input;

    function onChange(e) {
      console.log(`checked = ${e.target.checked}`);
    }
    
    return (
      <div className="header">
        <p>CALPOLYRIDES</p>
      <div className="padding">
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
              <Input placeholder="Name" className="sizing"></Input>
              <Input placeholder="Cost" className="sizing"></Input>
              <Input placeholder="To" className="sizing"></Input>
              <Input placeholder="From" className="sizing"></Input>
              <br />
              <Input placeholder="Seats Available" className="sizing"></Input>
              <br />
              <TextArea rows={4} placeholder="Extra Details" className="sizing"/>
              <Checkbox onChange={onChange}>Drop off along the way</Checkbox>
              <br />
              <br />
              <br />
              <br />
              <br />
              <Button className="but">
                Create Post
              </Button>
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />
              <br />

            </TabPane>
            <TabPane
              tab={
                <span>
                  <Icon type="team"/>
                  Riders
                </span>
              }
              key="2"
            >
              <span>
              <Search
                placeholder="Search!"
                onSearch={value => console.log(value)}
                className="search"
              />
              <Button className="but">
                Create Post
              </Button>
              <br />
              <br />
              <Card title="San Francisco to SLO" extra={<Icon type="user"/>}>
                    <p>Friday 3/3 @ 4:00PM</p>
                    <p>$20</p>
                    <p> 4 spots left <Icon type="user"/>
                    <Icon type="user"/>
                    <Icon type="user"/>
                    <Icon type="user"/></p>
                </Card>
                <br />
                <br />
                <Card title="Los Angeles to SLO" extra={<Icon type="user"/>}>
                    <p>Saturday 3/4 @ 7:00AM</p>
                    <p>$20</p>
                    <p> 1 spot left <Icon type="user"/>
                    <Icon type="user"/></p>
                </Card>
                <br />
                <br />
                <Card title="SLO to Alaska" extra={<Icon type="user"/>}>
                    <p> 3/17 @ 1:00PM</p>
                    <p>$2000</p>
                    <p> 3 spots left <Icon type="user"/>
                    <Icon type="user"/>
                    <Icon type="user"/></p>
                </Card>
              </span>
            </TabPane>
          </Tabs>
      </div>
      </div>
    );
  }
}

export default Home;