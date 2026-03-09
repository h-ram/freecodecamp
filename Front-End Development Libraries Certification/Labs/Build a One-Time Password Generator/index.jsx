const { useState, useEffect, useRef } = React;

export function OTPGenerator() {
  const [otp, setOtp] = useState(null);
  const [timeLeft, setTimeLeft] = useState(0);

  function generateOTP() {
    const newOtp = Math.floor(100000 + Math.random() * 900000);
    setOtp(newOtp);
    setTimeLeft(5);
  }

  useEffect(() => {
    if (timeLeft <= 0) return;

    const timer = setInterval(() => {
      setTimeLeft((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft]);

  let displayText = "Click 'Generate OTP' to get a code";
  if (otp && timeLeft > 0) displayText = otp;

  let timerText = "";
  if (timeLeft > 0) {
    timerText = `Expires in: ${timeLeft} seconds`;
  } else if (otp && timeLeft === 0) {
    timerText = "OTP expired. Click the button to generate a new OTP.";
  }

  return (
    <div className="container">
      <h1 id="otp-title">OTP Generator</h1>

      <h2 id="otp-display">{displayText}</h2>

      <p id="otp-timer" aria-live="polite">
        {timerText}
      </p>

      <button
        id="generate-otp-button"
        onClick={generateOTP}
        disabled={timeLeft > 0}
      >
        Generate OTP
      </button>
    </div>
  );
}
