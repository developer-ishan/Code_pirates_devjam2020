import React, {Component} from 'react';
import QrReader from 'react-qr-reader'

class App extends Component {
  state = {
    result: 'No result',
    regno: '',
    name: '',
    roomNo: '',
    imgUrl: '',
    Toload: false
  }
 
  handleScan = data => {
    if (data) {
      this.setState({
        result: data
      })
      var compo = this.state.result
      var values = compo.split(";")
      this.setState({regno: values[0], name: values[1], roomNo: values[2], imgUrl: `http://localhost:8000/${values[3]}`, Toload:true})   
      fetch(`http://localhost:8000/api/tick-status/${this.state.regno}/true`,
      {
        method : 'GET'
      }).then((res) => {
        return res.json()
      })
    }
  }

  createOrDelete = () => {
    fetch(`http://localhost:8000/api/entry/${this.state.regno}/`,
    {method: 'POST',
    headers: {
     'Content-Type': 'application/json',
     'Authorization': 'application/json'
    }  
    }).then((res) => {
      return res.json()
    })
    window.location.reload(false)
  }

  showList = () => {
    fetch('http://localhost:8000/api/list',
    {
      method: 'GET'
    }).then((res) => {
      return res.json()
    }).then(data => {
      console.log(data)
    })
  }

  handleError = err => {
    console.error(err)
  }
  render() {
    return (
      <div style={{'display': 'flex'}}>
        <div style={{'width':'50%'}}>
        <QrReader
          delay={100}
          onError={this.handleError}
          onScan={this.handleScan}
          style={{ width: '50vw', 'height':'100%'}}
        />
        </div>
        <div style={{'display':'flex','flexDirection':'column', 'width': '50%','justifyContent':'center','alignItems':'center'}}>
        {
          this.state.Toload && (
        <div style={{'fontSize': '20px', 'paddingLeft':'18vw'}}>
        <p><b>Registraion No. : </b>{this.state.regno}</p>
        <p><b>Name : </b>{this.state.name}</p>
        <p><b>Room No. : </b>{this.state.roomNo}</p>
        <img src={this.state.imgUrl} alt='Server Error!!' style={{'height':'60%', 'width':'60%'}} /><br />
        <p>Plzz Verify The Above Profile!</p>
        <button style={{'padding': '6px 20px', 'fontSize': '20px', 'background':'green', 'color':'#fff'}} onClick={this.createOrDelete}>Entry Register</button>
        </div>
          )}
        <button style={{'width':'25%','display':'inline','padding': '6px 20px', 'fontSize': '20px', 'background':'blue', 'color':'#fff'}} onClick={this.showList}>Open Entries</button>
        </div>
      </div>
    )
  }
}

export default App