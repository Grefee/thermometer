import React, {useState, useEffect} from 'react';
import './App.css';
import Teplomer from './Teplomer';
import Vlhkomer from './Vlhkomer';

function App() {
  return (
    <div className="App">
        <div className='container'>
          <div className='div0'>
            <h1>Teplomery Sklad</h1>
          </div>    
          <div className='div1'>
            <Teplomer name="Příjem zboží" hidenName="TCZLIB302" minT={18} maxT={30} />
            <Teplomer name="Rampy" hidenName="TCZLIB301" minT={18} maxT={30} />
            <Teplomer name="Regál A chemie 2,5 m" hidenName="TCZLIB304" minT={18} maxT={30} />
            <Teplomer name="Průjezd na Encapsulaci" hidenName="TCZLIB306" minT={18} maxT={30} />
            <Teplomer name="Regál A chemie 1,5 m" hidenName="TCZLIB307" minT={18} maxT={30} />
            <Teplomer name="Přebalování / Kytování" hidenName="TCZLIB308" minT={18} maxT={30} />
            <Teplomer name="Lednice A" hidenName="TCZLIB309" minT={2} maxT={8} />
            <Teplomer name="Regál J Glass" hidenName="TCZLIB310" minT={18} maxT={30} />
            <Teplomer name="Kontejner Hořlavin" hidenName="TCZLIB315" last="True" minT={5} maxT={25} />
            <Teplomer name="Schenker" hidenName="TCZLIB312" minT={5} maxT={30} />
            <Teplomer name="Lednice B" hidenName="TCZLIB313" minT={2} maxT={8} />
            <Teplomer name="Halla A1" hidenName="TCZLIB305" minT={20} maxT={30} />
            <Teplomer name="Halla A2" hidenName="TCZLIB314" minT={20} maxT={30} />
            <Vlhkomer name="FG" hidenName="TCZLIB303" minT={18} maxT={30} minV={40.00} maxV={99} />
          </div>
        </div>
    </div>
  );
}

export default App;
