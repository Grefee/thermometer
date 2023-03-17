import "./Vlhkomer.css"
import React, {useState, useEffect} from 'react';

function Vlhkomer(props){
  const [valueV, setValueV] = useState([]);
  const [date, setDate] = useState([]);
  const [valueT, setValueT] = useState([]);
  const [query, seQuery] = useState('');
  const [intervalID, setIntervalID] = useState(0);


  const minT = props.minT;
  const maxT = props.maxT;

  const minV = props.minV;
  const maxV = props.maxV;
  const IP = process.env.REACT_APP_BACKEND_API

  async function  getData() {
    let response = await fetch(
      `http://${IP}:3001/value/${props.hidenName}`,
    );
    const x = await response.json();
    setValueT(x[0].teplota_value)  
    setDate(x[0].teplota_cas)
    let response2 = await fetch(
      `http://${IP}:3001/valueV/${props.hidenName}`,
    );
    const x2 = await response2.json();
    console.log(x2[0])
    setValueV(x2[0].vlhkost_value)
    }


useEffect(() => {
  getData();
  const interval = setInterval(()=>{
    getData()
  },10000)
  return()=>clearInterval(interval)
}, []);

    return (
      <div className="vlhkomer">
        <table>
            <tr>
                <th>{props.name}   <a>  ({props.hidenName})</a></th>

            </tr>
            <tr>
                {
                minT < valueT && valueT < maxT
                  ? 
                  <td className="val">Teplota: {valueT} °C</td>
                  : <td className="valError">Teplota: {valueT} °C</td>
                } 
            </tr>
            <tr>
                {
                minV < valueV && valueV < maxV
                  ? 
                  <td className="val">Vlhkost: {valueV} %</td>
                  : <td className="valError">Vlhkost: {valueV} %</td>
                 }
            </tr>
            <tr>
                <td className="green">Optimum: {props.minT} - {props.maxT}°C</td>
            </tr>
            <tr>
                <td className="green">Optimum: {props.minV} - {props.maxV}%</td>
            </tr>
            <tr>
                <td>Datum: {date}</td>
            </tr>
        </table>
      </div>
    );
    }
  export default Vlhkomer;
