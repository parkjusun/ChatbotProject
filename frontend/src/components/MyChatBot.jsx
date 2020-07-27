import React, { Component } from 'react';
import axios from  'axios';
import ChatBot from 'react-simple-chatbot';

class CarSearch extends Component {
    constructor(props) {
        super(props);
        this.state = {
            search: '',
            result: [],
        };
    }

    componentWillMount() {
        const { steps } = this.props;
        this.state.search = steps.search.value;
        axios.get('http://localhost:5000/car/carSearch/'+ this.state.search)
            .then( response => {
                response.data.forEach(item => {this.state.result.push({
                    carName: item.carName,
                    employee: item.employee,
                    img: item.img
                })})
                console.log(this.state.result)
                alert('검색결과:'+this.state.result.length)
            } ) // SUCCESS
            .catch( response => { console.log(response); } ); // ERROR
    }

    render() {
        return (
            <div>
                {this.state.result.length}
            </div>
        );
    }
}

const ExampleDBPedia = () => (
    <ChatBot
        steps={[
            {
                id: '1',
                message: '자동차 이름을 입력하세요',
                trigger: 'search',
            },
            {
                id: 'search',
                user: true,
                trigger: '3',
            },
            {
                id: '3',
                component: <CarSearch/>,
                waitAction: true,
                trigger: '1',
            },
        ]}
    />
);

export default ExampleDBPedia;