export function MoodBoardItem({ color, image, description }) {
  const boardStyle = {
    backgroundColor: color,
  };
  return (
    <div className="mood-board-item" style={boardStyle}>
      <img className="mood-board-image" src={image} />
      <h3 className="mood-board-text">{description}</h3>
    </div>
  );
}

export function MoodBoard() {
  const moodBoardItems = [
    {
      id: "dest-1",
      color: "#a2d2ff",
      image: "https://cdn.freecodecamp.org/curriculum/labs/santorini.jpg",
      description: "Serene Santorini Skies",
    },
    {
      id: "dest-2",
      color: "#efefd0",
      image: "https://cdn.freecodecamp.org/curriculum/labs/shore.jpg",
      description: "Golden Shoreline Retreat",
    },
    {
      id: "dest-3",
      color: "#d4e09b",
      image: "https://cdn.freecodecamp.org/curriculum/labs/grass.jpg",
      description: "Lush Valley Meadows",
    },
    {
      id: "dest-4",
      color: "#f4a261",
      image: "https://cdn.freecodecamp.org/curriculum/labs/pathway.jpg",
      description: "Rustic Autumn Pathway",
    },
    {
      id: "dest-5",
      color: "#2a9d8f",
      image: "https://cdn.freecodecamp.org/curriculum/labs/ship.jpg",
      description: "Deep Sea Expeditions",
    },
    {
      id: "dest-6",
      color: "#ccd5ae",
      image: "https://cdn.freecodecamp.org/curriculum/labs/pigeon.jpg",
      description: "Peaceful Urban Nature",
    },
  ];
  return (
    <div>
      <h1 className="mood-board-heading">Destination Mood Board</h1>
      <div className="mood-board">
        {moodBoardItems.map((item) => (
          <MoodBoardItem
            key={item.id}
            color={item.color}
            image={item.image}
            description={item.description}
          />
        ))}
      </div>
    </div>
  );
}
