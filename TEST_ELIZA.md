# ELIZA Interactive Test

The ELIZA program now works correctly! Try these test inputs:

```bash
python3 latin.py examples/eliza.lat
```

Test interactions:
1. Type `sum tristis` → responds "Cur tristis es?" (Why are you sad?)
2. Type `sum felix` → responds "Gaudeo!" (I rejoice!)
3. Type `mater mea` → responds "Dic mihi de matre tua." (Tell me about your mother.)
4. Type `pater meus` → responds "Quomodo pater tuus te afficit?" (How does your father affect you?)
5. Type `cur hoc?` → responds "Cur putas?" (Why do you think?)
6. Type `volo dormire` → responds "Quid accideret si id haberes?" (What would happen if you had it?)
7. Type `VALE` → exits with "Vale! Cura ut valeas." (Farewell! Take care!)

The program now correctly:
- Loops continuously until VALE is typed
- Checks all keywords on each iteration
- Multiple keywords can match (e.g., "mater et pater")
- FINIS correctly distinguishes between SI blocks and DUM loops using depth tracking
