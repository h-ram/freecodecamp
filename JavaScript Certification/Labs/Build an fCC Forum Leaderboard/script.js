const forumLatest =
  "https://cdn.freecodecamp.org/curriculum/forum-latest/latest.json";
const forumTopicUrl = "https://forum.freecodecamp.org/t/";
const forumCategoryUrl = "https://forum.freecodecamp.org/c/";
const avatarUrl = "https://cdn.freecodecamp.org/curriculum/forum-latest";

const allCategories = {
  299: { category: "Career Advice", className: "career" },
  409: { category: "Project Feedback", className: "feedback" },
  417: { category: "freeCodeCamp Support", className: "support" },
  421: { category: "JavaScript", className: "javascript" },
  423: { category: "HTML - CSS", className: "html-css" },
  424: { category: "Python", className: "python" },
  432: { category: "You Can Do This!", className: "motivation" },
  560: { category: "Back-End Development", className: "backend" },
};

function timeAgo(isoTimestamp) {
  const past = new Date(isoTimestamp).getTime();
  const diff = Date.now() - past;

  const minutes = Math.floor(diff / (1000 * 60));
  if (minutes < 60) return `${minutes}m ago`;

  const hours = Math.floor(diff / (1000 * 60 * 60));
  if (hours < 24) return `${hours}h ago`;

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  return `${days}d ago`;
}

function viewCount(views) {
  if (views >= 1000) {
    return `${Math.floor(views / 1000)}k`;
  }
  return views;
}

function forumCategory(categoryId) {
  const { category = "General", className = "general" } =
    allCategories[categoryId] ?? {};

  return `<a class="category ${className}" href="${forumCategoryUrl}${className}/${categoryId}">${category}</a>`;
}

function avatars(posters, users) {
  return posters
    .map((poster) => {
      const user = users.find((u) => u.id === poster.user_id);
      if (!user) return "";

      let avatar = user.avatar_template.replace("{size}", "30");

      if (!avatar.startsWith("http")) {
        avatar = `${avatarUrl}${avatar}`;
      }

      return `<img src="${avatar}" alt="${user.name}">`;
    })
    .join("");
}

function showLatestPosts(data) {
  const { users, topic_list } = data;
  const { topics } = topic_list;

  const rows = topics
    .map((topic) => {
      const {
        id,
        title,
        views,
        posts_count,
        slug,
        posters,
        category_id,
        bumped_at,
      } = topic;

      return `
      <tr>
        <td>
          <a class="post-title" href="${forumTopicUrl}${slug}/${id}">
            ${title}
          </a>
          ${forumCategory(category_id)}
        </td>
        <td>
          <div class="avatar-container">
            ${avatars(posters, users)}
          </div>
        </td>
        <td>${posts_count - 1}</td>
        <td>${viewCount(views)}</td>
        <td>${timeAgo(bumped_at)}</td>
      </tr>
    `;
    })
    .join("");

  document.querySelector("#posts-container").innerHTML = rows;
}

async function fetchData() {
  try {
    const response = await fetch(forumLatest);
    const data = await response.json();
    showLatestPosts(data);
  } catch (error) {
    console.log(error);
  }
}

fetchData();
