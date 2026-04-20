const statusEl = document.getElementById("status");
const listEl = document.getElementById("courseList");
const findResultEl = document.getElementById("findResult");

const setStatus = (message, isError = false) => {
  statusEl.textContent = message;
  statusEl.style.color = isError ? "#a23b3b" : "#5b5248";
};

const request = async (path, options = {}) => {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(errorText || `Ошибка запроса: ${response.status}`);
  }

  return response.json();
};

const renderCourses = (courses = []) => {
  if (!courses.length) {
    listEl.innerHTML = "<div class='list__item'>Пока нет курсов.</div>";
    return;
  }

  listEl.innerHTML = courses
    .map(
      (course) => `
        <div class="list__item">
          <div class="list__name">${course.name}</div>
          <div class="list__meta">ID: ${course.id} · Уроков: ${course.qty}</div>
        </div>
      `
    )
    .join("");
};

const loadCourses = async () => {
  try {
    const courses = await request("/courses");
    renderCourses(courses);
    setStatus(`Загружено курсов: ${courses.length}`);
  } catch (error) {
    setStatus(`Не удалось получить список: ${error.message}`, true);
  }
};

const healthCheck = async () => {
  try {
    const result = await request("/health");
    setStatus(`API ответ: ${result.status}`);
  } catch (error) {
    setStatus(`Health check не прошел: ${error.message}`, true);
  }
};

document.getElementById("refreshBtn").addEventListener("click", loadCourses);
document.getElementById("healthBtn").addEventListener("click", healthCheck);

document.getElementById("createForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const payload = {
    id: Number(form.id.value),
    name: form.name.value.trim(),
    qty: Number(form.qty.value),
  };

  try {
    const result = await request("/courses", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    setStatus(result.message || "Курс создан");
    form.reset();
    loadCourses();
  } catch (error) {
    setStatus(`Ошибка создания: ${error.message}`, true);
  }
});

document.getElementById("findForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const id = Number(form.id.value);

  try {
    const result = await request(`/courses/${id}`, {
      method: "POST",
      body: JSON.stringify({ id }),
    });
    if (result?.message) {
      throw new Error(result.message);
    }
    findResultEl.textContent = JSON.stringify(result, null, 2);
    setStatus(`Курс ${id} найден`);
  } catch (error) {
    findResultEl.textContent = "—";
    setStatus(`Ошибка поиска: ${error.message}`, true);
  }
});

document.getElementById("updateForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const id = Number(form.id.value);
  const name = form.name.value.trim();
  const qty = form.qty.value;

  const payload = { id };
  if (name) payload.name = name;
  if (qty !== "") payload.qty = Number(qty);

  if (Object.keys(payload).length === 1) {
    setStatus("Укажите новое имя или количество уроков.", true);
    return;
  }

  try {
    const result = await request(`/courses/${id}`, {
      method: "PATCH",
      body: JSON.stringify(payload),
    });
    if (result?.message) {
      throw new Error(result.message);
    }
    setStatus(`Курс ${id} обновлен`);
    findResultEl.textContent = JSON.stringify(result, null, 2);
    loadCourses();
  } catch (error) {
    setStatus(`Ошибка обновления: ${error.message}`, true);
  }
});

document.getElementById("deleteForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const id = Number(form.id.value);

  try {
    const result = await request(`/courses/${id}`, {
      method: "DELETE",
      body: JSON.stringify({ id }),
    });
    if (result?.message) {
      throw new Error(result.message);
    }
    setStatus(`Курс ${id} удален`);
    form.reset();
    loadCourses();
  } catch (error) {
    setStatus(`Ошибка удаления: ${error.message}`, true);
  }
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll("[data-reveal]").forEach((card) => observer.observe(card));

loadCourses();
