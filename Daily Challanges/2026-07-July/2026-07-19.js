function elevatorStops(currentFloor, requestedFloors) {
  const above = requestedFloors
    .filter((f) => f > currentFloor)
    .sort((a, b) => a - b);
  const below = requestedFloors
    .filter((f) => f < currentFloor)
    .sort((a, b) => b - a);

  let upDistance;
  if (above.length === 0) {
    upDistance = currentFloor - below[below.length - 1];
  } else if (below.length === 0) {
    upDistance = above[above.length - 1] - currentFloor;
  } else {
    upDistance =
      above[above.length - 1] -
      currentFloor +
      (above[above.length - 1] - below[below.length - 1]);
  }

  let downDistance;
  if (below.length === 0) {
    downDistance = above[above.length - 1] - currentFloor;
  } else if (above.length === 0) {
    downDistance = currentFloor - below[below.length - 1];
  } else {
    downDistance =
      currentFloor -
      below[below.length - 1] +
      (above[above.length - 1] - below[below.length - 1]);
  }

  if (upDistance <= downDistance) {
    return above.concat(below);
  }

  return below.concat(above);
}

console.log(elevatorStops(5, [2, 8, 3, 9]));
console.log(elevatorStops(6, [2, 10, 8, 3, 1, 9]));
console.log(elevatorStops(1, [4, 8, 3, 6, 9]));
console.log(elevatorStops(12, [6, 10, 7, 3, 1, 4]));
console.log(elevatorStops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]));
