# LeetCode Solutions

Repository with algorithmic problem solutions in Python.

[![CI](https://github.com/irefuse3585/leetcode/actions/workflows/ci.yml/badge.svg)](https://github.com/irefuse3585/leetcode/actions)  
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org)

---

## 📖 Description

This repository contains Python solutions for LeetCode algorithmic problems.  
Each problem is organized in its own folder: code, tests, and detailed description.

---

## 📥 Installation and Setup

1. **Clone the repository**  
   ```bash
   git clone git@github.com:irefuse3585/leetcode.git
   cd leetcode
   ```

2. **Create a virtual environment**  
   ```bash
   python3 -m venv .venv
   ```
   If you have multiple Python versions, specify one explicitly, e.g.:  
   ```bash
   python3.10 -m venv .venv
   ```

3. **Activate the environment**  
   - macOS / Linux:  
     ```bash
     source .venv/bin/activate
     ```  
   - Windows (PowerShell):  
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

4. **Install dependencies**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## ✅ Running Tests

```bash
pytest
```

---

## 🚀 Usage Example

```python
from two_sum.two_sum import Solution

nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))  # [0, 1]
```

---

## ➕ How to Add a New Problem

1. Checkout and update `main`:  
   ```bash
   git checkout main && git pull
   ```
2. Create a branch:  
   ```bash
   git checkout -b feat/p{number}_{snake_case}
   ```
3. Add a folder `p{number}_{snake_case}` containing:  
   - `__init__.py`  
   - `{snake_case}.py` (solution)  
   - `test_{snake_case}.py`  
   - `README.md`
4. Commit your changes:  
   ```bash
   git add .
   git commit -m "feat(p{number}_{snake_case}): add solution"
   ```
5. Push and open a PR:  
   ```bash
   git push -u origin feat/p{number}_{snake_case}
   ```
   After CI passes and review is approved — merge into `main`, then:  
   ```bash
   git checkout main && git pull
   ```

---

## 🤝 Contributing

Contributions are welcome! Please ensure:

- Code follows **PEP8**.  
- Unit tests are provided.  
- The problem folder structure is respected.

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## ✉️ Contact

If you have questions or suggestions, email **kutgos@gmail.com** or open an issue.
