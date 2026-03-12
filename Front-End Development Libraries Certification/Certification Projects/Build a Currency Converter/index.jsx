const { useState, useMemo } = React;

const RATES = {
  USD: 1,
  EUR: 0.92,
  GBP: 0.78,
  JPY: 156.7
};

export function CurrencyConverter() {
  const [currency, setCurrency] = useState({
    source: "USD",
    destination: "EUR"
  })
  const [amount, setAmount] = useState(1);

  const amountInUSD = useMemo(() => {
    const numericAmount = Number(amount) || 0;
    return numericAmount / RATES[currency.source];
  }, [amount, currency.source]);

  const convertedAmount = (amountInUSD * RATES[currency.destination]).toFixed(2);

  function handleInput(event){
    setAmount(event.target.value)
  }
  function handleSelect(event){
    const {name, value} = event.target
    setCurrency((prev) => ({ ...prev, [name]: value }))
  }
  return (
    <form id="converter-form">
    <h1>Currency Converter</h1>
    <input 
      type="number" 
      min="0"
      value={amount} 
      onChange={handleInput}/>
    <select name="source" value={currency.source} onChange={handleSelect}>
      <option>USD</option>
      <option>EUR</option>
      <option>GBP</option>
      <option>JPY</option>
    </select>
    <select name="destination" value={currency.destination} onChange={handleSelect}>
      <option>USD</option>
      <option>EUR</option>
      <option>GBP</option>
      <option>JPY</option>
    </select>
    <p id="result">Converted Amount: <span>{convertedAmount} {currency.destination}</span></p>
    </form>)
  ;
}