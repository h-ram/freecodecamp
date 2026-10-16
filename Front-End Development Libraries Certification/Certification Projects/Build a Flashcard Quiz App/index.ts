interface FlashCard {
  questionText: string;
  questionAnswer: string;
}

class InvalidUserInputError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "InvalidUserInputError";
    Object.setPrototypeOf(this, InvalidUserInputError.prototype);
  }
}

const currentCards: FlashCard[] = [
  {
    questionText: "Which keyword declares a variable that cannot be reassigned?",
    questionAnswer: "const",
  },
  {
    questionText: "What TypeScript feature describes the shape of an object?",
    questionAnswer: "An interface (or a type alias)",
  },
  {
    questionText: "What does the `never` type represent?",
    questionAnswer: "A value that can never occur, such as a function that always throws.",
  },
];

// Start on the newest card so "previous" always means the card before it.
let currentIndex: number = currentCards.length - 1;

// Elements are looked up inside initializeApp, once the DOM exists.
let flashcard: HTMLElement;
let frontText: HTMLElement;
let backText: HTMLElement;
let counter: HTMLElement;
let prevBtn: HTMLButtonElement;
let nextBtn: HTMLButtonElement;
let deleteBtn: HTMLButtonElement;
let entryForm: HTMLFormElement;
let frontInput: HTMLTextAreaElement;
let backInput: HTMLTextAreaElement;
let formMessage: HTMLElement;

const getElement = (id: string): HTMLElement => {
  const el = document.getElementById(id);
  if (!el) throw new Error(`Element not found: ${id}`);
  return el;
};

const renderCard = (): void => {
  flashcard.classList.remove("flipped");

  if (currentCards.length === 0) {
    frontText.textContent = "No cards left. Add one below!";
    backText.textContent = "Use the form to write a new question and answer.";
    counter.textContent = "0 / 0";
  } else {
    const card = currentCards[currentIndex];
    frontText.textContent = card.questionText;
    backText.textContent = card.questionAnswer;
    counter.textContent = `${currentIndex + 1} / ${currentCards.length}`;
  }

  const empty = currentCards.length === 0;
  prevBtn.disabled = empty || currentIndex === 0;
  nextBtn.disabled = empty || currentIndex === currentCards.length - 1;
  deleteBtn.disabled = empty;
};

const flipCard = (): void => {
  flashcard.classList.toggle("flipped");
};

const deleteCurrentCard = (): void => {
  if (currentCards.length === 0) return;

  currentCards.splice(currentIndex, 1);
  // Show the previous card (or the first one if the first card was deleted).
  currentIndex = Math.max(0, currentIndex - 1);
  renderCard();
};

const handleSubmit = (e: Event): void => {
  e.preventDefault();

  const questionText = frontInput.value.trim();
  const questionAnswer = backInput.value.trim();

  if (!questionText || !questionAnswer) {
    const message = "Both the question and the answer are required.";
    formMessage.textContent = message;
    throw new InvalidUserInputError(message);
  }

  currentCards.push({ questionText, questionAnswer });
  currentIndex = currentCards.length - 1;
  formMessage.textContent = "";
  entryForm.reset();
  renderCard();
};

const initializeApp = (): void => {
  flashcard = getElement("flashcard");
  frontText = getElement("card-front-text");
  backText = getElement("card-back-text");
  counter = getElement("counter");
  prevBtn = getElement("prev-btn") as HTMLButtonElement;
  nextBtn = getElement("next-btn") as HTMLButtonElement;
  deleteBtn = getElement("delete-btn") as HTMLButtonElement;
  entryForm = getElement("entry-form") as HTMLFormElement;
  frontInput = getElement("front-text") as HTMLTextAreaElement;
  backInput = getElement("back-text") as HTMLTextAreaElement;
  formMessage = getElement("form-message");

  flashcard.addEventListener("click", flipCard);
  flashcard.addEventListener("keydown", (e: KeyboardEvent) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      flipCard();
    }
  });

  prevBtn.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
      renderCard();
    }
  });

  nextBtn.addEventListener("click", () => {
    if (currentIndex < currentCards.length - 1) {
      currentIndex++;
      renderCard();
    }
  });

  deleteBtn.addEventListener("click", deleteCurrentCard);
  entryForm.addEventListener("submit", handleSubmit);

  renderCard();
};

// Works whether the script runs before or after the page has finished loading.
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initializeApp);
} else {
  initializeApp();
}