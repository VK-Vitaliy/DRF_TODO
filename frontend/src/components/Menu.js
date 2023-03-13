import {Link} from "react-router-dom";

function Menu() {
    return (
        <div className="Menu">
            <ul>
                <li>
                    <Link to='/'>Users</Link>
                </li>
                <li>
                    <Link to='/projects/'>Projects</Link>
                </li>
                <li>
                    <Link to='/notes/'>Notes</Link>
                </li>

            </ul>

        </div>
    );

}

export default Menu