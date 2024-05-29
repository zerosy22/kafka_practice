import logo from './logo.svg';
import './App.css';
import {Paper} from "@material-ui/core";
import AddToDo from "./AddSignup";
import Axios from "axios";


function App() {
  // 데이터 추가를 위한 함수
  const add = (user) => {
    console.log("user : ", user);
    Axios.post("http://127.0.0.1:8000/cqrs/signup/", user).then((response) => {
      console.log(response.data)
      if (response.data.bid) {
        alert("저장에 성공했습니다.")
      } else {
        alert("코멘트를 저장하지 못했습니다.");
      }
    });
};

  return (
    <div className="App">
      <Paper style={{ margin: 16 }}>
        <AddSignup add = {add}/>
      </Paper>
    </div>
  );

  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //     </header>
  //   </div>
  // );
}

export default App;
