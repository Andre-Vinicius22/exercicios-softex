import React from "react";
import { Link } from "react-router-dom";
import './style.css'

function Header() {
    return(
        <div>
            <nav className="header">
                <ul className="link">
                    <li><Link to='/' style={{ textDecoration: 'none', color: '#fff' }}>Home</Link></li>
                    <li><Link to='/about' style={{ textDecoration: 'none', color: '#fff' }}>About</Link></li>
                </ul>
            </nav>
        </div>
    )
}

export default Header;