function isValidSchema(obj) {
  const roles = new Set(["user", "creator", "moderator", "staff", "admin"]);

  if (
    typeof obj !== "object" ||
    obj === null ||
    !Array.isArray(obj.users)
  ) {
    return false;
  }

  for (const user of obj.users) {
    if (typeof user !== "object" || user === null) {
      return false;
    }

    if (
      typeof user.username !== "string" ||
      typeof user.posts !== "number" ||
      typeof user.verified !== "boolean" ||
      !roles.has(user.role) ||
      !Array.isArray(user.badges)
    ) {
      return false;
    }

    if (
      "supporter" in user &&
      typeof user.supporter !== "boolean"
    ) {
      return false;
    }

    if (!user.badges.every(badge => typeof badge === "string")) {
      return false;
    }
  }

  return true;
}

console.log(
  isValidSchema({
    users: [
      {
        username: "ron",
        posts: 14,
        verified: true,
        role: "creator",
        badges: ["early-adopter"]
      },
      {
        username: "cher",
        posts: 25,
        verified: true,
        role: "moderator",
        supporter: true,
        followers: 20,
        badges: ["helper"]
      }
    ]
  })
);

console.log(isValidSchema({ users: [] }));

console.log(
  isValidSchema({
    users: {
      username: "anne",
      posts: 0,
      verified: false,
      role: "user",
      supporter: false,
      badges: []
    }
  })
);

console.log(
  isValidSchema({
    users: [
      {
        username: "tony",
        posts: 10,
        verified: true,
        role: "creator",
        supporter: true,
        badges: ["liked", 6]
      }
    ]
  })
);

console.log(
  isValidSchema({
    users: [
      {
        username: "ursula",
        posts: 3,
        verified: false,
        role: "user",
        supporter: "false",
        badges: ["comeback"]
      }
    ]
  })
);

console.log(
  isValidSchema({
    users: [
      {
        username: "benny",
        posts: 55,
        verified: true,
        role: "superstar",
        supporter: true,
        badges: ["veteran"]
      }
    ]
  })
);

console.log(
  isValidSchema({
    users: [
      {
        username: "chase",
        posts: 1,
        verified: "yes",
        role: "staff",
        supporter: false,
        badges: ["superstar"]
      }
    ]
  })
);

console.log(
  isValidSchema({
    users: [
      {
        username: "carla",
        posts: "10",
        verified: false,
        role: "user",
        supporter: false,
        badges: ["newbie"]
      }
    ]
  })
);

console.log(
  isValidSchema({
    users: [
      {
        posts: 4,
        verified: false,
        role: "admin",
        supporter: false,
        badges: ["superuser", "veteran"]
      }
    ]
  })
);

console.log(
  isValidSchema({
    users: [
      {
        username: "harold",
        posts: 80,
        verified: true,
        role: "creator",
        supporter: true,
        badges: ["liked", "hero"]
      },
      {
        username: "kim",
        posts: 11,
        verified: false,
        role: "admin",
        supporter: true,
        badges: ["first"]
      },
      {}
    ]
  })
);