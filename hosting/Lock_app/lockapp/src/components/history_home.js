import React,{Component} from 'react';

class history_home extends Component {
    handleGoBack = () =>{
        this.props.history.goBack();

    };

    handleGoForward = () =>{
        this.props.history.goForward();
    };

    componentDidMount(){
        //페이지에 변화가 생길때마다 
        this.unblock=this.props.history.block("정말 떠나실건가요?");
    }

    componentWillUnmount(){
        //component가 unmount 되면 query 멈춤
        
        if(this.unblock){
            this.unblock();
        }
    }

    render(){
        return(
            <div>
                <button className='cnt_button' onClick={this.handleGoBack}>뒤</button>
                <button className='cnt_button' onClick={this.handleGoForward}>앞</button>
            </div>
        );
    }
}

export default history_home;