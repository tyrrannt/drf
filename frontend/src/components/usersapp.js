import React from 'react'


const UsersItem = ({customuser}) => {
   return (
       <tr>
           <td>
               {customuser.username}
           </td>
           <td>
               {customuser.first_name}
           </td>
           <td>
               {customuser.last_name}
           </td>
           <td>
               {customuser.surname}
           </td>
           <td>
               {customuser.email}
           </td>
       </tr>
   )
}
const UsersList = ({customusers}) => {
   return (
       <table>
           <th>
               User name
           </th>
           <th>
               First name
           </th>
           <th>
               Last Name
           </th>
           <th>
               Surname
           </th>
           <th>
               email
           </th>
           {customusers.map((customuser) => <UsersItem customuser={customuser} />)}
       </table>
   )
}


export default UsersList