function isValidSchema(obj) {
  const roles = new Set(["user", "creator", "moderator", "staff", "admin"]);
  const required = ["username", "posts", "verified", "role", "badges"];

  if (!required.every((key) => key in obj)) {
    return false;
  }

  if (typeof obj.username !== "string") {
    return false;
  }

  if (typeof obj.posts !== "number") {
    return false;
  }

  if (typeof obj.verified !== "boolean") {
    return false;
  }

  if (!roles.has(obj.role)) {
    return false;
  }

  if ("supporter" in obj && typeof obj.supporter !== "boolean") {
    return false;
  }

  if (!Array.isArray(obj.badges)) {
    return false;
  }

  if (!obj.badges.every((badge) => typeof badge === "string")) {
    return false;
  }

  return true;
}

console.log(
  isValidSchema({
    username: "gill",
    posts: 12,
    verified: false,
    role: "creator",
    supporter: false,
    badges: ["early-adopter", "popular"],
  }),
);
console.log(
  isValidSchema({
    username: "tonya",
    posts: 299,
    verified: true,
    role: "moderator",
    supporter: true,
    badges: ["streak-master", "veteran"],
    followers: 1233,
  }),
);
console.log(
  isValidSchema({
    username: "zara",
    posts: 0,
    verified: false,
    role: "user",
    supporter: false,
    badges: [],
  }),
);
console.log(
  isValidSchema({
    username: "nicole",
    posts: 65,
    verified: true,
    role: "admin",
    supporter: false,
    badges: ["first-post", 18],
  }),
);
console.log(
  isValidSchema({
    username: "tim",
    posts: 25,
    verified: true,
    role: "staff",
    supporter: false,
  }),
);
console.log(
  isValidSchema({
    username: "charlie",
    posts: 0,
    verified: false,
    role: "user",
    supporter: "no",
    badges: ["first-post", "anniversary"],
  }),
);
console.log(
  isValidSchema({
    username: "wanda",
    posts: 15,
    verified: true,
    role: "friend",
    supporter: true,
    badges: ["popular"],
  }),
);
console.log(
  isValidSchema({
    username: "guy",
    posts: 5,
    verified: "false",
    role: "staff",
    supporter: true,
    badges: ["helper"],
  }),
);
console.log(
  isValidSchema({
    username: "carrie",
    verified: true,
    role: "moderator",
    supporter: true,
    badges: ["helper", "sharer"],
  }),
);
console.log(
  isValidSchema({
    username: true,
    posts: 75,
    verified: true,
    role: "creator",
    supporter: true,
    badges: ["veteran"],
  }),
);
