import React from "react";


const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.text}</td>
            <td>{item.created_at}</td>
            <td>{item.project}</td>
            <td>{item.user}</td>
        </tr>
    )
}

const ToDoList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>Text</th>
                <th>Created at</th>
                <th>Project</th>
                <th>User</th>
            </tr>
            {items.map((item) => < ToDoItem item={item}/>)}
        </table>
    )
}

export default ToDoList