import React from 'react';

const Sidebar = () => {

    return (
        <div className="col-md-4">
            <div className="content-section">
                <h3>Our Sidebar</h3>
                <p className='text-muted'>You can put any information here you'd like.
                <ul className="list-group">
                    <li className="list-group-item list-group-item-light">Latest Posts</li>
                    <li className="list-group-item list-group-item-light">Announcements</li>
                    <li className="list-group-item list-group-item-light">Calendars</li>
                    <li className="list-group-item list-group-item-light">etc</li>
                </ul>
                </p>
            </div>
        </div>
    )
};

export default Sidebar;