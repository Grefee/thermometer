import "./Teplomer.css"
import React, {useState, useEffect} from 'react';
import { type } from "@testing-library/user-event/dist/type";

function Teplomer(props){
  const [value, setValue] = useState([]);
  const [date, setDate] = useState([]);
  const [query, seQuery] = useState('');
  const [intervalID, setIntervalID] = useState(0);

  const minT = props.minT;
  const maxT = props.maxT;


  async function  getData() {
    let response = await fetch(
      `http://172.23.30.216:3001/value/${props.hidenName}`,
    );
    const x = await response.json();
    setValue(x[0].teplota_value)

    setDate(x[0].teplota_cas)
    
    }

console.log(minT,maxT)
console.log(typeof(minT))
console.log(value)
console.log(typeof(value))
useEffect(() => {
  getData();

  const interval = setInterval(()=>{
    getData()
  },10000)
  return()=>clearInterval(interval)
}, []);

    return (
      <div className="teplomer">
        <table>
            <tr>
                <th>{props.name}</th>

            </tr>
            <tr>
              ({props.hidenName})
            </tr>
            <tr>
                 {
/*                 (() => {
                  if({value} >0 ){
                    <td className="val">Teplota: {value} °C</td>
                  } else {
                    <td className="valError">Teplota: {value} °C</td>
                  
                  }})() */

                  minT < value && value < maxT
                  ? 
                  <td className="val">Teplota: {value} °C</td>
                  : <td className="valError">Teplota: {value} °C</td>

              } 
                

            </tr>
            <tr>
                <td className="green">Optimum: {props.minT} - {props.maxT}°C</td>

            </tr>
            <tr>
                <td>Datum: {date}</td>

            </tr>
        </table>

      </div>
    );
    }
  
  export default Teplomer;