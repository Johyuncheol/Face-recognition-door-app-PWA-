import React from 'react';

const data= {
    finos:{
        name : '조현철',
        description: '작성자'  
    },

    cho3703: {
        name : '확인용',
        description : '확인용'
    }
};

const Profile =({match})=>{
    const {username} = match.params;
    const profile = data[username];
    
    if(!profile){
        return <div>존재하지않는 사용자입니다 </div>
    }

    return(
        <div>
            <h3>
                {username}({profile.name})
            </h3>
            <p>{profile.description}</p>
        </div>
    );

};

export default Profile;