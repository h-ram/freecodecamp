function mongoIdToDate(id) {
  const timestamp = parseInt(id.slice(0, 8), 16);
  const d = new Date(timestamp * 1000);
  return d.toISOString();
}

console.log(mongoIdToDate("6a094b50bcf86cd799439011"));
