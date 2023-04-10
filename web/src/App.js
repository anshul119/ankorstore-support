import React, { useState } from 'react';
import axios from 'axios';
import "./App.css";

function InputOutputComponent() {
  const [inputValue, setInputValue] = useState('');
  const [outputValue, setOutputValue] = useState('');
  const [err, setErr] = useState(false);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleButtonClick = async event => {
    event.preventDefault();
    if(!inputValue) return;
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/ask', { query: inputValue } );
      if (err) {
        setErr(false);
      }
      setOutputValue(response.data)
    } catch (error) {
      setErr(true)
      setOutputValue("Oops! Something went wrong.")
      console.error(error);
    }
  };

  return (
    <div className="wrapper content">
      <h1 className="has-text-centered">Welcome to Ankorstore Integration support <span role="img">🤓 🛠️</span></h1>
      <form className="form" onSubmit={handleButtonClick}>
        <label className="label">How can I help?</label>
        <div className="field is-grouped">  
          <div className="control">
            <input className="input" type="text" value={inputValue} onChange={handleInputChange} />
          </div>
          <div className="control">
            <button className="button is-primary">Ask</button>
          </div>
        </div>
      </form>
      {outputValue &&
        <article className={`result message ${err ? "is-danger" : "is-dark"}`}>
          <div className="message-body">
            {outputValue}
          </div>
        </article>
      }
    </div>
  );
}

export default InputOutputComponent;