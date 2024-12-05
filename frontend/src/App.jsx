import { useState, useEffect } from "react";
import { BsArrowRight } from "react-icons/bs";

import "./App.css";

function App() {
    const url = "http://127.0.0.1:5000/";

    const [currencys, setCurrencys] = useState([]);
    const [currency1, setCurrency1] = useState("BRL");
    const [currency2, setCurrency2] = useState("USD");
    const [filterCurrency1, setFilterCurrecy1] = useState([]);
    const [filterCurrency2, setFilterCurrecy2] = useState([]);
    const [myValue, setMyValue] = useState(1);
    const [res, setRes] = useState({});
    const valueElement = document.querySelector("#value");

    // console.log(valueElement.value.length);

    const getCurrencys = async (endpoint, set) => {
        const response = await fetch(url + endpoint);
        const data = await response.json();
        set(data);
    };

    const handleSubmit = async (e, set) => {
        const newValue = e.target.value;

        if (e.target.name == "value" && (newValue === "" || isNaN(newValue)))
            return;

        set(newValue);

        const obj = {
            currency1: e.target.name === "currency1" ? newValue : currency1,
            currency2: e.target.name === "currency2" ? newValue : currency2,
            value: e.target.name === "value" ? newValue : myValue,
        };

        try {
            const response = await fetch(url + "convert", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(obj),
            });

            const data = await response.json();
            setRes(data);
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        setFilterCurrecy1(
            currencys.filter((currency) => currency.code !== currency2)
        );
        setFilterCurrecy2(
            currencys.filter((currency) => currency.code !== currency1)
        );
    }, [currencys, currency1, currency2]);

    useEffect(() => {
        getCurrencys("currencys", setCurrencys);
        getCurrencys("brlusd", setRes);
    }, []);

    return (
        <div className="app">
            <div className="container">
                <h1>Conversor de Moeda</h1>
                <form>
                    <div className="form-group">
                        <div className="form-control">
                            <select
                                name="currency1"
                                id="currency1"
                                value={currency1}
                                onChange={(e) => handleSubmit(e, setCurrency1)}>
                                {filterCurrency1 &&
                                    filterCurrency1.map((currency) => (
                                        <option
                                            value={currency.code}
                                            key={currency.code}>
                                            {currency.code} ({currency.name})
                                        </option>
                                    ))}
                            </select>
                        </div>
                        <div className="icon">
                            <BsArrowRight />
                        </div>
                        <div className="form-control">
                            <select
                                name="currency2"
                                id="currency2"
                                value={currency2}
                                onChange={(e) => handleSubmit(e, setCurrency2)}>
                                {filterCurrency2 &&
                                    filterCurrency2.map((currency) => (
                                        <option
                                            value={currency.code}
                                            key={currency.code}>
                                            {currency.code} ({currency.name})
                                        </option>
                                    ))}
                            </select>
                        </div>
                    </div>
                    <div className="row">
                        <label htmlFor="value">Valor a converter:</label>
                        <input
                            type="number"
                            name="value"
                            id="value"
                            value={myValue}
                            onChange={(e) => handleSubmit(e, setMyValue)}
                        />
                    </div>
                </form>
                <div className="result">
                    <div className="label">Cotação:</div>
                    <div className="quote">
                        {res.quote && res.quote.toFixed(2)}
                    </div>
                    <div className="label">Valor Convertido:</div>
                    <div className="convert-value">
                        {res.value_converting &&
                            res.value_converting.toFixed(2)}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default App;
