import contents_1 from '../data/contents_1';
import contents_2 from '../data/contents_2';
import contents_3 from '../data/contents_3';
import React from 'react';

const Home = () =>{

    function ContentCard(props){
        return(
            <div className="contents_{n}">
                <a href={props.cnt.link}><img src={props.cnt.picture}/></a>
            </div>
        );
    }
    
    return(
    
    <div>
        <section id="main">
            <div className="contents_1">
                {
                contents_1.map((a,i,n)=>{
                    return <ContentCard cnt={contents_1[i]} i={i} key={i} n={1}/>
                })
                }
            </div>

            <div className="contents_2">
                {
                contents_2.map((a,i,n)=>{
                    return <ContentCard cnt={contents_2[i]} i={i} key={i} n={2}/>
                })
                }
            </div>

            <div className="contents_3">
                {
                contents_3.map((a,i,n)=>{
                    return <ContentCard cnt={contents_3[i]} i={i} key={i} n={3}/>
                })
                }
            </div>
        </section>
    </div>
    );
};

export default Home;