import React from "react";


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.rep_url}</td>
            <td>{item.users}</td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Rep_url</th>
                <th>Users</th>
            </tr>
            {items.map((item) => <ProjectItem item={item}/>)}
        </table>
    )
}

export default ProjectList