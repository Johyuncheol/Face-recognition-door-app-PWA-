import { Route, Link } from 'react-router-dom';
import Profile from './Profile';
import React from 'react';


const Profiles = ()=>{
    return(
        <div>
            <h3>사용자 목록</h3>
            <ul>
                <li>
                    <Link to ="/profiles/finos">finos</Link>
                </li>
                <li>
                    <Link to ="/profiles/cho3703">cho3703</Link>
                </li>
            </ul>

            <Route
                path="/profiles"
                exact
                render={()=><div>사용자를 선택해 주세요 </div>}
            />

            <Route path ="/profiles/:username" component={Profile} />

        </div>
    );
};

export default Profiles;