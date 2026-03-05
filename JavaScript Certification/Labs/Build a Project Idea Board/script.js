const projectStatus = {
  PENDING: { description: "Pending Execution" },
  SUCCESS: { description: "Executed Successfully" },
  FAILURE: { description: "Execution Failed" },
};

class ProjectIdea {
  constructor(title, description) {
    this.title = title;
    this.description = description;
    this.status = projectStatus.PENDING;
  }
  updateProjectStatus(newStatus) {
    this.status = newStatus;
  }
}

class ProjectIdeaBoard {
  constructor(title) {
    this.title = title;
    this.ideas = [];
  }
  pin(projectIdea) {
    this.ideas.push(projectIdea);
  }
  unpin(idea) {
    const index = this.ideas.indexOf(idea);
    if (index !== -1) {
      this.ideas.splice(index, 1);
    }
  }
  count() {
    return this.ideas.length;
  }
  formatToString() {
    let str = `${this.title} has ${this.count()} idea(s)\n`;

    this.ideas.forEach((idea) => {
      str += `${idea.title} (${idea.status.description}) - ${idea.description}\n`;
    });
    return str;
  }
}

const board = new ProjectIdeaBoard("Tech Projects Board");
board.pin(
  new ProjectIdea(
    "Smart Home System",
    "An integrated system to control lighting, temperature, and security devices remotely.",
  ),
);

console.log(board.formatToString());

const emptyBoard = new ProjectIdeaBoard("Empty Board");
console.log(emptyBoard.formatToString());
