function isValidSchema(obj) {
  return (
    typeof obj === "object" &&
    obj !== null &&
    typeof obj.username === "string" &&
    typeof obj.posts === "number" &&
    typeof obj.verified === "boolean" &&
    ["user", "creator", "moderator", "staff", "admin"].includes(obj.role)
  );
}

console.log(
  isValidSchema({
    username: "henry",
    posts: 0,
    verified: true,
    role: "staff",
  }),
);

console.log(
  isValidSchema({
    username: "sara",
    posts: 45,
    verified: false,
    role: "creator",
    followers: 70,
  }),
);
