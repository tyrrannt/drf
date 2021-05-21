import axios from 'axios'
import React from 'react';
import logo from './logo.svg';
import './App.css';
import UsersList from './components/usersapp.js'


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'customusers': []
       }
   }

   // componentDidMount() {
   //     const customusers = [
   //         {
   //             'first_name': 'Фёдор',
   //             'last_name': 'Достоевский',
   //             'surname': '1821',
   //         },
   //         {
   //             'first_name': 'Александр',
   //             'last_name': 'Грин',
   //             'surname': '1880',
   //         },
   //     ]
   //     this.setState(
   //         {
   //             'customusers': customusers
   //         }
   //     )
   // }
   componentDidMount() {
   axios.get('http://localhost:8000/api/usersapp')
       .then(response => {
           const customusers = response.data
               this.setState(
               {
                   'customusers': customusers
               }
           )
       }).catch(error => console.log(error))
   }

   render () {
       return (
           <div>
               <UsersList customusers={this.state.customusers} />
           </div>
       )
   }
}
export default App;