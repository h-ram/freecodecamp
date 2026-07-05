function migrateRecord(defaultRecord, record) {
  let result = { ...record };

  for (let key in defaultRecord) {
    if (!(key in result)) {
      result[key] = defaultRecord[key];
    }
  }

  return result;
}

console.log(migrateRecord({ username: "", posts: 0 }, { verified: true }));
console.log(
  migrateRecord({ username: "", posts: 0 }, { username: "camper", posts: 5 }),
);
console.log(
  migrateRecord(
    { username: "", posts: 0, verified: false },
    { username: "camper" },
  ),
);
console.log(
  migrateRecord(
    { username: "", posts: 0 },
    { username: "camper", role: "admin" },
  ),
);
console.log(
  migrateRecord(
    {
      username: "",
      email: "",
      posts: 0,
      verified: false,
      role: "user",
      banned: false,
    },
    {
      username: "camper",
      email: "camper@freecodecamp.org",
      role: "admin",
    },
  ),
);
