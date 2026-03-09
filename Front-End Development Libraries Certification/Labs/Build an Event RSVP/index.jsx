const { useState } = React;

export function EventRSVPForm() {
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    attendeeCount: "",
    dietaryPreferences: "",
    hasAdditionalGuests: false,
  });
  const [submitStatus, setSubmitStatus] = useState(false);

  const {
    fullName,
    email,
    attendeeCount,
    dietaryPreferences,
    hasAdditionalGuests,
  } = formData;

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;
    setFormData((previous) => ({
      ...previous,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  function handleSubmit(event) {
    event.preventDefault();
    setSubmitStatus(true);
  }
  return (
    <div className="container">
      <form id="rsvp-form" onSubmit={handleSubmit}>
        <label>
          Full Name:
          <input
            type="text"
            name="fullName"
            value={fullName}
            onChange={handleChange}
            placeholder="Aagon Targaryen"
            required
          />
        </label>

        <label>
          Email:
          <input
            type="email"
            name="email"
            value={email}
            onChange={handleChange}
            placeholder="aagon@targaryen.got"
            required
          />
        </label>

        <label>
          Number of attendees:
          <input
            type="number"
            name="attendeeCount"
            value={attendeeCount}
            onChange={handleChange}
            placeholder="Between 1 and 8"
            required
            min="1"
            max="8"
          />
        </label>

        <label>
          Dietary Preferences (Optional):
          <input
            type="text"
            name="dietaryPreferences"
            value={dietaryPreferences}
            onChange={handleChange}
            placeholder="No Gluten, No lactose, ...etc"
          />
        </label>

        <label>
          Bringing Additional Guests?
          <input
            type="checkbox"
            name="hasAdditionalGuests"
            checked={hasAdditionalGuests}
            onChange={handleChange}
          />
        </label>

        <button type="submit">Send</button>
      </form>
      {submitStatus && (
        <div id="status-msg">
          <h2>RSVP Submitted!</h2>
          <dl>
            <dt>Name:</dt>
            <dd>{fullName}</dd>
            <dt>Email:</dt>
            <dd>{email}</dd>
            <dt>Attendees:</dt>
            <dd>{attendeeCount}</dd>
            <dt>Dietary:</dt>
            <dd>{dietaryPreferences || "None"}</dd>
            <dt>Additional Guests:</dt>
            <dd>{hasAdditionalGuests ? "Yes" : "No"}</dd>
          </dl>
        </div>
      )}
    </div>
  );
}
