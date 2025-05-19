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
   git clone git@github.com:irefuse3585/leetcode.git
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

1. Перейти на `main` и обновиться:  
   ```bash
   git checkout main && git pull
   ```
2. Создать ветку:
   ```bash
   git checkout -b feat/p{номер}_{snake_case}
   ```
3. Добавить папку `p{номер}_{snake_case}` с файлами:
   - `__init__.py`
   - `{snake_case}.py` (решение)
   - `test_{snake_case}.py`
   - `README.md`
4. Закоммитить:
   ```bash
   git add . 
   git commit -m "feat(p{номер}_{snake_case}): add solution"
   ```
5. Запушить и открыть PR:
   ```bash
   git push -u origin feat/p{номер}_{snake_case}
   ```
   После зелёного CI и одобрения — **Merge pull request**, затем:
   ```bash
   git checkout main && git pull
   ```

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

Если есть вопросы или предложения — пишите на kutgos@gmail.com или открывайте issue.
