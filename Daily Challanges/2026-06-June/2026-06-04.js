function isValidSchema(obj) {
  const roles = new Set(["user", "creator", "moderator", "staff", "admin"]);

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

  return true;
}

console.log(
  isValidSchema({
    username: "vivian",
    posts: 1,
    verified: false,
    role: "user",
    supporter: true,
  }),
);

console.log(
  isValidSchema({
    username: "rudolph",
    posts: 15,
    verified: true,
    role: "creator",
  }),
);

console.log(
  isValidSchema({
    username: "julia",
    posts: 50,
    verified: true,
    role: "admin",
    supporter: "true",
  }),
);
