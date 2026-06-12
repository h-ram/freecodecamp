function analyzeIdeas(ideas) {
  return ideas
    .slice()
    .sort((a, b) => {
      const expectedA = ((a[1] + 4 * a[2] + a[3]) / 6) * a[0].length;
      const expectedB = ((b[1] + 4 * b[2] + b[3]) / 6) * b[0].length;
      return expectedA - expectedB;
    })
    .map(([name]) => name);
}

console.log(
  analyzeIdeas([
    ["Add logging", 2, 5, 15],
    ["SEO optimization", 4, 8, 20],
    ["Fix bug", 1, 3, 5],
  ]),
);

console.log(
  analyzeIdeas([
    ["Dark mode", 1, 3, 8],
    ["Real-time collaboration feature", 6, 12, 20],
    ["Add tooltip", 1, 2, 4],
  ]),
);

console.log(
  analyzeIdeas([
    ["Update user profile page", 3, 7, 14],
    ["Add pagination", 2, 5, 10],
    ["Add tags", 2, 3, 6],
    ["Fix login bug", 1, 4, 8],
  ]),
);

console.log(
  analyzeIdeas([
    ["Migrate database", 14, 25, 40],
    ["Add chat assistant", 8, 15, 24],
    ["Redesign onboarding flow", 3, 7, 13],
    ["Add language support", 6, 11, 18],
  ]),
);

console.log(
  analyzeIdeas([
    ["Add email notifications", 3, 7, 10],
    ["Migrate deployment flow", 6, 10, 16],
    ["Add push notifications", 2, 6, 10],
    ["Optimize continuous integration", 5, 8, 15],
    ["Analyze user patterns", 5, 10, 18],
    ["Create onboarding curriculum", 6, 15, 25],
  ]),
);
