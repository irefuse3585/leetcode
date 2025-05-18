# LeetCode Solutions

Репозиторий с решениями алгоритмических задач на Python.

[![CI](https://github.com/irefuse3585/leetcode/actions/workflows/ci.yml/badge.svg)](https://github.com/irefuse3585/leetcode/actions)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org)

---

## 📖 Описание

В этом репозитории собраны решения алгоритмических задач LeetCode на Python.  
Каждая задача оформлена в отдельной папке: код, тесты и подробное описание.

---

## 📥 Установка и настройка

1. **Клонируем репозиторий**  
   ```bash
   git clone git@github.com:yourusername/leetcode.git
   cd leetcode
   ```

2. **Создаём виртуальное окружение**  
   ```bash
   python3 -m venv .venv
   ```
   Если установлено несколько версий Python, можно явно указать версию, например:
   ```bash
   python3.10 -m venv .venv
   ```

3. **Активируем окружение**  
   - macOS / Linux:  
     ```bash
     source .venv/bin/activate
     ```  
   - Windows (PowerShell):  
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

4. **Устанавливаем зависимости**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## ✅ Запуск тестов

```bash
pytest
```

---

## 🚀 Пример использования решения

```python
from two_sum.two_sum import Solution

nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))  # [0, 1]
```

---

## ➕ Как добавить новую задачу

1. Создать ветку:
   ```bash
   git checkout -b add-<problem-name>
   ```
2. Добавить папку `<problem-name>/` с файлом решения, тестами и `README.md`.
3. При необходимости обновить `requirements.txt`.
4. `git add . && git commit -m "Add <Problem Name>"`
5. `git push -u origin add-<problem-name>` и открыть Pull Request.

---

## 🤝 Contributing

Буду рад новым задачам и улучшениям! Пожалуйста, соблюдайте:

- Оформляйте код по PEP8.  
- Пишите unit-тесты.  
- Следуйте шаблону папки задачи.

---

## 📜 Лицензия

Этот проект распространяется под условиями **MIT License** — подробности в файле [LICENSE](LICENSE).

---

## ✉️ Контакты

Если есть вопросы или предложения — пишите на your.email@example.com или открывайте issue.
