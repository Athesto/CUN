const loading = document.querySelector('#loading');
const quizPanel = document.querySelector('#quiz-panel');
const resultPanel = document.querySelector('#result-panel');
const progressText = document.querySelector('#progress-text');
const scoreText = document.querySelector('#score-text');
const progressBar = document.querySelector('#progress-bar');
const questionText = document.querySelector('#question-text');
const optionsContainer = document.querySelector('#options');
const answerForm = document.querySelector('#answer-form');
const checkButton = document.querySelector('#check-button');
const nextButton = document.querySelector('#next-button');
const feedback = document.querySelector('#feedback');
const feedbackTitle = document.querySelector('#feedback-title');
const explanation = document.querySelector('#explanation');
const source = document.querySelector('#source');
const resultTitle = document.querySelector('#result-title');
const resultText = document.querySelector('#result-text');
const restartButton = document.querySelector('#restart-button');

let questions = [];
let currentIndex = 0;
let score = 0;
let answered = false;

async function loadQuestions() {
  try {
    const response = await fetch('questions.json');
    if (!response.ok) throw new Error(`Error HTTP ${response.status}`);
    questions = await response.json();
    if (!Array.isArray(questions) || questions.length === 0) throw new Error('No hay preguntas disponibles');
    loading.hidden = true;
    quizPanel.hidden = false;
    showQuestion();
  } catch (error) {
    loading.classList.add('error');
    loading.innerHTML = '<strong>No se pudieron cargar las preguntas.</strong><br>Abre esta carpeta desde un servidor local para permitir que fetch() lea questions.json.';
    console.error(error);
  }
}

function showQuestion() {
  const question = questions[currentIndex];
  answered = false;
  progressText.textContent = `Pregunta ${currentIndex + 1} de ${questions.length}`;
  scoreText.textContent = `Aciertos: ${score}`;
  progressBar.style.width = `${((currentIndex + 1) / questions.length) * 100}%`;
  questionText.textContent = question.question;
  optionsContainer.replaceChildren();

  question.options.forEach((option, index) => {
    const label = document.createElement('label');
    label.className = 'option';
    const input = document.createElement('input');
    input.type = 'radio';
    input.name = 'answer';
    input.value = index;
    input.required = true;
    const text = document.createElement('span');
    text.textContent = option;
    label.append(input, text);
    optionsContainer.append(label);
  });

  feedback.hidden = true;
  feedback.className = 'feedback';
  nextButton.hidden = true;
  checkButton.hidden = false;
}

answerForm.addEventListener('submit', (event) => {
  event.preventDefault();
  if (answered) return;

  const selected = answerForm.elements.answer.value;
  if (selected === '') return;

  answered = true;
  const question = questions[currentIndex];
  const isCorrect = Number(selected) === question.correctAnswer;
  if (isCorrect) score += 1;

  feedback.classList.add(isCorrect ? 'correct' : 'incorrect');
  feedbackTitle.textContent = isCorrect ? '¡Correcto!' : 'Respuesta incorrecta';
  explanation.textContent = question.explanation;
  source.textContent = question.source;
  feedback.hidden = false;
  scoreText.textContent = `Aciertos: ${score}`;
  checkButton.hidden = true;
  nextButton.textContent = currentIndex === questions.length - 1 ? 'Ver resultado' : 'Siguiente pregunta';
  nextButton.hidden = false;

  optionsContainer.querySelectorAll('input').forEach((input) => { input.disabled = true; });
});

nextButton.addEventListener('click', () => {
  currentIndex += 1;
  if (currentIndex < questions.length) showQuestion();
  else showResult();
});

function showResult() {
  quizPanel.hidden = true;
  resultPanel.hidden = false;
  const percentage = Math.round((score / questions.length) * 100);
  resultTitle.textContent = `${score} de ${questions.length} correctas`;
  resultText.textContent = percentage === 100
    ? '¡Excelente! Dominas los conceptos principales.'
    : `Obtuviste ${percentage} %. Puedes intentarlo de nuevo para reforzar los temas.`;
}

restartButton.addEventListener('click', () => {
  currentIndex = 0;
  score = 0;
  resultPanel.hidden = true;
  quizPanel.hidden = false;
  showQuestion();
});

loadQuestions();
