import Main  from "./Student/index";
import { Routes, Route } from "react-router-dom";
import Peer from "./Student/components/Peer";
import Self from "./Student/components/Self";
import Calender from "./Student/components/Calender";
import Classwork from "./Student/components/Classwork";
import Quizzes from "./Student/components/Quizzes";

function App() {
  return (
    <div className="App">
 <Routes>
              <Route path="/Student" element={<Main />} />
            
              <Route path="/classwork" element={<Classwork />} />
              <Route path="/calender" element={<Calender />} />
              <Route path="/quiz" element={<Quizzes />} />
              <Route path="/self" element={<Self />} />
              <Route path="/peer" element={<Peer />} />
           
            
            </Routes>
    </div>
  );
}

export default App;
