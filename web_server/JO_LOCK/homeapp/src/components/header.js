import React,{useState} from 'react' 

export function Header()
{

    let [header1,h1Change]=useState(['Login','Logout','MyPage']);
    let [header2,h2Change]=useState(['Door','Windows','Light','Speaker','humidifier']);
    let [header3,h3Change]=useState(['알림','설정']);

    return(

    <section id="header">

      <h1 className="Name"><a className="Name" href="/">JI</a></h1>

        
        <nav className="header_content1">
          <ul>
          {
            header1.map((a)=>{
              return <li><a href={a}>{a}</a></li>
            })
          }
          </ul>
        </nav>
  
        <nav className="header_content2">
          <ul>
          {
            header2.map((a)=>{
              return <li><a href={a}>{a}</a></li>
            })
          }
          </ul>
        </nav>

        <nav className="header_content3">
          <ul>
          {
            header3.map((a)=>{
              return <li><a href={a}>{a}</a></li>
            })
          }
          </ul>
        </nav>
        
    </section>
    )
}