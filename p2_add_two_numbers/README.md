# LeetCode #2: Add Two Numbers

## 📖 Условие

Даны два непустых односвязных списка (ListNode), представляющих два неотрицательных числа.  
Цифры хранятся в обратном порядке (младший разряд — в начале списка).  
Каждый узел содержит одну цифру (0–9).  

Нужно сложить эти два числа и вернуть результат в виде связного списка таким же образом.

## 🚀 Решение (O(n))

1. Инициализируем:
   - `dummy = ListNode(0)` — фиктивная голова результирующего списка.
   - `tail = dummy` — указатель на «хвост» результата.
   - `carry = 0` — перенос «десятков».

2. Пока есть цифры в `l1` или `l2` или непустой `carry`:
   ```python
   v1 = l1.val if l1 else 0
   v2 = l2.val if l2 else 0
   carry, digit = divmod(v1 + v2 + carry, 10)
   tail.next = ListNode(digit)
   tail = tail.next
   l1 = l1.next if l1 else None
   l2 = l2.next if l2 else None
   ```

3. Возвращаем `dummy.next` — голову готового списка.

## 🔢 Пример

```
l1 = [2,4,3]   # 342
l2 = [5,6,4]   # 465
результат → [7,0,8]  # 807
```

## 📊 Сложность

- Время: O(max(n, m))  
- Память: O(max(n, m))
