const { useState } = React;

export const ColorPicker = () => {
  const [color, setColor] = useState("#ffffff");
  function handleChange(e) {
    setColor(e.target.value);
  }
  return (
    <div
      id="color-picker-container"
      style={{
        backgroundColor: color,
      }}
    >
      <input
        type="color"
        id="color-input"
        onChange={handleChange}
        value={color}
      />
    </div>
  );
};
